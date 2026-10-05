"""Archive published client-reference records; editorial decisions stay manual."""
import gzip
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).parent
soup = BeautifulSoup((root / 'metabot-skills.html').read_text(encoding='utf-8'), 'html.parser')
links = list(dict.fromkeys(a['href'] for a in soup.select('main a[href]') if '/skills/' in a['href']))
(root / 'raw-skills').mkdir(exist_ok=True)

def fetch(href):
    slug = href.rsplit('/', 1)[-1]
    url = 'https://metabot.gg' + href
    response = requests.get(url, timeout=35)
    response.raise_for_status()
    with gzip.open(root / 'raw-skills' / (slug + '.html.gz'), 'wt', encoding='utf-8') as out:
        out.write(response.text)
    main = BeautifulSoup(response.text, 'html.parser').find('main')
    text = main.get_text(' ', strip=True)
    (root / 'raw-skills' / (slug + '.txt')).write_text(text, encoding='utf-8')
    intro = text.split('Read More')[0]
    return {'slug': slug, 'url': url, 'checkedAt': datetime.now(timezone.utc).isoformat(),
            'region': 'Global', 'version': 'Published client extraction, build 0.0.4387.0; not independently unpacked',
            'intro': intro, 'text': text}

records, failures = [], []
with ThreadPoolExecutor(max_workers=6) as pool:
    jobs = {pool.submit(fetch, href): href for href in links}
    for i, job in enumerate(as_completed(jobs), 1):
        try:
            records.append(job.result())
        except Exception as error:
            failures.append({'href': jobs[job], 'error': str(error)})
        if i % 25 == 0:
            print(f'{i}/{len(links)} read, {len(failures)} failed', flush=True)
(root / 'client-skill-records.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
(root / 'client-skill-failures.json').write_text(json.dumps(failures, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Complete: {len(records)} records, {len(failures)} failures', flush=True)
