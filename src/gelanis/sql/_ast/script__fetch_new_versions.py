import json
import re
from pathlib import Path

import requests

local_dir = Path(__file__).parent


print("Retrieving all branches.")
all_branches = json.loads(requests.get('https://api.github.com/repos/apache/spark/branches', verify=False).text)
for branch in all_branches:
    match = re.match(r'^branch-(\d\.\d)$', branch['name'])
    if not match:
        continue

    branch_version = match.group(1)
    if branch_version[0] < '2':
        continue  # Before version 2, there is no SqlBase to speak of.

    print(f" - fetching SqlBase.g4 from branch {branch_version}")
    target_file = local_dir / branch_version / 'SqlBase.g4'
    target_file.parent.mkdir(parents=True, exist_ok=True)

    sql_base = (
        f"https://raw.githubusercontent.com/apache/spark/{branch['name']}"
        "/sql/catalyst/src/main/antlr4/org/apache/spark/sql/catalyst/parser/SqlBase.g4"
    )

    target_file.write_bytes(
        requests.get(sql_base, verify=False).content
    )

print("All done")
