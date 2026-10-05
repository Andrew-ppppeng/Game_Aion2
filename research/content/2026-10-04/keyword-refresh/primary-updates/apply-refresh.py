"""Explicit four-language content changes for the approved keyword refresh."""
import json
import re
import shutil
from pathlib import Path

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
LOCALES = ("en", "ja", "es", "de")
SLUGS = ("classes", "leveling", "download", "notmeter")

TEXT = {
"en": {
"classes_meta": ["AION 2 Classes: Roles, Icons, Skills and Gameplay", "Compare all eight AION 2 Global classes, their icons and combat roles. Find skill guides and choose for solo play, PvE groups or PvP.", "Global offers eight classes. Compare their roles and controls, use the icons to identify them, and follow the skill guide for the class you want to try."],
"skills_title": "Class skills and gameplay guides",
"skills": "For skill choices and an opening combat loop, use the [Gladiator](/gladiator), [Ranger](/ranger), [Spiritmaster](/spiritmaster), [Chanter](/chanter), or [Cleric](/cleric-build) guide. The [builds overview](/builds) explains active skills and Stigma choices.\n\nFor **PvE**, compare the job you will perform in a dungeon: positioning the boss, recovering allies, keeping buffs active, or dealing damage through mechanics. For **PvP**, compare target access, control, escape options, and recovery under pressure. Use the [PvE and PvP tier comparison](/tier-list) with the [PvP guide](/pvp); keep the activity and service region consistent when choosing a build.",
"brawler": "Brawler uses Gauntlets for frontline attacks and combo-based charges. Basic attacks and active skills build Rage; its Rage gauge activates Rampage. This is a **KR/TW Chapter 1** class, with no announced Global availability date.",
"level_meta": ["AION 2 Max Level and Leveling: Global 45, KR/TW 50", "AION 2's Global launch max level is 45; KR/TW Chapter 1 raises it to 50. Follow faction routes, resolve progression gates and plan what to do at the cap.", "Global launches with a character-level cap of 45. KR/TW Chapter 1 has a cap of 50. Follow your faction's campaign, then finish unlocks and progress equipment at the cap.", "The Global launch maximum character level is 45. KR/TW Chapter 1 raises it to 50. Skill levels and gathering proficiency are separate progression systems; reaching the character cap does not finish your story or dungeon unlocks."],
"level_heading": "What is the AION 2 max level?",
"cap_intro": "**Global's launch max level is 45. KR/TW Chapter 1 raises the character cap to 50.**\n\n| Service | Character level cap | Route to follow |\n| --- | --- | --- |\n| Global launch | 45 | Your faction's 1–45 campaign |\n| KR/TW, Chapter 1 | 50 | Continue into Eltnen or Morheim after the earlier campaign |\n\nCharacter level, skill level, and gathering proficiency use separate progression. The level-50 KR/TW route is not the Global launch route. For collection and extraction progression, use the [gathering guide](/gathering); for skill upgrades, use [builds](/builds).\n\nFollow the main story and complete nearby objectives when they meet the next progression requirement. Finish remaining story unlocks after reaching the cap.\n\n",
"cap_faq": "<h3>How long does it take to reach max level?</h3>\n\nThere is no fixed completion time. Travel, side objectives, progression gates and time spent learning your class change the length of the run. Plan a session around the next campaign unlock rather than a promised number of hours.\n\n<h3>Why does a level-45 character still have progression left?</h3>\n\nThe character-level cap does not complete unfinished quests or meet every dungeon's equipment requirement. Use this order:\n\n1. Finish pending campaign objectives and turn-ins.\n2. Open the entry panel for the activity you want to play and identify the missing quest or equipment condition.\n3. Review active skills and equipped options for that activity.\n4. Choose accessible content that supplies the specific unlock or equipment improvement you need.\n\n",
"download_meta": ["AION 2 Download and PC Specs: System Requirements", "Check AION 2 Global minimum and recommended PC specs, 100 GB storage and installation steps for Steam or PURPLE, plus the separate Taiwan client.", "Global's Windows PC client needs 8 GB RAM minimum, with 16 GB recommended, and 100 GB available storage. Compare the full CPU/GPU table, then install through Steam or PURPLE.", "Global PC minimum specs include Windows 10/11 64-bit, 8 GB RAM and GTX 1050 Ti 4 GB; recommended specs include 16 GB RAM and RTX 2070 8 GB. Reserve 100 GB of available space. Install the official Steam or PURPLE client and check account access separately."],
"spec_scope": "**Global PC requirements:** use this table for the Windows Global client. KR/TW mobile specifications apply to separate regional clients and do not establish Global mobile availability. See [platform support](/steam#platform-and-controller-support) before choosing a device.\n\n",
"spec_title": "Check your own PC specs",
"spec_check": "1. Press **Windows + R**, enter `dxdiag`, and open the DirectX Diagnostic Tool.\n2. On **System**, check the operating system, processor, memory and DirectX version. Compare each with the table above.\n3. On **Display**, check the graphics adapter's name. If your PC has several adapters, check the other Display or Render tabs too.\n4. Check free space on the drive you will select in Steam or PURPLE. The storage requirement is available disk space, not an exact download size.\n\nStart with **Very Low at FHD** on the listed minimum hardware or **Low at FHD** on the recommended hardware. These presets do not promise a fixed frame rate.\n\n**Can I install it on a phone?** These instructions install Global's Windows PC client. Do not use a KR/TW mobile download or phone requirements as a substitute for the Global installer.\n\n",
"tw_title": "Install the separate Taiwan client",
"tw": "**TW:** use the [official Taiwan download page](https://tw.ncsoft.com/aion2/download/index). It installs a separate regional service; the Global Steam app is not a Taiwan-server installer.\n\n1. Download and install **PurpleInstaller** from the Taiwan page.\n2. Start PURPLE and choose **AION2** in **STORE**.\n3. In the game lobby, select **安裝遊戲** (Install Game) and finish the download and updates.\n\nInstallation does not establish account eligibility. Follow the Taiwan service's sign-in and verification requirements for your account before expecting server access. Do not change your account country or use a purchased account to follow these installation steps.\n\n",
"not_meta": ["AION 2 DPS Meter: NotMeter Setup and Damage Records", "Use NotMeter's AION 2 damage records, install Npcap and compare DPS or nDPS. Check desktop region support and account policy before combat capture.", "NotMeter is a third-party AION 2 DPS meter and combat-record website. Website Global searches and desktop capture are separate; current Global desktop compatibility is unconfirmed.", "NotMeter provides third-party AION 2 damage records. Its Windows setup is Npcap, then the extracted NotMeter ZIP. Global website search is available, but current Global desktop capture compatibility is unconfirmed; check region support and account policy before installing."],
"not_intro": "NotMeter is a third-party **AION 2 DPS meter** with a combat-record and ranking website. Choose the feature you need before installing anything: character search and existing records work through the website; capturing a new fight uses the desktop tool.\n\n",
"not_title": "Website records or desktop damage capture?",
"not_features": "| What you want | Where to start | Important condition |\n| --- | --- | --- |\n| Find a character's equipment, skills or records | [NotMeter website](https://notmeter.com/) | Select KR, TW or Global, then the correct server and character name |\n| Compare existing damage records | Website encounter and ranking filters | Match boss, difficulty, period and CP range |\n| Capture your own combat | Maintainer's desktop distribution | Check game-region and patch compatibility before installing |\n\n**Global:** website character search is available; current desktop combat-capture compatibility is unconfirmed. A Global search option does not make an older desktop release compatible with the Global game client.\n\nThis guide covers NotMeter's Npcap-dependent setup. OCR tools read screen text and use a different setup; do not mix their installation instructions with NotMeter's.\n\n",
"not_install": "1. Open [notmeter.com](https://notmeter.com/) and use its linked [Npcap installer](https://npcap.com/) if Npcap is not already installed.\n2. Download the NotMeter ZIP from the linked [maintainer releases](https://github.com/Not4You-Dev/NotMeter-Releases/releases).\n3. Extract the ZIP into a folder before running `NotMeter.exe`; keep the included files together.\n4. Confirm the release's supported service region and patch before attempting combat capture. If it records nothing, use the checks below rather than assuming a successful installation means compatibility.\n\n",
},
"ja": {
"classes_meta": ["AION 2のクラス：役割・アイコン・スキルと操作", "AION 2 Globalの全8クラスを役割とアイコンで比較。スキルガイドから操作を確認し、ソロ・PvE・PvPに合う職業を選びましょう。", "Globalは8クラスです。役割と操作を比較し、アイコンで職業を見分け、試したいクラスのスキルガイドへ進みましょう。"],
"skills_title": "クラスのスキルと操作ガイド",
"skills": "スキル選択と最初の攻撃手順は、[Gladiator](/gladiator)、[Ranger](/ranger)、[Spiritmaster](/spiritmaster)、[Chanter](/chanter)、[Cleric](/cleric-build)のガイドで確認できます。[ビルド概要](/builds)ではアクティブスキルとStigmaの選択を扱います。\n\n**PvE**では、ボスの位置調整、味方の回復、バフ維持、ギミック中の攻撃など、ダンジョンで担当する仕事を比較します。**PvP**では、敵への接近、妨害、離脱、攻撃を受けながらの立て直しを比較しましょう。[PvE・PvPのティア比較](/tier-list)と[PvPガイド](/pvp)を使い、活動とサービス地域をそろえて構成を選びます。",
"brawler": "BrawlerはGauntletsを使う前衛で、連続攻撃と突進を得意とします。通常攻撃とアクティブスキルでRageがたまり、ゲージによってRampageが発動します。**KR/TWのChapter 1**のクラスで、Globalへの追加日は発表されていません。",
"level_meta": ["AION 2の最大レベルと育成：Global 45・KR/TW 50", "AION 2 Global開始時の最大レベルは45、KR/TW Chapter 1は50です。種族別の育成、進行条件の解決、上限到達後の優先順位を確認できます。", "Global開始時のキャラクターレベル上限は45、KR/TW Chapter 1は50です。種族のストーリーを進め、上限後も開放条件と装備を整えましょう。", "Global開始時の最大キャラクターレベルは45です。KR/TW Chapter 1では50になります。スキルレベルと採集熟練度は別の成長要素で、レベル上限だけではストーリーやダンジョンの開放は終わりません。"],
"level_heading": "AION 2の最大レベルはいくつ？",
"cap_intro": "**Global開始時の最大レベルは45です。KR/TW Chapter 1ではキャラクター上限が50になります。**\n\n| サービス | キャラクターレベル上限 | 進めるルート |\n| --- | --- | --- |\n| Global開始時 | 45 | 種族別の1～45キャンペーン |\n| KR/TW、Chapter 1 | 50 | 以前のキャンペーン後にEltnenまたはMorheimへ進む |\n\nキャラクターレベル、スキルレベル、採集熟練度は別々に成長します。KR/TWのレベル50ルートはGlobal開始時のルートではありません。採集と抽出の成長は[採集ガイド](/gathering)、スキル強化は[ビルド](/builds)で確認できます。\n\nメインストーリーを軸に、次の条件を満たす近くの目標を進めます。上限到達後も残るストーリー開放を終えましょう。\n\n",
"cap_faq": "<h3>最大レベルまで何時間かかる？</h3>\n\n所要時間は一定ではありません。移動、サブ目標、進行条件、クラスの操作を覚える時間によって変わります。決められた時間を目指すより、次のキャンペーン開放を一回のプレイ目標にしましょう。\n\n<h3>レベル45でも成長が残るのはなぜ？</h3>\n\nレベル上限に達しても、未完了のクエストや各ダンジョンの装備条件は残ります。次の順に進めましょう。\n\n1. 残っているキャンペーン目標と報告を終える。\n2. 参加したい活動の入場画面で、不足しているクエストや装備条件を確認する。\n3. その活動に合うアクティブスキルと装備の選択肢を見直す。\n4. 必要な開放や装備改善が得られる、参加可能な活動を選ぶ。\n\n",
"download_meta": ["AION 2のダウンロードとPCスペック：必要環境", "AION 2 Globalの最低・推奨PCスペック、100 GBの空き容量、Steam・PURPLEの導入手順と別サービスの台湾クライアントを確認できます。", "GlobalのWindows PC版は最低8 GB、推奨16 GBのRAMと100 GBの空き容量が必要です。CPU・GPUの表を確認し、SteamかPURPLEで導入します。", "Global PC版の最低環境はWindows 10/11 64-bit、8 GB RAM、GTX 1050 Ti 4 GBなどです。推奨は16 GB RAMとRTX 2070 8 GB。100 GBの空き容量を用意し、SteamかPURPLEから導入してアカウントの利用権を別途確認します。"],
"spec_scope": "**Global PC版の必要環境：** この表はGlobalのWindowsクライアント用です。KR/TWのモバイル環境は別の地域クライアント用で、Globalのモバイル提供を意味しません。端末選びの前に[対応プラットフォーム](/steam#platform-and-controller-support)を確認しましょう。\n\n",
"spec_title": "自分のPCスペックを確認する",
"spec_check": "1. **Windows + R**を押し、`dxdiag`を入力してDirectX診断ツールを開きます。\n2. **System**でOS、CPU、メモリ、DirectXの版を確認し、上の表と比較します。\n3. **Display**でGPU名を確認します。複数のGPUがあるPCでは、ほかのDisplayやRenderタブも確認しましょう。\n4. SteamかPURPLEで選ぶドライブの空き容量を確認します。100 GBは必要な空き容量で、固定のダウンロード量ではありません。\n\n表の最低環境では**FHD・Very Low**、推奨環境では**FHD・Low**から始めます。一定のフレームレートを保証する設定ではありません。\n\n**スマートフォンにも入れられる？** ここではGlobalのWindows PC版を導入します。KR/TWのモバイルダウンロードやスマートフォンの環境をGlobalインストーラーの代わりに使わないでください。\n\n",
"tw_title": "別サービスの台湾クライアントを導入する",
"tw": "**TW：** [台湾の公式ダウンロードページ](https://tw.ncsoft.com/aion2/download/index)を使います。別の地域サービスを導入する手順で、GlobalのSteamアプリは台湾サーバー用のインストーラーではありません。\n\n1. 台湾のページから**PurpleInstaller**をダウンロードして導入します。\n2. PURPLEを起動し、**STORE**で**AION2**を選びます。\n3. ゲームロビーで**安裝遊戲**（ゲームをインストール）を選び、ダウンロードと更新を終えます。\n\n導入だけではアカウントの利用資格は決まりません。サーバーに入る前に、そのアカウントに適用される台湾サービスのログイン・認証条件を満たしてください。この導入手順のためにアカウントの国を変えたり、購入したアカウントを使ったりしないでください。\n\n",
"not_meta": ["AION 2 DPSメーター：NotMeterの導入とダメージ記録", "NotMeterでAION 2のDPS・nDPSを比較し、Npcapを導入する手順を確認。戦闘の記録前にデスクトップ版の地域対応とアカウント規約を確認します。", "NotMeterは第三者製のAION 2 DPSメーターと戦闘記録サイトです。GlobalのWeb検索とデスクトップ記録は別機能で、現行Global版での記録互換性は未確認です。", "NotMeterは第三者製のAION 2ダメージ記録ツールです。WindowsではNpcapとNotMeterのZIPを導入します。WebのGlobal検索は利用できますが、現行Global版のデスクトップ記録互換性は未確認です。導入前に地域対応と規約を確認してください。"],
"not_intro": "NotMeterは第三者製の**AION 2 DPSメーター**で、戦闘記録とランキングのサイトも提供します。導入前に目的を選びましょう。キャラクター検索と既存記録はWeb、戦闘の新規記録はデスクトップ版を使います。\n\n",
"not_title": "Webの記録を見る？デスクトップで記録する？",
"not_features": "| 目的 | 開始場所 | 重要な条件 |\n| --- | --- | --- |\n| 装備・スキル・キャラクター記録を探す | [NotMeterサイト](https://notmeter.com/) | KR・TW・Globalと正しいサーバー、名前を選ぶ |\n| 既存のダメージ記録を比較する | Webの戦闘・ランキングフィルター | ボス、難度、期間、CP帯をそろえる |\n| 自分の戦闘を記録する | 開発者のデスクトップ配布先 | 導入前にゲーム地域とパッチへの対応を確認する |\n\n**Global：** Webのキャラクター検索は利用できます。現行デスクトップ版の戦闘記録互換性は未確認です。Global検索の選択肢があっても、古いデスクトップ版がGlobalクライアントに対応しているとは限りません。\n\nこのガイドはNpcapを必要とするNotMeterの導入手順です。OCRツールは画面の文字を読み取る別方式なので、その導入手順をNotMeterと混ぜないでください。\n\n",
"not_install": "1. [notmeter.com](https://notmeter.com/)を開き、Npcapがなければリンク先の[Npcapインストーラー](https://npcap.com/)を使います。\n2. リンクされている[開発者のリリース](https://github.com/Not4You-Dev/NotMeter-Releases/releases)からNotMeterのZIPを入手します。\n3. ZIPをフォルダーに展開してから`NotMeter.exe`を実行します。同梱ファイルはまとめて置いてください。\n4. 記録前に、そのリリースの対応地域とパッチを確認します。記録されない場合は下の確認項目を使い、導入成功だけで互換性があると判断しないでください。\n\n",
},
"es": {
"classes_meta": ["Clases de AION 2: roles, iconos, habilidades y juego", "Compara las ocho clases Global de AION 2, sus iconos y roles. Encuentra guías de habilidades y elige para jugar solo, en grupos PvE o en PvP.", "Global ofrece ocho clases. Compara sus roles y controles, reconoce sus iconos y sigue la guía de habilidades de la clase que quieras probar."],
"skills_title": "Guías de habilidades y juego por clase",
"skills": "Para elegir habilidades y preparar una primera secuencia de combate, consulta las guías de [Gladiator](/gladiator), [Ranger](/ranger), [Spiritmaster](/spiritmaster), [Chanter](/chanter) o [Cleric](/cleric-build). El [resumen de builds](/builds) explica habilidades activas y opciones de Stigma.\n\nEn **PvE**, compara el trabajo que harás en una mazmorra: colocar al jefe, recuperar aliados, mantener buffs o atacar mientras resuelves mecánicas. En **PvP**, compara acceso al objetivo, control, escapes y recuperación bajo presión. Usa la [comparación de tiers PvE y PvP](/tier-list) con la [guía PvP](/pvp); mantén la misma actividad y región al elegir una build.",
"brawler": "Brawler usa Gauntlets para ataques de primera línea y cargas encadenadas. Los ataques básicos y las habilidades activas generan Rage; su medidor activa Rampage. Es una clase de **Chapter 1 en KR/TW**, sin fecha anunciada para Global.",
"level_meta": ["Nivel máximo de AION 2: Global 45, KR/TW 50 y rutas", "El nivel máximo de lanzamiento Global de AION 2 es 45; KR/TW Chapter 1 lo eleva a 50. Sigue rutas por facción y prepara el progreso tras alcanzar el límite.", "Global empieza con un límite de nivel de personaje de 45. KR/TW Chapter 1 tiene 50. Sigue la campaña de tu facción y continúa los desbloqueos y el equipo al llegar al máximo.", "El nivel máximo de personaje en el lanzamiento Global es 45. KR/TW Chapter 1 lo eleva a 50. Los niveles de habilidades y la pericia de recolección progresan aparte; el máximo de personaje no completa historia ni desbloqueos de mazmorras."],
"level_heading": "¿Cuál es el nivel máximo de AION 2?",
"cap_intro": "**El nivel máximo de lanzamiento Global es 45. KR/TW Chapter 1 eleva el límite de personaje a 50.**\n\n| Servicio | Nivel máximo de personaje | Ruta que seguir |\n| --- | --- | --- |\n| Lanzamiento Global | 45 | Campaña de tu facción de 1 a 45 |\n| KR/TW, Chapter 1 | 50 | Continúa hacia Eltnen o Morheim tras la campaña anterior |\n\nNivel de personaje, nivel de habilidad y pericia de recolección progresan por separado. La ruta KR/TW hasta 50 no es la del lanzamiento Global. Consulta la [guía de recolección](/gathering) para recolección y extracción, y las [builds](/builds) para mejoras de habilidades.\n\nSigue la historia principal y completa objetivos cercanos que resuelvan el siguiente requisito. Termina los desbloqueos pendientes tras alcanzar el límite.\n\n",
"cap_faq": "<h3>¿Cuánto se tarda en llegar al nivel máximo?</h3>\n\nNo hay un tiempo fijo. Los viajes, objetivos secundarios, requisitos de progreso y práctica de tu clase cambian la duración. Organiza la sesión alrededor del siguiente desbloqueo de campaña en vez de un número prometido de horas.\n\n<h3>¿Por qué queda progreso al llegar al nivel 45?</h3>\n\nEl límite de personaje no termina las misiones pendientes ni cumple todos los requisitos de equipo de las mazmorras. Sigue este orden:\n\n1. Termina los objetivos y entregas pendientes de la campaña.\n2. Abre el panel de entrada de la actividad que quieres jugar e identifica la condición de misión o equipo que falta.\n3. Revisa las habilidades activas y opciones equipadas para esa actividad.\n4. Elige contenido accesible que dé el desbloqueo o mejora de equipo concretos que necesitas.\n\n",
"download_meta": ["Descarga y specs de AION 2: requisitos de PC", "Comprueba las specs mínimas y recomendadas de AION 2 Global, 100 GB libres y la instalación en Steam o PURPLE, además del cliente separado de Taiwán.", "El cliente Windows de Global necesita un mínimo de 8 GB de RAM, con 16 GB recomendados, y 100 GB libres. Compara CPU y GPU y después instala desde Steam o PURPLE.", "Los mínimos de Global PC incluyen Windows 10/11 de 64 bits, 8 GB RAM y GTX 1050 Ti de 4 GB; se recomiendan 16 GB RAM y RTX 2070 de 8 GB. Reserva 100 GB libres. Instala el cliente oficial Steam o PURPLE y comprueba el acceso de la cuenta por separado."],
"spec_scope": "**Requisitos Global PC:** esta tabla corresponde al cliente Windows de Global. Las especificaciones móviles de KR/TW pertenecen a otros clientes regionales y no establecen disponibilidad móvil en Global. Consulta las [plataformas compatibles](/steam#platform-and-controller-support) antes de elegir un dispositivo.\n\n",
"spec_title": "Comprueba las specs de tu PC",
"spec_check": "1. Pulsa **Windows + R**, introduce `dxdiag` y abre la herramienta de diagnóstico de DirectX.\n2. En **System**, comprueba sistema operativo, procesador, memoria y versión de DirectX. Compáralos con la tabla.\n3. En **Display**, comprueba el nombre del adaptador gráfico. Si hay varios, revisa también las otras pestañas Display o Render.\n4. Comprueba el espacio libre de la unidad que elegirás en Steam o PURPLE. El requisito es espacio disponible, no el tamaño exacto de descarga.\n\nEmpieza con **Very Low en FHD** en el hardware mínimo indicado o **Low en FHD** en el recomendado. Estos ajustes no garantizan una tasa fija de fotogramas.\n\n**¿Puedo instalarlo en un teléfono?** Estas instrucciones instalan el cliente Windows de Global. No uses una descarga móvil KR/TW ni sus requisitos como sustituto del instalador Global.\n\n",
"tw_title": "Instala el cliente separado de Taiwán",
"tw": "**TW:** usa la [página oficial de descarga de Taiwán](https://tw.ncsoft.com/aion2/download/index). Instala otro servicio regional; la app Steam de Global no es un instalador para servidores de Taiwán.\n\n1. Descarga e instala **PurpleInstaller** desde la página de Taiwán.\n2. Abre PURPLE y elige **AION2** en **STORE**.\n3. En el lobby, selecciona **安裝遊戲** (Instalar juego) y termina la descarga y las actualizaciones.\n\nInstalarlo no establece la elegibilidad de tu cuenta. Cumple las condiciones de inicio de sesión y verificación de Taiwán aplicables a tu cuenta antes de esperar acceso al servidor. No cambies el país de tu cuenta ni uses una cuenta comprada para seguir estos pasos de instalación.\n\n",
"not_meta": ["DPS meter de AION 2: NotMeter y registros de daño", "Compara DPS y nDPS de AION 2 con NotMeter y consulta la instalación de Npcap. Comprueba soporte regional y política de cuenta antes de capturar combates.", "NotMeter es un DPS meter de terceros y un sitio de registros de AION 2. La búsqueda Global y la captura de escritorio son funciones distintas; su compatibilidad actual con Global no está confirmada.", "NotMeter ofrece registros de daño de AION 2 de terceros. En Windows requiere Npcap y extraer su ZIP. La búsqueda web Global está disponible, pero la compatibilidad actual de captura de escritorio no está confirmada. Comprueba soporte regional y política de cuenta antes de instalar."],
"not_intro": "NotMeter es un **DPS meter de AION 2** de terceros, con un sitio de registros y rankings. Decide qué función necesitas antes de instalar: la búsqueda de personajes y los registros existentes se consultan en la web; capturar un combate nuevo requiere la herramienta de escritorio.\n\n",
"not_title": "¿Registros web o captura de daño en escritorio?",
"not_features": "| Objetivo | Por dónde empezar | Condición importante |\n| --- | --- | --- |\n| Buscar equipo, habilidades o registros de un personaje | [Web de NotMeter](https://notmeter.com/) | Selecciona KR, TW o Global y el servidor y nombre correctos |\n| Comparar registros de daño existentes | Filtros web de encuentro y rankings | Iguala jefe, dificultad, periodo y rango de CP |\n| Capturar tu propio combate | Distribución de escritorio del desarrollador | Comprueba compatibilidad con región y parche antes de instalar |\n\n**Global:** la búsqueda web de personajes está disponible; la compatibilidad actual de captura de escritorio no está confirmada. Una opción de búsqueda Global no hace compatible una versión de escritorio antigua con el cliente Global.\n\nEsta guía cubre la instalación de NotMeter con Npcap. Las herramientas OCR leen texto de pantalla y se configuran de otra forma; no mezcles sus instrucciones con las de NotMeter.\n\n",
"not_install": "1. Abre [notmeter.com](https://notmeter.com/) y usa su enlace al [instalador Npcap](https://npcap.com/) si aún no está instalado.\n2. Descarga el ZIP de NotMeter desde los [releases del desarrollador](https://github.com/Not4You-Dev/NotMeter-Releases/releases) enlazados.\n3. Extrae el ZIP en una carpeta antes de ejecutar `NotMeter.exe`; conserva juntos los archivos incluidos.\n4. Confirma región y parche compatibles antes de capturar. Si no registra nada, usa las comprobaciones siguientes; instalar correctamente no garantiza compatibilidad.\n\n",
},
"de": {
"classes_meta": ["AION 2 Klassen: Rollen, Icons, Skills und Spielweise", "Vergleiche alle acht Global-Klassen in AION 2, ihre Icons und Kampfrollen. Finde Fertigkeitsguides und wähle für Solo-Spiel, PvE-Gruppen oder PvP.", "Global bietet acht Klassen. Vergleiche Rollen und Steuerung, erkenne die Icons und folge dem Fertigkeitsguide der Klasse, die du ausprobieren möchtest."],
"skills_title": "Fertigkeiten und Spielweise der Klassen",
"skills": "Für Fertigkeitswahl und eine erste Angriffsfolge nutze die Guides für [Gladiator](/gladiator), [Waldläufer](/ranger), [Beschwörer](/spiritmaster), [Kantor](/chanter) oder [Kleriker](/cleric-build). Die [Build-Übersicht](/builds) erklärt aktive Fertigkeiten und Stigma-Auswahl.\n\nIm **PvE** vergleichst du die Aufgabe im Dungeon: den Boss positionieren, Verbündete heilen, Buffs aufrechterhalten oder während Mechaniken Schaden verursachen. Im **PvP** vergleichst du Zielzugang, Kontrolle, Fluchtmöglichkeiten und Erholung unter Druck. Nutze den [PvE- und PvP-Tiervergleich](/tier-list) mit dem [PvP-Guide](/pvp); wähle Builds für dieselbe Aktivität und Dienstregion.",
"brawler": "Brawler nutzt Gauntlets für Frontangriffe und kombinierte Anstürme. Grundangriffe und aktive Fertigkeiten erzeugen Rage; die Rage-Leiste aktiviert Rampage. Die Klasse gehört zu **KR/TW Chapter 1**. Für Global ist kein Verfügbarkeitstermin angekündigt.",
"level_meta": ["AION 2 Max Level und Leveln: Global 45, KR/TW 50", "Das Global-Startlimit von AION 2 ist Level 45; KR/TW Chapter 1 erhöht es auf 50. Folge Fraktionsrouten, löse Fortschrittsbedingungen und plane den Weg am Limit.", "Global startet mit Charakterlevel 45 als Obergrenze. KR/TW Chapter 1 hat Level 50. Folge der Fraktionskampagne und arbeite am Limit weiter an Freischaltungen und Ausrüstung.", "Das maximale Charakterlevel zum Global-Start ist 45. KR/TW Chapter 1 erhöht es auf 50. Fertigkeitslevel und Sammelroutine entwickeln sich getrennt; das Charakterlimit beendet weder Story noch Dungeon-Freischaltungen."],
"level_heading": "Was ist das maximale Level in AION 2?",
"cap_intro": "**Zum Global-Start beträgt das Max Level 45. KR/TW Chapter 1 erhöht das Charakterlimit auf 50.**\n\n| Dienst | Maximales Charakterlevel | Passende Route |\n| --- | --- | --- |\n| Global-Start | 45 | Fraktionskampagne von 1 bis 45 |\n| KR/TW, Chapter 1 | 50 | Nach der früheren Kampagne weiter nach Eltnen oder Morheim |\n\nCharakterlevel, Fertigkeitslevel und Sammelroutine entwickeln sich getrennt. Die KR/TW-Route bis 50 ist nicht die Route zum Global-Start. Für Sammeln und Extraktion nutze den [Sammelguide](/gathering), für Fertigkeitsverbesserungen die [Builds](/builds).\n\nFolge der Hauptstory und erledige nahe Ziele, wenn sie die nächste Fortschrittsbedingung erfüllen. Schließe auch nach dem Limit verbleibende Story-Freischaltungen ab.\n\n",
"cap_faq": "<h3>Wie lange dauert es bis zum Max Level?</h3>\n\nEs gibt keine feste Abschlusszeit. Reisewege, Nebenziele, Fortschrittsbedingungen und das Lernen deiner Klasse verändern die Dauer. Plane eine Sitzung um die nächste Kampagnenfreischaltung statt um eine versprochene Stundenzahl.\n\n<h3>Warum bleibt auf Level 45 noch Fortschritt übrig?</h3>\n\nDas Charakterlimit erledigt keine offenen Quests und erfüllt nicht jede Ausrüstungsbedingung eines Dungeons. Gehe in dieser Reihenfolge vor:\n\n1. Schließe offene Kampagnenziele und Abgaben ab.\n2. Öffne das Zugangsfenster deiner gewünschten Aktivität und erkenne die fehlende Quest- oder Ausrüstungsbedingung.\n3. Prüfe aktive Fertigkeiten und ausgerüstete Optionen für diese Aktivität.\n4. Wähle zugängliche Inhalte, die genau die benötigte Freischaltung oder Ausrüstungsverbesserung liefern.\n\n",
"download_meta": ["AION 2 Download und PC-Specs: Systemanforderungen", "Prüfe AION 2 Globals minimale und empfohlene PC-Specs, 100 GB freien Speicher und die Installation über Steam oder PURPLE sowie den separaten Taiwan-Client.", "Globals Windows-PC-Client benötigt mindestens 8 GB RAM, empfohlen sind 16 GB, und 100 GB freien Speicher. Vergleiche die CPU-/GPU-Tabelle und installiere über Steam oder PURPLE.", "Global-PC-Mindestwerte umfassen Windows 10/11 64-Bit, 8 GB RAM und GTX 1050 Ti 4 GB; empfohlen sind 16 GB RAM und RTX 2070 8 GB. Halte 100 GB frei. Installiere den offiziellen Steam- oder PURPLE-Client und prüfe die Kontoberechtigung getrennt."],
"spec_scope": "**Global-PC-Anforderungen:** Diese Tabelle gilt für den Windows-Client von Global. Mobile KR/TW-Spezifikationen gehören zu separaten regionalen Clients und bestätigen keine Global-Mobilversion. Prüfe vor der Gerätewahl die [Plattformunterstützung](/steam#platform-and-controller-support).\n\n",
"spec_title": "Prüfe die Specs deines PCs",
"spec_check": "1. Drücke **Windows + R**, gib `dxdiag` ein und öffne das DirectX-Diagnoseprogramm.\n2. Prüfe unter **System** Betriebssystem, Prozessor, Arbeitsspeicher und DirectX-Version. Vergleiche sie mit der Tabelle.\n3. Prüfe unter **Display** den Namen des Grafikadapters. Bei mehreren Adaptern prüfst du auch weitere Display- oder Render-Tabs.\n4. Prüfe den freien Platz auf dem Laufwerk, das du in Steam oder PURPLE wählen wirst. Die Anforderung ist freier Speicherplatz, keine genaue Downloadgröße.\n\nBeginne auf der genannten Mindesthardware mit **FHD und Very Low**, auf empfohlener Hardware mit **FHD und Low**. Diese Einstellungen garantieren keine feste Bildrate.\n\n**Kann ich es auf einem Telefon installieren?** Diese Anleitung installiert Globals Windows-PC-Client. Verwende keine mobile KR/TW-Version oder Telefonanforderungen als Ersatz für den Global-Installer.\n\n",
"tw_title": "Installiere den separaten Taiwan-Client",
"tw": "**TW:** Nutze die [offizielle Taiwan-Downloadseite](https://tw.ncsoft.com/aion2/download/index). Sie installiert einen separaten regionalen Dienst; die Global-Steam-App ist kein Installer für Taiwan-Server.\n\n1. Lade **PurpleInstaller** von der Taiwan-Seite herunter und installiere ihn.\n2. Starte PURPLE und wähle **AION2** in **STORE**.\n3. Wähle in der Spiellobby **安裝遊戲** (Spiel installieren) und schließe Download und Updates ab.\n\nEine Installation bestätigt keine Kontoberechtigung. Erfülle die für dein Konto geltenden Taiwan-Anmelde- und Verifizierungsbedingungen, bevor du Serverzugang erwartest. Ändere für diese Installationsschritte nicht dein Kontoland und verwende kein gekauftes Konto.\n\n",
"not_meta": ["AION 2 DPS-Meter: NotMeter und Schadensaufzeichnungen", "Vergleiche DPS und nDPS von AION 2 mit NotMeter und prüfe die Npcap-Installation. Beachte Desktop-Regionsunterstützung und Kontoregeln vor der Kampfaufzeichnung.", "NotMeter ist ein Drittanbieter-DPS-Meter mit AION-2-Kampfaufzeichnungen. Global-Websuche und Desktop-Aufzeichnung sind getrennt; die aktuelle Global-Desktop-Kompatibilität ist unbestätigt.", "NotMeter bietet AION-2-Schadensaufzeichnungen eines Drittanbieters. Windows benötigt Npcap und die entpackte NotMeter-ZIP. Global-Websuche ist verfügbar, die aktuelle Desktop-Aufzeichnungskompatibilität aber unbestätigt. Prüfe vor der Installation Regionsunterstützung und Kontoregeln."],
"not_intro": "NotMeter ist ein **AION 2 DPS-Meter** eines Drittanbieters mit einer Website für Kampfaufzeichnungen und Ranglisten. Wähle vor einer Installation die benötigte Funktion: Charaktere und bestehende Aufzeichnungen suchst du im Web; neue Kämpfe zeichnet das Desktop-Tool auf.\n\n",
"not_title": "Web-Aufzeichnungen oder Schadensaufnahme am Desktop?",
"not_features": "| Ziel | Einstieg | Wichtige Bedingung |\n| --- | --- | --- |\n| Ausrüstung, Fertigkeiten oder Charakteraufzeichnungen finden | [NotMeter-Website](https://notmeter.com/) | KR, TW oder Global sowie richtigen Server und Namen wählen |\n| Bestehende Schadensaufzeichnungen vergleichen | Web-Filter für Kämpfe und Ranglisten | Boss, Schwierigkeit, Zeitraum und CP-Bereich abgleichen |\n| Eigene Kämpfe aufzeichnen | Desktop-Verteilung des Entwicklers | Vor Installation Region und Patch-Unterstützung prüfen |\n\n**Global:** Die Web-Charaktersuche ist verfügbar; aktuelle Desktop-Kompatibilität für Kampfaufzeichnungen ist unbestätigt. Eine Global-Suchoption macht eine ältere Desktop-Version nicht mit dem Global-Client kompatibel.\n\nDieser Guide behandelt NotMeters Einrichtung mit Npcap. OCR-Tools lesen Bildschirmtext und werden anders eingerichtet; vermische ihre Installationsschritte nicht mit NotMeter.\n\n",
"not_install": "1. Öffne [notmeter.com](https://notmeter.com/) und nutze den verlinkten [Npcap-Installer](https://npcap.com/), falls Npcap noch fehlt.\n2. Lade die NotMeter-ZIP über die verlinkten [Entwickler-Releases](https://github.com/Not4You-Dev/NotMeter-Releases/releases) herunter.\n3. Entpacke die ZIP in einen Ordner, bevor du `NotMeter.exe` startest; halte die enthaltenen Dateien zusammen.\n4. Prüfe Dienstregion und Patch-Unterstützung vor einer Kampfaufnahme. Wenn nichts aufgezeichnet wird, nutze die folgenden Prüfungen; erfolgreiche Installation allein bestätigt keine Kompatibilität.\n\n",
}}

