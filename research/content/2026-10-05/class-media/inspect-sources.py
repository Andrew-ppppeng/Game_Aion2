import json
import re
from pathlib import Path
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor

root = Path(__file__).parent
urls = {
    'about': 'https://aion2.plaync.com/en-us/about/index',
    'guide-en': 'https://aion2.plaync.com/en-us/guidebook/view?title=Skills',
    'guide-kr': 'https://aion2.plaync.com/ko-kr/guidebook/view?title=%EC%8A%A4%ED%82%AC',
    'orbynia': 'https://orbynia.fr/en/aion-2/news/classes-video',
}

def fetch(entry):
    key, url = entry
    try:
        response = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=35)
        raw = response.read()
        (root / f'{key}.html').write_bytes(raw)
        text = raw.decode('utf-8', errors='replace')
        scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)', text)
        media = re.findall(r'(?:https?[^\s"<>]+(?:webp|png|jpg|mp4)[^\s"<>]*|(?:src|href)=["\'][^"\']*(?:youtube|guidebook|about|skill)[^"\']*)', text)
        return {'key': key, 'url': url, 'status': response.status, 'bytes': len(raw), 'scripts': scripts, 'media': list(dict.fromkeys(media))[:50]}
    except Exception as error:
        return {'key': key, 'url': url, 'error': str(error)}

results = list(ThreadPoolExecutor(max_workers=4).map(fetch, urls.items()))
(root / 'fetch-log.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
print(json.dumps(results, indent=2))
about = json.loads((root.parent / 'eight-classes/official-about.json').read_text(encoding='utf-8'))
print('ABOUT KEYS', list(about))
for key, value in about.items():
    if key not in ('jsonData', 'json'):
        print(key, str(value)[:5000])
skills = json.loads(Path('src/content/class-skills.json').read_text(encoding='utf-8'))
first = str(skills['templar'][0]['id'])
record = json.loads((root.parent / f'eight-classes/client-records/{first}.json').read_text(encoding='utf-8'))
print('SKILL RECORD', str(record)[:5000])
