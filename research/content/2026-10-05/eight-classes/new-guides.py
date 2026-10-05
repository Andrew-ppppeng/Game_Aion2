import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOCALES = ['en', 'ja', 'es', 'de']
pages = {}

HEADINGS = {
    'en': ['Role and reasons to choose it', 'Active skills and triggers', 'Early skill and passive priorities', 'Choose Stigmas for the encounter', 'Manual opener and combat loop', 'Gear and Daevanion decisions', 'Adjustments and troubleshooting', 'Complete skill list'],
    'ja': ['役割と選ぶ理由', 'アクティブスキルと発動条件', '序盤のスキルとパッシブの優先度', '戦闘に合わせたスティグマ', '手動の起手と攻撃ループ', '装備とDaevanionの判断', '調整と問題の解決', '全スキル一覧'],
    'es': ['Función y motivos para elegirla', 'Habilidades activas y condiciones', 'Prioridades iniciales de habilidades y pasivas', 'Estigmas según el encuentro', 'Apertura y ciclo manual', 'Equipo y Daevanion', 'Ajustes y resolución de problemas', 'Lista completa de habilidades'],
    'de': ['Rolle und Gründe für die Klassenwahl', 'Aktive Fertigkeiten und Auslöser', 'Frühe Fertigkeiten und passive Prioritäten', 'Stigmas für den Kampf wählen', 'Manuelle Eröffnung und Kampfablauf', 'Ausrüstung und Daevanion', 'Anpassungen und Problemlösung', 'Vollständige Fertigkeitenliste'],
}

def compact(slug, locale, title, description, summary, answer, role, upgrades, choices, loop, gear, faq, next_slug='builds'):
    h = HEADINGS[locale]
    ids = [slug+'-role', 'key-skills', 'starter-build', 'stigma-choices', 'manual-loop', 'gear-and-daevanion', slug+'-troubleshooting', 'all-skills']
    th = {'en': '| Choice | Use and condition |', 'ja': '| 選択肢 | 用途と条件 |', 'es': '| Opción | Uso y condición |', 'de': '| Wahl | Nutzen und Bedingung |'}[locale]
    table = th+'\n| --- | --- |\n'+'\n'.join('| '+a+' | '+b+' |' for a, b in choices)
    sections = [role, f'<GuideSkillFocus classId="{slug}" />', upgrades, table,
                '\n'.join(f'{i+1}. {s}' for i,s in enumerate(loop)), gear, faq,
                f'<GuideSkillList classId="{slug}" />']
    body = answer+'\n\n<GuideVisual id="topic" />\n\n'+'\n\n'.join(f'<h2 id="{id}">{title}</h2>\n\n{text}' for id,title,text in zip(ids,h,sections))+f'\n\n<GuideNext slug="{next_slug}" />\n'
    page(slug, locale, title, description, summary, answer, body)

def page(slug, locale, title, description, summary, answer, body):
    pages.setdefault(slug, {})[locale] = dict(title=title, description=description, summary=summary, quickAnswer=answer, body=body)

page('templar', 'en', 'AION 2 Templar: Skills, Tanking and PvE Builds',
     'Learn Templar skills, Judgment triggers, threat management, Stigma choices and safe Punishment windows for solo play, dungeons and PvP.',
     'Build a shield-based frontline character around Judgment triggers, Punishment, threat and timed protection.',
     'Templar uses a sword and shield. Connect shield skills to Judgment, use Pummel to shorten Punishment with its selected option, and keep Taunt and manual protection ready when tanking.', '''
Templar combines a sword and shield with threat, charged damage and party protection. Choose it if you want to keep enemies positioned for the party while reacting to incoming attacks. Its damage depends on using short follow-up windows rather than simply waiting behind a shield.

<GuideVisual id="topic" />

<h2 id="templar-role">Choose Templar for frontline control</h2>

Your party job adds three decisions to the damage loop: where the enemy faces, when to use protection and when to recover threat. Keep the enemy's front directed away from allies who need its back. A gap closer that moves the boss out of their attacks can cost the group more than it adds to your damage.

[Gladiator](/gladiator) also supplies frontline damage and block-related party benefits. Choose Templar for the shield-trigger loop and its larger selection of protection and damage-sharing tools. Compare the full [class roster](/classes) before committing to a role.

<h2 id="key-skills">Active skills and their trigger conditions</h2>

Shield Smite and Warding Strike each open Judgment briefly. Shield Rush and the Stigma Doom Shield also open it. Use the follow-up while the window is active; activating several triggers together does not make their windows accumulate.

<GuideSkillFocus classId="templar" />

<h2 id="starter-build">Spend early points on a working loop</h2>

Choose the MP-restoring option on Vicious Strike while mana limits your attacks. At skill rank 12, its Warding Strike cooldown reduction connects regular attacks to recovery and another Judgment trigger. Shield Smite's rank-8 resource option removes its MP cost and restores MP on a hit.

Pummel's rank-12 option reduces Punishment's cooldown on hit. Punishment's faster-cast option helps complete its charge before movement is required; its rank-12 mobile option lets you change position while using it. Select the effects after unlocking them.

For passives, Fury gives the party a damage buff after you block; Insulting Roar adds threat and an attack buff after a front attack. Ironclad Defense improves defense and endurance. Fury's party damage boost overlaps with Gladiator's Experienced Counterstrike, so their presence does not multiply that same benefit.

<h2 id="stigma-choices">Stigmas: damage, threat and protection</h2>

| Choice | Use it for | When to change the slot |
| --- | --- | --- |
| Taunt | Threat and an enemy attack/accuracy debuff | Keep when responsible for holding the enemy |
| Doom Shield | Approach, protection and a Judgment trigger | Preserve manual control over where you move |
| Executing Blade | Damage and a defense debuff | Use inside a safe attack window |
| Battlefield Banner | Converts defense into a temporary attack benefit | Coordinate with Punishment rather than spending it during movement |
| Shield of Protection / Nezekan's Shield | Timed block / party shielding | Replace a damage slot when incoming damage is the failure |
| Second Skin / Comrade in Arms | Personal damage tolerance / sharing an ally's damage | Damage sharing adds damage to you; use it with enough survival |

These are choices for the available slots, not six simultaneously equipped skills. Start with the threat and protection the encounter needs, then fill the remaining slots with useful damage. An offensive beginner setup does not guarantee that a harder encounter needs no defense.

<h2 id="manual-loop">A manual attack loop with room to tank</h2>

1. Approach and establish the enemy's position. Use Taunt when you need its threat and debuff.
2. Shield Smite → Judgment. Use Warding Strike → Judgment in the next available window.
3. Use Battlefield Banner when equipped, then charge Punishment during a safe interval. Resume Vicious Strike and Pummel to feed the selected cooldown reductions.
4. Use Annihilate when its condition appears; use Flash Rampage during Stagger. Interrupt the damage loop for a block, movement or party protection.

Keep Taunt, protection and Defiance independent of any repeating damage chain. Judge a block by the enemy attack timing; a long chain cannot decide which attack deserves your defensive button.

<h2 id="gear-and-daevanion">Gear and Daevanion decisions</h2>

Prioritize enough accuracy to land the attacks that feed cooldowns. Choose routes to Vicious Strike, Pummel, Shield Smite and Punishment when they unlock the next useful specialization. Compare the shortest route to the same skill across boards before spending points.

After the loop works, combat speed and cooldown improvements increase useful attack opportunities. Add defense, HP or block investment when your tanking deaths prevent the group from completing the encounter. Critical-damage investment needs actual critical hits; measure that before giving it priority over a working trigger or protection skill. The [builds guide](/builds) covers skill ranks, point sources and saving a configuration.

<h2 id="templar-troubleshooting">Solo, party and PvP adjustments</h2>

**Judgment does not appear:** use one shield trigger manually, stay within attack range and use the short window. Confirm the skill itself is ready before spending another trigger.

**Punishment is repeatedly canceled:** choose a shorter or mobile cast, or wait for a longer safe window. A completed smaller attack contributes more than a charge you never finish.

**The boss switches targets:** use your threat tools, resume landed attacks and check positioning. Do not chase damage at the cost of the tanking job.

**Solo pulls take too long:** use Poach's kill reset for suitable small enemies and retain the offensive loop. **Party damage is too high:** replace a damage Stigma with the appropriate block, shield or tolerance tool. For [PvP](/pvp), revisit pulls, control resistance, Defiance and protection rather than copying a stationary boss opener.

<h2 id="all-skills">Complete Templar skill list</h2>

<GuideSkillList classId="templar" />

<GuideNext slug="builds" />
''')

