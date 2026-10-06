"""One-time targeted supplements, source ledger and UI figures."""
import json
import shutil
from pathlib import Path
from PIL import Image
from author_articles import ROOT, LOCALES

OUT = Path(__file__).parent
def write_json(p, d):
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

gather_sections = [
 ('start-gathering', ['Gather materials for your first recipe','最初の配方に必要な素材','Recolecta para tu primera receta','Materialien für das erste Rezept sammeln'], [
 'For one [Orichalcum Longsword attempt](/crafting#prepare-a-batch), gather **6 Orichalcum Ore and 2 Odyle**; buy **3 Orichalcum Solvent (Bound)** and obtain **5 Refining Stones** from monster drops. This covers three Ingots and one sword attempt before failures. Ore and Odyle are different node filters.',
 '[Orichalcum Longsword 1回](/crafting#prepare-a-batch)には**Orichalcum Ore 6、Odyle 2**を採集し、**Orichalcum Solvent (Bound) 3**を買い、モンスターから**Refining Stone 5**を集めます。失敗分を除くIngot 3と剣1回の素材です。鉱石とOdyleは地図の別フィルターです。',
 'Para un [intento de Orichalcum Longsword](/crafting#prepare-a-batch), recoge **6 Orichalcum Ore y 2 Odyle**, compra **3 Orichalcum Solvent (Bound)** y consigue **5 Refining Stones** de monstruos. Cubre tres lingotes y una espada antes de fallos. Ore y Odyle usan filtros distintos.',
 'Für einen [Orichalcum-Longsword-Versuch](/crafting#prepare-a-batch) **6 Orichalcum Ore und 2 Odyle** sammeln, **3 Orichalcum Solvent (Bound)** kaufen und **5 Refining Stones** aus Monsterbeute holen. Das reicht vor Fehlschlägen für drei Barren und ein Schwert. Erz und Odyle haben getrennte Filter.']),
 ('experience-specialization', ['Gathering proficiency and skill points','採集熟練度とスキルポイント','Competencia y puntos de recolección','Sammelfertigkeit und Fertigkeitspunkte'], [
 'The game calls gathering **Essence Extraction**. Its Success and Failure gauges race to fill; **Item Extraction** instead consumes equipment. Crafting profession levels are separate.\n\nFor a beginner gathering allocation, start with **Proficient Handling 10 / Delicate Touch 10 / Lady Luck 5** once enough points are available: success and reduced failure come before the occasional bonus. This is a starter allocation, not a guarantee of every attempt. Specialize in **Odyle** plus the resource used by your first craft: **ore** for Blacksmithing, or the relevant **gems/logs** for Handicrafting.',
 '採集は**Essence Extraction**で、SuccessとFailureのゲージが競争します。**Item Extraction**は装備消費で、製作職業レベルも別です。\n\nポイントが足りれば初期配分の目安は**Proficient Handling 10 / Delicate Touch 10 / Lady Luck 5**。偶発的なボーナスより成功と失敗抑制を優先し、毎回成功を保証する配分ではありません。**Odyle**と最初の製作資源に特化：Blacksmithingは**鉱石**、Handicraftingは対象配方の**宝石・木材**です。',
 'La recolección es **Essence Extraction**: compiten medidores Success y Failure. **Item Extraction** consume equipo y los niveles de oficio son separados.\n\nCon puntos suficientes, empieza con **Proficient Handling 10 / Delicate Touch 10 / Lady Luck 5**: prioriza éxito y menor fallo sobre premios ocasionales. No garantiza cada intento. Especializa **Odyle** y el recurso del primer oficio: **mena** para Blacksmithing o **gemas/madera** para Handicrafting.',
 'Sammeln heißt **Essence Extraction**; Success- und Failure-Balken füllen sich gegeneinander. **Item Extraction** verbraucht Ausrüstung; Handwerksstufen sind getrennt.\n\nBei genug Punkten ist **Proficient Handling 10 / Delicate Touch 10 / Lady Luck 5** eine Startverteilung: Erfolg und weniger Fehlschläge vor gelegentlichen Boni. Sie garantiert keine Versuche. Spezialisiere **Odyle** und dein Handwerksmaterial: **Erz** für Blacksmithing oder passende **Edelsteine/Holz** für Handicrafting.']),
 ('gathering-routes', ['Two routes with a concrete purpose','目的を決めた2つの採集ルート','Dos rutas con un objetivo concreto','Zwei Routen mit klarem Zweck'], [
 '**Recipe route:** open [Aion2T map](https://aion2t.com/map), choose your faction zone and enable **Orichalcum** and **Odyle** markers. Gather the ore on your current quest path; extract Odyle when passing its aerial nodes or after a Conquest boss. Turn ore into Ingots only after obtaining Solvent.\n\n**Asmodian promotion route:** at **Novice 50**, visit **Alzirr in Safe Haven**, then gather **Ruby nodes in Calderon Canyon** for **Splendent Ruby (Bound)**. Turn in that quest item to advance the stage. **Radiant Ruby Gemstone** is a crafting material and cannot replace it. Use [map height layers](/map) when a node is on a cliff or inside a cave.',
 '**配方ルート**：[Aion2Tマップ](https://aion2t.com/map)で陣営の地域を選び**Orichalcum**と**Odyle**を表示。クエスト経路の鉱石を採り、空中ノードやConquestボス後にOdyleを抽出。Solventを入手してからIngotにします。\n\n**魔族の昇級ルート**：**Novice 50**で**Safe HavenのAlzirr**へ。**Calderon CanyonのRubyノード**で**Splendent Ruby (Bound)**を採って報告します。**Radiant Ruby Gemstone**は製作素材で代用できません。崖や洞窟のノードには[地図の高さレイヤー](/map)を使います。',
 '**Ruta de receta:** en [Aion2T](https://aion2t.com/map), elige zona y activa **Orichalcum** y **Odyle**. Recoge mena en el camino de misiones y extrae Odyle de nodos aéreos o tras un jefe Conquest. Refina cuando tengas Solvent.\n\n**Promoción Asmodian:** en **Novice 50**, habla con **Alzirr en Safe Haven** y recoge **Ruby en Calderon Canyon** hasta obtener **Splendent Ruby (Bound)**. Entrégalo para avanzar. **Radiant Ruby Gemstone** es material de fabricación y no sirve. Usa [capas de altura](/map) para cuevas y riscos.',
 '**Rezeptroute:** auf der [Aion2T-Karte](https://aion2t.com/map) Fraktionsgebiet wählen und **Orichalcum-/Odyle**-Marker aktivieren. Erz am Questweg sammeln; Odyle an Luftvorkommen oder nach einem Conquest-Boss extrahieren. Erst mit Solvent zu Barren verarbeiten.\n\n**Asmodier-Aufstieg:** auf **Novice 50** zu **Alzirr in Safe Haven**, dann **Ruby-Vorkommen in Calderon Canyon** für **Splendent Ruby (Bound)** sammeln und abgeben. **Radiant Ruby Gemstone** ist Handwerksmaterial und kein Ersatz. Für Höhlen und Klippen [Höhenebenen](/map) nutzen.']),
 ('route-results', ['Fix the gathering block','採集が止まる原因','Resuelve el bloqueo de recolección','Sammelhürden lösen'], [
 '**Proficiency stops at 50:** complete the promotion, rather than grinding more ordinary nodes. **Repeated failures:** improve Proficient Handling/Delicate Touch and use nodes within your proficiency. **Wrong material grade:** Fine and Pure recipes need those exact grades, not more plain Ore. **Missing node:** move to the next marked location; the map marks possible locations, not guaranteed live spawns.',
 '**50で熟練度が止まる**：通常ノードを続けず昇級クエストへ。**失敗が多い**：Proficient HandlingとDelicate Touchを上げ、熟練度に合うノードを使います。**品質違い**：FineやPureはその品質が必要で、通常Oreの増量では代用不可。**ノードがない**：次のマーカーへ。地図は候補位置で、現時点の出現保証ではありません。',
 '**Se detiene en 50:** completa promoción. **Fallos frecuentes:** mejora Proficient Handling/Delicate Touch y usa nodos de tu competencia. **Calidad incorrecta:** Fine/Pure necesitan esa calidad, no más mena normal. **Nodo ausente:** ve al siguiente marcador; son ubicaciones posibles, no apariciones garantizadas.',
 '**Fertigkeit stoppt auf 50:** Aufstiegsquest abschließen. **Viele Fehlschläge:** Proficient Handling/Delicate Touch erhöhen und passende Vorkommen nutzen. **Falsche Qualität:** Fine/Pure brauchen diese Qualität statt mehr normalem Erz. **Vorkommen fehlt:** zum nächsten Marker; Karten zeigen mögliche, keine garantierten aktuellen Vorkommen.'])]

