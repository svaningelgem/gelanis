import json
import logging
import os
import re
import subprocess
import warnings
from collections import namedtuple
from datetime import datetime, timedelta
from pathlib import Path

import requests
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter(action='ignore', category=InsecureRequestWarning)

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] (%(name)s) %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

local_dir = Path(__file__).parent
antlr_jar_path = max(local_dir.glob('antlr-*.jar'))


logger.info("Retrieving all branches.")
all_branches = json.loads(requests.get('https://api.github.com/repos/apache/spark/branches', verify=False).text)
for branch in all_branches:
    match = re.match(r'^branch-(\d\.\d)$', branch['name'])
    if not match:
        continue

    branch_version = match.group(1)
    if branch_version[0] < '2':
        continue  # Before version 2, there is no SqlBase to speak of.

    target_file = local_dir / branch_version / 'SqlBase.g4'
    target_file.parent.mkdir(parents=True, exist_ok=True)
    if target_file.exists() and datetime.fromtimestamp(target_file.stat().st_mtime) > datetime.today() - timedelta(days=31):
        continue

    logger.info(f" - fetching SqlBase.g4 from branch {branch_version}")
    sql_base = (
        f"https://raw.githubusercontent.com/apache/spark/{branch['name']}"
        "/sql/catalyst/src/main/antlr4/org/apache/spark/sql/catalyst/parser/SqlBase.g4"
    )

    target_file.write_bytes(
        requests.get(sql_base, verify=False).content
    )


def _convert_java_docstring_into_python(txt: str) -> str:
    def convert_one_string(t):
        everything = t.group(0)
        in_between = t.group(1)
        removed_stars = []

        for line in in_between.split('\n'):
            line = line.lstrip()
            if line.strip() == '*':  # For a line with nothing else on it.
                removed_stars.append('')
            else:
                removed_stars.append(line.replace('* ', '', 1))

        removed_stars = ('\n'.join(removed_stars)).strip()
        return '\n"""\n' + removed_stars + '\n"""\n'

    return re.sub(r'\s*/\*\*(.*?)\*/\s*', convert_one_string, txt, flags=re.MULTILINE|re.DOTALL)


def _convert_functions(members):
    Function2Convert = namedtuple('Function2Convert', 'name original changed')
    known_methods = [
        Function2Convert(name='isValidDecimal', original='''{
    int nextChar = _input.LA(1);
    if (nextChar >= 'A' && nextChar <= 'Z' || nextChar >= '0' && nextChar <= '9' ||
      nextChar == '_') {
      return false;
    } else {
      return true;
    }
  }''', changed='''
    nextChar = self._input.LA(1)
    return not ('A' <= nextChar <= 'Z' or '0' <= nextChar <= '9' or nextChar == '_')
'''),
        Function2Convert(name='isHint', original='''{
    int nextChar = _input.LA(1);
    if (nextChar == '+') {
      return true;
    } else {
      return false;
    }
  }''', changed='''
    nextChar = self._input.LA(1);
    return nextChar == '+'
''')
    ]

    all_methods = re.findall(r'(?P<function_def>public.*?\s*(?P<function_name>\w+)\s*\(\))', members)
    for function_def, function_name in all_methods:
        for known in known_methods:
            if known.name == function_name:
                original_pos = members.find(known.original)
                if original_pos == -1:
                    raise ValueError(f"I know a method '{function_name}', but it is not the same!")
                members = members.replace(known.original, known.changed)
                # TODO: change definition header (public boolean ...)
                members = members.replace(function_def, f'def {function_name}(self):')
                break
        else:
            raise ValueError(f"I don't know '{function_name}' yet? Please add this here.")

    return members


logger.info("Generating Python code from SqlBase:")
original_dir = Path.cwd()


def _convert_booleans(members):
    # public boolean legacy_setops_precedence_enbled = false;
    members = re.sub(r'public boolean (\w+) = false;', r'\1 = False', members)
    members = re.sub(r'public boolean (\w+) = true;', r'\1 = True', members)

    return members


def _convert_members(whole_file, start, stop='\n}\n'):
    start_pos = whole_file.index(start)
    stop_pos = whole_file.index(stop, start_pos) + len(stop)

    members_original = whole_file[start_pos:stop_pos]
    members_docstring_adjusted = _convert_java_docstring_into_python(members_original)
    members_functions_adjusted = _convert_functions(members_docstring_adjusted)
    members_booleans_adjusted = _convert_booleans(members_functions_adjusted)

    return whole_file.replace(members_original, members_booleans_adjusted)


def _replace_python_keywords(txt: str) -> str:
    return re.sub(r'\b(from|str|input|len|complex)\b', r'\1_', txt)


def _replace_invalid_sequences(txt: str) -> str:
    txt = txt.replace("'\\\"'", "'\"'") # '\"' -> '"'
    txt = txt.replace('{!', '{not self.')
    txt = re.sub(r'{(\w+)', r'{self.\1', txt)
    txt = txt.replace('{self.not self.', '{not self.')
    txt = txt.replace('{not self.not self.', '{self.')
    return txt


for file in local_dir.rglob('SqlBase.g4'):
    logger.info(f'- {file}')

    whole_file = file.read_text(encoding='utf8')

    logger.debug('Converting @members into Python code')
    try:
        whole_file = _convert_members(whole_file, '@members {')
    except ValueError:
        whole_file = _convert_members(whole_file, '@parser::members {')
        whole_file = _convert_members(whole_file, '@lexer::members {')

    logger.debug("Fixing some warnings in the g4 file")
    whole_file = _replace_python_keywords(whole_file)
    whole_file = _replace_invalid_sequences(whole_file)
    file.write_text(whole_file, encoding='utf8')

    logger.debug("Converting into python files")
    os.chdir(file.parent)
    subprocess.call([
        'java',
        '-Xmx500M',
        '-cp',
        str(antlr_jar_path)+os.path.pathsep+'$CLASSPATH',
        'org.antlr.v4.Tool',
        '-Dlanguage=Python3',
        'SqlBase.g4',
    ])

    logger.debug("Re-formatting the resulting files.")
    subprocess.call(['black', str(file.parent) + '/*.py'])


os.chdir(original_dir)


logger.info("All done")
