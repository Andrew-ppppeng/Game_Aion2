import json
import re
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[4]
spec = importlib.util.spec_from_file_location('new_guides', Path(__file__).with_name('new-guides.py'))
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.pages.clear()

def guide(slug, locale, answer, role, upgrades, choices, loop, gear, faq):
    meta=json.loads((ROOT/f'src/content/{locale}/{slug}.json').read_text(encoding='utf8'))
    base.compact(slug,locale,meta['title'],meta['description'],meta['summary'],answer,role,upgrades,choices,loop,gear,faq,next_slug='leveling' if slug=='ranger' else 'builds')

guide('gladiator','en',
'Gladiator uses a greatsword for close-range damage and frontline defense. Build MP recovery with Keen Strike, connect Ruinous Blow to your attack window, and use Rage Burst to open Overhead Slam; keep Focused Block ready when tanking.',
'''Choose Gladiator if you want melee pressure with recovery, control and a tanking option. Its short-range attacks require returning to the enemy after mechanics. [Templar](/templar) offers a shield-focused loop and more party protection; Gladiator adds offensive buffs and conditional follow-ups.

When tanking, hold the enemy facing away from the party and keep a timed defensive control available. When another player tanks, take a safe damage position instead of competing for enemy movement. Compare the [class roster](/classes) for other roles.''',
'''Keen Strike restores MP; its rank-8 MP option improves sustain, while rank 12 shortens Ruinous Blow on hit. Rending Blow's cost reduction helps repeated area attacks. Ruinous Blow grants Prepare for Battle: use its buff before the skills it improves.

Crushing Wave offers HP recovery or MP recovery on critical hits among its rank-8 choices. Overhead Slam's rank-12 guaranteed critical option and rank-16 cooldown removal change its follow-up window. Pick the effects you need rather than assuming every specialization is active.

Blood Absorption heals on landed attacks and provides an emergency heal at low HP; it does not require a front attack. Attack Preparation improves damage, accuracy and defense. Experienced Counterstrike adds front-attack damage and a party buff after Block; that party damage effect does not stack with [Templar](/templar)'s Fury. Murderous Burst rewards maintaining attacks until its five stacks discharge.''',
[('Lunge Stance / Zikel’s Blessing','Combat speed / attack and accuracy. Activate for a window in which you can keep attacking.'),('Rage Burst','Damage, an enemy attack debuff and an Overhead Slam trigger. Its attack reduction overlaps Templar Taunt.'),('Blade Toss','Ranged damage with defense and incoming-healing reduction. Useful before continued pressure.'),('Focused Block','Timed protection with guaranteed Parry and resource recovery. Keep it manual when tanking.'),('Lifestealing Blade','Damage with HP absorption. Exchange a damage slot for it when recovery limits continued attacks.'),('Tenaciousness','Brief immunity followed by tolerance. Certain powerful attacks bypass it; use encounter positioning as well.')],
['Activate equipped Lunge Stance or Zikel’s Blessing before a safe attack window; approach with Ruinous Blow or Leaping Slam.','Use Rage Burst when equipped, then available Overhead Slam. Continue Keen Strike and Rending Blow between ready attacks.','Use Crushing Wave for the selected damage or recovery effect. Ankle Slice follows Parry or a selected Leaping Slam trigger; Aerial Snare requires its knockdown or immunity trigger.','During Stagger use Sword Aura Rampage. Interrupt damage for Focused Block, movement or Defiance; do not spend protection merely because it is next in a chain.'],
'''If misses break attack-based recovery or cooldown reduction, improve accuracy first. Compare attack, critical effects and combat speed after the loop works. Choose Daevanion destinations for Keen Strike, Ruinous Blow and the follow-ups you actually use; a new skill-rank threshold is useful only with its option selected.

For solo pulls, retain MP and HP recovery. For party damage, take offense once recovery is reliable; for tanking, preserve survival and front-attack/block benefits. Save each version in the [builds checklist](/builds) before reallocating.''',
'''**Overhead Slam is unavailable:** it needs a knocked-down target, an immunity-target proc or Rage Burst's trigger. It is not an unconditional attack.

**MP empties during pulls:** choose Keen Strike's MP option or lower Rending Blow's cost before adding another repeated attack.

**The party dies while you survive:** inspect enemy facing and attack timing, not just your HP. Focused Block protects your response; it does not make the boss safe behind you.

For [PvP](/pvp), keep Defiance, approach and control reachable. An enemy who escapes the attack window changes the next action; shorten the chain rather than spending every buff into empty space.''')

guide('gladiator','ja',
'グラディエーターはグレートソードで近接攻撃と前衛防御を行います。Keen StrikeでMPを維持し、Ruinous Blowの強化とRage BurstからのOverhead Slamをつなげます。タンク時はFocused Blockを独立操作にします。',
'''近接攻撃、自己回復、制御とタンクの選択肢を求める人向け。ギミック後に敵の近くへ戻る操作が必要です。[テンプラー](/templar)は盾の連携と味方保護を重視し、こちらは攻撃強化と条件付き追撃を組み合わせます。

タンクなら敵の正面を味方から外し、防御操作を残します。別の人がタンクなら敵を動かさず安全な攻撃位置へ。[全クラス](/classes)で役割を比較できます。''',
'''Keen StrikeはMPを回復し、ランク8の回復特化で継戦、ランク12で命中時のRuinous Blow短縮を得ます。Rending Blowの消費軽減は範囲攻撃の反復向け。Ruinous BlowのPrepare for Battleを主要攻撃の前に使います。

Crushing Waveのランク8ではHP回復やクリティカル時のMP回復を選べます。Overhead Slamはランク12の確定クリティカル、ランク16の再使用削除で追撃が変化。解放後に必要な特化を選択します。

Blood Absorptionは攻撃命中で回復し、低HP時に緊急回復。正面攻撃は条件ではありません。Attack Preparationは攻撃、命中、防御を補強。Experienced Counterstrikeは正面攻撃とブロック後の味方強化を持ち、後者は[テンプラー](/templar)のFuryと重複しません。Murderous Burstは攻撃を維持して5スタックを消費します。''',
[('Lunge Stance / Zikel’s Blessing','戦闘速度／攻撃力と命中。攻撃を続けられる時間に使用。'),('Rage Burst','攻撃、敵攻撃力低下、Overhead Slam発動。攻撃力低下はTauntと重複しません。'),('Blade Toss','遠距離攻撃と防御・被回復低下。継続攻撃の前に使用。'),('Focused Block','時間を合わせた防御、確定パリィ、資源回復。タンク時は手動操作。'),('Lifestealing Blade','攻撃とHP吸収。回復不足で攻撃が止まる時に交換。'),('Tenaciousness','短い免疫と終了後の耐性。一部の強力な攻撃は防げません。')],
['攻撃可能な時間に装備したLunge StanceやZikel’s Blessing。Ruinous BlowやLeaping Slamで接近。','Rage Burstから使用可能なOverhead Slam。合間にKeen StrikeとRending Blow。','Crushing Waveで選んだ攻撃・回復。Ankle SliceはパリィやLeaping Slam特化、Aerial Snareは転倒などの条件に反応。','スタガー中はSword Aura Rampage。防御、移動、Defianceのために攻撃を中断します。'],
'''命中が外れて回復や再使用短縮が止まるなら命中を先に改善。その後に攻撃、クリティカル、戦闘速度を比較。DaevanionはKeen Strike、Ruinous Blow、使う追撃の特化到達を目標にします。

ソロはMP・HP回復、攻撃役は継戦を確保して火力、タンクは生存と正面・ブロック効果を重視。[ビルド](/builds)に変更前の構成を保存します。''',
'''**Overhead Slamが出ない：**転倒、制御免疫対象への発動、Rage Burstが必要です。

**MPが尽きる：**Keen StrikeのMP回復やRending Blowの消費軽減を選びます。

**自分は生きても味方が倒れる：**敵の向きと攻撃タイミングを確認。自分の防御だけでは味方を守れません。

[PvP](/pvp)ではDefiance、接近、制御を別操作に。敵が離れたら長い連携を止め、次の攻撃機会を作ります。''')

