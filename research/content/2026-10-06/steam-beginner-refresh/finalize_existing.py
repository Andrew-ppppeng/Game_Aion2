from pathlib import Path
import ast,json,re
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).parent
copy=next(ast.literal_eval(n.value) for n in ast.parse((HERE/'refresh_existing.py').read_text(encoding='utf-8')).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='COPY' for t in n.targets))
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
schedule={
 'en':('Launch history','| Stage | UTC window |\n| --- | --- |\n| Advanced Access — ended | September 30, 13:00–October 5, 05:00 |\n| Launch maintenance — past | October 5, 05:00–13:00 |\n| Public access — open | October 5, 13:00 |','Europe launch time','Europe opened on **October 5, 2026 at 13:00 UTC / 14:00 BST / 15:00 CEST / 16:00 EEST**. Public access is free-to-play. Select Europe in the [server guide](/server#europe-pairings).'),
 'ja':('公開までの日程','| 段階 | UTC日程 |\n| --- | --- |\n| 先行アクセス — 終了 | 9月30日13:00–10月5日05:00 |\n| 公開メンテナンス — 過去 | 10月5日05:00–13:00 |\n| 一般公開 — 開始済み | 10月5日13:00 |','欧州での公開時刻','欧州の公開は**2026年10月5日13:00 UTC / 14:00 BST / 15:00 CEST / 16:00 EEST**です。一般公開は基本プレイ無料です。[サーバーガイド](/server#europe-pairings)でEuropeを選んでください。'),
 'es':('Historial del lanzamiento','| Etapa | Ventana UTC |\n| --- | --- |\n| Acceso anticipado — terminado | 30 de septiembre, 13:00–5 de octubre, 05:00 |\n| Mantenimiento de lanzamiento — pasado | 5 de octubre, 05:00–13:00 |\n| Acceso público — abierto | 5 de octubre, 13:00 |','Hora de lanzamiento en Europa','Europa abrió el **5 de octubre de 2026 a las 13:00 UTC / 14:00 BST / 15:00 CEST / 16:00 EEST**. El acceso público es gratuito. Selecciona Europe en la [guía de servidores](/server#europe-pairings).'),
 'de':('Verlauf des Spielstarts','| Phase | UTC-Zeitraum |\n| --- | --- |\n| Vorabzugang — beendet | 30. September, 13:00–5. Oktober, 05:00 |\n| Startwartung — vergangen | 5. Oktober, 05:00–13:00 |\n| Öffentlicher Zugang — geöffnet | 5. Oktober, 13:00 |','Startzeit in Europa','Europa öffnete am **5. Oktober 2026 um 13:00 UTC / 14:00 BST / 15:00 CEST / 16:00 EEST**. Der öffentliche Zugang ist kostenlos. Wähle Europe im [Serverguide](/server#europe-pairings).'),
}
def section(t,a,title,text):return re.sub(r'<h2 id="'+a+r'">.*?(?=<h2 |\Z)',f'<h2 id="{a}">{title}</h2>\n\n{text}\n\n',t,flags=re.S)
for loc in ['en','ja','es','de']:
 c=copy[loc];p=ROOT/f'src/content/{loc}/server.mdx';t=p.read_text(encoding='utf-8');parts=[x for x in t.split('\n\n') if '/maintenance)' not in x and 'App 3393110' not in x];t='\n\n'.join(parts);t=t.replace('<GuideNext',c['live']+' [Maintenance](/maintenance).\n\n<GuideNext',1);p.write_text(t,encoding='utf-8')
 p=ROOT/f'src/content/{loc}/steam.mdx';t=p.read_text(encoding='utf-8');s=schedule[loc]
 t=section(t,'access-schedule',s[0],s[1]+'\n\n[Maintenance](/maintenance).')
 t=section(t,'europe-launch-time',s[2],s[3])
 # Supported Korean language is a Steam compatibility fact, not a service guide.
 original=(HERE/f'before/src/content/{loc}/steam.mdx').read_text(encoding='utf-8')
 language=re.search(r'<h2 id="supported-languages">.*?(?=<h2 |\Z)',original,re.S)
 if language:t=re.sub(r'<h2 id="supported-languages">.*?(?=<h2 |\Z)',lambda m:language[0],t,flags=re.S)
 p.write_text(t,encoding='utf-8')
 p=ROOT/f'src/content/{loc}/steam.json';m=json.loads(p.read_text(encoding='utf-8'))
 for entry in m['toc']:
  if entry['id']=='access-schedule':entry['title']=s[0]
  if entry['id']=='europe-launch-time':entry['title']=s[2]
 m['quickAnswer']=c['live'];m['visuals']['workflow']['steps'][-1]['description']=c['live'];save(p,m)
 p=ROOT/f'src/content/{loc}/monetization.mdx';t=p.read_text(encoding='utf-8')
 blocks=t.split('\n\n')
 for i,b in enumerate(blocks):
  if re.search(r'October 5|5 de octubre|5\. Oktober|10月5日',b) and re.search(r'05:00|13:00',b):blocks[i]=c['expired_access']
 p.write_text('\n\n'.join(blocks),encoding='utf-8')
print('Aligned launch history, server links and supported languages.')
