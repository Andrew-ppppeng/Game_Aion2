import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
identities=json.loads((ROOT/'src/content/class-identities.json').read_text(encoding='utf8'))
order=[x['id'] for x in identities]
copy={}
copy['en']={
'title':'AION 2 Builds: Eight Class Loops, Skills and Stigmas',
'description':'Compare starting builds for all eight classes. Learn skill-rank thresholds, Stigma swaps, manual combat loops, Daevanion priorities and build-planner steps.',
'summary':'Choose a class loop, budget the skill ranks and Stigma slots you have, then improve the missing resource, trigger or party tool.',
'answer':'Start with MP recovery, the attacks that open your class follow-ups and the defense or healing your role needs. Select unlocked specializations, equip Stigmas within your slots and practice the loop manually before adding a repeating combo.',
'headings':['Choose a starting build for any class','Match skill ranks to your progression','Skills, Stigmas, Daevanion and equipment','Eight starting combat loops','Keep reactions outside the damage chain','Use the skill build planner','Save a setup and fix its weak point'],
'table':['Class guide','Core build decision','First useful upgrade'],
'rows':[
('MP sustain and frontline damage; preserve block when tanking','Keen Strike MP recovery, then its Ruinous Blow cooldown option'),
('Judgment triggers, threat and shield timing','Vicious Strike → Warding Strike and Pummel → Punishment cooldown options'),
('Back attacks and target-bound Insignia stacks','Quick Slice sustain and Insignia Explosion cooldown; Heart Gore for critical windows'),
('Range, critical follow-ups and Deadshot availability','Snipe MP recovery and on-hit Deadshot cooldown reduction'),
('Dark Crush windows plus party mantras','Spinning Strike cooldown and Dark Crush options; add recovery for healer duty'),
('Automatic direct healing, cleanse and safe damage','Radiant Recovery choices and Condemnation’s critical reset when damage is sustainable'),
('Completed charges and mana-dependent passives','Firestorm → Hellfire and Ice Chain → Winter’s Shackles cooldown options'),
('Active spirit, short procs and Four Elements','Cold Shock sustain, summon upgrades and Elemental Fusion options')],
'progress':'''A **character level** unlocks a skill or its next purchased rank. A **skill rank** unlocks specialization choices: many active skills open options at ranks 8, 12 and 16, but each skill has its own thresholds. A rank-12 example does not mean character level 12.

Select the specialization after reaching its threshold. Options offered in the same slot are alternatives. For example, Sorcerer's rank-8 Hellfire can favor faster casting, damage over time or mobile casting; one choice does not supply all three.

Record purchased ranks separately from bonus ranks supplied by equipment, Arcana and Daevanion. A later build may reach a threshold your current points and bonuses cannot. Preserve the lower-rank loop until you can reproduce the selected effect.

Check your visible Stigma slots and available upgrade points before equipping a suggested list. Learning another Stigma skill does not create another slot. Regional Daevanion layouts and values differ; use the matching board and locate the effect rather than copying a KR/TW screenshot.''',
'layers':[
('Active skills','Fund the ordinary attack, main damage and recovery that you actually use. Sustain comes before a longer chain that immediately empties MP.'),
('Specializations','Select the required cooldown, resource, mobile or trigger effect. Check its rank threshold and the slot it occupies.'),
('Passives','Match the trigger to your loop: Assassin back damage, Ranger critical procs, Spiritmaster spirit hits or Chanter attack-built shields.'),
('Stigmas','Equip role tools within the unlocked slots. Trade a damage slot for block, cleanse, healing or dispel when that missing action causes failure.'),
('Daevanion','Compare total route cost to the destination skill or passive. A reached rank threshold can change a loop more than unrelated neighboring stats.'),
('Equipment and Arcana','Count the skill-rank bonuses that complete your chosen options. Check whether changing an item removes a required threshold.')],
'layerHeaders':['Build layer','What to do'],
'loops':[
('Buffs → Ruinous Blow → Rage Burst → available Overhead Slam; Keen Strike and Rending Blow between cooldowns','Overhead Slam needs its target condition or Rage Burst. Keep Focused Block manual if tanking.'),
('Shield Smite → Judgment; Warding Strike → Judgment; safe Punishment charge; Vicious Strike and Pummel between windows','Spend each short Judgment window before another trigger. Keep Taunt and shields independent.'),
('Buffs → approach behind target → Savage Roar stacks → Insignia Explosion; critical Heart Gore opportunities','Insignia lasts briefly on this target. Illusive Clone removes Heart Gore cooldown for its window, not permanently.'),
('Gale Arrow → Marking Shot → available Suppressing Arrow; Deadshot and Snipe; Drill Dart on a critical proc','Burst Arrow requires Slow or Root. Resume firing within range after movement.'),
('Rushing Smash → Spinning Strike → Dark Crush; later Impactful Crush or ranged Stigma → Dark Crush','Before selected rank-16 cooldown removal, wait between Dark Crush windows. Recuperation remains separate.'),
('Light of Regeneration → Debilitating Mark → Chain of Torment; equipped Earth Punishment → available Condemnation','Stop damage for urgent healing or Radiant Recovery. Condemnation reset needs its selected option and a critical hit.'),
('Damage buffs → fire attacks and available Blaze; safe Hellfire → Firestorm; Ice Chain → Winter’s Shackles','Blaze needs Fire Mark. Restore MP to preserve mana-dependent passive effects; keep defense reachable.'),
('Useful spirit → available Dimensional Control → own attacks → Elemental Fusion when Four Elements appears','Four Elements comes from spirit skills. Spend it before more stacks; choose Water for MP or Wind for HP.')],
'loopHeaders':['Class','Manual practice loop','Condition and separate control'],
'reactions':'''These are starting priorities, not one fixed endgame rotation. Use only equipped and unlocked skills. Attack buffs belong before a window you can finish; a control-dependent follow-up belongs after its actual trigger. The class pages explain alternate slots, passives and skill lists.

Keep **Defiance, timed blocks, emergency healing, cleansing, resurrection and situational movement** outside the repeating damage chain. Stagger-only attacks also wait for Stagger; they are not ordinary filler. A critical-hit proc cannot be guaranteed by putting its button next in a combo.

Practice the normal loop, then test returning after movement and interrupting for your party job. Only combine the attacks you want repeated in that order. The [in-game macro guide](/macro-guide) covers combo controls; another character's cooldown reduction and attack speed can change its timing.''',
'planner':'''Open the [AION 2 Build Planner](https://aion2.gaming.tools/build-planner), choose your class and faction, then use **Skills** to change ranks with **Raise / Lower**. Select specialization options and track the point totals as you change them. Keep the planner's available slots and bonus-rank inputs consistent with your character.

Use the current plan to compare two allocations before spending points in game. Its local plan is stored in that browser; account-based **Save to My Builds** requires signing in. Keep a separate record if you need the setup in another browser.

The planner helps budget points. It does not choose your encounter role or demonstrate that you can complete a cast while moving. Test the selected trigger, recovery and defensive response on your character.''',
'failHeaders':['Failure','Change to test first'],
'failures':[
('MP runs out','Select the ordinary-attack MP option or reduce the cost of the repeated area attack. Check whether recovery attacks actually land.'),
('A follow-up never appears','Check its target status, critical proc, resource or short activation window before adding more damage buttons.'),
('Copied cooldowns do not match','Check selected cooldown options and total skill ranks, including bonuses lost when equipment changed.'),
('Charged attacks keep stopping','Choose speed or mobility where offered, or start the charge in a longer safe window.'),
('Party recovery is insufficient','Replace the least useful damage Stigma with the needed heal, shield or cleanse. Keep it on a reachable control.'),
('Two support classes duplicate a buff','Chanter Undefeated Mantra and Cleric Light of Protection do not stack their damage boost; Templar Fury and Gladiator Experienced Counterstrike also overlap.')],
'save':'''Save the class, activity, party role, equipment and Arcana, purchased and bonus skill ranks, selected specializations, equipped Stigmas and Daevanion route. Keep the working version before changing points.

Compare one change against the same enemy with the same gear and fight length. Record MP, successful follow-ups, interrupted casts and whether support was available, alongside damage. A larger burst that prevents the next healing response is a poor improvement for a healer. Prepare a separate [PvP setup](/pvp) for control, escape and recovery under pressure.'''
}
copy['ja']={
'title':'AION 2 ビルド：8職の連携・スキル・スティグマ',
'description':'8職の序盤ビルドを比較。スキルランク、スティグマ交換、手動連携、Daevanion、ビルドプランナーの使い方を解説。',
'summary':'職の連携を選び、ランクと枠数に合わせて構成。足りない資源、発動条件、味方支援を改善します。',
'answer':'MP回復、追撃を開くスキル、担当役割の防御・回復から始めます。解放済み特化を選び、枠内でスティグマを装備し、反復コンボ前に手動で練習します。',
'headings':['8職の序盤ビルドを選ぶ','進行度とスキルランクを合わせる','スキル・スティグマ・Daevanion・装備','8職の手動連携','反応操作を攻撃連携から分ける','スキルビルドプランナーを使う','構成を保存し弱点を改善する'],
'table':['クラスガイド','中心となる判断','最初の有効強化'],
'rows':[
('MP継戦と前衛攻撃。タンクなら防御維持','Keen StrikeのMPとRuinous Blow短縮'),('Judgment、敵対値、盾の時間合わせ','Vicious Strike→Warding Strike、Pummel→Punishment短縮'),('背面攻撃と対象ごとのInsignia','Quick Sliceの継戦とExplosion短縮、クリティカル時Heart Gore'),('射程、クリティカル追撃、Deadshot','SnipeのMPと命中時Deadshot短縮'),('Dark Crushの発動時間とマントラ','Spinning Strike短縮とDark Crush特化。回復役なら支援追加'),('自動直接回復、解除、安全な攻撃','Radiant Recoveryの選択と、攻撃可能ならCondemnationリセット'),('完了できるチャージとMP条件','Firestorm→Hellfire、Ice Chain→Winter’s Shackles短縮'),('残す精霊、短い発動、Four Elements','Cold Shock継戦、精霊強化、Fusion特化')],
'progress':'''**キャラクターレベル**は習得や購入ランクを解放し、**スキルランク**は特化を解放します。多くの攻撃は8・12・16で選択肢を得ますが、閾値はスキルごとに違います。ランク12の例はキャラクターレベル12ではありません。

到達後に特化を選びます。同じ枠の効果は代替選択。例えばHellfireのランク8は高速化、継続ダメージ、移動可能化から選び、全部を同時に得るわけではありません。

購入ランクと装備・Arcana・Daevanionの追加ランクを別々に記録。現在到達できない特化は、低ランクの連携で運用します。

スティグマは実際の枠数と強化ポイントを確認。習得だけで枠は増えません。地域でDaevanionの配置や値は異なるため、KR/TW画像を写すより自分の盤面で目的効果を探します。''',
'layerHeaders':['構成要素','行うこと'],
'layers':[
('アクティブ','使う通常攻撃、主力、回復に投資。即MPが尽きる長い連携より継戦。'),('特化','再使用、資源、移動、発動効果を選択。必要ランクと枠を確認。'),('パッシブ','アサシンの背面、レンジャーのクリティカル、精霊攻撃、チャンターの攻撃盾など実際の発動へ。'),('スティグマ','解放枠内で役割を装備。失敗原因に合う防御、解除、回復へ攻撃枠を交換。'),('Daevanion','目的スキルまでの総コストを比較。特化到達は無関係な周辺ステータスより連携を変えます。'),('装備・Arcana','選んだ特化を完成させるランクを計算。装備交換で閾値を失わないか確認。')],
'loopHeaders':['クラス','手動の練習連携','条件と独立操作'],
'loops':[
('強化→Ruinous Blow→Rage Burst→Overhead Slam。合間にKeen StrikeとRending Blow','Overhead Slamは対象条件やRage Burstが必要。タンクのFocused Blockは手動。'),('Shield Smite→Judgment、Warding Strike→Judgment、安全なPunishment、合間にVicious StrikeとPummel','短いJudgmentを消費してから次の発動。Tauntと盾は独立。'),('強化→背後へ→Savage Roarの層→Insignia Explosion。クリティカル時Heart Gore','Insigniaは対象限定で短時間。Illusive Cloneの再使用削除は効果時間内。'),('Gale Arrow→Marking Shot→Suppressing Arrow。DeadshotとSnipe、クリティカル時Drill Dart','Burst Arrowには減速・束縛。移動後は射程へ戻る。'),('Rushing Smash→Spinning Strike→Dark Crush。次にImpactful Crushや遠距離スティグマ','ランク16の再使用削除前は待機。Recuperationは別操作。'),('Light of Regeneration→Debilitating Mark→Chain of Torment、Earth Punishment→Condemnation','急な回復・解除で中断。リセットには特化とクリティカル。'),('強化→火攻撃とBlaze。安全なHellfire→Firestorm、Ice Chain→Winter’s Shackles','BlazeはFire Mark。MP条件を維持し防御を残す。'),('必要な精霊→Dimensional Control→自分の攻撃→Four ElementsでFusion','精霊スキルで層を得て先に消費。MPは水、HPは風。')],
'reactions':'''これは序盤の優先順位で、固定の最終連携ではありません。装備・解放したスキルだけ使います。攻撃強化は完了できる時間へ、条件付き追撃は実際の発動後へ。各職ページに交換枠と全スキルがあります。

**Defiance、防御、緊急回復、解除、復活、状況別移動**は反復攻撃から分離。スタガー限定技は通常の穴埋めではありません。次のボタンに置くだけでクリティカルは保証されません。

通常連携、移動から復帰、役割のため中断を練習。その順で繰り返したい攻撃だけまとめます。[ゲーム内マクロ](/macro-guide)で操作を確認。他のキャラの速度や再使用は自分と違う場合があります。''',
'planner':'''[AION 2 Build Planner](https://aion2.gaming.tools/build-planner)で職と種族を選び、**Skills**の**Raise / Lower**でランクを変更。特化を選びポイント合計を確認します。枠数と追加ランク入力も実キャラに合わせます。

ゲーム内で振る前に2案を比較。ローカル構成はそのブラウザーに保存され、アカウントの**Save to My Builds**はログインが必要です。別ブラウザーへ移すなら別途記録します。

プランナーは配分の道具です。戦闘中の役割や安全な詠唱時間は、実キャラで発動・回復・防御を確認します。''',
'failHeaders':['失敗','最初に変える点'],
'failures':[
('MPが尽きる','通常攻撃のMP回復や範囲技の消費軽減。回復攻撃の命中も確認。'),('追撃が出ない','対象状態、クリティカル、資源、短い発動時間を確認。'),('再使用が例と違う','選んだ短縮と総ランク、装備変更で失った追加ランクを確認。'),('チャージが止まる','速度・移動特化か、より長い安全な使用時間。'),('味方回復が足りない','不要な攻撃枠を必要な回復・盾・解除へ。別操作を確保。'),('支援が重複する','MantraとLight of Protectionの火力、FuryとExperienced Counterstrikeは重複しません。')],
'save':'''職、活動、担当役割、装備・Arcana、購入・追加ランク、特化、スティグマ、Daevanion経路を保存。振り直し前に動く構成を残します。

同じ敵、装備、戦闘時間で1点を比較。ダメージだけでなくMP、追撃成功、中断、支援の使用可能性を記録。回復が間に合わなくなる瞬間火力は回復役の改善にはなりません。[PvP構成](/pvp)は制御、退避、圧力下の回復を別に準備。'''
}
copy['es']={
'title':'AION 2 Builds: Ocho Clases, Habilidades y Estigmas',
'description':'Compara builds iniciales de ocho clases: rangos, estigmas, ciclos manuales, prioridades de Daevanion y pasos del planificador.',
'summary':'Elige un ciclo, ajusta rangos y ranuras y mejora el recurso, activación o apoyo que falta.',
'answer':'Empieza con recuperación de MP, ataques que abren seguimientos y defensa o curación de tu función. Selecciona especializaciones, equipa estigmas dentro de tus ranuras y practica manualmente antes de repetir combos.',
'headings':['Elige una build de cualquier clase','Ajusta rangos a tu progreso','Habilidades, estigmas, Daevanion y equipo','Ocho ciclos manuales iniciales','Separa reacciones de la cadena de daño','Usa el planificador de habilidades','Guarda el plan y corrige su punto débil'],
'table':['Guía de clase','Decisión central','Primera mejora útil'],
'rows':[
('MP y daño frontal; bloqueo si tanqueas','MP de Keen Strike y reducción de Ruinous Blow'),('Judgment, amenaza y escudo','Reducciones Vicious Strike→Warding Strike y Pummel→Punishment'),('Ataques traseros y marcas del objetivo','Quick Slice y reducción de Insignia Explosion; Heart Gore con críticos'),('Alcance, críticos y Deadshot','MP de Snipe y reducción de Deadshot al acertar'),('Ventanas de Dark Crush y mantras','Recarga de Spinning Strike y opciones de Dark Crush; curación si hace falta'),('Curación automática, disipación y daño seguro','Opciones de Radiant Recovery y reinicio de Condemnation si puedes atacar'),('Cargas completas y pasivas de MP','Firestorm→Hellfire e Ice Chain→Winter’s Shackles'),('Espíritu activo y Four Elements','Cold Shock, invocaciones y opciones de Elemental Fusion')],
'progress':'''El **nivel de personaje** permite aprender o comprar rangos. El **rango de habilidad** abre especializaciones: muchas activas ofrecen opciones en 8, 12 y 16, pero cada habilidad tiene sus umbrales. Rango 12 no significa nivel de personaje 12.

Selecciona la opción tras alcanzarla. Las opciones de una misma ranura son alternativas: Hellfire de rango 8 puede acelerar, añadir daño periódico o permitir movimiento; una elección no aporta las tres.

Anota rangos comprados y adicionales de equipo, Arcana y Daevanion por separado. Mantén el ciclo inferior si no alcanzas la opción de la build avanzada.

Comprueba ranuras Stigma y puntos disponibles. Aprender otra habilidad no añade un espacio equipado. Los tableros regionales de Daevanion difieren: busca el efecto en el tuyo en vez de copiar una captura KR/TW.''',
'layerHeaders':['Capa','Acción'],
'layers':[
('Activas','Financia ataque normal, daño principal y recuperación utilizados; suministro antes de una cadena que agota MP.'),('Especializaciones','Selecciona recarga, recurso, movimiento o disparador; revisa rango y ranura.'),('Pasivas','Ajusta condiciones: espalda del Asesino, críticos del Arquero, impactos de espíritus o escudos del Cantor.'),('Estigmas','Equipa según función y ranuras. Cambia daño por bloqueo, curación o disipación cuando falte esa acción.'),('Daevanion','Compara coste total hasta la habilidad o pasiva. Alcanzar una opción puede cambiar más que estadísticas vecinas.'),('Equipo y Arcana','Cuenta rangos adicionales que completan opciones y revisa si cambiar un objeto pierde el umbral.')],
'loopHeaders':['Clase','Ciclo manual','Condición y control aparte'],
'loops':[
('Mejoras→Ruinous Blow→Rage Burst→Overhead Slam; Keen Strike y Rending Blow entre recargas','Overhead Slam exige condición o Rage Burst. Focused Block manual al tanquear.'),('Shield Smite→Judgment; Warding Strike→Judgment; Punishment seguro; Vicious Strike y Pummel','Consume cada ventana breve de Judgment. Taunt y escudos aparte.'),('Mejoras→espalda→Savage Roar→Insignia Explosion; Heart Gore con crítico','Marcas breves por objetivo. Illusive Clone elimina recarga de Heart Gore solo durante su ventana.'),('Gale Arrow→Marking Shot→Suppressing Arrow; Deadshot y Snipe; Drill Dart tras crítico','Burst Arrow exige ralentización o inmovilización. Vuelve a alcance tras moverte.'),('Rushing Smash→Spinning Strike→Dark Crush; luego Impactful Crush o estigma a distancia','Espera antes de eliminar recarga en rango 16. Recuperation aparte.'),('Light of Regeneration→Debilitating Mark→Chain of Torment; Earth Punishment→Condemnation','Interrumpe ante curación o disipación urgente. El reinicio exige opción y crítico.'),('Mejoras→fuego y Blaze; Hellfire seguro→Firestorm; Ice Chain→Winter’s Shackles','Blaze necesita Fire Mark. Mantén MP para pasivas y defensa accesible.'),('Espíritu útil→Dimensional Control→ataques propios→Fusion con Four Elements','Elementos mediante habilidades de espíritu. Consume antes de más; Agua para MP, Viento para HP.')],
'reactions':'''Son prioridades iniciales, no una rotación final fija. Usa habilidades aprendidas y equipadas. Activa mejoras antes de ventanas completas y seguimientos tras su condición real. Cada clase explica pasivas, cambios y lista completa.

Separa **Defiance, bloqueos, curación urgente, disipación, resurrección y movimiento situacional** de la cadena. Ataques de tambaleo esperan ese estado; no son relleno habitual. Colocar una habilidad después de otra no garantiza un crítico.

Practica el ciclo, regresar tras moverte e interrumpir para tu función. Combina solo ataques que quieras repetir en ese orden. La [guía de macros](/macro-guide) explica controles; velocidad y recargas de otro personaje pueden cambiar los tiempos.''',
'planner':'''Abre [AION 2 Build Planner](https://aion2.gaming.tools/build-planner), elige clase y facción y cambia rangos en **Skills** con **Raise / Lower**. Selecciona opciones y observa puntos totales. Ajusta ranuras y rangos adicionales a tu personaje.

Compara dos asignaciones antes de gastar en el juego. El plan local queda en ese navegador; **Save to My Builds** requiere iniciar sesión. Guarda otro registro para usarlo en otro navegador.

El planificador calcula asignaciones. Prueba activaciones, recuperación y defensa con tu personaje para saber si completas el lanzamiento durante las mecánicas.''',
'failHeaders':['Fallo','Primer cambio que probar'],
'failures':[
('Se acaba MP','Recuperación de ataque normal o menor coste de área; confirma impactos.'),('No aparece seguimiento','Estado, crítico, recurso o ventana de activación antes de añadir ataques.'),('Recargas distintas','Opciones seleccionadas y rango total, incluidos bonos perdidos al cambiar equipo.'),('Cargas interrumpidas','Velocidad, movilidad o ventana segura más larga.'),('Falta recuperación de party','Sustituye daño poco útil por curación, escudo o disipación accesible.'),('Mejoras duplicadas','Mantra y Light of Protection no acumulan daño; Fury y Experienced Counterstrike tampoco.')],
'save':'''Guarda clase, actividad, función, equipo y Arcana, rangos comprados y adicionales, opciones, estigmas y ruta Daevanion. Conserva el plan funcional antes de experimentar.

Compara un cambio con mismo enemigo, equipo y duración. Anota MP, seguimientos, cargas interrumpidas y disponibilidad de apoyo junto al daño. Más ráfaga que impide curar no mejora a un sanador. Prepara otra [build PvP](/pvp) para control, escape y recuperación bajo presión.'''
}
copy['de']={
'title':'AION 2 Builds: Acht Klassen, Fertigkeiten und Stigmas',
'description':'Vergleiche Startbuilds für acht Klassen: Fertigkeitsränge, Stigma-Wechsel, manuelle Abläufe, Daevanion und Schritte im Build-Planer.',
'summary':'Wähle einen Klassenablauf, plane erreichbare Ränge und Plätze und verbessere fehlende Ressourcen, Auslöser oder Gruppenwerkzeuge.',
'answer':'Beginne mit MP-Regeneration, Folgeangriffsauslösern und benötigter Abwehr oder Heilung. Wähle freigeschaltete Spezialisierungen, rüste Stigmas innerhalb deiner Plätze aus und übe manuell vor einer wiederholten Kombo.',
'headings':['Startbuild für jede Klasse wählen','Fertigkeitsränge an Fortschritt anpassen','Fertigkeiten, Stigmas, Daevanion und Ausrüstung','Acht manuelle Startabläufe','Reaktionen von Schaden trennen','Den Fertigkeitenplaner nutzen','Konfiguration sichern und Schwächen beheben'],
'table':['Klassenguide','Zentrale Entscheidung','Erste nützliche Verbesserung'],
'rows':[
('MP und Frontschaden; als Tank Block behalten','Keen-Strike-MP und Ruinous-Blow-Verkürzung'),('Judgment, Bedrohung und Schildtiming','Vicious Strike→Warding Strike, Pummel→Punishment'),('Rückenangriffe und zielgebundene Insignia','Quick Slice, Insignia-Explosion-Verkürzung und kritisches Heart Gore'),('Reichweite, kritische Folgeangriffe und Deadshot','Snipe-MP und Deadshot-Verkürzung bei Treffern'),('Dark-Crush-Fenster und Mantras','Spinning-Strike-Abklingzeit und Dark-Crush-Optionen; Heilung bei Bedarf'),('Automatische Heilung, Reinigung und sicherer Schaden','Radiant-Recovery-Optionen und kritischer Condemnation-Reset'),('Abgeschlossene Aufladungen und MP-Passive','Firestorm→Hellfire und Ice Chain→Winter’s Shackles'),('Aktiver Geist und Four Elements','Cold Shock, Beschwörungen und Elemental-Fusion-Optionen')],
'progress':'''Die **Charakterstufe** erlaubt Lernen und Rangkäufe. Der **Fertigkeitsrang** öffnet Spezialisierungen: viele aktive Fertigkeiten auf 8, 12 und 16, jedoch mit eigenen Schwellen. Rang 12 bedeutet nicht Charakterstufe 12.

Option nach Erreichen auswählen. Optionen im selben Platz sind Alternativen: Hellfire auf Rang 8 bietet schnelleres Wirken, laufenden Schaden oder mobiles Wirken, nicht alles gleichzeitig.

Gekaufte und zusätzliche Ränge aus Ausrüstung, Arcana und Daevanion getrennt notieren. Den früheren Ablauf behalten, wenn die spätere Option noch unerreichbar ist.

Sichtbare Stigma-Plätze und Punkte prüfen. Lernen fügt keinen Platz hinzu. Regionale Daevanion-Bretter und Werte unterscheiden sich: auf deinem Brett den Effekt suchen statt einen KR/TW-Screenshot zu kopieren.''',
'layerHeaders':['Buildteil','Aktion'],
'layers':[
('Aktive Fertigkeiten','Genutzte Standardangriffe, Hauptschaden und Heilung finanzieren. Regeneration vor einer sofort leeren MP-Leiste.'),('Spezialisierungen','Abkling-, Ressourcen-, Bewegungs- oder Auslöseoption wählen; Rang und Platz prüfen.'),('Passive Effekte','Auslöser passend wählen: Rücken beim Assassinen, kritische Treffer beim Waldläufer, Geisttreffer oder Kantors Angriffsschilde.'),('Stigmas','Rollenwerkzeuge in vorhandenen Plätzen. Bei fehlender Abwehr, Heilung oder Reinigung Schaden ersetzen.'),('Daevanion','Gesamtkosten zum Ziel vergleichen. Ein neuer Optionsrang kann mehr ändern als fremde Nachbarwerte.'),('Ausrüstung und Arcana','Zusatzränge für Optionen zählen; beim Gegenstandswechsel verlorene Schwellen prüfen.')],
'loopHeaders':['Klasse','Manueller Ablauf','Bedingung und separate Bedienung'],
'loops':[
('Buffs→Ruinous Blow→Rage Burst→Overhead Slam; Keen Strike und Rending Blow dazwischen','Overhead Slam benötigt Zielbedingung oder Rage Burst. Focused Block als Tank manuell.'),('Shield Smite→Judgment; Warding Strike→Judgment; sicheres Punishment; Vicious Strike und Pummel','Kurzes Judgment-Fenster verbrauchen. Taunt und Schilde separat.'),('Buffs→Rücken→Savage Roar→Insignia Explosion; Heart Gore bei kritischer Gelegenheit','Kurze zielgebundene Insignia. Illusive Clone entfernt Heart-Gore-Abklingzeit nur im Wirkfenster.'),('Gale Arrow→Marking Shot→Suppressing Arrow; Deadshot und Snipe; kritisches Drill Dart','Burst Arrow benötigt Verlangsamung oder Festhalten. Nach Bewegung in Reichweite zurück.'),('Rushing Smash→Spinning Strike→Dark Crush; später Impactful Crush oder Fernstigma','Vor gewählter Rang-16-Entfernung warten. Recuperation separat.'),('Light of Regeneration→Debilitating Mark→Chain of Torment; Earth Punishment→Condemnation','Für dringende Heilung oder Reinigung abbrechen. Reset benötigt Option und kritischen Treffer.'),('Buffs→Feuer und Blaze; sicheres Hellfire→Firestorm; Ice Chain→Winter’s Shackles','Blaze benötigt Fire Mark. MP für passive Effekte halten; Abwehr erreichbar.'),('Nützlicher Geist→Dimensional Control→eigene Angriffe→Fusion bei Four Elements','Elemente durch Geistfertigkeiten. Vor neuen Stapeln verbrauchen; Wasser für MP, Wind für HP.')],
'reactions':'''Dies sind Startprioritäten, kein fester Endgame-Ablauf. Nur erlernte und ausgerüstete Fertigkeiten nutzen. Buffs vor abgeschlossenen Fenstern, Folgeangriffe nach echten Auslösern. Klassenseiten erklären Wechsel, Passive und vollständige Listen.

**Defiance, Block, Notheilung, Reinigung, Wiederbelebung und situative Bewegung** separat halten. Taumel-Angriffe warten auf Taumeln; sie sind keine regulären Füller. Eine folgende Taste garantiert keinen kritischen Treffer.

Ablauf, Rückkehr nach Bewegung und Unterbrechung für die Gruppenrolle üben. Nur gewünschte Reihenfolgen kombinieren. Der [Makroguide](/macro-guide) erklärt Bedienung; fremdes Tempo und Abklingzeit verändern den Ablauf.''',
'planner':'''Im [AION 2 Build Planner](https://aion2.gaming.tools/build-planner) Klasse und Fraktion wählen, unter **Skills** Ränge mit **Raise / Lower** ändern. Optionen wählen und Punktsumme verfolgen. Plätze und Zusatzränge mit deinem Charakter abgleichen.

Zwei Verteilungen vor dem Ausgeben vergleichen. Der lokale Plan bleibt in diesem Browser; **Save to My Builds** benötigt Anmeldung. Für einen anderen Browser separat sichern.

Der Planer unterstützt Verteilung. Auslöser, Heilung und Abwehr am Charakter testen, um nutzbare Zauberfenster im Kampf zu prüfen.''',
'failHeaders':['Fehler','Erste Änderung zum Testen'],
'failures':[
('MP gehen aus','Standardangriffsregeneration oder Flächenkosten ändern; Treffer prüfen.'),('Folgeangriff fehlt','Zielstatus, kritischen Treffer, Ressource und kurzes Auslösefenster prüfen.'),('Fremde Abklingzeit passt nicht','Gewählte Optionen und Gesamtrang einschließlich verlorener Ausrüstungsboni prüfen.'),('Aufladungen brechen ab','Tempo, mobile Option oder längeres sicheres Fenster wählen.'),('Gruppenheilung reicht nicht','Wenig nützlichen Schadensplatz durch erreichbare Heilung, Schild oder Reinigung ersetzen.'),('Support doppelt Buffs','Mantra und Light of Protection stapeln ihren Schaden nicht; Fury und Experienced Counterstrike ebenfalls nicht.')],
'save':'''Klasse, Aktivität, Rolle, Ausrüstung und Arcana, Kauf- und Bonusränge, Optionen, Stigmas und Daevanion sichern. Funktionierenden Plan vor Änderungen behalten.

Eine Änderung mit gleichem Gegner, Ausrüstung und Kampfdauer vergleichen. MP, Folgeangriffe, abgebrochene Zauber und Support-Verfügbarkeit neben Schaden notieren. Mehr Burst bei verlorener Heilreaktion verbessert keinen Heiler. Separaten [PvP-Build](/pvp) für Kontrolle, Flucht und Heilung unter Druck vorbereiten.'''
}

