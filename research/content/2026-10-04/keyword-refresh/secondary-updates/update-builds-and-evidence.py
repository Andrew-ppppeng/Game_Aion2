from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[5]
CONTENT = ROOT / 'src/content'
LANGS = ['en', 'ja', 'es', 'de']

# Place the generic region instructions before, rather than inside, the EU-only selector.
for lang in LANGS:
    p = CONTENT / lang / 'server.mdx'
    text = p.read_text(encoding='utf-8')
    pattern = r'(<GuideRegion region="eu">\s*)(<h2 id="global-server-regions">.*?)(?=<h2 id="europe-pairings">)'
    text, count = re.subn(pattern, lambda m: m[2] + m[1], text, count=1, flags=re.S)
    assert count == 1, lang
    p.write_text(text, encoding='utf-8')

titles = ['Talent calculator: plan skills with a Global tool', 'タレント計算機：Globalツールでスキルを計画する', 'Calculadora de talentos: planifica habilidades Global', 'Talent-Rechner: Global-Fertigkeiten planen']
bodies = [
'''For an **AION 2 talent calculator**, use a skill planner that matches your region and character progression. The [Global Build Planner](https://aion2.gaming.tools/build-planner) combines gear, skills and Daevanion; its **Skills** tab is the starting point for a skill-point plan.

1. Select your class and faction.
2. Open **Skills** and inspect the displayed skill-point and Stigma budgets.
3. Use **Raise** beside a skill to add a level; **Lower** reverses it. Watch the used-points counter before investing in another skill.
4. Review Active, Passive and Stigma choices separately. Preserve the recovery or defensive skill your role needs.
5. Apply only the levels and options your character can actually use in game.

The plan stays in the current browser and survives a page reload. **Save to My Builds** requires an account for the site's saved-build workflow. Keep a separate copy of your choices before clearing browser data or changing devices. The planner's totals are planning aids; use your character's current tooltips and unlocked slots when applying the plan.

Do not copy a KR/TW allocation into Global just because the class name matches.''',
'''**AION 2のタレント計算機**を探す場合は、自分の地域と成長段階に合うスキル計画ツールを使います。[Global Build Planner](https://aion2.gaming.tools/build-planner)は装備・スキル・Daevanionをまとめて扱い、スキルポイントの計画は**Skills**タブから始めます。

1. クラスと種族を選ぶ。
2. **Skills**を開き、表示されたスキルポイントとStigmaの予算を見る。
3. **Raise**でスキルレベルを上げ、**Lower**で戻す。次のスキルに使う前に消費ポイントを確認する。
4. Active・Passive・Stigmaを分けて確認し、役割に必要な回復や防御を残す。
5. 自分のキャラクターが実際に使えるレベルと選択肢だけをゲーム内に反映する。

計画は現在のブラウザに残り、ページを再読み込みしても保持されます。サイトの保存機能**Save to My Builds**にはアカウントが必要です。ブラウザデータ削除や端末変更前に、選択内容を別にも保存してください。ツールの合計は計画用です。反映するときは現在の説明と解放済み枠を優先します。

同じクラス名でも、KR/TWの配分をそのままGlobalへコピーしないでください。''',
'''Para una **calculadora de talentos de AION 2**, usa un planificador de habilidades de tu región y progresión. [Global Build Planner](https://aion2.gaming.tools/build-planner) reúne equipo, habilidades y Daevanion; empieza en **Skills** para repartir puntos.

1. Selecciona clase y facción.
2. Abre **Skills** y revisa los presupuestos de puntos y Stigma mostrados.
3. Pulsa **Raise** para subir una habilidad y **Lower** para deshacerlo. Comprueba el contador de puntos usados antes de mejorar otra.
4. Revisa Active, Passive y Stigma por separado. Conserva la recuperación o defensa necesaria para tu función.
5. Aplica en el juego solo niveles y opciones disponibles para tu personaje.

El plan permanece en el navegador actual tras recargar la página. **Save to My Builds** requiere una cuenta para el sistema de builds guardadas. Conserva otra copia antes de borrar datos o cambiar de dispositivo. Los totales orientan la planificación; al aplicarlos, manda la descripción actual y las ranuras desbloqueadas de tu personaje.

No copies una distribución KR/TW a Global solo porque coincide el nombre de la clase.''',
'''Wenn du einen **AION-2-Talent-Rechner** suchst, nutze einen Fertigkeitsplaner für deine Region und deinen Fortschritt. Der [Global Build Planner](https://aion2.gaming.tools/build-planner) verbindet Ausrüstung, Fertigkeiten und Daevanion; im Reiter **Skills** planst du Fertigkeitspunkte.

1. Klasse und Fraktion wählen.
2. **Skills** öffnen und angezeigte Fertigkeits- und Stigma-Budgets prüfen.
3. Mit **Raise** eine Fertigkeitsstufe erhöhen, mit **Lower** zurücknehmen. Vor weiteren Aufwertungen verbrauchte Punkte prüfen.
4. Active, Passive und Stigma getrennt prüfen. Benötigte Heilung oder Verteidigung für deine Rolle erhalten.
5. Im Spiel nur Stufen und Optionen übernehmen, die dein Charakter tatsächlich nutzen kann.

Der Plan bleibt im aktuellen Browser und übersteht ein Neuladen. **Save to My Builds** benötigt ein Konto für gespeicherte Builds. Sichere deine Auswahl zusätzlich vor dem Löschen von Browserdaten oder Gerätewechseln. Die Summen dienen der Planung; beim Umsetzen gelten die aktuellen Tooltips und freigeschalteten Plätze deines Charakters.

Übernimm keine KR/TW-Verteilung für Global allein wegen desselben Klassennamens.'''
]

