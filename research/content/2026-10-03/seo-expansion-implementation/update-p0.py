"""Apply the manually authored, four-language P0 additions once."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOCALES = ('en', 'ja', 'es', 'de')

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def save_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def add_section(slug, section_id, titles, paragraphs, before):
    for locale in LOCALES:
        base = ROOT / 'src' / 'content' / locale
        path = base / f'{slug}.mdx'
        body = path.read_text(encoding='utf-8-sig')
        if f'id="{section_id}"' in body:
            raise RuntimeError(f'Section already exists: {locale}/{slug}/{section_id}')
        marker = f'<h2 id="{before}">'
        assert marker in body, (locale, slug, before)
        section = f'<h2 id="{section_id}">{titles[locale]}</h2>\n\n{paragraphs[locale].strip()}\n\n'
        path.write_text(body.replace(marker, section + marker, 1), encoding='utf-8')
        meta_path = base / f'{slug}.json'
        meta = read_json(meta_path)
        index = next(i for i, item in enumerate(meta['toc']) if item['id'] == before)
        meta['toc'].insert(index, {'id': section_id, 'title': titles[locale]})
        save_json(meta_path, meta)
    data_path = ROOT / 'src' / 'content' / 'article-data' / f'{slug}.json'
    data = read_json(data_path)
    data['revision'] = '2026-10-03.seo-1'
    save_json(data_path, data)

add_section('classes', 'class-icons', {
    'en': 'Class icons and names', 'ja': 'クラスアイコンと名称の対応',
    'es': 'Iconos y nombres de las clases', 'de': 'Klassen-Icons, Symbole und Namen',
}, {
    'en': 'Use this reference to identify an emblem in a class guide or screenshot. The English name stays visible when you switch language, so you can match another player’s build to the correct Global class.\n\n<GuideClassIcons />',
    'ja': '攻略やスクリーンショットにある紋章を確認するための一覧です。日本語名と英語名を並べているので、海外のビルドを読むときにもGlobal版のクラスを照合できます。\n\n<GuideClassIcons />',
    'es': 'Consulta esta lista para identificar un emblema en una guía o captura. El nombre inglés permanece visible al cambiar de idioma para relacionar el build de otro jugador con la clase correcta de Global.\n\n<GuideClassIcons />',
    'de': 'Mit dieser Übersicht erkennst du ein Klassensymbol in einem Guide oder Screenshot. Der englische Name bleibt neben dem deutschen sichtbar, damit du den Build eines anderen Spielers der richtigen Global-Klasse zuordnen kannst.\n\n<GuideClassIcons />',
}, 'choose-a-role')

add_section('steam', 'global-and-regional-versions', {
    'en': 'Global, Japan and Taiwan release information', 'ja': 'Global・日本・台湾のサービスを区別する',
    'es': 'Global, Japón y Taiwán: qué versión consultar', 'de': 'Global, Japan und Taiwan unterscheiden',
}, {
    'en': '''Choose the service before comparing release dates. The UTC schedule above is NC’s Global announcement; an earlier Korea or Taiwan guide may describe a different operating version.

| What you searched for | Which source to use |
| --- | --- |
| Global release date or release time | The Global opening and transition-maintenance schedule above |
| Japan release date | The [official Japanese Global site](https://aion2.plaync.com/ja-jp/about/index); its AION2 title and Japanese interface do not establish a separate launch date |
| Taiwan release or client | The [official Taiwan service](https://tw.ncsoft.com/aion2/); check its own client, account and announcements |

The announced Global public opening of October 5 at 13:00 UTC corresponds to October 5 at 22:00 JST. Treat this as an announced schedule, and check for changes before arranging a session. It does not establish a Taiwan opening time.

For pre-registration queries, use the current Global announcement rather than assuming an old campaign remains open. This guide has not confirmed an ongoing pre-registration campaign. Installing the game or registering an account does not itself establish Advanced Access eligibility. The paid access window and public free-to-play opening are separate in the [official access announcement](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ab85cc646be804931c31335).''',
    'ja': '''発売日を比べる前にサービス地域を確認しましょう。上のUTC日程はNCのGlobal版告知です。韓国や台湾の古い攻略が、別の運営バージョンを説明している場合があります。

| 検索した内容 | 確認する情報 |
| --- | --- |
| Global版の発売日・開始時刻 | 上の正式サービスと移行メンテナンスの日程 |
| 日本のサービス開始日 | [日本語のGlobal公式サイト](https://aion2.plaync.com/ja-jp/about/index)。AION2という表記や日本語対応だけで別の開始日が決まるわけではありません |
| 台湾版の開始日・クライアント | [台湾の公式サービス](https://tw.ncsoft.com/aion2/)。その地域のクライアント、アカウント、告知を確認します |

Global版の告知された正式開始時刻である10月5日13:00 UTCは、日本時間では10月5日22:00です。予定として扱い、プレイ前に変更の有無を確認してください。台湾版の開始時刻を示すものではありません。

事前登録を探している場合は、過去のキャンペーンが続いていると考えず、最新のGlobal告知を確認しましょう。本ガイドでは現在進行中の事前登録キャンペーンを確認していません。インストールやアカウント登録だけで先行アクセス権が得られるとは限りません。[公式アクセス告知](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ab85cc646be804931c31335)では、有料の先行期間と基本無料の正式開始が区別されています。''',
    'es': '''Elige el servicio antes de comparar fechas. El horario UTC de arriba corresponde al anuncio de NC para Global; una guía anterior de Corea o Taiwán puede describir otra versión en servicio.

| Qué buscaste | Qué fuente consultar |
| --- | --- |
| Fecha u hora de lanzamiento de Global | El horario de apertura pública y mantenimiento de transición de arriba |
| Fecha de lanzamiento en Japón | El [sitio oficial japonés de Global](https://aion2.plaync.com/ja-jp/about/index); el título AION2 y la interfaz japonesa no establecen una fecha de lanzamiento distinta |
| Lanzamiento o cliente de Taiwán | El [servicio oficial de Taiwán](https://tw.ncsoft.com/aion2/); revisa su cliente, cuenta y anuncios |

La apertura pública de Global anunciada para el 5 de octubre a las 13:00 UTC equivale al 5 de octubre a las 22:00 JST. Es un horario anunciado: comprueba posibles cambios antes de organizar una sesión. No establece una hora de apertura para Taiwán.

Si buscas el prerregistro, consulta el anuncio actual de Global en lugar de suponer que una campaña antigua sigue abierta. Esta guía no ha confirmado una campaña de prerregistro vigente. Instalar el juego o registrar una cuenta no demuestra por sí solo que tengas derecho al acceso anticipado. El periodo de acceso de pago y la apertura pública gratuita están separados en el [anuncio oficial de acceso](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ab85cc646be804931c31335).''',
    'de': '''Wähle zuerst den Dienst, bevor du Veröffentlichungstermine vergleichst. Der UTC-Zeitplan oben stammt aus NCs Global-Ankündigung; ein älterer Guide aus Korea oder Taiwan kann eine andere laufende Version beschreiben.

| Deine Suchanfrage | Passende Quelle |
| --- | --- |
| Global-Veröffentlichungsdatum oder Startzeit | Der Zeitplan für öffentlichen Start und Übergangswartung oben |
| Veröffentlichung in Japan | Die [offizielle japanische Global-Seite](https://aion2.plaync.com/ja-jp/about/index); der Titel AION2 und japanische Texte begründen keinen getrennten Veröffentlichungstermin |
| Veröffentlichung oder Client in Taiwan | Der [offizielle taiwanische Dienst](https://tw.ncsoft.com/aion2/); prüfe dessen Client, Konto und Ankündigungen |

Der angekündigte öffentliche Global-Start am 5. Oktober um 13:00 UTC entspricht dem 5. Oktober um 22:00 JST. Behandle dies als angekündigten Termin und prüfe Änderungen vor einer geplanten Sitzung. Daraus folgt keine Startzeit für Taiwan.

Suche bei Fragen zur Vorregistrierung nach der aktuellen Global-Ankündigung, statt eine alte Aktion als weiterhin offen anzusehen. Dieser Guide hat keine laufende Vorregistrierung bestätigt. Eine Installation oder Kontoregistrierung allein belegt keine Berechtigung für Advanced Access. Der kostenpflichtige Zugangszeitraum und der öffentliche Free-to-play-Start sind in der [offiziellen Zugangsankündigung](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ab85cc646be804931c31335) getrennt.''',
}, 'system-requirements')

add_section('steam', 'platform-and-controller-support', {
    'en': 'PS5, mobile and controller support', 'ja': 'PS5・モバイル・コントローラー対応',
    'es': 'PS5, móvil y compatibilidad con mando', 'de': 'PS5, Mobilgeräte und Controller',
}, {
    'en': '''The Global Steam product data checked on October 3 lists a Windows client. Choose that client for the requirements and installation instructions on this site.

| Platform or control option | What these Global sources establish |
| --- | --- |
| Windows PC | Listed Steam platform; Steam and PURPLE are the Global download choices |
| PS5 | No PS5 release is established by the Global PC sources checked here |
| Native iOS or Android client | Not established by these Global download sources; a PURPLE mobile app or remote-play feature is not the same as a native Global game client |
| Controller | The captured Steam categories do not list full or partial controller support; that absence does not establish that every controller mapping is impossible |

For a controller setup, check the current store compatibility labels and the actual in-game control options before relying on a mapping. Keyboard, mouse, menus and emergency skills all need to remain usable. This guide has not tested a Global controller configuration and does not present a KR/TW video as confirmation of Global support. [Official Steam listing](https://store.steampowered.com/app/3393110/AION_2/).''',
    'ja': '''10月3日に確認したGlobal版Steam製品データはWindowsクライアントを掲載しています。本サイトの動作環境とインストール手順は、そのクライアントを対象にしています。

| プラットフォーム・操作方法 | 確認したGlobal資料で分かること |
| --- | --- |
| Windows PC | Steam掲載プラットフォーム。Globalのダウンロード入口はSteamとPURPLEです |
| PS5 | 今回確認したGlobal PC向け資料ではPS5版の発売を確認していません |
| iOS・Androidのネイティブ版 | Globalのダウンロード資料では確認していません。PURPLEのモバイルアプリやリモート機能は、Global版ゲームのネイティブクライアントとは別です |
| コントローラー | 保存したSteamカテゴリには完全対応・部分対応の表示がありません。それだけで全てのキー割り当てが不可能とは言えません |

コントローラーを使う場合は、最新のストア表示と実際のゲーム内操作設定を先に確認してください。メニューや緊急スキルも含め、必要な操作を行えるかが重要です。本ガイドはGlobal版のコントローラー設定を実測しておらず、KR/TWの動画をGlobal対応の証拠として扱っていません。[公式Steamページ](https://store.steampowered.com/app/3393110/AION_2/)。''',
    'es': '''Los datos del producto de Steam para Global consultados el 3 de octubre muestran un cliente de Windows. Ese es el cliente al que se aplican los requisitos y pasos de instalación de este sitio.

| Plataforma o control | Qué confirman estas fuentes de Global |
| --- | --- |
| PC con Windows | Plataforma indicada en Steam; Steam y PURPLE son las opciones de descarga de Global |
| PS5 | Las fuentes de Global para PC consultadas aquí no establecen un lanzamiento en PS5 |
| Cliente nativo de iOS o Android | No está establecido por estas fuentes de descarga de Global; una aplicación móvil de PURPLE o una función remota no equivale a un cliente nativo del juego Global |
| Mando | Las categorías de Steam archivadas no indican compatibilidad total ni parcial con mando; esa ausencia no demuestra que todas las asignaciones sean imposibles |

Antes de depender de un mando, revisa las etiquetas actuales de la tienda y las opciones reales de control dentro del juego. También deben funcionar los menús y las habilidades de emergencia. Esta guía no ha probado una configuración de mando en Global ni presenta un vídeo de KR/TW como confirmación de compatibilidad con Global. [Página oficial de Steam](https://store.steampowered.com/app/3393110/AION_2/).''',
    'de': '''Die am 3. Oktober geprüften Steam-Produktdaten für Global führen einen Windows-Client auf. Auf diesen Client beziehen sich die Systemanforderungen und Installationsschritte dieser Seite.

| Plattform oder Steuerung | Aussage der geprüften Global-Quellen |
| --- | --- |
| Windows-PC | Auf Steam aufgeführte Plattform; Steam und PURPLE sind die Global-Downloadoptionen |
| PS5 | Die geprüften Global-PC-Quellen belegen keine PS5-Veröffentlichung |
| Nativer iOS- oder Android-Client | Durch diese Global-Downloadquellen nicht belegt; eine mobile PURPLE-App oder Fernspielfunktion ist nicht dasselbe wie ein nativer Global-Spielclient |
| Controller | Die archivierten Steam-Kategorien nennen weder vollständige noch teilweise Controller-Unterstützung; das beweist nicht, dass jede Tastenbelegung unmöglich ist |

Prüfe vor einer Controller-Konfiguration die aktuellen Store-Kennzeichnungen und die tatsächlichen Steuerungsoptionen im Spiel. Auch Menüs und Notfallfähigkeiten müssen bedienbar bleiben. Dieser Guide hat keine Global-Controller-Konfiguration getestet und verwendet kein KR/TW-Video als Bestätigung für Global-Unterstützung. [Offizielle Steam-Seite](https://store.steampowered.com/app/3393110/AION_2/).''',
}, 'supported-languages')

TITLES = {
    'classes': {'en': 'AION 2 Classes: Icons, Names and the Eight Global Roles', 'ja': 'AION2 クラス：8クラスのアイコン・名称・役割', 'es': 'Clases de AION 2: iconos, nombres y ocho funciones de Global', 'de': 'AION 2 Klassen: Icons, Symbole und acht Global-Rollen'},
    'chanter': {'en': 'AION 2 Chanter Build and Skills Guide', 'ja': 'AION2 チャンターのビルド・スキルガイド', 'es': 'Build y habilidades del Cantor en AION 2', 'de': 'AION 2 Kantor: Build und Fähigkeiten'},
    'map': {'en': 'AION 2 Interactive Map: Tools, Resources and Collectibles', 'ja': 'AION2 インタラクティブマップ：採集・収集品・使い方', 'es': 'Mapa interactivo de AION 2: recursos y coleccionables', 'de': 'AION 2 Interaktive Karte: Ressourcen und Sammelobjekte'},
    'maintenance': {'en': 'AION 2 Server Status and Maintenance: Official Updates', 'ja': 'AION2 サーバー状況・メンテナンス：公式告知を確認', 'es': 'Estado de servidores y mantenimiento de AION 2', 'de': 'AION 2 Serverstatus und Wartung: offizielle Meldungen'},
    'download': {'en': 'AION 2 Download: Steam, PURPLE and PC Requirements', 'ja': 'AION2 ダウンロード：Steam・PURPLE・PC動作環境', 'es': 'Descargar AION 2: Steam, PURPLE y requisitos de PC', 'de': 'AION 2 Download: Steam, PURPLE und PC-Anforderungen'},
    'monetization': {'en': 'Is AION 2 Free? Monetization and Founder’s Packs', 'ja': 'AION2 は基本無料？課金とファウンダーパック', 'es': '¿AION 2 es gratis? Monetización y paquetes de fundador', 'de': 'Ist AION 2 kostenlos? Monetarisierung und Gründerpakete'},
    'spacetime-rift': {'en': 'AION 2 Spacetime Rift: Timer, Global Schedule and PvP Entry', 'ja': 'AION2 時空の亀裂：タイマー・Global日程・PvP入口', 'es': 'Grieta espacio-temporal de AION 2: horario y temporizador', 'de': 'AION 2 Raumzeit-Riss: Timer, Global-Zeitplan und PvP'},
}

for slug, translations in TITLES.items():
    for locale, title in translations.items():
        path = ROOT / 'src' / 'content' / locale / f'{slug}.json'
        data = read_json(path)
        data['title'] = title
        if slug == 'classes':
            data['description'] = {
                'en': 'Identify the eight official Global class icons, match English and localized names, and compare combat roles, solo choices and regional Brawler guides.',
                'ja': 'Global版8クラスの公式アイコンと英語・日本語名を照合し、役割やソロ選択、地域別のブローラー情報を比較します。',
                'es': 'Identifica los ocho iconos oficiales de Global, compara nombres en inglés y español, funciones de combate, opciones en solitario y guías regionales del Brawler.',
                'de': 'Erkenne die acht offiziellen Global-Klassensymbole, vergleiche englische und deutsche Namen sowie Rollen, Solowahl und regionale Brawler-Guides.',
            }[locale]
        if slug == 'maintenance':
            data['summary'] = {
                'en': 'Check dated Global server and maintenance announcements, planned downtime and login fixes. These notice snapshots do not measure live server uptime.',
                'ja': '確認日時点のGlobalサーバー告知、予定メンテナンス、ログイン修正を確認できます。公式告知の記録であり、稼働状況のリアルタイム測定ではありません。',
                'es': 'Consulta anuncios fechados de Global, mantenimiento previsto y soluciones de acceso. Estas instantáneas de avisos no miden la disponibilidad del servidor en tiempo real.',
                'de': 'Prüfe datierte Global-Meldungen, geplante Wartung und Login-Korrekturen. Diese Ankündigungsstände messen keine Serververfügbarkeit in Echtzeit.',
            }[locale]
        save_json(path, data)
    shared = ROOT / 'src' / 'content' / 'article-data' / f'{slug}.json'
    data = read_json(shared)
    data['revision'] = '2026-10-03.seo-1'
    save_json(shared, data)

print('Applied sourced class-icon references, release/platform FAQs and focused metadata in four languages.')
