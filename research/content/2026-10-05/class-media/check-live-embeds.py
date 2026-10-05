import json
import re
import sys
from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding='utf-8')
root=Path(__file__).parent
videos=json.loads((root/'official-class-videos.json').read_text(encoding='utf-8'))
def check(entry):
 url='https://www.youtube.com/embed/'+entry['videoId']
 item={'classId':entry['classId'],'url':url}
 try:
  response=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0','Referer':'https://aion2wiki.space/'}),timeout=25)
  raw=response.read()
  (root/f'embed-{entry["classId"]}.html').write_bytes(raw)
  html=raw.decode('utf-8',errors='replace')
  item.update(status=response.status,bytes=len(raw),hasPlayerConfig='PLAYER_CONFIG' in html or 'PLAYER_VARS' in html or 'ytcfg.set' in html)
  matches=list(re.finditer(r'playabilityStatus|isEmbeddable|embeddable|UNPLAYABLE|LOGIN_REQUIRED|ERROR|embedError',html))
  item['playerStatusSnippets']=[html[max(0,m.start()-60):m.end()+180] for m in matches[:12]]
 except Exception as error: item['error']=str(error)
 return item
result=list(ThreadPoolExecutor(max_workers=4).map(check,videos))
(root/'live-embed-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