page('templar', 'ja', 'AION 2 テンプラー：スキル・タンク・PvEビルド',
     'テンプラーのJudgment発動、敵対値管理、スティグマ、Punishmentの安全な使い方を解説。ソロ・パーティ・PvPの調整に対応。',
     '盾スキルからJudgmentにつなげ、Punishment、敵対値、タイミングを合わせた防御で前衛を組み立てます。',
     'テンプラーは剣と盾を使います。盾スキルからJudgmentにつなげ、Pummelの特化でPunishmentの再使用を短縮。タンク時はTauntと防御をすぐ使えるようにします。', '''
テンプラーは剣と盾で敵対値、チャージ攻撃、パーティ防御を扱う前衛です。敵を味方が攻撃しやすい位置に保ち、攻撃のタイミングに合わせて防御したい人に向きます。盾を構えて待つだけでなく、短い追撃時間を使うことが攻撃の軸になります。

<GuideVisual id="topic" />

<h2 id="templar-role">前衛で敵の位置を管理する</h2>

パーティでは攻撃に加え、敵の向き、防御のタイミング、敵対値の回復を判断します。背後を必要とする味方から敵の正面を離しましょう。接近スキルでボスを味方の攻撃範囲外へ動かすと、自分の攻撃以上にパーティの損失が増えます。

[グラディエーター](/gladiator)も前衛攻撃とブロック時の支援を持ちます。盾の追撃ループと豊富な防御・ダメージ分担を使いたいならテンプラーを検討してください。[全クラス](/classes)でも役割を比較できます。

<h2 id="key-skills">アクティブスキルと発動条件</h2>

Shield SmiteとWarding Strikeはそれぞれ短時間Judgmentを使用可能にします。Shield RushとスティグマDoom Shieldも起点です。複数の起点を一度に使っても、追撃時間をためておけるわけではありません。

<GuideSkillFocus classId="templar" />

<h2 id="starter-build">最初に機能するループを作る</h2>

MPが攻撃を制限する間はVicious StrikeのMP回復特化を使います。ランク12のWarding Strike再使用短縮で、通常攻撃から回復とJudgmentにつながります。Shield Smiteのランク8特化はMP消費をなくし、命中時にMPを回復します。

Pummelのランク12特化はPunishmentの再使用を命中時に短縮します。Punishmentの高速化は移動前のチャージ完了を助け、ランク12の移動可能化は使用中の位置変更に役立ちます。解放した効果は別途選択してください。

Furyはブロック後にパーティを攻撃強化します。Insulting Roarは敵対値と正面攻撃時の攻撃力を増やし、Ironclad Defenseは防御と耐久を高めます。Furyのパーティダメージ強化はグラディエーターのExperienced Counterstrikeと重複しません。

<h2 id="stigma-choices">攻撃・敵対値・防御のスティグマ</h2>

| 選択肢 | 用途 | 枠を調整する場面 |
| --- | --- | --- |
| Taunt | 敵対値と敵の攻撃・命中低下 | 敵を保持する担当なら維持 |
| Doom Shield | 接近、防護、Judgment発動 | 移動先を手動で管理 |
| Executing Blade | 攻撃と防御低下 | 安全な攻撃時間に使用 |
| Battlefield Banner | 防御を一時的な攻撃力へ変換 | 移動中ではなくPunishmentに合わせる |
| Shield of Protection / Nezekan's Shield | タイミングを合わせたブロック／パーティの盾 | 被ダメージが敗因なら攻撃枠と交換 |
| Second Skin / Comrade in Arms | 自分の耐性／味方とのダメージ分担 | 分担は自分の被ダメージを増やすため生存力が必要 |

これは枠に合わせて選ぶ候補であり、6つ同時装備ではありません。必要な敵対値と防御を確保してから攻撃を追加します。初心者向け攻撃構成が、難しい戦闘でも防御不要であることを意味しません。

<h2 id="manual-loop">タンクの判断を残す攻撃手順</h2>

1. 接近して敵の位置を決め、必要な敵対値と減益のためTauntを使います。
2. Shield Smite → Judgment。次の使用可能時間にWarding Strike → Judgment。
3. 装備していればBattlefield Bannerを使い、安全な時間にPunishmentをチャージ。Vicious StrikeとPummelで選んだ再使用短縮を進めます。
4. Annihilateは発動条件が満たされた時、Flash Rampageはスタガー中に使用。防御、移動、味方の保護が必要なら攻撃を中断します。

Taunt、防御、Defianceは反復攻撃から分けます。どの攻撃を防ぐべきかは敵の動作を見て判断します。

<h2 id="gear-and-daevanion">装備とDaevanionの判断</h2>

再使用短縮を生む攻撃が命中するだけの命中を確保します。次の特化に届くならVicious Strike、Pummel、Shield Smite、Punishmentの強化を選び、同じスキルへの最短経路を各盤で比較します。

ループが成立してから戦闘速度と再使用短縮で攻撃機会を増やします。タンクの死亡で進めない場合は防御、HP、ブロックを追加。クリティカルダメージは実際にクリティカルが出る構成で役立ちます。[ビルドガイド](/builds)でランク、ポイント源、構成保存を確認できます。

<h2 id="templar-troubleshooting">ソロ・パーティ・PvPの調整</h2>

**Judgmentが出ない：**盾の起点を1つ手動で使い、射程内で短い時間に追撃します。再使用待ち中に起点を重ねないようにします。

**Punishmentが中断される：**高速化、移動可能化、長い安全時間を選びます。完了できる攻撃を優先します。

**ボスが別の味方を狙う：**敵対値スキルと命中する攻撃を使い、位置を整えます。攻撃のためにタンクの仕事を捨てないようにします。

**ソロが遅い：**適した雑魚にはPoachの撃破リセットと攻撃ループを使用。**パーティの被害が大きい：**攻撃枠をブロック、盾、耐性へ交換。[PvP](/pvp)では引き寄せ、行動阻害耐性、Defiance、防御を組み直します。

<h2 id="all-skills">テンプラーの全スキル</h2>

<GuideSkillList classId="templar" />

<GuideNext slug="builds" />
''')

page('templar', 'es', 'AION 2 Templario: habilidades, tanque y builds PvE',
     'Aprende los activadores de Judgment, amenaza, estigmas y ventanas seguras de Punishment para jugar solo, en mazmorras o en PvP.',
     'Combina espada y escudo con activadores de Judgment, Punishment, amenaza y protección a tiempo.',
     'Templario usa espada y escudo. Enlaza habilidades de escudo con Judgment, selecciona la reducción de Punishment en Pummel y conserva Taunt y protección manual cuando seas tanque.', '''
Templario combina espada y escudo con amenaza, ataques cargados y protección del grupo. Encaja si quieres colocar enemigos para tus aliados y reaccionar al daño entrante. Su daño depende de aprovechar ventanas de seguimiento cortas.

<GuideVisual id="topic" />

<h2 id="templar-role">Controlar la primera línea</h2>

Como tanque decides hacia dónde mira el enemigo, cuándo proteger y cuándo recuperar amenaza. Aparta su frente de aliados que atacan por detrás. Mover un jefe fuera del alcance del grupo puede costar más daño del que añade tu acercamiento.

[Gladiador](/gladiator) también ofrece daño frontal y beneficios tras bloquear. Elige Templario por su ciclo de escudo y sus opciones de protección y reparto de daño. Compara las [ocho clases](/classes) antes de comprometerte con una función.

<h2 id="key-skills">Habilidades activas y condiciones</h2>

Shield Smite y Warding Strike habilitan Judgment brevemente. Shield Rush y el estigma Doom Shield también lo hacen. Consume el seguimiento dentro de su ventana: activar varios iniciadores juntos no acumula sus duraciones.

<GuideSkillFocus classId="templar" />

<h2 id="starter-build">Invertir en un ciclo que funcione</h2>

Elige recuperación de MP en Vicious Strike mientras el maná limite tus ataques. Su opción de rango 12 reduce Warding Strike, conectando ataques normales con recuperación y otro Judgment. La opción de rango 8 de Shield Smite elimina su coste y devuelve MP al golpear.

La opción de rango 12 de Pummel reduce Punishment al golpear. Lanzar Punishment más rápido ayuda a acabar antes de una mecánica; su opción móvil de rango 12 permite recolocarte durante la carga. Selecciona los efectos después de desbloquearlos.

Fury mejora el daño del grupo tras bloquear; Insulting Roar aporta amenaza y ataque tras un golpe frontal. Ironclad Defense aumenta defensa y resistencia. La mejora de daño de Fury se solapa con Experienced Counterstrike de Gladiador: no multipliques el mismo beneficio por llevar ambos.

<h2 id="stigma-choices">Estigmas de daño, amenaza y protección</h2>

| Opción | Utilidad | Cuándo ajustar la ranura |
| --- | --- | --- |
| Taunt | Amenaza y reducción de ataque/precisión enemiga | Consérvalo si debes retener al enemigo |
| Doom Shield | Acercamiento, protección y activación de Judgment | Controla manualmente dónde te desplazas |
| Executing Blade | Daño y reducción de defensa | Úsalo dentro de una ventana segura |
| Battlefield Banner | Convierte defensa en ataque temporal | Coordínalo con Punishment, no con desplazamientos |
| Shield of Protection / Nezekan's Shield | Bloqueo a tiempo / escudo del grupo | Sustituye daño si el problema es daño entrante |
| Second Skin / Comrade in Arms | Tolerancia propia / compartir daño de un aliado | Compartir aumenta el daño que recibes; exige supervivencia |

Son alternativas para tus ranuras disponibles, no seis habilidades equipadas a la vez. Asegura amenaza y protección necesarias y añade daño en las ranuras restantes. Un inicio ofensivo no demuestra que el contenido difícil no requiera defensa.

<h2 id="manual-loop">Ciclo manual que deja espacio para tanquear</h2>

1. Acércate y coloca al enemigo. Usa Taunt cuando necesites amenaza y su perjuicio.
2. Shield Smite → Judgment. En la siguiente ventana, Warding Strike → Judgment.
3. Activa Battlefield Banner si está equipado y carga Punishment durante un intervalo seguro. Vuelve a Vicious Strike y Pummel para las reducciones seleccionadas.
4. Usa Annihilate cuando aparezca su condición y Flash Rampage durante tambaleo. Interrumpe el daño para bloquear, moverte o proteger al grupo.

Mantén Taunt, protección y Defiance fuera de una cadena repetida. Una cadena larga no decide qué ataque enemigo merece tu defensa.

<h2 id="gear-and-daevanion">Equipo y Daevanion</h2>

Consigue precisión suficiente para acertar los ataques que reducen recargas. Busca Vicious Strike, Pummel, Shield Smite y Punishment cuando permitan la siguiente especialización útil. Compara la ruta más corta hacia la misma habilidad entre tableros.

Una vez funciona el ciclo, velocidad de combate y recargas mejoran oportunidades. Añade defensa, HP o bloqueo si tus muertes impiden terminar la pelea. El daño crítico necesita críticos reales; compruébalo antes de priorizarlo sobre un activador o protección. La [guía de builds](/builds) explica rangos, puntos y guardar configuraciones.

<h2 id="templar-troubleshooting">Ajustes solo, grupo y PvP</h2>

**No aparece Judgment:** prueba un activador de escudo manualmente, quédate a alcance y consume la ventana. Revisa su recarga antes de gastar otro activador.

**Punishment se cancela:** usa lanzamiento más rápido o móvil, o espera una ventana segura más larga.

**El jefe cambia de objetivo:** emplea amenaza, vuelve a acertar ataques y revisa la posición. No abandones la función de tanque por daño.

**Matar solo tarda mucho:** usa el reinicio de Poach con enemigos apropiados. **El grupo recibe demasiado daño:** cambia un estigma ofensivo por bloqueo, escudo o tolerancia. Para [PvP](/pvp), revisa atracciones, resistencia al control, Defiance y protección.

<h2 id="all-skills">Lista completa de habilidades de Templario</h2>

<GuideSkillList classId="templar" />

<GuideNext slug="builds" />
''')

