"""Keep review dates scoped to changed articles; attach new official evidence."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[4]
BEFORE = Path(__file__).parent / 'before'
restored = []
changed = []
for path in (ROOT / 'src/content/article-data').glob('*.json'):
    original = BEFORE / 'src/content/article-data' / path.name
    if not original.exists() or path.stem == 'global-changes':
        continue
    touched = False
    for locale in ['en', 'ja', 'es', 'de']:
        for suffix in ['.mdx', '.json']:
            current = ROOT / 'src/content' / locale / (path.stem + suffix)
            old = BEFORE / 'src/content' / locale / (path.stem + suffix)
            if not current.exists() or not old.exists():
                touched = True
                continue
            a, b = current.read_text(encoding='utf-8'), old.read_text(encoding='utf-8')
            if (json.loads(a) != json.loads(b)) if suffix == '.json' else (a.strip() != b.strip()):
                touched = True
    record = json.loads(path.read_text(encoding='utf-8'))
    if not touched:
        prior = json.loads(original.read_text(encoding='utf-8'))
        record['checkedAt'], record['revision'] = prior['checkedAt'], prior['revision']
        restored.append(path.stem)
    else:
        changed.append(path.stem)
    if not touched and record == prior:
        path.write_bytes(original.read_bytes())
    else:
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')

launch = {'id': 'steam-public-launch-20261005', 'title': 'Launch Into AION 2 Now!', 'url': 'https://steamcommunity.com/games/3393110/announcements/detail/712288224875119583', 'kind': 'official', 'region': 'Global', 'publishedAt': '2026-10-05', 'version': 'Read through official Steam news API on 2026-10-06; public launch October 5 at 13:00 UTC.'}
update = {'id': 'steam-launch-maintenance-20261005', 'title': 'Launch maintenance and update', 'url': 'https://steamcommunity.com/games/3393110/announcements/detail/689769594581155933', 'kind': 'official', 'region': 'Global', 'publishedAt': '2026-10-04', 'version': 'Official Steam snapshot captured 2026-10-06; October 5 maintenance 05:00–13:00 UTC and announced Journal Duty access fix; not a verification of individual account runtime behavior.'}
for slug in ['guide', 'steam', 'download', 'server', 'code', 'monetization', 'maintenance']:
    path = ROOT / f'src/content/article-data/{slug}.json'
    record = json.loads(path.read_text(encoding='utf-8'))
    for source in [launch] + ([update] if slug == 'maintenance' else []):
        if not any(s['id'] == source['id'] for s in record['sources']):
            record['sources'].append(source)
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(json.dumps({'changedArticles': changed, 'originalReviewDatesRetained': restored}, ensure_ascii=False, indent=2))
