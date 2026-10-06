"""One-time companion for daily/weekly, beginner and leveling content."""
from author_articles import page, section, write_pages, ROOT, LOCALES
import json

page('daily-weekly-checklist',
 ['AION 2 Daily & Weekly Checklist: Tasks and Rewards', 'AION 2 日課・週課：タスクと報酬', 'AION 2: lista diaria y semanal de tareas y recompensas', 'AION 2: Tages- und Wochenaufgaben mit Belohnungen'],
 ['Duty, dungeon energy, Nightmare, Shugo and weekly crafts in a usable priority order.', 'Duty、ダンジョンエネルギー、Nightmare、Shugo、週ごとの製作を優先順に整理。', 'Duty, energía de mazmorras, Nightmare, Shugo y recetas semanales ordenados por prioridad.', 'Duty, Dungeon-Energie, Nightmare, Shugo und Wochenrezepte nach Priorität.'],
 ['At 45, do your five daily Duty quests on your main, spend Odyle Energy before it caps and use available Nightmare/Shugo entries. Before the weekly reset, finish Ascension Trial and Daily Dungeon allowances and make the two weekly Odyle Energy recipes.', '45からはメインで毎日Dutyを5件、上限前にOdyle Energyを消費し、NightmareとShugoの利用可能回数を使います。週のリセット前にAscension Trial、Daily Dungeon、2種類のOdyle Energy変換を済ませます。', 'Al 45, completa cinco Duty diarias en tu principal, gasta energía Odyle antes del tope y usa entradas Nightmare/Shugo. Antes del reinicio semanal, termina Ascension Trial, Daily Dungeon y las dos recetas de energía Odyle.', 'Erledige auf 45 fünf tägliche Duty-Quests auf deinem Hauptcharakter, verbrauche Odyle-Energie vor dem Limit und nutze Nightmare-/Shugo-Eintritte. Vor dem Wochenreset folgen Ascension Trial, Daily Dungeon und beide Odyle-Energie-Rezepte.'],
 [section('different-counters', ['Your short-session priority list', '短時間のプレイで優先すること', 'Prioridades de una sesión corta', 'Prioritäten für eine kurze Sitzung'], [
 'Use this order: **Duty → energy or tickets near their cap → one next-upgrade activity**. Duty is the daily task; a dungeon with “Daily” in its name is not automatically a daily-reset reward. The Journal → Duty countdown shows the server reset. Use **Reset** on the checklist for a new session.',
 '順序は**Duty → 上限に近いエネルギーやチケット → 次の更新に必要な活動1つ**。Dutyは日課ですが、名前にDailyがあるダンジョンの報酬が毎日リセットされるとは限りません。サーバーのリセットはJournal → Dutyのカウントダウンで確認。新しいセッションはチェックリストの**リセット**を使います。',
 'Sigue **Duty → energía o tickets cerca del tope → una actividad para la próxima mejora**. Duty es diaria; “Daily” en el nombre no implica que las recompensas se reinicien a diario. El contador Journal → Duty muestra el reinicio del servidor. Usa **Reiniciar** en la lista al empezar otra sesión.',
 'Reihenfolge: **Duty → Energie oder Tickets nahe am Limit → eine Aktivität für das nächste Upgrade**. Duty ist täglich; „Daily“ im Dungeon-Namen bedeutet nicht automatisch tägliche Belohnungen. Der Countdown unter Journal → Duty zeigt den Serverreset. Für eine neue Sitzung die Liste **zurücksetzen**.']),
 section('duty-missions', ['Daily tasks: entry, reward and cost', '毎日の活動：入口・報酬・消費', 'Tareas diarias: entrada, premio y coste', 'Tagesaufgaben: Zugang, Belohnung und Kosten'], [
 '''| Priority | Activity and entry | Action and reward | Limit or cost |
| --- | --- | --- | --- |
| 1 | **Journal → Duty**, level 45 | Complete nearby objectives; favor needed growth resources or hidden-cube keys | **5/day per server**, shared by its characters |
| 2 | **Expedition** reward cubes | Claim equipment or Arcana rewards for the next upgrade | Common claims cost **40 Odyle Energy**; energy refills **15 every 3 hours** |
| 3 | **Nightmare**, level 45 | Defeat an available boss tier for progression tokens | Uses its own entry tickets |
| 4 | **Shugo Festival** | Join a minigame for growth and crafting resources | Uses its own keys; spend before their cap |
| Optional | **Map → Exploration → Field Boss** | Join a nearby spawning boss while already in the area | Scheduled encounter; separate from Duty |

Odyle Energy stores up to **560**, or **840 with membership**. The energy counter belongs to the character. An alt does not provide five extra Duty quests on the same server. The old Duty-tab access issue was fixed in the October 5 launch update.''',
 '''| 優先 | 活動と入口 | 操作と報酬 | 制限・消費 |
| --- | --- | --- | --- |
| 1 | **Journal → Duty**、レベル45 | 近くの目標を完了。必要な成長資源や隠しキューブの鍵を優先 | **サーバーごとに1日5件**、キャラクター間で共有 |
| 2 | **Expedition**の報酬キューブ | 次の更新用の装備やArcanaを受領 | 通常の受領は**Odyle Energy 40**。**3時間ごと15**回復 |
| 3 | **Nightmare**、レベル45 | 挑めるボス段階を倒し成長トークンを得る | 専用入場チケット |
| 4 | **Shugo Festival** | ミニゲームで成長・製作資源を得る | 専用の鍵。上限前に使う |
| 任意 | **Map → Exploration → Field Boss** | 近くに出現するボスへ参加 | 出現時刻あり。Dutyとは別 |

Odyle Energy上限は**560**、メンバーシップでは**840**。残量はキャラクター単位です。同サーバーのサブキャラでDutyを5件追加はできません。Duty欄の旧アクセス不具合は10月5日の更新で修正済みです。''',
 '''| Prioridad | Actividad y entrada | Acción y recompensa | Límite o coste |
| --- | --- | --- | --- |
| 1 | **Journal → Duty**, nivel 45 | Objetivos cercanos; prioriza recursos o llaves de cubos ocultos | **5/día por servidor**, compartidas entre personajes |
| 2 | Cubos de **Expedition** | Reclama equipo o Arcana para la próxima mejora | Normalmente **40 Odyle Energy**; recarga **15 cada 3 horas** |
| 3 | **Nightmare**, nivel 45 | Derrota un tier disponible por fichas de progreso | Tickets propios |
| 4 | **Shugo Festival** | Minijuegos para recursos de progreso y fabricación | Llaves propias; gástalas antes del tope |
| Opcional | **Map → Exploration → Field Boss** | Participa en un jefe cercano | Aparición programada; distinto de Duty |

Odyle Energy almacena **560**, o **840 con membresía**, por personaje. Un alternativo no añade cinco Duty en el mismo servidor. El fallo antiguo de acceso a Duty se corrigió el 5 de octubre.''',
 '''| Priorität | Aktivität und Zugang | Aktion und Belohnung | Limit oder Kosten |
| --- | --- | --- | --- |
| 1 | **Journal → Duty**, Stufe 45 | Nahe Ziele erledigen; Wachstumsressourcen oder Würfelschlüssel wählen | **5/Tag je Server**, von Charakteren geteilt |
| 2 | **Expedition**-Belohnungswürfel | Ausrüstung oder Arcana für das nächste Upgrade holen | Üblich: **40 Odyle Energy**; **15 alle 3 Stunden** Nachfüllung |
| 3 | **Nightmare**, Stufe 45 | Verfügbaren Bossrang für Fortschrittstoken besiegen | Eigene Eintrittstickets |
| 4 | **Shugo Festival** | Minispiel für Wachstums- und Handwerksmaterialien | Eigene Schlüssel; vor ihrem Limit nutzen |
| Optional | **Map → Exploration → Field Boss** | Nahen Feldboss besuchen | Geplante Begegnung; getrennt von Duty |

Odyle Energy speichert **560**, mit Mitgliedschaft **840**, je Charakter. Ein Zweitcharakter gibt keine fünf zusätzlichen Duty-Quests auf demselben Server. Das frühere Duty-Zugangsproblem wurde am 5. Oktober behoben.''']),
 section('energy-and-rewards', ['A kill and a reward claim are different', '討伐と報酬受領は別', 'Matar y reclamar son acciones distintas', 'Sieg und Belohnungsanspruch sind verschieden'], [
 'The paid reward **cube** consumes Odyle Energy; defeating the boss does not itself prove the cube was claimed. Open the reward cube before leaving when you want its loot. Selection-box progress also counts claims, so three kills without the relevant claims do not complete a three-claim track. While leveling, prioritize required story clears and avoid buying every temporary cube reward. Energy near its cap should be spent rather than left to waste recovery.',
 'Odyle Energyを消費するのは有料報酬の**キューブ**です。ボス討伐だけでは受領になりません。報酬が必要なら退出前に開けます。選択箱の進行も受領回数を数えるため、3回討伐だけでは3回受領の条件を満たしません。育成中はストーリー必須のクリアを優先し、すべての一時装備キューブを買わないようにします。上限近くのEnergyは回復を無駄にせず使います。',
 'El **cubo** de recompensa consume Odyle Energy; derrotar al jefe no implica reclamarlo. Ábrelo antes de salir si quieres su botín. El progreso del cofre de selección también cuenta reclamaciones: tres muertes sin reclamar no completan una ruta de tres premios. Al subir de nivel, prioriza la historia y evita comprar todos los cubos de equipo temporal. Gasta energía cerca del tope para no perder recarga.',
 'Der Belohnungs**würfel** verbraucht Odyle Energy; der Boss-Sieg bestätigt keinen Anspruch. Öffne ihn vor dem Verlassen, wenn du die Beute brauchst. Auswahlkisten zählen ebenfalls abgeholte Belohnungen: drei Siege ohne Ansprüche erfüllen keinen Drei-Ansprüche-Pfad. Beim Leveln notwendige Story-Abschlüsse priorisieren und nicht jeden Übergangs-Würfel kaufen. Energie nahe am Limit nutzen, damit keine Nachfüllung verloren geht.']),
 section('before-a-reset', ['Weekly tasks and the two Energy recipes', '週の活動と2種類のEnergy配方', 'Tareas semanales y dos recetas de energía', 'Wochenaufgaben und zwei Energierezepte'], [
 '''| Activity | Where | What to finish before reset |
| --- | --- | --- |
| Ascension Trial | Its activity entry | Complete the available allowance at the strongest difficulty you can clear |
| Daily Dungeon | Its activity entry | Use the **weekly** allowance; do not infer its period from the name |
| Odyle Energy crafting | **Substance Morph → Special** | Make the **4-per-character** recipe and assign the **16-per-server** recipe to your main |
| Command scrolls | Capital Command Merchant / Abyss Command Merchant | Buy needed weekly scrolls and complete their listed objectives |
| Supply Requests | Supply Request menu | Turn in affordable surplus materials for Abyss Points; protect needed recipe inputs |

The two morph allowances let your main make **20 Energy items**; an alt has its own four, not another server allotment of sixteen. These recipes consume gathered **Odyle** and Kina. Shop purchases are separate and may require [membership](/monetization).''',
 '''| 活動 | 入口 | リセット前にすること |
| --- | --- | --- |
| Ascension Trial | 活動入口 | クリアできる最も高い難度で利用可能回数を完了 |
| Daily Dungeon | 活動入口 | **週の**利用回数を使う。名前で周期を判断しない |
| Odyle Energy製作 | **Substance Morph → Special** | **キャラごと4個**の配方と、メインで**サーバーごと16個**の配方を作る |
| Commandスクロール | 首都・AbyssのCommand Merchant | 必要な週のスクロールを購入し目標を完了 |
| Supply Requests | 供給依頼メニュー | 安価な余剰素材をAbyss Pointへ。必要な配方素材は残す |

2種類でメインは**Energyアイテム20個**を製作できます。サブには独自の4個があり、サーバー枠16個が増えるわけではありません。採集した**Odyle**とKinaを使います。ショップ購入は別で、[メンバーシップ](/monetization)が必要な場合があります。''',
 '''| Actividad | Entrada | Qué completar antes del reinicio |
| --- | --- | --- |
| Ascension Trial | Entrada de actividad | Agota la cuota en la dificultad más alta que puedas completar |
| Daily Dungeon | Entrada de actividad | Usa la cuota **semanal**; el nombre no define la frecuencia |
| Fabricar Odyle Energy | **Substance Morph → Special** | Haz la receta de **4 por personaje** y reserva la de **16 por servidor** para el principal |
| Pergaminos Command | Command Merchant de capital / Abyss | Compra los semanales necesarios y completa sus objetivos |
| Supply Requests | Menú de solicitudes | Entrega excedentes económicos por Abyss Points; conserva ingredientes necesarios |

Tu principal puede fabricar **20 objetos de energía**. Cada alternativo tiene cuatro propios, no otra cuota de dieciséis. Las recetas consumen **Odyle** recolectado y Kina. Las compras de tienda son distintas y pueden exigir [membresía](/monetization).''',
 '''| Aktivität | Zugang | Vor dem Reset erledigen |
| --- | --- | --- |
| Ascension Trial | Aktivitätseintrag | Kontingent auf der höchsten schaffbaren Schwierigkeit nutzen |
| Daily Dungeon | Aktivitätseintrag | **Wöchentliches** Kontingent nutzen; der Name legt den Zeitraum nicht fest |
| Odyle Energy herstellen | **Substance Morph → Special** | Rezept mit **4 je Charakter** und Rezept mit **16 je Server** auf dem Hauptcharakter nutzen |
| Command-Schriftrollen | Command Merchant in Hauptstadt / Abyss | Benötigte Wochenrollen kaufen und ihre Ziele erfüllen |
| Supply Requests | Lieferanfragen-Menü | Günstigen Überschuss für Abyss Points abgeben; Rezeptzutaten behalten |

Dein Hauptcharakter kann **20 Energiegegenstände** herstellen. Ein Zweitcharakter hat eigene vier, keine weiteren sechzehn. Die Rezepte verbrauchen gesammeltes **Odyle** und Kina. Shopkäufe sind getrennt und können [Mitgliedschaft](/monetization) erfordern.''']),
 section('one-time-and-events', ['Keep one-time progress out of the daily list', '一度きりの成長を日課と分ける', 'Separa el progreso único de la rutina', 'Einmaligen Fortschritt von der Routine trennen'], [
 '**Campaign, green side quests, sealed dungeons, strongholds and feather collection** belong to the one-time cleanup route. Their rewards feed the [equipment route](/gear-progression), but they are not five more daily obligations. Mail gifts, [codes](/code) and [Twitch Drops](/twitch-drops) have their own claim deadlines; a daily reset does not extend them.',
 '**ストーリー、緑のサブクエスト、封印ダンジョン、要塞、羽の収集**は一度きりの整理ルートです。[装備成長](/gear-progression)に役立ちますが追加の日課ではありません。メール、[コード](/code)、[Twitch Drops](/twitch-drops)は独自の期限があり、日課リセットでは延長されません。',
 '**Campaña, misiones verdes, mazmorras selladas, fortalezas y plumas** son progreso único para la [ruta de equipo](/gear-progression), no más obligaciones diarias. Correo, [códigos](/code) y [Twitch Drops](/twitch-drops) tienen fechas propias; el reinicio diario no las amplía.',
 '**Kampagne, grüne Nebenquests, versiegelte Dungeons, Festungen und Federn** sind einmalige Schritte für den [Ausrüstungsweg](/gear-progression), keine weiteren Tagespflichten. Postgeschenke, [Codes](/code) und [Twitch Drops](/twitch-drops) haben eigene Fristen; ein Tagesreset verlängert sie nicht.'])], 'gear-progression',
 [(['Duty first', 'Dutyを先に', 'Primero Duty', 'Duty zuerst'], ['Five quests per day share one server allowance.', '1日5件はサーバーで共有。', 'Cinco misiones diarias comparten cuota del servidor.', 'Fünf Tagesquests teilen ein Serverkontingent.']),
  (['Prevent capped resources', '資源の上限を防ぐ', 'Evita topar recursos', 'Ressourcenlimit vermeiden'], ['Spend near-cap Energy, then available Nightmare tickets and Shugo keys.', '上限近くのEnergy、Nightmareチケット、Shugoの鍵を使う。', 'Gasta energía cerca del tope, tickets Nightmare y llaves Shugo.', 'Energie nahe am Limit, Nightmare-Tickets und Shugo-Schlüssel nutzen.']),
  (['Finish weekly allowances', '週の枠を完了', 'Completa cuotas semanales', 'Wochenkontingente nutzen'], ['Trials, Daily Dungeon and 4 + 16 Energy morphs before reset.', 'リセット前にTrial、Daily Dungeon、Energy変換4 + 16。', 'Trial, Daily Dungeon y transformaciones de energía 4 + 16.', 'Trials, Daily Dungeon und 4 + 16 Energieumwandlungen vor Reset.'])])