page('templar', 'de', 'AION 2 Templer: Fertigkeiten, Tanken und PvE-Builds',
     'Lerne Judgment-Auslöser, Bedrohung, Stigmas und sichere Punishment-Fenster für Solo-Spiel, Gruppen und PvP.',
     'Verbinde Schwert und Schild mit Judgment-Auslösern, Punishment, Bedrohung und rechtzeitigem Schutz.',
     'Templer nutzen Schwert und Schild. Verbinde Schildfertigkeiten mit Judgment, wähle die Punishment-Verkürzung von Pummel und halte beim Tanken Taunt und manuelle Abwehr bereit.', '''
Templer verbinden Schwert und Schild mit Bedrohung, aufgeladenem Schaden und Gruppenschutz. Die Klasse passt, wenn du Gegner für deine Gruppe positionieren und auf eingehende Angriffe reagieren möchtest. Ihr Schaden lebt von kurzen Folgeangriffsfenstern.

<GuideVisual id="topic" />

<h2 id="templar-role">Die Front kontrollieren</h2>

Beim Tanken entscheidest du zusätzlich über Blickrichtung, Abwehrzeitpunkt und Bedrohung. Halte die Gegnerfront von Verbündeten fern, die den Rücken benötigen. Ein Vorstoß, der den Boss aus ihren Angriffen zieht, kann mehr Gruppenschaden kosten, als er dir bringt.

[Gladiator](/gladiator) bietet ebenfalls Frontschaden und Gruppenbuffs durch Blocken. Wähle Templer für den Schildablauf und die größere Auswahl an Schutz und Schadensaufteilung. Vergleiche die [acht Klassen](/classes) vor der Rollenwahl.

<h2 id="key-skills">Aktive Fertigkeiten und Voraussetzungen</h2>

Shield Smite und Warding Strike öffnen Judgment kurz. Shield Rush und das Stigma Doom Shield tun dies ebenfalls. Nutze den Folgeangriff im Fenster; mehrere gleichzeitig eingesetzte Auslöser sammeln ihre Dauer nicht an.

<GuideSkillFocus classId="templar" />

<h2 id="starter-build">Frühe Punkte für einen funktionierenden Ablauf</h2>

Wähle die MP-Regeneration von Vicious Strike, solange Mana deine Angriffe begrenzt. Die Rang-12-Option verkürzt Warding Strike und verbindet normale Angriffe mit Heilung und Judgment. Die Rang-8-Option von Shield Smite entfernt die MP-Kosten und stellt bei Treffern MP her.

Pummels Rang-12-Option verkürzt Punishment bei Treffern. Schnellere Ausführung hilft vor Bewegungsmechaniken; die mobile Rang-12-Option erlaubt Positionierung während der Nutzung. Wähle freigeschaltete Effekte gesondert aus.

Fury verstärkt die Gruppe nach einem Block. Insulting Roar erhöht Bedrohung und Angriff nach einem Fronttreffer. Ironclad Defense verbessert Verteidigung und Ausdauer. Der Gruppenschadensbuff von Fury überschneidet sich mit Experienced Counterstrike des Gladiators und wird dadurch nicht verdoppelt.

<h2 id="stigma-choices">Stigmas für Schaden, Bedrohung und Schutz</h2>

| Wahl | Nutzen | Wann den Platz ändern |
| --- | --- | --- |
| Taunt | Bedrohung sowie weniger Gegnerangriff und Genauigkeit | Behalten, wenn du den Gegner halten sollst |
| Doom Shield | Annäherung, Schutz und Judgment-Auslösung | Bewegungsziel manuell kontrollieren |
| Executing Blade | Schaden und Verteidigungsdebuff | Im sicheren Angriffsfenster nutzen |
| Battlefield Banner | Verteidigung wird zum vorübergehenden Angriffsbonus | Mit Punishment statt Bewegung abstimmen |
| Shield of Protection / Nezekan's Shield | Gezielter Block / Gruppenschild | Schadensplatz ersetzen, wenn eingehender Schaden das Problem ist |
| Second Skin / Comrade in Arms | Eigene Toleranz / Schaden mit einem Verbündeten teilen | Geteilter Schaden belastet dich zusätzlich; genug Überleben nötig |

Dies sind Alternativen für verfügbare Plätze, keine sechs gleichzeitig ausgerüsteten Fertigkeiten. Sichere nötige Bedrohung und Schutz, dann ergänze Schaden. Ein offensiver Einstieg beweist nicht, dass schwerere Kämpfe keine Abwehr benötigen.

<h2 id="manual-loop">Manueller Ablauf mit Platz zum Tanken</h2>

1. Annähern und Gegnerposition festlegen. Taunt nutzen, wenn Bedrohung und Debuff benötigt werden.
2. Shield Smite → Judgment. Im nächsten Fenster Warding Strike → Judgment.
3. Falls ausgerüstet Battlefield Banner einsetzen, dann Punishment sicher aufladen. Mit Vicious Strike und Pummel die gewählten Abklingverkürzungen nutzen.
4. Annihilate bei erfüllter Bedingung, Flash Rampage während Taumeln. Für Block, Bewegung oder Gruppenschutz den Schaden unterbrechen.

Halte Taunt, Schutz und Defiance außerhalb einer wiederholten Schadenskette. Eine lange Kette kann nicht entscheiden, welcher Gegnerangriff deine Abwehr benötigt.

<h2 id="gear-and-daevanion">Ausrüstung und Daevanion</h2>

Sichere genug Genauigkeit für die Treffer, die Abklingzeiten verkürzen. Suche Vicious Strike, Pummel, Shield Smite und Punishment, wenn sie die nächste nützliche Spezialisierung öffnen. Vergleiche den kürzesten Weg zur gleichen Fertigkeit auf mehreren Tafeln.

Nach einem funktionierenden Ablauf erhöhen Kampftempo und Abklingverbesserungen die Angriffsmöglichkeiten. Ergänze Verteidigung, HP oder Blocken, wenn Tanktode den Abschluss verhindern. Kritischer Schaden benötigt echte kritische Treffer; prüfe dies vor einer Priorisierung über Auslöser und Schutz. Der [Build-Guide](/builds) erklärt Ränge, Punkte und gespeicherte Konfigurationen.

<h2 id="templar-troubleshooting">Solo, Gruppe und PvP anpassen</h2>

**Judgment erscheint nicht:** Einen Schildauslöser manuell verwenden, in Reichweite bleiben und das kurze Fenster nutzen. Vor dem nächsten Auslöser die Abklingzeit prüfen.

**Punishment wird abgebrochen:** Schnellere oder mobile Ausführung wählen oder auf ein längeres sicheres Fenster warten.

**Der Boss wechselt das Ziel:** Bedrohungswerkzeuge nutzen, Treffer wieder aufnehmen und Position prüfen. Schaden ersetzt deine Tankaufgabe nicht.

**Solo dauert zu lange:** Poachs Kill-Reset bei passenden kleinen Gegnern verwenden. **Die Gruppe nimmt zu viel Schaden:** Einen Schadensplatz gegen Block, Schild oder Toleranz tauschen. Für [PvP](/pvp) Heranziehen, Kontrollresistenz, Defiance und Schutz neu abstimmen.

<h2 id="all-skills">Alle Templer-Fertigkeiten</h2>

<GuideSkillList classId="templar" />

<GuideNext slug="builds" />
''')

compact('assassin', 'en', 'AION 2 Assassin: Skills, Insignias and PvE Builds',
'Learn Assassin back attacks, Insignia stacks, Heart Gore triggers, Stigma choices and a manual opener for bosses, farming and PvP.',
'Build Assassin damage around safe back attacks, critical opportunities and an Insignia finisher.',
'Assassin uses dual daggers. Build up to five Insignias with Savage Roar and available attacks, then use Insignia Explosion. Shadowstrike helps reach the back; Heart Gore depends on a critical trigger.',
'''Choose Assassin if you enjoy close-range damage, changing position and spending a resource at the right moment. Position matters twice: Ambush and Triniel's Dagger gain back-attack damage, while Rear Smite improves your back-attack contribution. A rear position is useful only while it is safe to remain there.

You are not the party's main healer or shield tank. Ask the tank to keep the enemy facing stable, then return to its back after mechanics. Compare [Gladiator](/gladiator) for a frontline style or the [class roster](/classes) for ranged and support alternatives.''',
'''First secure Quick Slice's MP recovery and its rank-12 Insignia Explosion cooldown reduction. Savage Roar supplies Insignias; avoid a finisher before enough stacks exist on your current target. Stacks belong to the target and last briefly, so a target switch changes the opener.

Heart Gore becomes available after a critical hit. Its rank-16 critical-reset option supports repetition only when you actually crit. Illusive Clone removes the cooldown during its buff window; it does not establish permanent resets outside that window.

For passives, prioritize Rear Smite for back attacks and Exploit Weakness for critical interactions. Assault Stance improves critical damage. Ambush Stance adds a damage opportunity after movement skills. Improve the triggers you can use before paying for critical damage that rarely activates.''',
[('Illusive Clone', 'Temporary Heart Gore cooldown removal and extra damage; use with a safe attack window.'), ('Swift Contract', 'Combat-speed buff; coordinate it with your damage window.'), ("Triniel's Dagger", 'Back-attack damage and an enemy cooldown penalty; approach from behind.'), ('Throw Shadowblade', 'Ranged contact and Slow; its later on-kill reset is a farming option.'), ('Evasion Stance / Evasion Contract', 'Timed evasion / removing Slow and Root. Replace an offensive slot when survival or access fails.'), ('Shadow Walk / Smoke Bomb', 'Out-of-combat Stealth / Blind for control. Shadow Walk cannot be started in combat.')],
['Use your equipped buffs when a full attack window is available. Shadowstrike to the back, then Triniel’s Dagger if equipped.', 'Use Flash Slice or Ambush where their conditions and position are suitable. Return to the back if a movement skill crosses the target.', 'Use Quick Slice and Savage Roar; take Heart Gore opportunities. At five Insignias, use Insignia Explosion, then rebuild.', 'Use Storm Rampage during Stagger. Interrupt for movement or Defiance instead of committing into an incoming mechanic.'],
'''Accuracy comes before a finisher that misses. Critical chance supplies Heart Gore opportunities and makes Exploit Weakness useful; critical damage pays off after those hits occur. Combat speed helps build stacks, but stack generation without enough Insignia Explosion availability can waste opportunities.

On Daevanion, reach the Quick Slice, Heart Gore and Insignia Explosion ranks that unlock the required cooldown or reset options. Compare short routes before filling unrelated nodes. Save your selected options and equipped Stigmas with the allocation. The [builds guide](/builds) explains how to separate base skill ranks from bonus ranks.''',
'''**Heart Gore will not repeat:** check whether its critical trigger occurred, whether Illusive Clone is active and whether the later reset is selected. Continue normal attacks while waiting.

**Insignia Explosion feels weak:** inspect stacks on this target before using it. A new target does not inherit the old target's stack.

**Damage falls after moving:** check your new facing and whether Ambush or Rear Smite lost the back-attack condition. Do not chase the back through dangerous ground effects.

**MP runs out:** keep Quick Slice's recovery choice until sustain works. For solo farming, consider Throw Shadowblade's kill-reset option; for bosses, prioritize the back-attack window and finisher cycle. For [PvP](/pvp), build access, escape and control into the equipped slots rather than treating the boss opener as guaranteed.''')