for locale in LOCALES:
    t = TEXT[locale]
    for slug in SLUGS:
        for suffix in ("mdx", "json"):
            source = ROOT / "src/content" / locale / f"{slug}.{suffix}"
            target = OUT / "before" / locale / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                raise FileExistsError(target)
            shutil.copyfile(source, target)
    def read(slug):
        return (ROOT / "src/content" / locale / f"{slug}.mdx").read_text(encoding="utf-8")
    def save(slug, body, meta_key):
        (ROOT / "src/content" / locale / f"{slug}.mdx").write_text(body, encoding="utf-8")
        path = ROOT / "src/content" / locale / f"{slug}.json"
        metadata = json.loads(path.read_text(encoding="utf-8"))
        for key, value in zip(("title", "description", "summary", "quickAnswer"), t[meta_key]):
            metadata[key] = value
        return path, metadata
    def finish(path, metadata):
        path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    body = read("classes")
    anchor = '<h2 id="brawler-and-regional-guides">'
    addition = f'<h2 id="class-skills-and-gameplay">{t["skills_title"]}</h2>\n\n{t["skills"]}\n\n'
    body = body.replace(anchor, addition + anchor, 1)
    region = re.search(r'(<h2 id="brawler-and-regional-guides">.*?</h2>\n\n.*?\n\n)', body, re.S)
    assert region
    body = body[:region.end()] + t["brawler"] + "\n\n" + body[region.end():]
    path, meta = save("classes", body, "classes_meta")
    index = next(i for i, item in enumerate(meta["toc"]) if item["id"] == "brawler-and-regional-guides")
    meta["toc"].insert(index, {"id": "class-skills-and-gameplay", "title": t["skills_title"]})
    finish(path, meta)

    body = read("leveling")
    marker = {"en": "Keep three goals separate:", "ja": "**キャラクターレベル**", "es": "Mantén separados", "de": "Halte drei"}[locale]
    if marker not in body:
        paragraphs = body.split("\n\n")
        marker = paragraphs[3][:20]
    start = body.index(marker)
    body = f'<h2 id="global-leveling">{t["level_heading"]}</h2>\n\n{t["cap_intro"]}' + body[start:]
    body = body.replace('<GuideNext slug="builds" />', t["cap_faq"] + '<GuideNext slug="builds" />', 1)
    path, meta = save("leveling", body, "level_meta")
    meta["toc"][0]["title"] = t["level_heading"]
    finish(path, meta)

    body = read("download")
    requirements = re.search(r'(<h2 id="pc-requirements">.*?</h2>\n\n)', body)
    assert requirements
    body = body[:requirements.end()] + t["spec_scope"] + body[requirements.end():]
    body = body.replace('<h2 id="steam-installation">', f'<h2 id="check-your-specs">{t["spec_title"]}</h2>\n\n{t["spec_check"]}<h2 id="steam-installation">', 1)
    body = body.replace('<h2 id="launch-troubleshooting">', f'<h2 id="taiwan-client">{t["tw_title"]}</h2>\n\n{t["tw"]}<h2 id="launch-troubleshooting">', 1)
    path, meta = save("download", body, "download_meta")
    index = next(i for i, item in enumerate(meta["toc"]) if item["id"] == "steam-installation")
    meta["toc"].insert(index, {"id": "check-your-specs", "title": t["spec_title"]})
    index = next(i for i, item in enumerate(meta["toc"]) if item["id"] == "launch-troubleshooting")
    meta["toc"].insert(index, {"id": "taiwan-client", "title": t["tw_title"]})
    finish(path, meta)

    body = read("notmeter")
    body = t["not_intro"] + f'<h2 id="website-or-desktop">{t["not_title"]}</h2>\n\n{t["not_features"]}' + body[body.index('<h2 id="source-and-global-support">'):]
    installation = re.search(r'(<h2 id="maintainer-installation">.*?</h2>\n\n)(1\..*?)(?=Npcap)', body, re.S)
    assert installation
    body = body[:installation.start(2)] + t["not_install"] + body[installation.end(2):]
    path, meta = save("notmeter", body, "not_meta")
    meta["toc"].insert(0, {"id": "website-or-desktop", "title": t["not_title"]})
    finish(path, meta)