page('guide',
 ['AION 2 Beginner Guide: First Session and Key Mistakes', 'AION 2 初心者ガイド：最初の操作と失敗対策', 'AION 2: primeros pasos y errores para principiantes', 'AION 2: Erste Schritte und typische Anfängerfehler'],
 ['A short first-session checklist, essential resource mistakes and where to go after level 45.', '最初のチェックリスト、資源消費の失敗、レベル45以降の行き先。', 'Una lista inicial, errores de recursos y el siguiente paso tras el nivel 45.', 'Eine Startliste, Ressourcenfehler und der nächste Schritt nach Stufe 45.'],
 ['Install the Steam main game, match region/faction/server with friends, set targeting and buffs, then follow Journal → Episode. Fill Ascension gates with regional quests or sealed dungeons. At 45, switch to the equipment route and Duty checklist.', 'Steamの本編を入れ、友人と地域・陣営・サーバーを合わせ、ターゲットとバフを設定してJournal → Episodeへ。昇級ゲージは地域クエストや封印ダンジョンで満たします。45以降は装備ルートとDuty清単へ。', 'Instala el juego principal en Steam, coordina región/facción/servidor, configura objetivos y buffs y sigue Journal → Episode. Completa ascensión con misiones regionales o selladas. Al 45, sigue equipo y Duty.', 'Steam-Hauptspiel installieren, Region/Fraktion/Server abstimmen, Ziele und Buffs einstellen und Journal → Episode folgen. Aufstieg mit Gebietsquests oder versiegelten Dungeons füllen. Auf 45 zum Ausrüstungsweg und Duty wechseln.'],
 [section('start-global', ['First-session checklist', '最初のチェックリスト', 'Lista de la primera sesión', 'Checkliste für die erste Sitzung'], [
 'Install the free-to-play **Steam main game, App 3393110** using the [download guide](/download). Then complete the checklist below before spending upgrade resources.',
 '[ダウンロードガイド](/download)から無料の**Steam本編、App 3393110**を入れます。強化資源を使う前に下の項目を完了します。',
 'Instala el **juego principal gratuito de Steam, App 3393110**, con la [guía de descarga](/download). Completa la lista antes de gastar recursos de mejora.',
 'Installiere das kostenlose **Steam-Hauptspiel, App 3393110**, mit der [Download-Anleitung](/download). Erledige die Liste vor dem Einsatz von Upgrade-Ressourcen.']),
 section('how-to-play-by-region', ['Play on the same server as friends', '友人と同じサーバーで遊ぶ', 'Juega en el mismo servidor que tus amigos', 'Mit Freunden auf demselben Server spielen'], [
 'Match **region → faction → exact server** before creating characters. Regions are **NA West, NA East, Europe, South America and Asia**. Steam and the official PURPLE service share game servers; the launcher alone does not decide whether you can group. Use [server selection](/server) for the current list.',
 '作成前に**地域 → 陣営 → サーバー名**を合わせます。地域は**NA West、NA East、Europe、South America、Asia**。Steamと公式PURPLEはゲームサーバーを共有し、ランチャーだけで組めるかは決まりません。[サーバー選択](/server)で一覧を確認します。',
 'Coordina **región → facción → servidor exacto** antes de crear personajes. Regiones: **NA West, NA East, Europe, South America y Asia**. Steam y PURPLE comparten servidores; el launcher no decide por sí solo si podéis agruparos. Consulta [servidores](/server).',
 'Stimme **Region → Fraktion → genauer Server** vor der Charaktererstellung ab. Regionen: **NA West, NA East, Europe, South America und Asia**. Steam und PURPLE teilen Spielserver; der Launcher allein entscheidet nicht über gemeinsames Spielen. Siehe [Serverwahl](/server).']),
 section('main-story-first', ['Story route and Ascension gates', 'ストーリーと昇級条件', 'Historia y barreras de ascensión', 'Story und Aufstiegsbedingungen'], [
 'Press **J → Episode** and track the next main-story objective. When Ascension is below **100%**, do nearby **Regional quests** or **sealed dungeons** (question-mark map objectives). At 100%, use the Ascension quest teleport and return to Episode. Activate travel points on the route and combine side quests with the same destination. The [leveling guide](/leveling) covers dungeon checkpoints.',
 '**J → Episode**で次のストーリー目標を追います。昇級が**100%**未満なら近くの**Regionalクエスト**や**封印ダンジョン**（地図の疑問符）を完了。100%で昇級クエストの移動を使いEpisodeへ戻ります。道中の移動点を有効にし、同じ目的地のサブクエストをまとめます。ダンジョン節目は[レベル上げ](/leveling)へ。',
 'Pulsa **J → Episode** y sigue la historia. Si ascensión está bajo **100%**, completa **Regional quests** cercanas o **mazmorras selladas** (interrogaciones del mapa). Al 100%, usa el teletransporte de ascensión y vuelve a Episode. Activa puntos de viaje y combina objetivos de la misma zona. Consulta los hitos en [subida de nivel](/leveling).',
 'Mit **J → Episode** das nächste Story-Ziel verfolgen. Unter **100% Aufstieg** nahe **Regional-Quests** oder **versiegelte Dungeons** mit Fragezeichen erledigen. Bei 100% den Quest-Teleport nutzen und zu Episode zurückkehren. Reisepunkte aktivieren und Ziele mit gleichem Weg bündeln. Dungeon-Meilensteine stehen in [Leveln](/leveling).']),
 section('skills-and-gear', ['Four mistakes that consume useful resources', '資源を失う4つの失敗', 'Cuatro errores que consumen recursos útiles', 'Vier Fehler beim Ressourcenverbrauch'], [
 '- **Automatic buffs set to Always:** switch to In Combat so travel does not consume scrolls.\n- **Every dungeon cube claimed while leveling:** Odyle Energy is spent on the reward, not just the story clear.\n- **Green starter belt dismantled:** keep it for the +10-to-blue morph recipe.\n- **Expensive stones in temporary gear:** Manastones and Theostones do not survive equipment transfer.\n\nUse [settings](/settings), [gear progression](/gear-progression) and your [class skill guide](/classes) for the exact next action.',
 '- **自動バフをAlwaysにする**：In Combatにして移動中のスクロール消費を防ぐ。\n- **育成中のキューブを全部受領**：Energyを使うのは報酬で、ストーリークリアとは別。\n- **緑の初期ベルトを抽出**：+10から青へ変換する素材として残す。\n- **一時装備に高価な石**：ManastoneとTheostoneは装備継承で残らない。\n\n具体的な操作は[設定](/settings)、[装備成長](/gear-progression)、[職業スキル](/classes)へ。',
 '- **Buffs automáticos en Always:** usa In Combat para no gastar pergaminos al viajar.\n- **Todos los cubos durante leveo:** la recompensa consume energía, no solo completar la historia.\n- **Desmontar el cinturón verde:** guárdalo para transformarlo de +10 a azul.\n- **Piedras caras en equipo temporal:** Manastones y Theostones no sobreviven a la transferencia.\n\nSigue [ajustes](/settings), [equipo](/gear-progression) y [habilidades de clase](/classes) para los pasos concretos.',
 '- **Automatische Buffs auf Always:** In Combat spart Reiseschriftrollen.\n- **Jeden Würfel beim Leveln abholen:** die Belohnung kostet Energie, nicht allein der Story-Abschluss.\n- **Grünen Startgürtel zerlegen:** für die Umwandlung von +10 zu Blau behalten.\n- **Teure Steine in Übergangsausrüstung:** Manastones und Theostones bleiben beim Transfer nicht erhalten.\n\nDie Schritte stehen in [Einstellungen](/settings), [Ausrüstungsfortschritt](/gear-progression) und [Klassenfertigkeiten](/classes).']),
 section('next-session', ['Your first session at level 45', 'レベル45で最初にすること', 'Primera sesión en el nivel 45', 'Erste Sitzung auf Stufe 45'], [
 'Open **Journal → Duty** for daily quests, then finish remaining story and exploration rewards. Follow the [equipment route](/gear-progression) to upgrade your weapon, belt and missing slots. Use the [daily/weekly checklist](/daily-weekly-checklist) for repeating activities; keep one-time exploration separate. Claim available [codes](/code) and [Twitch Drops](/twitch-drops) before their deadlines.',
 '**Journal → Duty**で日課を開き、残りのストーリーと探索報酬を進めます。[装備ルート](/gear-progression)で武器、ベルト、不足部位を更新。反復活動は[日課・週課](/daily-weekly-checklist)、一度きりの探索とは分けます。[コード](/code)と[Twitch Drops](/twitch-drops)は期限内に受領します。',
 'Abre **Journal → Duty** y termina historia y exploración pendientes. Sigue la [ruta de equipo](/gear-progression) para arma, cinturón y piezas faltantes. La [lista diaria/semanal](/daily-weekly-checklist) organiza actividades repetibles. Reclama [códigos](/code) y [Twitch Drops](/twitch-drops) antes de vencer.',
 '**Journal → Duty** öffnen und offene Story- und Erkundungsbelohnungen erledigen. Der [Ausrüstungsweg](/gear-progression) verbessert Waffe, Gürtel und fehlende Plätze. Die [Tages-/Wochenliste](/daily-weekly-checklist) ordnet Wiederholbares. [Codes](/code) und [Twitch Drops](/twitch-drops) rechtzeitig abholen.'])], 'leveling',
 [(['Set up', '初期設定', 'Prepara', 'Vorbereiten'], ['Match server and set Front of Camera / In Combat buffs.', 'サーバーを合わせ、Front of CameraとIn Combatバフを設定。', 'Coordina servidor y configura Front of Camera y buffs In Combat.', 'Server abstimmen, Front of Camera und In-Combat-Buffs einstellen.']),
  (['Reach 45', '45へ', 'Llega al 45', 'Stufe 45 erreichen'], ['Episode quests; Regional quests and sealed dungeons fill Ascension.', 'Episodeを進め、Regionalと封印ダンジョンで昇級。', 'Episode; Regional y selladas completan ascensión.', 'Episode; Regional-Quests und versiegelte Dungeons füllen Aufstieg.']),
  (['Start progression', '成長を始める', 'Empieza progresión', 'Fortschritt beginnen'], ['Duty, exploration and the equipment route at 45.', '45でDuty、探索、装備ルートへ。', 'Duty, exploración y ruta de equipo al 45.', 'Duty, Erkundung und Ausrüstungsweg auf 45.'])])

