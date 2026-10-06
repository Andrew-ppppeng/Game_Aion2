import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
for locale in ['en', 'ja', 'es', 'de']:
    path = ROOT / f'src/messages/{locale}.json'
    record = json.loads(path.read_text(encoding='utf-8'))
    record['home']['aboutGame']['stats'][1]['value'] = 'Windows PC · Steam'
    record['metadata']['keywords'] = record['metadata']['keywords'].replace('Global, ', '')
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
