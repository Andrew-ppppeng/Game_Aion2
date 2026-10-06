"""One-time, reviewed migration from archived originals to Steam-only public copy."""
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[4]
BEFORE = Path(__file__).parent / 'before'
LOCALES = ['en', 'ja', 'es', 'de']
FORBIDDEN = re.compile(r'(?<![a-zA-Z])(?:KR|TW)(?![a-zA-Z])|Taiwan|Taiwán|Korea(?!n\b)|Corea|韓国|台湾|韓台', re.I)

COPY = {
 'en': {
  'live': 'AION 2 is free-to-play on Steam. Public access opened on October 5, 2026 at 13:00 UTC. Install the main game, App 3393110, and sign in with your playing account.',
  'cap': 'The character-level cap is **45**. Follow your faction’s campaign and finish its remaining unlocks after reaching the cap. Character level, skill rank and gathering proficiency are separate progression systems.',
  'region_title':'Choose your server region', 'region':'Choose **NA West, NA East, Europe, South America or Asia** in the client. Match the region, faction and exact server with friends. Steam and the official PURPLE service share the same game servers.',
  'community_title':'Official news and community help', 'community':'Use [official Discord](https://discord.gg/aion2official) for announcements and help. Watch [AION2Official on Twitch](https://www.twitch.tv/aion2official) for broadcasts and [Drops](/twitch-drops). For account errors, contact [NC support](https://help.plaync.com/faq/aion2global) with the exact error, region, server and launcher. Keep passwords and authentication codes private.',
  'slots':'Check your visible Stigma slots and available upgrade points. Learning another Stigma does not create an equipment slot. On the Daevanion board, locate the required skill effect and count the route’s total cost before spending points.',
  'server':'Players in Southeast Asia can select the Asia server pool. Match the region, faction and exact server with friends before creating a character.',
  'database':'Use the official item and character links on this site to inspect equipment and players. For an external database, select the Steam release and match its item name, acquisition route and requirements with your client before spending materials.',
  'database_title':'AION 2 Database: Items, Skills and Character Lookup',
  'tier_title':'AION 2 Tier List: Launch Class Ratings and Roles',
  'tier':'These launch ratings describe early solo comfort, party contribution and Abyss utility. They are not measurements of current endgame damage. Compare the role and combat loop for your intended activity before changing class.',
  'tier_heading':'What the launch ratings measure',
  'ranger':'Ranger deals physical damage at range. Keep MP sustainable and use follow-ups when their target conditions are met. Practice maintaining attacks while moving out of danger.',
  'expired_access':'Advanced Access ended on October 5. The base game is now free-to-play; a Founder’s Pack is not required to enter. Compare paid cosmetics, membership and one-time rewards separately.',
  'maintenance':'Public access opened on **October 5, 2026 at 13:00 UTC** after the launch transition. For a current outage or upcoming maintenance, read the latest [service announcement](https://aion2.plaync.com/en-us/board/notice/list).',
  'maintenance_title':'Past launch maintenance', 'maintenance_table':'| Event | UTC time | Status |\n| --- | --- | --- |\n| Public-launch transition | October 5, 05:00–13:00 | Past maintenance window |\n| Public access | October 5, 13:00 | Opened |',
  'patch_title':'Launch update and Duty access', 'patch':'The October 5 launch update included quest-object interaction improvements and a fix for Journal → Duty access after reaching level 45. Open the current Duty panel after reaching 45; do not follow the old advice to avoid opening it before leveling. If access still fails, record the error and contact support.',
  'support':'Check the latest [official Discord](https://discord.gg/aion2official) update and the announcement for your server region.',
  'quick':'Install AION 2 through Steam, choose your region, faction and exact server, adjust your controls and follow the main story. Public access is free-to-play.',
  'settings_link':'Before questing, use the [settings guide](/settings) to adjust targeting, bindings, HUD and graphics.',
  'gear_link':'At 45, finish the remaining campaign, inspect your available activities and use [gear progression](/gear-progression) to plan the next upgrade. Use the [daily and weekly checklist](/daily-weekly-checklist) to review limited rewards.',
  'craft_link':'For recipes and material preparation, continue with the [crafting guide](/crafting).',
 },
 'ja': {
  'live':'AION2はSteamで基本プレイ無料です。一般公開は2026年10月5日13:00 UTCに開始しました。本編のApp 3393110をインストールし、プレイ用のアカウントでログインしてください。',
  'cap':'キャラクターレベルの上限は**45**です。所属勢力のメインストーリーを進め、上限に達した後も残りの解放クエストを完了しましょう。キャラクターレベル、スキルランク、採集熟練度は別々に成長します。',
  'region_title':'サーバー地域を選ぶ','region':'クライアントで**北米西部、北米東部、ヨーロッパ、南米、アジア**を選択します。友人と地域、勢力、正確なサーバー名を合わせてください。Steamと公式PURPLEサービスは同じゲームサーバーでプレイできます。',
  'community_title':'公式情報とサポート','community':'告知や相談には[公式Discord](https://discord.gg/aion2official)を利用します。公式放送と[Drops](/twitch-drops)は[AION2OfficialのTwitch](https://www.twitch.tv/aion2official)で確認できます。アカウントの問題は、エラー全文、地域、サーバー、ランチャーを添えて[NCサポート](https://help.plaync.com/faq/aion2global)に連絡してください。パスワードや認証コードは共有しないでください。',
  'slots':'表示されているスティグマ枠と強化ポイントを確認します。別のスティグマを習得しても装備枠は増えません。ディーヴァニオンでは必要なスキル効果を探し、到達までの合計コストを確認してからポイントを使います。',
  'server':'東南アジアのプレイヤーはアジアのサーバー群を選べます。キャラクター作成前に、友人と地域、勢力、正確なサーバー名を合わせてください。',
  'database':'装備やプレイヤーの確認には、当サイトの公式アイテム・キャラクターリンクを使います。外部データベースではSteam版を選び、素材を使う前にアイテム名、入手方法、条件をクライアントと照合します。',
  'database_title':'AION2データベース：アイテム・スキル・キャラクター検索','tier_title':'AION2職業ティア：開始時の評価と役割',
  'tier':'開始時の評価は、序盤のソロ操作、パーティー貢献、アビスでの役割を扱います。現在のエンドゲーム火力の測定値ではありません。職業を変更する前に、目的のコンテンツに必要な役割と操作を比較してください。','tier_heading':'開始時の評価が扱う内容',
  'ranger':'ボウ ウイングは遠距離から物理ダメージを与えます。MPを維持し、対象条件を満たしたときに追撃を使います。危険を避けて移動しながら攻撃を続ける練習をしましょう。',
  'expired_access':'先行アクセスは10月5日に終了しました。本編は基本プレイ無料で、入場にファウンダーパックは不要です。外見、メンバーシップ、一度限りの特典はそれぞれ確認してください。',
  'maintenance':'一般公開はサービス移行後の**2026年10月5日13:00 UTC**に開始しました。現在の障害や今後のメンテナンスは最新の[サービス告知](https://aion2.plaync.com/en-us/board/notice/list)で確認してください。',
  'maintenance_title':'過去の正式公開メンテナンス','maintenance_table':'| イベント | UTC時刻 | 状態 |\n| --- | --- | --- |\n| 正式公開への移行 | 10月5日05:00–13:00 | 過去のメンテナンス枠 |\n| 一般公開 | 10月5日13:00 | 開始済み |',
  'patch_title':'正式公開アップデートとDutyの利用','patch':'10月5日のアップデートにはクエストオブジェクトの操作改善と、レベル45到達後のJournal → Dutyアクセスの修正が含まれます。45になったら現在のDuty画面を開いてください。レベル上げ前に画面を開くなという古い回避策は使いません。利用できない場合はエラーを記録してサポートへ連絡します。',
  'support':'最新の[公式Discord](https://discord.gg/aion2official)更新と、利用するサーバー地域の告知を確認してください。',
  'quick':'SteamでAION2をインストールし、地域、勢力、正確なサーバー名を選びます。操作設定を調整してメインストーリーを進めてください。一般公開は基本プレイ無料です。',
  'settings_link':'クエスト開始前に[設定ガイド](/settings)でターゲット選択、キー、HUD、画面設定を調整します。',
  'gear_link':'45になったら残りのストーリーと利用可能な活動を確認し、[装備成長](/gear-progression)で次の強化を決めます。[毎日・毎週チェックリスト](/daily-weekly-checklist)では回数制限のある報酬を確認できます。',
  'craft_link':'レシピと素材の準備は[製作ガイド](/crafting)を参照してください。',
 },
 'es': {
  'live':'AION 2 es gratuito en Steam. El acceso público comenzó el 5 de octubre de 2026 a las 13:00 UTC. Instala el juego principal, App 3393110, e inicia sesión con tu cuenta de juego.',
  'cap':'El nivel máximo de personaje es **45**. Sigue la campaña de tu facción y termina los desbloqueos pendientes al llegar al límite. El nivel del personaje, el rango de habilidad y la competencia de recolección progresan por separado.',
  'region_title':'Elige la región del servidor','region':'Selecciona **Norteamérica Oeste, Norteamérica Este, Europa, Sudamérica o Asia** en el cliente. Coincide con tus amigos en región, facción y servidor exacto. Steam y el servicio oficial de PURPLE comparten servidores de juego.',
  'community_title':'Noticias oficiales y ayuda','community':'Usa el [Discord oficial](https://discord.gg/aion2official) para anuncios y ayuda. Sigue [AION2Official en Twitch](https://www.twitch.tv/aion2official) para emisiones y [Drops](/twitch-drops). Para problemas de cuenta, contacta con [soporte de NC](https://help.plaync.com/faq/aion2global) e incluye el error exacto, región, servidor y lanzador. No compartas contraseñas ni códigos de autenticación.',
  'slots':'Comprueba las ranuras visibles de Estigma y los puntos disponibles. Aprender otro Estigma no crea una ranura. En Daevanion, localiza el efecto necesario y calcula el coste total de la ruta antes de gastar puntos.',
  'server':'Los jugadores del sudeste asiático pueden elegir el grupo de servidores de Asia. Acuerda la región, facción y servidor exacto con tus amigos antes de crear el personaje.',
  'database':'Usa los enlaces oficiales de objetos y personajes de este sitio para consultar equipo y jugadores. En una base de datos externa, selecciona la versión de Steam y compara el nombre, la obtención y los requisitos con el cliente antes de gastar materiales.',
  'database_title':'Base de datos de AION 2: objetos, habilidades y personajes','tier_title':'Tier list de AION 2: valoraciones iniciales y funciones',
  'tier':'Las valoraciones iniciales describen comodidad en solitario, contribución al grupo y utilidad en el Abismo. No miden el daño actual de final de juego. Compara la función y el ciclo de combate de tu actividad antes de cambiar de clase.','tier_heading':'Qué miden las valoraciones iniciales',
  'ranger':'El Explorador inflige daño físico a distancia. Mantén el MP y utiliza los ataques de seguimiento cuando se cumplan sus condiciones. Practica seguir atacando mientras evitas el peligro.',
  'expired_access':'El acceso anticipado terminó el 5 de octubre. El juego base ya es gratuito; no necesitas un paquete de fundador para entrar. Compara por separado cosméticos, membresía y recompensas únicas.',
  'maintenance':'El acceso público comenzó el **5 de octubre de 2026 a las 13:00 UTC**, tras la transición de lanzamiento. Consulta el último [anuncio del servicio](https://aion2.plaync.com/en-us/board/notice/list) para interrupciones actuales o próximos mantenimientos.',
  'maintenance_title':'Mantenimiento de lanzamiento anterior','maintenance_table':'| Evento | Hora UTC | Estado |\n| --- | --- | --- |\n| Transición al lanzamiento | 5 de octubre, 05:00–13:00 | Ventana de mantenimiento pasada |\n| Acceso público | 5 de octubre, 13:00 | Abierto |',
  'patch_title':'Actualización de lanzamiento y acceso a Duty','patch':'La actualización del 5 de octubre incluyó mejoras al interactuar con objetos de misión y una corrección de acceso a Journal → Duty al alcanzar el nivel 45. Abre el panel actual de Duty al llegar a 45; no sigas el consejo antiguo de evitarlo antes de subir de nivel. Si el acceso falla, registra el error y contacta con soporte.',
  'support':'Consulta la actualización del [Discord oficial](https://discord.gg/aion2official) y el anuncio de tu región de servidor.',
  'quick':'Instala AION 2 en Steam, elige región, facción y servidor exacto, ajusta los controles y sigue la historia principal. El acceso público es gratuito.',
  'settings_link':'Antes de empezar, usa la [guía de ajustes](/settings) para configurar objetivos, teclas, HUD y gráficos.',
  'gear_link':'Al llegar a 45, termina la campaña pendiente y revisa las actividades disponibles. Usa la [progresión de equipo](/gear-progression) para decidir la próxima mejora y la [lista diaria y semanal](/daily-weekly-checklist) para revisar recompensas limitadas.',
  'craft_link':'Para preparar recetas y materiales, continúa con la [guía de fabricación](/crafting).',
 },
 'de': {
  'live':'AION 2 ist auf Steam kostenlos spielbar. Der öffentliche Zugang begann am 5. Oktober 2026 um 13:00 UTC. Installiere das Hauptspiel, App 3393110, und melde dich mit deinem Spielkonto an.',
  'cap':'Die maximale Charakterstufe ist **45**. Folge der Kampagne deiner Fraktion und erledige nach Erreichen des Limits die übrigen Freischaltungen. Charakterstufe, Fertigkeitsrang und Sammelerfahrung entwickeln sich getrennt.',
  'region_title':'Wähle deine Serverregion','region':'Wähle im Client **Nordamerika West, Nordamerika Ost, Europa, Südamerika oder Asien**. Stimme Region, Fraktion und genauen Server mit Freunden ab. Steam und der offizielle PURPLE-Dienst nutzen dieselben Spielserver.',
  'community_title':'Offizielle Nachrichten und Hilfe','community':'Nutze den [offiziellen Discord](https://discord.gg/aion2official) für Ankündigungen und Hilfe. Bei [AION2Official auf Twitch](https://www.twitch.tv/aion2official) findest du Sendungen und [Drops](/twitch-drops). Kontoprobleme meldest du mit genauer Fehlermeldung, Region, Server und Launcher beim [NC-Support](https://help.plaync.com/faq/aion2global). Teile keine Passwörter oder Bestätigungscodes.',
  'slots':'Prüfe die sichtbaren Stigma-Plätze und verfügbaren Punkte. Ein weiteres erlerntes Stigma schafft keinen Ausrüstungsplatz. Suche auf dem Daevanion-Brett den benötigten Fertigkeitseffekt und zähle die Gesamtkosten des Weges, bevor du Punkte ausgibst.',
  'server':'Spieler in Südostasien können den asiatischen Serverpool wählen. Stimme Region, Fraktion und genauen Server vor der Charaktererstellung mit Freunden ab.',
  'database':'Nutze die offiziellen Gegenstands- und Charakterlinks dieser Website für Ausrüstung und Spieler. Wähle bei einer externen Datenbank die Steam-Fassung und gleiche Namen, Erwerbsweg und Voraussetzungen vor dem Materialverbrauch mit dem Client ab.',
  'database_title':'AION 2 Datenbank: Gegenstände, Fertigkeiten und Charaktere','tier_title':'AION 2 Tier List: Bewertungen zum Start und Rollen',
  'tier':'Die Bewertungen zum Start beschreiben frühes Solospiel, Gruppenbeitrag und Nutzen im Abyss. Sie messen keinen aktuellen Endgame-Schaden. Vergleiche Rolle und Kampfschleife für deine Aktivität, bevor du die Klasse wechselst.','tier_heading':'Was die Bewertungen zum Start erfassen',
  'ranger':'Der Jäger verursacht physischen Fernkampfschaden. Halte MP verfügbar und nutze Folgeangriffe, wenn ihre Zielbedingungen erfüllt sind. Übe, beim Ausweichen weiter anzugreifen.',
  'expired_access':'Der Vorabzugang endete am 5. Oktober. Das Hauptspiel ist jetzt kostenlos; ein Gründerpaket ist zum Spielen nicht erforderlich. Vergleiche Kosmetik, Mitgliedschaft und einmalige Belohnungen getrennt.',
  'maintenance':'Der öffentliche Zugang begann nach dem Startübergang am **5. Oktober 2026 um 13:00 UTC**. Aktuelle Ausfälle oder kommende Wartungen findest du in der neuesten [Dienstmeldung](https://aion2.plaync.com/en-us/board/notice/list).',
  'maintenance_title':'Vergangene Wartung zum Spielstart','maintenance_table':'| Ereignis | UTC-Zeit | Status |\n| --- | --- | --- |\n| Übergang zum öffentlichen Start | 5. Oktober, 05:00–13:00 | Vergangenes Wartungsfenster |\n| Öffentlicher Zugang | 5. Oktober, 13:00 | Geöffnet |',
  'patch_title':'Startupdate und Duty-Zugang','patch':'Das Update vom 5. Oktober enthielt Verbesserungen für Questobjekte und eine Korrektur des Zugangs zu Journal → Duty nach Stufe 45. Öffne auf Stufe 45 das aktuelle Duty-Fenster; befolge den alten Rat, es vor dem Leveln zu meiden, nicht mehr. Bleibt der Zugang gesperrt, halte die Fehlermeldung fest und wende dich an den Support.',
  'support':'Prüfe die neueste Meldung im [offiziellen Discord](https://discord.gg/aion2official) und die Ankündigung für deine Serverregion.',
  'quick':'Installiere AION 2 auf Steam, wähle Region, Fraktion und genauen Server, passe die Steuerung an und folge der Hauptgeschichte. Der öffentliche Zugang ist kostenlos.',
  'settings_link':'Passe vor den Quests mit dem [Einstellungsguide](/settings) Zielwahl, Tasten, HUD und Grafik an.',
  'gear_link':'Erledige auf Stufe 45 die übrige Kampagne und prüfe verfügbare Aktivitäten. Plane mit dem [Ausrüstungsfortschritt](/gear-progression) die nächste Verbesserung und mit der [Tages- und Wochenliste](/daily-weekly-checklist) begrenzte Belohnungen.',
  'craft_link':'Für Rezepte und Materialvorbereitung lies den [Herstellungsguide](/crafting).',
 },
}