page('leveling',
 ['AION 2 Leveling Guide: Episode, Ascension & Level 45', 'AION 2 レベル上げ：Episode・昇級・45到達', 'AION 2: subir de nivel con Episode y ascensión hasta 45', 'AION 2: Mit Episode und Aufstieg bis Stufe 45'],
 ['Follow Episode quests, resolve Ascension gates and reach the first dungeon milestones without wasting rewards.', 'Episode、昇級条件、最初のダンジョン節目を報酬の無駄なく進めます。', 'Sigue Episode, supera barreras de ascensión y alcanza las primeras mazmorras sin gastar premios innecesarios.', 'Episode verfolgen, Aufstiegshürden lösen und die ersten Dungeons ohne unnötige Belohnungskosten erreichen.'],
 ['The level cap is 45. Follow J → Episode; fill blocked Ascension gauges with nearby Regional quests and sealed dungeons, then use the quest teleport at 100%. Combine matching destinations and save optional Odyle cube claims for useful gear.', '上限は45。J → Episodeを追い、昇級で止まったら近くのRegionalと封印ダンジョンでゲージを満たし、100%でクエスト移動。同じ目的地をまとめ、任意のOdyleキューブは役立つ装備に使います。', 'El máximo es 45. Sigue J → Episode; completa ascensión con Regional cercanas y selladas y usa el teletransporte al 100%. Agrupa destinos y reserva cubos Odyle opcionales para equipo útil.', 'Maximalstufe ist 45. J → Episode verfolgen, Aufstieg mit nahen Regional-Quests und versiegelten Dungeons füllen, bei 100% Quest-Teleport nutzen. Gleiche Ziele bündeln und optionale Odyle-Würfel für nützliche Ausrüstung sparen.'],
 [section('global-leveling', ['Main route: Episode → Ascension → Episode', '基本ルート：Episode → 昇級 → Episode', 'Ruta principal: Episode → ascensión → Episode', 'Hauptroute: Episode → Aufstieg → Episode'], [
 '1. Press **J**, select **Episode**, and track the next story quest.\n2. Accept **Regional** quests sharing its destination; turn them in on the same trip.\n3. At an Ascension gate, use current-area Regional quests and nearby **sealed dungeons** until the gauge is **100%**.\n4. Use the Ascension quest **teleport**, complete it and return to Episode.\n5. Activate travel points as you pass; teleport back instead of retracing long routes.',
 '1. **J → Episode**で次のストーリーを追います。\n2. 同じ目的地の**Regional**クエストを受け、同じ移動で報告。\n3. 昇級で止まったら地域クエストと近くの**封印ダンジョン**で**100%**へ。\n4. 昇級クエストの**移動**を使って完了しEpisodeへ戻ります。\n5. 道中の移動点を有効にし、長い道を戻る代わりに転送します。',
 '1. Pulsa **J → Episode** y sigue la siguiente misión.\n2. Acepta **Regional** del mismo destino y entrégalas juntas.\n3. Si ascensión bloquea, haz Regional y **mazmorras selladas** cercanas hasta **100%**.\n4. Usa el **teletransporte** de ascensión, complétala y vuelve a Episode.\n5. Activa puntos de viaje y teletranspórtate en vez de repetir caminos largos.',
 '1. **J → Episode** öffnen und nächste Story-Quest verfolgen.\n2. **Regional-Quests** mit gleichem Ziel annehmen und gemeinsam abgeben.\n3. Aufstieg mit nahen Regional-Quests und **versiegelten Dungeons** bis **100%** füllen.\n4. Den Aufstiegs**teleport** nutzen, Quest abschließen und zu Episode zurück.\n5. Reisepunkte unterwegs aktivieren und lange Rückwege durch Teleport ersetzen.']),
 section('elyos-route', ['Elyos route landmarks', '天族ルートの目印', 'Referencias de la ruta Elyos', 'Wegpunkte der Elyos-Route'], [
 '<GuideFaction faction="elyos">\n\nIn **Verteron**, connect campaign destinations around **Cantas Valley** and **Dawn Legion Base**. Return to the base for turn-ins and use the surrounding Regional objectives to fill Ascension. The same Episode-first order applies; do not switch to an opposite-faction route.\n\n</GuideFaction>',
 '<GuideFaction faction="elyos">\n\n**Verteron**の**Cantas Valley**と**Dawn Legion Base**周辺のストーリーをつなげます。拠点で報告し、周辺のRegional目標で昇級を満たします。Episode優先の順序は同じで、他陣営のルートに切り替えません。\n\n</GuideFaction>',
 '<GuideFaction faction="elyos">\n\nEn **Verteron**, enlaza destinos de **Cantas Valley** y **Dawn Legion Base**. Regresa a la base para entregas y usa Regional cercanas para ascensión. Mantén Episode como prioridad, sin seguir una ruta de la facción opuesta.\n\n</GuideFaction>',
 '<GuideFaction faction="elyos">\n\nIn **Verteron** Kampagnenziele um **Cantas Valley** und **Dawn Legion Base** verbinden. Für Abgaben zur Basis zurück und nahe Regional-Ziele für Aufstieg nutzen. Episode bleibt vorrangig; keine Route der anderen Fraktion übernehmen.\n\n</GuideFaction>']),
 section('asmodian-route', ['Asmodian route landmarks', '魔族ルートの目印', 'Referencias de la ruta Asmodian', 'Wegpunkte der Asmodier-Route'], [
 '<GuideFaction faction="asmodians">\n\nIn **Altgard**, use campaign destinations around **Safe Haven, Moslan Forest and Nornir Assembly**. Combine nearby Regional objectives with those trips. Sealed dungeons are question-mark objectives on the map; [map layers](/map) help separate them from collectibles.\n\n</GuideFaction>',
 '<GuideFaction faction="asmodians">\n\n**Altgard**の**Safe Haven、Moslan Forest、Nornir Assembly**周辺のストーリーを進め、同じ移動のRegionalを組み合わせます。封印ダンジョンは地図の疑問符。[マップレイヤー](/map)で収集物と区別します。\n\n</GuideFaction>',
 '<GuideFaction faction="asmodians">\n\nEn **Altgard**, sigue destinos de **Safe Haven, Moslan Forest y Nornir Assembly** y combina Regional cercanas. Las selladas son interrogaciones del mapa; usa [capas del mapa](/map) para distinguirlas de coleccionables.\n\n</GuideFaction>',
 '<GuideFaction faction="asmodians">\n\nIn **Altgard** die Ziele um **Safe Haven, Moslan Forest und Nornir Assembly** verfolgen und Regional-Ziele bündeln. Versiegelte Dungeons sind Fragezeichen auf der Karte; [Kartenebenen](/map) trennen sie von Sammelobjekten.\n\n</GuideFaction>']),
 section('dungeon-checkpoints', ['Dungeon checkpoints and cube costs', 'ダンジョンの節目とキューブ消費', 'Hitos de mazmorras y coste de cubos', 'Dungeon-Meilensteine und Würfelkosten'], [
 '''| Level | Story / Exploration checkpoint | Next action |
| --- | --- | --- |
| 20 | First Exploration expedition | Complete its story introduction; separate completion from the cube claim |
| 28 | Urugugu Canyon | Progress its story objective and equip useful rewards |
| 35 | Fire Temple | Follow the campaign encounter and update your active skills |
| 45 | Level cap | Open Duty and begin the equipment route |

These are leveling checkpoints, not Conquest-mode equipment requirements. Cube claims commonly cost **40 Odyle Energy**. Save optional claims when the reward will be replaced immediately; spend when it resolves a real equipment block or energy is nearing its cap.''',
 '''| レベル | ストーリー・探索の節目 | 次の操作 |
| --- | --- | --- |
| 20 | 最初の探索遠征 | ストーリー導入を完了。クリアとキューブ受領を分ける |
| 28 | Urugugu Canyon | ストーリー目標を進め有用な報酬を装備 |
| 35 | Fire Temple | ストーリー戦を進めアクティブスキルを更新 |
| 45 | レベル上限 | Dutyを開き装備ルートへ |

これは育成の節目で、Conquestの装備条件ではありません。通常のキューブ受領は**Odyle Energy 40**。すぐ交換する装備の任意受領は節約し、装備で詰まったときやEnergyが上限に近いときに使います。''',
 '''| Nivel | Hito de historia / Exploration | Siguiente acción |
| --- | --- | --- |
| 20 | Primera expedición Exploration | Completa la introducción; separa terminar de reclamar cubo |
| 28 | Urugugu Canyon | Avanza la misión y equipa premios útiles |
| 35 | Fire Temple | Sigue el encuentro y actualiza habilidades activas |
| 45 | Nivel máximo | Abre Duty y sigue la ruta de equipo |

Son hitos de leveo, no requisitos Conquest. Los cubos suelen costar **40 Odyle Energy**. Evita premios que sustituirás enseguida; gasta si resuelven un bloqueo de equipo o la energía se acerca al máximo.''',
 '''| Stufe | Story-/Exploration-Meilenstein | Nächste Aktion |
| --- | --- | --- |
| 20 | Erste Exploration-Expedition | Story-Einführung abschließen; Abschluss und Würfelanspruch trennen |
| 28 | Urugugu Canyon | Story-Ziel erledigen und nützliche Belohnungen anlegen |
| 35 | Fire Temple | Kampagnenkampf verfolgen und aktive Fertigkeiten aktualisieren |
| 45 | Maximalstufe | Duty öffnen und Ausrüstungsweg beginnen |

Das sind Level-Meilensteine, keine Conquest-Anforderungen. Übliche Würfelansprüche kosten **40 Odyle Energy**. Bald ersetzte Belohnungen sparen; bei Ausrüstungshürden oder Energie nahe am Limit ausgeben.''']),
 section('leveling-blockers', ['Three fixes when leveling stalls', '育成が止まったときの3つの対処', 'Tres soluciones cuando se frena el leveo', 'Drei Lösungen bei stockendem Leveln'], [
 '**Ascension short:** nearby Regional quests and sealed dungeons, then teleport at 100%. **Boss damage too low:** equip the latest weapon reward, allocate points to your main attack and use its linked follow-up skills; see your [class guide](/classes). **Too much travel:** activate return points and stack quests at the same destination. After 45, finish the campaign and continue with [gear progression](/gear-progression); reaching the cap alone does not complete the story.',
 '**昇級不足**：近くのRegionalと封印ダンジョンを進め、100%で移動。**ボスへの火力不足**：新しい武器報酬を装備し主力攻撃にポイント、連携スキルを使用。[職業ガイド](/classes)へ。**移動が長い**：帰還点を有効にして同じ目的地のクエストをまとめます。45でも残りのストーリーを完了して[装備成長](/gear-progression)へ進みます。',
 '**Ascensión incompleta:** Regional y selladas cercanas, después teletransporte al 100%. **Poco daño al jefe:** equipa la última arma, asigna puntos al ataque principal y usa sus continuaciones; consulta tu [clase](/classes). **Mucho viaje:** activa retornos y agrupa destinos. Al 45, termina la campaña y continúa con [equipo](/gear-progression); el máximo no completa la historia.',
 '**Aufstieg fehlt:** nahe Regional-Quests und versiegelte Dungeons, bei 100% teleportieren. **Zu wenig Bossschaden:** neueste Waffenbelohnung anlegen, Hauptangriff leveln und Folgefertigkeiten nutzen; siehe [Klasse](/classes). **Lange Wege:** Rückreisepunkte aktivieren und Ziele bündeln. Auf 45 die Kampagne abschließen und zum [Ausrüstungsweg](/gear-progression) wechseln.'])], 'gear-progression',
 [(['Episode', 'Episode', 'Episode', 'Episode'], ['J → Episode is the main-story route.', 'J → Episodeがメインルート。', 'J → Episode es la ruta principal.', 'J → Episode ist die Hauptroute.']),
  (['Ascension', '昇級', 'Ascensión', 'Aufstieg'], ['Regional quests and sealed dungeons fill the gauge to 100%.', 'Regionalと封印ダンジョンで100%へ。', 'Regional y selladas llenan hasta 100%.', 'Regional-Quests und versiegelte Dungeons füllen auf 100%.']),
  (['Return to Episode', 'Episodeへ戻る', 'Vuelve a Episode', 'Zurück zu Episode'], ['Use the Ascension teleport, then resume the story.', '昇級の移動を使いストーリーを再開。', 'Usa el teletransporte de ascensión y sigue la historia.', 'Aufstiegs-Teleport nutzen und Story fortsetzen.'])])

