"""Read-only, bounded public research capture; preserves response bodies and provenance."""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent
RAW = ROOT / 'raw'
RAW.mkdir(exist_ok=True)
sys.stdout.reconfigure(encoding='utf-8')

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.hidden += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.hidden = max(0, self.hidden - 1)
    def handle_data(self, data):
        if not self.hidden and data.strip(): self.parts.append(data.strip())

def capture(job):
    label, url, kind = job
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    meta = dict(label=label, url=url, kind=kind, retrieved_at_utc=stamp)
    target = RAW / label
    if target.with_suffix('.meta.json').exists():
        return json.loads(target.with_suffix('.meta.json').read_text(encoding='utf-8'))
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'AION2-Website-Research/1.0', 'Accept': '*/*'})
        with urllib.request.urlopen(req, timeout=18) as res:
            body = res.read(8_000_000)
            meta.update(status=res.status, final_url=res.url, content_type=res.headers.get('Content-Type'), bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
        target.with_suffix('.body').write_bytes(body)
        decoded = body.decode('utf-8', errors='replace')
        if kind == 'rdap':
            data = json.loads(decoded)
            meta['events'] = data.get('events', [])
            meta['domain'] = data.get('ldhName')
        elif kind == 'wayback':
            meta['archive_result'] = json.loads(decoded)
        elif kind == 'html':
            parser = TextParser()
            parser.feed(decoded)
            target.with_suffix('.txt').write_text('\n'.join(parser.parts), encoding='utf-8')
            title = re.search(r'<title[^>]*>(.*?)</title>', decoded, re.S | re.I)
            meta['title'] = title.group(1) if title else None
        elif kind == 'json':
            data = json.loads(decoded)
            meta['top_keys'] = list(data)[:20] if isinstance(data, dict) else ['list']
    except urllib.error.HTTPError as err:
        meta.update(status=err.code, error=str(err))
        target.with_suffix('.body').write_bytes(err.read(100_000))
    except Exception as err:
        meta['error'] = str(err)
    target.with_suffix('.meta.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    return meta

DOMAINS = ['questlog.gg', 'shugo.gg', 'aion2hub.com', 'aion2hub.me', 'aion2.app', 'aion2atlas.com', 'aion2.tools', 'dbaion2.online', 'gamers4.life', 'aion2timers.com', 'aion2gg.com', 'elysion.quest', 'atool.kr']

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'catalog'
    jobs = []
    if mode == 'catalog':
        for domain in DOMAINS:
            slug = domain.replace('.', '-')
            home = 'https://' + domain + ('/aion-2/en' if domain == 'questlog.gg' else '/aion-2/database/en/' if domain == 'gamers4.life' else '/')
            jobs.extend([(slug+'-home', home, 'html'), (slug+'-rdap', 'https://rdap.org/domain/'+domain, 'rdap')])
    elif mode == 'traffic':
        for domain in DOMAINS:
            jobs.append((domain.replace('.', '-')+'-semrush', 'https://www.semrush.com/website/'+domain+'/overview/', 'html'))
    elif mode == 'history':
        for domain in DOMAINS:
            jobs.append((domain.replace('.', '-')+'-wayback', 'https://web.archive.org/cdx/search/cdx?url='+domain+'/*&output=json&filter=statuscode:200&filter=mimetype:text/html&collapse=timestamp:4&limit=1&filter=!warc/revisit', 'wayback'))
    elif mode == 'extra':
        filename = sys.argv[2] if len(sys.argv) > 2 else 'extra_jobs.json'
        jobs = json.loads((ROOT/filename).read_text(encoding='utf-8'))
    else: raise ValueError(mode)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4 if mode != 'traffic' else 2) as pool:
        for meta in pool.map(capture, jobs):
            print(json.dumps({k:v for k,v in meta.items() if k not in ('sha256','content_type','retrieved_at_utc','bytes','final_url')}, ensure_ascii=False), flush=True)

if __name__ == '__main__': main()
