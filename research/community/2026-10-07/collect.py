"""Read-only public community archive. No cookies, credentials or account tokens."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib, json, re, sys
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
RAW = ROOT / 'raw'
RAW.mkdir(exist_ok=True)

def fetch(entry):
    name, url = entry
    stamp = datetime.now(timezone.utc).isoformat()
    record = {'name': name, 'url': url, 'retrieved_at_utc': stamp}
    try:
        r = requests.get(url, timeout=25, headers={'User-Agent': 'AION2CommunityResearch/1.0 (read-only public discussion archive)', 'Accept-Language': 'en-US,en;q=0.8'})
        record.update(status=r.status_code, final_url=r.url, content_type=r.headers.get('Content-Type'), bytes=len(r.content), sha256=hashlib.sha256(r.content).hexdigest())
        ext = '.json' if 'json' in r.headers.get('Content-Type', '') else '.html'
        target = RAW / (name + ext)
        if target.exists():
            target = RAW / (name + '-' + datetime.now(timezone.utc).strftime('%H%M%S') + ext)
        target.write_bytes(r.content)
        record['file'] = str(target.relative_to(ROOT)).replace('\\', '/')
        if ext == '.html':
            soup = BeautifulSoup(r.content, 'html.parser')
            for tag in soup(['script', 'style', 'nav', 'footer']): tag.decompose()
            text = soup.get_text('\n', strip=True)
            target.with_suffix('.txt').write_text(text, encoding='utf-8')
            record['title'] = soup.title.get_text(strip=True) if soup.title else None
            if 'steamcommunity.com' in url:
                links = []
                for a in soup.select('a.forum_topic_overlay'):
                    parent = a.parent
                    links.append({'url': a.get('href'), 'text': parent.get_text(' ', strip=True)})
                record['threads'] = links
        elif 'reddit' in url and r.status_code == 200:
            data = r.json()
            record['posts'] = [{k: c['data'].get(k) for k in ['id', 'title', 'created_utc', 'score', 'num_comments', 'permalink', 'selftext']} for c in data.get('data', {}).get('children', [])]
    except Exception as e:
        record['error'] = str(e)
    return record

if __name__ == '__main__':
    entries = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8-sig'))
    with ThreadPoolExecutor(max_workers=5) as pool: records = list(pool.map(fetch, entries))
    logfile = ROOT / ('fetch-' + datetime.now(timezone.utc).strftime('%H%M%S') + '.json')
    logfile.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
    for record in records:
        brief = {k:v for k,v in record.items() if k not in ['posts', 'threads']}
        print(json.dumps(brief, ensure_ascii=False))
        for t in record.get('threads', []): print(json.dumps(t, ensure_ascii=False))
        for p in record.get('posts', [])[:40]: print(json.dumps({k:v for k,v in p.items() if k != 'selftext'}, ensure_ascii=False))