if __name__ == '__main__':
    write_pages()
    checklist = [
      ('duty', ['Complete the five Duty quests on your main', 'メインでDutyを5件完了', 'Completa cinco Duty en el principal', 'Fünf Duty-Quests auf dem Hauptcharakter']),
      ('energy', ['Spend Odyle Energy that is nearing its cap', '上限に近いOdyle Energyを使う', 'Gasta energía Odyle cerca del tope', 'Odyle-Energie nahe am Limit nutzen']),
      ('nightmare', ['Use available Nightmare entries for progression tokens', '利用可能なNightmareで成長トークン', 'Usa entradas Nightmare para fichas', 'Nightmare-Eintritte für Fortschrittstoken nutzen']),
      ('shugo', ['Use Shugo keys before their cap', '上限前にShugoの鍵を使う', 'Usa llaves Shugo antes del tope', 'Shugo-Schlüssel vor dem Limit nutzen']),
      ('weekly', ['Before reset: finish Trial and Daily Dungeon allowances', 'リセット前：TrialとDaily Dungeonの枠を完了', 'Antes del reinicio: Trial y Daily Dungeon', 'Vor Reset: Trial und Daily Dungeon nutzen']),
      ('morph', ['Before reset: make the 4 + 16 Energy recipes', 'リセット前：Energy配方4 + 16', 'Antes del reinicio: recetas de energía 4 + 16', 'Vor Reset: Energierezepte 4 + 16']),
    ]
    starter = [
      ('official-client', ['Install the Steam main game (App 3393110)', 'Steam本編（App 3393110）を入れる', 'Instala el juego Steam (App 3393110)', 'Steam-Hauptspiel (App 3393110) installieren']),
      ('coordinate-server', ['Match region, faction and exact server with friends', '友人と地域・陣営・サーバーを合わせる', 'Coordina región, facción y servidor', 'Region, Fraktion und Server abstimmen']),
      ('choose-class', ['Choose a class and create the character', '職業を選びキャラクターを作成', 'Elige clase y crea personaje', 'Klasse wählen und Charakter erstellen']),
      ('check-controls', ['Set Front of Camera and In Combat buffs', 'Front of CameraとIn Combatバフを設定', 'Configura Front of Camera y buffs In Combat', 'Front of Camera und In-Combat-Buffs einstellen']),
      ('follow-story', ['Track the next quest in J → Episode', 'J → Episodeで次の目標を追う', 'Sigue la misión en J → Episode', 'Nächste Quest in J → Episode verfolgen']),
      ('upgrade-skills', ['Equip the latest weapon and assign main-skill points', '新しい武器を装備し主力スキルにポイント', 'Equipa arma reciente y mejora habilidad principal', 'Neueste Waffe anlegen und Hauptfertigkeit leveln']),
    ]
    for slug, items, titles in [('guide', starter, ['First-session checklist','最初のチェックリスト','Lista inicial','Startcheckliste']), ('daily-weekly-checklist', checklist, ['Session checklist — reset for each new session','セッション用チェックリスト：次回はリセット','Lista de sesión: reinicia para la siguiente','Sitzungsliste — für jede neue Sitzung zurücksetzen'])]:
        for i, locale in enumerate(LOCALES):
            p = ROOT / f'src/content/{locale}/{slug}.json'
            m = json.loads(p.read_text(encoding='utf-8'))
            m['checklist'] = {'title': titles[i], 'items': [{'id': id, 'label': labels[i]} for id, labels in items]}
            p.write_text(json.dumps(m, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
            p = p.with_suffix('.mdx')
            body = p.read_text(encoding='utf-8')
            index = body.index('\n\n<h2', 1)
            body = body[:index]+'\n\n<GuideChecklist />'+body[index:]
            p.write_text(body, encoding='utf-8')
    print('Six core topics rewritten in four languages; session checklists added.')