guide('gladiator','es',
'Gladiador usa mandoble para daño cercano y defensa frontal. Mantén MP con Keen Strike, prepara la ventana con Ruinous Blow y abre Overhead Slam con Rage Burst. Si tanqueas, reserva Focused Block en un control independiente.',
'''Elígelo para presión cuerpo a cuerpo, recuperación y control con opción de tanque. Debes regresar al enemigo tras cada mecánica. [Templario](/templar) ofrece una cadena de escudo y más protección; Gladiador combina mejoras ofensivas y seguimientos condicionados.

Como tanque, orienta al enemigo lejos de aliados y conserva defensa manual. Con otro tanque, busca posición segura sin mover el objetivo. Compara las [clases](/classes).''',
'''Keen Strike recupera MP: su opción de rango 8 mejora el suministro y en rango 12 reduce Ruinous Blow al acertar. Menor coste de Rending Blow sostiene ataques de área. Usa Prepare for Battle de Ruinous Blow antes del daño que mejora.

Crushing Wave ofrece curación o MP con críticos en rango 8. Overhead Slam cambia con crítico garantizado en rango 12 y eliminación de recarga en rango 16. Selecciona cada efecto tras desbloquearlo.

Blood Absorption cura al acertar y a HP bajos; no exige atacar de frente. Attack Preparation mejora daño, precisión y defensa. Experienced Counterstrike mejora ataques frontales y aporta daño a la party al bloquear; ese beneficio no se acumula con Fury del [Templario](/templar). Murderous Burst descarga al llegar a cinco acumulaciones de ataques.''',
[('Lunge Stance / Zikel’s Blessing','Velocidad / ataque y precisión. Úsalos cuando puedas seguir atacando.'),('Rage Burst','Daño, reducción de ataque y apertura de Overhead Slam. Su reducción se solapa con Taunt.'),('Blade Toss','Daño a distancia, menor defensa y curación recibida antes de mantener presión.'),('Focused Block','Protección temporal, parada garantizada y recursos. Control manual si tanqueas.'),('Lifestealing Blade','Daño con absorción de HP cuando la recuperación limita ataques.'),('Tenaciousness','Inmunidad breve y tolerancia posterior. Ciertos ataques potentes la atraviesan.')],
['Activa Lunge Stance o Zikel’s Blessing equipados en ventana segura; acércate con Ruinous Blow o Leaping Slam.','Rage Burst y Overhead Slam disponible. Keen Strike y Rending Blow entre ataques listos.','Crushing Wave para el efecto elegido. Ankle Slice tras parar o el disparador de Leaping Slam; Aerial Snare con su condición de derribo o inmunidad.','Sword Aura Rampage durante tambaleo. Interrumpe para defensa, movimiento o Defiance.'],
'''Si fallar rompe recuperación o recargas, mejora precisión primero. Después compara ataque, críticos y velocidad. Daevanion debe alcanzar opciones de Keen Strike, Ruinous Blow y seguimientos utilizados; selecciona la especialización obtenida.

Solo necesita MP y HP; daño de party permite más ofensiva tras asegurar recuperación; tanque exige supervivencia y bloqueos. Guarda cada configuración con [builds](/builds).''',
'''**Overhead Slam no aparece:** necesita derribo, activación contra inmunidad o Rage Burst.

**Falta MP:** mejora recuperación de Keen Strike o reduce coste de Rending Blow.

**Sobrevives y la party muere:** revisa orientación y tiempo de ataques del enemigo; tu bloqueo no protege automáticamente a quienes están detrás.

En [PvP](/pvp), separa Defiance, acercamiento y control. Si el enemigo sale de alcance, corta la cadena antes de gastar más mejoras.''')

guide('gladiator','de',
'Gladiator nutzt ein Großschwert für Nahschaden und Frontverteidigung. Halte MP mit Keen Strike, bereite Schaden mit Ruinous Blow vor und öffne Overhead Slam durch Rage Burst. Beim Tanken bleibt Focused Block separat erreichbar.',
'''Wähle ihn für Nahkampfdruck, Heilung, Kontrolle und eine Tankoption. Nach Mechaniken musst du wieder in Nahreichweite. [Templer](/templar) bietet einen Schildablauf und mehr Gruppenschutz; Gladiator kombiniert offensive Buffs mit bedingten Folgeangriffen.

Als Tank das Gegnergesicht von Verbündeten wegdrehen und manuelle Abwehr behalten. Mit einem anderen Tank sicher angreifen, ohne das Ziel zu verschieben. Vergleiche die [Klassen](/classes).''',
'''Keen Strike stellt MP her: Rang 8 verbessert Regeneration, Rang 12 verkürzt Ruinous Blow bei Treffern. Rending Blows Kostenoption hilft bei Flächenangriffen. Ruinous Blows Prepare for Battle vor den verbesserten Angriffen einsetzen.

Crushing Wave bietet auf Rang 8 HP-Heilung oder MP bei kritischen Treffern. Overhead Slam verändert sich durch garantierte kritische Treffer auf Rang 12 und fehlende Abklingzeit auf Rang 16. Effekte nach Freischaltung auswählen.

Blood Absorption heilt bei Treffern und niedrigem HP; Frontangriffe sind keine Voraussetzung. Attack Preparation verbessert Schaden, Genauigkeit und Verteidigung. Experienced Counterstrike verbessert Frontangriffe und Gruppenschaden nach Blocken; der Gruppenbuff stapelt nicht mit Fury des [Templers](/templar). Murderous Burst entlädt nach fünf Angriffsstapeln.''',
[('Lunge Stance / Zikel’s Blessing','Kampftempo / Angriff und Genauigkeit während nutzbarer Angriffszeit.'),('Rage Burst','Schaden, Angriffsreduktion und Overhead-Slam-Auslöser. Reduktion überschneidet sich mit Taunt.'),('Blade Toss','Fernangriff mit Verteidigungs- und Heilreduktion vor anhaltendem Druck.'),('Focused Block','Zeitabhängige Abwehr, garantiertes Parieren und Ressourcen. Als Tank manuell behalten.'),('Lifestealing Blade','Schaden mit HP-Absorption bei Regenerationsproblemen.'),('Tenaciousness','Kurze Immunität und anschließende Toleranz. Bestimmte mächtige Angriffe umgehen sie.')],
['Ausgerüstetes Lunge Stance oder Zikel’s Blessing im sicheren Fenster; Ruinous Blow oder Leaping Slam zum Nähern.','Rage Burst und verfügbares Overhead Slam. Dazwischen Keen Strike und Rending Blow.','Crushing Wave mit gewähltem Effekt. Ankle Slice nach Parieren oder Leaping-Slam-Auslöser; Aerial Snare bei passender Bedingung.','Sword Aura Rampage während Taumeln. Für Abwehr, Bewegung oder Defiance unterbrechen.'],
'''Wenn Fehlschläge Regeneration und Verkürzungen stoppen, zuerst Genauigkeit verbessern. Danach Angriff, kritische Effekte und Tempo vergleichen. Daevanion zu Keen Strike, Ruinous Blow und genutzten Folgeangriffen führen; neue Optionen auswählen.

Solo MP und HP erhalten; als Schadensrolle nach gesicherter Heilung mehr Offensive; als Tank Überleben und Blockeffekte behalten. Konfiguration in [Builds](/builds) sichern.''',
'''**Overhead Slam fehlt:** benötigt Niederschlag, eine Auslösung am immunen Ziel oder Rage Burst.

**MP gehen aus:** Keen Strikes Regeneration oder Rending Blows Kostenreduktion wählen.

**Du überlebst, die Gruppe stirbt:** Gegnerausrichtung und Angriffstiming prüfen. Dein Block schützt nicht automatisch alle hinter dir.

Für [PvP](/pvp) Defiance, Annäherung und Kontrolle separat halten. Verlässt das Ziel die Reichweite, die Kette vor weiteren Buffs abbrechen.''')

