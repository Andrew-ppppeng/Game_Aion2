"""Add newly observed Google-result tools and verified launch account conditions."""
import ast
import json
import re
from pathlib import Path

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
tree = ast.parse((OUT / "apply-refresh.py").read_text(encoding="utf-8"))
TEXT = ast.literal_eval(next(node.value for node in tree.body if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "TEXT" for target in node.targets)))
EXTRA = {
"en": {
"tools_title": "Choose a DPS meter by capture method and region",
"tools": "| Tool | Method and setup | Region and cost conditions |\n| --- | --- | --- |\n| [NotMeter](https://notmeter.com/) | Website records; Npcap-dependent desktop capture | KR/TW/Global website search; current Global desktop compatibility unconfirmed |\n| [aion2t DPS Meter](https://github.com/Grachy/aion2t-dps-meter) | Windows network capture with Npcap | Global (EU) and TW release paths; some features require Premium |\n| [Aletheia](https://github.com/p62003/aletheia_AION2_DPS_Meter) | Windows network capture with Npcap; English and Chinese interfaces | TW-focused; free overlay and Sponsor features; Discord sign-in and report-upload consent required |\n| [Projack OCR meter](https://github.com/ProjackL2/aion2_dps_meter) | Screenshots of the combat log; Windows, Python 3.12 and Tesseract | Large UI and Aion 1 control mode required; current Global compatibility unconfirmed |\n\n**Free does not mean every feature is included.** Aletheia's basic overlay does not require a Sponsor key; advanced analysis does. Its free tier automatically uploads eligible reports after consent. Review each tool's current feature and data-sharing settings before use.\n\nFor OCR, keep the combat log visible at the size and position configured in the tool. Changes to log language, UI scale or window position can affect text recognition. For network capture, confirm the release supports your service region and game patch. Downloadable third-party tools do not carry NC approval simply because they avoid changing game files.\n\n",
"steam_account": "**Steam account:** you do not need to link a PURPLE account to play through Steam. Link accounts only if you want the same character and progress in both launchers; both use the same Global content and servers.\n\n",
"tw_progress": "**TW/KR progress does not transfer to Global.** Choose the service you want before creating a character.\n\n",
},
"ja": {
"tools_title": "記録方式と地域でDPSメーターを選ぶ",
"tools": "| ツール | 記録方式と導入環境 | 地域・料金の条件 |\n| --- | --- | --- |\n| [NotMeter](https://notmeter.com/) | Web記録、Npcapを使うデスクトップ記録 | KR/TW/GlobalのWeb検索。現行Globalのデスクトップ互換性は未確認 |\n| [aion2t DPS Meter](https://github.com/Grachy/aion2t-dps-meter) | WindowsでNpcapによるネットワーク記録 | Global（EU）とTW向けのリリース。一部機能はPremium |\n| [Aletheia](https://github.com/p62003/aletheia_AION2_DPS_Meter) | WindowsとNpcap。英語・中国語の表示 | TW向け。無料オーバーレイとSponsor機能。Discordログインとレポート送信への同意が必要 |\n| [Projack OCR meter](https://github.com/ProjackL2/aion2_dps_meter) | 戦闘ログの画面撮影。Windows、Python 3.12、Tesseract | 大きいUIとAion 1操作モードが必要。現行Globalの互換性は未確認 |\n\n**無料でも全機能が含まれるとは限りません。** Aletheiaの基本オーバーレイにSponsorキーは不要ですが、高度な分析には必要です。無料版は同意後に対象レポートを自動送信します。利用前に、各ツールの現在の機能とデータ共有設定を確認しましょう。\n\nOCRでは、設定した大きさと位置で戦闘ログを表示します。ログ言語、UI倍率、ウィンドウ位置の変更は文字認識に影響します。ネットワーク記録ではサービス地域とパッチへの対応を確認してください。ゲームファイルを変えない第三者ツールでも、それだけでNCの承認を受けていることにはなりません。\n\n",
"steam_account": "**Steamアカウント：** Steamで遊ぶためにPURPLEアカウントを連携する必要はありません。両方のランチャーで同じキャラクターと進行を使いたい場合に連携します。Globalの内容とサーバーは共通です。\n\n",
"tw_progress": "**TW/KRの進行はGlobalに移りません。** キャラクター作成前に遊ぶサービスを選びましょう。\n\n",
},
"es": {
"tools_title": "Elige un DPS meter por método y región",
"tools": "| Herramienta | Método y configuración | Condiciones de región y coste |\n| --- | --- | --- |\n| [NotMeter](https://notmeter.com/) | Registros web y captura de escritorio con Npcap | Búsqueda web KR/TW/Global; compatibilidad actual de escritorio Global sin confirmar |\n| [aion2t DPS Meter](https://github.com/Grachy/aion2t-dps-meter) | Captura de red Windows con Npcap | Versiones para Global (EU) y TW; algunas funciones requieren Premium |\n| [Aletheia](https://github.com/p62003/aletheia_AION2_DPS_Meter) | Captura de red Windows con Npcap; interfaz inglesa y china | Enfocado en TW; overlay gratuito y funciones Sponsor; exige Discord y consentimiento de subida de informes |\n| [Projack OCR meter](https://github.com/ProjackL2/aion2_dps_meter) | Capturas del registro de combate; Windows, Python 3.12 y Tesseract | Requiere UI grande y controles Aion 1; compatibilidad actual Global sin confirmar |\n\n**Gratis no significa que incluya todas las funciones.** El overlay básico de Aletheia no necesita clave Sponsor; el análisis avanzado sí. Su modalidad gratuita sube automáticamente informes aptos tras el consentimiento. Revisa funciones y ajustes actuales de intercambio de datos antes de usar cada herramienta.\n\nPara OCR, mantén visible el registro con el tamaño y la posición configurados. Cambiar idioma, escala de UI o posición puede afectar al reconocimiento. Para captura de red, comprueba que la versión admite tu región y parche. Un programa de terceros no tiene aprobación de NC solo por no modificar archivos del juego.\n\n",
"steam_account": "**Cuenta Steam:** no necesitas vincular una cuenta PURPLE para jugar desde Steam. Vincúlalas si quieres usar el mismo personaje y progreso en ambos lanzadores; comparten contenido y servidores Global.\n\n",
"tw_progress": "**El progreso TW/KR no se transfiere a Global.** Elige el servicio antes de crear un personaje.\n\n",
},
"de": {
"tools_title": "Wähle ein DPS-Meter nach Methode und Region",
"tools": "| Tool | Methode und Einrichtung | Regions- und Kostenbedingungen |\n| --- | --- | --- |\n| [NotMeter](https://notmeter.com/) | Web-Aufzeichnungen; Desktop-Aufnahme mit Npcap | KR/TW/Global-Websuche; aktuelle Global-Desktop-Kompatibilität unbestätigt |\n| [aion2t DPS Meter](https://github.com/Grachy/aion2t-dps-meter) | Windows-Netzwerkaufnahme mit Npcap | Releases für Global (EU) und TW; einige Funktionen benötigen Premium |\n| [Aletheia](https://github.com/p62003/aletheia_AION2_DPS_Meter) | Windows-Netzwerkaufnahme mit Npcap; englische und chinesische Oberfläche | Auf TW ausgerichtet; kostenloses Overlay und Sponsor-Funktionen; Discord-Anmeldung und Zustimmung zum Berichtupload erforderlich |\n| [Projack OCR meter](https://github.com/ProjackL2/aion2_dps_meter) | Screenshots des Kampflogs; Windows, Python 3.12 und Tesseract | Große UI und Aion-1-Steuerungsmodus erforderlich; aktuelle Global-Kompatibilität unbestätigt |\n\n**Kostenlos bedeutet nicht, dass jede Funktion enthalten ist.** Aletheias Basis-Overlay braucht keinen Sponsor-Schlüssel, die erweiterte Analyse dagegen schon. Der kostenlose Tarif lädt nach Zustimmung geeignete Berichte automatisch hoch. Prüfe aktuelle Funktionen und Datenfreigabeeinstellungen vor der Nutzung.\n\nFür OCR bleibt das Kampflog in der eingestellten Größe und Position sichtbar. Änderungen an Sprache, UI-Skalierung oder Fensterposition können die Erkennung beeinflussen. Für Netzwerkaufnahme prüfst du Dienstregion und Patch-Unterstützung. Ein Drittanbieter-Tool ist nicht schon deshalb von NC genehmigt, weil es keine Spieldateien ändert.\n\n",
"steam_account": "**Steam-Konto:** Zum Spielen über Steam brauchst du kein verknüpftes PURPLE-Konto. Verknüpfe sie, wenn du denselben Charakter und Fortschritt in beiden Launchern verwenden möchtest; Global-Inhalte und Server sind gleich.\n\n",
"tw_progress": "**TW/KR-Fortschritt wird nicht nach Global übertragen.** Wähle den Dienst vor der Charaktererstellung.\n\n",
}}