compact('assassin', 'ja', 'AION 2 アサシン：スキル・Insignia・PvEビルド',
'背面攻撃、Insignia、Heart Goreの発動、スティグマ、ボス・狩り・PvPの手動起手を解説します。',
'安全な背面攻撃、クリティカルの機会、Insigniaのフィニッシャーで攻撃を組み立てます。',
'アサシンは二刀のダガーを使います。Savage RoarなどでInsigniaを最大5つためてInsignia Explosionで消費。Shadowstrikeで背後へ移動し、Heart Goreはクリティカル後に使います。',
'''近接で位置を変え、適切な時に資源を消費する攻撃が好きな人に向きます。AmbushとTriniel's Daggerは背面で強くなり、Rear Smiteも背面攻撃を強化します。ただし背後が危険なら移動を優先します。

主なヒーラーや盾タンクではありません。タンクに敵の向きを安定させてもらい、ギミック後に背後へ戻ります。正面で戦うなら[グラディエーター](/gladiator)、遠距離や支援は[クラス一覧](/classes)で比較できます。''',
'''まずQuick SliceのMP回復と、ランク12のInsignia Explosion再使用短縮を確保します。Savage Roarで対象にInsigniaをためます。スタックには時間制限があり、対象を変更すると起手も変わります。

Heart Goreはクリティカル後に使えます。ランク16のリセット特化も実際のクリティカルが必要です。Illusive Cloneは強化時間中に再使用をなくしますが、それ以外の常時リセットを保証しません。

Rear Smiteは背面、Exploit Weaknessはクリティカルの連携、Assault Stanceはクリティカルダメージを強化。Ambush Stanceは移動スキル後の攻撃機会を追加します。発動しにくい強化より、使える起点を優先します。''',
[('Illusive Clone', '一時的なHeart Goreの再使用削除と追加攻撃。安全な攻撃時間に使用。'), ('Swift Contract', '戦闘速度強化。攻撃時間に合わせる。'), ("Triniel's Dagger", '背面ダメージと敵の再使用時間への妨害。背後から使用。'), ('Throw Shadowblade', '遠距離からの接触と減速。後の撃破リセットは狩り向け。'), ('Evasion Stance / Evasion Contract', 'タイミングを合わせた回避／減速と束縛の解除。生存や接近が失敗するなら攻撃枠と交換。'), ('Shadow Walk / Smoke Bomb', '非戦闘時の隠密／暗闇による制御。Shadow Walkは戦闘中に開始できない。')],
['十分な攻撃時間に装備した強化を使い、Shadowstrikeで背後へ。装備していればTriniel’s Daggerを使います。', '条件と位置が合うFlash SliceやAmbushを使い、移動で反対側へ出たら背後へ戻ります。', 'Quick SliceとSavage Roarを使い、Heart Goreの機会に追撃。Insigniaが5つになったらExplosionを使ってため直します。', 'スタガー中はStorm Rampage。危険なギミックには移動やDefianceを優先します。'],
'''命中しないフィニッシャーを先に改善します。クリティカルはHeart GoreとExploit Weaknessの発動を増やし、その後でクリティカルダメージが活きます。攻撃速度だけでスタックを増やしても、Explosionの再使用が間に合わなければ機会を失います。

DaevanionではQuick Slice、Heart Gore、Insignia Explosionの必要な特化に届くランクを狙い、短い経路を比較します。特化とスティグマも構成と一緒に保存。[ビルドガイド](/builds)で基本ランクと追加ランクを区別できます。''',
'''**Heart Goreを連打できない：**クリティカル、Illusive Cloneの有効時間、後のリセット特化を確認し、待つ間は通常攻撃。

**Explosionが弱い：**今の対象のスタックを確認。別の敵にスタックは引き継がれません。

**移動後に攻撃が弱い：**背面条件と向きを確認。危険な地面を通って背後を追わないようにします。

**MPが不足：**Quick Sliceの回復を維持。ソロ狩りはThrow Shadowbladeの撃破リセット、ボスは背面とフィニッシャーを重視。[PvP](/pvp)では接近、離脱、制御を別に準備します。''')

compact('assassin', 'es', 'AION 2 Asesino: habilidades, Insignias y builds PvE',
'Aprende ataques por detrás, Insignias, activaciones de Heart Gore, estigmas y aperturas manuales para jefes, farmeo y PvP.',
'Construye daño con ataques seguros por detrás, oportunidades críticas y un remate de Insignias.',
'Asesino usa dos dagas. Acumula hasta cinco Insignias con Savage Roar y otros ataques y gástalas con Insignia Explosion. Shadowstrike te lleva detrás; Heart Gore depende de un crítico.',
'''Elige Asesino si disfrutas del daño cercano, recolocarte y gastar recursos en el momento adecuado. Ambush y Triniel's Dagger ganan daño por detrás; Rear Smite también recompensa esa posición. La espalda solo sirve mientras sea seguro permanecer allí.

No eres el sanador principal ni un tanque de escudo. Pide al tanque que estabilice la orientación y vuelve detrás tras las mecánicas. Compara [Gladiador](/gladiator) para luchar frontalmente o las [ocho clases](/classes) para funciones a distancia y de apoyo.''',
'''Asegura recuperación de MP en Quick Slice y su reducción de Insignia Explosion de rango 12. Savage Roar graba marcas en el objetivo. Duran poco y pertenecen a ese enemigo: cambiar de objetivo cambia la apertura.

Heart Gore se habilita tras un crítico. Su reinicio de rango 16 exige críticos reales. Illusive Clone elimina la recarga durante su mejora; no garantiza reinicios permanentes fuera de ella.

Rear Smite mejora ataques por detrás y Exploit Weakness aporta interacciones críticas. Assault Stance aumenta daño crítico; Ambush Stance añade daño tras habilidades de movimiento. Mejora activadores utilizables antes de pagar por daño crítico que rara vez ocurre.''',
[('Illusive Clone', 'Elimina temporalmente la recarga de Heart Gore y añade daño; úsalo en una ventana segura.'), ('Swift Contract', 'Velocidad de combate; coordínala con tu ventana de daño.'), ("Triniel's Dagger", 'Daño por detrás y penalización de recargas enemigas; acércate por la espalda.'), ('Throw Shadowblade', 'Contacto a distancia y ralentización; el reinicio posterior al matar sirve para farmeo.'), ('Evasion Stance / Evasion Contract', 'Evasión a tiempo / eliminar ralentización e inmovilización. Sustituye daño si falla la supervivencia o el acceso.'), ('Shadow Walk / Smoke Bomb', 'Sigilo fuera de combate / ceguera para control. Shadow Walk no se inicia en combate.')],
['Activa tus mejoras cuando haya una ventana completa. Shadowstrike hacia la espalda y Triniel’s Dagger si está equipado.', 'Usa Flash Slice o Ambush según condiciones y posición. Vuelve detrás si cruzas al otro lado.', 'Quick Slice y Savage Roar; aprovecha Heart Gore. Con cinco marcas usa Insignia Explosion y vuelve a acumular.', 'Storm Rampage durante tambaleo. Interrumpe para moverte o usar Defiance ante una mecánica.'],
'''Precisión antes de un remate que falla. Los críticos habilitan Heart Gore y Exploit Weakness; el daño crítico rinde cuando esas activaciones ocurren. Velocidad acumula marcas, pero generar más sin disponer de Explosion desperdicia oportunidades.

En Daevanion busca los rangos de Quick Slice, Heart Gore e Insignia Explosion que desbloqueen recargas o reinicios necesarios. Compara rutas cortas y guarda opciones y estigmas. La [guía de builds](/builds) distingue rangos base y adicionales.''',
'''**Heart Gore no se repite:** revisa crítico, duración de Illusive Clone y reinicio seleccionado. Sigue con ataques normales mientras esperas.

**Explosion hace poco daño:** mira las marcas de este objetivo. No hereda las del anterior.

**Pierdes daño al moverte:** revisa orientación y condición de espalda. No cruces áreas peligrosas por perseguirla.

**Falta MP:** mantén recuperación de Quick Slice. Para farmeo solo considera el reinicio de Throw Shadowblade; ante jefes prioriza espalda y remate. Para [PvP](/pvp), prepara acceso, escape y control por separado.''')

