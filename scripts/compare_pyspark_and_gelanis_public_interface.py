# pylint: disable=logging-fstring-interpolation, too-many-return-statements, too-many-boolean-expressions
import contextlib
from functools import partial
from importlib import import_module
import inspect
import io
import logging
from pathlib import Path

import pyspark

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()


IGNORE_SUBPACKAGES = ['ml', 'mllib']


pyspark_root = Path(pyspark.__file__).parent
gelanis_root = Path('../gelanis')

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

    gelanis_files = {
        file.relative_to(gelanis_root)
        for file in gelanis_root.rglob('*.py')
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

    for file in sorted(gelanis_files - pyspark_files):
        log.info('- %s', file)


def compare_one_symbol(txt: str, pyspark_class, gelanis_class, attr: inspect.Attribute):
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


def compare_symbols(pyspark_symbol, gelanis_symbol):
    if type(pyspark_symbol) is not type(gelanis_symbol):
        log.warning(f'    - [CHECK] {pyspark_symbol.__name__} is of type "{type(pyspark_symbol)}".'
                    f' Pysparklings one is "{type(gelanis_symbol)}".')
        return

    if hasattr(pyspark_symbol, '__module__'):
        pass

    if inspect.isclass(pyspark_symbol):
        pyspark_attributes = {
            x.name: x
            for x in inspect.classify_class_attrs(pyspark_symbol)
            if (
                not _is_private(x.name)
                and x.defining_class not in [object, BaseException]
            )
        }
        gelanis_attributes = {
            x.name: x
            for x in inspect.classify_class_attrs(gelanis_symbol)
            if (
                not _is_private(x.name)
                and x.defining_class not in [object, BaseException]
            )
        }

        compare = partial(compare_one_symbol, pyspark_class=pyspark_symbol, gelanis_class=gelanis_symbol)

        for x in sorted(set(pyspark_attributes) - set(gelanis_attributes)):
            compare('ADD', attr=pyspark_attributes[x])

        for x in sorted(set(gelanis_attributes) - set(pyspark_attributes)):
            compare('DEL', attr=gelanis_attributes[x])

        for x in sorted(set(pyspark_attributes) & set(gelanis_attributes)):  # In both. Check signatures
            a1 = getattr(pyspark_symbol, x, None)
            a2 = getattr(gelanis_symbol, x, None)

            if (
                pyspark_attributes[x].kind != gelanis_attributes[x].kind
                or (
                    'method' in pyspark_attributes[x].kind
                    and inspect.signature(a1) != inspect.signature(a2)
                )
                or (
                    pyspark_attributes[x].kind == 'data'
                    and a1 != a2
                )
                or (
                    pyspark_attributes[x].kind == 'property'
                    and (
                        ((a1.fget is None) ^ (a2.fget is None))
                        or ((a1.fset is None) ^ (a2.fset is None))
                        or ((a1.fdel is None) ^ (a2.fdel is None))
                    )
                )
            ):
                compare('CORRECT', attr=pyspark_attributes[x])

        return

    if inspect.isfunction(pyspark_symbol):
        sig1 = inspect.signature(pyspark_symbol)
        sig2 = inspect.signature(gelanis_symbol)

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
    if name in [
        '__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__',
    ]:
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
def compare_with_module(gelanis_path, converted_to_module_name, pyspark_mod):
    gelanis_module_name = 'gelanis' + converted_to_module_name[7:]

    # Load the module, suppressing std output
    try:
        with suppress_std():
            gelanis_mod = import_module(gelanis_module_name)
    except ImportError:
        log.error("  *--> CANNOT LOAD %s*", gelanis_module_name.replace('_', r'\_'))
        return

    pyspark_vars = {x for x in vars(pyspark_mod) if not _is_private(x, pyspark_mod)}
    gelanis_vars = {x for x in vars(gelanis_mod) if not _is_private(x, gelanis_mod)}

    try:
        pyspark_all = {x for x in pyspark_mod.__all__ if not _is_private(x, pyspark_mod)}
        pyspark_has_all_set = True
    except AttributeError:
        pyspark_all = pyspark_vars
        pyspark_has_all_set = False

    try:
        gelanis_all = {x for x in gelanis_mod.__all__ if not _is_private(x, gelanis_mod)}
        gelanis_has_all_set = True
    except AttributeError:
        gelanis_all = gelanis_vars
        gelanis_has_all_set = False

    if pyspark_has_all_set and not gelanis_has_all_set:
        log.warning(rf"! set this in gelanis: \_\_all\_\_ = {list(pyspark_all)}")
    elif not pyspark_has_all_set and gelanis_has_all_set:
        log.warning(r'! _pyspark_ has no \_\_all\_\_ set, remove it from gelanis')
    # Neither of them has it set. Or both have it set... So all's fine.

    def _give_class_def_txt(a, x):
        attr = getattr(a, x)

        if inspect.isclass(attr):
            return 'class'
        if inspect.isfunction(attr):
            return 'def'
        if isinstance(attr, property):
            return '@property'
        if isinstance(attr, classmethod):
            return '@classmethod'
        if isinstance(attr, staticmethod):
            return '@staticmethod'
        return ''

    for x in sorted(pyspark_all - gelanis_all):  # Missing gelanis
        log.warning('    - [ADD] %s %s', _give_class_def_txt(pyspark_mod, x), x)

    for x in sorted(gelanis_all - pyspark_all):  # Is not in the public API of pyspark
        log.warning('    - [DEL] %s %s', _give_class_def_txt(gelanis_mod, x), x)

    for x in sorted(pyspark_all & gelanis_all):  # Is in both
        compare_symbols(
            getattr(pyspark_mod, x),
            getattr(gelanis_mod, x),
        )


def tell_differences_between_modules():
    log.info('REPORT: pyspark vs gelanis')
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

        gelanis_path = gelanis_root / file.relative_to(pyspark_root)

        compare_with_module(
            gelanis_path,
            converted_to_module_name,
            mod
        )


if __name__ == '__main__':
    tell_files_to_be_internalized()
    tell_differences_between_modules()