def write_json(path, value):
 path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')

def section(body, anchor, title, text):
 return re.sub(r'<h2 id="'+re.escape(anchor)+r'">.*?(?=<h2 |\Z)',f'<h2 id="{anchor}">{title}</h2>\n\n{text}\n\n',body,flags=re.S)

def clean(value, fallback):
 if isinstance(value,str): return fallback if FORBIDDEN.search(value) else value
 if isinstance(value,list): return [clean(v,fallback) for v in value]
 if isinstance(value,dict): return {k:clean(v,fallback) for k,v in value.items()}
 return value

for loc in LOCALES:
 c=COPY[loc]; p=ROOT/'src/content'/loc
 for original in (BEFORE/'src/content'/loc).glob('*.mdx'):
  slug=original.stem
  if slug=='global-changes':
   (p/original.name).unlink(missing_ok=True);(p/f'{slug}.json').unlink(missing_ok=True);continue
  body=original.read_text(encoding='utf-8');meta=json.loads((BEFORE/'src/content'/loc/f'{slug}.json').read_text(encoding='utf-8'))
  # Entire dedicated regional sections, including their tables, are removed.
  removed={'download':['taiwan-client'],'classes':['brawler-and-regional-guides'],'steam':['global-and-regional-versions'],'code':['regional-coupons']}.get(slug,[])
  next_tags=re.findall(r'<GuideNext[^>]+/>',body)
  for anchor in removed:body=re.sub(r'<h2 id="'+anchor+r'">.*?(?=<h2 |\Z)','',body,flags=re.S)
  meta['toc']=[x for x in meta['toc'] if x['id'] not in removed]
  if slug=='guide':
   body=body[body.index('<h2'):];body=re.sub(r'(<h2 id="start-global">.*?</h2>\s*).*?(?=\n\n)',lambda m:m[1]+c['live'],body,count=1,flags=re.S)
   body=section(body,'how-to-play-by-region',c['region_title'],c['region'])
   body=section(body,'community-resources',c['community_title'],c['community'])
   body=body.replace('<GuideChecklist />',c['settings_link']+'\n\n<GuideChecklist />')
   meta.update(quickAnswer=c['quick'],summary=c['quick'],description=c['live'])
   meta['summary']=c['region']
   for entry in meta['toc']:
    if entry['id']=='how-to-play-by-region':entry['title']=c['region_title']
    if entry['id']=='community-resources':entry['title']=c['community_title']
  if slug=='leveling':
   start=body.index('<GuideVisual');body=re.sub(r'(?<=</h2>)\s*.*?(?=<GuideVisual)', '\n\n'+c['cap']+'\n\n',body,count=1,flags=re.S)
   body=re.sub(r'\*\*TW.*?(?=</GuideFaction>)','',body,flags=re.S)
   body=body.replace('<GuideNext',c['gear_link']+'\n\n<GuideNext',1)
   meta.update(quickAnswer=c['cap'].replace('**',''),summary=c['region'],description=c['cap'].replace('**',''))
  if slug=='tier-list':
   lines=body.splitlines();new=[];in_tiers=False
   for line in lines:
    if '<h2 id="author-tier-comparison"' in line:in_tiers=True
    elif line.startswith('<h2 '):in_tiers=False
    if in_tiers and line.startswith('|'):
     parts=line.split('|');line='|'+ '|'.join(parts[1:3])+'|'
    new.append(line)
   body='\n'.join(new)
   body=section(body,'what-each-list-measures',c['tier_heading'],c['tier'])
   body=section(body,'spiritmaster-and-ranger',meta['toc'][2]['title'],c['ranger'])
   meta.update(title=c['tier_title'],description=c['tier'],summary=c['tier'],quickAnswer=c['ranger'])
   meta['toc'][1]['title']=c['tier_heading']
  if slug=='maintenance':
   body=c['maintenance']+'\n\n'+body[body.index('<h2'):]
   body=section(body,'announced-windows',c['maintenance_title'],c['maintenance_table']+'\n\n<GuideTimers />\n\n<GuideVisual id="workflow" />')
   body=section(body,'patch-and-compensation',c['patch_title'],c['patch'])
   meta.update(description=c['maintenance'].replace('**',''),quickAnswer=c['maintenance'].split(' For ')[0].replace('**',''))
   for t in meta['toc']:
    if t['id']=='announced-windows':t['title']=c['maintenance_title']
    if t['id']=='patch-and-compensation':t['title']=c['patch_title']
  if slug=='steam':body=c['live']+'\n\n'+body[body.index('<h2'):]
  if slug=='gathering':body=body.replace('<GuideNext',c['craft_link']+'\n\n<GuideNext',1)
  # Remove remaining cross-service paragraphs, never relabel their facts as Global.
  paragraphs=re.split(r'\n\s*\n',body); kept=[]
  for para in paragraphs:
   if FORBIDDEN.search(para):
    if para.startswith('|'):para='\n'.join(line for line in para.splitlines() if not FORBIDDEN.search(line))
    elif slug=='builds' and ('Stigma' in para or 'スティグマ' in para or 'Estigma' in para):para=c['slots']
    elif slug=='server':para=c['server']
    elif slug=='ranger':para=c['slots']
    elif slug=='database':para=c['database']
    elif slug=='maintenance':para=c['support']
    else:continue
   kept.append(para)
  body='\n\n'.join(kept).strip()+'\n'
  for tag in next_tags:
   if tag not in body:body+='\n'+tag+'\n'
  for visual in meta['visuals']:
   tag=f'<GuideVisual id="{visual}" />'
   if tag not in body:body=body.replace('<GuideNext',tag+'\n\n<GuideNext',1)
  body=body.replace('/global-changes','/guide')
  # Replace obsolete access paragraphs in the affected public guides.
  if slug in ['guide','server','monetization','code']:
   blocks=body.split('\n\n')
   for i,b in enumerate(blocks):
    if re.search(r'October 5|5 de octubre|5\. Oktober|10月5日',b) and re.search(r'scheduled|before|ends|programado|termina|endet|geplant|予定|終了',b) and not b.startswith('<h'):
     blocks[i]=c['expired_access'] if slug=='monetization' else c['live']
   body='\n\n'.join(blocks)
  meta=clean(meta,c['database'] if slug=='database' else c['quick'])
  if slug=='database':meta.update(title=c['database_title'],summary=c['database'],quickAnswer=c['database'],description=c['database']+' '+c['cap'].replace('**',''))
  if slug in ['download','steam']:meta['description']=c['live'];meta['summary']=c['region']
  if meta['quickAnswer']==meta['summary']:meta['summary']=c['region']
  (p/f'{slug}.mdx').write_text(body,encoding='utf-8');write_json(p/f'{slug}.json',meta)
 # Public labels: remove the retired page and add the approved topics later.
 messages=json.loads((BEFORE/'src/messages'/f'{loc}.json').read_text(encoding='utf-8'))
 messages['topics'].pop('global-changes',None)
 messages['categories'].pop('regionalDifferences',None)
 messages['home']['hero']['stats'][1]={'en':'Read current service announcements','ja':'最新のサービス告知を確認','es':'Consulta los avisos actuales','de':'Aktuelle Dienstmeldungen lesen'}[loc]
 write_json(ROOT/'src/messages'/f'{loc}.json',messages)

plan=json.loads((BEFORE/'content-topics.json').read_text(encoding='utf-8'))
plan['categories']=[g for g in plan['categories'] if g['category']!='regional differences']
write_json(ROOT/'content-topics.json',plan)
for p in (ROOT/'src/content/article-data').glob('*.json'):
 d=json.loads(p.read_text(encoding='utf-8'));d['related']=[x for x in d['related'] if x!='global-changes']
 if p.stem!='global-changes':d['checkedAt']='2026-10-06';d['revision']='2026-10-06.steam-beginner-1'
 write_json(p,d)
for relative in ['src/lib/articles.ts','src/lib/reading-paths.ts']:
 p=ROOT/relative;t=p.read_text(encoding='utf-8');t='\n'.join(line for line in t.splitlines() if 'global_changes' not in line and "'global-changes'" not in line)+'\n';p.write_text(t,encoding='utf-8')
p=ROOT/'src/lib/topics.ts';t=p.read_text(encoding='utf-8').replace("  'regional differences': 'regionalDifferences',\n",'');p.write_text(t,encoding='utf-8')
print('Updated archived public articles and retired regional comparison route.')