for slug in SLUGS:
    path = ROOT / "src/content/article-data" / f"{slug}.json"
    backup = OUT / "before/article-data" / path.name
    backup.parent.mkdir(parents=True, exist_ok=True)
    if backup.exists():
        raise FileExistsError(backup)
    shutil.copyfile(path, backup)
    article = json.loads(path.read_text(encoding="utf-8"))
    article["checkedAt"] = "2026-10-04"
    article["revision"] = "2026-10-04.keyword-refresh-1"
    if slug == "classes":
        for source in article["sources"]:
            if source["id"] == "global-classes":
                source["version"] = "Global official public about-en content, eight-class roster re-read 2026-10-04; gender restrictions and class-change process not established"
            if source["id"] == "chapter-one":
                source["version"] = "KR/TW Chapter 1: Brawler Gauntlets, Rage and Rampage re-read 2026-10-04; no Global availability date established"
    if slug == "download":
        if "TW" not in article["regions"]:
            article["regions"].append("TW")
        for source in article["sources"]:
            if source["id"] == "requirements":
                source["version"] = "Official Steam Global appdetails re-read successfully 2026-10-04; Windows-only listing, minimum/recommended and FHD presets unchanged"
            if source["id"] == "purple-region":
                source["version"] = "Official Global notice public article re-read 2026-10-04; five listed countries and launcher Global setting"
        article["sources"].extend([
            {"id": "tw-download", "title": "AION2 Taiwan official download and PURPLE installation", "url": "https://tw.ncsoft.com/aion2/download/index", "kind": "official", "region": "TW", "publishedAt": None, "version": "Taiwan official installer steps re-read 2026-10-04; foreign-account eligibility not established; regional configuration not copied into Global table"},
            {"id": "windows-spec-check", "title": "Microsoft basic display adapter in Windows", "url": "https://support.microsoft.com/en-us/windows/hardware/display-graphics/microsoft-basic-display-adapter-in-windows", "kind": "official", "region": "Mixed", "publishedAt": None, "version": "Microsoft Windows 10/11 DirectX Diagnostic Tool instructions re-read 2026-10-04"},
        ])
    if slug == "notmeter":
        for source in article["sources"]:
            if source["id"] == "notmeter-maintainer":
                source["version"] = "2026-10-04 maintainer website: KR/TW/Global website searches; Npcap then ZIP installation; desktop Global capture untested"
            if source["id"] == "notmeter-distribution":
                source["version"] = "Public GitHub releases API re-read 2026-10-04: v1.0.249, published 2026-08-29T00:37:48Z, empty release body; no Global compatibility statement"
            if source["id"] == "global-operation-policy":
                source["version"] = "Official Global operation policy re-read 2026-10-04; no specific NotMeter approval established"
    path.write_text(json.dumps(article, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("Updated four existing topics in four languages; historical content archived before edits.")