compact('assassin', 'de', 'AION 2 Assassine: Fertigkeiten, Insignien und PvE-Builds',
'Lerne Rückenangriffe, Insignien, Heart-Gore-Auslöser, Stigmas und manuelle Eröffnungen für Bosse, Farmen und PvP.',
'Baue Schaden mit sicheren Rückenangriffen, kritischen Möglichkeiten und dem Insignien-Abschluss auf.',
'Assassinen nutzen zwei Dolche. Baue mit Savage Roar und Angriffen bis zu fünf Insignien auf und verbrauche sie mit Insignia Explosion. Shadowstrike führt hinter das Ziel; Heart Gore benötigt einen kritischen Auslöser.',
'''Wähle Assassine für Nahkampfschaden, Positionswechsel und den gezielten Verbrauch einer Ressource. Ambush und Triniel's Dagger erhalten Rückenboni; Rear Smite verbessert ebenfalls Rückenangriffe. Diese Position ist nur sinnvoll, solange sie sicher bleibt.

Du bist weder Hauptheiler noch Schildtank. Bitte den Tank um stabile Blickrichtung und kehre nach Mechaniken zum Rücken zurück. Vergleiche [Gladiator](/gladiator) für Frontangriffe oder die [Klassenübersicht](/classes) für Fernkampf und Unterstützung.''',
'''Sichere Quick Slices MP-Regeneration und die Rang-12-Verkürzung von Insignia Explosion. Savage Roar baut Insignien am Gegner auf. Sie laufen rasch ab und gehören zum jeweiligen Ziel: Ein Zielwechsel verändert die Eröffnung.

Heart Gore öffnet nach einem kritischen Treffer. Der Rang-16-Reset benötigt tatsächliche kritische Treffer. Illusive Clone entfernt die Abklingzeit während des Buffs, nicht dauerhaft außerhalb des Fensters.

Rear Smite unterstützt Rückenangriffe, Exploit Weakness kritische Wechselwirkungen. Assault Stance erhöht kritischen Schaden; Ambush Stance ergänzt Schaden nach Bewegungsfertigkeiten. Verbessere nutzbare Auslöser vor selten wirksamem kritischem Schaden.''',
[('Illusive Clone', 'Entfernt vorübergehend Heart Gores Abklingzeit und ergänzt Schaden; im sicheren Fenster nutzen.'), ('Swift Contract', 'Kampftempo; mit deinem Schadensfenster abstimmen.'), ("Triniel's Dagger", 'Rückenschaden und gegnerische Abklingstrafe; von hinten angreifen.'), ('Throw Shadowblade', 'Fernkontakt und Verlangsamung; der spätere Kill-Reset hilft beim Farmen.'), ('Evasion Stance / Evasion Contract', 'Gezielte Ausweichphase / Verlangsamung und Festhalten entfernen. Schadensplatz bei Überlebens- oder Zugangsproblemen ersetzen.'), ('Shadow Walk / Smoke Bomb', 'Tarnung außerhalb des Kampfes / Blendung. Shadow Walk lässt sich im Kampf nicht beginnen.')],
['Buffs bei einem vollständigen Angriffsfenster aktivieren. Shadowstrike zum Rücken, dann Triniel’s Dagger, falls ausgerüstet.', 'Flash Slice oder Ambush bei passenden Bedingungen nutzen. Nach einem Seitenwechsel zum Rücken zurückkehren.', 'Quick Slice und Savage Roar nutzen, Heart Gore mitnehmen. Bei fünf Insignien Explosion einsetzen und neu aufbauen.', 'Storm Rampage während Taumeln. Für Bewegung oder Defiance bei gefährlichen Mechaniken unterbrechen.'],
'''Genauigkeit kommt vor einem verfehlenden Abschluss. Kritische Treffer ermöglichen Heart Gore und Exploit Weakness; kritischer Schaden lohnt sich danach. Tempo erzeugt Stapel, aber ohne verfügbares Explosion-Fenster gehen Chancen verloren.

Suche auf Daevanion die Quick-Slice-, Heart-Gore- und Explosion-Ränge für benötigte Verkürzungen oder Resets. Vergleiche kurze Wege und speichere Optionen und Stigmas. Der [Build-Guide](/builds) trennt Grundränge von zusätzlichen Rängen.''',
'''**Heart Gore lässt sich nicht wiederholen:** Kritischen Auslöser, Illusive-Clone-Fenster und gewählten Reset prüfen. Während der Wartezeit normale Angriffe nutzen.

**Explosion wirkt schwach:** Stapel am aktuellen Ziel prüfen. Ein neues Ziel übernimmt keine alten Insignien.

**Schaden sinkt nach Bewegung:** Blickrichtung und Rückenbedingung prüfen. Keine gefährlichen Bodenflächen für den Rücken durchqueren.

**MP fehlen:** Quick Slices Regeneration behalten. Solo hilft gegebenenfalls Throw Shadowblades Kill-Reset; am Boss zählen Rücken und Abschluss. Für [PvP](/pvp) Zugang, Rückzug und Kontrolle eigens vorbereiten.''')

compact('sorcerer', 'en', 'AION 2 Sorcerer: Skills, Mana and PvE Builds',
'Learn Sorcerer fire and frost skills, Hellfire cooldown links, MP-dependent passives, Stigma choices and safe casting for PvE and PvP.',
'Connect fire damage, frost control and mana recovery so charged attacks fit the encounter.',
'Sorcerer uses a spellbook for ranged magic damage. Firestorm can shorten Hellfire, Ice Chain can shorten Winter’s Shackles, and MP recovery keeps both casting and mana-dependent passives working.',
'''Choose Sorcerer if you enjoy planning cast windows, maintaining resources and controlling enemies at range. Fire attacks supply the main damage chain; frost and slowing effects create other attacks and passive interactions. Charged attacks need time, so a mechanic that forces movement changes your next skill.

Compare [Ranger](/ranger) for bow attacks or [Spiritmaster](/spiritmaster) for summon management. The [class comparison](/classes) covers their different responsibilities. A spellbook character still needs to dodge and control distance; range does not protect you from every mechanic.''',
'''Prioritize Flame Arrow's MP-restoring choice while sustain is limited. Firestorm's rank-8 cost reduction reduces repeated spending; its rank-12 Hellfire cooldown option connects the two attacks. Ice Chain's rank-12 option reduces Winter's Shackles, whose damage-boost option improves your next window.

For Hellfire, faster casting helps complete charges safely. Its rank-8 mobile option is useful when the encounter makes you move. A mobile-casting choice competes with other options; build around the one selected rather than assuming all effects apply.

Robe of Flame supplies accuracy and damage amplification. Grace of Enhancement needs at least 25% MP for its damage benefit; Robe of Earth's critical benefit needs at least 50% MP. Running almost empty therefore affects more than the next cast. Fire Mark enables Blaze, and Cold Snap adds damage against slowed targets.''',
[('Element Enhancement', 'Fire/water damage buff. Its rank-10 and rank-15 upgrades strengthen Robe of Flame and Grace of Enhancement respectively.'), ('Cold Storm / Fire Wall', 'Area damage and damage over time. Place the effect where the enemy will actually be hit.'), ('Delayed Explosion', 'Delayed damage plus increased damage taken from you during the delay. Use before the burst lands.'), ('Steel Barrier / Arctic Armor', 'Shield or tolerance for survival. Arctic Armor’s mana-sharing effect requires sufficient MP.'), ('Curse: Tree / Soul Freeze', 'Polymorph or Seal against susceptible enemies. Attacking cancels Tree’s polymorph.'), ('Hibernation', 'Brief damage/status immunity with a manual exit; some powerful attacks bypass it.')],
['Apply fire attacks for Fire Mark, then use available Blaze. Slow with Ice Chain when its effects or Cold Snap contribute.', 'Use Element Enhancement and Wish of Concentration before a safe damage window. Add Delayed Explosion and placed damage if equipped.', 'Charge Hellfire when the mechanic allows it. Use Firestorm and its selected cooldown option, then cast the next Hellfire when ready.', 'Use Winter’s Shackles when available and Frost Burst when its prerequisite appears. During Stagger, use Flame Scattershot; return to MP-restoring attacks between windows.'],
'''A landed Firestorm can improve Hellfire availability; a missed one cannot. Address accuracy first when misses break the loop. Invest in attack, combat speed or cooldown improvement to increase completed casts, and keep enough MP recovery to preserve the passive thresholds.

Choose Daevanion skill levels that open Firestorm's cooldown link, Flame Arrow's fire benefit or the casting option you need. Critical-damage investment becomes useful when you have a reliable critical rate; avoid replacing a functioning mana loop solely for it. The [builds guide](/builds) helps compare skill bonuses and point costs.''',
'''**Hellfire stays on cooldown:** select Firestorm's rank-12 cooldown effect and verify its hits. A skill level without the option does not produce the reduction.

**Damage drops before MP reaches zero:** check the 25% and 50% passive thresholds, then reduce repeated costs or restore MP.

**Blaze does not open:** apply Fire Mark first. **Frost Burst does not open:** it needs Frost or its immune-target proc; Slow alone is not the same condition.

**Charges keep getting canceled:** shorten the cast, select a mobile option or move first. For short solo pulls, use damage that lands before the enemy dies. For [PvP](/pvp), keep control and escape separate; do not break Tree immediately if you need its control window.''')

