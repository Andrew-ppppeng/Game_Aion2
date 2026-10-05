"""Apply reviewed four-language hub links and community resources once."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOCALES = ('en', 'ja', 'es', 'de')
def read(path):
    return path.read_text(encoding='utf-8')
def save(path, value):
    path.write_text(value, encoding='utf-8')
def json_save(path, value):
    save(path, json.dumps(value, ensure_ascii=False, indent=2) + '\n')

bridges = {
 'classes': [
  'For practical starting choices, compare the [Gladiator guide](/gladiator), [Ranger leveling guide](/ranger) and [Spiritmaster guide](/spiritmaster). Each separates its regional build examples from verified Global class information.',
  '序盤の選択は[グラディエーター](/gladiator)、[レンジャーの育成](/ranger)、[スピリット マスター](/spiritmaster)の各ガイドで比較できます。地域版の構成例と確認済みのGlobal職業情報を分けて説明しています。',
  'Para las primeras decisiones, compara las guías de [Gladiador](/gladiator), [Arquero para subir de nivel](/ranger) y [Espiritualista](/spiritmaster). Cada una distingue sus ejemplos regionales de la información de clase confirmada para Global.',
  'Vergleiche für den Einstieg die Guides zu [Gladiator](/gladiator), [Waldläufer beim Leveln](/ranger) und [Beschwörer](/spiritmaster). Sie trennen regionale Build-Beispiele von bestätigten Global-Klasseninformationen.'
 ],
 'builds': [
  'Use the dedicated [Gladiator](/gladiator), [Ranger](/ranger) and [Spiritmaster](/spiritmaster) pages for starting skill choices. The [built-in macro guide](/macro-guide) explains how to inspect skill combinations; [Notmeter](/notmeter) covers the third-party tool and its unverified Global compatibility. Neither tool establishes an optimal build by itself.',
  '序盤のスキル選択は[グラディエーター](/gladiator)、[レンジャー](/ranger)、[スピリット マスター](/spiritmaster)の専用ページへ。[ゲーム内マクロ](/macro-guide)ではスキル組み合わせの確認方法、[Notmeter](/notmeter)では外部ツールと未確認のGlobal互換性を説明します。ツールだけで最適構成が決まるわけではありません。',
  'Consulta [Gladiador](/gladiator), [Arquero](/ranger) y [Espiritualista](/spiritmaster) para elegir habilidades al empezar. La [guía de macros del juego](/macro-guide) explica cómo revisar combinaciones; [Notmeter](/notmeter) cubre la herramienta externa y su compatibilidad Global sin verificar. Ninguna herramienta demuestra por sí sola una configuración óptima.',
  'Nutze die eigenen Seiten zu [Gladiator](/gladiator), [Waldläufer](/ranger) und [Beschwörer](/spiritmaster) für die ersten Fertigkeitsentscheidungen. Der [Guide zu Spielmakros](/macro-guide) erklärt Fertigkeitskombinationen; [Notmeter](/notmeter) behandelt das externe Tool und seine ungeprüfte Global-Kompatibilität. Ein Tool allein belegt keinen optimalen Build.'
 ],
 'tier-list': [
  'Compare a ranking with the actual starting decisions in the [Gladiator](/gladiator), [Ranger](/ranger) and [Spiritmaster](/spiritmaster) guides before choosing. Their regional examples do not supply a measured Global tier order.',
  '選ぶ前に、順位と[グラディエーター](/gladiator)、[レンジャー](/ranger)、[スピリット マスター](/spiritmaster)の序盤ガイドを照らし合わせてください。地域版の例は、実測したGlobal順位を示すものではありません。',
  'Antes de elegir, contrasta las posiciones con las decisiones iniciales de las guías de [Gladiador](/gladiator), [Arquero](/ranger) y [Espiritualista](/spiritmaster). Sus ejemplos regionales no establecen una clasificación Global medida.',
  'Vergleiche vor der Auswahl eine Rangliste mit den Einstiegsentscheidungen für [Gladiator](/gladiator), [Waldläufer](/ranger) und [Beschwörer](/spiritmaster). Die regionalen Beispiele liefern keine gemessene Global-Rangfolge.'
 ],
 'character-creation': [
  'Before saving a character, use the [faction guide](/races) to check Elyos, Asmodian and grouping restrictions. A cosmetic preset does not change the faction and server choices that determine where you start.',
  'キャラクター保存前に[陣営ガイド](/races)でエリオス、アスモディアンとグループ制限を確認してください。外見プリセットは、開始先を決める陣営とサーバーの選択を変更しません。',
  'Antes de guardar el personaje, revisa Elíos, Asmodianos y las restricciones de grupo en la [guía de facciones](/races). Un preset de apariencia no cambia la facción ni el servidor que determinan dónde empiezas.',
  'Prüfe vor dem Speichern Elyos, Asmodier und Gruppenbeschränkungen im [Fraktionsguide](/races). Eine Aussehensvorlage ändert nicht die Fraktions- und Serverwahl für deinen Start.'
 ],
 'server': [
  'Read the [faction comparison](/races) before coordinating a group. For a later move, the [server-transfer guide](/server-transfer) records NC’s announced October 14 start, same-faction restriction and initial Early Access server limits; it is preparation for an announced feature, rather than an active transfer-menu walkthrough.',
  'グループの相談前に[陣営比較](/races)を確認してください。後で移動する場合は[サーバー移転ガイド](/server-transfer)にNC発表の10月14日開始予定、同陣営条件、初期の先行アクセスサーバー制限をまとめています。発表済み機能への準備であり、稼働中の移転メニュー手順ではありません。',
  'Lee la [comparación de facciones](/races) antes de coordinar un grupo. Para mudarte después, la [guía de transferencia](/server-transfer) recoge el inicio anunciado para el 14 de octubre, la misma facción y los límites iniciales de acceso anticipado. Sirve para preparar la función anunciada, no como recorrido de un menú de transferencia activo.',
  'Lies den [Fraktionsvergleich](/races), bevor ihr eine Gruppe plant. Der [Servertransfer-Guide](/server-transfer) nennt NCs angekündigten Start am 14. Oktober, die gleiche Fraktion und die anfänglichen Early-Access-Servergrenzen. Er bereitet auf die angekündigte Funktion vor und zeigt kein bereits aktives Transfermenü.'
 ],
 'steam': [
  'For SteamCharts, SteamDB and concurrent-player searches, use the [player-count guide](/player-count). It labels the observed Steam snapshot and explains why Steam concurrency does not equal every Global player.',
  'SteamCharts、SteamDB、同時接続数は[プレイヤー数ガイド](/player-count)へ。観測したSteamのスナップショットを明示し、Steam同時接続数とGlobal全体の人数が異なる理由を説明します。',
  'Para SteamCharts, SteamDB y jugadores simultáneos, consulta la [guía de población](/player-count). Identifica la captura observada de Steam y explica por qué no equivale a todos los jugadores Global.',
  'Für SteamCharts, SteamDB und gleichzeitige Spieler nutze den [Spielerzahlen-Guide](/player-count). Er kennzeichnet die beobachtete Steam-Momentaufnahme und erklärt, warum Steam nicht alle Global-Spieler zählt.'
 ]
}
community = [
 ('Community resources: Discord, Twitch, Reddit and Bahamut', '''Use the resource that fits the question, and check the post’s date and operating region before following its instructions.

| Resource | Best use | Region and authority |
| --- | --- | --- |
| [Official Global Discord](https://discord.gg/aion2official) | NC announcements, community events and bug reports | Official Global server, linked by [NC’s Steam developer post](https://steamcommunity.com/app/3393110/discussions/6/802345327968609673/) |
| [AION2Official on Twitch](https://www.twitch.tv/aion2official) | Official broadcasts | Official channel linked in the archived Global broadcast announcement; watch eligible creators for [Drops](/twitch-drops) |
| [r/Aion2 on Reddit](https://www.reddit.com/r/Aion2/) | Player questions, build discussions and community tools | Community posts; inspect whether advice concerns Global, KR or TW |
| [AION2 Bahamut board](https://forum.gamer.com.tw/B.php?bsn=82913) | Traditional Chinese player discussions | Taiwan community context; this check identified the board, but direct access returned 403, so no current Global instructions are endorsed from it |

For account problems, use [NC support](https://help.plaync.com/faq/aion2global). Community posts can suggest a diagnosis, but do not establish a current official rule. Include region, server, client and the exact message when asking for help; exclude passwords and account tokens.'''),
 ('コミュニティ：Discord・Twitch・Reddit・Bahamut', '''質問に合う場所を選び、手順を使う前に投稿の日付と運営地域を確認してください。

| リソース | 主な用途 | 地域と立場 |
| --- | --- | --- |
| [Global公式Discord](https://discord.gg/aion2official) | NCのお知らせ、イベント、不具合報告 | [Steamの開発者投稿](https://steamcommunity.com/app/3393110/discussions/6/802345327968609673/)が案内するGlobal公式サーバー |
| [TwitchのAION2Official](https://www.twitch.tv/aion2official) | 公式配信 | 保存済みGlobal配信告知の公式チャンネル。[Drops](/twitch-drops)は対象配信者を視聴 |
| [Redditのr/Aion2](https://www.reddit.com/r/Aion2/) | プレイヤーの質問、構成の議論、ツール | コミュニティ投稿。Global・KR・TWのどの情報か確認 |
| [BahamutのAION2掲示板](https://forum.gamer.com.tw/B.php?bsn=82913) | 繁体字中国語でのプレイヤー交流 | 台湾コミュニティ。掲示板は特定済みですが直接アクセスは403だったため、現在のGlobal手順はここから推奨していません |

アカウント問題は[NCサポート](https://help.plaync.com/faq/aion2global)へ。コミュニティの助言だけで現行公式ルールは確定しません。相談時は地域、サーバー、クライアント、表示されたメッセージを添え、パスワードやアカウントトークンは載せないでください。'''),
 ('Recursos: Discord, Twitch, Reddit y Bahamut', '''Elige el recurso según tu pregunta y comprueba la fecha y la región del servicio antes de seguir instrucciones.

| Recurso | Mejor uso | Región y autoridad |
| --- | --- | --- |
| [Discord oficial Global](https://discord.gg/aion2official) | Avisos de NC, eventos y errores | Servidor oficial Global enlazado por [el desarrollador en Steam](https://steamcommunity.com/app/3393110/discussions/6/802345327968609673/) |
| [AION2Official en Twitch](https://www.twitch.tv/aion2official) | Emisiones oficiales | Canal del anuncio Global archivado; mira a creadores elegibles para [Drops](/twitch-drops) |
| [r/Aion2 en Reddit](https://www.reddit.com/r/Aion2/) | Preguntas, configuraciones y herramientas de jugadores | Publicaciones comunitarias; distingue Global, KR y TW |
| [Foro AION2 de Bahamut](https://forum.gamer.com.tw/B.php?bsn=82913) | Conversaciones en chino tradicional | Comunidad taiwanesa; se identificó el foro, pero el acceso directo devolvió 403, así que no se avalan instrucciones Global actuales de él |

Para problemas de cuenta, usa [el soporte de NC](https://help.plaync.com/faq/aion2global). Un comentario puede orientar el diagnóstico, pero no confirma una regla oficial vigente. Al pedir ayuda, incluye región, servidor, cliente y mensaje exacto; excluye contraseñas y tokens de cuenta.'''),
 ('Community: Discord, Twitch, Reddit und Bahamut', '''Wähle die Ressource passend zur Frage und prüfe Datum sowie Betriebsregion, bevor du eine Anleitung übernimmst.

| Ressource | Geeignet für | Region und Zuständigkeit |
| --- | --- | --- |
| [Offizielles Global-Discord](https://discord.gg/aion2official) | NC-Mitteilungen, Events und Fehlermeldungen | Offizieller Global-Server, verlinkt im [Steam-Entwicklerbeitrag](https://steamcommunity.com/app/3393110/discussions/6/802345327968609673/) |
| [AION2Official auf Twitch](https://www.twitch.tv/aion2official) | Offizielle Übertragungen | Offizieller Kanal aus der archivierten Global-Ankündigung; für [Drops](/twitch-drops) berechtigte Creator ansehen |
| [r/Aion2 auf Reddit](https://www.reddit.com/r/Aion2/) | Spielerfragen, Builds und Community-Tools | Community-Beiträge; Global, KR und TW unterscheiden |
| [AION2-Forum bei Bahamut](https://forum.gamer.com.tw/B.php?bsn=82913) | Austausch auf traditionellem Chinesisch | Taiwan-Community; das Forum ist identifiziert, der Direktzugriff ergab jedoch 403. Deshalb werden daraus keine aktuellen Global-Anleitungen bestätigt |

Nutze bei Kontoproblemen den [NC-Support](https://help.plaync.com/faq/aion2global). Community-Beiträge helfen bei der Diagnose, belegen aber keine aktuelle offizielle Regel. Nenne Region, Server, Client und genaue Meldung; veröffentliche keine Passwörter oder Kontotokens.''')
]
timer = [
 'For other dated events, use the [code deadline](/code), [Twitch Drops campaigns](/twitch-drops) and [maintenance notices](/maintenance). Their countdowns refer to their own announced windows; they do not establish a recurring Rift opening.',
 '他の時限イベントは[コード期限](/code)、[Twitch Drops期間](/twitch-drops)、[メンテナンス告知](/maintenance)で確認できます。各カウントダウンはその発表期間を示し、裂け目の定期開放時刻を確定するものではありません。',
 'Para otros eventos con fecha, consulta el [plazo de códigos](/code), las [campañas Twitch Drops](/twitch-drops) y los [avisos de mantenimiento](/maintenance). Sus contadores corresponden a sus propios periodos anunciados; no fijan aperturas recurrentes de Grietas.',
 'Für andere datierte Ereignisse nutze die [Code-Frist](/code), [Twitch-Drops-Kampagnen](/twitch-drops) und [Wartungsmitteilungen](/maintenance). Ihre Countdown-Zeiten gelten für die jeweiligen angekündigten Zeitfenster und belegen keine wiederkehrende Rift-Öffnung.'
]
tw_names = ['official Taiwan download page', '台湾の公式ダウンロードページ', 'página oficial de descarga de Taiwán', 'offizielle Taiwan-Downloadseite']
old_tw_names = ['official Taiwan service', '台湾の公式サービス', 'servicio oficial de Taiwán', 'offiziellen Taiwan-Dienst']
for i, locale in enumerate(LOCALES):
    for slug, texts in bridges.items():
        path = ROOT / f'src/content/{locale}/{slug}.mdx'
        body = read(path)
        assert texts[i] not in body, (locale, slug, 'already applied')
        idx = body.rfind('<GuideNext ')
        assert idx >= 0, (locale, slug)
        save(path, body[:idx] + texts[i] + '\n\n' + body[idx:])
    path = ROOT / f'src/content/{locale}/guide.mdx'
    body = read(path)
    title, section = community[i]
    idx = body.rfind('<GuideNext ')
    assert 'id="community-resources"' not in body
    save(path, body[:idx] + f'<h2 id="community-resources">{title}</h2>\n\n{section}\n\n' + body[idx:])
    meta_path = path.with_suffix('.json')
    meta = json.loads(read(meta_path))
    meta['toc'].append({'id': 'community-resources', 'title': title})
    json_save(meta_path, meta)
    path = ROOT / f'src/content/{locale}/spacetime-rift.mdx'
    body = read(path)
    marker = '<GuideTimers />'
    assert body.count(marker) == 1
    save(path, body.replace(marker, timer[i] + '\n\n' + marker))
    path = ROOT / f'src/content/{locale}/steam.mdx'
    body = read(path).replace('https://tw.ncsoft.com/aion2/)', 'https://tw.ncsoft.com/aion2/download/index)')
    body = body.replace(old_tw_names[i], tw_names[i])
    save(path, body)

path = ROOT / 'src/content/class-identities.json'
entries = json.loads(read(path))
for entry in entries:
    if entry['id'] in ('gladiator', 'ranger', 'spiritmaster'):
        entry['href'] = '/' + entry['id']
json_save(path, entries)
for slug in [*bridges, 'guide', 'spacetime-rift']:
    path = ROOT / f'src/content/article-data/{slug}.json'
    data = json.loads(read(path))
    data['revision'] = '2026-10-03.seo-2'
    json_save(path, data)

path = ROOT / 'src/content/article-data/steam.json'
data = json.loads(read(path))
data['regions'] = ['Global', 'TW']
data['sources'].extend([
 {'id': 'global-ja-about', 'title': 'AION2 Japanese Global introduction', 'url': 'https://aion2.plaync.com/ja-jp/about/index', 'kind': 'official', 'region': 'Global', 'publishedAt': None, 'version': 'Japanese Global site; terminology captured 2026-10-02; regional distinction checked 2026-10-03'},
 {'id': 'tw-download', 'title': 'AION2 Taiwan official download', 'url': 'https://tw.ncsoft.com/aion2/download/index', 'kind': 'official', 'region': 'TW', 'publishedAt': None, 'version': 'Taiwan service download entry checked 2026-10-03; not Global platform or launch-date evidence'}
])
json_save(path, data)

path = ROOT / 'src/content/article-data/guide.json'
data = json.loads(read(path))
data['regions'] = list(dict.fromkeys(data['regions'] + ['Mixed']))
data['sources'].extend([
 {'id': 'official-discord-post', 'title': 'AION 2 Official Discord Server', 'url': 'https://steamcommunity.com/app/3393110/discussions/6/802345327968609673/', 'kind': 'official', 'region': 'Global', 'publishedAt': '2026-04-20', 'version': 'NC developer-pinned Discord invitation; checked 2026-10-03'},
 {'id': 'official-twitch', 'title': 'AION2Official Twitch channel', 'url': 'https://www.twitch.tv/aion2official', 'kind': 'official', 'region': 'Global', 'publishedAt': None, 'version': 'Channel linked by archived Global broadcast announcement in research/discord/aion2_news.json; no stream timetable inferred'},
 {'id': 'reddit-community', 'title': 'r/Aion2', 'url': 'https://www.reddit.com/r/Aion2/', 'kind': 'community', 'region': 'Mixed', 'publishedAt': None, 'version': 'Community resource index checked 2026-10-03; individual posts not official game rules'},
 {'id': 'bahamut-board', 'title': 'AION2 Bahamut board', 'url': 'https://forum.gamer.com.tw/B.php?bsn=82913', 'kind': 'community', 'region': 'TW', 'publishedAt': None, 'version': 'Board identity confirmed in indexed Bahamut post; direct board returned 403 on 2026-10-03; no current instructions extracted'}
])
json_save(path, data)
print('Four-language hub links, community resources, timer links and regional source labels updated.')