guide('ranger','en',
'Ranger uses a bow for ranged damage. Snipe restores MP and can shorten Deadshot; Marking Shot grants Precision for Suppressing Arrow. Drill Dart opens after a critical hit, while Burst Arrow needs Slow or Root on the target.',
'''Choose Ranger for ranged attacks with movement, traps and conditional follow-ups. A critical proc, a target's status and the next safe firing position determine what to press. [Sorcerer](/sorcerer) focuses on spell windows; [Spiritmaster](/spiritmaster) adds summon management.

Several attacks reach 20m. Stay within the useful range after dodging rather than moving so far that every ready attack stops. Distance does not replace reacting when a melee enemy closes in. Compare the [class roster](/classes).''',
'''Snipe is your ordinary MP-restoring attack. Select its rank-8 MP option when supply limits you; at rank 12 choose its on-hit Deadshot cooldown reduction. Deadshot offers no MP cost, faster use or mobile casting at rank 8: choose the one that solves your interruption.

Tempest Shot's cost reduction supports repeated area damage. Marking Shot creates Precision for Suppressing Arrow; its later guaranteed-critical choice also improves critical-dependent opportunities. Drill Dart only opens after a critical hit and restores MP if its own attack is critical.

Focused Eye improves accuracy and damage; Hunter's Resolve improves critical damage. Concentrated Fire rewards attacks against damage-over-time targets, while Rooting Eye requires Slow or Root. Hunter's Soul procs on critical hits. Do not invest around a status that your current target never receives.''',
[('Vaizel’s Authority / Bow of Blessing','Attack / critical hit and accuracy before a safe damage window.'),('Griffon Arrow','Area damage and damage over time; target movement increases its continuing damage.'),('Explosive Arrow','Area damage with an extra benefit against Slow or Root targets.'),('Supporting Fire','Temporary supporting shots and HP absorption. Retain when useful sustain accompanies damage.'),('Ambush Kick / Ensnaring Trap','Create distance or punish an approaching opponent. Traps belong on the route the target will cross.'),('Mother Nature’s Breath / Sealing Arrow','Personal tolerance and recovery / enemy Seal. Use a defensive or control slot for the failure you need to prevent.')],
['Activate equipped attack or critical buffs. Use Gale Arrow for its combat benefit and Marking Shot for Precision.','Use available Suppressing Arrow, charge Deadshot in a safe window, and fill gaps with Snipe to supply MP and the selected cooldown reduction.','Use Drill Dart after a critical proc. Apply Snare Shot’s Slow or Root to enable Burst Arrow; a target without that status does not enable it.','Use Arrow Scattershot during Stagger. Reposition after mechanics and resume attacks; keep Defiance, traps and escape decisions independent.'],
'''Critical hit affects both damage and Drill Dart availability. Accuracy matters when misses stop Snipe's cooldown feed; cast speed or Deadshot's mobility matters when mechanics interrupt charges. Choose Daevanion routes to the next useful Snipe, Deadshot or passive upgrade within your point budget.

Regional Daevanion layouts and values differ, so locate the desired skill effect on your own board rather than copying a TW route. The [leveling guide](/leveling) covers progression; [builds](/builds) keeps skill ranks separate from character levels.''',
'''**Drill Dart is missing:** it requires an actual critical hit. A skill sequence cannot guarantee a random prerequisite.

**Burst Arrow is missing:** Slow or Root must be on this target. An immune boss may require a different available attack.

**Deadshot stays on cooldown:** select Snipe's rank-12 cooldown option and land its hits.

For solo pulls, keep MP and manageable area damage. For bosses, resume firing within range after mechanics. For [PvP](/pvp), place traps for approach routes and preserve an escape; Stealth only starts outside combat and ends when combat begins.''')

guide('ranger','ja',
'レンジャーはボウで遠距離攻撃。SnipeでMPとDeadshot再使用を支え、Marking ShotのPrecisionからSuppressing Arrowにつなげます。Drill Dartはクリティカル後、Burst Arrowは減速・束縛中の対象に使用できます。',
'''移動、罠、条件付き追撃を持つ遠距離職です。クリティカル、対象の状態、安全な射撃位置で次の行動が変わります。[ソーサラー](/sorcerer)は詠唱時間、[スピリットマスター](/spiritmaster)は召喚管理が中心。

多くの攻撃は20m。回避後も攻撃が届く距離へ戻ります。遠距離でも接近された時の反応は必要です。[全クラス](/classes)と比較できます。''',
'''Snipeは通常のMP回復攻撃。ランク8の回復特化と、ランク12の命中時Deadshot短縮が基本です。Deadshotのランク8はMP消費削除、高速化、移動可能化から問題に合う効果を選びます。

Tempest Shotの消費軽減は範囲攻撃向け。Marking ShotのPrecisionでSuppressing Arrowを開き、後の確定クリティカル特化で追撃の機会を増やせます。Drill Dartはクリティカル後だけ使用でき、その攻撃もクリティカルならMP回復。

Focused Eyeは命中と攻撃、Hunter's Resolveはクリティカルダメージ。Concentrated Fireは継続ダメージ対象、Rooting Eyeは減速・束縛対象、Hunter's Soulはクリティカルに反応。対象に付かない状態を前提に投資しないようにします。''',
[('Vaizel’s Authority / Bow of Blessing','攻撃力／クリティカルと命中を攻撃時間の前に強化。'),('Griffon Arrow','範囲攻撃と継続ダメージ。対象の移動で継続ダメージ増加。'),('Explosive Arrow','減速・束縛対象に追加効果のある範囲攻撃。'),('Supporting Fire','補助射撃とHP吸収。攻撃と継戦を両立。'),('Ambush Kick / Ensnaring Trap','距離を作る／接近を罠で止める。敵が通る位置へ配置。'),('Mother Nature’s Breath / Sealing Arrow','自己耐性と回復／封印。防ぎたい失敗に合わせて交換。')],
['装備した攻撃・クリティカル強化。Gale Arrowの強化とMarking ShotのPrecision。','Suppressing Arrowと安全なDeadshot。合間にSnipeでMPと選択した再使用短縮。','クリティカル後のDrill Dart。Snare Shotで減速・束縛を付けBurst Arrow。状態がない敵には開きません。','スタガーにArrow Scattershot。ギミック後に射程へ戻り、Defiance・罠・退避は別操作。'],
'''クリティカルは火力とDrill Dartの頻度に影響。命中が外れるとSnipeの短縮も止まります。チャージ中断が多いなら速度や移動特化を比較。DaevanionはSnipe、Deadshot、使うパッシブの次の有効特化へ。

地域でDaevanionの配置や値が違うため、TWの経路ではなく自分の盤面の目的効果を探します。[レベリング](/leveling)と[ビルド](/builds)で進行とスキルランクを確認。''',
'''**Drill Dartが出ない：**実際のクリティカルが必要です。

**Burst Arrowが出ない：**現在の対象に減速・束縛が必要。免疫対象なら別の攻撃へ。

**Deadshotが短縮されない：**Snipeのランク12特化を選び、命中させます。

ソロはMPと制御できる範囲攻撃、ボスは射程への復帰。[PvP](/pvp)は接近経路の罠と退避を準備。Stealthは戦闘外限定で、戦闘開始時に解除されます。''')