for locale, t in EXTRA.items():
    path = ROOT / "src/content" / locale / "notmeter.mdx"
    body = path.read_text(encoding="utf-8")
    original = (OUT / "before" / locale / "notmeter.mdx").read_text(encoding="utf-8")
    section = re.search(r'<h2 id="maintainer-installation">.*?</h2>\n\n(.*?)(?=<h2 id="read-combat-records">)', original, re.S)
    assert section
    explanation = section.group(1).split("\n\n", 1)[1].strip()
    body = re.sub(r'(<h2 id="maintainer-installation">.*?</h2>\n\n).*?(?=<h2 id="read-combat-records">)', lambda m: m.group(1) + TEXT[locale]["not_install"] + explanation + "\n\n", body, count=1, flags=re.S)
    anchor = '<h2 id="source-and-global-support">'
    body = body.replace(anchor, f'<h2 id="dps-meter-options">{t["tools_title"]}</h2>\n\n{t["tools"]}' + anchor, 1)
    path.write_text(body, encoding="utf-8")
    meta_path = path.with_suffix(".json")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    meta["toc"].insert(1, {"id": "dps-meter-options", "title": t["tools_title"]})
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    path = ROOT / "src/content" / locale / "download.mdx"
    body = path.read_text(encoding="utf-8")
    heading = re.search(r'(<h2 id="steam-installation">.*?</h2>\n\n)', body)
    assert heading
    body = body[:heading.end()] + t["steam_account"] + body[heading.end():]
    heading = re.search(r'(<h2 id="taiwan-client">.*?</h2>\n\n)', body)
    assert heading
    body = body[:heading.end()] + t["tw_progress"] + body[heading.end():]
    path.write_text(body, encoding="utf-8")

    path = ROOT / "src/content" / locale / "classes.mdx"
    body = path.read_text(encoding="utf-8")
    paragraphs = body.split("\n\n")
    duplicate = next(i for i, paragraph in enumerate(paragraphs) if i > len(paragraphs) - 5 and paragraph.count("/gladiator") and paragraph.count("/ranger") and paragraph.count("/spiritmaster"))
    paragraphs.pop(duplicate)
    path.write_text("\n\n".join(paragraphs), encoding="utf-8")

