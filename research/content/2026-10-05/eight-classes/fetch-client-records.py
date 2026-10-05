import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests

sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).parent
planner = json.loads((root / 'planner-data-en.json').read_text(encoding='utf-8'))
out = root / 'client-records'
out.mkdir(exist_ok=True)

def decode(a):
    memo = {}
    def value(i):
        if i < 0: return None
        if i in memo: return memo[i]
        x = a[i]
        if isinstance(x, dict):
            result = {}; memo[i] = result
            result.update({k: value(v) for k, v in x.items()})
        elif isinstance(x, list):
            result = []; memo[i] = result
            result.extend(value(v) for v in x)
        else:
            result = x; memo[i] = result
        return result
    return value(0)

def fetch(skill):
    url = f'https://cdn-hosted.gaming.tools/aion2/data/en/skills/{skill["id"]}.d.json?version=1791128411844'
    response = requests.get(url, timeout=25)
    response.raise_for_status()
    record = {'url': url, 'checkedAt': '2026-10-05', 'region': 'Global',
              'version': 'gaming.tools Global 1.0.21.0, updated 2026-09-30',
              'skill': skill, 'response': decode(response.json())}
    (out / (skill['id'] + '.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
    return record

records, errors = [], []
with ThreadPoolExecutor(max_workers=6) as pool:
    jobs = {pool.submit(fetch, skill): skill for skill in planner['skills']}
    for i, job in enumerate(as_completed(jobs), 1):
        try: records.append(job.result())
        except Exception as error: errors.append({'id': jobs[job]['id'], 'error': str(error)})
        if i % 50 == 0: print(f'{i}/280; {len(errors)} failed', flush=True)
(root / 'client-record-errors.json').write_text(json.dumps(errors, indent=2), encoding='utf-8')
print(f'Complete: {len(records)} skill records; {len(errors)} failed', flush=True)
