import json
import shutil
import sys
from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding='utf-8')
root=Path(__file__).parent
records=json.loads((root/'skill-icon-sources.json').read_text(encoding='utf-8'))
public=Path('public/media/skills')
by_path={r['iconPath']:public/f'{r["skillId"]}.webp' for r in records if (public/f'{r["skillId"]}.webp').exists()}
def retry(r):
 target=public/f'{r["skillId"]}.webp'
 if target.exists(): return r
 if r['iconPath'] in by_path:
  shutil.copyfile(by_path[r['iconPath']],target)
  r.pop('error',None)
  r['bytes']=target.stat().st_size
  r['recovery']='Same exact iconPath from a successfully downloaded skill'
  return r
 for attempt in range(3):
  try:
   blob=urlopen(Request(r['originalUrl'],headers={'User-Agent':'Mozilla/5.0'}),timeout=15).read()
   target.write_bytes(blob)
   r.pop('error',None)
   r['bytes']=len(blob)
   print('RECOVERED',r['skillId'],flush=True)
   return r
  except Exception as error: r['error']=str(error)
 return r
recovered=list(ThreadPoolExecutor(max_workers=3).map(retry,records))
(root/'skill-icon-sources-final.json').write_text(json.dumps(recovered,ensure_ascii=False,indent=2),encoding='utf-8')
print('ICONS',sum('error' not in r for r in recovered),'FAILURES',[r['skillId'] for r in recovered if 'error' in r])