macro_sections = [
 ('bind-and-open', ['Create one working macro','動くマクロを1つ作る','Crea una macro funcional','Ein funktionierendes Makro erstellen'], [
 '1. Open **Key Settings → General → Gameplay** and bind the ability-macro activation key; **Q** is one option after moving its previous action.\n2. Open the skill menu’s **ability-macro editor** and add a macro.\n3. Select the **hotbar chain/stack**, not just the skill icon currently showing in that slot.\n4. Hold the activation key to run the selected stack; release it to stop.\n\n<GuideVisual id="macro-global-keybind" />\n\n<GuideVisual id="macro-global-editor" />',
 '1. **Key Settings → General → Gameplay**でマクロキーを設定。**Q**を使う場合は元の操作を移します。\n2. スキル画面の**ability-macro editor**でマクロを追加。\n3. 表示中の1スキルではなく**ホットバーの連鎖・スタック**を選びます。\n4. キーを押している間に実行し、離して停止します。\n\n<GuideVisual id="macro-global-keybind" />\n\n<GuideVisual id="macro-global-editor" />',
 '1. En **Key Settings → General → Gameplay**, asigna la tecla de macro; **Q** sirve si mueves su acción anterior.\n2. Abre **ability-macro editor** en habilidades y añade una macro.\n3. Selecciona la **cadena/pila de la barra**, no solo el icono visible.\n4. Mantén la tecla para ejecutar y suéltala para parar.\n\n<GuideVisual id="macro-global-keybind" />\n\n<GuideVisual id="macro-global-editor" />',
 '1. Unter **Key Settings → General → Gameplay** Aktivierungstaste belegen; **Q** ist nach Verschieben der bisherigen Aktion möglich.\n2. Im Fertigkeitsmenü **ability-macro editor** öffnen und Makro hinzufügen.\n3. Die **Hotbar-Kette/den Stapel** wählen, nicht nur das sichtbare Fertigkeitssymbol.\n4. Taste für Ausführung halten, zum Stoppen loslassen.\n\n<GuideVisual id="macro-global-keybind" />\n\n<GuideVisual id="macro-global-editor" />']),
 ('priority-stack', ['Skill priority and a Ranger example','優先順と弓星の例','Prioridad y ejemplo Ranger','Priorität und Ranger-Beispiel'], [
 'The stack checks the **bottom skill first**. A cooldown-free attack at the bottom can occupy the stack and stop upper entries from firing. Keep conditional follow-ups above your ordinary filler unless their prerequisite is ready.\n\nFor [Ranger](/ranger#manual-loop), the useful sequence is **Marking Shot → Precision → Suppressing Arrow**, with **Snipe** supplying MP between attacks. **Drill Dart** needs a critical hit; **Burst Arrow** needs Slow or Root. A macro cannot create those prerequisites. Put a ready follow-up ahead of the filler, and keep target-control skills separate.',
 'スタックは**一番下を先に**判定。最下段のクールダウンなし攻撃が上のスキルを妨げる場合があります。条件が未成立の追撃は通常攻撃の埋め技と区別します。\n\n[弓星](/ranger#manual-loop)は**Marking Shot → Precision → Suppressing Arrow**、間に**Snipe**でMP回復。**Drill Dart**はクリティカル、**Burst Arrow**はSlowかRootが必要で、マクロは条件を作れません。使用可能な追撃を埋め技より優先し、対象を制御するスキルは別キーにします。',
 'La pila revisa **primero la habilidad inferior**. Un ataque sin enfriamiento abajo puede impedir las superiores. Distingue continuaciones condicionales del relleno.\n\nEn [Ranger](/ranger#manual-loop), usa **Marking Shot → Precision → Suppressing Arrow**, con **Snipe** para MP. **Drill Dart** exige crítico y **Burst Arrow** Slow o Root. La macro no crea requisitos. Prioriza la continuación disponible sobre relleno y deja control de objetivos separado.',
 'Der Stapel prüft die **unterste Fertigkeit zuerst**. Ein Angriff ohne Abklingzeit unten kann obere Einträge verdrängen. Bedingte Folgeangriffe von Füllern trennen.\n\nBeim [Ranger](/ranger#manual-loop): **Marking Shot → Precision → Suppressing Arrow**, dazwischen **Snipe** für MP. **Drill Dart** braucht einen kritischen Treffer, **Burst Arrow** Slow oder Root. Das Makro erzeugt diese Bedingungen nicht. Bereite Folgeangriffe vor Füllern priorisieren und Zielkontrolle separat halten.']),
 ('manual-actions', ['Class actions to keep on direct keys','職業ごとに直接キーへ残す操作','Acciones por clase en teclas directas','Klassenaktionen auf direkten Tasten'], [
 '''| Class | Direct action and condition |
| --- | --- |
| [Assassin](/assassin#manual-loop) | Insignia Explosion after **five Insignias**; movement to the back only when safe |
| [Spiritmaster](/spiritmaster#summon-sequence) | Elemental Fusion at **Four Elements**; choose Water for MP or Wind for HP |
| [Ranger](/ranger#manual-loop) | Traps, escape and charged Deadshot when a safe cast window exists |
| [Cleric](/cleric#manual-loop) | Healing, cleanse and resurrection; stop damage for urgent recovery |

Keep dodge/block and interrupt outside the damage stack for every class.''',
 '''| 職業 | 直接操作と条件 |
| --- | --- |
| [殺星](/assassin#manual-loop) | **Insignia 5**でInsignia Explosion。安全なときだけ背後へ移動 |
| [精霊星](/spiritmaster#summon-sequence) | **Four Elements**でElemental Fusion。MPはWater、HPはWind |
| [弓星](/ranger#manual-loop) | 罠、離脱、安全な詠唱時間のDeadshot |
| [治癒星](/cleric#manual-loop) | 回復、解除、蘇生。緊急時は攻撃を止める |

全職業で回避・防御・中断を攻撃スタックとは別に残します。''',
 '''| Clase | Acción directa y condición |
| --- | --- |
| [Assassin](/assassin#manual-loop) | Insignia Explosion con **cinco Insignias**; ve detrás solo si es seguro |
| [Spiritmaster](/spiritmaster#summon-sequence) | Elemental Fusion con **Four Elements**; Water para MP, Wind para HP |
| [Ranger](/ranger#manual-loop) | Trampas, escape y Deadshot con ventana segura |
| [Cleric](/cleric#manual-loop) | Curación, limpieza y resurrección; detén daño para emergencias |

Deja esquiva/bloqueo e interrupción fuera de la pila de daño.''',
 '''| Klasse | Direkte Aktion und Bedingung |
| --- | --- |
| [Assassine](/assassin#manual-loop) | Insignia Explosion bei **fünf Insignias**; nur sicher hinter das Ziel bewegen |
| [Beschwörer](/spiritmaster#summon-sequence) | Elemental Fusion bei **Four Elements**; Water für MP, Wind für HP |
| [Ranger](/ranger#manual-loop) | Fallen, Flucht und Deadshot in sicheren Wirkfenstern |
| [Kleriker](/cleric#manual-loop) | Heilung, Reinigung, Wiederbelebung; Schaden bei Notfällen stoppen |

Ausweichen/Blocken und Unterbrechen außerhalb des Schadensstapels halten.''']),
 ('delay-and-basic-attack', ['Macro delay: a starting value','マクロ遅延の初期値','Retardo de macro: valor inicial','Makroverzögerung: Startwert'], [
 'If the editor exposes delay, **50 ms** is a conservative starting value. With stable low latency, **10 ms** is an option to try; a shorter delay is useful only if the intended attacks still fire. Watch one full cooldown cycle: if a ready entry is skipped, raise delay before changing skill priorities. Keep the MP-restoring basic attack available rather than replacing it with a chain that drains MP.',
 '遅延を設定できる場合、初期値の目安は**50 ms**。安定した低遅延なら**10 ms**も候補ですが、予定の攻撃が出ることが条件です。1周期で使用可能スキルが飛ばされるなら、優先順を変える前に遅延を増やします。MP回復の通常攻撃は残し、消費だけの連鎖に置き換えません。',
 'Si el editor permite retardo, **50 ms** es un inicio conservador. Con latencia baja y estable puedes probar **10 ms**, si todos los ataques siguen ejecutándose. Observa un ciclo: si omite una habilidad lista, sube retardo antes de cambiar prioridades. Conserva el ataque básico que recupera MP.',
 'Wenn der Editor Verzögerung anbietet, sind **50 ms** ein vorsichtiger Start. Bei stabiler niedriger Latenz sind **10 ms** eine Option, solange alle gewünschten Angriffe auslösen. Überspringt ein voller Zyklus einen bereiten Eintrag, zuerst die Verzögerung erhöhen. MP-wiederherstellenden Grundangriff verfügbar halten.']),
 ('debug-one-stack', ['Fix a macro that does not work','動かないマクロの対処','Arregla una macro que falla','Ein fehlerhaftes Makro korrigieren'], [
 '**Nothing fires:** activation binding and chosen hotbar chain. **Only the filler repeats:** bottom-first priority. **Follow-up missing:** cooldown, MP, range or its required status/critical proc. **Character runs forward:** turn pursuit off in [settings](/settings). For the four class walkthroughs, use the Class supplements filter in the [video library](/beginner-videos).',
 '**何も出ない**：起動キーと選んだホットバー連鎖。**埋め技だけ**：最下段優先。**追撃がない**：クールダウン、MP、距離、状態・クリティカル条件。**前へ走る**：[設定](/settings)で追撃OFF。4職業の実演は[動画一覧](/beginner-videos)の職業別フィルターへ。',
 '**Nada se activa:** tecla y cadena seleccionada. **Solo relleno:** prioridad inferior. **Falta continuación:** enfriamiento, MP, alcance o estado/crítico. **Corres hacia delante:** desactiva persecución en [ajustes](/settings). Los cuatro ejemplos están en el filtro de clases de [vídeos](/beginner-videos).',
 '**Nichts löst aus:** Aktivierungstaste und gewählte Hotbar-Kette. **Nur Füller:** unterste Priorität. **Folgeangriff fehlt:** Abklingzeit, MP, Reichweite oder Zustand/kritischer Proc. **Charakter läuft vor:** Verfolgung in [Einstellungen](/settings) aus. Vier Klassenbeispiele im Klassenfilter der [Videothek](/beginner-videos).']),
 ('built-in-and-policy', ['Use the built-in editor','ゲーム内エディターを使う','Usa el editor integrado','Den eingebauten Editor nutzen'], [
 'These steps use the game’s own editor. NC’s operation policy sanctions programs or devices that circumvent protection or interfere with normal operation. For accessibility arrangements beyond built-in controls, consult NC support and its current policy.',
 'ここではゲーム内エディターを使います。保護を回避したり通常動作を妨げたりするプログラム・装置はNCの運営規約で制裁対象です。標準操作以外のアクセシビリティはNCサポートと現在の規約に確認します。',
 'Estos pasos usan el editor del juego. NC sanciona programas o dispositivos que eluden protección o interfieren con funcionamiento normal. Para accesibilidad fuera de controles integrados, consulta soporte y la política vigente.',
 'Diese Schritte nutzen den Spieleeditor. NC sanktioniert Programme oder Geräte, die Schutz umgehen oder normalen Betrieb stören. Für Barrierefreiheit außerhalb eingebauter Steuerung NC-Support und aktuelle Richtlinie konsultieren.'])]

