import json
import os
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

import requests

local_dir = Path(__file__).parent
antlr_jar_path = max(local_dir.glob('antlr-*.jar'))


print("Retrieving all branches.")
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

    print(f" - fetching SqlBase.g4 from branch {branch_version}")
    sql_base = (
        f"https://raw.githubusercontent.com/apache/spark/{branch['name']}"
        "/sql/catalyst/src/main/antlr4/org/apache/spark/sql/catalyst/parser/SqlBase.g4"
    )

    target_file.write_bytes(
        requests.get(sql_base, verify=False).content
    )


print("Generating Python code from SqlBase:")
original_dir = Path.cwd()
for file in local_dir.rglob('SqlBase.g4'):
    print(f'- {file}')

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

os.chdir(original_dir)


print("All done")
