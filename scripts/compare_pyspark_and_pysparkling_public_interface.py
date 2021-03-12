import contextlib
import inspect
from functools import partial
from importlib import import_module
import io
import logging
from pathlib import Path

import pyspark

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()


IGNORE_SUBPACKAGES = ['ml', 'mllib']


pyspark_root = Path(pyspark.__file__).parent
pysparkling_root = Path('../pysparkling')

examples = pyspark_root / 'examples'

files_to_compare = [
    module
    for module in pyspark_root.rglob('*.py')
    if examples not in module.parents
]


files_to_compare = sorted(files_to_compare)


@contextlib.contextmanager
def suppress_std():
    with contextlib.redirect_stdout(io.StringIO()):
        with contextlib.redirect_stderr(io.StringIO()):
            yield


def tell_files_to_be_internalized():
    log.info('Files that should not be exposed:')
    log.info('---')

    pysparkling_files = {
        file.relative_to(pysparkling_root)
        for file in pysparkling_root.rglob('*.py')
        if (
            not file.name.startswith('_')
            and not any(parent.name.startswith('_') for parent in file.parents)
            and not any('tests' in x.name for x in file.parents)
        )
    }

    pyspark_files = {
        file.relative_to(pyspark_root)
        for file in files_to_compare
        if (
            not file.name.startswith('_')
            and not any(parent.name.startswith('_') for parent in file.parents)
        )
    }

    for file in sorted(pysparkling_files - pyspark_files):
        log.info('- %s', file)


def compare_one_symbol(txt: str, pyspark_class, pysparkling_class, attr: inspect.Attribute):
    txt_to_report = f'    - [{txt}] {pyspark_class.__name__}.'
    if txt in ['ADD', 'CORRECT']:
        txt_to_report += attr.name
        if attr.kind == 'data':  # Plain attribute.
            pass
        elif attr.kind == 'property':
            txt_to_report += ' @property'
        else:
            txt_to_report += str(inspect.signature(getattr(pyspark_class, attr.name)))
            if attr.kind == 'static method':
                txt_to_report += ' @staticmethod'
            if attr.kind == 'class method':
                txt_to_report += ' @classmethod'
    elif txt == 'DEL':
        txt_to_report += attr.name
    else:
        raise NotImplementedError

    log.info(txt_to_report)


def compare_symbols(pyspark_symbol, pysparkling_symbol):
    if type(pyspark_symbol) != type(pysparkling_symbol):
        log.warning(f'    - [CHECK] {pyspark_symbol.__name__} is of type "{type(pyspark_symbol)}". Pysparklings one is "{type(pysparkling_symbol)}".')
        return

    if hasattr(pyspark_symbol, '__module__'):
        pass

    if inspect.isclass(pyspark_symbol):
        pyspark_attributes = {x.name: x for x in inspect.classify_class_attrs(pyspark_symbol) if not _is_private(x.name) and x.defining_class not in [object, BaseException]}
        pysparkling_attributes = {x.name: x for x in inspect.classify_class_attrs(pysparkling_symbol) if not _is_private(x.name) and x.defining_class not in [object, BaseException]}

        compare = partial(compare_one_symbol, pyspark_class=pyspark_symbol, pysparkling_class=pysparkling_symbol)

        for x in sorted(set(pyspark_attributes) - set(pysparkling_attributes)):
            compare('ADD', attr=pyspark_attributes[x])

        for x in sorted(set(pysparkling_attributes) - set(pyspark_attributes)):
            compare('DEL', attr=pysparkling_attributes[x])

        for x in sorted(set(pyspark_attributes) & set(pysparkling_attributes)):  # In both. Check signatures
            if (
                pyspark_attributes[x].kind != pysparkling_attributes[x].kind
                or (
                    'method' in pyspark_attributes[x].kind
                    and
                    inspect.signature(getattr(pyspark_symbol, x)) != inspect.signature(getattr(pysparkling_symbol, x))
                )
                or (
                    pyspark_attributes[x].kind == 'data'
                    and getattr(pyspark_symbol, x) != getattr(pysparkling_symbol, x)
                )
                or (
                    pyspark_attributes[x].kind == 'property'
                    and (
                        ((getattr(pyspark_symbol, x).fget is None) ^ (getattr(pysparkling_symbol, x).fget is None))
                        or ((getattr(pyspark_symbol, x).fset is None) ^ (getattr(pysparkling_symbol, x).fset is None))
                        or ((getattr(pyspark_symbol, x).fdel is None) ^ (getattr(pysparkling_symbol, x).fdel is None))
                    )
                )
            ):
                compare('CORRECT', attr=pyspark_attributes[x])

        return

    if inspect.isfunction(pyspark_symbol):
        sig1 = inspect.signature(pyspark_symbol)
        sig2 = inspect.signature(pysparkling_symbol)

        if sig1 != sig2:
            log.info(f'    - [CORRECT] {pyspark_symbol.__name__}{sig1}')

        return

    if inspect.ismodule(pyspark_symbol):
        return

    log.error(f'************ Implement {type(pyspark_symbol)}')


