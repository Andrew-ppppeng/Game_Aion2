from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from bs4 import BeautifulSoup
import requests, json, sys

sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).resolve().parent
sources = {
    'tw-service-contract': 'https://www.plaync.com/policy/api/view/tw_game_service/aion2_tw',
    'tw-membership-terms': 'https://tw.ncsoft.com/ap/wb/legal/termsOfUse',
    'tw-public-faq-shell': 'https://help.plaync.com/faq/aion2_tw?locale=zh-TW',
    'support-public-script': 'https://help.plaync.com/static/js/main.a35ec0a7.js',
    'tw-login-public-page': 'https://login.plaync.com/nclogin/signin?prelogin_country_code=TW',
}

def collect(item):
    name, url = item
    out = root / (name + '.json')
    if out.exists():
        return {'name': name, 'preserved': True}
    try:
        response = requests.get(url, timeout=35)
        response.encoding = 'utf-8'
        data = {'url': url, 'final_url': response.url, 'retrieved_utc': datetime.now(timezone.utc).isoformat(), 'status': response.status_code, 'region': 'TW' if name != 'support-public-script' else 'public multi-region support app', 'version': 'public page on retrieval', 'content': response.text}
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        if name != 'support-public-script':
            (root / (name + '-text.txt')).write_text(BeautifulSoup(response.text, 'html.parser').get_text('\n', strip=True), encoding='utf-8')
        return {'name': name, 'status': response.status_code, 'length': len(response.content), 'final_url': response.url}
    except requests.RequestException as e:
        data = {'url': url, 'retrieved_utc': datetime.now(timezone.utc).isoformat(), 'error': str(e)}
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        return {'name': name, 'error': str(e)}

with ThreadPoolExecutor(max_workers=5) as pool:
    for result in pool.map(collect, sources.items()):
        print(json.dumps(result, ensure_ascii=False))