compact('sorcerer', 'ja', 'AION 2 ソーサラー：スキル・MP・PvEビルド',
'火と氷のスキル、Hellfireの再使用短縮、MP条件のパッシブ、スティグマ、安全な詠唱を解説します。',
'火の攻撃、氷の制御、MP回復をつなぎ、戦闘に合うチャージ時間を作ります。',
'ソーサラーはスペルブックで遠距離魔法攻撃を行います。FirestormでHellfire、Ice ChainでWinter’s Shacklesの再使用を短縮でき、MP回復で詠唱とMP条件のパッシブを維持します。',
'''詠唱できる時間を計画し、MPを管理し、遠距離で敵を制御したい人に向きます。火の攻撃が主な攻撃ループとなり、凍結と減速は別の攻撃やパッシブにつながります。移動を強いるギミックでは次のスキルを変えます。

弓なら[レンジャー](/ranger)、召喚管理なら[スピリットマスター](/spiritmaster)、役割の比較は[クラス一覧](/classes)へ。遠距離でも回避と距離管理は必要です。''',
'''継戦が難しい間はFlame ArrowのMP回復を優先。Firestormのランク8消費軽減とランク12のHellfire再使用短縮で反復攻撃を支えます。Ice Chainのランク12特化でWinter's Shacklesを早め、そのダメージ強化につなげます。

Hellfireの詠唱高速化は安全なチャージ完了を助けます。ランク8の移動可能化は移動が多い戦闘向け。各特化を同時にすべて使えるわけではないため、選んだ構成に合わせます。

Robe of Flameは命中とダメージ増幅。Grace of Enhancementのダメージ強化にはMP25%以上、Robe of Earthのクリティカル強化には50%以上が必要です。MP不足は次の詠唱だけでなく強化にも影響します。Fire MarkはBlazeの条件、Cold Snapは減速対象への追加攻撃です。''',
[('Element Enhancement', '火・水属性強化。ランク10と15でRobe of Flame、Grace of Enhancementをそれぞれ強化。'), ('Cold Storm / Fire Wall', '範囲攻撃と持続ダメージ。敵が実際に当たる位置に設置。'), ('Delayed Explosion', '遅延ダメージと、その間の自分からの被ダメージ増加。バースト前に使用。'), ('Steel Barrier / Arctic Armor', '生存用の盾／耐性。Arctic ArmorのMP分担には十分なMPが必要。'), ('Curse: Tree / Soul Freeze', '有効な敵への変身／封印。攻撃するとTreeの変身が解除される。'), ('Hibernation', '短いダメージ・状態異常免疫と手動解除。一部の強力な攻撃は防げない。')],
['火攻撃でFire Markを付け、使用可能なBlaze。Ice Chainの効果やCold Snapが役立つ時は減速を使います。', '安全な攻撃時間の前にElement EnhancementとWish of Concentration。装備した遅延攻撃や設置攻撃を追加します。', 'ギミックに余裕があればHellfireをチャージ。Firestormの選んだ特化で再使用を短縮し、次を使います。', 'Winter’s Shacklesと条件が成立したFrost Burstを使用。スタガーにはFlame Scattershot。合間はMP回復攻撃に戻ります。'],
'''Firestormが外れるとHellfireの再使用短縮も活かせません。ループを妨げるミスには命中を改善。完了できる詠唱を増やす攻撃力、戦闘速度、再使用短縮と、パッシブのMP条件を維持する回復を組み合わせます。

DaevanionではFirestormの連携、Flame Arrowの火属性強化、必要な詠唱特化に届くランクを選びます。安定したクリティカル率ができてからクリティカルダメージを評価。[ビルドガイド](/builds)で追加ランクとポイントを比較できます。''',
'''**Hellfireが短縮されない：**Firestormのランク12特化を選び、命中を確認。ランクだけでは効果は有効になりません。

**MPが0になる前に弱くなる：**25%と50%の条件を確認し、消費軽減や回復を追加します。

**Blazeが出ない：**Fire Markが必要。**Frost Burstが出ない：**Frostか免疫対象への発動が条件で、減速だけとは異なります。

**チャージが中断される：**高速化、移動可能化、先に移動を選択。短いソロ戦では倒す前に着弾する攻撃を使います。[PvP](/pvp)では制御と離脱を分け、Treeで制御したい時はすぐ攻撃で解除しないようにします。''')

compact('sorcerer', 'es', 'AION 2 Hechicero: habilidades, maná y builds PvE',
'Aprende fuego, escarcha, recargas de Hellfire, pasivas que dependen de MP, estigmas y lanzamientos seguros en PvE y PvP.',
'Conecta daño de fuego, control de escarcha y recuperación de MP para completar cargas durante el encuentro.',
'Hechicero usa un libro de hechizos para daño mágico a distancia. Firestorm puede acortar Hellfire, Ice Chain puede acortar Winter’s Shackles y el MP mantiene lanzamientos y pasivas dependientes de maná.',
'''Elige Hechicero si disfrutas planear lanzamientos, gestionar recursos y controlar a distancia. El fuego aporta el ciclo principal; escarcha y ralentización habilitan otros ataques e interacciones. Una mecánica que obliga a moverte cambia la próxima habilidad.

Compara [Arquero](/ranger) para arco o [Espiritualista](/spiritmaster) para invocaciones. La [comparación de clases](/classes) explica sus funciones. La distancia exige igualmente esquivar y colocarte.''',
'''Prioriza recuperación de Flame Arrow mientras falte MP. La reducción de coste de Firestorm en rango 8 sostiene la repetición; su opción de rango 12 reduce Hellfire. Ice Chain en rango 12 reduce Winter's Shackles, cuya opción de daño mejora la siguiente ventana.

Hellfire más rápido permite completar cargas. Su opción móvil de rango 8 ayuda en encuentros con movimiento. Compite con otras opciones: no supongas que todas se aplican simultáneamente.

Robe of Flame aporta precisión y amplificación. Grace of Enhancement requiere al menos 25% MP para el daño; el crítico de Robe of Earth requiere 50%. Jugar casi vacío afecta también a las pasivas. Fire Mark habilita Blaze; Cold Snap aporta daño contra ralentizados.''',
[('Element Enhancement', 'Mejora fuego/agua. En rangos 10 y 15 potencia Robe of Flame y Grace of Enhancement respectivamente.'), ('Cold Storm / Fire Wall', 'Área y daño periódico. Colócalos donde el enemigo realmente reciba el efecto.'), ('Delayed Explosion', 'Daño retardado y mayor daño recibido de ti durante la espera; úsalo antes de la ráfaga.'), ('Steel Barrier / Arctic Armor', 'Escudo o tolerancia. Compartir daño con maná mediante Arctic Armor requiere MP suficiente.'), ('Curse: Tree / Soul Freeze', 'Transformación o sello contra objetivos susceptibles. Atacar cancela Tree.'), ('Hibernation', 'Inmunidad breve a daño y estados con salida manual; no bloquea ciertos ataques poderosos.')],
['Aplica fuego para Fire Mark y usa Blaze disponible. Ice Chain cuando la ralentización o Cold Snap aporten valor.', 'Element Enhancement y Wish of Concentration antes de una ventana segura. Añade explosión retardada y áreas si están equipadas.', 'Carga Hellfire si la mecánica lo permite. Usa Firestorm con su reducción seleccionada y repite Hellfire cuando esté listo.', 'Winter’s Shackles al estar disponible; Frost Burst con su condición. Flame Scattershot durante tambaleo; vuelve a recuperar MP entre ventanas.'],
'''Firestorm debe acertar para mejorar la disponibilidad de Hellfire. Corrige precisión si los fallos rompen el ciclo. Ataque, velocidad o recargas deben producir lanzamientos completados; conserva recuperación suficiente para los umbrales de MP.

En Daevanion alcanza rangos para la conexión de Firestorm, el beneficio de fuego de Flame Arrow o la opción de lanzamiento necesaria. El daño crítico necesita críticos fiables. La [guía de builds](/builds) permite comparar rangos extra y costes.''',
'''**Hellfire no reduce recarga:** selecciona la opción de rango 12 de Firestorm y confirma impactos.

**Pierdes daño antes de vaciar MP:** revisa los umbrales de 25% y 50% y reduce costes o recupera maná.

**Blaze no se habilita:** aplica Fire Mark. **Frost Burst no aparece:** requiere Frost o su activación contra inmunes; ralentizar no equivale a Frost.

**Se cancelan cargas:** acorta o vuelve móvil el lanzamiento, o muévete primero. En grupos breves usa ataques que impacten antes de morir el objetivo. Para [PvP](/pvp), separa control y escape; no rompas Tree inmediatamente si necesitas su ventana.''')

compact('sorcerer', 'de', 'AION 2 Magier: Fertigkeiten, Mana und PvE-Builds',
'Lerne Feuer, Frost, Hellfire-Verkürzungen, MP-abhängige passive Effekte, Stigmas und sicheres Wirken für PvE und PvP.',
'Verbinde Feuerschaden, Frostkontrolle und MP-Regeneration mit sicheren aufgeladenen Angriffen.',
'Magier nutzen ein Zauberbuch für magischen Fernschaden. Firestorm kann Hellfire verkürzen, Ice Chain verkürzt Winter’s Shackles; MP-Regeneration hält Zauber und manaabhängige passive Effekte aktiv.',
'''Wähle Magier, wenn du Zauberfenster planst, Ressourcen verwaltest und Gegner auf Distanz kontrollierst. Feuer liefert die Hauptangriffe, Frost und Verlangsamung eröffnen weitere Wechselwirkungen. Erzwungene Bewegung verändert die nächste Fertigkeit.

Vergleiche [Waldläufer](/ranger) für Bögen oder [Beschwörer](/spiritmaster) für Geister. Die [Klassenübersicht](/classes) beschreibt die Rollen. Auch Fernkampf benötigt Ausweichen und Abstandskontrolle.''',
'''Priorisiere Flame Arrows MP-Regeneration bei Ressourcenproblemen. Firestorms Rang-8-Kostenoption ermöglicht Wiederholung; die Rang-12-Option verkürzt Hellfire. Ice Chain verkürzt auf Rang 12 Winter's Shackles, dessen Schadensoption das nächste Fenster verbessert.

Schnelleres Hellfire hilft bei vollständigen Aufladungen. Die mobile Rang-8-Option hilft bei Bewegungsmechaniken. Sie konkurriert mit anderen Optionen; alle Effekte gelten nicht gleichzeitig.

Robe of Flame liefert Genauigkeit und Verstärkung. Grace of Enhancement benötigt mindestens 25% MP für den Schaden; Robe of Earth benötigt 50% MP für seinen kritischen Vorteil. Fast leere MP kosten somit auch passive Vorteile. Fire Mark ermöglicht Blaze; Cold Snap liefert Schaden gegen verlangsamte Ziele.''',
[('Element Enhancement', 'Feuer-/Wasserbuff. Rang 10 und 15 verstärken Robe of Flame beziehungsweise Grace of Enhancement.'), ('Cold Storm / Fire Wall', 'Flächenschaden und Schaden über Zeit. Dort platzieren, wo der Gegner getroffen wird.'), ('Delayed Explosion', 'Verzögerter Schaden und mehr Schaden durch dich während der Verzögerung; vor dem Schadensschub einsetzen.'), ('Steel Barrier / Arctic Armor', 'Schild oder Toleranz. Arctic Armors Manaaufteilung benötigt ausreichend MP.'), ('Curse: Tree / Soul Freeze', 'Verwandlung oder Versiegelung anfälliger Gegner. Angriffe beenden Tree.'), ('Hibernation', 'Kurze Schadens-/Statusimmunität mit manuellem Ende; bestimmte mächtige Angriffe umgehen sie.')],
['Feuer für Fire Mark, dann verfügbares Blaze nutzen. Ice Chain einsetzen, wenn Verlangsamung oder Cold Snap helfen.', 'Element Enhancement und Wish of Concentration vor einem sicheren Fenster nutzen. Verzögerten Schaden und Flächen ergänzen, falls ausgerüstet.', 'Hellfire bei passender Mechanik aufladen. Firestorm mit gewählter Verkürzung nutzen, danach verfügbares Hellfire wiederholen.', 'Winter’s Shackles bei Verfügbarkeit und Frost Burst bei erfüllter Bedingung. Flame Scattershot während Taumeln; dazwischen MP regenerieren.'],
'''Firestorm muss treffen, um Hellfire verfügbar zu machen. Behebe Genauigkeitsprobleme, wenn Fehlschläge den Ablauf brechen. Angriff, Kampftempo und Abklingverbesserungen sollen abgeschlossene Zauber erhöhen; erhalte die MP-Schwellen durch Regeneration.

Erreiche auf Daevanion die Firestorm-Verbindung, Flame Arrows Feuerbonus oder die benötigte Zauberoption. Kritischer Schaden benötigt zuverlässige kritische Treffer. Der [Build-Guide](/builds) hilft beim Vergleich zusätzlicher Ränge und Kosten.''',
'''**Hellfire bleibt auf Abklingzeit:** Firestorms Rang-12-Option auswählen und Treffer prüfen.

**Schaden sinkt vor leeren MP:** Die Schwellen von 25% und 50% prüfen, Kosten senken oder Mana regenerieren.

**Blaze öffnet nicht:** Fire Mark anbringen. **Frost Burst fehlt:** Frost oder eine Auslösung gegen immune Ziele benötigt; Verlangsamung ist nicht Frost.

**Aufladungen brechen ab:** Schneller oder mobil wirken oder erst bewegen. Bei kurzen Solozügen Angriffe wählen, die rechtzeitig treffen. Für [PvP](/pvp) Kontrolle und Rückzug trennen; Tree nicht sofort brechen, wenn sein Kontrollfenster benötigt wird.''')

