"""One-time, manually authored four-language task guides. Do not rerun after later edits."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOCALES = ['en', 'ja', 'es', 'de']
PAGES = {}

def section(id, headings, bodies):
    return (id, headings, bodies)

def page(slug, titles, summaries, answers, sections, next_slug, diagram):
    PAGES[slug] = dict(titles=titles, summaries=summaries, answers=answers, sections=sections, next=next_slug, diagram=diagram)

page('settings',
 ['AION 2 Settings: Controls, Potions & Graphics', 'AION 2 設定：操作・ポーション・画質', 'AION 2: ajustes de controles, pociones y gráficos', 'AION 2: Steuerung, Tränke und Grafik einstellen'],
 ['Menu paths and starting values for targeting, movement, automatic consumables and crowded fights.', 'ターゲット、移動、自動消耗品、大人数戦のメニューと初期設定。', 'Rutas de menú y valores iniciales para objetivos, movimiento, consumibles y combates multitudinarios.', 'Menüpfade und Startwerte für Ziele, Bewegung, automatische Verbrauchsgegenstände und große Kämpfe.'],
 ['Set Target Scanning to Front of Camera. Keep pursuit off for ranged combat; turn it on for melee farming. Set buff auto-use to In Combat, then reduce other-player effects in crowded fights.', 'Target ScanningをFront of Cameraに設定。遠距離戦は追撃OFF、近接の狩りはON。バフ自動使用はIn Combatにし、大人数戦では他プレイヤーのエフェクトを減らします。', 'Selecciona Front of Camera en Target Scanning. Desactiva persecución a distancia y actívala para farmear cuerpo a cuerpo. Usa buffs In Combat y reduce efectos ajenos en grupos grandes.', 'Wähle Front of Camera bei Target Scanning. Verfolgung für Fernkampf aus, für Nahkampf-Farming an. Buffs nur In Combat nutzen und fremde Effekte in großen Kämpfen reduzieren.'],
 [section('control-mode', ['AION 1 or AION 2 controls?', 'AION 1とAION 2の操作の違い', '¿Controles AION 1 o AION 2?', 'AION-1- oder AION-2-Steuerung?'], [
 'Open **Settings → Combat → Controls**. **AION 2 mode** uses mouse movement for the camera and hides the cursor; hold **Alt** to access interface buttons. **AION 1 mode** provides the traditional cursor and target-based controls. Use AION 2 for direct camera aiming, or AION 1 when you want a persistent cursor for selecting targets and party frames.',
 '**Settings → Combat → Controls**を開きます。**AION 2 mode**はマウスでカメラを動かし、カーソルは非表示。**Alt**を押してUIを操作します。**AION 1 mode**は従来型のカーソルとターゲット操作です。カメラで照準を合わせるならAION 2、ターゲットやパーティー欄をカーソルで選ぶならAION 1を選びます。',
 'Abre **Settings → Combat → Controls**. **AION 2 mode** mueve la cámara con el ratón y oculta el cursor; mantén **Alt** para usar la interfaz. **AION 1 mode** ofrece cursor y selección tradicional de objetivos. Elige AION 2 para apuntar con la cámara o AION 1 para seleccionar objetivos y miembros del grupo con el cursor.',
 'Öffne **Settings → Combat → Controls**. Im **AION 2 mode** bewegt die Maus die Kamera; **Alt** zeigt den Cursor für die Oberfläche. **AION 1 mode** bietet die klassische Cursor- und Zielsteuerung. Nutze AION 2 zum Zielen mit der Kamera oder AION 1 für die direkte Auswahl von Zielen und Gruppenfenstern.']),
 section('targeting-and-pursuit', ['Targeting and movement: starting values', 'ターゲットと移動の初期設定', 'Objetivos y movimiento: valores iniciales', 'Ziele und Bewegung: Startwerte'], [
 '''| Menu | Setting | Starting value and purpose |
| --- | --- | --- |
| Combat → Target Scanning | Preferred Search Direction | **Front of Camera**: scan toward the fight instead of selecting an enemy behind you |
| Combat → Controls | Pursue Targets with Skill Activation | **Off** for ranged combat and positioning-sensitive bosses; **On** for melee mob farming |
| Combat → Controls | Auto Target upon Skill Use | **On** for ordinary PvE; **Off** for deliberate PvP target selection |
| Combat → Controls | Skill Queue | **On**: queue the next skill during the current animation |
| Combat → Movement | Interact after Auto Move | **On**: interact on arrival at a quest NPC or object |
| Combat → Movement | Auto Sprint | **On** for quest travel |''',
 '''| メニュー | 項目 | 初期値と用途 |
| --- | --- | --- |
| Combat → Target Scanning | Preferred Search Direction | **Front of Camera**：背後ではなく戦闘方向の敵を選ぶ |
| Combat → Controls | Pursue Targets with Skill Activation | 遠距離戦や位置取りが重要なボスは**OFF**、近接の通常狩りは**ON** |
| Combat → Controls | Auto Target upon Skill Use | 通常PvEは**ON**、PvPで対象を指定するなら**OFF** |
| Combat → Controls | Skill Queue | **ON**：現在の動作中に次のスキルを予約 |
| Combat → Movement | Interact after Auto Move | **ON**：クエストNPCや対象に到着すると操作 |
| Combat → Movement | Auto Sprint | クエスト移動では**ON** |''',
 '''| Menú | Opción | Valor inicial y función |
| --- | --- | --- |
| Combat → Target Scanning | Preferred Search Direction | **Front of Camera**: selecciona hacia la pelea, no detrás de ti |
| Combat → Controls | Pursue Targets with Skill Activation | **Off** a distancia o contra jefes que exigen posición; **On** para farmear cuerpo a cuerpo |
| Combat → Controls | Auto Target upon Skill Use | **On** para PvE normal; **Off** para elegir objetivos en PvP |
| Combat → Controls | Skill Queue | **On**: prepara la siguiente habilidad durante la animación actual |
| Combat → Movement | Interact after Auto Move | **On**: interactúa al llegar al NPC u objeto de misión |
| Combat → Movement | Auto Sprint | **On** para viajar entre misiones |''',
 '''| Menü | Option | Startwert und Zweck |
| --- | --- | --- |
| Combat → Target Scanning | Preferred Search Direction | **Front of Camera**: Ziele vor der Kamera statt hinter dir wählen |
| Combat → Controls | Pursue Targets with Skill Activation | **Off** für Fernkampf und Bosse mit wichtiger Positionierung; **On** für Nahkampf-Farming |
| Combat → Controls | Auto Target upon Skill Use | **On** für normales PvE; **Off** für gezielte Auswahl im PvP |
| Combat → Controls | Skill Queue | **On**: nächste Fertigkeit während der aktuellen Animation einreihen |
| Combat → Movement | Interact after Auto Move | **On**: am Quest-NPC oder Objekt direkt interagieren |
| Combat → Movement | Auto Sprint | **On** für Wege zwischen Quests |''']),
 section('potions-and-loot', ['Potion thresholds and automatic buffs', 'ポーション条件と自動バフ', 'Umbrales de pociones y buffs automáticos', 'Trankschwellen und automatische Buffs'], [
 '**Combat → Auto Use:** start HP potion auto-use at **70%** while learning encounters. For low-risk farming, **40–50%** saves potions but leaves less room for burst damage. These are starting recommendations, not different potion effects. Set **Buff Auto Use Conditions → In Combat** so scrolls and buffs are not consumed while standing in town. Keep a manual potion button accessible. In **Combat → Looting**, configure collection rules separately from equipment extraction; extraction consumes the selected item.',
 '**Combat → Auto Use**：戦闘を覚える間はHPポーションを**70%**で自動使用。危険の少ない狩りは**40～50%**で節約できますが、瞬間ダメージへの余裕は減ります。効果の違いではなく初期設定の提案です。**Buff Auto Use Conditions → In Combat**にして街でのバフやスクロール消費を防ぎます。手動ポーションのキーも残します。**Combat → Looting**の収集設定と装備抽出は別で、抽出は対象装備を消費します。',
 '**Combat → Auto Use:** empieza con pociones de HP al **70%** mientras aprendes encuentros. Para farmear con poco riesgo, **40–50%** ahorra pociones pero reduce el margen frente a ráfagas. Son recomendaciones iniciales. Selecciona **Buff Auto Use Conditions → In Combat** para evitar gastar buffs y pergaminos en la ciudad. Conserva una tecla manual de poción. Las reglas de **Combat → Looting** son distintas de extracción, que consume el equipo seleccionado.',
 '**Combat → Auto Use:** beginne beim Lernen von Kämpfen mit HP-Tränken bei **70%**. **40–50%** spart beim risikoarmen Farming Tränke, lässt aber weniger Spielraum gegen Schadensspitzen. Das sind Startempfehlungen. Wähle **Buff Auto Use Conditions → In Combat**, damit Buffs und Schriftrollen nicht in der Stadt verbraucht werden. Behalte eine manuelle Tranktaste. **Combat → Looting** regelt Beute; Ausrüstungsextraktion verbraucht dagegen den gewählten Gegenstand.']),
 section('keybinds-and-hud', ['Buttons to keep outside your macro', 'マクロとは別に残すキー', 'Teclas que deben quedar fuera de la macro', 'Tasten außerhalb des Makros'], [
 'Bind **dodge/block, interrupt, potion, healing and cleanse** directly. Put repeatable damage skills in the [built-in macro](/macro-guide). In **HUD Edit**, place HP/MP near your skill bar and keep party frames visible for healing. **Info Display → Common** controls nameplates; hiding your own nameplate reduces central clutter, but retain the HUD health bar.',
 '**回避・防御、中断、ポーション、回復、解除**は直接キーに割り当てます。繰り返す攻撃は[ゲーム内マクロ](/macro-guide)へ。**HUD Edit**でHP/MPをスキル欄の近くに置き、回復用のパーティー欄を見える位置にします。**Info Display → Common**でネームプレートを調整。自分の表示を消してもHUDのHP欄は残します。',
 'Asigna directamente **esquiva/bloqueo, interrupción, poción, curación y limpieza**. Pon ataques repetitivos en la [macro integrada](/macro-guide). En **HUD Edit**, coloca HP/MP cerca de habilidades y deja visibles los marcos del grupo. **Info Display → Common** controla nombres; puedes ocultar el tuyo para despejar el centro sin quitar la barra de salud del HUD.',
 'Belege **Ausweichen/Blocken, Unterbrechen, Trank, Heilung und Reinigung** direkt. Wiederholbare Angriffe gehören ins [eingebaute Makro](/macro-guide). Platziere HP/MP in **HUD Edit** nahe der Fertigkeitsleiste und lasse Gruppenfenster sichtbar. **Info Display → Common** regelt Namensanzeigen; deine eigene kannst du ausblenden, die HUD-Gesundheitsleiste bleibt.']),
 section('graphics-and-crowds', ['Crowded-fight graphics preset', '大人数戦の画質設定', 'Gráficos para combates multitudinarios', 'Grafik für große Kämpfe'], [
 '''| Option | Starting value | Result |
| --- | --- | --- |
| Identical Player Appearance | **On** | Simplifies other characters' cosmetic models |
| Other Players' Effects | **Self / Party** | Reduces effects covering enemy warnings |
| Shadows | **Low** | Reduces shadow detail and rendering load |
| Reflections | **Low** | Reduces reflection detail and rendering load |
| Upscaling | Supported **DLSS / FSR** option | Trades native rendering for upscaling; availability depends on GPU |

Keep encounter warnings visible. Lower reflections and shadows before hiding information needed to dodge.''',
 '''| 項目 | 初期値 | 結果 |
| --- | --- | --- |
| Identical Player Appearance | **ON** | 他キャラクターの外見モデルを簡略化 |
| Other Players' Effects | **Self / Party** | 敵の予告を覆うエフェクトを減らす |
| Shadows | **Low** | 影の細部と描画負荷を減らす |
| Reflections | **Low** | 反射の細部と描画負荷を減らす |
| Upscaling | 対応する**DLSS / FSR** | ネイティブ描画をアップスケーリングに置換。GPUにより対応が異なる |

敵の攻撃予告は見える状態を保ちます。回避に必要な表示を消す前に、反射と影を下げます。''',
 '''| Opción | Valor inicial | Resultado |
| --- | --- | --- |
| Identical Player Appearance | **On** | Simplifica apariencias de otros personajes |
| Other Players' Effects | **Self / Party** | Reduce efectos que tapan avisos enemigos |
| Shadows | **Low** | Reduce detalle y carga de sombras |
| Reflections | **Low** | Reduce detalle y carga de reflejos |
| Upscaling | **DLSS / FSR** compatible | Sustituye renderizado nativo por reescalado; depende de la GPU |

Mantén visibles los avisos del encuentro. Baja sombras y reflejos antes de ocultar información necesaria para esquivar.''',
 '''| Option | Startwert | Wirkung |
| --- | --- | --- |
| Identical Player Appearance | **On** | Vereinfacht kosmetische Modelle anderer Spieler |
| Other Players' Effects | **Self / Party** | Weniger Effekte über gegnerischen Warnungen |
| Shadows | **Low** | Weniger Schattendetails und Renderlast |
| Reflections | **Low** | Weniger Reflexionsdetails und Renderlast |
| Upscaling | Unterstütztes **DLSS / FSR** | Ersetzt natives Rendering durch Upscaling; GPU-Unterstützung erforderlich |

Kampfwarnungen sichtbar lassen. Reduziere zuerst Schatten und Reflexionen, bevor du Informationen zum Ausweichen ausblendest.''']),
 section('test-your-settings', ['Fix three common control problems', 'よくある操作の問題3つ', 'Resuelve tres problemas de control', 'Drei Steuerungsprobleme lösen'], [
 '**Running into enemies when casting:** disable Pursue Targets with Skill Activation. **Selecting enemies behind you:** use Front of Camera. **Buffs disappearing during travel:** change Buff Auto Use Conditions from Always to In Combat.',
 '**詠唱時に敵へ走る**：Pursue Targets with Skill ActivationをOFF。**背後の敵を選ぶ**：Front of Cameraへ。**移動中にバフを消費**：Buff Auto Use ConditionsをAlwaysからIn Combatへ。',
 '**Corres hacia enemigos al lanzar:** desactiva Pursue Targets with Skill Activation. **Seleccionas enemigos detrás:** usa Front of Camera. **Gastas buffs al viajar:** cambia Buff Auto Use Conditions de Always a In Combat.',
 '**Beim Wirken zu Gegnern laufen:** Pursue Targets with Skill Activation ausschalten. **Ziele hinter dir auswählen:** Front of Camera nutzen. **Buffs auf Reisen verbrauchen:** Buff Auto Use Conditions von Always auf In Combat ändern.'])], 'guide',
 [(['Aim forward', '前方を狙う', 'Apunta al frente', 'Nach vorn zielen'], ['Front of Camera selects in the camera direction.', 'Front of Cameraでカメラ方向を検索。', 'Front of Camera busca hacia la cámara.', 'Front of Camera sucht in Kamerarichtung.']),
  (['Control movement', '移動を制御', 'Controla movimiento', 'Bewegung steuern'], ['Pursuit off keeps ranged casts from moving you into enemies.', '追撃OFFで遠距離スキル時の接近を防ぐ。', 'Persecución desactivada evita acercarte al lanzar a distancia.', 'Verfolgung aus verhindert Annäherung bei Fernangriffen.']),
  (['Save consumables', '消耗品を節約', 'Ahorra consumibles', 'Verbrauch sparen'], ['In Combat stops automatic buffs while traveling.', 'In Combatで移動中の自動バフ消費を防ぐ。', 'In Combat evita buffs automáticos al viajar.', 'In Combat verhindert automatische Reise-Buffs.'])])

page('crafting',
 ['AION 2 Crafting: Professions, Recipes & Materials', 'AION 2 製作：職業・配方・素材', 'AION 2: oficios, recetas y materiales', 'AION 2: Handwerke, Rezepte und Materialien'],
 ['Choose a profession and follow two exact starter recipes into the Orichalcum equipment chain.', '製作職業を選び、2つの初期配方からOrichalcum装備の連鎖へ進みます。', 'Elige un oficio y sigue dos recetas iniciales hasta la cadena de equipo Orichalcum.', 'Wähle ein Handwerk und folge zwei konkreten Startrezepten in die Orichalcum-Ausrüstungskette.'],
 ['Blacksmithing makes melee weapons and Guards; Handicrafting makes bows, staffs and jewelry. One Orichalcum Longsword needs 3 Ingots, 5 Refining Stones and 2 Odyle; each Ingot needs 2 Ore and 1 Solvent.', 'Blacksmithingは近接武器とGuard、Handicraftingは弓・杖・装飾品を製作。Orichalcum LongswordはIngot 3、Refining Stone 5、Odyle 2。Ingot 1つにはOre 2とSolvent 1が必要です。', 'Blacksmithing fabrica armas cuerpo a cuerpo y Guards; Handicrafting, arcos, bastones y joyas. Una Orichalcum Longsword requiere 3 lingotes, 5 Refining Stones y 2 Odyle; cada lingote, 2 menas y 1 solvente.', 'Blacksmithing stellt Nahkampfwaffen und Guards her; Handicrafting Bögen, Stäbe und Schmuck. Ein Orichalcum Longsword braucht 3 Barren, 5 Refining Stones und 2 Odyle; jeder Barren braucht 2 Erz und 1 Lösungsmittel.'],
 [section('start-with-a-recipe', ['Which profession makes your equipment?', '装備を作る製作職業', '¿Qué oficio fabrica tu equipo?', 'Welches Handwerk stellt deine Ausrüstung her?'], [
 '''| Profession | Products | First target |
| --- | --- | --- |
| Blacksmithing | Longswords, greatswords, daggers, maces, Guards | Melee weapon or Guard |
| Armorsmithing | Armor pieces | A specific armor replacement |
| Handicrafting | Bows, staffs, necklaces, earrings, rings | Bow/staff or offensive jewelry |
| Alchemy | Spellbooks, orbs, potions and scrolls | Caster weapon or consumables |
| Cooking | Food | Combat food |

For a bow or staff character, Handicrafting covers both the weapon and jewelry. For a sword or mace character, Blacksmithing covers the weapon; jewelry requires Handicrafting.''',
 '''| 職業 | 製作品 | 最初の目標 |
| --- | --- | --- |
| Blacksmithing | 長剣、大剣、短剣、メイス、Guard | 近接武器またはGuard |
| Armorsmithing | 防具 | 必要な防具の更新 |
| Handicrafting | 弓、杖、ネックレス、イヤリング、指輪 | 弓・杖または攻撃用装飾品 |
| Alchemy | 魔法書、オーブ、ポーション、スクロール | 魔法武器または消耗品 |
| Cooking | 食料 | 戦闘用の料理 |

弓・杖ならHandicraftingで武器と装飾品を作れます。長剣・メイスの武器はBlacksmithing、装飾品はHandicraftingです。''',
 '''| Oficio | Productos | Primer objetivo |
| --- | --- | --- |
| Blacksmithing | Espadas, mandobles, dagas, mazas y Guards | Arma cuerpo a cuerpo o Guard |
| Armorsmithing | Armaduras | Sustituir una pieza concreta |
| Handicrafting | Arcos, bastones, collares, pendientes y anillos | Arco/bastón o joyería ofensiva |
| Alchemy | Libros, orbes, pociones y pergaminos | Arma mágica o consumibles |
| Cooking | Comida | Alimentos de combate |

Handicrafting cubre arma y joyería para arcos y bastones. Para espadas o mazas, Blacksmithing fabrica el arma y Handicrafting la joyería.''',
 '''| Handwerk | Produkte | Erstes Ziel |
| --- | --- | --- |
| Blacksmithing | Langschwerter, Großschwerter, Dolche, Streitkolben, Guards | Nahkampfwaffe oder Guard |
| Armorsmithing | Rüstungsteile | Ein bestimmtes Rüstungsteil ersetzen |
| Handicrafting | Bögen, Stäbe, Halsketten, Ohrringe, Ringe | Bogen/Stab oder offensiver Schmuck |
| Alchemy | Zauberbücher, Kugeln, Tränke, Schriftrollen | Magiewaffe oder Verbrauchsgegenstände |
| Cooking | Nahrung | Kampfnahrung |

Für Bogen und Stab deckt Handicrafting Waffe und Schmuck ab. Für Schwert oder Streitkolben kommt die Waffe aus Blacksmithing, Schmuck aus Handicrafting.''']),
 section('different-material-systems', ['Get the correct ingredients', '必要な素材の入手先', 'Consigue los ingredientes correctos', 'Die richtigen Zutaten beschaffen'], [
 '''| Material | Where to get it |
| --- | --- |
| Orichalcum Ore and its higher grades | Gather ore nodes; use [resource map filters](/map#gathering-map-filters) |
| Odyle | Extract Odyle nodes, including those after Conquest bosses; this is a material, not the Energy counter |
| Orichalcum Solvent (Bound) | Crafting-material merchant |
| Refining Stone / Expert's Refining Stone | Monster drops while questing or farming pets |
| Higher-grade refining stones | Shugo rewards and dungeon rewards |

**Essence Extraction** gathers nodes. **Item Extraction** consumes equipment. **Substance Morph** converts materials or equipment through its own recipes; it does not level the same crafting profession.''',
 '''| 素材 | 入手先 |
| --- | --- |
| Orichalcum Oreと上位品質 | 鉱石ノードを採集。[資源マップ](/map#gathering-map-filters)を使用 |
| Odyle | 征服ボス後を含むOdyleノードから抽出。Energyの残量とは別の素材 |
| Orichalcum Solvent (Bound) | 製作素材の商人 |
| Refining Stone / Expert’s Refining Stone | クエストやペット集め中のモンスタードロップ |
| 上位の精錬石 | Shugoやダンジョンの報酬 |

**Essence Extraction**はノード採集、**Item Extraction**は装備を消費する抽出です。**Substance Morph**は専用配方で素材や装備を変換し、製作職業と同じレベルを上げる操作ではありません。''',
 '''| Material | Dónde obtenerlo |
| --- | --- |
| Orichalcum Ore y calidades superiores | Nodos de mena; usa los [filtros del mapa](/map#gathering-map-filters) |
| Odyle | Nodos Odyle, incluidos los de después de jefes Conquest; es material, no el contador de energía |
| Orichalcum Solvent (Bound) | Comerciante de materiales de fabricación |
| Refining Stone / Expert’s Refining Stone | Monstruos al hacer misiones o conseguir mascotas |
| Piedras de refinado superiores | Recompensas Shugo y de mazmorras |

**Essence Extraction** recolecta nodos; **Item Extraction** consume equipo. **Substance Morph** transforma materiales o equipo mediante sus propias recetas y no sube el mismo oficio.''',
 '''| Material | Fundort |
| --- | --- |
| Orichalcum Ore und höhere Qualitäten | Erzvorkommen; nutze [Ressourcenfilter](/map#gathering-map-filters) |
| Odyle | Odyle-Vorkommen, auch nach Conquest-Bossen; Material und Energiezähler sind verschieden |
| Orichalcum Solvent (Bound) | Händler für Handwerksmaterialien |
| Refining Stone / Expert’s Refining Stone | Monsterbeute beim Questen oder Begleitersammeln |
| Höhere Veredelungssteine | Shugo- und Dungeon-Belohnungen |

**Essence Extraction** sammelt Vorkommen; **Item Extraction** verbraucht Ausrüstung. **Substance Morph** wandelt Materialien oder Ausrüstung mit eigenen Rezepten um und levelt nicht dasselbe Handwerk.''']),
 section('prepare-a-batch', ['Worked recipe: one Orichalcum Longsword', '実例：Orichalcum Longswordを1本作る', 'Receta completa: una Orichalcum Longsword', 'Rezeptbeispiel: ein Orichalcum Longsword'], [
 '''Open **Crafting → Blacksmithing**.

| Recipe | Crafting requirement | Ingredients for one attempt |
| --- | --- | --- |
| Orichalcum Ingot | Novice **1** | **2 Orichalcum Ore + 1 Orichalcum Solvent (Bound)** |
| Orichalcum Longsword | Novice **3** | **3 Orichalcum Ingots + 5 Refining Stones + 2 Odyle (Bound)** |

Starting from raw ore, one sword attempt therefore needs **6 Ore, 3 Solvent, 5 Refining Stones and 2 Odyle**, assuming all three Ingot crafts succeed. For ten sword attempts, budget **60 Ore, 30 Solvent, 50 Stones and 20 Odyle** before failed crafts or further tiers. Craft in a safe place: taking a hit can interrupt crafting and consume its materials.''',
 '''**Crafting → Blacksmithing**を開きます。

| 配方 | 製作条件 | 1回分の素材 |
| --- | --- | --- |
| Orichalcum Ingot | Novice **1** | **Orichalcum Ore 2 + Orichalcum Solvent (Bound) 1** |
| Orichalcum Longsword | Novice **3** | **Orichalcum Ingot 3 + Refining Stone 5 + Odyle (Bound) 2** |

Ingotの3回が全て成功すれば、剣1回分は原料から**Ore 6、Solvent 3、Refining Stone 5、Odyle 2**です。剣10回分は**Ore 60、Solvent 30、石50、Odyle 20**。失敗分や次の段階は別に必要です。攻撃を受けると製作が中断して素材を消費するため、安全な場所で作ります。''',
 '''Abre **Crafting → Blacksmithing**.

| Receta | Requisito | Ingredientes por intento |
| --- | --- | --- |
| Orichalcum Ingot | Novice **1** | **2 Orichalcum Ore + 1 Orichalcum Solvent (Bound)** |
| Orichalcum Longsword | Novice **3** | **3 Orichalcum Ingots + 5 Refining Stones + 2 Odyle (Bound)** |

Desde la mena, un intento de espada necesita **6 Ore, 3 Solvent, 5 Refining Stones y 2 Odyle**, si los tres lingotes salen bien. Diez intentos requieren **60 Ore, 30 Solvent, 50 piedras y 20 Odyle**, sin contar fallos ni tiers superiores. Fabrica en un lugar seguro: recibir un golpe puede interrumpir el proceso y consumir materiales.''',
 '''Öffne **Crafting → Blacksmithing**.

| Rezept | Voraussetzung | Zutaten je Versuch |
| --- | --- | --- |
| Orichalcum Ingot | Novice **1** | **2 Orichalcum Ore + 1 Orichalcum Solvent (Bound)** |
| Orichalcum Longsword | Novice **3** | **3 Orichalcum Ingots + 5 Refining Stones + 2 Odyle (Bound)** |

Aus Rohmaterial braucht ein Schwertversuch **6 Ore, 3 Solvent, 5 Refining Stones und 2 Odyle**, sofern alle drei Barren gelingen. Zehn Schwertversuche kosten **60 Ore, 30 Solvent, 50 Steine und 20 Odyle**, ohne Fehlschläge oder höhere Stufen. Stelle an einem sicheren Ort her: ein Treffer kann die Herstellung abbrechen und Zutaten verbrauchen.''']),
 section('gather-or-buy', ['The Splendent chain: why the plain sword is not enough', 'Splendentの連鎖：通常品だけでは進めない理由', 'Cadena Splendent: por qué no basta la espada normal', 'Splendent-Kette: warum das normale Schwert nicht reicht'], [
 '''**Orichalcum Longsword → Splendent Orichalcum Longsword → Expert's Orichalcum Longsword → Expert's Splendent Orichalcum Longsword → Artisan's Orichalcum Longsword.**

The **Splendent** output from one tier is an ingredient for the next. The starter sword screen shows **25% Combo Activation Chance**; this is not a guarantee of one upgraded sword every four attempts, and activation is separate from craft success.

One **Expert's Orichalcum Longsword** attempt consumes **1 Splendent Orichalcum Longsword, 5 Expert's Refining Stones, 6 Fine Orichalcum Ore and 3 Fine Odyle (Bound)**. Keep Splendent results; ordinary results cannot substitute for them.''',
 '''**Orichalcum Longsword → Splendent Orichalcum Longsword → Expert’s Orichalcum Longsword → Expert’s Splendent Orichalcum Longsword → Artisan’s Orichalcum Longsword。**

前の段階の**Splendent**品を次の素材に使います。初期の剣は**Combo Activation Chance 25%**ですが、4回ごとに上位品が確定する意味ではなく、発動と製作成功は別です。

**Expert’s Orichalcum Longsword**1回は**Splendent Orichalcum Longsword 1、Expert’s Refining Stone 5、Fine Orichalcum Ore 6、Fine Odyle (Bound) 3**を消費。Splendent品を保管し、通常品で代用しないようにします。''',
 '''**Orichalcum Longsword → Splendent Orichalcum Longsword → Expert’s Orichalcum Longsword → Expert’s Splendent Orichalcum Longsword → Artisan’s Orichalcum Longsword.**

El resultado **Splendent** de un tier sirve de ingrediente del siguiente. La espada inicial muestra **25% Combo Activation Chance**: no garantiza una mejora cada cuatro intentos, y activar combo es distinto de tener éxito.

Un intento de **Expert’s Orichalcum Longsword** consume **1 Splendent Orichalcum Longsword, 5 Expert’s Refining Stones, 6 Fine Orichalcum Ore y 3 Fine Odyle (Bound)**. Conserva los resultados Splendent; los normales no los sustituyen.''',
 '''**Orichalcum Longsword → Splendent Orichalcum Longsword → Expert’s Orichalcum Longsword → Expert’s Splendent Orichalcum Longsword → Artisan’s Orichalcum Longsword.**

Das **Splendent**-Ergebnis einer Stufe ist die Zutat der nächsten. Das Startschwert zeigt **25% Combo Activation Chance**: kein garantiertes Upgrade alle vier Versuche; Combo-Aktivierung und Herstellungserfolg sind verschieden.

Ein Versuch für **Expert’s Orichalcum Longsword** verbraucht **1 Splendent Orichalcum Longsword, 5 Expert’s Refining Stones, 6 Fine Orichalcum Ore und 3 Fine Odyle (Bound)**. Behalte Splendent-Ergebnisse; normale Stücke ersetzen sie nicht.''']),
 section('first-craft', ['Level the profession before an expensive chain', '高価な連鎖の前に製作レベルを上げる', 'Sube el oficio antes de una cadena cara', 'Handwerk vor teuren Ketten leveln'], [
 'Use low-tier material recipes such as **Orichalcum Ingot** to raise Blacksmithing before spending Splendent inputs. A useful early target is **Novice 20** before starting repeated equipment attempts. This is a preparation target, not the unlock level of the starter sword. Each profession levels separately; high gathering proficiency does not unlock a Blacksmithing recipe.',
 '**Orichalcum Ingot**など低位素材の配方でBlacksmithingを上げてから、Splendent品を消費します。装備を繰り返し作る前の目安は**Novice 20**。初期の剣の解放条件とは別の準備目標です。製作職業のレベルは個別で、採集熟練度が高くてもBlacksmithing配方は解放されません。',
 'Usa recetas de materiales básicos como **Orichalcum Ingot** para subir Blacksmithing antes de consumir piezas Splendent. **Novice 20** es un objetivo inicial de preparación para intentos repetidos de equipo, no el nivel que desbloquea la espada básica. Cada oficio sube por separado; recolección alta no desbloquea recetas de Blacksmithing.',
 'Nutze einfache Materialrezepte wie **Orichalcum Ingot**, um Blacksmithing vor dem Einsatz von Splendent-Zutaten zu leveln. **Novice 20** ist ein frühes Vorbereitungsziel für wiederholte Ausrüstungsversuche, nicht die Freischaltstufe des Startschwerts. Handwerke leveln getrennt; hohe Sammelfertigkeit schaltet kein Blacksmithing-Rezept frei.']),
 section('crafting-blockers', ['Why a recipe says materials are missing', '素材不足になる理由', 'Por qué faltan materiales en la receta', 'Warum das Rezept fehlende Zutaten meldet'], [
 '**Wrong quality:** Fine Ore is not plain Ore. **Wrong output:** Splendent is not the ordinary sword. **Wrong count:** batch size multiplies every input. **Equipment unavailable:** remove the input from every equipped preset. Buying missing inputs on the Market requires its [membership access](/monetization); [gathering](/gathering) and merchant materials provide alternatives for the starter recipe.',
 '**品質違い**：Fine Oreと通常Oreは別。**成品違い**：Splendentと通常の剣は別。**数量違い**：製作回数は全素材の必要数を増やします。**装備が使えない**：全プリセットから素材装備を外します。Marketの購入には[メンバーシップ条件](/monetization)があります。初期配方は[採集](/gathering)と商人の素材でも準備できます。',
 '**Calidad incorrecta:** Fine Ore no es Ore normal. **Resultado incorrecto:** Splendent no es la espada normal. **Cantidad:** el lote multiplica todos los ingredientes. **Equipo no disponible:** quita el ingrediente de todos los presets. Comprar en Market exige [acceso de membresía](/monetization); la [recolección](/gathering) y los materiales del comerciante sirven para la receta inicial.',
 '**Falsche Qualität:** Fine Ore ist nicht normales Ore. **Falsches Ergebnis:** Splendent ist nicht das normale Schwert. **Menge:** die Losgröße multipliziert alle Zutaten. **Ausrüstung nicht verfügbar:** Zutat aus allen angelegten Presets entfernen. Käufe im Market erfordern [Mitgliedschaftszugang](/monetization); [Sammeln](/gathering) und Händlermaterialien decken das Startrezept ab.'])], 'gathering',
 [(['Refine ore', '鉱石を精錬', 'Refina mena', 'Erz verarbeiten'], ['2 Ore + 1 Solvent → 1 Ingot.', 'Ore 2 + Solvent 1 → Ingot 1。', '2 Ore + 1 Solvent → 1 Ingot.', '2 Ore + 1 Solvent → 1 Ingot.']),
  (['Make the starter sword', '初期の剣を作る', 'Fabrica la espada inicial', 'Startschwert herstellen'], ['3 Ingots + 5 Refining Stones + 2 Odyle per attempt.', '1回：Ingot 3 + Refining Stone 5 + Odyle 2。', '3 Ingots + 5 Refining Stones + 2 Odyle por intento.', '3 Ingots + 5 Refining Stones + 2 Odyle je Versuch.']),
  (['Keep Splendent output', 'Splendent品を保管', 'Conserva el resultado Splendent', 'Splendent-Ergebnis behalten'], ['The Expert recipe consumes the Splendent sword, not the plain one.', 'Expert配方は通常品ではなくSplendentの剣を消費。', 'La receta Expert consume la espada Splendent, no la normal.', 'Das Expert-Rezept verbraucht das Splendent-Schwert.'])])

page('gear-progression',
 ['AION 2 Gear Progression: Level 45 Upgrade Route', 'AION 2 装備成長：レベル45の更新ルート', 'AION 2: ruta de mejoras de equipo en el nivel 45', 'AION 2: Ausrüstungsweg ab Stufe 45'],
 ['An ordered route through exploration, starter upgrades, Draupnir, belt morphing and later equipment.', '探索、初期強化、Draupnir、ベルト変換、次の装備へ進む順序。', 'Una ruta por exploración, mejoras iniciales, Draupnir, transformación del cinturón y equipo posterior.', 'Eine Reihenfolge für Erkundung, Start-Upgrades, Draupnir, Gürtelumwandlung und spätere Ausrüstung.'],
 ['At 45, collect exploration rewards and spend Daevanion points, enhance your Spirit Forged weapon and Guard, morph the +10 green belt, then fill weak slots through Draupnir. Work toward 1,400 for Vakron Sky Island Conquest.', '45になったら探索報酬とDaevanionポイントを使い、Spirit Forged武器とGuardを強化。緑のベルトを+10で変換し、Draupnirで不足部位を更新。Vakron Sky IslandのConquestに向けて1,400を目標にします。', 'Al 45, recoge recompensas y usa puntos Daevanion, mejora arma y Guard Spirit Forged, transforma el cinturón verde +10 y completa piezas con Draupnir. Apunta a 1.400 para Vakron Sky Island Conquest.', 'Sammle auf 45 Erkundungsbelohnungen und nutze Daevanion-Punkte. Verstärke Spirit-Forged-Waffe und Guard, wandle den grünen +10-Gürtel um und fülle Lücken in Draupnir. Ziel: 1.400 für Vakron Sky Island Conquest.'],
 [section('three-progression-numbers', ['Which number is blocking entry?', '入場を妨げる数値の違い', '¿Qué cifra bloquea la entrada?', 'Welche Zahl blockiert den Eintritt?'], [
 '''| Number | What it controls |
| --- | --- |
| Character level | Skill learning and level-based content unlocks; cap **45** |
| Gear score / item level | Equipment progression and activity entry gates |
| Combat Power | Wider strength from equipment, skill ranks and other growth systems |

The route's **1,400** target is for Vakron Sky Island **Conquest**, not every mode or dungeon. Daevanion points contribute to gear score as well as their selected stat bonuses.''',
 '''| 数値 | 役割 |
| --- | --- |
| キャラクターレベル | スキル習得とレベル条件の解放。上限**45** |
| Gear score / item level | 装備成長とコンテンツの入場条件 |
| Combat Power | 装備、スキルランク、成長要素を含む強さ |

ルートの**1,400**はVakron Sky Islandの**Conquest**向けで、全モードや全ダンジョン共通ではありません。Daevanionのポイントは選んだ能力に加えて装備スコアにも寄与します。''',
 '''| Cifra | Función |
| --- | --- |
| Nivel de personaje | Aprendizaje y desbloqueos por nivel; máximo **45** |
| Gear score / item level | Progresión del equipo y requisitos de entrada |
| Combat Power | Fuerza de equipo, rangos de habilidad y otros sistemas |

El objetivo **1.400** corresponde a Vakron Sky Island **Conquest**, no a todos los modos. Los puntos Daevanion aportan gear score además de sus bonificaciones. ''',
 '''| Zahl | Bedeutung |
| --- | --- |
| Charakterstufe | Fertigkeiten und stufenabhängige Freischaltungen; Maximum **45** |
| Gear score / item level | Ausrüstungsfortschritt und Eintrittsbedingungen |
| Combat Power | Stärke aus Ausrüstung, Fertigkeitsrängen und weiteren Systemen |

Das Ziel **1.400** gilt für Vakron Sky Island **Conquest**, nicht für alle Modi. Daevanion-Punkte tragen neben den gewählten Boni zum Gear Score bei.''']),
 section('fresh-level-45', ['Follow this first equipment route', '最初の装備更新の順序', 'Sigue esta primera ruta de equipo', 'Diese erste Ausrüstungsroute verfolgen'], [
 '''| Order | Action | Result |
| --- | --- | --- |
| 1 | Complete green regional quests, sealed dungeons and strongholds | Daevanion Crystals, skill resources and equipment rewards |
| 2 | Use the Crystals and spend points on the Daevanion board | Permanent stat bonuses and gear score |
| 3 | Enhance the yellow Spirit Forged weapon and Guard; **+10** is a starting target | More weapon strength and equipment score |
| 4 | Morph the starter belt and amulet after the required enhancement | Higher-rarity accessories |
| 5 | Claim useful **Expedition → Exploration → Draupnir** rewards | Fill weak slots; the selection-box track counts reward claims |
| 6 | Finish the remaining campaign and obtain its bracelet rewards | Additional accessory slots for your route |
| 7 | Build toward **1,400** and **Vakron Sky Island Conquest** | Your next dungeon equipment target |

Stop buying temporary upgrades when the next entry goal is met; spare materials can fund the next lasting piece.''',
 '''| 順序 | 操作 | 結果 |
| --- | --- | --- |
| 1 | 緑の地域クエスト、封印ダンジョン、要塞を完了 | Daevanion Crystal、スキル資源、装備報酬 |
| 2 | Crystalを使いDaevanionボードにポイントを振る | 恒久能力と装備スコア |
| 3 | 黄色のSpirit Forged武器とGuardを強化。初期目標は**+10** | 武器性能と装備スコア |
| 4 | 必要な強化後に初期ベルトとアミュレットを変換 | 上位レアリティの装飾品 |
| 5 | **Expedition → Exploration → Draupnir**の必要な報酬を受領 | 弱い部位を更新。選択箱の進行は報酬受領を数える |
| 6 | 残りのストーリーを完了してブレスレット報酬を得る | 追加の装飾品更新 |
| 7 | **1,400**を目指し**Vakron Sky Island Conquest**へ | 次のダンジョン装備目標 |

次の入場目標に届いたら、一時装備への追加購入を止めて次の長く使う装備に素材を残します。''',
 '''| Orden | Acción | Resultado |
| --- | --- | --- |
| 1 | Completa misiones verdes, mazmorras selladas y fortalezas | Daevanion Crystals, recursos de habilidad y equipo |
| 2 | Usa los cristales y gasta puntos en el tablero Daevanion | Estadísticas permanentes y gear score |
| 3 | Mejora arma y Guard Spirit Forged amarillos; **+10** como objetivo inicial | Más fuerza de arma y puntuación |
| 4 | Transforma cinturón y amuleto tras la mejora requerida | Accesorios de mayor rareza |
| 5 | Reclama recompensas útiles de **Expedition → Exploration → Draupnir** | Sustituye piezas débiles; el cofre de selección cuenta reclamaciones |
| 6 | Termina la campaña y consigue sus brazaletes | Más mejoras de accesorios |
| 7 | Alcanza **1.400** para **Vakron Sky Island Conquest** | Siguiente objetivo de equipo |

Cuando alcances la entrada siguiente, deja de comprar mejoras temporales y reserva materiales para una pieza duradera.''',
 '''| Reihenfolge | Aktion | Ergebnis |
| --- | --- | --- |
| 1 | Grüne Gebietsquests, versiegelte Dungeons und Festungen abschließen | Daevanion-Kristalle, Fertigkeitsressourcen und Ausrüstung |
| 2 | Kristalle nutzen und Punkte im Daevanion-Board ausgeben | Dauerhafte Werte und Gear Score |
| 3 | Gelbe Spirit-Forged-Waffe und Guard verstärken; frühes Ziel **+10** | Waffenstärke und Ausrüstungswert |
| 4 | Startgürtel und Amulett nach erforderlicher Verstärkung umwandeln | Höhere Seltenheit |
| 5 | Nützliche Belohnungen aus **Expedition → Exploration → Draupnir** abholen | Schwache Plätze ersetzen; Auswahlkisten zählen Belohnungsansprüche |
| 6 | Verbleibende Kampagne für ihre Armreif-Belohnungen abschließen | Weitere Accessoire-Upgrades |
| 7 | **1.400** für **Vakron Sky Island Conquest** anstreben | Nächstes Dungeon-Ausrüstungsziel |

Nach Erreichen des nächsten Eintrittsziels keine weiteren Übergangs-Upgrades kaufen; Materialien für ein länger genutztes Stück sparen.''']),
 section('growth-and-enhancement', ['Spend on the right upgrade system', '強化システムごとの用途', 'Usa el sistema de mejora adecuado', 'Das passende Upgrade-System nutzen'], [
 "**Growth/Enhancement** raises the item's enhancement level. **Manastones** add socket stats; use inexpensive stones on pieces you will soon replace. **Theostones** add their own weapon/Guard effects. **Soul Binding → Synchronization** rerolls one stat using a sacrificed item; **Reset** rerolls the stat set; **Bind** improves the values of the chosen lines. Choose useful lines before spending to raise their values. These operations have different inputs and are not interchangeable.",
 '**Growth/Enhancement**は装備の強化値、**Manastone**はソケット能力です。短期装備には安価な石を使います。**Theostone**は武器・Guardの効果。**Soul Binding → Synchronization**は装備を素材に1能力を再抽選、**Reset**は能力の組、**Bind**は選んだ能力値を上げます。能力の種類を決めてから数値に投資します。各操作の素材と結果は別です。',
 '**Growth/Enhancement** aumenta el nivel de mejora. **Manastones** añaden estadísticas de ranura; usa piedras económicas en piezas temporales. **Theostones** aportan efectos de arma/Guard. **Soul Binding → Synchronization** cambia una línea sacrificando un objeto; **Reset** cambia el conjunto; **Bind** mejora valores de las líneas elegidas. Elige primero las líneas útiles y después mejora sus valores.',
 '**Growth/Enhancement** erhöht die Verstärkungsstufe. **Manastones** geben Sockelwerte; günstige Steine reichen für Übergangsteile. **Theostones** geben Waffen-/Guard-Effekte. **Soul Binding → Synchronization** würfelt eine Zeile mit einem geopferten Gegenstand neu; **Reset** den Zeilensatz; **Bind** verbessert die Werte gewählter Zeilen. Wähle zuerst passende Zeilen, bevor du ihre Werte erhöhst.']),
 section('belt-and-amulet', ['Noble Belt: green +10 to blue', 'Noble Belt：緑+10から青へ', 'Noble Belt: de verde +10 a azul', 'Noble Belt: von Grün +10 zu Blau'], [
 '1. Enhance the green **Noble Belt to +10**.\n2. Unequip it from **every preset**, not just the active one.\n3. Open **Substance Morph → Gear** and select the **blue Noble Belt** recipe.\n4. Submit the **+10 green Noble Belt** as its input. The shown recipe has **100% success** and produces the blue belt.\n\nAmulet recipes are in the same Gear list, including **Revelation Amulet** and **Fierce Battle Amulet**. Match your amulet to its own recipe; an unrelated accessory cannot replace the required input.',
 '1. 緑の**Noble Beltを+10**にします。\n2. 使用中だけでなく**全プリセット**から外します。\n3. **Substance Morph → Gear**で**青のNoble Belt**配方を選びます。\n4. **緑の+10 Noble Belt**を素材に使用。配方の成功率は**100%**で青のベルトになります。\n\n同じGear欄には**Revelation Amulet**と**Fierce Battle Amulet**の配方があります。自分のアミュレットに対応するものを選び、別の装飾品で代用しないようにします。',
 '1. Mejora el **Noble Belt verde a +10**.\n2. Quítalo de **todos los presets**, no solo del activo.\n3. Abre **Substance Morph → Gear** y elige la receta del **Noble Belt azul**.\n4. Usa el **Noble Belt verde +10** como ingrediente. La receta muestra **100% de éxito** y produce el cinturón azul.\n\nLa lista Gear incluye **Revelation Amulet** y **Fierce Battle Amulet**. Elige la receta de tu amuleto; otro accesorio no sustituye al ingrediente.',
 '1. Den grünen **Noble Belt auf +10** verstärken.\n2. Aus **allen Presets** ablegen, nicht nur aus dem aktiven.\n3. **Substance Morph → Gear** öffnen und das Rezept für den **blauen Noble Belt** wählen.\n4. Den **grünen +10 Noble Belt** einsetzen. Das Rezept zeigt **100% Erfolg** und ergibt den blauen Gürtel.\n\nIn der Gear-Liste stehen auch **Revelation Amulet** und **Fierce Battle Amulet**. Wähle das Rezept deines Amuletts; ein anderes Accessoire ersetzt die Zutat nicht.']),
 section('sockets-binding-and-transfer', ['What equipment transfer keeps and loses', '装備継承で残るもの・失うもの', 'Qué conserva y pierde la transferencia', 'Was Transfer behält und verliert'], [
 '''| Upgrade on the source | Transfer result |
| --- | --- |
| Enhancement level | Carried to the destination |
| Soul Binding lines | Carried to the destination |
| Manastones | Not retained |
| Theostones | Not retained |
| Potential | Not retained |

Use **Enhancement → Transfer** for eligible equipment. The source is consumed, so keep the new piece and required transfer material ready before confirming. Do not socket expensive stones into a temporary source expecting them to move with it.''',
 '''| 元装備の強化 | 継承結果 |
| --- | --- |
| 強化値 | 次の装備へ継承 |
| Soul Bindingの能力 | 次の装備へ継承 |
| Manastone | 継承されない |
| Theostone | 継承されない |
| Potential | 継承されない |

対応装備は**Enhancement → Transfer**を使います。元装備は消費されるため、新しい装備と継承素材を用意してから確定。高価な石が移ると思って一時装備に入れないようにします。''',
 '''| Mejora del objeto original | Resultado |
| --- | --- |
| Nivel de mejora | Se transfiere |
| Líneas Soul Binding | Se transfieren |
| Manastones | No se conservan |
| Theostones | No se conservan |
| Potential | No se conserva |

Usa **Enhancement → Transfer** con equipo compatible. El original se consume: prepara destino y materiales antes de confirmar. No coloques piedras caras en una pieza temporal esperando transferirlas.''',
 '''| Upgrade der Quelle | Transfer-Ergebnis |
| --- | --- |
| Verstärkungsstufe | Wird übertragen |
| Soul-Binding-Zeilen | Werden übertragen |
| Manastones | Werden nicht behalten |
| Theostones | Werden nicht behalten |
| Potential | Wird nicht behalten |

Nutze **Enhancement → Transfer** für zulässige Ausrüstung. Die Quelle wird verbraucht; Ziel und Transfermaterial vor der Bestätigung bereithalten. Teure Steine in einem Übergangsteil wandern nicht mit.''']),
 section('next-upgrade', ['After your first dungeon equipment', '最初のダンジョン装備の次', 'Después del primer equipo de mazmorra', 'Nach der ersten Dungeon-Ausrüstung'], [
 'Use **Transcendence** for Arcana progression when its mode opens to you. Add crafted jewelry or a weapon when you can fund its full [recipe chain](/crafting), rather than spending on one incomplete tier. Keep Class Runes equipped; risky enhancement can destroy a rune. Obtain a replacement before gambling with your only copy. For repeatable resource tasks, use the [daily and weekly checklist](/daily-weekly-checklist).',
 '利用できるモードが開いたら**Transcendence**でArcanaを進めます。製作武器や装飾品は[配方の連鎖](/crafting)全体の素材が用意できてから追加。Class Runeは装備しておき、失敗で失う強化は唯一の1個で行わず、予備を入手してからにします。反復する資源集めは[日課と週課](/daily-weekly-checklist)へ。',
 'Usa **Transcendence** para Arcana cuando se abra el modo. Añade joyas o armas fabricadas cuando puedas financiar toda la [cadena de recetas](/crafting). Mantén equipadas Class Runes: las mejoras arriesgadas pueden destruirlas. Consigue otra antes de arriesgar tu única copia. Organiza recursos con la [lista diaria y semanal](/daily-weekly-checklist).',
 'Nutze **Transcendence** für Arcana, sobald der passende Modus offen ist. Stelle Schmuck oder Waffen erst her, wenn die ganze [Rezeptkette](/crafting) finanzierbar ist. Class Runes angelegt lassen; riskante Verstärkung kann eine Rune zerstören. Vor dem Risiko mit der einzigen Kopie Ersatz besorgen. Ressourcenaufgaben stehen in der [Tages- und Wochenliste](/daily-weekly-checklist).'])], 'daily-weekly-checklist',
 [(['Exploration', '探索', 'Exploración', 'Erkundung'], ['Green quests, sealed dungeons and strongholds supply Daevanion resources.', '緑クエスト、封印ダンジョン、要塞でDaevanion資源。', 'Misiones verdes, selladas y fortalezas dan recursos Daevanion.', 'Grüne Quests, versiegelte Dungeons und Festungen liefern Daevanion.']),
  (['Starter equipment', '初期装備', 'Equipo inicial', 'Startausrüstung'], ['Spirit Forged upgrades and +10 Noble Belt morphing.', 'Spirit Forged強化と+10 Noble Belt変換。', 'Mejoras Spirit Forged y transformación de Noble Belt +10.', 'Spirit-Forged-Upgrades und Noble Belt +10 umwandeln.']),
  (['Next dungeon', '次のダンジョン', 'Siguiente mazmorra', 'Nächster Dungeon'], ['Draupnir fills slots on the route toward Vakron Sky Island Conquest.', 'Draupnirで更新しVakron Sky Island Conquestへ。', 'Draupnir completa piezas hacia Vakron Sky Island Conquest.', 'Draupnir füllt Plätze auf dem Weg zu Vakron Sky Island Conquest.'])])

def write_pages():
    for slug, p in PAGES.items():
        for i, locale in enumerate(LOCALES):
            folder = ROOT / f'src/content/{locale}'
            meta = json.loads((folder / f'{slug}.json').read_text(encoding='utf-8'))
            meta.update(title=p['titles'][i], summary=p['summaries'][i], quickAnswer=p['answers'][i], description=p['summaries'][i], toc=[{'id': id, 'title': heads[i]} for id, heads, bodies in p['sections']], inlineNext=[p['next']])
            meta['visuals'] = {'workflow': {'title': p['titles'][i], 'caption': p['summaries'][i], 'steps': [{'label': labels[i], 'description': details[i]} for labels, details in p['diagram']]}}
            body = '\n\n'.join(f'<h2 id="{id}">{heads[i]}</h2>\n\n{bodies[i]}' for id, heads, bodies in p['sections'])
            body += f'\n\n<GuideVisual id="workflow" />\n\n<GuideNext slug="{p["next"]}" />\n'
            (folder / f'{slug}.mdx').write_text(body, encoding='utf-8')
            (folder / f'{slug}.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        data_path = ROOT / f'src/content/article-data/{slug}.json'
        data = json.loads(data_path.read_text(encoding='utf-8'))
        data.update(checkedAt='2026-10-06', revision='2026-10-06.beginner-depth-2')
        data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

if __name__ == '__main__':
    write_pages()
    print(f'Authored {len(PAGES)} task guides in four languages.')