guide('ranger','es',
'Explorador usa arco a distancia. Snipe recupera MP y puede reducir Deadshot; Marking Shot da Precision para Suppressing Arrow. Drill Dart se abre tras un crítico y Burst Arrow requiere ralentización o inmovilización del objetivo.',
'''Elígelo para ataques a distancia, movimiento, trampas y seguimientos condicionados. Críticos, estados del enemigo y posición segura determinan el siguiente botón. [Hechicero](/sorcerer) prioriza ventanas de lanzamiento; [Maestro espiritual](/spiritmaster), invocaciones.

Muchos ataques alcanzan 20m. Vuelve a alcance tras esquivar: alejarte demasiado también detiene el daño. Reacciona cuando el enemigo se acerca. Compara las [clases](/classes).''',
'''Snipe recupera MP normalmente. Elige su opción de MP de rango 8 si falta suministro y reducción de Deadshot al acertar en rango 12. Deadshot permite eliminar coste, acelerar o lanzar en movimiento en rango 8; elige según la interrupción.

Menor coste de Tempest Shot mantiene áreas. Marking Shot da Precision para Suppressing Arrow; su crítico garantizado posterior ayuda a abrir seguimientos. Drill Dart solo aparece tras un crítico y devuelve MP si su propio golpe es crítico.

Focused Eye mejora precisión y daño; Hunter's Resolve, daño crítico. Concentrated Fire necesita daño periódico en el objetivo; Rooting Eye, ralentización o inmovilización; Hunter's Soul, críticos. No inviertas alrededor de un estado que tu enemigo no recibe.''',
[('Vaizel’s Authority / Bow of Blessing','Ataque / crítico y precisión antes de una ventana segura.'),('Griffon Arrow','Área y daño periódico que aumenta cuando el objetivo se mueve.'),('Explosive Arrow','Área con beneficio adicional contra ralentización o inmovilización.'),('Supporting Fire','Disparos de apoyo y absorción de HP para sostener daño.'),('Ambush Kick / Ensnaring Trap','Crear distancia o castigar acercamiento. Pon trampas en la ruta del enemigo.'),('Mother Nature’s Breath / Sealing Arrow','Tolerancia y recuperación personal / sello enemigo según el problema.')],
['Activa mejoras equipadas. Gale Arrow para su beneficio y Marking Shot para Precision.','Suppressing Arrow disponible, Deadshot en ventana segura y Snipe entre recargas para MP y reducción seleccionada.','Drill Dart tras crítico. Snare Shot para ralentizar o inmovilizar y abrir Burst Arrow; sin ese estado no se habilita.','Arrow Scattershot durante tambaleo. Recolócate en alcance tras mecánicas; separa Defiance, trampas y escape.'],
'''Crítico afecta daño y frecuencia de Drill Dart. Precisión evita perder reducciones de Snipe; velocidad o movilidad de Deadshot ayudan si interrumpes cargas. Daevanion debe alcanzar la siguiente mejora útil de Snipe, Deadshot o pasivas.

Los diseños y valores regionales de Daevanion difieren: busca el efecto en tu tablero en lugar de copiar la ruta TW. [Subir nivel](/leveling) y [builds](/builds) explican progresión y rangos. ''',
'''**Falta Drill Dart:** requiere un crítico real; una secuencia no garantiza su condición aleatoria.

**Falta Burst Arrow:** el objetivo necesita ralentización o inmovilización. Cambia de ataque ante inmunidad.

**Deadshot no se acorta:** selecciona la opción de rango 12 de Snipe y acierta.

Solo necesita MP y áreas controlables; en jefes vuelve a alcance. En [PvP](/pvp), conserva escape y trampas en rutas de acercamiento. Stealth empieza fuera de combate y termina al entrar en él.''')

guide('ranger','de',
'Jäger nutzt einen Bogen. Snipe stellt MP her und kann Deadshot verkürzen; Marking Shot gibt Precision für Suppressing Arrow. Drill Dart öffnet nach kritischen Treffern, Burst Arrow benötigt Verlangsamung oder Festhalten am Ziel.',
'''Wähle ihn für Fernangriffe, Bewegung, Fallen und bedingte Folgeangriffe. Kritische Treffer, Zielstatus und sichere Position bestimmen den nächsten Angriff. [Magier](/sorcerer) nutzt Zauberfenster; [Beschwörer](/spiritmaster) verwaltet Geister.

Viele Angriffe reichen 20m. Nach Ausweichen in Reichweite zurückkehren, statt Schaden durch zu große Entfernung zu stoppen. Bei gegnerischer Annäherung reagieren. Vergleiche die [Klassen](/classes).''',
'''Snipe stellt regulär MP her. Bei Ressourcenmangel die Rang-8-MP-Option wählen, auf Rang 12 Deadshot bei Treffern verkürzen. Deadshot bietet auf Rang 8 keine MP-Kosten, schnelleres oder mobiles Wirken; nach der Ursache von Unterbrechungen wählen.

Tempest Shots Kostenoption unterstützt Flächenschaden. Marking Shot öffnet Suppressing Arrow durch Precision; die spätere garantierte kritische Option hilft bei Folgeangriffen. Drill Dart benötigt zuvor einen kritischen Treffer und stellt MP her, wenn sein eigener Angriff kritisch trifft.

Focused Eye verbessert Genauigkeit und Schaden; Hunter's Resolve kritischen Schaden. Concentrated Fire benötigt laufenden Schaden, Rooting Eye Verlangsamung oder Festhalten, Hunter's Soul kritische Treffer. Keine Investition auf einen Zielstatus bauen, der hier nicht auftritt.''',
[('Vaizel’s Authority / Bow of Blessing','Angriff / kritische Treffer und Genauigkeit vor sicherem Schaden.'),('Griffon Arrow','Fläche und laufender Schaden, der bei Zielbewegung steigt.'),('Explosive Arrow','Fläche mit Zusatznutzen gegen verlangsamte oder festgehaltene Ziele.'),('Supporting Fire','Unterstützungsschüsse und HP-Absorption für anhaltenden Schaden.'),('Ambush Kick / Ensnaring Trap','Abstand herstellen oder Annäherung bestrafen. Fallen auf gegnerischen Wegen platzieren.'),('Mother Nature’s Breath / Sealing Arrow','Eigene Toleranz und Heilung / gegnerische Versiegelung nach Bedarf.')],
['Ausgerüstete Buffs aktivieren. Gale Arrow für den Nutzen und Marking Shot für Precision.','Verfügbares Suppressing Arrow, Deadshot sicher aufladen und dazwischen Snipe für MP und gewählte Verkürzung.','Drill Dart nach kritischem Treffer. Snare Shot für Verlangsamung oder Festhalten, danach Burst Arrow; ohne Status fehlt es.','Arrow Scattershot bei Taumeln. Nach Mechaniken in Reichweite; Defiance, Fallen und Flucht separat.'],
'''Kritische Treffer beeinflussen Schaden und Drill Dart. Genauigkeit verhindert verlorene Snipe-Verkürzungen; Tempo oder mobiles Deadshot hilft bei abgebrochenen Aufladungen. Daevanion zu nutzbaren Snipe-, Deadshot- und passiven Optionen führen.

Regionale Daevanion-Anordnung und Werte unterscheiden sich. Suche den Effekt auf deinem Brett statt einen TW-Pfad zu kopieren. [Leveln](/leveling) und [Builds](/builds) erklären Fortschritt und Fertigkeitsränge.''',
'''**Drill Dart fehlt:** benötigt einen echten kritischen Treffer; eine Kette garantiert diese Zufallsbedingung nicht.

**Burst Arrow fehlt:** Ziel muss verlangsamt oder festgehalten sein. Bei Immunität einen anderen Angriff nutzen.

**Deadshot bleibt auf Abklingzeit:** Snipe-Option auf Rang 12 wählen und treffen.

Solo MP und kontrollierbare Flächen; am Boss schnell in Reichweite zurück. Für [PvP](/pvp) Fallen und Flucht sichern. Stealth beginnt außerhalb des Kampfes und endet beim Kampfeintritt.''')