compact('cleric', 'en', 'AION 2 Cleric: Skills, Healing and Party Play',
'Understand Cleric healing targets, cleansing, resurrection, damage skills, party buffs and build adjustments for solo, dungeons and PvP.',
'Learn when to heal, cleanse, resurrect or attack, then select the Stigmas and passives that support that job.',
'Cleric uses a mace for magic damage and party recovery. Healing Light heals you and the lowest-HP party member in range; Radiant Recovery heals and removes a debuff. Equip Summon Resurrection separately when your group needs revival.',
'''Choose Cleric if you want to watch party health while contributing debuffs and damage. Healing, cleansing and resurrection solve different problems: healing repairs lost HP, cleansing removes a removable harmful effect, and resurrection restores a fallen party member.

Compare [Chanter](/chanter) for melee support and mantras. A Cleric has direct recovery tools, but an ally outside their range or dying to a bypassing mechanic still needs repositioning or a mechanic response. The [class roster](/classes) compares the other jobs.''',
'''Earth's Retribution restores MP, and its rank-12 Discharge option reduces Bolt's cooldown. Chain of Torment is the condition for Condemnation; select Condemnation's rank-12 critical-reset option only for a loop that can actually produce critical hits.

Radiant Recovery already removes one debuff. At rank 8 you can choose removal of up to two, an additional use or a shorter cooldown. These are different choices. Healing Light heals you and the lowest-HP party member in range rather than a freely selected ally. Light of Regeneration covers continuing party damage over time.

Healing Enhancement converts Attack into Heal Boost, so attack investment also affects recovery. Radiant Benediction heals nearby party members when your attacks land, with a cooldown. Keep attacking when the group is stable, but do not wait for a passive heal during an urgent recovery need.''',
[('Summon Resurrection', 'Revives a fallen party member; its later faster-cast option helps reduce exposure.'), ('Light of Protection', 'Party offense and tolerance. Its damage boost does not stack with Chanter’s Undefeated Mantra.'), ('Earth Punishment / Noble Aura', 'Damage over time / a following damage summon. Use damage slots while recovery is sufficient.'), ('Absolution', 'Party heal and removal of multiple debuffs; useful when one removal is not enough.'), ('Benevolence / Yustiel’s Power', 'Continuing party healing / party damage tolerance. Choose for sustained loss or incoming damage.'), ('Salvation', 'Brief personal immunity; it does not block certain powerful attacks or replace party healing.')],
['Start Light of Regeneration before sustained party damage. Keep Radiant Recovery available for removable debuffs.', 'Apply Debilitating Mark and Chain of Torment; add Earth Punishment if equipped. Use available Condemnation while the party is stable.', 'Use Bolt in a safe charge window and Earth’s Retribution between larger attacks. Stop damage immediately for urgent healing or cleanse.', 'If an ally dies, move to a safe casting position and use equipped Summon Resurrection. Do not become a second casualty while reviving.'],
'''First fix missed attacks and interrupted healing. Attack supports damage and Healing Enhancement; cooldown improvements provide more recovery opportunities. Add survival when your own deaths stop all healing, and critical investment only after a reset-based loop reliably crits.

On Daevanion, choose the heal or damage specialization that addresses the actual failure: Radiant Recovery for cleanse/cooldown choices, Healing Light for recovery and Earth's Retribution or Condemnation for the selected damage loop. The [Cleric build guide](/cleric-build) gives a dedicated setup workflow and replacement choices.''',
'''**My selected ally did not get Healing Light:** its default party target is the lowest-HP member in range. Position for coverage and use the recovery tool that fits the situation.

**The debuff remains:** some effects are not removable, one cast removes only its allowed number, and an ally can be outside range. Use extra cleansing only when it solves that problem.

**Condemnation stays unavailable:** apply Chain of Torment to the current target. A reset still needs the selected option and a critical hit.

**A Chanter joins:** compare Undefeated Mantra and Light of Protection before duplicating the damage boost. For solo play, keep damage and self-recovery; for [PvP](/pvp), preserve healing access while moving and prepare personal control breaks.''', next_slug='cleric-build')

compact('cleric', 'ja', 'AION 2 クレリック：スキル・回復・パーティ戦',
'回復対象、減益解除、蘇生、攻撃スキル、パーティ強化とソロ・ダンジョン・PvPの調整を解説します。',
'回復・解除・蘇生・攻撃の判断を学び、その役割を支えるスティグマとパッシブを選びます。',
'クレリックはメイスで魔法攻撃とパーティ回復を行います。Healing Lightは自分と範囲内でHPが最も低い味方、Radiant Recoveryは回復と減益解除。蘇生にはSummon Resurrectionを別途装備します。',
'''味方のHPを見ながら減益と攻撃も行いたい人に向きます。回復は失ったHP、解除は除去可能な有害効果、蘇生は倒れた味方に対応します。必要な操作はそれぞれ異なります。

近接支援とマントラなら[チャンター](/chanter)と比較。回復の射程外や防御を貫通するギミックで倒れる味方には、位置変更やギミック対処も必要です。[クラス一覧](/classes)で他の役割を比較できます。''',
'''Earth's RetributionはMPを回復し、ランク12のDischarge特化でBoltを早めます。CondemnationにはChain of Tormentが必要。ランク12のクリティカルリセットは、実際にクリティカルが出る構成で使います。

Radiant Recoveryは基本効果で減益を1つ解除します。ランク8では最大2つの解除、追加使用、再使用短縮から選べます。Healing Lightは任意の味方ではなく、自分と範囲内でHPが最も低い味方を回復。Light of Regenerationは継続的な被害に対応します。

Healing Enhancementは攻撃力を回復強化へ反映します。Radiant Benedictionは攻撃命中時に近くの味方を回復しますが再使用時間があります。安定時は攻撃を続け、緊急時はパッシブ回復を待たずに対応します。''',
[('Summon Resurrection', '倒れた味方を蘇生。後の詠唱高速化で危険にさらされる時間を短縮。'), ('Light of Protection', 'パーティの攻撃と耐性。ダメージ強化はチャンターのUndefeated Mantraと重複しない。'), ('Earth Punishment / Noble Aura', '持続攻撃／追従する攻撃召喚。回復が足りている時の攻撃枠。'), ('Absolution', 'パーティ回復と複数の減益解除。1つの解除では不足する時に使用。'), ('Benevolence / Yustiel’s Power', '継続回復／パーティの耐性。継続的なHP減少か被ダメージに合わせる。'), ('Salvation', '自分の短い免疫。一部の強力な攻撃は防げず、パーティ回復の代わりではない。')],
['継続的な被害前にLight of Regeneration。解除可能な減益にRadiant Recoveryを用意します。', 'Debilitating MarkとChain of Torment、装備していればEarth Punishment。安定時にCondemnationを使います。', '安全な時間にBoltをチャージし、合間にEarth’s Retribution。緊急回復や解除には攻撃を中断します。', '味方が倒れたら安全な詠唱位置からSummon Resurrection。蘇生中に自分も倒れないようにします。'],
'''命中しない攻撃と中断される回復を先に改善。攻撃力は攻撃とHealing Enhancementに、再使用短縮は回復の機会に寄与します。自分の死亡で回復が止まるなら生存力を追加し、クリティカル構成はリセットが安定してから評価します。

Daevanionは実際の問題に合う特化へ。Radiant Recoveryは解除・再使用、Healing Lightは回復、Earth's RetributionとCondemnationは選んだ攻撃連携です。[クレリックビルド](/cleric-build)で枠の交換と構成手順を確認できます。''',
'''**選んだ味方にHealing Lightが届かない：**基本の対象は範囲内でHPが最も低い味方です。位置と回復手段を合わせます。

**減益が残る：**解除不可、解除数の上限、射程外を区別。追加解除はその問題を解決する時に選びます。

**Condemnationが使えない：**今の対象にChain of Tormentを付けます。リセットには特化とクリティカルも必要です。

**チャンターが加入：**Undefeated MantraとLight of Protectionの重複を比較。ソロでは攻撃と自己回復、[PvP](/pvp)では移動中の回復と自分の行動阻害解除を確保します。''', next_slug='cleric-build')