intro_replacements = [
'''[Aion2Hub’s Cleric directory](https://aion2hub.com/builds/cleric/) separates Global Launch Scale Test examples from KR/TW builds. KR/TW equipment, stats and Gear Scores are not valid for Global; a test-client example may also differ from launch. Choose an example for your service and compare it with your available skills before applying it.''',
'''[Aion2Hubのクレリック一覧](https://aion2hub.com/builds/cleric/)はGlobal Launch Scale TestとKR/TWのビルドを分けています。KR/TWの装備・数値・Gear ScoreはGlobal用ではなく、テスト版の例も開始後とは異なる場合があります。自分のサービスに合う例を選び、使えるスキルと比較してください。''',
'''El [directorio de Clérigo de Aion2Hub](https://aion2hub.com/builds/cleric/) separa ejemplos Global Launch Scale Test de builds KR/TW. Equipo, estadísticas y Gear Scores KR/TW no son válidos para Global; un ejemplo del cliente de prueba también puede cambiar. Elige tu servicio y compara las habilidades disponibles antes de copiarlo.''',
'''[Aion2Hubs Kleriker-Verzeichnis](https://aion2hub.com/builds/cleric/) trennt Global-Launch-Scale-Test-Beispiele von KR/TW-Builds. KR/TW-Ausrüstung, Werte und Gear Scores gelten nicht für Global; auch Testclient-Beispiele können vom Start abweichen. Wähle deinen Dienst und vergleiche verfügbare Fertigkeiten vor dem Übernehmen.'''
]

metas = [
 ('AION 2 Builds: Skills, Stigmas and Talent Planner', 'Plan AION 2 skill points with a Global calculator, choose skill options and Stigmas, save your setup, and test practical class attack loops.', 'Build a setup for your region, role and unlocked skills. Use a Global skill planner for point allocation, then test the actual choices and attack loop in game.', 'Choose skills and Stigmas for your activity, select unlocked specialization options and practice the loop manually. Use the Global Build Planner Skills tab to budget points with Raise/Lower; its local plan stays in your browser.'),
 ('AION 2 ビルド：スキル・Stigma・計画ツール', 'Global計算機でAION 2のスキルポイントを配分し、選択肢・Stigma・実用的な攻撃ループを確認。', '地域・役割・解放済みスキルに合わせて構成します。Globalスキル計画ツールでポイントを配分し、実際の選択と攻撃ループをゲームで試しましょう。', '活動に合うスキルとStigmaを選び、解放済み専門化を設定して手動でループを練習。Global Build PlannerのSkillsでRaise/Lowerを使ってポイントを計画し、現在のブラウザに保持できます。'),
 ('Builds AION 2: habilidades, Stigmas y calculadora', 'Reparte puntos de AION 2 con una calculadora Global, elige opciones y Stigmas, guarda la configuración y prueba ciclos de ataque útiles.', 'Adapta la build a región, función y habilidades disponibles. Planifica puntos con una herramienta Global y prueba la selección y el ciclo en el juego.', 'Elige habilidades y Stigmas para tu actividad y activa especializaciones desbloqueadas. Practica el ciclo a mano; usa Skills en Global Build Planner con Raise/Lower para presupuestar puntos. El plan local queda en el navegador.'),
 ('AION 2 Builds: Fertigkeiten, Stigmas und Planer', 'Plane AION-2-Fertigkeitspunkte mit einem Global-Rechner, wähle Optionen und Stigmas, sichere den Aufbau und teste Klassen-Angriffsfolgen.', 'Stimme Region, Rolle und freigeschaltete Fertigkeiten ab. Verteile Punkte mit einem Global-Planer und teste Auswahl und Angriffsfolge im Spiel.', 'Wähle Fertigkeiten und Stigmas passend zur Aktivität, aktiviere freigeschaltete Optionen und übe manuell. Im Global Build Planner budgetierst du unter Skills mit Raise/Lower; der lokale Plan bleibt im Browser.'),
]