guide('spiritmaster','en',
'Spiritmaster uses an orb and elemental spirits. Fire supplies area damage, Water restores MP, Wind restores HP and Earth generates threat. Spirit skills build four element stacks for Elemental Fusion; spend Fusion before more stacks are blocked.',
'''Choose Spiritmaster if you enjoy coordinating your own ranged attacks with summon effects and short proc windows. The spirit you leave active changes recovery, threat and the effects of Jointstrike skills. [Ranger](/ranger) has fewer summon decisions; [Sorcerer](/sorcerer) focuses on charged spells.

Elemental Fusion needs four stacks from spirit-skill activations, not four different elemental spirits. Once Four Elements is ready you cannot gain further elements until Fusion consumes it. Watch the status rather than blindly counting four summon buttons. Compare the [classes](/classes).''',
'''Cold Shock restores MP; its rank-8 MP option improves sustain and its rank-12 option shortens Combustion. Combustion has a rank-8 cost reduction. Dimensional Control also restores MP, so respond to its brief availability between your own attacks.

Raise the summons you use for their stat gains and selected effects. Water restores MP on its attacks without requiring a special recovery option; Wind's attacks restore your HP. Earth creates high threat, so choose its role before leaving it active beside a party tank.

Spirit Strike improves both caster and spirit damage. Spirit Communion adds accuracy and a chance to heal both on your hits. Spirit Revitalization can shorten summon cooldowns on hits. Spirit's Descent adds damage after a summon; Element Unification stacks critical damage after spirit-skill hits.''',
[('Summon: Ancient Spirit','Temporary spirit that grants Four Elements with each skill use, opening more Fusion opportunities.'),('Enhance: Spirit’s Benediction','Damage, tolerance and healing for you and the spirit. Use while both can contribute.'),('Jointstrike: Corrode','Damage-over-time and increased damage taken from the spirit. The coordinated effect changes with the active spirit.'),('Jointstrike: Destructive Attack','Coordinated damage; match the active spirit to the desired area or single-target pressure.'),('Siphon / Seize Magic','HP and MP recovery / removal of enemy buffs. Choose for resource shortage or a dispellable buff.'),('Command: Proxy / Cry of Terror','Shares damage with a spirit within 25m / Fear. Keep the spirit alive and close for damage sharing.')],
['Choose the opening spirit for the immediate need: Fire for area damage, Water for MP, Wind for HP, Earth for threat.','Use the available Dimensional Control window after a summon or spirit-skill activation. Add your own Cold Shock and Combustion attacks.','When Four Elements appears, use Elemental Fusion before trying to gain more stacks. With Ancient Spirit equipped, respond to its repeated Four Elements grants.','Apply equipped Jointstrike: Corrode before continued spirit damage. Use Rapid Scattershot during Stagger; keep defense and Fear separate.'],
'''Accuracy preserves your on-hit passive chances. Compare damage for both the caster and spirit, summon cooldowns and the Fusion threshold your points can reach. Fusion's rank-12 charge option changes the required safe window; do not copy that timing without the selected effect.

Use Daevanion for Cold Shock, Elemental Fusion, important summons and Spirit Revitalization when they change the working loop. Regional board drawings may differ: choose the effect and point cost. Save the configuration through [builds](/builds).''',
'''**Four summons do not open Fusion:** watch actual spirit-skill activations and element stacks. Pressing four names is not its condition.

**Water does not restore MP:** it must land attacks; check range, target and whether it is still active.

**The spirit draws unwanted attention:** Earth has high-threat attacks. Change the active spirit if another player should hold the enemy.

Solo can emphasize Water or Wind sustain. In a party, fit summons and debuffs around enemy positioning. For [PvP](/pvp), retain Fear, Seal or dispel choices for the opponent and keep a response available before they reach you.''')

guide('spiritmaster','ja',
'スピリットマスターはオーブと精霊で攻撃。火は範囲、水はMP、風はHP、土は敵対値を担当します。精霊スキルで4層ためElemental Fusionを使用。Four Elements中は追加層を得られないため先に消費します。',
'''自分の遠距離攻撃、精霊の効果、短い発動時間を組み合わせる職です。残す精霊で回復、敵対値、Jointstrikeが変化。[レンジャー](/ranger)は召喚管理が少なく、[ソーサラー](/sorcerer)はチャージ魔法が中心。

Fusionは精霊スキル発動による4層が条件で、4種類の精霊が必須ではありません。Four Elements中は追加層を受け取れず、Fusionで消費します。召喚ボタンの数ではなく状態を確認。[クラス](/classes)で比較できます。''',
'''Cold ShockはMP回復、ランク8は回復強化、ランク12はCombustion短縮。Combustionの消費軽減とDimensional ControlのMP回復で継戦します。

使う精霊を強化し、各効果を選択。Waterは基本の命中効果でMP回復し、専用回復特化は不要。Windは自分のHP、Earthは高い敵対値を生み、味方タンクとの役割を確認します。

Spirit Strikeは双方の火力。Spirit Communionは命中と双方の回復機会。Spirit Revitalizationは命中で召喚短縮。Spirit's Descentは召喚後の追加攻撃、Element Unificationは精霊スキル命中後のクリティカルダメージを強化します。''',
[('Summon: Ancient Spirit','一時精霊。スキル使用ごとにFour Elementsを与え、Fusionの機会を増やします。'),('Enhance: Spirit’s Benediction','本人と精霊の攻撃、耐性、回復。双方が働ける時間へ。'),('Jointstrike: Corrode','継続ダメージと精霊から受けるダメージ増加。連携効果は現在の精霊で変化。'),('Jointstrike: Destructive Attack','精霊との連携攻撃。範囲・単体用途に合わせる。'),('Siphon / Seize Magic','HP・MP回復／敵バフ解除。資源不足や解除可能な強化に対応。'),('Command: Proxy / Cry of Terror','25m内の精霊とダメージ共有／恐怖。共有には近くの生きた精霊が必要。')],
['火は範囲、水はMP、風はHP、土は敵対値から必要な精霊を選択。','召喚や精霊スキル後のDimensional Control発動時間に使用。自分のCold ShockとCombustionも加えます。','Four Elementsを見てFusionで消費。Ancient Spirit装備時は繰り返す付与にも反応します。','Jointstrike: Corrodeから精霊の継続攻撃。スタガーはRapid Scattershot。防御と恐怖は別操作。'],
'''命中でパッシブの機会を保ちます。本人・精霊の火力、召喚再使用、到達可能なFusion特化を比較。ランク12のチャージ特化は安全な使用時間が変わります。

DaevanionはCold Shock、Fusion、使う精霊、Spirit Revitalizationが候補。地域の図より目的効果と総コストを確認。[ビルド](/builds)で保存します。''',
'''**4回召喚してもFusionが出ない：**精霊スキル発動と実際の層数を確認。

**水でMPが戻らない：**攻撃命中、射程、現在の精霊を確認。

**精霊が敵を引く：**Earthは高い敵対値。味方がタンクなら残す精霊を変更。

ソロは水・風の継戦、パーティーは敵配置と減益を維持。[PvP](/pvp)は相手に合う恐怖・封印・解除と、接近前に使える防御を確保します。''')