def table(head,rows):
 return '| '+' | '.join(head)+' |\n| '+' | '.join(['---']*len(head))+' |\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rows)
anchors=['find-a-starting-build','check-region-and-progression','skills-stigmas-and-daevanion','three-concrete-examples','combos-and-reactive-skills','talent-calculator','save-and-improve-your-build']
for loc,c in copy.items():
 names={x['id']:x['names'][loc] for x in identities}
 roster=table(c['table'],[(f'[{names[s]}](/{s})',*r) for s,r in zip(order,c['rows'])])
 loops=table(c['loopHeaders'],[(f'[{names[s]}](/{s}#key-skills)',*r) for s,r in zip(order,c['loops'])])
 sections=[roster,c['progress']+'\n\n<GuideVisual id="workflow" />',table(c['layerHeaders'],c['layers'])+'\n\n<GuideVisual id="topic" />',loops,c['reactions'],c['planner'],table(c['failHeaders'],c['failures'])+'\n\n'+c['save']]
 body=c['answer']+'\n\n'+'\n\n'.join(f'<h2 id="{id}">{h}</h2>\n\n{body}' for id,h,body in zip(anchors,c['headings'],sections))+'\n\n<GuideNext slug="classes" />\n'
 p=ROOT/f'src/content/{loc}/builds.mdx';p.write_text(body,encoding='utf8')
 mpath=p.with_suffix('.json');m=json.loads(mpath.read_text(encoding='utf8'))
 m.update(title=c['title'],description=c['description'],summary=c['summary'],quickAnswer=c['answer'],toc=[dict(id=id,title=h) for id,h in zip(anchors,c['headings'])],inlineNext=['classes'])
 mpath.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Rebuilt the builds hub around all eight classes, preserving all seven section anchors.')