def _is_private(name: str, in_module=None) -> bool:
    if not name.startswith('_') and in_module is None:
        return False

    # Ignore these names (module)
    if name in ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__',]:
        return True

    # Ignore these names (classes)
    if name in ['__dict__', '__doc__', '__module__', '__weakref__', ]:
        return True

    if name.startswith('__') and name.endswith('__'):
        return False

    if in_module is None:
        return True

    attr = getattr(in_module, name)
    if hasattr(attr, '__module__'):
        if not attr.__module__.startswith('pyspark'):
            return True  # Imported?
    elif hasattr(type(attr), '__module__'):
        if not type(attr).__module__.startswith('pyspark'):
            return True  # Imported?

    # So now name is of the pattern '_*', but not '__*__'
    return name.startswith('_')  # Assume it's private


# pylint: disable=too-many-branches
def compare_with_module(pysparkling_path, converted_to_module_name, pyspark_mod):
    pysparkling_module_name = 'pysparkling' + converted_to_module_name[7:]

    # Load the module, suppressing std output
    try:
        with suppress_std():
            pysparkling_mod = import_module(pysparkling_module_name)
    except ImportError:
        log.error("  *--> CANNOT LOAD %s*", pysparkling_module_name.replace('_', r'\_'))
        return

    pyspark_vars = {x for x in vars(pyspark_mod) if not _is_private(x, pyspark_mod)}
    pysparkling_vars = {x for x in vars(pysparkling_mod) if not _is_private(x, pysparkling_mod)}

    try:
        pyspark_all = {x for x in pyspark_mod.__all__ if not _is_private(x, pyspark_mod)}
        pyspark_has_all_set = True
    except AttributeError:
        pyspark_all = pyspark_vars
        pyspark_has_all_set = False

    try:
        pysparkling_all = {x for x in pysparkling_mod.__all__ if not _is_private(x, pysparkling_mod)}
        pysparkling_has_all_set = True
    except AttributeError:
        pysparkling_all = pysparkling_vars
        pysparkling_has_all_set = False

    if pyspark_has_all_set and not pysparkling_has_all_set:
        log.warning(rf"! set this in pysparkling: \_\_all\_\_ = {list(pyspark_all)}")
    elif not pyspark_has_all_set and pysparkling_has_all_set:
        log.warning(r'! _pyspark_ has no \_\_all\_\_ set, remove it from pysparkling')
    # Neither of them has it set. Or both have it set... So all's fine.

    def _give_class_def_txt(a, x):
        attr = getattr(a, x)

        if inspect.isclass(attr):
            return 'class'
        elif inspect.isfunction(attr):
            return 'def'
        elif isinstance(attr, property):
            return '@property'
        elif isinstance(attr, classmethod):
            return '@classmethod'
        elif isinstance(attr, staticmethod):
            return '@staticmethod'
        else:
            return ''

    for x in sorted(pyspark_all - pysparkling_all):  # Missing pysparkling
        log.warning('    - [ADD] %s %s', _give_class_def_txt(pyspark_mod, x), x)

    for x in sorted(pysparkling_all - pyspark_all):  # Is not in the public API of pyspark
        log.warning('    - [DEL] %s %s', _give_class_def_txt(pysparkling_mod, x), x)

    for x in sorted(pyspark_all & pysparkling_all):  # Is in both
        compare_symbols(
            getattr(pyspark_mod, x),
            getattr(pysparkling_mod, x),
        )


def tell_differences_between_modules():
    log.info('REPORT: pyspark vs pysparkling')
    log.info('---')

    for file in files_to_compare:
        if _is_private(file.name):  # Don't compare not public files.
            continue

        if any(parent.name in IGNORE_SUBPACKAGES for parent in file.parents):
            continue

        relative_path = file.relative_to(pyspark_root.parent)

        converted_to_module_name = (
            str(relative_path)[:-3]  # Strip .py
            .replace('\\', '/')      # Windows paths?
            .replace('/', '.')       # --> module name
        )

        log.info('* %s', converted_to_module_name.replace('_', r'\_'))
        try:
            with suppress_std():
                mod = import_module(converted_to_module_name)
        except ImportError:
            log.error("  --> CANNOT IMPORT %s", converted_to_module_name.replace('_', r'\_'))
            continue

        pysparkling_path = pysparkling_root / file.relative_to(pyspark_root)

        compare_with_module(
            pysparkling_path,
            converted_to_module_name,
            mod
        )


if __name__ == '__main__':
    tell_files_to_be_internalized()
    tell_differences_between_modules()
