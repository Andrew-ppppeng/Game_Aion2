"""Validate saved provenance and create readable copies of web-tool logs."""
from pathlib import Path
from collections import Counter
import hashlib, json

ROOT = Path(__file__).resolve().parent
errors = []
fetches = []
for path in sorted(ROOT.glob('fetch-*.json')):
 for record in json.loads(path.read_text(encoding='utf-8')):
  fetches.append(record)
  if record.get('file'):
   target = ROOT / record['file']
   if not target.exists():
    errors.append('Missing archive: ' + str(target))
   elif hashlib.sha256(target.read_bytes()).hexdigest() != record.get('sha256'):
    errors.append('Hash mismatch: ' + str(target))
for path in sorted((ROOT / 'raw').glob('web-*.json')):
 value = json.loads(path.read_text(encoding='utf-8'))
 text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2)
 target = path.with_suffix('.log.txt')
 if not target.exists(): target.write_text(text + '\n', encoding='utf-8')
evidence = json.loads((ROOT / 'evidence.json').read_text(encoding='utf-8'))
ids = [record['id'] for record in evidence]
if len(ids) != len(set(ids)): errors.append('Duplicate evidence IDs')
for record in evidence:
 if not record['url'].startswith('https://'): errors.append('Invalid URL: ' + record['id'])
 for name in record['raw_files']:
  if not (ROOT / name).is_file(): errors.append('Missing evidence file: ' + name)
manifest = {
 'status': 'passed' if not errors else 'failed',
 'errors': errors,
 'download_attempts': len(fetches),
 'successful_http_200': sum(r.get('status')==200 for r in fetches),
 'non_200_responses': sum('status' in r and r['status']!=200 for r in fetches),
 'transport_failures': sum('status' not in r for r in fetches),
 'success_note': 'Includes an excluded wrong-game board and SPA shells. HTTP 200 is not proof of readable discussion content.',
 'raw_html_files': len(list((ROOT / 'raw').glob('*.html'))),
 'web_log_batches': len(list((ROOT / 'raw').glob('web-*.json'))),
 'evidence_indexed': len(evidence),
 'demand_records': sum(r['theme']!='not-used-in-analysis' for r in evidence),
 'screening_only': sum(r['theme']=='not-used-in-analysis' for r in evidence),
 'demand_platform_counts': dict(Counter(r['platform'] for r in evidence if r['theme']!='not-used-in-analysis')),
 'meaning': 'Counts describe stored records and access attempts, not all community traffic or full comment coverage.'
}
(ROOT / 'archive-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(manifest, ensure_ascii=False))
if errors: raise SystemExit(1)
