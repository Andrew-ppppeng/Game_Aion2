"""Read-only anonymous fetches of public AION 2 official materials."""
import concurrent.futures
import datetime
import json
import pathlib
import requests
from bs4 import BeautifulSoup

OUT = pathlib.Path(__file__).resolve().parent
JOBS = [
    ('global-about', 'https://aion2.plaync.com/en-us/about/index', 'Global', 'html'),
    ('global-teaser', 'https://aion2.ncsoft.jp/en/', 'Global', 'html'),
    ('kr-about', 'https://aion2.plaync.com/ko-kr/about/index', 'KR', 'html'),
    ('tw-about', 'https://tw.ncsoft.com/aion2/about/index', 'TW', 'html'),
    ('steam-appdetails', 'https://store.steampowered.com/api/appdetails?appids=3393110&l=english&cc=us', 'Global', 'json'),
    ('steam-news', 'https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3393110&count=100&maxlength=0', 'Global', 'json'),
    ('global-pairing', 'https://api-global-community.plaync.com/aion2_global/board/notice_en/article/6abab930eea53f5d6dbcf939', 'Global', 'json'),
    ('global-transfers', 'https://api-global-community.plaync.com/aion2_global/board/notice_en/article/6abd2d50a279104f7d9d5ee2', 'Global', 'json'),
    ('nc-march-cross-faction', 'https://about.ncsoft.com/en/news/article/aion2_update_260311', 'KR service context; not Global launch evidence', 'html'),
    ('nc-chaotic-abyss', 'https://about.ncsoft.com/en/news/article/aion2_update_260325', 'KR service context; not Global launch evidence', 'html'),
    ('nc-new-regions', 'https://about.ncsoft.com/en/news/article/aion2_update_260706', 'KR service context; not Global launch evidence', 'html'),
]

def capture(job):
    slug, url, region, kind = job
    meta = dict(slug=slug,url=url,region=region,retrievedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        response=requests.get(url,timeout=40,headers={'User-Agent':'Mozilla/5.0'})
        meta.update(status=response.status_code,finalUrl=response.url,contentType=response.headers.get('content-type'))
        response.encoding='utf-8'
        (OUT/(slug+'.'+kind)).write_text(response.text,encoding='utf-8')
        if kind=='html':
            soup=BeautifulSoup(response.text,'html.parser')
            for tag in soup(['script','style','noscript']): tag.decompose()
            text='\n'.join(line.strip() for line in soup.get_text('\n').splitlines() if line.strip())
            (OUT/(slug+'-text.txt')).write_text(text,encoding='utf-8')
        else:
            data=response.json()
            (OUT/(slug+'-pretty.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    except Exception as error:
        meta['error']=str(error)
    (OUT/(slug+'-request.json')).write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    return meta

if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(capture,JOBS))
    (OUT/'fetch-manifest.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(results,ensure_ascii=False,indent=2))
