from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[4]
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for loc,labels in {
 'en':['Beginner videos','Install the Steam client, check PC requirements and resolve installation problems.','Find the official Steam game, account login, supported platforms and available languages.'],
 'ja':['初心者向け動画','Steamクライアントのインストール、PC要件、インストール時の問題への対処を確認します。','公式Steamゲーム、アカウントログイン、対応プラットフォームと言語を確認します。'],
 'es':['Vídeos para principiantes','Instala el cliente de Steam, comprueba los requisitos de PC y resuelve problemas de instalación.','Encuentra el juego oficial de Steam, el inicio de sesión, las plataformas y los idiomas disponibles.'],
 'de':['Einsteiger-Videos','Installiere den Steam-Client, prüfe PC-Anforderungen und behebe Installationsprobleme.','Finde das offizielle Steam-Spiel, Kontoanmeldung, unterstützte Plattformen und verfügbare Sprachen.'],
}.items():
 p=ROOT/f'src/messages/{loc}.json';m=json.loads(p.read_text(encoding='utf-8'));m['ui']['beginnerVideos']=labels[0];save(p,m)
 for i,slug in enumerate(['download','steam']):
  p=ROOT/f'src/content/{loc}/{slug}.json';m=json.loads(p.read_text(encoding='utf-8'));m['description']=labels[i+1];save(p,m)
 for slug in ['settings','gear-progression','daily-weekly-checklist','crafting']:
  p=ROOT/f'src/content/{loc}/{slug}.mdx';body=p.read_text(encoding='utf-8')
  messages=json.loads((ROOT/f'src/messages/{loc}.json').read_text(encoding='utf-8'))
  for topic,label in messages['topics'].items():body=body.replace(f'[{topic}](/',f'[{label}](/')
  p.write_text(body,encoding='utf-8')
p=ROOT/'src/content/ja/tier-list.mdx';p.write_text(p.read_text(encoding='utf-8').replace('ボウ ウイング','レンジャー'),encoding='utf-8')
p=ROOT/'src/app/globals.css';t=p.read_text(encoding='utf-8');end=t.index('@import')
if end>0:t=t[end:]+'\n'+t[:end];p.write_text(t,encoding='utf-8')
home=json.loads((ROOT/'home.en.json').read_text(encoding='utf-8'));home['home']['hero']['stats'][1]='Read current service announcements';save(ROOT/'home.en.json',home)
print('Fixed localized navigation and unique metadata.')