guide('spiritmaster','es',
'Maestro espiritual usa orbe e invocaciones. Fuego aporta área, Agua MP, Viento HP y Tierra amenaza. Las habilidades de espíritu acumulan cuatro elementos para Elemental Fusion; consúmelos antes de bloquear más acumulaciones.',
'''Elígelo para coordinar ataques propios, efectos de invocación y ventanas breves. El espíritu activo cambia recuperación, amenaza y Jointstrike. [Explorador](/ranger) gestiona menos invocaciones; [Hechicero](/sorcerer), hechizos cargados.

Fusion necesita cuatro acumulaciones de activaciones de espíritu, no cuatro elementos diferentes. Four Elements impide nuevas acumulaciones hasta consumirlo. Mira el estado, no cuatro botones de invocación. Compara las [clases](/classes).''',
'''Cold Shock recupera MP; en rango 8 mejora suministro y en rango 12 acorta Combustion. Menor coste de Combustion y MP de Dimensional Control ayudan a sostener ataques.

Mejora invocaciones utilizadas y selecciona efectos. Agua restaura MP con sus ataques básicos sin una opción especial de recuperación; Viento cura tus HP. Tierra genera mucha amenaza: decide si debe seguir activa con otro tanque.

Spirit Strike mejora daño de ambos. Spirit Communion da precisión y probabilidad de curarlos. Spirit Revitalization puede acortar invocaciones al acertar. Spirit's Descent añade daño tras invocar; Element Unification acumula daño crítico con impactos de habilidad del espíritu.''',
[('Summon: Ancient Spirit','Espíritu temporal que concede Four Elements cada vez que usa su habilidad.'),('Enhance: Spirit’s Benediction','Daño, tolerancia y curación de ambos mientras puedan contribuir.'),('Jointstrike: Corrode','Daño periódico y mayor daño recibido del espíritu; coordinación según espíritu activo.'),('Jointstrike: Destructive Attack','Daño coordinado de área o presión individual según espíritu activo.'),('Siphon / Seize Magic','Recuperar HP y MP / eliminar mejoras enemigas según el problema.'),('Command: Proxy / Cry of Terror','Compartir daño con espíritu a 25m / miedo. Mantén al espíritu vivo y cerca.')],
['Elige Fuego para área, Agua para MP, Viento para HP o Tierra para amenaza.','Usa Dimensional Control en su ventana tras invocación o habilidad de espíritu; añade Cold Shock y Combustion.','Consume Four Elements con Fusion antes de más acumulaciones. Con Ancient Spirit, responde a sus concesiones repetidas.','Jointstrike: Corrode antes de daño continuo. Rapid Scattershot durante tambaleo; defensa y miedo aparte.'],
'''Precisión conserva oportunidades de pasivas. Compara daño de ambos, recargas de invocación y umbrales de Fusion alcanzables. Su opción cargada de rango 12 cambia la ventana segura.

Daevanion puede mejorar Cold Shock, Fusion, invocaciones y Spirit Revitalization. Busca efecto y coste total en tu tablero regional; guarda todo con [builds](/builds).''',
'''**Cuatro invocaciones no abren Fusion:** observa activaciones de habilidad y acumulaciones reales.

**Agua no devuelve MP:** debe acertar; comprueba alcance, objetivo y espíritu activo.

**El espíritu atrae al enemigo:** Tierra genera amenaza alta; cambia si otro jugador debe tanquear.

Solo puede usar Agua o Viento para sostenerse. En party, encaja invocaciones con posición y perjuicios. Para [PvP](/pvp), conserva miedo, sello o disipación según enemigo y defensa antes de su acercamiento.''')

guide('spiritmaster','de',
'Beschwörer nutzt eine Kugel und Geister. Feuer liefert Flächen, Wasser MP, Wind HP und Erde Bedrohung. Geistfertigkeiten sammeln vier Elemente für Elemental Fusion; verbrauche sie, bevor weitere Stapel blockiert bleiben.',
'''Wähle ihn zur Koordination eigener Fernangriffe mit Geisteffekten und kurzen Auslösefenstern. Der aktive Geist verändert Heilung, Bedrohung und Jointstrike. [Jäger](/ranger) verwaltet weniger Beschwörungen; [Magier](/sorcerer) aufgeladene Zauber.

Fusion benötigt vier Stapel aus Geistfertigkeiten, nicht vier verschiedene Geister. Four Elements blockiert weitere Stapel bis zum Verbrauch. Status statt vier Beschwörungstasten beobachten. Vergleiche die [Klassen](/classes).''',
'''Cold Shock stellt MP her, Rang 8 verbessert Regeneration, Rang 12 verkürzt Combustion. Dessen Kostenoption und Dimensional Controls MP erhalten den Ablauf.

Genutzte Geister verbessern und Effekte wählen. Wasser stellt bei Angriffen MP ohne besondere Regenerationsoption her; Wind heilt deine HP. Erde erzeugt hohe Bedrohung: mit anderem Tank bewusst über den aktiven Geist entscheiden.

Spirit Strike verbessert beide Schadensquellen. Spirit Communion gibt Genauigkeit und Heilchancen für beide. Spirit Revitalization kann Beschwörungen bei Treffern verkürzen. Spirit's Descent ergänzt Schaden nach Beschwörung; Element Unification stapelt kritischen Schaden nach Geistfertigkeitstreffern.''',
[('Summon: Ancient Spirit','Temporärer Geist, der bei jeder Fertigkeitsnutzung Four Elements gibt.'),('Enhance: Spirit’s Benediction','Schaden, Toleranz und Heilung für beide während nutzbarer Kampfzeit.'),('Jointstrike: Corrode','Laufender Schaden und mehr eingehender Geistschaden; Koordination variiert mit aktivem Geist.'),('Jointstrike: Destructive Attack','Koordinierter Einzel- oder Flächenschaden je nach Geist.'),('Siphon / Seize Magic','HP und MP herstellen / gegnerische Buffs entfernen.'),('Command: Proxy / Cry of Terror','Schaden mit Geist innerhalb 25m teilen / Furcht. Geist am Leben und nahe halten.')],
['Feuer für Fläche, Wasser für MP, Wind für HP oder Erde für Bedrohung wählen.','Dimensional Control im kurzen Fenster nach Beschwörung oder Geistfertigkeit; Cold Shock und Combustion ergänzen.','Four Elements mit Fusion vor neuen Stapeln verbrauchen. Bei Ancient Spirit auf wiederholte Vergaben reagieren.','Jointstrike: Corrode vor anhaltendem Schaden. Rapid Scattershot bei Taumeln; Abwehr und Furcht separat.'],
'''Genauigkeit erhält passive Trefferchancen. Beide Schadensquellen, Beschwörungszeiten und erreichbare Fusion-Schwellen vergleichen. Die aufgeladene Rang-12-Option verändert das sichere Fenster.

Daevanion kann Cold Shock, Fusion, Geister und Spirit Revitalization verbessern. Auf regionalem Brett Effekt und Gesamtkosten suchen. Mit [Builds](/builds) sichern.''',
'''**Vier Beschwörungen öffnen Fusion nicht:** Geistfertigkeiten und wirkliche Stapel beobachten.

**Wasser liefert keine MP:** muss treffen; Reichweite, Ziel und aktiven Geist prüfen.

**Geist zieht Gegner an:** Erde erzeugt hohe Bedrohung; bei anderem Tank wechseln.

Solo Wasser oder Wind zur Regeneration; in Gruppen Beschwörungen mit Position und Debuffs abstimmen. Für [PvP](/pvp) Furcht, Siegel oder Entzauberung nach Gegner sowie Abwehr vor Annäherung behalten.''')