for slug, sections, next_slug in [('gathering', gather_sections, 'crafting'), ('macro-guide', macro_sections, 'builds')]:
    for i, locale in enumerate(LOCALES):
        p = ROOT / f'src/content/{locale}/{slug}.json'
        m = json.loads(p.read_text(encoding='utf-8'))
        m['toc'] = [{'id': id, 'title': h[i]} for id,h,b in sections]
        # Preserve the macro's actual UI figures; remove generic workflow padding.
        m['visuals'] = {k:v for k,v in m['visuals'].items() if k.startswith('macro-global')} if slug == 'macro-guide' else {'workflow': {
            'title': ['First sword material route','最初の剣の素材ルート','Ruta de materiales de la primera espada','Materialroute für das erste Schwert'][i],
            'caption': ['Materials for one attempt before failed crafts.','失敗分を除く1回の素材。','Materiales por intento antes de fallos.','Materialien je Versuch vor Fehlschlägen.'][i],
            'steps': [dict(label='Orichalcum Ore ×6',description=['Gather ore nodes.','鉱石ノードから採集。','Recoge nodos de mena.','Erzvorkommen sammeln.'][i]),dict(label='Odyle ×2',description=['Extract Odyle nodes.','Odyleノードを抽出。','Extrae nodos Odyle.','Odyle-Vorkommen extrahieren.'][i]),dict(label='Solvent ×3 + Refining Stone ×5',description=['Buy Solvent and collect monster-drop stones.','Solvent購入とモンスタードロップの石。','Compra Solvent y consigue piedras de monstruos.','Solvent kaufen und Steine aus Monsterbeute holen.'][i])]}}
        m['summary'] = [b[0] for _,_,b in sections][0] if locale == 'en' else sections[0][2][i]
        m['summary'] = m['summary'].split('\n')[0]
        m['description'] = sections[0][1][i] + ': ' + (['material quantities, promotion and resource routes.','素材数、昇級、資源ルート。','cantidades, promoción y rutas.','Mengen, Aufstieg und Ressourcenrouten.'][i] if slug=='gathering' else ['bindings, chain priority and class conditions.','キー、連鎖の優先順、職業条件。','teclas, prioridad y condiciones de clase.','Tasten, Kettenpriorität und Klassenbedingungen.'][i])
        m['quickAnswer'] = sections[1][2][i].split('\n')[0]
        m['inlineNext'] = [next_slug]
        body = '\n\n'.join(f'<h2 id="{id}">{h[i]}</h2>\n\n{b[i]}' for id,h,b in sections)
        if slug == 'gathering': body += '\n\n<GuideVisual id="workflow" />'
        body += f'\n\n<GuideNext slug="{next_slug}" />\n'
        p.with_suffix('.mdx').write_text(body, encoding='utf-8')
        write_json(p,m)

