"""One-time authored update; reads the preserved collection and writes the public catalogue."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).parent
COLLECTION = ROOT / 'research/youtube/2026-10-06-beginner-guides'
LOCALES = ['en', 'ja', 'es', 'de']
manifest = json.loads((COLLECTION / 'manifest.json').read_text(encoding='utf-8'))
original = {s['id']: s for s in manifest['sources']}

def localized(values):
    return dict(zip(LOCALES, values))

records = []
def add(id, category, titles, reasons, topics, chapters, rank=None):
    s = original[id]
    c = [{'seconds': seconds, 'labels': localized(labels)} for seconds, labels in chapters]
    record = dict(id=id, originalTitle=s['title'], channel=s['channel'].strip(), publishedAt=s['upload_date'], durationSeconds=s['duration'], language='en', category=category, cover=f'/media/videos/{id}.jpg', startSeconds=c[0]['seconds'], topics=list(topics), articleStarts=topics, chapters=c, titles=localized(titles), reasons=localized(reasons))
    if rank:
        record['featuredRank'] = rank
    records.append(record)

add('0KJtQApx_o4', 'settings',
    ['Combat, HUD and graphics settings', '戦闘・HUD・グラフィック設定', 'Ajustes de combate, HUD y gráficos', 'Kampf-, HUD- und Grafikeinstellungen'],
    ['Set pursuit, target scanning and combat-only buffs; jump to the HUD or graphics walkthrough.', '追撃、ターゲット検索、戦闘中のみのバフを設定し、HUDと画質の実演を確認。', 'Configura persecución, selección de objetivos y mejoras solo en combate; consulta el HUD y los gráficos.', 'Richte Verfolgung, Zielsuche und Kampf-Buffs ein; sieh dir HUD und Grafikoptionen an.'],
    {'settings': 62, 'download': 542},
    [(62, ['Combat controls', '戦闘操作', 'Controles de combate', 'Kampfsteuerung']), (418, ['HUD layout', 'HUDの配置', 'Distribución del HUD', 'HUD-Anordnung']), (542, ['Graphics options', 'グラフィック設定', 'Opciones gráficas', 'Grafikoptionen'])], 2)
add('Ei17ATvSLGM', 'basics',
    ['Settings, skills and exploration essentials', '設定・スキル・探索の基本', 'Ajustes, habilidades y exploración', 'Einstellungen, Fertigkeiten und Erkundung'],
    ['Start with targeting and potions, then learn where skill points, Daevanion and hidden cubes fit.', 'ターゲットとポーション設定から始め、スキルポイント、Daevanion、隠しキューブを理解。', 'Empieza por objetivos y pociones y aprende cómo funcionan los puntos de habilidad, Daevanion y los cubos ocultos.', 'Beginne mit Zielen und Tränken; lerne Fertigkeitspunkte, Daevanion und versteckte Würfel kennen.'],
    {'guide': 34, 'settings': 34, 'builds': 134, 'map': 233},
    [(34, ['Starting settings', '最初の設定', 'Ajustes iniciales', 'Erste Einstellungen']), (134, ['Skill points and Specialty', 'スキルポイントと特化', 'Puntos de habilidad y especialización', 'Fertigkeitspunkte und Spezialisierung']), (233, ['Exploration rewards', '探索報酬', 'Recompensas de exploración', 'Erkundungsbelohnungen'])], 1)
add('A0hpQaWDYgs', 'leveling',
    ['Episode quests and Ascension gates', 'エピソードクエストと昇級条件', 'Misiones de episodio y barreras de ascensión', 'Episode-Quests und Aufstiegsbedingungen'],
    ['Find Episode quests in the Journal, fill Ascension with nearby objectives and save unnecessary cube claims.', 'Journalでエピソードを追い、近くの目標で昇級ゲージを満たし、不要なキューブ消費を抑える。', 'Sigue los episodios del diario, completa ascensión con objetivos cercanos y evita gastar energía en cubos innecesarios.', 'Folge Episoden im Journal, fülle Aufstieg mit nahen Zielen und spare unnötige Würfelbelohnungen.'],
    {'leveling': 16},
    [(16, ['Episode and Ascension route', 'エピソードと昇級', 'Ruta de episodios y ascensión', 'Episoden und Aufstieg']), (86, ['Odyle Energy while leveling', '育成中のOdyle Energy', 'Energía Odyle al subir de nivel', 'Odyle-Energie beim Leveln'])], 3)
add('J8WVY3FxPQM', 'gear',
    ['Equipment progression after level 45', 'レベル45以降の装備成長', 'Progresión de equipo después del nivel 45', 'Ausrüstung nach Stufe 45'],
    ['Follow the exploration-to-dungeon route, upgrade your belt and amulet, and plan when crafting enters the route.', '探索からダンジョンへ進み、ベルトとアミュレットを強化し、製作を始める段階を確認。', 'Avanza de exploración a mazmorras, mejora cinturón y amuleto y decide cuándo incorporar fabricación.', 'Gehe von Erkundung zu Dungeons, verbessere Gürtel und Amulett und plane den Einstieg ins Handwerk.'],
    {'gear-progression': 53, 'crafting': 713},
    [(53, ['First equipment steps', '最初の装備更新', 'Primeras mejoras', 'Erste Ausrüstungsschritte']), (137, ['Belt and amulet morphing', 'ベルトとアミュレットの変換', 'Transformar cinturón y amuleto', 'Gürtel und Amulett umwandeln']), (713, ['When to craft', '製作を始める段階', 'Cuándo fabricar', 'Wann sich Herstellung lohnt'])], 4)
add('Iqi6pR8r6FY', 'crafting',
    ['First professions and the Orichalcum craft chain', '最初の製作職業とOrichalcumの製作連鎖', 'Primeros oficios y cadena de Orichalcum', 'Erste Handwerke und die Orichalcum-Kette'],
    ['Choose a profession by its outputs, farm refining stones and follow the gray-to-green-to-blue recipe inputs.', '作れる品で職業を選び、精錬石を集め、灰色・緑・青の配方素材を追う。', 'Elige un oficio por sus productos, consigue piedras de refinado y sigue los ingredientes de gris a verde y azul.', 'Wähle nach Produkten, sammle Veredelungssteine und verfolge die Rezeptzutaten von Grau über Grün zu Blau.'],
    {'crafting': 101, 'gathering': 17},
    [(101, ['Choose a profession', '製作職業を選ぶ', 'Elegir un oficio', 'Handwerk wählen']), (239, ['Farm crafting materials', '製作素材を集める', 'Conseguir materiales', 'Materialien sammeln']), (382, ['Orichalcum recipe chain', 'Orichalcumの製作連鎖', 'Cadena de recetas Orichalcum', 'Orichalcum-Rezeptkette'])], 5)
add('hAl6c_LwE3M', 'week-one',
    ['Duty quests and weekly resource preparation', 'Dutyクエストと週ごとの資源準備', 'Misiones Duty y recursos semanales', 'Duty-Quests und Wochenressourcen'],
    ['See Duty objectives and the two Odyle Energy morph recipes. Use the current in-game counters for allowances.', 'Dutyの目標と2種類のOdyle Energy変換レシピを確認。回数はゲーム内の現在の表示に従う。', 'Mira los objetivos Duty y las dos recetas de energía Odyle. Las cuotas se consultan en los contadores actuales.', 'Sieh Duty-Ziele und beide Odyle-Energie-Rezepte. Für Kontingente gelten die aktuellen Spielzähler.'],
    {'daily-weekly-checklist': 53},
    [(53, ['Duty quests', 'Dutyクエスト', 'Misiones Duty', 'Duty-Quests']), (377, ['Weekly morph recipes', '週ごとの変換レシピ', 'Recetas semanales de transformación', 'Wöchentliche Umwandlungsrezepte'])], 6)
add('OFA-92_9S6w', 'level-45',
    ['What to do first at level 45', 'レベル45で最初にすること', 'Qué hacer primero en el nivel 45', 'Erste Schritte auf Stufe 45'],
    ['Connect side quests and Daevanion with belt upgrades, rifts and your first equipment target.', 'サブクエストとDaevanionを、ベルト強化、亀裂、最初の装備目標につなげる。', 'Combina misiones secundarias y Daevanion con mejoras de cinturón, grietas y el primer objetivo de equipo.', 'Verbinde Nebenquests und Daevanion mit Gürtel-Upgrades, Rissen und deinem ersten Ausrüstungsziel.'],
    {'gear-progression': 35, 'daily-weekly-checklist': 380},
    [(35, ['Starting at 45', 'レベル45の出発点', 'Inicio en el nivel 45', 'Start auf Stufe 45']), (240, ['Belt and amulet', 'ベルトとアミュレット', 'Cinturón y amuleto', 'Gürtel und Amulett']), (380, ['Daily dungeon', 'デイリーダンジョン', 'Mazmorra diaria', 'Täglicher Dungeon'])])
add('VO6Ym4iHmJ0', 'first-day',
    ['Your first day: controls, questing and skills', '初日：操作・クエスト・スキル', 'Primer día: controles, misiones y habilidades', 'Erster Tag: Steuerung, Quests und Fertigkeiten'],
    ['Watch target settings, main-story pathing and first skill allocations before building a macro.', 'ターゲット設定、メインストーリーの移動、最初のスキル配分を確認してからマクロを組む。', 'Revisa selección de objetivos, recorrido de la historia y primeros puntos antes de crear una macro.', 'Sieh Zieloptionen, Hauptquest-Navigation und erste Fertigkeitspunkte vor deinem ersten Makro.'],
    {'guide': 46, 'leveling': 252},
    [(46, ['Starting controls', '初期操作設定', 'Controles iniciales', 'Erste Steuerung']), (252, ['Main-story pathing', 'ストーリーの移動', 'Ruta de la historia', 'Hauptquest-Navigation']), (408, ['First skill points', '最初のスキルポイント', 'Primeros puntos de habilidad', 'Erste Fertigkeitspunkte'])])
add('3Yn91qaBD5s', 'gear',
    ['Enhancement, sockets and equipment transfer', '強化・ソケット・装備継承', 'Mejoras, ranuras y transferencia de equipo', 'Verstärkung, Sockel und Transfer'],
    ['Identify the upgrade tabs and compare enhancement and Soul Binding with the upgrades transfer does not retain.', '強化メニューを見分け、強化とSoul Bindingの継承、継承されない要素を比較。', 'Identifica los menús de mejora y distingue lo que se transfiere de las mejoras que se pierden.', 'Erkenne die Upgrade-Tabs und unterscheide übertragene Verstärkung und Seelenbindung von verlorenen Upgrades.'],
    {'gear-progression': 89},
    [(89, ['Growth and enhancement', '成長と強化', 'Crecimiento y mejoras', 'Wachstum und Verstärkung']), (257, ['Manastone sockets', 'Manastoneソケット', 'Ranuras de manastones', 'Manastein-Sockel']), (500, ['Equipment transfer', '装備継承', 'Transferencia de equipo', 'Ausrüstungstransfer'])])
add('G1l8__2Q4-w', 'mistakes',
    ['Launch mistakes: gear and reward resources', '開始時の失敗：装備と報酬資源', 'Errores iniciales: equipo y recursos', 'Startfehler bei Ausrüstung und Belohnungen'],
    ['Review Soul Binding and dungeon keys before consuming equipment or reward resources.', '装備や報酬資源を消費する前にSoul Bindingとダンジョンの鍵を確認。', 'Consulta Soul Binding y las llaves antes de consumir equipo o recursos de recompensa.', 'Prüfe Seelenbindung und Dungeon-Schlüssel, bevor du Ausrüstung oder Belohnungsressourcen verbrauchst.'],
    {'guide': 210},
    [(210, ['Soul Binding', 'Soul Binding', 'Soul Binding', 'Seelenbindung']), (538, ['Keys and reward cubes', '鍵と報酬キューブ', 'Llaves y cubos de recompensa', 'Schlüssel und Belohnungswürfel'])])
add('pbA-7lq9Xmk', 'mistakes',
    ['Travel shortcuts and combat bindings', '移動の工夫と戦闘キー設定', 'Atajos de viaje y teclas de combate', 'Reiseabkürzungen und Kampftasten'],
    ['Learn flight and travel shortcuts, map display and direct controls for basic attacks.', '飛行と移動の工夫、地図表示、通常攻撃の操作を確認。', 'Aprende atajos de vuelo y viaje, visualización del mapa y controles de ataques básicos.', 'Lerne Flug- und Reiseabkürzungen, Kartenanzeige und direkte Grundangriffe.'],
    {'map': 225},
    [(21, ['Flight techniques', '飛行テクニック', 'Técnicas de vuelo', 'Flugtechniken']), (225, ['Map overlay', '地図オーバーレイ', 'Mapa superpuesto', 'Kartenoverlay'])])
add('r9ypUSiClQM', 'basics',
    ['A tour of beginner progression systems', '初心者向け成長システムの全体像', 'Recorrido por los sistemas de progresión', 'Überblick über Fortschrittssysteme'],
    ['Use the chapter shortcuts for combat and progression systems when a menu name is unfamiliar.', 'メニュー名が分からないときに、戦闘と成長システムの実演へ移動。', 'Usa los capítulos de combate y progresión para orientarte en los menús.', 'Nutze die Kapitel zu Kampf und Fortschritt, wenn dir ein Menü unbekannt ist.'],
    {'builds': 649},
    [(649, ['Skills and growth systems', 'スキルと成長システム', 'Habilidades y sistemas de progreso', 'Fertigkeiten und Fortschrittssysteme'])])
add('XYzIx0pYdYo', 'settings',
    ['Interface and beginner menu walkthrough', 'インターフェースと初期メニューの実演', 'Interfaz y menús para principiantes', 'Oberfläche und Einsteigermenüs'],
    ['Locate the character and skill panels, then follow the exploration and pet menus.', 'キャラクターとスキル画面を見つけ、探索とペットのメニューを確認。', 'Localiza las pantallas de personaje y habilidades y consulta los menús de exploración y mascotas.', 'Finde Charakter- und Fertigkeitsfenster sowie Erkundungs- und Begleitermenüs.'],
    {'settings': 132, 'map': 681},
    [(132, ['Control modes', '操作モード', 'Modos de control', 'Steuerungsmodi']), (681, ['Collection menus', 'コレクション画面', 'Menús de colección', 'Sammlungsmenüs'])])
for id, cls, seconds, demonstration, names in [
    ('njRrjTJCENU', 'ranger', 234, 597, ['Ranger', '弓星', 'Ranger', 'Ranger']),
    ('E29vReeuSNo', 'assassin', 303, 620, ['Assassin', '殺星', 'Assassin', 'Assassine']),
    ('NdsTPYuL6E4', 'spiritmaster', 214, 507, ['Spiritmaster', '精霊星', 'Spiritmaster', 'Beschwörer']),
    ('YeHM0TzzZ4s', 'cleric', 300, 510, ['Cleric', '治癒星', 'Cleric', 'Kleriker']),
]:
    add(id, 'class',
        [f'{names[0]}: early PvE macro setup', f'{names[1]}：序盤PvEマクロ', f'{names[2]}: macro PvE inicial', f'{names[3]}: frühes PvE-Makro'],
        ['Follow the in-game macro setup and skill demonstration; keep timing-sensitive actions on separate buttons.', 'ゲーム内マクロ設定とスキル実演を確認。タイミングが重要な操作は別キーに残す。', 'Sigue la configuración y la demostración; conserva acciones que requieren precisión en teclas separadas.', 'Folge Einrichtung und Fertigkeitsvorführung; behalte zeitkritische Aktionen auf eigenen Tasten.'],
        {cls: seconds, 'macro-guide': seconds, **({'cleric-build': seconds} if cls == 'cleric' else {})},
        [(seconds, ['Macro and skill setup', 'マクロとスキル設定', 'Configuración de macro y habilidades', 'Makro und Fertigkeiten einrichten']), (demonstration, ['Skill timing and use', 'スキルのタイミングと使用', 'Ritmo y uso de habilidades', 'Fertigkeiten und Timing'])])

# Preserve all original material. One generic compilation and two explicit TW routes remain internal.
excluded = {'p5UXLn7XDF8': 'Explicit TW Elyos Ranger route; not a Steam route.', 'N_weZCpUbKY': 'Explicit TW Asmodian Ranger route; not a Steam route.', 'ZjkBi0bDIPM': 'Secondary compilation based on other-service research; duplicates stronger first-hand tutorials and adds no verified Steam-specific steps.'}
review = {'checkedAt': '2026-10-06', 'scope': 'Steam AION 2 Global', 'method': 'All 20 collected metadata records, introductions and indexed chapter transcripts reviewed. Selected menu/recipe frames extracted; no claim of full-length playback or exact client-patch provenance. Recommendations concern the named task/chapters, not every claim in a video. Public prose has a separate fact ledger.', 'videos': []}
for id, s in original.items():
    r = next((r for r in records if r['id'] == id), None)
    review['videos'].append({'id': id, 'title': s['title'], 'originalScope': s['region'], 'status': 'recommended-chapters' if r else 'internal-only', 'chapters': [c['seconds'] for c in r['chapters']] if r else [], 'reason': excluded.get(id, 'Relevant first-hand task chapters; current settings and source terminology checked against other collected Steam-targeted tutorials. Region experience elsewhere does not automatically invalidate the selected demonstration.'), 'notAdopted': ['sponsor recommendations', 'universal fastest/best/FPS promises', 'other-service comparisons', 'unconfirmed client limits or future balance predictions']})
for v in review['videos']:
    if v['id'] == 'hAl6c_LwE3M':
        v['notAdopted'] += ['12:03 Wednesday reset assumption', 'Shugo +2/day allowance shown on earlier client', 'first-week calendar deadlines', 'subscription shop quotas']
    if v['id'] == '3Yn91qaBD5s':
        v['notAdopted'] += ['Soul Fuse availability at launch', 'global upgrade caps inferred solely from this prerelease demonstration']
    if v['id'] == 'XYzIx0pYdYo':
        v['notAdopted'] += ['09:29 speculative stigma-slot comparison']

(ROOT / 'src/content/beginner-videos.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
(OUT / 'video-review.json').write_text(json.dumps(review, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
for r in records:
    cover = ROOT / ('public'+r['cover'])
    if not cover.exists():
        subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-ss', str(r['startSeconds']+5), '-i', str(COLLECTION/'videos'/r['id']/'video.mp4'), '-frames:v', '1', '-vf', 'scale=480:270', '-q:v', '3', '-y', str(cover)], check=True)
print(f'Published {len(records)} chapter-linked videos; preserved all {len(original)} sources.')
