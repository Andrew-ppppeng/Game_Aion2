"""Editorially authored localized class pages; source logs remain append-only."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PAGES = {}

def page(slug, locale, title, description, summary, body, alt='', caption=''):
    PAGES.setdefault(slug, {})[locale] = dict(title=title, description=description, summary=summary, body=body.strip()+'\n', alt=alt, caption=caption)

page('gladiator', 'en', 'AION 2 Gladiator Guide: Starter Build, Skills and Tanking',
     'Build an AION 2 Gladiator around useful passives, MP management and reachable defenses. Adapt a sourced early-game example for solo play or party tanking.',
     'Start with sustainable melee damage, select your unlocked skill options, and equip protection when your party asks you to tank.', r'''
Gladiator is the Global roster's heavy melee fighter. [NC's class introduction](https://aion2.plaync.com/en-us/about/index) presents its frontline identity. The starter build below follows [aLuckyRO's beginner demonstration](https://www.youtube.com/watch?v=wyjck6TfJiE): a newly leveled live-server character used to model early Global progression. Treat its choices as a starting example and compare the effects with your client.

<GuideVisual id="topic" />

<h2 id="gladiator-role">Gladiator's job: damage with frontline responsibility</h2>

Choose Gladiator if you enjoy fighting near the enemy, keeping an attack loop going, and reacting with defensive tools. In [Grobs' class walkthrough](https://www.youtube.com/watch?v=RXYBucBwRtk), it combines melee damage with self-sustain and can take a tanking role in suitable groups. That is a player's regional experience, not a guarantee that every fresh Global Gladiator can tank every encounter.

Before entering a dungeon, agree whether you are its tank or a damage dealer. Tanking adds enemy positioning and defensive timing to your own damage decisions. Compare [the other classes](/classes) if you want a shield-focused frontline role or ranged attacks instead.

<h2 id="starter-build">A practical Gladiator starter build</h2>

| Part of the setup | Starting choice in the demonstration | Check in your client |
| --- | --- | --- |
| Main attacks | Raise the attacks you can use consistently; select MP recovery or lower MP cost where available | Does the selected option keep your attack loop running? |
| Passives | Prioritize the demonstrated damage passives and Blood Absorption | Read the actual trigger, including any frontal requirement |
| Approach | Keep an unlocked gap closer reachable | Does its reset require a kill, and can you use it safely here? |
| Survival | Choose available HP recovery when learning; consider a damage option once survival is reliable | Is the death caused by a missed mechanic or insufficient recovery? |

aLuckyRO spends limited points on useful passives instead of maximizing every active skill. Blood Absorption, Overhead Slam and Crushing Wave appear in his explanation of sustain choices. Those English names follow the guide: match the description in your client rather than assuming identical translations or values.

Do not copy his point total or skill levels as universal unlock requirements. Your budget may differ. Preserve a repeatable attack loop, resource recovery and the job the party needs before investing in a less-used attack. The [build setup guide](/builds) explains how to record selected specializations and equipped Stigmas.

<h2 id="stigmas-and-tanking">Change Stigmas when you become the tank</h2>

The demonstration gives Focusing Block an important place when tanking. Keep it on a separate reachable control so you can use it for an enemy attack, rather than spending it automatically at the start of an ordinary damage loop. When another player tanks, the creator instead considers an offensive or defense-reducing Stigma for that slot.

This is a role-dependent tradeoff, not an instruction to remove all defense. Read your equipped skill's effect, confirm the group's tank, and keep the protection you need for the encounter. Do not fill PvE slots with control effects only because they look useful in a PvP clip; check whether the intended enemy can actually be affected.

<h2 id="manual-attack-loop">Learn the attack loop before simplifying controls</h2>

Start with your useful damage buffs, approach only when the enemy's position is safe, and use the strongest available attacks inside that opportunity. Fill cooldown gaps with your ordinary attack and watch MP. In the creator's demonstration, action and tab-target modes behave differently between skill presses; test your selected mode instead of assuming ordinary attacks continue by themselves.

Practice three actions separately: resume attacking after movement, interrupt for a defensive reaction, and recover when MP becomes low. Only then consider the game's built-in sequence controls. Keep a tanking block and situational movement independent. A damage sequence that makes you face the boss incorrectly or leaves no defensive response is an unsuitable tank setup.

<h2 id="daevanion-priorities">Daevanion: follow useful effects, not copied coordinates</h2>

aLuckyRO's regional starter example values offensive routes, combat speed and multi-hit choices, then upgrades important active skills and passives such as Blood Absorption. Use that reasoning to inspect your own board: identify an effect your setup uses, compare the cost to reach it, and check whether the upgrade changes the skill as expected.

The exact Global node layout, values and full optimal route are not independently established here. Avoid treating a later regional board as your point map. If the problem is missed attacks or repeated deaths, address that observed problem before following a recommendation to spend every point on offense.

<h2 id="solo-party-and-pvp">Adjust the build to the activity</h2>

For solo questing, useful resource recovery and controlled pulls help you keep moving. For a party damage role, return to a safe attack position after mechanics and coordinate debuffs. For tanking, preserve the defensive response and enemy position the party relies on. For [PvP](/pvp), reassess target access, control and survival separately instead of reusing a boss-damage setup unchanged.

**Why does my damage stop between attacks?** First check MP, your ordinary attack input, and whether a skill option was unlocked but never selected. Increasing skill level alone does not prove that its new effect is active.

**Can I use this as a complete endgame build?** It is a limited-progression starter. Recheck it when you gain new options, equipment or Stigma slots, and after a regional or Global balance update.

<GuideNext slug="builds" />
''', 'Official AION 2 Gladiator class artwork', 'Official Global Gladiator artwork. The starter choices below come from a named player demonstration, not a skill screen in this image.')

page('gladiator', 'ja', 'AION 2 グラディエーター：序盤ビルド・スキル・タンク運用',
     'AION 2 グラディエーターの序盤ビルドを、パッシブ、MP管理、防御操作から整理。出典付きの例をソロやパーティーの役割に合わせて調整します。',
     '継続できる近接攻撃を作り、解放済みのスキル特性を選択。タンクを担当する場合は必要な防御を装備しましょう。', r'''
グラディエーターはGlobalの近接前衛職です。[NCのクラス紹介](https://aion2.plaync.com/en-us/about/index)でその役割を確認できます。以下の序盤ビルドは[aLuckyROの初心者向け実演](https://www.youtube.com/watch?v=wyjck6TfJiE)を基にしています。既存の稼働地域で育てた新しいキャラクターを使い、Global序盤を想定した例です。自分のクライアントの効果説明と照らし合わせてください。

<GuideVisual id="topic" />

<h2 id="gladiator-role">近接火力と前衛の責任</h2>

敵の近くで攻撃を続けつつ、防御操作で対応する遊び方が好きなら候補になります。[Grobsのクラス解説](https://www.youtube.com/watch?v=RXYBucBwRtk)では、近接ダメージと自己回復を併せ持ち、条件の合うパーティーでタンクも担当できると説明されています。これは既存地域でのプレイヤー経験であり、作ったばかりのGlobalキャラクターがすべてのコンテンツを受け持てるという保証ではありません。

入場前に、自分がタンクなのか火力役なのかを決めましょう。タンクには攻撃以外に敵の位置と防御タイミングの管理が必要です。盾中心の前衛や遠距離攻撃を求めるなら、[他クラスの比較](/classes)も確認してください。

<h2 id="starter-build">実行しやすい序盤ビルド</h2>

| 要素 | 実演での序盤の選択 | 自分のクライアントで確認すること |
| --- | --- | --- |
| 主力攻撃 | 継続使用する攻撃を育て、使えるMP回復・消費軽減を選ぶ | 選択した特性で攻撃を継続できるか |
| パッシブ | 実演のダメージ系パッシブとBlood Absorptionを優先 | 正面などの発動条件を読む |
| 接近 | 解放済みの接近手段を操作しやすい場所に置く | 再使用に討伐条件があるか、今使って安全か |
| 生存 | 慣れる間は使えるHP回復を選び、安定後に火力特性を検討 | 死因がギミック失敗か回復不足か |

aLuckyROはすべてのアクティブを最大まで上げるより、有用なパッシブに限られたポイントを使います。回復の説明にはBlood Absorption、Overhead Slam、Crushing Waveが登場します。英語名は動画に従っているため、自分のクライアントでは名前だけでなく説明を確認してください。

動画のポイント総数やスキルレベルを、共通の解放条件としてコピーしないでください。まず攻撃の流れ、MP回復、パーティーに必要な役割を確保します。[ビルドの組み方](/builds)では特性の選択とStigmaの装備を整理できます。

<h2 id="stigmas-and-tanking">タンクを担当するときのStigma</h2>

実演ではタンク用にFocusing Blockを重視しています。通常の攻撃列で自動消費するより、敵の攻撃に合わせて使える独立したキーに置きましょう。他の人がタンクを担当する場合、作者はその枠に攻撃や敵の防御低下を検討しています。

これは役割による調整です。必要な防御まで外す意味ではありません。現在の効果、担当タンク、戦闘に必要な保護を確認します。PvP動画で便利に見えた行動妨害をPvEに入れる前に、対象の敵に効くかを調べてください。

<h2 id="manual-attack-loop">操作をまとめる前に攻撃を覚える</h2>

有用な火力バフを使い、安全な敵位置へ接近し、攻撃機会に主力を使います。クールダウンの間は通常攻撃とMPを確認してください。作者の実演ではアクション方式とターゲット方式でスキル後の動作が異なります。自分の操作方式で通常攻撃が続くか試しましょう。

移動後の攻撃再開、防御による中断、MP不足への対応を別々に練習します。その後にゲーム内の連続操作を検討してください。タンクのブロックや状況依存の移動は独立させます。敵の向きを乱したり、防御対応できなくなる攻撃列はタンク運用に不向きです。

<h2 id="daevanion-priorities">Daevanionは座標より効果で選ぶ</h2>

aLuckyROの地域版序盤例では、攻撃系ルート、戦闘速度、複数ヒットを重視し、その後にBlood Absorptionなどの重要スキルを強化します。同じ考え方で自分の盤を調べましょう。使用する効果を探し、そこへ到達する費用を比較して、強化後の動作を確認します。

Globalの完全なノード配置、数値、最適ルートはここでは独立検証していません。後期の地域版画像をそのまま配分図にしないでください。命中失敗や死亡が問題なら、すべてを火力に振る提案より、実際の問題への対処を先にします。

<h2 id="solo-party-and-pvp">遊ぶ内容に合わせて調整</h2>

ソロではMP回復と無理のない敵数で進めます。パーティーの火力役ではギミック後に安全な位置へ戻り、弱体化を相談します。タンクなら仲間が頼る防御と敵の位置を優先します。[PvP](/pvp)では接近、行動妨害、生存を改めて検討し、ボス用設定をそのまま流用しないでください。

**攻撃が途中で止まる場合は？** MP、通常攻撃の入力、解放したまま選択していない特性を確認します。スキルレベルを上げただけでは新しい効果が有効とは限りません。

**最終ビルドとして使えますか？** 限られた育成段階の出発点です。新しい特性、装備、Stigma枠、バランス更新に合わせて見直しましょう。

<GuideNext slug="builds" />
''', 'AION 2 グラディエーターの公式クラスアート', 'Global公式のグラディエーター画像です。序盤の選択例は紹介したプレイヤーの実演に基づき、画像内のスキル画面を示すものではありません。')

page('gladiator', 'es', 'AION 2 Gladiador: build inicial, habilidades y tanque',
     'Prepara un Gladiador de AION 2 con pasivas útiles, gestión de MP y defensas accesibles. Adapta un ejemplo documentado a juego en solitario o al rol de tanque.',
     'Empieza con daño cuerpo a cuerpo sostenible, selecciona las mejoras desbloqueadas y equipa protección cuando tu grupo necesite que tanques.', r'''
El Gladiador es el combatiente pesado cuerpo a cuerpo de Global. [La presentación de NC](https://aion2.plaync.com/en-us/about/index) confirma su identidad de primera línea. La build inicial sigue [la demostración de aLuckyRO](https://www.youtube.com/watch?v=wyjck6TfJiE): un personaje recién subido en un servidor regional para representar la progresión inicial de Global. Contrasta sus elecciones con las descripciones de tu cliente.

<GuideVisual id="topic" />

<h2 id="gladiator-role">Daño con responsabilidad en primera línea</h2>

Elige Gladiador si disfrutas atacando cerca del enemigo y reaccionando con defensas. [Grobs](https://www.youtube.com/watch?v=RXYBucBwRtk) describe daño, recuperación propia y la posibilidad de tanquear en grupos adecuados. Es experiencia de un jugador en versiones regionales, sin garantizar que cualquier Gladiador nuevo de Global pueda tanquear todos los encuentros.

Antes de entrar, acordad si serás tanque o responsable de daño. Tanquear añade posicionamiento del enemigo y uso oportuno de defensas. Consulta [las otras clases](/classes) si prefieres una primera línea centrada en el escudo o ataques a distancia.

<h2 id="starter-build">Una build inicial que puedes poner en práctica</h2>

| Parte | Elección inicial de la demostración | Qué comprobar en tu cliente |
| --- | --- | --- |
| Ataques principales | Mejora los ataques constantes y elige recuperación o menor consumo de MP disponibles | ¿La opción permite mantener los ataques? |
| Pasivas | Prioriza las pasivas de daño mostradas y Blood Absorption | Lee la condición, incluido cualquier requisito frontal |
| Acercamiento | Deja accesible una habilidad de aproximación desbloqueada | ¿El reinicio exige matar y resulta seguro usarla aquí? |
| Supervivencia | Usa recuperación de HP al aprender y considera daño cuando sobrevivas con regularidad | ¿Mueres por una mecánica o por falta de recuperación? |

aLuckyRO invierte puntos limitados en pasivas útiles en lugar de maximizar todos los ataques. Blood Absorption, Overhead Slam y Crushing Wave aparecen en sus opciones de recuperación. Los nombres ingleses siguen el vídeo; identifica el efecto en tu cliente en vez de asumir traducciones o cifras idénticas.

No copies su presupuesto o niveles como requisitos universales. Conserva primero un ciclo repetible, recuperación de recursos y la función necesaria para el grupo. [La guía de builds](/builds) explica cómo registrar especializaciones seleccionadas y Stigmas equipados.

<h2 id="stigmas-and-tanking">Cambia Stigmas cuando seas el tanque</h2>

El ejemplo da importancia a Focusing Block al tanquear. Colócalo en un control independiente y accesible para responder a un ataque enemigo, sin gastarlo automáticamente al empezar el ciclo. Si otra persona tanquea, el autor considera una opción ofensiva o de reducción de defensa para ese espacio.

Es una elección según el rol. Lee el efecto actual, confirma quién tanquea y conserva la protección necesaria. Antes de equipar en PvE un control visto en PvP, comprueba que afecta al enemigo previsto.

<h2 id="manual-attack-loop">Aprende el ciclo antes de simplificar controles</h2>

Activa los beneficios de daño útiles, acércate cuando la posición sea segura y emplea tus ataques principales durante esa oportunidad. Entre enfriamientos, usa el ataque normal y vigila MP. La demostración muestra comportamientos distintos entre modo de acción y selección de objetivo; prueba tu modo para saber si continúan los ataques normales.

Practica por separado volver a atacar tras moverte, interrumpir para defenderte y responder a la falta de MP. Después considera las secuencias del juego. Mantén independientes el bloqueo de tanque y el movimiento situacional. Una secuencia que cambia mal la orientación del jefe o impide defenderte no sirve para tanquear.

<h2 id="daevanion-priorities">Daevanion: efectos útiles antes que coordenadas</h2>

El ejemplo regional de aLuckyRO prioriza rutas ofensivas, velocidad de combate y múltiples impactos, después mejoras de ataques y pasivas importantes como Blood Absorption. Aplica ese razonamiento a tu tablero: localiza un efecto que uses, compara el coste de llegar y comprueba la habilidad después de mejorarla.

La disposición exacta de Global, las cifras y una ruta óptima completa no se han verificado aquí. Evita copiar un tablero regional avanzado. Si fallas ataques o mueres repetidamente, resuelve ese problema observable antes de invertir todo en daño.

<h2 id="solo-party-and-pvp">Adapta la build a la actividad</h2>

Para misiones en solitario, conserva recursos y controla los grupos de enemigos. Como atacante de grupo, vuelve a una posición segura después de las mecánicas y coordina perjuicios. Como tanque, protege la posición y la respuesta defensiva que necesita el equipo. Para [PvP](/pvp), reconsidera acceso al objetivo, control y supervivencia.

**¿Por qué se detienen mis ataques?** Comprueba MP, entrada del ataque normal y si desbloqueaste una especialización sin seleccionarla. Subir el nivel no demuestra que su efecto esté activo.

**¿Es una build final?** Es un punto de partida con progresión limitada. Revísalo al conseguir nuevas opciones, equipo, espacios de Stigma o cambios de balance.

<GuideNext slug="builds" />
''', 'Ilustración oficial del Gladiador de AION 2', 'Ilustración oficial del Gladiador de Global. Las elecciones iniciales proceden de la demostración del jugador citado, no de una pantalla de habilidades en esta imagen.')

page('gladiator', 'de', 'AION 2 Gladiator: Einstiegsbuild, Fertigkeiten und Tanken',
     'Stelle einen AION 2 Gladiator mit passenden Passiven, MP-Versorgung und erreichbaren Defensiven auf. Passe ein belegtes Einstiegsbeispiel an Solo-Spiel oder Tanken an.',
     'Beginne mit dauerhaft nutzbaren Nahkampfangriffen, wähle freigeschaltete Optionen und rüste Schutz aus, wenn deine Gruppe dich als Tank braucht.', r'''
Der Gladiator ist Globals schwerer Nahkämpfer. [NCs Klassenvorstellung](https://aion2.plaync.com/en-us/about/index) bestätigt seine Frontlinienrolle. Der Einstiegsbuild folgt [aLuckyROs Anfängerbeispiel](https://www.youtube.com/watch?v=wyjck6TfJiE): einem frisch gelevelten Charakter einer bestehenden Regionalversion, der frühe Global-Fortschritte nachbilden soll. Vergleiche die Entscheidungen mit den Beschreibungen deines Clients.

<GuideVisual id="topic" />

<h2 id="gladiator-role">Schaden mit Verantwortung an der Front</h2>

Wähle Gladiator, wenn du gern nahe am Gegner angreifst und mit Defensivfertigkeiten reagierst. [Grobs' Klassenübersicht](https://www.youtube.com/watch?v=RXYBucBwRtk) beschreibt Nahkampfschaden, eigene Regeneration und eine mögliche Tankrolle in geeigneten Gruppen. Das ist regionale Spielererfahrung und keine Garantie, dass jeder neue Global-Gladiator jeden Kampf tanken kann.

Kläre vor dem Dungeon, ob du tankst oder Schaden verursachst. Als Tank verantwortest du zusätzlich Gegnerposition und defensive Reaktionen. Vergleiche [die anderen Klassen](/classes), wenn du eine stärker auf den Schild ausgerichtete Frontlinie oder Fernangriffe suchst.

<h2 id="starter-build">Ein praktisch nutzbarer Einstiegsbuild</h2>

| Teil | Einstiegsentscheidung im Beispiel | Im eigenen Client prüfen |
| --- | --- | --- |
| Hauptangriffe | Regelmäßig genutzte Angriffe verbessern und verfügbare MP-Erholung oder Kostenreduktion wählen | Hält die Option deine Angriffe am Laufen? |
| Passive | Gezeigte Schadenspassive und Blood Absorption priorisieren | Auslöser lesen, einschließlich möglicher Frontbedingungen |
| Annäherung | Einen freigeschalteten Ansturm erreichbar halten | Braucht der Reset einen Kill und ist der Einsatz hier sicher? |
| Überleben | Beim Lernen verfügbare HP-Erholung wählen; später eine Schadensoption erwägen | Liegt der Tod an einer Mechanik oder fehlender Erholung? |

aLuckyRO investiert begrenzte Punkte in nützliche Passive, statt jeden aktiven Angriff zu maximieren. Blood Absorption, Overhead Slam und Crushing Wave kommen bei seinen Erholungsoptionen vor. Die englischen Namen folgen dem Video: Vergleiche den Effekt im Client, statt identische Übersetzungen oder Werte anzunehmen.

Kopiere sein Punktebudget und die Fertigkeitsstufen nicht als allgemeine Freischaltbedingungen. Sichere zuerst einen wiederholbaren Ablauf, Ressourcenversorgung und deine Gruppenaufgabe. Der [Build-Leitfaden](/builds) erklärt das Festhalten ausgewählter Spezialisierungen und ausgerüsteter Stigmas.

<h2 id="stigmas-and-tanking">Stigmas für die Tankrolle anpassen</h2>

Im Beispiel ist Focusing Block beim Tanken wichtig. Halte ihn auf einer eigenen erreichbaren Taste, um auf einen gegnerischen Angriff zu reagieren. Verbrauche ihn nicht automatisch zu Beginn gewöhnlicher Schadensfolgen. Wenn jemand anderes tankt, erwägt der Autor für diesen Platz eine offensive oder verteidigungssenkende Option.

Das ist eine Entscheidung nach Rolle. Lies den aktuellen Effekt, bestätige den Tank und behalte den Schutz, den der Kampf braucht. Prüfe vor dem Einsatz einer aus PvP bekannten Kontrolle in PvE, ob sie den vorgesehenen Gegner betrifft.

<h2 id="manual-attack-loop">Den Ablauf vor vereinfachten Tasten lernen</h2>

Nutze passende Schadensbuffs, nähere dich erst bei sicherer Gegnerposition und setze die Hauptangriffe im passenden Fenster ein. Fülle Abklingzeiten mit normalen Angriffen und beobachte MP. Im Beispiel unterscheiden sich Aktions- und Zielmodus zwischen Tastendrücken. Teste deinen Modus, statt automatische normale Angriffe vorauszusetzen.

Übe getrennt das Weiterangreifen nach Bewegung, die Unterbrechung für Schutz und den Umgang mit wenig MP. Erwäge erst danach die eingebauten Sequenzfunktionen. Tankblock und situationsabhängige Bewegung bleiben separat. Eine Folge, die den Boss ungünstig dreht oder eine Schutzreaktion verhindert, eignet sich nicht zum Tanken.

<h2 id="daevanion-priorities">Daevanion nach Effekten auswählen</h2>

aLuckyROs regionales Einstiegsbeispiel bevorzugt offensive Wege, Kampftempo und Mehrfachtreffer, danach wichtige aktive und passive Verbesserungen wie Blood Absorption. Nutze diese Überlegung auf deinem Board: Suche einen verwendeten Effekt, vergleiche die Wegkosten und prüfe die Fertigkeit nach der Verbesserung.

Globals genaue Knoten, Werte und ein vollständiger optimaler Weg sind hier nicht unabhängig bestätigt. Übernimm kein späteres Regionalboard als Punktkarte. Verfehlst du Angriffe oder stirbst wiederholt, löse das beobachtete Problem vor einer pauschalen Verteilung aller Punkte auf Schaden.

<h2 id="solo-party-and-pvp">Nach Aktivität anpassen</h2>

Beim Solo-Questen helfen Ressourcenversorgung und kontrollierte Gegnergruppen. Als Gruppenschadensrolle kehrst du nach Mechaniken in eine sichere Angriffsposition zurück und stimmst Debuffs ab. Als Tank erhältst du die defensive Reaktion und Gegnerposition für die Gruppe. Für [PvP](/pvp) bewertest du Zielzugang, Kontrolle und Überleben neu.

**Warum stoppen meine Angriffe?** Prüfe MP, die Eingabe für normale Angriffe und freigeschaltete, aber nicht ausgewählte Optionen. Eine höhere Fertigkeitsstufe allein bestätigt keinen aktiven Zusatz.

**Ist das ein Endgame-Build?** Es ist ein Einstieg mit begrenztem Fortschritt. Prüfe ihn bei neuen Optionen, Ausrüstung, Stigmaplätzen und Balanceänderungen erneut.

<GuideNext slug="builds" />
''', 'Offizielle AION 2 Klassenillustration des Gladiators', 'Offizielle Global-Illustration des Gladiators. Die Einstiegsentscheidungen stammen aus dem genannten Spielerbeispiel und nicht aus einem Fertigkeitsfenster im Bild.')

def write_pages():
    for slug, locales in PAGES.items():
        for locale, content in locales.items():
            headings = re.findall(r'<h2 id="([a-z0-9-]+)">([^<]+)</h2>', content['body'])
            meta = {key: content[key] for key in ['title', 'description', 'summary']}
            meta['toc'] = [{'id': id, 'title': title} for id, title in headings]
            meta['visuals'] = {'topic': {'assetId': 'class-'+slug, 'alt': content['alt'], 'caption': content['caption']}}
            if slug == 'races':
                meta['visuals'] = {'topic': {'title': content['alt'], 'caption': content['caption'], 'steps': content['steps']}}
            meta['inlineNext'] = re.findall(r'<GuideNext slug="([a-z0-9-]+)" />', content['body'])
            directory = ROOT / 'src' / 'content' / locale
            for suffix, text in [('json', json.dumps(meta, ensure_ascii=False, indent=2)+'\n'), ('mdx', content['body'])]:
                target = directory / (slug+'.'+suffix)
                if target.exists():
                    raise RuntimeError(f'Append-only generator will not replace {target}')
                target.write_text(text, encoding='utf-8')

page('races', 'en', 'AION 2 Races Guide: Elyos, Asmodians and Choosing a Faction',
     'Choose between AION 2 Elyos and Asmodians using official Global faction, server-pairing and transfer rules. Coordinate friends before creating your character.',
     'Choose your faction together with your region and server. Opposing server pairings determine cross-faction opponents and can change over time.', r'''
AION 2's playable faction choice is **Elyos or Asmodians**, as shown in [NC's Global introduction](https://aion2.plaync.com/en-us/about/index). If you are searching for races, this is the practical choice to settle before character creation. Choose with your friends first: faction affects your server choice and the opposing side you encounter in cross-faction modes.

<h2 id="elyos-or-asmodians">Elyos or Asmodians: what differs?</h2>

| Choice | Official world identity | Useful decision |
| --- | --- | --- |
| Elyos | Light-associated faction with Global world locations in Verteron, including Cantas Valley and Dawn Legion Base | Choose it if its world and your group's faction suit you |
| Asmodians | Shadow-associated faction with Global world locations in Altgard, including Safe Haven and Moslan Forest | Choose it if its world and your group's faction suit you |
| Class | The Global introduction lists eight classes separately from faction | Choose a combat role using the class roster, not an unverified racial damage ranking |

The official descriptions establish world identity. They do not supply a measured universal advantage for either faction. This guide does not invent racial damage bonuses, a population winner or a permanent PvP advantage. Preview the world and [character creation](/character-creation), then compare [classes](/classes) for the job you actually want to play.

<h2 id="choose-with-friends">Choose faction and server with friends</h2>

Agree on region, faction and exact server before finalizing the character. A familiar server name alone is insufficient: the same name can appear in different regions. Send a full choice such as Europe, Elyos, Siel rather than only Siel.

NC's [server-matchmaking explanation](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939) states that Elyos and Asmodians live on their own servers. Being assigned an opposing-faction server is a war matchup, not a shared home server. Use [the server guide](/server) to compare the official region and faction lists, then check current creation availability in the client.

NC separately confirms cross-server instanced content, including dungeons, in its [transfer announcement](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2). That statement does not establish cross-region grouping or cross-faction cooperation. For a reliable shared questing plan, choose the same region, faction and server.

<GuideVisual id="topic" />

<h2 id="cross-faction-opponents">How faction affects your opponents</h2>

The matchmaking announcement pairs an Elyos server with an Asmodian server for a limited period. In cross-faction activities such as the Abyss and Spacetime Rifts, the opposing players come from the matched server. NC says those pairings will change periodically to maintain faction balance.

Treat a pairing table as a dated snapshot. A current opposing guild or population does not establish your opponent forever. See [PvP modes](/pvp) to understand which activity you are preparing for, and [Spacetime Rifts](/spacetime-rift) before planning a trip into opposing territory. This faction page does not provide an unverified Global rift schedule.

<h2 id="changing-faction">Can a server transfer change your faction?</h2>

The official transfer notice checked on October 3 announces transfers starting **October 14, 2026, within the same faction**. It also limits Early Access characters to Early Access servers initially. Those announced transfers therefore cannot be used as evidence that an Elyos character can become Asmodian, or the reverse.

No independent Global faction-change procedure, price or cooldown is verified here. Do not finalize a faction on the assumption that a paid voucher or future server transfer will fix it. Appearance changes are a separate decision; an appearance preset does not establish a faction change.

<h2 id="faction-choice-checklist">A useful final check before creation</h2>

1. Ask your group for its complete region, faction and server choice.
2. Check the client currently allows creation on that server; keep a same-faction backup agreed with everyone.
3. Preview the desired faction's world and appearance options.
4. Select the class whose actual responsibility you enjoy.
5. Read any restriction shown before confirming; do not substitute an old KR/TW rule for Global.

**Which faction is best for a beginner?** The verified sources do not establish a universal winner. Friends, server availability and your preferred world are actionable starting criteria.

**Does server pairing let me quest with the other faction?** The cited pairing describes opponents in cross-faction modes. It does not confirm shared ordinary questing with the opposite side.

**Are faction and class the same choice?** No. The official introduction presents the two factions and the class roster separately. Settle both decisions before investing time in customization.

<GuideNext slug="server" />
''', 'Choose a faction with your group', 'A practical decision order based on the official Global server and faction rules. Check current creation availability before confirming.')
PAGES['races']['en']['steps'] = [
    {'label': 'Agree on region', 'description': 'Use the same region as the friends you want to quest with.'},
    {'label': 'Agree on faction', 'description': 'Choose Elyos or Asmodians together before selecting a server.'},
    {'label': 'Confirm the server', 'description': 'Check the exact name, creation availability and a same-faction backup.'}
]

page('races', 'ja', 'AION 2 種族ガイド：天族・魔族と陣営の選び方',
     'AION 2 の天族と魔族を、Global公式の世界紹介、サーバーマッチング、移動ルールから比較。キャラクター作成前に仲間と陣営を合わせましょう。',
     '地域・陣営・サーバーをまとめて選択。敵対サーバーの組み合わせが対人コンテンツの相手を決め、定期的に変更されます。', r'''
AION 2で選ぶ陣営は **天族（Elyos）または魔族（Asmodians）** です。[NCのGlobal紹介](https://aion2.plaync.com/en-us/about/index)で確認できます。種族を調べているなら、キャラクター作成前に決める実際の選択はこの二つです。陣営はサーバー選択と敵対コンテンツの相手に関わるため、最初に仲間と合わせましょう。

<h2 id="elyos-or-asmodians">天族と魔族の違い</h2>

| 選択 | 公式の世界設定 | 判断に使える点 |
| --- | --- | --- |
| 天族 | 光に関連する陣営。ベルテロンにはCantas ValleyやDawn Legion Baseが登場 | 世界観と仲間の陣営が合う場合に選ぶ |
| 魔族 | 影に関連する陣営。アルトガルドにはSafe HavenやMoslan Forestが登場 | 世界観と仲間の陣営が合う場合に選ぶ |
| クラス | Global紹介は陣営と別に八クラスを掲載 | 未検証の種族火力順位ではなく役割で選ぶ |

公式の説明は世界設定を確認できる資料です。両陣営の共通する数値的優劣は示していません。種族ダメージボーナス、人口の勝者、恒久的なPvP優位を作っていません。世界と[キャラクター作成](/character-creation)を確認し、[クラス](/classes)で好きな役割を選んでください。

<h2 id="choose-with-friends">仲間と陣営・サーバーを合わせる</h2>

確定前に地域、陣営、正確なサーバー名を決めます。同名サーバーが複数地域にあるため、名前だけでは不十分です。Sielだけでなく「Europe・天族・Siel」のように伝えましょう。

NCの[サーバーマッチング説明](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939)では天族と魔族は別のサーバーに住みます。敵対陣営との組み合わせは対戦相手の指定で、共有の本拠サーバーではありません。[サーバーガイド](/server)で公式の地域・陣営一覧を見て、作成可否はクライアントで確認します。

[移動の告知](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2)ではダンジョンを含むインスタンスのサーバー間利用を確認できます。ただし地域間や陣営間の協力は確定しません。一緒に通常クエストを進めるなら、同じ地域・陣営・サーバーを選びましょう。

<GuideVisual id="topic" />

<h2 id="cross-faction-opponents">陣営と対戦相手の関係</h2>

告知では一定期間、天族サーバーと魔族サーバーを組み合わせます。アビスや時空の亀裂などでは、組み合わされた敵対サーバーのプレイヤーと遭遇します。NCは陣営バランスのため定期的に組み合わせを変更すると説明しています。

配対表は日付付きの記録として使います。現在の敵ギルドや人口が永続的な相手とは限りません。[PvPモード](/pvp)で参加する内容を確認し、敵側へ行く前に[時空の亀裂](/spacetime-rift)を読みましょう。このページでは未検証のGlobal亀裂日程を掲載していません。

<h2 id="changing-faction">サーバー移動で陣営を変えられる？</h2>

10月3日に確認した公式告知は、**2026年10月14日から同じ陣営内で移動**すると説明しています。当初はEarly AccessキャラクターがEarly Accessサーバーへ移る制限もあります。これを天族から魔族、または逆に変われる根拠にはできません。

Globalの独立した陣営変更手順、価格、再使用期間はここでは検証していません。チケットや将来の移動で解決できると想定せずに選んでください。外見変更は別の操作で、外見プリセットから陣営変更は確定しません。

<h2 id="faction-choice-checklist">作成前の最終確認</h2>

1. 仲間の地域・陣営・サーバーをすべて聞く。
2. 作成可能かを確認し、同陣営の予備サーバーも全員で決める。
3. 選ぶ陣営の世界と外見設定を確認する。
4. 自分が楽しめる実際の役割からクラスを選ぶ。
5. 確定画面の制限を読み、古いKR/TWルールでGlobalを判断しない。

**初心者にはどちらが強い？** 共通の勝者は検証されていません。仲間、作成可否、好みの世界観が判断しやすい条件です。

**配対相手と一緒にクエストできる？** 告知は敵対モードの相手を説明しており、逆陣営との通常クエスト共有を確認する資料ではありません。

**陣営とクラスは同じ？** 別です。公式紹介は二陣営とクラス一覧を分けています。外見に時間を使う前に両方を決めましょう。

<GuideNext slug="server" />
''', '仲間と陣営を決める順番', 'Global公式のサーバー・陣営ルールに基づく選択順です。確定前に現在のキャラクター作成可否を確認してください。')
PAGES['races']['ja']['steps'] = [
    {'label': '地域を合わせる', 'description': '一緒にクエストをする仲間と同じ地域を選びます。'},
    {'label': '陣営を合わせる', 'description': 'サーバーを選ぶ前に天族か魔族かを相談します。'},
    {'label': 'サーバーを確認', 'description': '正確な名前、作成可否、同陣営の予備を確認します。'}
]

page('races', 'es', 'AION 2 Razas: Elios, Asmodianos y elección de facción',
     'Elige entre Elios y Asmodianos de AION 2 con las reglas oficiales Global de facciones, emparejamiento y traslados. Coordina tu grupo antes de crear el personaje.',
     'Elige facción junto con región y servidor. Los emparejamientos determinan enemigos en modos entre facciones y pueden cambiar periódicamente.', r'''
La elección de facción jugable de AION 2 es **Elios o Asmodianos**, según [la presentación Global de NC](https://aion2.plaync.com/en-us/about/index). Si buscas razas, esta es la decisión práctica antes de crear el personaje. Acuérdala con tus amigos: afecta al servidor y a los adversarios de los modos entre facciones.

<h2 id="elyos-or-asmodians">Elios o Asmodianos: diferencias</h2>

| Elección | Identidad oficial del mundo | Decisión útil |
| --- | --- | --- |
| Elios | Facción asociada a la luz; Verteron incluye Cantas Valley y Dawn Legion Base | Elígela si encaja con tu mundo preferido y tu grupo |
| Asmodianos | Facción asociada a las sombras; Altgard incluye Safe Haven y Moslan Forest | Elígela si encaja con tu mundo preferido y tu grupo |
| Clase | La presentación Global muestra ocho clases aparte de la facción | Decide por función, sin usar clasificaciones raciales no verificadas |

Las descripciones confirman identidad del mundo, sin medir una ventaja universal. No inventamos bonificaciones raciales de daño, ganadores de población o ventajas permanentes de PvP. Revisa [la creación de personaje](/character-creation) y compara [las clases](/classes) según el papel que quieres jugar.

<h2 id="choose-with-friends">Coordina facción y servidor con amigos</h2>

Elegid región, facción y nombre exacto antes de confirmar. Un nombre puede aparecer en varias regiones: comunica Europe, Elios, Siel, en lugar de solo Siel.

[La explicación de emparejamiento de NC](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939) indica que cada facción vive en sus propios servidores. El emparejamiento identifica rivales, no un servidor de origen compartido. Consulta [la guía de servidores](/server) y comprueba la creación actual en el cliente.

[El anuncio de traslados](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2) confirma contenido instanciado entre servidores, incluidas mazmorras. No confirma grupos entre regiones o cooperación entre facciones. Para hacer misiones juntos, acordad la misma región, facción y servidor.

<GuideVisual id="topic" />

<h2 id="cross-faction-opponents">Cómo determina tus rivales la facción</h2>

El anuncio empareja un servidor Elios con uno Asmodiano durante un período limitado. En actividades como el Abismo y las Grietas Espaciotemporales, los rivales proceden del servidor emparejado. NC cambiará estas parejas periódicamente para equilibrar facciones.

Usa la tabla como una instantánea fechada. Un gremio rival o población actual no define al enemigo para siempre. Consulta [los modos PvP](/pvp) y [las grietas](/spacetime-rift) antes de viajar a territorio contrario. Esta página no aporta un horario Global sin verificar.

<h2 id="changing-faction">¿Un traslado permite cambiar de facción?</h2>

El aviso comprobado el 3 de octubre anuncia traslados desde el **14 de octubre de 2026, dentro de la misma facción**. Al principio, los personajes Early Access solo podrán ir a servidores Early Access. No demuestra que puedas pasar de Elios a Asmodiano o al revés.

No verificamos un procedimiento, precio o espera independiente para cambiar facción en Global. No elijas suponiendo que un cupón o traslado futuro lo solucionará. Cambiar apariencia es otra decisión y un preset no confirma cambio de facción.

<h2 id="faction-choice-checklist">Comprueba antes de crear</h2>

1. Pide región, facción y servidor completos a tu grupo.
2. Comprueba que admite creación y acordad una alternativa de la misma facción.
3. Previsualiza mundo y apariencia de la facción.
4. Elige una clase por la responsabilidad que disfrutas.
5. Lee las restricciones y no sustituyas Global por reglas antiguas de KR/TW.

**¿Qué facción es mejor para principiantes?** Las fuentes no establecen un ganador universal. Amigos, disponibilidad y preferencias de mundo son criterios prácticos.

**¿El emparejamiento permite misiones con la otra facción?** Describe adversarios en modos entre facciones, sin confirmar misiones ordinarias compartidas.

**¿Facción y clase son lo mismo?** Son decisiones distintas en la presentación oficial. Resuelve ambas antes de dedicar tiempo a personalizar.

<GuideNext slug="server" />
''', 'Elige facción con tu grupo', 'Orden práctico basado en las reglas oficiales Global de facciones y servidores. Comprueba la disponibilidad actual de creación antes de confirmar.')
PAGES['races']['es']['steps'] = [
    {'label': 'Acordad región', 'description': 'Usad la misma región que los amigos con quienes haréis misiones.'},
    {'label': 'Acordad facción', 'description': 'Elegid Elios o Asmodianos juntos antes del servidor.'},
    {'label': 'Confirmad servidor', 'description': 'Comprobad nombre exacto, creación y una alternativa de la misma facción.'}
]

page('races', 'de', 'AION 2 Völker: Elyos, Asmodier und Fraktionswahl',
     'Wähle AION 2 Elyos oder Asmodier anhand offizieller Global-Regeln zu Fraktionen, Paarungen und Transfers. Stimme dich vor der Erstellung mit Freunden ab.',
     'Wähle Fraktion, Region und Server gemeinsam. Die zeitlich begrenzten Paarungen bestimmen Gegner in fraktionsübergreifenden Modi.', r'''
Die spielbare Fraktionswahl in AION 2 ist **Elyos oder Asmodier**, wie [NCs Global-Vorstellung](https://aion2.plaync.com/en-us/about/index) zeigt. Wer nach Völkern sucht, sollte diese praktische Entscheidung vor der Charaktererstellung treffen. Stimme dich zuerst mit Freunden ab: Die Fraktion beeinflusst Server und Gegner in fraktionsübergreifenden Modi.

<h2 id="elyos-or-asmodians">Elyos oder Asmodier: Unterschiede</h2>

| Wahl | Offizielle Weltidentität | Nützliche Entscheidung |
| --- | --- | --- |
| Elyos | Lichtbezogene Fraktion; Verteron zeigt Cantas Valley und Dawn Legion Base | Wählen, wenn Welt und Gruppenfraktion passen |
| Asmodier | Schattenbezogene Fraktion; Altgard zeigt Safe Haven und Moslan Forest | Wählen, wenn Welt und Gruppenfraktion passen |
| Klasse | Die Global-Vorstellung nennt acht Klassen getrennt von der Fraktion | Nach Rolle statt unbelegter Volk-Schadensrangfolge wählen |

Die Beschreibungen bestätigen die Weltidentität, aber keinen gemessenen allgemeinen Vorteil. Hier werden weder Volk-Schadensboni noch Populationserfolge oder dauerhafte PvP-Vorteile erfunden. Prüfe die [Charaktererstellung](/character-creation) und vergleiche [Klassen](/classes) nach der gewünschten Aufgabe.

<h2 id="choose-with-friends">Fraktion und Server mit Freunden wählen</h2>

Einigt euch vor der Bestätigung auf Region, Fraktion und genauen Server. Ein Name kann in mehreren Regionen vorkommen. Nenne beispielsweise Europe, Elyos, Siel statt nur Siel.

[NCs Paarungserklärung](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939) bestätigt getrennte Fraktionsserver. Ein gegnerischer Paarungsserver ist ein Kriegsgegner und kein gemeinsamer Heimatserver. Nutze den [Serverleitfaden](/server) und prüfe aktuelle Erstellungsmöglichkeiten im Client.

Die [Transferankündigung](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2) bestätigt serverübergreifende Instanzen einschließlich Dungeons. Sie bestätigt keine regionsübergreifenden Gruppen oder Zusammenarbeit zwischen Fraktionen. Für gemeinsame normale Quests wählt dieselbe Region, Fraktion und denselben Server.

<GuideVisual id="topic" />

<h2 id="cross-faction-opponents">Wie die Fraktion Gegner bestimmt</h2>

Die Ankündigung verbindet für eine begrenzte Zeit einen Elyos- mit einem Asmodier-Server. In Abyss und Raumzeitrissen stammen gegnerische Spieler vom zugeordneten Server. NC ändert Paarungen regelmäßig für ein ausgeglicheneres Fraktionsverhältnis.

Eine Paarungstabelle ist eine datierte Momentaufnahme. Die aktuelle gegnerische Gilde oder Population legt Gegner nicht dauerhaft fest. Lies [PvP-Modi](/pvp) und [Raumzeitrisse](/spacetime-rift) vor einer Reise ins gegnerische Gebiet. Diese Seite nennt keinen unbestätigten Global-Zeitplan.

<h2 id="changing-faction">Ändert ein Servertransfer die Fraktion?</h2>

Die am 3. Oktober geprüfte Ankündigung nennt Transfers ab **14. Oktober 2026 innerhalb derselben Fraktion**. Anfangs dürfen Early-Access-Charaktere nur auf Early-Access-Server. Das belegt keinen Wechsel von Elyos zu Asmodiern oder umgekehrt.

Ein separates Global-Verfahren, Preis oder Wartezeit für Fraktionswechsel ist hier nicht bestätigt. Wähle nicht unter der Annahme, ein Gutschein oder späterer Transfer löse die Entscheidung auf. Aussehensänderungen sind separat; eine Vorlage bestätigt keinen Fraktionswechsel.

<h2 id="faction-choice-checklist">Vor der Erstellung prüfen</h2>

1. Frage die Gruppe nach vollständiger Region, Fraktion und Server.
2. Prüfe Erstellung und vereinbare einen Ersatz derselben Fraktion.
3. Sieh dir Welt und Aussehensoptionen an.
4. Wähle eine Klasse nach ihrer tatsächlichen Aufgabe.
5. Lies Einschränkungen, statt alte KR/TW-Regeln auf Global zu übertragen.

**Welche Fraktion ist für Anfänger besser?** Die Quellen nennen keinen allgemeinen Sieger. Freunde, Verfügbarkeit und Weltvorliebe sind praktische Kriterien.

**Kann ich mit dem Paarungsgegner questen?** Die Paarung beschreibt Gegner in entsprechenden Modi, keine bestätigten gemeinsamen normalen Quests.

**Sind Fraktion und Klasse dieselbe Wahl?** Die offizielle Vorstellung trennt beide. Entscheide sie vor aufwendiger Anpassung.

<GuideNext slug="server" />
''', 'Fraktion gemeinsam mit der Gruppe wählen', 'Praktische Reihenfolge auf Grundlage offizieller Global-Regeln. Prüfe vor der Bestätigung die aktuelle Charaktererstellung.')
PAGES['races']['de']['steps'] = [
    {'label': 'Region abstimmen', 'description': 'Nutze dieselbe Region wie deine Freunde für gemeinsame Quests.'},
    {'label': 'Fraktion abstimmen', 'description': 'Wählt Elyos oder Asmodier gemeinsam vor dem Server.'},
    {'label': 'Server bestätigen', 'description': 'Prüfe Namen, Erstellung und einen Ersatz derselben Fraktion.'}
]

def write_sources():
    official = {
        'id': 'global-introduction', 'title': 'About the Game : AION 2-NC',
        'url': 'https://aion2.plaync.com/en-us/about/index', 'kind': 'official',
        'region': 'Global', 'publishedAt': None,
        'version': 'Official Global content API rechecked 2026-10-03: eight class identities and two factions; source archived in class-launch-sources/about-en-source.json'
    }
    overview = {
        'id': 'class-gameplay', 'title': 'AION 2 Classes Explained – PvE & PvP Gameplay',
        'url': 'https://www.youtube.com/watch?v=RXYBucBwRtk', 'kind': 'player',
        'region': 'Mixed', 'publishedAt': None,
        'version': 'Grobs live-server class interpretation; full archived automatic captions read, Global final balance left open by creator'
    }
    video_ids = {'gladiator': 'wyjck6TfJiE', 'ranger': 'UOuiJT9E1xA', 'spiritmaster': 'Xey9go7iYqc'}
    names = {'gladiator': 'Gladiator', 'ranger': 'Ranger', 'spiritmaster': 'Spiritmaster'}
    times = {
        'gladiator': '00:00–01:23 newly leveled simulation and limited points; 01:26–02:49 targeting and ordinary attacks; 03:02–07:27 active/passive priorities, MP and sustain; 08:44–11:14 role-dependent Stigmas and Focusing Block; 12:17–13:09 manual defenses; 17:02–20:59 offensive board and important skill nodes.',
        'ranger': '00:00–02:23 beginner build and progression limits; 02:26–03:46 selecting specializations, Snipe and Deadshot; 05:38–07:01 MP-cost example; 07:18–09:23 Marking Shot, Drilling Dart and crit dependence; 11:50–14:35 passives; 15:23–17:09 explicit Taiwan/Global board differences; 17:09 onward skill-upgrade destinations.',
        'spiritmaster': '00:00–00:47 newly leveled beginner simulation; 02:47–04:40 skills and resource choices; 06:19–08:00 PvE/PvP Stigma differences and ancient summon; 10:16–10:39 Earth→Wind→Fire→Water with Water resource support; 16:54–20:58 cooldown/attack preference and spirit-upgrade routes.'
    }
    for slug in PAGES:
        sources = [official.copy()]
        if slug != 'races':
            video = video_ids[slug]
            title = ('AION 2 Latest Ranger PVE Build for Global | Skills, Stigmas & Daevanion | Beginner Guide | Rotation' if slug == 'ranger' else f'AION 2 {names[slug]} Guide For Skills & Stigmas | Daevanion & Macros Setup | Ultimate Beginners Guide')
            sources += [{
                'id': slug+'-start', 'title': title, 'url': 'https://www.youtube.com/watch?v='+video,
                'kind': 'player', 'region': 'Mixed', 'publishedAt': None,
                'version': 'aLuckyRO early-Global beginner teaching based on a regional live-server character; automatic English captions fetched 2026-10-03; exact client patch and Global tooltip parity not independently established'
            }, overview.copy()]
            if slug == 'ranger':
                sources.append({
                    'id': 'tw-elyos-leveling', 'title': 'AION 2 Elyos Leveling Guide Explained in Under 4 Minutes',
                    'url': 'https://www.youtube.com/watch?v=p5UXLn7XDF8', 'kind': 'player', 'region': 'TW',
                    'publishedAt': None, 'version': 'FRESHY explicitly says Taiwan Ranger at 00:11–00:18; route and speed are not asserted for Global'
                })
            log = f'''# aion 2 {slug}: implementation evidence

Checked: 2026-10-03. Target: Global; source example: regional live-server beginner simulation. Locales: en, ja, es, de. This note adds material without replacing any earlier research.

## Primary verification
- Opened official Global about URL through web tool: JavaScript-only text extraction.
- Independently refetched observed official content API URL; HTTP 200. Archived complete response at ../class-launch-sources/about-en-source.json. Confirmed all eight canonical names, including {names[slug]}.
- Official images reused from src/content/guide-assets.json; no new illustration or purported game screenshot fabricated.

## Player transcript logs
- https://www.youtube.com/watch?v={video}
- Retrieved complete automatic English captions through youtube_transcript_api on 2026-10-03. Additive raw files: research/youtube/{video}.json and .txt. Read the relevant spans, not only the search description.
- Used spans: {times[slug]}
- https://www.youtube.com/watch?v=RXYBucBwRtk : complete existing captions. 00:21–00:39 final Global balance uncertainty; 03:02–04:56 Ranger; 05:00–07:07 Spiritmaster; 11:23–13:29 Gladiator. Power claims excluded from new pages.
'''
            if slug == 'ranger':
                log += '- https://www.youtube.com/watch?v=p5UXLn7XDF8 : 00:11–00:18 explicitly Taiwan Ranger; linked as regional route with no Global speed promise.\n'
            log += '''
## Editorial decisions and remaining gaps
- Published helpful starter choices, manual checks, activity adjustments and troubleshooting; numerical final damage rankings, exact stat thresholds and optimal Global allocations are unsupported and omitted.
- English names in the transcript are not converted into asserted official localized button names. Unclear captions and on-screen-only labels are described by function.
- Daevanion is covered by intended skill/effect and point-cost checks. No unsupported Global coordinate diagram or full point table. Ranger source explicitly distinguishes TW and Global layouts; Spiritmaster sequence is attributed regional example.
- No first-hand gameplay test, automated macro success, safe class ranking, exact Global slot schedule or balance parity claimed. Further exact allocations require current Global tooltip and board evidence.
- All four translations preserve evidence links, section anchors, table dimensions, visuals and next-step placement. Existing classes/builds hub integration is owned by root agent.
'''
        else:
            for id, title, date in [
                ('6abab930eea53f5d6dbcf939', 'Advanced Access Server Matchmaking', '2026-09-29'),
                ('6abd2d50a279104f7d9d5ee2', 'Information on Server Transfer', '2026-09-30')
            ]:
                sources.append({'id': id, 'title': title, 'url': 'https://aion2.plaync.com/en-us/board/notice/view?articleId='+id, 'kind': 'official', 'region': 'Global', 'publishedAt': date, 'version': 'Public Global community API response refetched 2026-10-03 and archived in class-launch-sources; faction/server rules only, no live population inferred'})
            log = '''# aion 2 races: implementation evidence

Checked: 2026-10-03. Target and sources: Global. Locales: en, ja, es, de.

## Sources actually read
- Official about page: https://aion2.plaync.com/en-us/about/index . Web extraction is JavaScript-limited. Refetched the previously observed official content API URL; HTTP 200 and complete response archived at ../class-launch-sources/about-en-source.json.
- Confirmed two factions, Elyos and Asmodians, the separate eight-class roster, Verteron/Altgard world identities and named example locations. Reviewed official locale archives for canonical labels: ja 天族/魔族; es Elios/Asmodianos; de Elyos/Asmodier. No old AION racial skill copied.
- https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939 : refetched public API HTTP 200; full body read and archived at ../class-launch-sources/matchmaking-source.json. Separate faction servers, temporary opposing pairings and cross-faction opponents verified.
- https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2 : refetched public API HTTP 200; archived at ../class-launch-sources/transfer-source.json. October 14 start, same-faction transfer, initial EA-to-EA restriction and cross-server instances verified.

## Decisions and limitations
- One substantial page serves the original races keyword by explaining actual faction decisions, friend coordination, opponents and transfer limits. No new keyword invented.
- No unsupported racial damage bonus, population ranking, universal faction winner or cross-faction/cross-region grouping claim. Official cross-server instance claim does not prove those additional capabilities.
- Independent Global faction-change procedure/price/cooldown remains unverified. The same-faction transfer notice cannot be used to claim faction changes.
- Reusable three-step workflow is an editorial decision aid, not an in-game screenshot. All translations keep canonical faction names, evidence links and page anchors.
'''
        data = {
            'slug': slug, 'keyword': 'aion 2 '+slug, 'checkedAt': '2026-10-03', 'revision': '2026-10-03.1',
            'regions': ['Global'] if slug == 'races' else ['Global', 'KR', 'TW'],
            'related': ['classes', 'builds', 'leveling', 'pvp'] if slug != 'races' else ['server', 'character-creation', 'classes', 'pvp', 'spacetime-rift'],
            'sources': sources
        }
        target = ROOT / 'src/content/article-data' / (slug+'.json')
        if target.exists(): raise RuntimeError(f'Cannot replace {target}')
        target.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        notes = ROOT / 'research/content/2026-10-03' / slug / 'implementation-evidence.md'
        notes.parent.mkdir(parents=True, exist_ok=True)
        if notes.exists(): raise RuntimeError(f'Cannot replace {notes}')
        notes.write_text(log, encoding='utf-8')
        print(slug, '4 locale guides + metadata + dated source log')

page('spiritmaster', 'en', 'AION 2 Spiritmaster Guide: Spirits, Starter Build and Daevanion',
     'Learn an AION 2 Spiritmaster starter setup, a sourced elemental summon sequence, mana management and Daevanion priorities without copying unverified Global nodes.',
     'Build a repeatable summon-and-attack sequence, keep useful spirit effects available, and spend Daevanion points on skills and cooldowns your setup uses.', r'''
Spiritmaster is the elemental summoner on [NC's Global class roster](https://aion2.plaync.com/en-us/about/index). This guide uses [aLuckyRO's early-stage tutorial](https://www.youtube.com/watch?v=Xey9go7iYqc), which models a beginner's limited points with a newly leveled live-server character. Its spirit sequence and Daevanion choices are attributed regional examples; the exact Global skill values and node coordinates are not independently verified here.

<GuideVisual id="topic" />

<h2 id="spiritmaster-playstyle">Playstyle: combine your attacks with spirits</h2>

Spiritmaster adds summon decisions to ranged combat. [Grobs' walkthrough](https://www.youtube.com/watch?v=RXYBucBwRtk) describes elemental spirits with different immediate effects and explains why switching summons matters. Practice the summon effect and your own next attack together rather than treating the class as a pet that performs every job automatically.

This suits players who enjoy preparing pressure and managing several effects. It also means that movement, a missing summon or an interrupted opening can change your next decision. Compare [the class guide](/classes) if you prefer a ranged attacker with fewer summon decisions.

<h2 id="starter-skills">A starter build with limited points</h2>

| Part | Priority in the regional demonstration | Your check |
| --- | --- | --- |
| Spirits | Invest in the elemental summons your sequence uses | Read each summon effect and confirm it is available |
| Main attack | Select an available MP-recovery or resource-support option | Watch MP through repeated summons and attacks |
| Passives | Raise useful damage passives before unrelated options | Check that the passive affects your selected attacks or spirits |
| Stigmas | Consider Summon Ancient Spirit and applicable PvE damage choices | Confirm unlocked slots and the actual equipped skills |

aLuckyRO separates boss-damage choices from fear, seals and other controls he uses for PvP. Choose effects for the encounter instead of copying that distinction as a rule that no control ever matters in PvE. His descriptions sometimes refer to an on-screen skill without a reliable captioned name; this page does not convert those into invented official skill labels or a precise point table.

<h2 id="summon-sequence">A concrete summon sequence to understand</h2>

The tutorial's starter example cycles **Earth → Wind → Fire → Water**. It leaves Water active at the end for the resource support demonstrated on that character. Before copying the sequence, read your current summon effects and check whether the same support exists with your unlocked options.

Practice the four summons manually. Watch the immediate effects, the active spirit, and which cooldowns become unavailable. Then use your own attacks while waiting, rather than pressing summon buttons that cannot fire. The ancient summon is a separate available opportunity in the demonstration; confirm its effect and timing instead of assuming it belongs at every opening.

Do not treat this order as a universal highest-DPS rotation. A useful alternative spirit for an enemy, a different option or a need to move can change the order. Keep reactive protection and control on reachable inputs outside a long repeated attack sequence.

<h2 id="daevanion-build">Daevanion build: summons and cooldown priorities</h2>

In his regional starting model, aLuckyRO prioritizes attack benefits, cooldown reduction and nodes that upgrade the elemental summons. He values repeated summon opportunities more than buying combat speed first for that particular setup. This is a source's priority, not proof that combat speed has no value in every Global Spiritmaster build.

Use a destination-based approach: identify the summon or passive you want to improve, locate it on your own board, compare routes by total point cost, and check the effect after allocating. His demonstration looks for shorter routes to spirit upgrades instead of filling every neighboring stat. The captioned board names are inconsistent, so no supposed Global board coordinates are published here.

Before spending more, write down your points, skill levels and selected options. Follow [the general build guide](/builds) to keep a working setup and change one part at a time. A later regional board or extra skill slot does not establish your Global unlock schedule.

<h2 id="solo-party-and-pvp">Change the setup for solo, bosses and PvP</h2>

Solo pulls need a summon sequence you can operate while keeping resources and moving safely. On a longer boss fight, inspect whether all useful effects actually land and whether you resume attacks after mechanics. If a short target dies before the setup finishes, simplify the opening to the effects you can use in time.

For [PvP](/pvp), review control, defensive access and the first safe summon opportunity separately. The regional walkthrough's control examples do not verify an uninterrupted lock against every Global opponent. Prepare a response when an enemy reaches you before your preferred opening is complete.

<h2 id="spiritmaster-troubleshooting">Troubleshoot one missing effect at a time</h2>

**The final spirit does not help MP:** check that the effect exists in your client and selected option, then observe it without the full attack sequence.

**The summons stop midway:** check cooldown, targeting, current resource and the order manually. A later character's cooldown reduction can make its repetition unavailable to yours.

**The board screenshot does not match:** search for your desired skill upgrade and read its cost. The goal is the useful effect, not the regional drawing.

**The build cannot react:** separate control and defense from repeated damage. Confirm a manual response before adding more buttons to the sequence.

<GuideNext slug="builds" />
''', 'Official AION 2 Spiritmaster class artwork', 'Official Global Spiritmaster artwork. The summon order and board priorities are a named player’s early-stage example, not a verified Global endgame allocation.')

page('spiritmaster', 'ja', 'AION 2 スピリット マスター：精霊・序盤ビルド・Daevanion',
     'AION 2 スピリット マスターの序盤設定、出典付き精霊順、MP管理、Daevanion優先順を整理。未検証のGlobal座標をコピーせずに組み立てます。',
     '召喚と攻撃の流れを作り、有用な精霊効果を使える状態に。使用するスキルや再使用時間にDaevanionポイントを使いましょう。', r'''
スピリット マスターは[NCのGlobalクラス一覧](https://aion2.plaync.com/en-us/about/index)に登場する精霊召喚職です。このガイドは[aLuckyROの序盤教程](https://www.youtube.com/watch?v=Xey9go7iYqc)を使用しています。既存の稼働地域で新しく育てたキャラクターにより、初心者の限られたポイントを再現した例です。精霊順とDaevanion選択は地域版のプレイヤー例であり、Globalの正確な数値や座標を独立検証した配分表ではありません。

<GuideVisual id="topic" />

<h2 id="spiritmaster-playstyle">自分の攻撃と精霊を組み合わせる</h2>

遠距離戦闘に召喚の判断が加わります。[Grobsの解説](https://www.youtube.com/watch?v=RXYBucBwRtk)では精霊ごとの即時効果と、召喚を切り替える意味を紹介しています。ペットに任せるより、召喚効果と自分の次の攻撃を組み合わせて練習しましょう。

準備しながら複数の効果を管理する遊び方に向きます。移動、召喚失敗、開幕の中断で次の判断も変わります。召喚管理の少ない遠距離職を好むなら、[クラスガイド](/classes)で比較してください。

<h2 id="starter-skills">ポイントが少ない時期のビルド</h2>

| 要素 | 地域版実演の優先順 | 自分で確認すること |
| --- | --- | --- |
| 精霊 | 攻撃列に使う属性精霊へ投資 | 召喚効果を読み、使用可能か確認 |
| 主力攻撃 | 使用可能なMP回復・資源支援を選択 | 連続召喚と攻撃中のMPを観察 |
| パッシブ | 関係の薄い特性より有用な火力を優先 | 選択した攻撃や精霊に作用するか確認 |
| Stigma | Summon Ancient Spiritと有効なPvE火力を検討 | 解放枠と実際の装備を確認 |

aLuckyROはボス火力の選択と、PvPで使う恐怖や封印などを区別しています。PvEではすべての妨害が不要という共通ルールにせず、戦闘ごとに選んでください。字幕で正確な名前が分からない画面上のスキルは、公式名称や厳密なポイント表に置き換えていません。

<h2 id="summon-sequence">理解して試せる召喚順</h2>

教程の序盤例は **Earth → Wind → Fire → Water** の順です。最後にWaterを残すのは、そのキャラクターで示した資源支援のためです。コピー前に自分の召喚効果を読み、解放済みの特性で同じ支援が存在するか確認してください。

四つを手動で召喚し、即時効果、現在の精霊、クールダウンを観察します。待ち時間は使用可能な自分の攻撃を使い、使えない召喚を連打しないようにします。実演の古代精霊は別の攻撃機会です。毎回の開幕に入れると決めず、現在の効果とタイミングを調べます。

共通の最大火力ローテーションではありません。敵に有効な精霊、特性、移動の必要によって順番は変わります。状況依存の保護と妨害は長い攻撃列の外に置きましょう。

<h2 id="daevanion-build">召喚と再使用時間を軸にDaevanionを選ぶ</h2>

地域版の序盤モデルでは、作者は攻撃効果、再使用時間短縮、属性精霊の強化ノードを優先します。その設定では戦闘速度を先に買うより、召喚機会を増やす考え方です。すべてのGlobalビルドで速度が無価値という証明ではありません。

強化したい召喚やパッシブを決め、自分の盤で探し、ルート全体のポイント費用を比較して、配分後に効果を確認してください。実演も近隣をすべて埋めるより短い精霊強化ルートを探します。字幕の盤名称は不安定なため、Globalの座標として公開していません。

ポイント、スキルレベル、選択特性を記録します。[ビルド全般のガイド](/builds)で元の設定を残し、一つずつ変えましょう。後期地域版の盤や追加枠でGlobalの解放日程は確定しません。

<h2 id="solo-party-and-pvp">ソロ・ボス・PvPの調整</h2>

ソロではMPと安全な移動を保ちながら操作できる召喚列を作ります。長いボス戦では必要な効果が命中し、ギミック後に攻撃を再開できるか確認します。敵が準備前に倒れる場合は、間に合う効果に開幕を簡略化します。

[PvP](/pvp)では妨害、防御操作、最初に安全に召喚できる機会を別に検討します。地域版の妨害例は、すべてのGlobal相手を連続拘束できる検証ではありません。準備が終わる前に接近された場合の対応も用意してください。

<h2 id="spiritmaster-troubleshooting">一つの不足効果から確認</h2>

**最後の精霊でMPが改善しない：** 自分の説明と特性にその効果があるか読み、攻撃列から切り離して観察します。

**召喚が途中で止まる：** クールダウン、対象、資源、順番を手動で確認します。後期キャラクターの短縮効果で可能な反復は、自分では未使用の場合があります。

**盤の画像が違う：** 欲しいスキル強化を探して費用を読みます。目的は有用な効果です。

**戦闘に対応できない：** 妨害と防御を火力列から分離し、手動で対応できてから操作を追加します。

<GuideNext slug="builds" />
''', 'AION 2 スピリット マスターの公式クラスアート', 'Global公式のスピリット マスター画像です。召喚順と盤の優先順はプレイヤーの序盤例で、検証済みのGlobal最終配分ではありません。')

page('spiritmaster', 'es', 'AION 2 Espiritualista: espíritus, build inicial y Daevanion',
     'Aprende una configuración inicial de Espiritualista de AION 2, una secuencia documentada de invocaciones, gestión de maná y prioridades de Daevanion.',
     'Crea una secuencia repetible de invocaciones y ataques, conserva efectos útiles y mejora habilidades y enfriamientos que tu configuración utiliza.', r'''
El Espiritualista es el invocador elemental de [la lista Global de NC](https://aion2.plaync.com/en-us/about/index). Usamos [el tutorial inicial de aLuckyRO](https://www.youtube.com/watch?v=Xey9go7iYqc), que representa puntos limitados con un personaje recién subido en un servidor regional. Su secuencia y elecciones de Daevanion son ejemplos atribuidos; no se han verificado aquí los valores o coordenadas exactos de Global.

<GuideVisual id="topic" />

<h2 id="spiritmaster-playstyle">Combina tus ataques con los espíritus</h2>

El Espiritualista añade decisiones de invocación al combate a distancia. [Grobs](https://www.youtube.com/watch?v=RXYBucBwRtk) describe efectos inmediatos distintos y la importancia de cambiar espíritus. Practica la invocación junto con tu siguiente ataque en lugar de esperar que una mascota haga todo automáticamente.

Encaja si disfrutas preparando presión y gestionando varios efectos. Moverte, fallar una invocación o perder la apertura puede cambiar la siguiente decisión. Consulta [las clases](/classes) si prefieres menos decisiones de invocación.

<h2 id="starter-skills">Build inicial con puntos limitados</h2>

| Parte | Prioridad del ejemplo regional | Comprobación |
| --- | --- | --- |
| Espíritus | Invierte en las invocaciones de tu secuencia | Lee efectos y confirma disponibilidad |
| Ataque principal | Selecciona recuperación de MP o apoyo de recursos disponible | Observa MP durante invocaciones y ataques |
| Pasivas | Mejora daño útil antes de opciones sin relación | Comprueba que afecta a tus ataques o espíritus |
| Stigmas | Considera Summon Ancient Spirit y opciones de daño PvE | Confirma espacios y habilidades equipadas |

aLuckyRO separa daño a jefes de miedo, sellos y otros controles para PvP. Decide según el encuentro, sin interpretar que ningún control sirve nunca en PvE. Los subtítulos a veces señalan una habilidad en pantalla sin un nombre fiable; no los convertimos en etiquetas oficiales inventadas ni en una tabla exacta de puntos.

<h2 id="summon-sequence">Una secuencia concreta para comprender</h2>

El ejemplo usa **Earth → Wind → Fire → Water**. Deja Water al final por el apoyo de recursos mostrado en ese personaje. Lee tus efectos actuales y confirma que dispones del mismo apoyo con las opciones desbloqueadas.

Practica las cuatro invocaciones manualmente y observa efectos inmediatos, espíritu activo y enfriamientos. Después usa tus ataques mientras esperas. La invocación antigua es una oportunidad aparte: confirma efecto y momento sin asumir que debe abrir cada combate.

El orden no garantiza el mayor DPS universal. Otro espíritu útil, una especialización distinta o movimiento necesario puede modificarlo. Mantén protección y control reactivos fuera de una secuencia repetida larga.

<h2 id="daevanion-build">Daevanion: espíritus y enfriamientos</h2>

El modelo regional prioriza beneficios de ataque, reducción de enfriamientos y mejoras de invocaciones elementales. En esa configuración valora más repetir invocaciones que comprar primero velocidad de combate. No demuestra que la velocidad carezca de valor en cualquier build Global.

Elige una invocación o pasiva como destino, localízala en tu tablero, compara el coste total de las rutas y comprueba el efecto después. El ejemplo busca caminos cortos hacia mejoras de espíritus. Los nombres del tablero en subtítulos son inconsistentes; no publicamos supuestas coordenadas Global.

Registra puntos, niveles y opciones seleccionadas. [La guía de builds](/builds) ayuda a conservar una configuración funcional y cambiar una parte cada vez. Un tablero regional posterior no confirma los desbloqueos de Global.

<h2 id="solo-party-and-pvp">Ajustes para solitario, jefes y PvP</h2>

En solitario necesitas una secuencia compatible con recursos y movimiento seguro. En un jefe largo, comprueba que llegan los efectos y reanudas ataques tras las mecánicas. Si un enemigo muere antes de terminar la preparación, simplifica la apertura.

Para [PvP](/pvp), reconsidera control, acceso a defensa y primera oportunidad de invocar. Los controles regionales no verifican bloqueo continuo contra todos los oponentes de Global. Prepara una respuesta si te alcanzan antes de acabar la apertura.

<h2 id="spiritmaster-troubleshooting">Comprueba un efecto cada vez</h2>

**El último espíritu no ayuda al MP:** confirma el efecto en tu cliente y opción, y obsérvalo separado de los ataques.

**Las invocaciones se interrumpen:** comprueba enfriamiento, objetivo, recursos y orden manualmente. La reducción de un personaje avanzado puede permitir repeticiones que tú todavía no tienes.

**El tablero no coincide:** busca la mejora deseada y lee el coste. El objetivo es el efecto útil.

**No puedes reaccionar:** separa control y defensa del daño repetido; confirma una respuesta manual antes de añadir botones.

<GuideNext slug="builds" />
''', 'Ilustración oficial del Espiritualista de AION 2', 'Ilustración oficial de Global. El orden de invocación y las prioridades del tablero son un ejemplo inicial atribuido a un jugador, no una distribución final verificada.')

page('spiritmaster', 'de', 'AION 2 Beschwörer: Geister, Einstiegsbuild und Daevanion',
     'Lerne einen AION 2 Beschwörer-Einstieg mit belegter Elementarfolge, MP-Versorgung und Daevanion-Prioritäten ohne unbestätigte Global-Koordinaten.',
     'Verbinde Beschwörungen mit eigenen Angriffen, halte nützliche Geistereffekte verfügbar und verbessere genutzte Fertigkeiten und Abklingzeiten.', r'''
Der Beschwörer ist der elementare Geisterrufer in [NCs Global-Klassenliste](https://aion2.plaync.com/en-us/about/index). Dieser Leitfaden nutzt [aLuckyROs Einstiegstutorial](https://www.youtube.com/watch?v=Xey9go7iYqc), das begrenzte Anfängerpunkte mit einem frisch gelevelten Regionalcharakter nachbildet. Folge und Daevanion-Auswahl sind zugeordnete Beispiele; genaue Global-Werte und Knoten wurden hier nicht unabhängig bestätigt.

<GuideVisual id="topic" />

<h2 id="spiritmaster-playstyle">Eigene Angriffe mit Geistern verbinden</h2>

Der Beschwörer ergänzt Fernkampf um Beschwörungsentscheidungen. [Grobs](https://www.youtube.com/watch?v=RXYBucBwRtk) beschreibt unterschiedliche Soforteffekte und den Nutzen von Geisterwechseln. Übe Beschwörung und nächsten eigenen Angriff zusammen, statt alle Aufgaben automatisch einem Begleiter zu überlassen.

Die Klasse passt zu Spielern, die Druck vorbereiten und mehrere Effekte verwalten möchten. Bewegung, eine fehlende Beschwörung oder eine unterbrochene Eröffnung verändern die nächste Entscheidung. Vergleiche [die Klassen](/classes), wenn du weniger Beschwörungsverwaltung möchtest.

<h2 id="starter-skills">Einstiegsbuild mit begrenzten Punkten</h2>

| Teil | Priorität im regionalen Beispiel | Eigene Prüfung |
| --- | --- | --- |
| Geister | In verwendete Elementarbeschwörungen investieren | Effekt lesen und Verfügbarkeit prüfen |
| Hauptangriff | Verfügbare MP-Erholung oder Ressourcenhilfe auswählen | MP über Beschwörungen und Angriffe beobachten |
| Passive | Nützlichen Schaden vor unabhängigen Optionen verbessern | Wirkung auf ausgewählte Angriffe oder Geister prüfen |
| Stigmas | Summon Ancient Spirit und passende PvE-Schadensoptionen erwägen | Freie Plätze und ausgerüstete Fertigkeiten prüfen |

aLuckyRO trennt Boss-Schaden von Angst, Siegeln und anderer PvP-Kontrolle. Wähle nach Kampf, statt jede Kontrolle für PvE auszuschließen. Manche Untertitel beziehen sich ohne verlässlichen Namen auf eine Fertigkeit im Bild; daraus werden hier keine erfundenen offiziellen Namen oder genauen Punktetabellen.

<h2 id="summon-sequence">Eine konkrete Beschwörungsfolge verstehen</h2>

Das Beispiel nutzt **Earth → Wind → Fire → Water**. Water bleibt wegen der gezeigten Ressourcenhilfe am Ende aktiv. Lies deine aktuellen Effekte und prüfe dieselbe Hilfe mit deinen freigeschalteten Optionen.

Übe vier Beschwörungen manuell. Beobachte Soforteffekte, aktiven Geist und Abklingzeiten. Greife danach selbst an, während du wartest. Der alte Geist ist eine eigene verfügbare Gelegenheit; prüfe Effekt und Zeitpunkt statt ihn jeder Eröffnung fest zuzuordnen.

Die Reihenfolge garantiert keinen allgemein höchsten DPS. Ein anderer hilfreicher Geist, eine andere Option oder notwendige Bewegung ändern den Ablauf. Reaktiver Schutz und Kontrolle bleiben außerhalb langer wiederholter Angriffe.

<h2 id="daevanion-build">Daevanion: Beschwörungen und Abklingzeiten</h2>

Das regionale Einstiegsmodell priorisiert Angriffsvorteile, Abklingzeitreduktion und Elementargeist-Verbesserungen. Für diesen Aufbau schätzt der Autor wiederholte Beschwörungen höher ein als zuerst gekauftes Kampftempo. Das beweist nicht, dass Tempo in jedem Global-Build wertlos wäre.

Wähle einen Geist oder eine Passive als Ziel, finde den Knoten im eigenen Board, vergleiche gesamte Wegkosten und kontrolliere den Effekt danach. Das Beispiel sucht kurze Wege zu Geisterverbesserungen. Uneinheitliche Untertitel für Boardnamen werden nicht als vermeintliche Global-Koordinaten veröffentlicht.

Notiere Punkte, Stufen und ausgewählte Optionen. Nutze den [Build-Leitfaden](/builds), behalte einen funktionierenden Aufbau und ändere jeweils einen Teil. Spätere Regionalboards bestätigen keine Global-Freischaltungen.

<h2 id="solo-party-and-pvp">Solo, Bosse und PvP anpassen</h2>

Solo muss deine Folge Ressourcen und sichere Bewegung erlauben. Prüfe bei langen Bossen, ob Effekte treffen und du nach Mechaniken weiter angreifst. Stirbt ein kurzer Gegner vor Ende der Vorbereitung, vereinfache die Eröffnung.

Für [PvP](/pvp) prüfst du Kontrolle, erreichbare Defensiven und die erste sichere Beschwörung neu. Regionale Kontrollen bestätigen keine durchgehende Sperre aller Global-Gegner. Plane eine Reaktion, wenn dich jemand vor der vorbereiteten Eröffnung erreicht.

<h2 id="spiritmaster-troubleshooting">Einen fehlenden Effekt nach dem anderen prüfen</h2>

**Der letzte Geist hilft MP nicht:** Prüfe Effekt und Option im Client und beobachte ihn getrennt von der Angriffsfolge.

**Die Folge stoppt:** Prüfe Abklingzeit, Ziel, Ressourcen und Reihenfolge manuell. Spätere Abklingzeitreduktion ermöglicht Wiederholungen, die dir noch fehlen können.

**Das Boardbild weicht ab:** Suche die gewünschte Verbesserung und lies ihre Kosten. Der nützliche Effekt ist das Ziel.

**Reaktionen fehlen:** Trenne Kontrolle und Schutz vom wiederholten Schaden. Prüfe eine manuelle Antwort vor weiteren Tasten.

<GuideNext slug="builds" />
''', 'Offizielle AION 2 Klassenillustration des Beschwörers', 'Offizielle Global-Illustration. Beschwörungsfolge und Boardprioritäten sind ein zugeordnetes Spielerbeispiel für den Einstieg und keine bestätigte Endgame-Verteilung.')

page('ranger', 'en', 'AION 2 Ranger Guide: Leveling Build, Skills and Daevanion',
     'Start an AION 2 Ranger with MP-aware leveling choices, a Snipe and Deadshot example, and Daevanion priorities that account for Global and Taiwan differences.',
     'Keep ranged attacks sustainable, select the specializations you unlock, and upgrade the skills your current build actually uses.', r'''
Ranger is Global's ranged physical attacker. [NC's introduction](https://aion2.plaync.com/en-us/about/index) confirms the class; [aLuckyRO's Ranger tutorial](https://www.youtube.com/watch?v=UOuiJT9E1xA) supplies the early PvE build example. He explicitly compares Taiwan and Global Daevanion boards. Use the demonstrated effects to make decisions, rather than copying a regional point map.

<GuideVisual id="topic" />

<h2 id="ranger-playstyle">Ranger playstyle and early expectations</h2>

Ranger rewards staying in a useful attack position while reacting to enemies that approach. [Grobs' overview](https://www.youtube.com/watch?v=RXYBucBwRtk) emphasizes sustained ranged attacks and control tools; aLuckyRO emphasizes that an undeveloped character lacks the critical-hit support of his later build. These player descriptions concern different progression and should not become a promise of best-in-class Global damage.

Try normal attacks, movement and a defensive control before committing to a complicated sequence. When a boss makes you move, find the next safe attack position instead of kiting so far that you cannot resume damage. Compare [the class roster](/classes) if you prefer spell casting or spirit management.

<h2 id="leveling-build">A leveling build with useful priorities</h2>

| Priority | Starting job | What to verify |
| --- | --- | --- |
| Resource supply | Select the available MP-recovery option on your ordinary attack | Can you continue attacking through the next pull? |
| Main attacks | Keep a working Snipe and Deadshot relationship where unlocked | Does your selected Snipe option actually reduce Deadshot's cooldown? |
| Frequently used area attack | Consider available MP-cost reduction before spending everything on damage | Does a larger pull empty MP too quickly? |
| Reactive controls | Keep movement and defense reachable; add control for the enemies it affects | Can you interrupt the sequence and create safe distance? |

The tutorial demonstrates that unlocking a specialization does not select it automatically. Open the skill, choose the desired effect, and test it. Its Snipe and Deadshot interaction needs a later unlocked option; if your character lacks it, use the ordinary cooldown instead of expecting the same repetition. English names follow the tutorial, so match the effects in your client.

For the quest route, use [the leveling guide](/leveling). [FRESHY's short Elyos route](https://www.youtube.com/watch?v=p5UXLn7XDF8) explicitly uses a Taiwan Ranger: its side quests and completion time are regional examples, not a guaranteed Global leveling time. Follow your current quest requirements when the route differs.

<h2 id="damage-and-passives">Critical-dependent attacks and passive choices</h2>

aLuckyRO uses Marking Shot to demonstrate a damage opportunity, then explains why a follow-up such as Drilling Dart feels inconsistent before critical hits are dependable. He prioritizes damage-related passives including Focus Eye and Hunter's Resolve in his example. Read the actual trigger before putting a follow-up into an automatic sequence.

A useful test is to use the prerequisite once, watch whether the follow-up becomes available, and repeat without it. If the effect depends on a critical hit, a fixed button order cannot guarantee the same result each time. No universal critical threshold, damage percentage or endgame stat target is established by this guide.

<h2 id="daevanion-build">Daevanion: upgrade a skill for a reason</h2>

The tutorial identifies different Global and Taiwan layouts and values. Its practical objective is to reach useful active and passive upgrades and the specialization those upgrades enable. Start with a skill you repeatedly use, find its node in your own board, compare the point cost of reaching it, and check the current unlock requirement.

His early example values combat speed and important attack or passive upgrades before distant convenience choices. This does not establish a verified Global coordinate path. Do not allocate points solely because a Taiwan screenshot has a highlighted line. Save your working configuration and review the [build checks](/builds) when changing equipment or progression.

<h2 id="solo-party-and-pvp">Solo, party and PvP adjustments</h2>

Solo questing needs sustainable attacks and manageable pulls. In a party, choose effects for the actual encounter and return to a safe firing position after mechanics. A root chosen for a player opponent may contribute little against an enemy immune to that control; verify the target rather than labeling every control universally useless in PvE.

For [PvP](/pvp), reconsider control, distance and reactions separately. Keep situational defenses outside a repeating attack sequence. Learn the useful attack order manually before using the built-in combo controls; another character's attack speed and cooldowns may not match yours.

<h2 id="ranger-troubleshooting">When a copied build fails</h2>

**MP runs out:** check the recovery and cost options you selected, your pull size and how often you repeat the area attack. A missing selection can matter more than another skill level.

**Deadshot does not return as shown:** confirm that the required Snipe option is unlocked and selected, and observe whether the hit produces the cooldown change.

**A follow-up rarely appears:** read its prerequisite and test the trigger manually. Avoid hiding a critical-dependent skill inside a long sequence before you understand its availability.

**The board looks different:** use the skill and effect you want as the destination. The tutorial itself distinguishes the Global board from Taiwan; matching the drawing is not the goal.

<GuideNext slug="leveling" />
''', 'Official AION 2 Ranger class artwork', 'Official Global Ranger artwork. Skill interactions and starting priorities below are attributed player examples, with regional board differences stated explicitly.')

page('ranger', 'ja', 'AION 2 レンジャー：レベリングビルド・スキル・Daevanion',
     'AION 2 レンジャーの序盤を、MP管理、SnipeとDeadshotの関係、Daevanionの優先順から解説。Globalと台湾の違いを区別します。',
     '遠距離攻撃を継続できる状態にし、解放した特性を選択。現在のビルドで使うスキルを強化しましょう。', r'''
レンジャーはGlobalの物理遠距離職です。[NCの紹介](https://aion2.plaync.com/en-us/about/index)で職業を確認し、[aLuckyROのレンジャー教程](https://www.youtube.com/watch?v=UOuiJT9E1xA)から序盤PvEの例を整理しています。動画は台湾とGlobalのDaevanionを明確に比較しています。地域版の配分図をコピーするより、実演の効果を判断材料にしてください。

<GuideVisual id="topic" />

<h2 id="ranger-playstyle">遊び方と序盤の期待値</h2>

レンジャーでは攻撃しやすい位置を保ち、接近する敵へ対応します。[Grobsの解説](https://www.youtube.com/watch?v=RXYBucBwRtk)は継続的な遠距離攻撃と行動妨害を重視し、aLuckyROは育成前のキャラクターに後期ビルドのクリティカル支援がない点を説明しています。異なる育成段階の意見を、Global最強火力の保証として扱わないでください。

複雑な連続操作を作る前に通常攻撃、移動、防御を試しましょう。ボスで移動が必要になったら、攻撃を再開できる安全な位置へ戻ります。魔法や精霊管理の方が好みなら、[クラス一覧](/classes)を比較してください。

<h2 id="leveling-build">役割が分かるレベリングビルド</h2>

| 優先項目 | 序盤の役割 | 確認すること |
| --- | --- | --- |
| MP供給 | 通常攻撃の使用可能なMP回復特性を選ぶ | 次の敵まで攻撃を継続できるか |
| 主力攻撃 | 解放済みならSnipeとDeadshotの関係を作る | 選択したSnipeの特性で再使用時間が減るか |
| よく使う範囲攻撃 | 火力だけに振る前にMP消費軽減を検討 | 敵を増やすとMPがすぐ尽きないか |
| 対応用操作 | 移動と防御を届くキーに置き、効く敵への妨害を選ぶ | 攻撃列を中断して距離を作れるか |

動画では特性の解放と選択が別だと示しています。スキルを開き、欲しい効果を選択して試してください。SnipeとDeadshotの連携には後で解放する特性が必要です。未解放なら通常のクールダウンに合わせます。英語名は動画に従っているので、クライアントの説明で照合しましょう。

クエストの進行は[レベリングガイド](/leveling)へ。[FRESHYの天族向け短いルート解説](https://www.youtube.com/watch?v=p5UXLn7XDF8)は台湾のレンジャーだと明言しています。サブクエストや所要時間は地域版の例で、Globalの確約ではありません。異なる場合は現在のクエスト条件を優先します。

<h2 id="damage-and-passives">クリティカル依存の攻撃とパッシブ</h2>

aLuckyROはMarking Shotで攻撃機会を示し、クリティカルが安定しない段階ではDrilling Dartなどの派生が不安定になる理由を説明します。例ではFocus Eye、Hunter's Resolveなどの火力パッシブを優先しています。派生攻撃を自動列に入れる前に、現在の発動条件を読んでください。

前提スキルを一度使って派生の解放を観察し、前提なしでも試すと比較できます。クリティカル依存なら、固定順のキー入力で毎回同じ結果は保証できません。このガイドでは共通のクリティカル閾値、倍率、最終ステータスを設定していません。

<h2 id="daevanion-build">目的を決めてDaevanionを強化</h2>

動画はGlobalと台湾で配置や数値が異なると説明しています。目的は有用なアクティブ・パッシブの強化と、それで使える特性に到達することです。繰り返し使うスキルを一つ決め、自分の盤でノードを探し、必要ポイントと現在の解放条件を確認しましょう。

作者の序盤例は戦闘速度や重要スキルの強化を優先します。ただしGlobalの検証済み座標ルートではありません。台湾画像の線だけを理由に振らないでください。元の設定を保存し、装備や育成段階が変わったら[ビルド確認項目](/builds)を使います。

<h2 id="solo-party-and-pvp">ソロ・パーティー・PvPの調整</h2>

ソロは継続できる攻撃と無理のない敵数が重要です。パーティーでは実際の戦闘に合う特性を選び、ギミック後に安全な射撃位置へ戻ります。対人用の移動停止が無効な敵には役立たない場合があります。すべての妨害をPvEで無意味と決めつけず対象を確認してください。

[PvP](/pvp)では妨害、距離、反応を別に考えます。状況依存の防御は攻撃列の外へ。ゲーム内連続操作を使う前に手動で覚えましょう。他キャラクターの攻撃速度や再使用時間は自分と異なる場合があります。

<h2 id="ranger-troubleshooting">コピーした設定が動かない場合</h2>

**MPが尽きる：** 回復・消費特性、敵数、範囲攻撃の使用頻度を確認します。特性未選択の修正が追加レベルより先になる場合があります。

**Deadshotが戻らない：** 必要なSnipe特性を解放・選択し、命中でクールダウンが変わるか観察します。

**派生があまり出ない：** 前提を読んで手動で試します。利用条件が分かるまで、クリティカル依存の攻撃を長い列に隠さないでください。

**盤の見た目が違う：** 欲しいスキルと効果を到達先にします。動画もGlobalと台湾を区別しており、絵を一致させることが目的ではありません。

<GuideNext slug="leveling" />
''', 'AION 2 レンジャーの公式クラスアート', 'Global公式のレンジャー画像です。以下の連携と序盤優先順は出典付きのプレイヤー例で、地域ごとの盤の違いを明記しています。')

page('ranger', 'es', 'AION 2 Arquero: build de leveo, habilidades y Daevanion',
     'Empieza un Arquero de AION 2 con gestión de MP, un ejemplo de Snipe y Deadshot y prioridades de Daevanion que distinguen Global de Taiwán.',
     'Mantén ataques a distancia sostenibles, selecciona las especializaciones desbloqueadas y mejora las habilidades que utiliza tu build actual.', r'''
El Arquero es el atacante físico a distancia de Global. [NC confirma la clase](https://aion2.plaync.com/en-us/about/index); [el tutorial de aLuckyRO](https://www.youtube.com/watch?v=UOuiJT9E1xA) aporta el ejemplo inicial de PvE. Compara expresamente los tableros de Taiwán y Global. Decide por los efectos demostrados, sin copiar un mapa regional de puntos.

<GuideVisual id="topic" />

<h2 id="ranger-playstyle">Estilo de juego y expectativas iniciales</h2>

El Arquero requiere una posición útil para atacar y respuestas contra enemigos que se acercan. [Grobs](https://www.youtube.com/watch?v=RXYBucBwRtk) destaca ataques constantes y controles; aLuckyRO advierte que un personaje poco desarrollado carece del apoyo crítico de su build avanzada. Son experiencias en progresiones distintas, sin prometer el mayor daño de Global.

Prueba ataques normales, movimiento y defensa antes de crear una secuencia compleja. Tras una mecánica, busca la siguiente posición segura para disparar. Compara [las clases](/classes) si prefieres lanzar hechizos o gestionar espíritus.

<h2 id="leveling-build">Prioridades para una build de leveo</h2>

| Prioridad | Función inicial | Qué comprobar |
| --- | --- | --- |
| Recursos | Selecciona la recuperación de MP disponible en el ataque normal | ¿Puedes seguir atacando en el siguiente grupo? |
| Ataques principales | Usa la relación Snipe y Deadshot cuando esté desbloqueada | ¿La opción seleccionada reduce el enfriamiento de Deadshot? |
| Área frecuente | Considera menor consumo de MP antes de invertir todo en daño | ¿Los grupos grandes agotan MP demasiado rápido? |
| Respuestas | Deja accesibles movimiento y defensa; usa controles que afecten al objetivo | ¿Puedes interrumpir la secuencia y ganar distancia? |

Desbloquear una especialización no la selecciona automáticamente. Abre la habilidad, elige el efecto y pruébalo. La relación Snipe y Deadshot necesita una opción posterior; sin ella, respeta el enfriamiento normal. Los nombres ingleses siguen el tutorial: identifica las descripciones en tu cliente.

Para misiones, consulta [la guía de leveo](/leveling). [La ruta breve de FRESHY para Elios](https://www.youtube.com/watch?v=p5UXLn7XDF8) usa expresamente un Arquero de Taiwán. Sus misiones secundarias y duración son ejemplos regionales. Sigue los requisitos actuales de Global cuando difieran.

<h2 id="damage-and-passives">Ataques que dependen de críticos y pasivas</h2>

aLuckyRO demuestra una oportunidad con Marking Shot y explica por qué una continuación como Drilling Dart resulta irregular antes de lograr críticos frecuentes. Prioriza pasivas de daño, incluidas Focus Eye y Hunter's Resolve. Lee la condición antes de automatizar una continuación.

Usa el requisito una vez, observa si aparece la continuación y repite sin él. Si depende de un crítico, una secuencia fija no garantiza el mismo resultado. Esta guía no establece un umbral crítico universal, porcentajes de daño ni objetivos finales de estadísticas.

<h2 id="daevanion-build">Mejora Daevanion con un objetivo</h2>

El tutorial distingue disposición y valores de Global y Taiwán. Busca mejoras activas y pasivas útiles, y las especializaciones que permiten. Elige una habilidad frecuente, localiza su nodo en tu tablero, compara el coste del recorrido y comprueba el requisito actual.

El ejemplo inicial valora velocidad de combate y mejoras importantes antes de opciones lejanas. No es una ruta de coordenadas Global verificada. Guarda tu configuración y consulta [las comprobaciones de builds](/builds) al cambiar equipo o progresión.

<h2 id="solo-party-and-pvp">Ajustes para solitario, grupo y PvP</h2>

En solitario, conserva recursos y limita los grupos. En equipo, elige efectos para el encuentro y vuelve a una posición segura tras las mecánicas. Un control para jugadores puede aportar poco contra un enemigo inmune; comprueba el objetivo en vez de descartar todos los controles para PvE.

Para [PvP](/pvp), reconsidera distancia, control y reacciones. Mantén defensas situacionales fuera de la secuencia repetida. Aprende el orden manualmente antes de usar combos integrados; otro personaje puede tener velocidades y enfriamientos distintos.

<h2 id="ranger-troubleshooting">Cuando falla una build copiada</h2>

**MP agotado:** comprueba recuperación, reducción de consumo, tamaño del grupo y frecuencia del ataque de área. Una opción sin seleccionar puede importar más que otro nivel.

**Deadshot no vuelve:** verifica que la opción de Snipe está desbloqueada y seleccionada, y observa si cada impacto modifica el enfriamiento.

**La continuación apenas aparece:** lee el requisito y prueba el desencadenante manualmente antes de esconderlo en una secuencia larga.

**El tablero es diferente:** busca la habilidad y el efecto como destino. El vídeo también distingue Global de Taiwán; reproducir el dibujo no es el objetivo.

<GuideNext slug="leveling" />
''', 'Ilustración oficial del Arquero de AION 2', 'Ilustración oficial del Arquero de Global. Las interacciones y prioridades proceden de ejemplos de jugadores identificados y distinguen los tableros regionales.')

page('ranger', 'de', 'AION 2 Waldläufer: Levelbuild, Fertigkeiten und Daevanion',
     'Beginne einen AION 2 Waldläufer mit MP-Versorgung, einem Beispiel für Snipe und Deadshot und Daevanion-Prioritäten mit klarer Trennung zwischen Global und Taiwan.',
     'Halte Fernangriffe aufrecht, wähle freigeschaltete Spezialisierungen und verbessere die Fertigkeiten, die dein aktueller Build verwendet.', r'''
Der Waldläufer ist Globals physischer Fernkämpfer. [NC bestätigt die Klasse](https://aion2.plaync.com/en-us/about/index); [aLuckyROs Tutorial](https://www.youtube.com/watch?v=UOuiJT9E1xA) liefert das frühe PvE-Beispiel. Es vergleicht Taiwans Daevanion mit Global ausdrücklich. Entscheide anhand der gezeigten Effekte, statt eine regionale Punktekarte zu kopieren.

<GuideVisual id="topic" />

<h2 id="ranger-playstyle">Spielweise und Erwartungen am Anfang</h2>

Der Waldläufer braucht eine gute Angriffsposition und Reaktionen gegen herannahende Gegner. [Grobs](https://www.youtube.com/watch?v=RXYBucBwRtk) betont beständige Fernangriffe und Kontrolle; aLuckyRO beschreibt fehlende Krit-Unterstützung eines wenig entwickelten Charakters. Diese Erfahrungen betreffen unterschiedliche Fortschritte und versprechen keinen höchsten Global-Schaden.

Teste normale Angriffe, Bewegung und Schutz vor einer komplizierten Folge. Suche nach einer Bossmechanik die nächste sichere Schussposition. Vergleiche [die Klassen](/classes), wenn du Zauber oder Geisterverwaltung bevorzugst.

<h2 id="leveling-build">Prioritäten für einen Levelbuild</h2>

| Priorität | Aufgabe am Anfang | Prüfen |
| --- | --- | --- |
| Ressourcen | Verfügbare MP-Erholung des normalen Angriffs auswählen | Kannst du im nächsten Pull weiter angreifen? |
| Hauptangriffe | Freigeschaltetes Zusammenspiel von Snipe und Deadshot nutzen | Verkürzt die ausgewählte Option Deadshots Abklingzeit? |
| Häufiger Flächenangriff | Verfügbare MP-Kostenreduktion vor reinem Schaden erwägen | Leeren größere Pulls MP zu schnell? |
| Reaktionen | Bewegung und Schutz erreichbar halten; passende Kontrolle ergänzen | Kannst du unterbrechen und Abstand gewinnen? |

Eine freigeschaltete Spezialisierung wird nicht automatisch ausgewählt. Öffne die Fertigkeit, wähle den Effekt und teste ihn. Snipe und Deadshot benötigen für die gezeigte Verbindung eine spätere Option. Ohne diese wartest du die normale Abklingzeit ab. Die englischen Namen folgen dem Tutorial; vergleiche die Beschreibungen im Client.

Für Quests nutze den [Levelleitfaden](/leveling). [FRESHYs kurze Elyos-Route](https://www.youtube.com/watch?v=p5UXLn7XDF8) verwendet ausdrücklich einen Taiwan-Waldläufer. Nebenquests und Laufzeit sind regionale Beispiele. Befolge abweichende aktuelle Global-Anforderungen.

<h2 id="damage-and-passives">Krit-abhängige Angriffe und Passive</h2>

aLuckyRO zeigt eine Gelegenheit mit Marking Shot und erklärt, warum eine Folge wie Drilling Dart vor verlässlichen kritischen Treffern unregelmäßig wirkt. Er priorisiert Schadenspassive wie Focus Eye und Hunter's Resolve. Lies die Auslösebedingung vor einer automatischen Folge.

Nutze die Voraussetzung einmal, beobachte die Verfügbarkeit und wiederhole ohne sie. Bei Krit-Abhängigkeit garantiert eine feste Tastensequenz nicht denselben Ausgang. Dieser Leitfaden legt keine allgemeine Krit-Schwelle, Schadensprozente oder endgültige Stat-Ziele fest.

<h2 id="daevanion-build">Daevanion mit einem Ziel verbessern</h2>

Das Tutorial unterscheidet Anordnung und Werte von Global und Taiwan. Suche nützliche aktive und passive Verbesserungen sowie die dadurch möglichen Optionen. Wähle eine häufig genutzte Fertigkeit, finde ihren Knoten im eigenen Board und prüfe Wegkosten und aktuelle Voraussetzung.

Das Einstiegsbeispiel bevorzugt Kampftempo und wichtige Fertigkeitsverbesserungen vor entfernten Zusatzoptionen. Es bestätigt keinen Global-Koordinatenweg. Speichere die funktionierende Konfiguration und nutze die [Build-Prüfung](/builds) bei neuer Ausrüstung oder geändertem Fortschritt.

<h2 id="solo-party-and-pvp">Solo, Gruppe und PvP anpassen</h2>

Solo brauchst du nachhaltige Angriffe und kontrollierte Pulls. In der Gruppe wählst du Effekte für den Kampf und kehrst nach Mechaniken in eine sichere Schussposition zurück. Eine Spielerwurzel hilft gegen einen immunen Gegner möglicherweise wenig; prüfe das Ziel statt jede Kontrolle in PvE auszuschließen.

Für [PvP](/pvp) bewertest du Abstand, Kontrolle und Reaktionen neu. Situationsabhängiger Schutz bleibt außerhalb wiederholter Angriffsfolgen. Lerne den Ablauf vor eingebauten Combos manuell; andere Charaktere haben möglicherweise abweichendes Tempo und Abklingzeiten.

<h2 id="ranger-troubleshooting">Wenn ein kopierter Build scheitert</h2>

**MP ist leer:** Prüfe Erholung, Kostenoptionen, Pullgröße und Flächenangriffe. Eine nicht ausgewählte Option kann wichtiger als eine weitere Stufe sein.

**Deadshot kommt nicht zurück:** Prüfe Freischaltung und Auswahl der Snipe-Option und beobachte den Einfluss eines Treffers auf die Abklingzeit.

**Die Folge erscheint selten:** Lies die Voraussetzung und teste den Auslöser manuell, bevor du ihn in einer langen Sequenz versteckst.

**Das Board sieht anders aus:** Suche gewünschte Fertigkeit und Effekt als Ziel. Auch das Tutorial trennt Global von Taiwan; die Zeichnung nachzubauen ist nicht das Ziel.

<GuideNext slug="leveling" />
''', 'Offizielle AION 2 Klassenillustration des Waldläufers', 'Offizielle Global-Illustration des Waldläufers. Die gezeigten Prioritäten sind zugeordnete Spielerbeispiele; Unterschiede regionaler Boards werden ausdrücklich genannt.')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        PAGES = {slug: PAGES[slug] for slug in sys.argv[1:]}
    write_pages()
    write_sources()