assets_path = ROOT/'src/content/guide-assets.json'
assets = json.loads(assets_path.read_text(encoding='utf-8'))
figures = [
 ('crafting','recipe','Iqi6pR8r6FY',390,(320,0,1280,580),'craft-orichalcum-ingot',['Orichalcum Ingot recipe: 2 Ore and 1 Solvent.','Orichalcum Ingot配方：Ore 2とSolvent 1。','Receta Orichalcum Ingot: 2 Ore y 1 Solvent.','Orichalcum-Ingot-Rezept: 2 Ore und 1 Solvent.']),
 ('gear-progression','belt','OFA-92_9S6w',250,None,'gear-noble-belt-morph',['Blue Noble Belt recipe with a green +10 belt input.','緑+10のベルトを使う青Noble Belt配方。','Receta del Noble Belt azul con cinturón verde +10.','Blauer Noble Belt mit grünem +10-Gürtel als Zutat.']),
 ('settings','controls','0KJtQApx_o4',105,None,'settings-combat-controls',['Combat controls including target pursuit and automatic targeting.','ターゲット追撃と自動選択を含む戦闘設定。','Controles con persecución y selección automática.','Kampfoptionen mit Verfolgung und automatischer Zielwahl.'])]
for slug, visual, video, seconds, crop, id, captions in figures:
    im = Image.open(OUT/f'{video}-{seconds}.jpg')
    if crop: im = im.crop(crop)
    dest = ROOT/f'public/media/guides/{id}.webp'
    im.save(dest,quality=88)
    if not any(a['id']==id for a in assets):
        assets.append({'id':id,'src':f'/media/guides/{id}.webp','width':im.width,'height':im.height,'sourceUrl':f'https://www.youtube.com/watch?v={video}&t={seconds}s','originalUrl':f'https://www.youtube.com/watch?v={video}','publisher':json.loads((ROOT/f'research/youtube/2026-10-06-beginner-guides/metadata/{video}.json').read_text(encoding='utf-8')).get('channel','Player tutorial'),'region':'Global','version':'Collected October 2026 tutorial; selected task frame and menu text reviewed; exact client patch not independently established.','checkedAt':'2026-10-06'})
    for i,locale in enumerate(LOCALES):
        p=ROOT/f'src/content/{locale}/{slug}.json';m=json.loads(p.read_text(encoding='utf-8'))
        m['visuals'][visual]={'assetId':id,'alt':captions[i],'caption':captions[i]};write_json(p,m)
        p=p.with_suffix('.mdx');body=p.read_text(encoding='utf-8')
        heading={'crafting':'prepare-a-batch','gear-progression':'belt-and-amulet','settings':'targeting-and-pursuit'}[slug]
        start=body.index(f'<h2 id="{heading}"');end=body.find('\n\n<h2',start)
        if end<0:end=body.index('\n\n<GuideVisual id="workflow"',start)
        body=body[:end]+f'\n\n<GuideVisual id="{visual}" />'+body[end:];p.write_text(body,encoding='utf-8')
