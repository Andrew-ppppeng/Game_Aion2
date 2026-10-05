"""Additional official context; keeps the first capture files untouched."""
from fetch_official import capture
import concurrent.futures
import json
import pathlib

JOBS = [
  ('nc-global-launch-context','https://about.ncsoft.com/news/article/A2_update_20261001','Global','html'),
  ('nc-kr-new-regions-original','https://about.ncsoft.com/news/article/Aion2_update_20260701','KR service context','html'),
  ('nc-kr-tw-launch-context','https://about.ncsoft.com/news/article/aion2_update_251118','KR/TW','html'),
  ('global-clash-rune-example','https://aion2.plaync.com/en-us/api/gameconst/item?id=310900001&enchantLevel=0&lang=en-US&region=eu','Global EU; one item example only','json'),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  result=list(pool.map(capture,JOBS))
pathlib.Path(__file__).with_name('context-fetch-manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