path = ROOT / "src/content/article-data/notmeter.json"
article = json.loads(path.read_text(encoding="utf-8"))
article["sources"].extend([
    {"id": "aletheia-maintainer", "title": "Aletheia maintainer README", "url": "https://github.com/p62003/aletheia_AION2_DPS_Meter", "kind": "tool", "region": "TW", "publishedAt": None, "version": "2026-10-04 README: Windows/Npcap, TW, free/Sponsor, mandatory Discord/report consent; Global display mode is not Global server support; no executable run"},
    {"id": "ocr-maintainer", "title": "ProjackL2 AION 2 OCR DPS meter", "url": "https://github.com/ProjackL2/aion2_dps_meter", "kind": "tool", "region": "Mixed", "publishedAt": None, "version": "2026-10-04 README: screenshot combat-log OCR, Windows/Python 3.12/Tesseract, large UI/Aion1 controls; current Global compatibility not established; no dependencies installed"},
    {"id": "aion2t-meter-maintainer", "title": "aion2t DPS meter maintainer README", "url": "https://github.com/Grachy/aion2t-dps-meter", "kind": "tool", "region": "Global/TW", "publishedAt": None, "version": "2026-10-04 README: Windows/Npcap, Global(EU) release fixes and TW; Premium functions; maintainer support statement only, desktop not tested"},
])
path.write_text(json.dumps(article, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

path = ROOT / "src/content/article-data/download.json"
article = json.loads(path.read_text(encoding="utf-8"))
article["sources"].append({"id": "launch-faq", "title": "AION 2 Global Launch FAQ", "url": "https://store.steampowered.com/news/app/3393110?emclan=103582791475596239&emgid=680761758839734961", "kind": "official", "region": "Global", "publishedAt": "2026-10-01", "version": "Steam official ISteamNews Launch FAQ re-read 2026-10-04 by secondary-updates: Steam/PURPLE link optional for Steam-only play, same character cross-launcher requires link, TW/KR progress not transferred; raw log preserved in adjacent agent directory"})
path.write_text(json.dumps(article, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Applied primary-source and Google-result follow-ups.")