guide('chanter','en',
'Chanter uses a staff for melee damage and party support. Spinning Strike and Impactful Crush open Dark Crush; Marchutan’s Wrath and Ensnaring Mark add Stigma triggers. Keep Recuperation separate: it heals and removes one debuff before specialization.',
'''Choose Chanter for melee attacks, party mantras and decisions between damage and recovery. Unlike [Cleric](/cleric), you spend much of the loop close to the enemy while preserving group support. A damage setup does not supply every healing tool a difficult encounter needs.

With a Cleric, emphasize useful damage and complementary support. Without one, equip healing and shielding before entering as the healer. Read the [class comparison](/classes) if dedicated recovery is the role you prefer.''',
'''Onslaught supplies MP; its rank-8 recovery option improves sustain and rank 12 shortens Spinning Strike on hit. Rushing Smash's rank-8 on-kill reset helps repeated small pulls, not a boss without kills. Spinning Strike's rank-8 cooldown option improves trigger frequency.

Dark Crush has a rank-8 guaranteed-critical choice, a rank-12 chain and rank-16 cooldown removal. Until the last effect is selected, spread triggers around the actual cooldown. Recuperation already removes one debuff; rank 8 can improve cleansing or uses, while rank 12 adds percentage-HP recovery.

Protection Circle stacks through attacks and grants a party shield at ten stacks. Blessing of Life turns attack into Heal Boost. Attack Preparation improves accuracy and damage. Earth's Promise reduces target tolerance but does not combine with Cleric's Chain of Torment; do not count the same reduction twice.''',
[('Undefeated Mantra','Party damage and tolerance. Its damage boost does not stack with Cleric Light of Protection; higher skill level applies, with Mantra winning equal levels.'),('Sprint Mantra','Movement and healing on attacks. Useful utility after the main party role is covered.'),('Marchutan’s Wrath / Ensnaring Mark','Two ranged Dark Crush triggers; each opens a three-second window. Ensnaring Mark also supplies Seal.'),('Impeding Authority / Healing Touch','Party shielding / direct party healing. Replace a damage trigger when recovery is insufficient.'),('Power of the Storm','Temporary party speed and cooldown benefit. Use while the party can attack, not during a forced retreat.'),('Focused Defense / Barrier Spell','Timed personal block / short party HP-floor protection. Certain powerful attacks bypass Barrier Spell.')],
['Keep equipped mantras active. Approach with Rushing Smash without moving the enemy away from the tank’s position.','Spinning Strike → available Dark Crush. Before rank-16 cooldown removal, wait for its cooldown before another trigger.','Impactful Crush → Dark Crush, then an equipped Marchutan’s Wrath or Ensnaring Mark trigger when another follow-up can be used. Fill gaps with Onslaught.','Use Gust Rampage during Stagger. Interrupt for Recuperation, Healing Touch or shielding when the party needs them; do not put recovery inside the repeated damage chain.'],
'''Attack improves both damage and the healing contribution from Blessing of Life. Accuracy keeps Onslaught's cooldown feed and Protection Circle stacks working. Prioritize Spinning Strike and Dark Crush thresholds, then useful damage passives; improve Recuperation or support Stigmas when recovery is the failure.

Keep a damage configuration and a support configuration with their actual Stigma slots. Use [builds](/builds) for skill-rank and point budgets rather than copying a fully developed Daevanion route.''',
'''**Dark Crush does not open:** use one of its actual triggers and respond within the short window. Several triggers together waste their separate opportunities.

**The fast loop stops:** rank-16 cooldown removal must be unlocked and selected; earlier ranks need pauses between windows.

**Cleansing feels weak:** Recuperation removes one effect normally. Select its extra-cleansing option or equip Healing Touch's later cleanse when several removable effects are the problem.

Solo keeps attacks and recovery; parties choose complementary buffs and enough support. For [PvP](/pvp), keep Defiance and manual healing accessible while moving and under pressure.''')

guide('chanter','ja',
'チャンターはスタッフで近接攻撃と支援。Spinning StrikeとImpactful Crush、スティグマのMarchutan’s WrathとEnsnaring MarkがDark Crushを開きます。Recuperationは基本で回復と減益1個解除を持つため別操作にします。',
'''近接攻撃、味方マントラ、攻撃と回復の切り替えを楽しむ人向け。[クレリック](/cleric)より敵の近くで攻撃しながら支援を保ちます。攻撃構成だけで難しい戦闘の回復が足りるとは限りません。

クレリックがいる時は補完的な攻撃と支援。いない時に回復役なら入場前に回復と盾を装備。[クラス比較](/classes)で役割を選べます。''',
'''OnslaughtはMP回復、ランク8で回復強化、ランク12で命中時Spinning Strike短縮。Rushing Smashのランク8撃破リセットは小敵の反復向けで、撃破のないボスには働きません。Spinning Strikeのランク8短縮で発動頻度を増やせます。

Dark Crushはランク8の確定クリティカル、ランク12の連携、ランク16の再使用削除が候補。最後の特化前は再使用に合わせて発動を分散。Recuperationは基本で減益1個解除。ランク8で解除や回数、ランク12で割合HP回復を強化できます。

Protection Circleは攻撃で10層ため味方盾。Blessing of Lifeは攻撃力からHeal Boost、Attack Preparationは命中と火力。Earth's Promiseの耐性低下はClericのChain of Tormentと併用効果を得られません。''',
[('Undefeated Mantra','味方火力と耐性。Light of Protectionの火力とは重複せず高ランク優先。同ランクはMantra。'),('Sprint Mantra','移動と攻撃時回復。主要役割を確保して追加。'),('Marchutan’s Wrath / Ensnaring Mark','3秒のDark Crush発動時間。後者は封印も持ちます。'),('Impeding Authority / Healing Touch','味方盾／直接回復。回復不足なら攻撃発動枠を交換。'),('Power of the Storm','味方速度と再使用の一時強化。退避中ではなく攻撃可能時間へ。'),('Focused Defense / Barrier Spell','手動ブロック／短い味方HP下限保護。一部強攻撃は後者を無視。')],
['装備したマントラを維持。敵をタンク位置から動かさずRushing Smashで接近。','Spinning StrikeからDark Crush。ランク16の再使用削除前は待ちます。','Impactful CrushからDark Crush、次の使用可能時間にMarchutan’s WrathやEnsnaring Mark。合間にOnslaught。','スタガーはGust Rampage。味方のためRecuperation、Healing Touch、盾で攻撃を中断。'],
'''攻撃力は火力とBlessing of Lifeの回復に影響。命中はOnslaught短縮とProtection Circleの層を維持します。Spinning StrikeとDark Crushの特化、使う火力パッシブを優先し、回復不足ならRecuperationや支援を強化。

攻撃と支援の構成を実際の枠数で保存。[ビルド](/builds)でランクとポイントを管理します。''',
'''**Dark Crushが出ない：**実際の発動スキルを使い短時間内に追撃。発動を一度に使うと機会を無駄にします。

**高速連携が止まる：**ランク16の再使用削除を解放・選択。それまでは待機が必要。

**解除が足りない：**Recuperationは基本1個。複数の解除可能効果なら特化や後のHealing Touch解除を選びます。

ソロは攻撃と回復、パーティーは補完バフと支援。[PvP](/pvp)は移動中もDefianceと手動回復へアクセスできる操作にします。''')

guide('chanter','es',
'Cantor usa bastón para daño y apoyo. Spinning Strike e Impactful Crush abren Dark Crush; Marchutan’s Wrath y Ensnaring Mark añaden disparadores de estigma. Separa Recuperation: cura y elimina un perjuicio sin especialización.',
'''Elígelo para daño cercano, mantras y decisiones entre atacar y recuperar. Frente a [Clérigo](/cleric), pasas más tiempo junto al enemigo mientras sostienes al grupo. Una configuración ofensiva no cubre toda la curación de encuentros difíciles.

Con Clérigo, busca daño y apoyo complementario. Sin él, equipa curación y escudos antes de asumir recuperación. Compara las [clases](/classes).''',
'''Onslaught aporta MP, mejora recuperación en rango 8 y reduce Spinning Strike al acertar en rango 12. El reinicio por muerte de Rushing Smash en rango 8 sirve para enemigos pequeños, no para jefes sin bajas. Menor recarga de Spinning Strike en rango 8 abre más ventanas.

Dark Crush ofrece crítico garantizado en rango 8, cadena en rango 12 y eliminación de recarga en rango 16. Antes de esta última opción, reparte disparadores según su recarga. Recuperation ya elimina un perjuicio; rango 8 mejora disipación o usos y rango 12 añade curación porcentual.

Protection Circle acumula ataques y da escudo de party a diez cargas. Blessing of Life convierte ataque en Heal Boost; Attack Preparation mejora precisión y daño. Earth's Promise no combina su reducción de tolerancia con Chain of Torment del Clérigo.''',
[('Undefeated Mantra','Daño y tolerancia de party. Su daño no se acumula con Light of Protection: gana el nivel mayor y Mantra a igualdad.'),('Sprint Mantra','Movimiento y curación por ataques tras cubrir la función principal.'),('Marchutan’s Wrath / Ensnaring Mark','Disparadores a distancia de tres segundos para Dark Crush; el segundo también sella.'),('Impeding Authority / Healing Touch','Escudo / curación directa de party. Cambia un disparador si falta recuperación.'),('Power of the Storm','Velocidad y recargas temporales mientras el grupo pueda atacar.'),('Focused Defense / Barrier Spell','Bloqueo personal / protección breve del mínimo de HP. Ciertos ataques atraviesan Barrier Spell.')],
['Mantén mantras equipados. Rushing Smash sin sacar al enemigo de la posición del tanque.','Spinning Strike → Dark Crush disponible. Espera la recarga antes de rango 16 seleccionado.','Impactful Crush → Dark Crush; después Marchutan’s Wrath o Ensnaring Mark cuando pueda usarse otro seguimiento. Onslaught entre ventanas.','Gust Rampage durante tambaleo. Interrumpe para Recuperation, Healing Touch o escudos; recuperación fuera de la cadena ofensiva.'],
'''Ataque mejora daño y curación mediante Blessing of Life. Precisión mantiene reducciones de Onslaught y Protection Circle. Prioriza umbrales de Spinning Strike y Dark Crush, luego pasivas; mejora Recuperation o estigmas de apoyo ante falta de curación.

Guarda una configuración de daño y otra de apoyo con las ranuras reales. Usa [builds](/builds) para rangos y presupuesto de puntos.''',
'''**Dark Crush no aparece:** usa un disparador real y responde en su ventana. Usar varios juntos desperdicia oportunidades.

**El ciclo rápido se para:** exige eliminación de recarga de rango 16 seleccionada; antes debes esperar.

**Falta disipación:** Recuperation quita uno normalmente. Para varios efectos, elige su mejora o disipación posterior de Healing Touch.

Solo mantiene daño y recuperación; party, mejoras complementarias y apoyo suficiente. En [PvP](/pvp), deja Defiance y curación manual accesibles en movimiento.''')

