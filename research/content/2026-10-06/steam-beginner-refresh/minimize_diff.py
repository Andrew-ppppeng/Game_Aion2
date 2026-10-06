import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
before = Path(__file__).parent / 'before/keywords.json'
current_path = ROOT / 'keywords.json'
old = before.read_text(encoding='utf-8')
current = json.loads(current_path.read_text(encoding='utf-8'))
prior = json.loads(old)
for category in current['categories']:
    earlier = next(c for c in prior['categories'] if c['category'] == category['category'])
    if category['keywords'] != earlier['keywords']:
        original_array = json.dumps(earlier['keywords'], ensure_ascii=False)
        replacement_array = json.dumps(category['keywords'], ensure_ascii=False)
        if original_array not in old:
            raise ValueError('Unexpected keyword formatting; leave the file unchanged')
        old = old.replace(original_array, replacement_array, 1)
if json.loads(old) != current:
    raise ValueError('Formatting cleanup would change keyword values')
current_path.write_text(old, encoding='utf-8', newline='\n')
# The font update helper fetched the identical license with one trailing space.
# Restore its previous bytes; the font subset itself remains updated.
license_path = ROOT / 'public/fonts/OFL-NotoSansJP.txt'
original_license = subprocess.check_output(['git', 'show', 'HEAD:public/fonts/OFL-NotoSansJP.txt'], cwd=ROOT)
if license_path.read_text(encoding='utf-8').split() == original_license.decode('utf-8').split():
    license_path.write_bytes(original_license)