compact('cleric', 'es', 'AION 2 Clérigo: habilidades, curación y grupo',
'Entiende objetivos de curación, limpieza, resurrección, daño y mejoras del Clérigo para juego solo, mazmorras y PvP.',
'Aprende cuándo curar, limpiar, resucitar o atacar y elige estigmas y pasivas para esa tarea.',
'Clérigo usa maza para daño mágico y recuperación. Healing Light te cura y cura al miembro con menos HP en alcance; Radiant Recovery cura y elimina un perjuicio. Equipa Summon Resurrection por separado para revivir.',
'''Elige Clérigo si quieres vigilar la salud del grupo mientras aportas perjuicios y daño. Curar repara HP, limpiar elimina un efecto removible y resucitar recupera a un compañero caído. Son respuestas distintas.

Compara [Cantor](/chanter) para apoyo cuerpo a cuerpo y mantras. Un aliado fuera de alcance o que muere por una mecánica que ignora protección necesita también posición o respuesta a la mecánica. Las [ocho clases](/classes) muestran otras funciones.''',
'''Earth's Retribution recupera MP; su opción Discharge de rango 12 reduce Bolt. Chain of Torment habilita Condemnation. Elige el reinicio crítico de rango 12 de Condemnation para un ciclo con críticos reales.

Radiant Recovery elimina un perjuicio de base. En rango 8 puedes elegir hasta dos eliminaciones, un uso adicional o menor recarga: son opciones diferentes. Healing Light no apunta libremente a un aliado; cura al miembro con menos HP en alcance y a ti. Light of Regeneration cubre daño sostenido.

Healing Enhancement convierte ataque en potencia de curación. Radiant Benediction cura al grupo cercano cuando aciertas, con recarga. Ataca si el grupo está estable, pero no esperes una pasiva ante una urgencia.''',
[('Summon Resurrection', 'Revive a un miembro caído; una opción posterior de lanzamiento rápido reduce exposición.'), ('Light of Protection', 'Ofensiva y tolerancia del grupo. Su daño no se acumula con Undefeated Mantra de Cantor.'), ('Earth Punishment / Noble Aura', 'Daño periódico / invocación ofensiva que te sigue. Usa daño mientras la recuperación baste.'), ('Absolution', 'Curación de grupo y eliminación de varios perjuicios; útil si uno no basta.'), ('Benevolence / Yustiel’s Power', 'Curación continua / tolerancia del grupo. Elige según pérdida sostenida o daño entrante.'), ('Salvation', 'Inmunidad personal breve; no bloquea ciertos ataques poderosos ni sustituye curar al grupo.')],
['Light of Regeneration antes del daño sostenido; conserva Radiant Recovery para perjuicios eliminables.', 'Debilitating Mark y Chain of Torment; Earth Punishment si está equipado. Condemnation mientras el grupo esté estable.', 'Bolt durante una carga segura y Earth’s Retribution entre ataques. Interrumpe el daño ante curación o limpieza urgente.', 'Si alguien muere, busca posición segura y usa Summon Resurrection equipado. Evita convertirte en otra baja.'],
'''Corrige ataques fallidos y curas interrumpidas. Ataque mejora daño y Healing Enhancement; menor recarga añade oportunidades de recuperar. Aumenta supervivencia si tus muertes detienen toda la curación; invierte en críticos cuando los reinicios sean fiables.

En Daevanion elige lo que resuelva el fallo: Radiant Recovery para limpieza/recarga, Healing Light para recuperar y Earth's Retribution o Condemnation para el daño elegido. La [guía de build del Clérigo](/cleric-build) explica configuraciones y sustituciones.''',
'''**Healing Light no curó al aliado elegido:** su objetivo de grupo por defecto es quien tiene menos HP en alcance. Ajusta posición y herramienta.

**Queda el perjuicio:** puede no ser eliminable, exceder el número permitido o estar fuera de alcance. Añade limpieza si resuelve ese fallo.

**Condemnation no se habilita:** aplica Chain of Torment al objetivo actual. El reinicio requiere opción y crítico.

**Se une un Cantor:** compara Undefeated Mantra y Light of Protection antes de duplicar daño. Solo combina daño y autorrecuperación; en [PvP](/pvp), conserva acceso a curas al moverte y rompe tu propio control.''', next_slug='cleric-build')

compact('cleric', 'de', 'AION 2 Kleriker: Fertigkeiten, Heilung und Gruppe',
'Verstehe Heilziele, Reinigung, Wiederbelebung, Schaden und Gruppenbuffs für Solo-Spiel, Dungeons und PvP.',
'Entscheide zwischen Heilen, Reinigen, Wiederbeleben und Angreifen und wähle passende Stigmas und passive Effekte.',
'Kleriker nutzen einen Streitkolben für Magieschaden und Heilung. Healing Light heilt dich und das Gruppenmitglied mit den niedrigsten HP in Reichweite; Radiant Recovery heilt und entfernt einen negativen Effekt. Summon Resurrection muss für Wiederbelebung ausgerüstet sein.',
'''Wähle Kleriker, wenn du Gruppen-HP beobachten und gleichzeitig Debuffs und Schaden liefern möchtest. Heilung repariert HP, Reinigung entfernt einen entfernbaren Effekt und Wiederbelebung stellt ein gefallenes Mitglied wieder her. Diese Aufgaben benötigen unterschiedliche Antworten.

Vergleiche [Kantor](/chanter) für Nahkampfunterstützung und Mantras. Verbündete außerhalb der Reichweite oder mit tödlichen Mechanikfehlern benötigen auch Positionierung oder Mechanikreaktion. Die [Klassenübersicht](/classes) zeigt andere Aufgaben.''',
'''Earth's Retribution stellt MP her; die Discharge-Option auf Rang 12 verkürzt Bolt. Chain of Torment öffnet Condemnation. Der kritische Rang-12-Reset von Condemnation benötigt tatsächliche kritische Treffer.

Radiant Recovery entfernt standardmäßig einen negativen Effekt. Auf Rang 8 wählst du bis zu zwei Entfernungen, eine weitere Nutzung oder eine kürzere Abklingzeit. Healing Light heilt dich und das Gruppenmitglied mit den niedrigsten HP in Reichweite, keinen frei gewählten Verbündeten. Light of Regeneration deckt anhaltenden Schaden ab.

Healing Enhancement verwandelt Angriff in Heilverstärkung. Radiant Benediction heilt nahe Gruppenmitglieder bei Treffern mit eigener Abklingzeit. Greife bei stabiler Gruppe an, aber warte bei dringendem Heilbedarf nicht auf einen passiven Effekt.''',
[('Summon Resurrection', 'Belebt ein gefallenes Mitglied wieder; die spätere schnellere Ausführung reduziert Gefahrenzeit.'), ('Light of Protection', 'Gruppenoffensive und Toleranz. Der Schadensbuff stapelt nicht mit Undefeated Mantra des Kantors.'), ('Earth Punishment / Noble Aura', 'Schaden über Zeit / folgende Angriffsbeschwörung. Schadensplätze bei ausreichender Heilung nutzen.'), ('Absolution', 'Gruppenheilung und Entfernung mehrerer Effekte; wenn eine Entfernung nicht reicht.'), ('Benevolence / Yustiel’s Power', 'Anhaltende Heilung / Gruppentoleranz. Nach dauerhaftem HP-Verlust oder eingehendem Schaden wählen.'), ('Salvation', 'Kurze eigene Immunität; bestimmte mächtige Angriffe umgehen sie. Ersetzt keine Gruppenheilung.')],
['Light of Regeneration vor anhaltendem Schaden beginnen; Radiant Recovery für entfernbare Effekte bereithalten.', 'Debilitating Mark und Chain of Torment anbringen; Earth Punishment, falls ausgerüstet. Condemnation bei stabiler Gruppe nutzen.', 'Bolt sicher aufladen, dazwischen Earth’s Retribution. Schaden für dringende Heilung oder Reinigung abbrechen.', 'Bei einem Tod sichere Position suchen und ausgerüstetes Summon Resurrection nutzen. Nicht selbst zur nächsten Verlustperson werden.'],
'''Behebe verfehlte Angriffe und unterbrochene Heilungen. Angriff verbessert Schaden und Healing Enhancement; Abklingverkürzungen liefern mehr Heilfenster. Ergänze Überleben, wenn deine Tode alle Heilung stoppen; kritische Investitionen folgen zuverlässigen Resets.

Daevanion soll das konkrete Problem lösen: Radiant Recovery für Reinigung/Abklingzeit, Healing Light für Heilung und Earth's Retribution oder Condemnation für den gewählten Schaden. Der [Kleriker-Build-Guide](/cleric-build) erklärt Konfiguration und Ersatzplätze.''',
'''**Healing Light heilt nicht das gewählte Mitglied:** Das Standardziel ist das Gruppenmitglied mit den niedrigsten HP in Reichweite. Position und Heilwerkzeug abstimmen.

**Der Effekt bleibt:** Nicht entfernbare Effekte, zu viele Effekte oder fehlende Reichweite unterscheiden. Zusätzliche Reinigung nur bei passendem Problem wählen.

**Condemnation öffnet nicht:** Chain of Torment am aktuellen Ziel anwenden. Ein Reset benötigt die Option und einen kritischen Treffer.

**Ein Kantor kommt hinzu:** Undefeated Mantra und Light of Protection vergleichen, bevor derselbe Schaden doppelt eingeplant wird. Solo Schaden und Eigenheilung erhalten; für [PvP](/pvp) Heilzugriff in Bewegung und eigene Kontrollbefreiung sichern.''', next_slug='cleric-build')

def write_pages():
    identities = json.loads((ROOT / 'src/content/class-identities.json').read_text(encoding='utf-8'))
    names = {x['id']: x['names'] for x in identities}
    alt = {'en': 'Official {name} class artwork.', 'ja': '{name}の公式クラスイラスト。', 'es': 'Ilustración oficial de {name}.', 'de': 'Offizielle Klassenillustration: {name}.'}
    for slug, copies in pages.items():
        for locale, copy in copies.items():
            body = copy['body'].strip()+'\n'
            toc = [{'id': id, 'title': re.sub('<[^>]+>', '', title)} for id, title in re.findall(r'<h2 id="([a-z0-9-]+)">(.*?)</h2>', body)]
            caption = alt[locale].format(name=names[slug][locale])
            meta = {k:copy[k] for k in ['title','description','summary','quickAnswer']}
            meta.update(toc=toc, visuals={'topic': {'assetId':'class-'+slug, 'alt':caption, 'caption':caption}}, inlineNext=re.findall(r'<GuideNext slug="([a-z0-9-]+)"', body))
            target = ROOT / 'src/content' / locale
            (target / (slug+'.mdx')).write_text(body, encoding='utf-8')
            (target / (slug+'.json')).write_text(json.dumps(meta, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('Created four class guides in four languages.')

if __name__ == '__main__':
    write_pages()
