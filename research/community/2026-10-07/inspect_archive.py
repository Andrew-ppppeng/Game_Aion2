from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

ROOT = Path(__file__).resolve().parent
discovered = []
for file in sorted((ROOT / 'raw').glob('*.html')):
    if file.stem.startswith('inven'):
        soup = BeautifulSoup(file.read_bytes(), 'html.parser')
        rows = soup.select('tr')
        links = []
        for row in rows:
            a = row.select_one('a.subject-link')
            if not a: continue
            item = {'platform': 'Inven', 'region': 'KR unless explicitly Global', 'title': a.get_text(' ', strip=True), 'url': a.get('href'), 'listing_text': row.get_text(' ', strip=True), 'local_file': str(file.relative_to(ROOT)).replace('\\', '/')}
            links.append(item)
        discovered.extend(links)
        print(file.name, len(links))
        if links: print(json.dumps([links[5], links[-1]], ensure_ascii=False))
        body = soup.select_one('#powerbbsContent')
        if body:
            date = soup.select_one('.articleDate')
            print('DATE', date.get_text(' ', strip=True) if date else '')
            print('BODY', body.get_text('\n', strip=True)[:10000])
            replies = soup.select('.comment-content')
            print('REPLIES', '\n'.join(c.get_text(' ', strip=True) for c in replies)[:4000])
    elif file.stem.startswith('bahamut-aion2'):
        soup = BeautifulSoup(file.read_bytes(), 'html.parser')
        links = []
        for a in soup.select('.b-list__main__title'):
            row = a.find_parent('tr')
            item = {'platform': 'Bahamut', 'region': 'TW', 'title': a.get_text(' ', strip=True), 'url': urljoin('https://forum.gamer.com.tw/', a.get('href', '')), 'listing_text': row.get_text(' ', strip=True) if row else '', 'local_file': str(file.relative_to(ROOT)).replace('\\', '/')}
            links.append(item)
        discovered.extend(links)
        print(file.name, len(links))
        for item in links: print(json.dumps(item, ensure_ascii=False))

by_url = {row['url']:row for row in discovered}
(ROOT / 'discovered-forum-threads.json').write_text(json.dumps(list(by_url.values()), ensure_ascii=False, indent=2), encoding='utf-8')
