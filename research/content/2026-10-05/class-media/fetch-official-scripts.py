from pathlib import Path
from urllib.request import Request, urlopen
import re
root = Path(__file__).parent
urls = {
 'about-main': 'https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/js/main.js',
 'guide-view': 'https://assets.playnccdn.com/uikit/guidebook/2.1.2/js/view.js',
}
for key, url in urls.items():
 text = urlopen(Request(url, headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode('utf-8')
 (root / f'{key}.js').write_text(text,encoding='utf-8')
 patterns = 'mp4|youtube|classes/|skill|guidebook/|getGuide|apiUrl|apiDomain'
 print(key, len(text))
 matches = list(re.finditer(patterns,text,re.I))
 for match in matches[:45]:
  print(text[max(0,match.start()-180):match.end()+260])
