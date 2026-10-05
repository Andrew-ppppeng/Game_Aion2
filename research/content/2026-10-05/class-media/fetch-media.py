import json
import re
import sys
from pathlib import Path
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).parent
videos = dict(zip(['gladiator','templar','assassin','ranger','chanter','cleric','sorcerer','spiritmaster'], ['ndri5XpnRK4','Zs6HnL2N5Hk','jUW24SLKK3I','C6INRqEqv3Y','rtOt3KvmYCI','RU-4yiNNnY0','jh1ydFq6FI0','LJq1QGRJSLI']))

def download(url):
    return urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Accept':'application/json', 'Accept-Language':'ko-KR,ko;q=0.9,en;q=0.8', 'Referer':'https://aion2.plaync.com/ko-kr/guidebook/view?title=%EC%8A%A4%ED%82%AC'}),timeout=35).read()

guide_url = 'https://aion2.plaync.com/api/v2/aion2/guide/' + quote('스킬')
raw = download(guide_url)
(root / 'official-skills-guide.json').write_bytes(raw)
try:
    guide = json.loads(raw)
except Exception:
    guide = {'nonJsonResponse':raw.decode('utf-8',errors='replace')[:400]}
html = guide.get('contents', guide.get('content',''))
if not html:
    print('GUIDE KEYS', guide.keys(), str(guide)[:1400])
else:
    (root / 'official-skills-guide.html').write_text(html,encoding='utf-8')
    soup = BeautifulSoup(html,'html.parser')
    (root / 'official-skills-guide.txt').write_text(soup.get_text('\n',strip=True),encoding='utf-8')
    imgs = [{'src':img.get('src'),'alt':img.get('alt')} for img in soup.select('img')]
    (root / 'official-guide-images.json').write_text(json.dumps(imgs,ensure_ascii=False,indent=2),encoding='utf-8')
    print('GUIDE', str(guide)[:1200], 'IMAGES', imgs)

def fetch_video(entry):
    class_id, video_id = entry
    record = {'classId':class_id, 'videoId':video_id,'url':f'https://www.youtube.com/watch?v={video_id}', 'sourceUrl':'https://aion2.plaync.com/en-us/about/index','region':'Global','checkedAt':'2026-10-05','sourceVersion':'Official About the Game JS 1.0.0 class ordering'}
    try:
        url = 'https://www.youtube.com/oembed?' + urlencode({'url':record['url'],'format':'json'})
        record['oembed'] = json.loads(download(url))
        (root / f'{class_id}-oembed.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
        for resolution in ['maxresdefault','hqdefault']:
            try:
                url = f'https://img.youtube.com/vi/{video_id}/{resolution}.jpg'
                blob = download(url)
                (root / f'{class_id}-video.jpg').write_bytes(blob)
                record['thumbnailUrl']=url
                break
            except Exception:
                pass
        try:
            captions = list(YouTubeTranscriptApi().list(video_id))
            chosen = next((t for t in captions if t.language_code.startswith('en')),None) or captions[0]
            fetched = chosen.fetch()
            record['captions']={'language':fetched.language_code,'generated':fetched.is_generated,'snippets':fetched.to_raw_data()}
            (root / f'{class_id}-captions.json').write_text(json.dumps(record['captions'],ensure_ascii=False,indent=2),encoding='utf-8')
        except Exception as error:
            record['captionError']=str(error)[:500]
        print(class_id, record.get('oembed',{}).get('title'), record.get('oembed',{}).get('author_name'), 'captions',len(record.get('captions',{}).get('snippets',[])),flush=True)
    except Exception as error:
        record['error']=str(error)
    return record

records = list(ThreadPoolExecutor(max_workers=4).map(fetch_video,videos.items()))
(root / 'official-class-videos.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')

skills = json.loads(Path('src/content/class-skills.json').read_text(encoding='utf-8'))
public = Path('public/media/skills')
public.mkdir(parents=True,exist_ok=True)

def fetch_icon(entry):
    class_id, skill = entry
    record = json.loads((root.parent / f'eight-classes/client-records/{skill["id"]}.json').read_text(encoding='utf-8'))
    icon_path = record['skill']['iconPath']
    url = 'https://aion2.gaming.tools' + icon_path
    item = {'skillId':skill['id'],'classId':class_id,'name':skill['names']['en'],'originalUrl':url,'iconPath':icon_path,'sourceUrl':f'https://aion2.gaming.tools/skills/{skill["id"]}','region':'Global','version':'Client 1.0.21.0; data updated 2026-09-30','checkedAt':'2026-10-05'}
    try:
        blob = download(url)
        (public / f'{skill["id"]}.webp').write_bytes(blob)
        item['bytes']=len(blob)
    except Exception as error:
        item['error']=str(error)
    return item

icons=list(ThreadPoolExecutor(max_workers=8).map(fetch_icon,[(key,skill) for key,values in skills.items() for skill in values]))
(root / 'skill-icon-sources.json').write_text(json.dumps(icons,ensure_ascii=False,indent=2),encoding='utf-8')
print('ICONS',len(icons),'failures',[x for x in icons if 'error' in x])
