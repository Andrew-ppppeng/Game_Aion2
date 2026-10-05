"""Small anonymous GET probe of routes documented in the cited community client.
No credentials, no game access, no pagination crawl, no retry/bypass.
"""
import concurrent.futures
import json
import pathlib
import urllib.parse
from collect_public_evidence import capture, RAW

JOBS = [
 ('api-tw-servers', 'https://tw.ncsoft.com/aion2/api/gameinfo/servers?lang=zh', 'json'),
 ('api-tw-classes', 'https://tw.ncsoft.com/aion2/api/gameinfo/classes?lang=en', 'json'),
 ('api-tw-search-sdk', 'https://tw.ncsoft.com/aion2/api/search/character?keyword=fofo&page=1&size=3', 'json'),
 ('api-tw-search-spec', 'https://tw.ncsoft.com/aion2/api/search/aion2tw/search/v2/character?keyword=fofo&page=1&size=3', 'json'),
 ('api-tw-item', 'https://tw.ncsoft.com/aion2/api/gameconst/item?id=110120001&lang=en', 'json'),
 ('api-tw-catalog', 'https://tw.ncsoft.com/aion2_tw/v2.0/dict/search/item?page=1&size=3', 'json'),
 ('api-global-eu-servers', 'https://aion2.plaync.com/en-us/api/gameinfo/servers?lang=en-US&region=eu', 'json'),
 ('api-global-eu-classes', 'https://aion2.plaync.com/en-us/api/gameinfo/classes?lang=en-US&region=eu', 'json'),
 ('api-global-eu-search', 'https://api-search.plaync.com/aion2global/search/v2/character?keyword=a&page=1&size=3&lang=en-US&region=eu', 'json'),
 ('api-global-eu-item', 'https://aion2.plaync.com/en-us/api/gameconst/item?id=110120001&lang=en-US&region=eu', 'json'),
 ('api-kr-servers', 'https://aion2.plaync.com/api/gameinfo/servers?lang=ko', 'json'),
 ('api-kr-search', 'https://aion2.plaync.com/api/search/character?keyword=a&page=1&size=3', 'json')
]

CORRECTED = [
 ('api-tw-search-corrected', 'https://tw.ncsoft.com/aion2/api/search/character?keyword=fofo&race=2&page=1&size=3', 'json'),
 ('api-global-eu-search-corrected', 'https://api-search.plaync.com/aion2global/search/v2/character?keyword=a&page=1&size=3&localeInfo=en-US&region=eu', 'json'),
 ('api-tw-item-corrected', 'https://tw.ncsoft.com/aion2/api/gameconst/item?id=110120001&enchantLevel=0&lang=en', 'json'),
 ('api-global-eu-item-corrected', 'https://aion2.plaync.com/en-us/api/gameconst/item?id=110120001&enchantLevel=0&lang=en-US&region=eu', 'json'),
 ('api-tw-catalog-localized', 'https://tw.ncsoft.com/aion2_tw/v2.0/dict/search/item?page=1&size=3&locale=zh-TW', 'json')
]

def first_character(data):
    if isinstance(data, dict):
        if 'characterId' in data and 'serverId' in data: return data
        for val in data.values():
            found = first_character(val)
            if found: return found
    elif isinstance(data, list):
        for val in data:
            found = first_character(val)
            if found: return found
    return None

def summary(meta):
    result = {key: meta[key] for key in ('label','status','error','url') if key in meta}
    path = RAW / (meta['label']+'.body')
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
        result['keys'] = list(data)[:20] if isinstance(data, dict) else ['list']
        if isinstance(data, dict):
            result['modules'] = {k: list(v)[:12] if isinstance(v,dict) else 'list:'+str(len(v)) if isinstance(v,list) else v for k,v in data.items()}
        if len(json.dumps(result,ensure_ascii=False)) > 2600: result.pop('modules',None)
    except Exception: pass
    return result

def main():
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for meta in pool.map(capture,CORRECTED):
            results.append(meta)
            print(json.dumps(summary(meta),ensure_ascii=False),flush=True)
    for region, label, origin, lang, shard in [
        ('TW','api-tw-search-corrected','https://tw.ncsoft.com/aion2','en',''),
        ('Global-EU','api-global-eu-search-corrected','https://aion2.plaync.com','en-US','eu')
    ]:
        try: hit = first_character(json.loads((RAW/(label+'.body')).read_text(encoding='utf-8')))
        except Exception: hit = None
        if not hit: continue
        query = {'characterId': urllib.parse.unquote(hit['characterId']), 'serverId':hit['serverId'], 'lang':lang}
        if shard: query['region'] = shard
        for resource in ['info','equipment']:
            meta=capture(('api-'+region.lower()+'-'+resource,origin+'/api/character/'+resource+'?'+urllib.parse.urlencode(query),'json'))
            results.append(meta)
            print(json.dumps(summary(meta),ensure_ascii=False),flush=True)
    (pathlib.Path(__file__).resolve().parent/'api-probe-corrected-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')

if __name__ == '__main__': main()