guide('chanter','de',
'Kantor nutzt einen Stab für Nahschaden und Unterstützung. Spinning Strike und Impactful Crush öffnen Dark Crush; Marchutan’s Wrath und Ensnaring Mark ergänzen Stigma-Auslöser. Recuperation heilt und entfernt schon ohne Spezialisierung einen Debuff.',
'''Wähle ihn für Nahkampf, Mantras und Entscheidungen zwischen Angriff und Heilung. Gegenüber [Kleriker](/cleric) bleibst du öfter am Gegner und unterstützt nebenbei. Ein Schadensbuild deckt nicht jeden Heilbedarf schwieriger Kämpfe.

Mit Kleriker ergänzenden Schaden und Support wählen. Ohne ihn Heilung und Schilde vor Übernahme der Heilerrolle ausrüsten. Vergleiche die [Klassen](/classes).''',
'''Onslaught gibt MP, auf Rang 8 mehr Regeneration und auf Rang 12 Spinning-Strike-Verkürzung bei Treffern. Rushing Smashes Rang-8-Reset nach Tötung hilft bei kleinen Gegnern, nicht am Boss ohne Tötungen. Spinning Strikes Rang-8-Abklingoption öffnet mehr Fenster.

Dark Crush bietet garantierte kritische Treffer auf Rang 8, Kette auf Rang 12 und keine Abklingzeit auf Rang 16. Vor der letzten gewählten Option Auslöser verteilen. Recuperation entfernt bereits einen Debuff; Rang 8 verbessert Reinigung oder Nutzungen, Rang 12 ergänzt prozentuale Heilung.

Protection Circle gibt nach zehn Angriffsstapeln einen Gruppenschild. Blessing of Life wandelt Angriff in Heal Boost; Attack Preparation verbessert Genauigkeit und Schaden. Earth's Promise kombiniert seine Toleranzreduktion nicht mit Klerikers Chain of Torment.''',
[('Undefeated Mantra','Gruppenschaden und Toleranz. Schaden stapelt nicht mit Light of Protection: höherer Rang gilt, bei Gleichstand Mantra.'),('Sprint Mantra','Bewegung und Heilung bei Angriffen nach gesicherter Hauptrolle.'),('Marchutan’s Wrath / Ensnaring Mark','Fern-Auslöser für drei Sekunden Dark Crush; letzteres versiegelt zusätzlich.'),('Impeding Authority / Healing Touch','Gruppenschild / direkte Heilung. Bei Heilbedarf Schadensauslöser ersetzen.'),('Power of the Storm','Temporäres Gruppentempo und Abklingvorteil während Angriffszeit.'),('Focused Defense / Barrier Spell','Eigener Block / kurze HP-Untergrenze der Gruppe. Bestimmte Angriffe umgehen Barrier Spell.')],
['Ausgerüstete Mantras halten. Rushing Smash ohne Verschieben aus der Tankposition.','Spinning Strike → verfügbares Dark Crush. Vor gewähltem Rang-16-Effekt Abklingzeit abwarten.','Impactful Crush → Dark Crush; dann Marchutan’s Wrath oder Ensnaring Mark bei nutzbarem Folgefenster. Onslaught dazwischen.','Gust Rampage bei Taumeln. Für Recuperation, Healing Touch oder Schild unterbrechen; Heilung separat.'],
'''Angriff verbessert Schaden und Heilung durch Blessing of Life. Genauigkeit erhält Onslaught-Verkürzungen und Protection Circle. Spinning-Strike- und Dark-Crush-Schwellen priorisieren, dann passive Offensive; bei Heilbedarf Recuperation oder Support-Stigmas.

Schadens- und Support-Konfiguration mit wirklichen Plätzen sichern. [Builds](/builds) erklärt Ränge und Punktebudget.''',
'''**Dark Crush fehlt:** echten Auslöser nutzen und im kurzen Fenster reagieren. Mehrere gleichzeitig verschwenden Möglichkeiten.

**Schneller Ablauf stoppt:** Rang-16-Abklingentfernung muss ausgewählt sein; vorher zwischen Fenstern warten.

**Reinigung reicht nicht:** Recuperation entfernt regulär einen Effekt. Bei mehreren entfernbaren Effekten Option oder spätere Healing-Touch-Reinigung wählen.

Solo Schaden und Heilung; Gruppe ergänzende Buffs und Support. Für [PvP](/pvp) Defiance und manuelle Heilung in Bewegung erreichbar halten.''')

legacy = {
    'gladiator': {'gladiator-role':'gladiator-role','starter-build':'starter-build','stigma-choices':'stigmas-and-tanking','manual-loop':'manual-attack-loop','gear-and-daevanion':'daevanion-priorities','gladiator-troubleshooting':'solo-party-and-pvp'},
    'ranger': {'ranger-role':'ranger-playstyle','starter-build':'leveling-build','stigma-choices':'damage-and-passives','gear-and-daevanion':'daevanion-build'},
    'spiritmaster': {'spiritmaster-role':'spiritmaster-playstyle','starter-build':'starter-skills','manual-loop':'summon-sequence','gear-and-daevanion':'daevanion-build'},
    'chanter': {'chanter-role':'chanter-playstyle','starter-build':'starting-priorities','manual-loop':'damage-loop','gear-and-daevanion':'progression-and-old-builds'},
}
for slug,copies in base.pages.items():
    for loc,copy in copies.items():
        body=copy['body']
        for old,new in legacy[slug].items(): body=body.replace('id="'+old+'"','id="'+new+'"')
        if slug in ['ranger','spiritmaster']: body=body.replace('<h2 id="'+slug+'-troubleshooting">','<span id="solo-party-and-pvp" />\n\n<h2 id="'+slug+'-troubleshooting">')
        if slug=='chanter':
            body=body.replace('<h2 id="stigma-choices">','<span id="party-role-switch" />\n\n<h2 id="stigma-choices">')
            body=body.replace('<h2 id="progression-and-old-builds">','<GuideVisual id="workflow" />\n\n<h2 id="progression-and-old-builds">')
            body=body.replace('<h2 id="chanter-troubleshooting">','<GuideEquipment />\n\n<h2 id="chanter-troubleshooting">')
        copy['body']=body
        oldmeta=json.loads((ROOT/f'src/content/{loc}/{slug}.json').read_text(encoding='utf8'))
        copy['oldVisuals']=oldmeta['visuals']
base.write_pages()
for slug,copies in base.pages.items():
    for loc,copy in copies.items():
        p=ROOT/f'src/content/{loc}/{slug}.json';m=json.loads(p.read_text(encoding='utf8'))
        if slug=='chanter': m['visuals']['workflow']=copy['oldVisuals']['workflow']
        p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Expanded the four existing class guides and preserved their old anchors.')