for i, lang in enumerate(LANGS):
    p = CONTENT / lang / 'builds.mdx'
    text = p.read_text(encoding='utf-8')
    marker = '<h2 id="save-and-improve-your-build">'
    assert marker in text and 'id="talent-calculator"' not in text
    section = f'<h2 id="talent-calculator">{titles[i]}</h2>\n\n{bodies[i]}\n\n'
    text = text.replace(marker, section + marker, 1)
    pattern = r'(<h2 id="save-and-improve-your-build">.*?</h2>\s*)[^\n]+codexgames[^\n]+\n'
    text, count = re.subn(pattern, lambda m: m[1] + intro_replacements[i] + '\n', text, count=1, flags=re.S)
    assert count == 1, lang
    p.write_text(text, encoding='utf-8')
    p = CONTENT / lang / 'builds.json'
    meta = json.loads(p.read_text(encoding='utf-8'))
    index = next(n for n, item in enumerate(meta['toc']) if item['id'] == 'save-and-improve-your-build')
    meta['toc'].insert(index, {'id': 'talent-calculator', 'title': titles[i]})
    for key, value in zip(['title', 'description', 'summary', 'quickAnswer'], metas[i]):
        meta[key] = value
    p.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

faq_source = {'id': 'steam-launch-faq-20261001', 'title': 'Launch FAQ', 'url': 'https://store.steampowered.com/news/app/3393110?emclan=103582791475596239&emgid=680761758839734961', 'kind': 'official', 'region': 'Global', 'publishedAt': '2026-10-01', 'version': 'Official Steam community announcement read via ISteamNews/GetNewsForApp on 2026-10-04; Windows-only official support; controller playable but not supported; regions and same-launcher account rules'}
queue_source = {'id': 'steam-test-close-queue-policy', 'title': "Launch Scale Test Comes to a Close: What's Next?", 'url': 'https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844115010496396', 'kind': 'official', 'region': 'Global', 'publishedAt': '2026-09-19', 'version': 'Steam official feed read 2026-10-04; member queue priority not guaranteed entry, direct player item trade disabled'}
cosmetic_source = {'id': '6ac1229d5657e135c2f5ef65', 'title': "Founder's Packs Cosmetics Soon Available On All Characters", 'url': 'https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac1229d5657e135c2f5ef65', 'kind': 'official', 'region': 'Global', 'publishedAt': '2026-10-03', 'version': 'Updated 2026-10-03T18:18:43Z, checked 2026-10-04; implementation pending after Advanced Access; membership and consumable chests remain one-time'}
community_source = {'id': 'aion2-community-discord-live', 'title': 'AION 2 Community Discord', 'url': 'https://discord.gg/AION2', 'kind': 'community', 'region': 'Mixed', 'publishedAt': None, 'version': 'Public Discord invite resolved 2026-10-04 to guild 1377004046832894095 AION 2 Community; community-run, not Global official server; no private messages read'}
planner_source = {'id': 'global-skill-planner-ui', 'title': 'Global Build Planner', 'url': 'https://aion2.gaming.tools/build-planner', 'kind': 'tool', 'region': 'Global', 'publishedAt': None, 'version': 'Global client 1.0.21.0 updated October 1; browser tested 2026-10-04 Gladiator Skills Raise Keen Strike 1→2 with 1/203 points, reload persistence, Lower reversal; login/save/share not executed; budgets are tool calculations'}

by_slug = {
 'map': [], 'gathering': [],
 'server': [faq_source, queue_source],
 'steam': [faq_source],
 'guide': [faq_source, community_source],
 'monetization': [faq_source, queue_source, cosmetic_source],
 'builds': [planner_source],
}
for slug, sources in by_slug.items():
    p = CONTENT / 'article-data' / f'{slug}.json'
    data = json.loads(p.read_text(encoding='utf-8'))
    data['checkedAt'] = '2026-10-04'
    data['revision'] = '2026-10-04.keyword-refresh-1'
    old_ids = {source['id'] for source in data['sources']}
    assert not old_ids.intersection(source['id'] for source in sources)
    data['sources'].extend(sources)
    if slug == 'map':
        for source in data['sources']:
            if source['id'] == 'voxel-map':
                source['version'] = 'Current public UI read 2026-10-04; Global/TW map-card limits, Enter search, Alt lens, Floor slice and PgUp/PgDn, F completion, browser-local Export progress / Import controls; import round-trip not executed'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

print('Updated builds and evidence; moved generic Global selection outside EU-only component.')