write_json(assets_path,assets)

source_map={'settings':['0KJtQApx_o4','Ei17ATvSLGM','VO6Ym4iHmJ0'], 'crafting':['Iqi6pR8r6FY','J8WVY3FxPQM'], 'gear-progression':['J8WVY3FxPQM','OFA-92_9S6w','3Yn91qaBD5s'], 'daily-weekly-checklist':['hAl6c_LwE3M','A0hpQaWDYgs'], 'guide':['Ei17ATvSLGM','A0hpQaWDYgs','OFA-92_9S6w'], 'leveling':['A0hpQaWDYgs','VO6Ym4iHmJ0'], 'gathering':['Iqi6pR8r6FY'], 'macro-guide':['njRrjTJCENU','E29vReeuSNo','NdsTPYuL6E4','YeHM0TzzZ4s']}
for slug,ids in source_map.items():
    p=ROOT/f'src/content/article-data/{slug}.json';d=json.loads(p.read_text(encoding='utf-8'))
    for id in ids:
        sid=f'tutorial-{id}'
        if not any(s['id']==sid for s in d['sources']):
            raw=json.loads((ROOT/f'research/youtube/2026-10-06-beginner-guides/metadata/{id}.json').read_text(encoding='utf-8'))
            d['sources'].append({'id':sid,'title':raw['title'],'url':f'https://www.youtube.com/watch?v={id}','kind':'player','region':'Global','publishedAt':f"{raw['upload_date'][:4]}-{raw['upload_date'][4:6]}-{raw['upload_date'][6:8]}" if '-' not in raw['upload_date'] else raw['upload_date'],'version':'Selected task chapters and UI reviewed; provenance, conflicts and limits in beginner-depth/fact-ledger.json. Not an endorsement of all video claims.'})
    d.update(checkedAt='2026-10-06',revision='2026-10-06.beginner-depth-2');write_json(p,d)
print('Eight topics completed in four languages; three UI figures and source records added.')
