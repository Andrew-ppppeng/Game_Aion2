"""Create four localized transfer-preparation guides from NC's announcement."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
URL = 'https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2'
PAIR = 'https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939'
SLUG = 'server-transfer'
IDS = ['confirmed-transfer-rules', 'choose-a-destination', 'prepare-your-information', 'unannounced-details', 'check-at-opening']

DATA = {
'en': {
 'title': 'AION 2 Server Transfer: Date, Free Period and Global Rules',
 'description': 'Prepare for AION 2 Global server transfers: announced October 14 start, same-faction limits, Early Access restrictions and details still to check.',
 'summary': 'NC plans Global server transfers from October 14, initially free and within the same faction. Early Access characters are initially restricted to Early Access servers. This is a preparation guide; the announcement does not supply a transfer-menu walkthrough.',
 'heads': ['Confirmed Global transfer rules', 'Choose a destination before the opening', 'Prepare the information you will need', 'Details the announcement has not supplied', 'What to check when transfers open'],
 'visual': ['Prepare a transfer decision', 'Use the published conditions to shortlist a server, then verify the actual transfer screen when the feature opens.', [('Identify your current server', 'Write down your region, faction and whether it is an Early Access server.'), ('Check a destination', 'Compare the exact server name, faction and access pool with the announcement.'), ('Recheck at opening', 'Read the current notice and confirmation screen before starting a move.')]],
 'body': '''NC’s [Global transfer announcement]({url}) sets out an opening plan and initial restrictions. The notice was checked on October 3, 2026, before the announced start. It does not show that the feature is already available, and this page does not invent a menu, transfer duration or cooldown.

<h2 id="confirmed-transfer-rules">Confirmed Global transfer rules</h2>

| Question | Published condition |
| --- | --- |
| When are transfers planned to start? | October 14, 2026; no exact opening hour in this announcement |
| Can a move change faction? | The announced moves are within the same faction |
| Can Early Access players move to public-launch servers immediately? | Initially, Early Access players may transfer only between Early Access servers |
| What is the initial charge? | Transfers are initially free; the notice gives no end date for that period |
| Do friends need a transfer just to enter a dungeon together? | NC says instanced content, including dungeons, is available across servers |

Read those conditions together. “Free” concerns the initial charge; it does not remove the faction and Early Access restrictions. A planned date without an hour is not a verified midnight opening in your country. Use the [official notice]({url}) for subsequent changes.

<GuideVisual id="workflow" />

<h2 id="choose-a-destination">Choose a destination before the opening</h2>

Agree on an exact region, faction and server name with your group using the [server list](/server). NC’s [matchmaking explanation]({pair}) distinguishes your home server from its temporary opposing-faction partner. Moving within your faction is not the same as moving to that opposing server or switching to its faction.

Keep the two questions separate: where do you want your character to live, and which group activity are you trying to join? The transfer announcement explicitly mentions cross-server instances. It does not describe every party, guild or open-world restriction, so confirm the requirement for the activity you actually want instead of moving solely because two server names differ.

<h2 id="prepare-your-information">Prepare the information you will need</h2>

1. Record the character’s current region, faction and exact server name.
2. Record the destination your group agreed on, including its faction and access pool.
3. Reopen the transfer announcement and look for a later revision or a new eligibility notice.
4. Keep a note of the reason for moving: playing on the same home server, joining an organization, or another specific need.
5. At opening, read the actual destination selector and confirmation before committing.

This is a preparation checklist, not a claimed list of in-game eligibility fields. If a server is absent from the selector, its appearance on an old roster does not establish that it accepts transfers. Compare your [account and client identity](/steam) with the character you intend to move if the displayed roster is unexpected.

<h2 id="unannounced-details">Details the announcement has not supplied</h2>

The checked notice does not specify a menu path, exact opening hour, processing time, cooldown, cross-region permission, name-conflict handling, or the treatment of guild membership, mail and market listings. It also does not give an end date for free transfers. None of these fields should be filled with KR/TW rules or assumptions from another NC game.

Prepare questions about any of those details that matter to your character. When the feature opens, read the current instructions and the confirmation messages that apply to your move. A free initial offer is useful information, but it is not a reason to ignore an unresolved destination or character condition.

<h2 id="check-at-opening">What to check when transfers open</h2>

Check the latest [official announcements](https://aion2.plaync.com/en-us/board/notice/list) and [maintenance notices](/maintenance) first. An announced opening date and a scheduled maintenance window are different pieces of information. A countdown reaching a date is not proof that a transfer service is operating.

Use only the instructions applicable to Global and your current access pool. After NC publishes the actual interface and restrictions, this guide can add the confirmed operation sequence. Until then, use the conditions above to make a shortlist and keep the original notice available for comparison.

<GuideNext slug="server" />''',
},
'ja': {
 'title': 'AION2 サーバー移動：開始予定・無料期間・Globalの条件',
 'description': 'Global版のサーバー移動に備え、10月14日の開始予定、同じ種族の制限、先行サーバーの条件と未告知の詳細を確認します。',
 'summary': 'NCは10月14日から同じ種族内のサーバー移動を予定し、当初は無料と告知しています。先行アクセスのプレイヤーは当初、先行サーバー同士に制限されます。本稿は準備ガイドであり、未公開の移動メニューを推測した手順ではありません。',
 'heads': ['告知で確認できるGlobalの移動条件', '開始前に移動先を決める', '必要な情報を整理する', 'まだ告知されていない詳細', '開始時に確認すること'],
 'visual': ['移動先を選ぶための準備', '告知の条件で候補を絞り、機能開始後に実際の移動画面を確認します。', [('現在のサーバーを確認', '地域、種族、先行アクセスサーバーかどうかを記録します。'), ('移動先を照合', '正確なサーバー名、種族、アクセス区分を告知と比較します。'), ('開始時に再確認', '最新の告知と確認画面を読んでから移動を始めます。')]],
 'body': '''NCの[Global版サーバー移動告知]({url})には、開始予定と当初の制限が掲載されています。告知は予定日の前である2026年10月3日に確認しました。機能がすでに使えることを示すものではなく、本稿はメニュー、所要時間、クールダウンを推測しません。

<h2 id="confirmed-transfer-rules">告知で確認できるGlobalの移動条件</h2>

| 質問 | 公表された条件 |
| --- | --- |
| 開始予定はいつ？ | 2026年10月14日。この告知には正確な開始時刻がありません |
| 移動で種族を変えられる？ | 告知されている移動は同じ種族内です |
| 先行アクセスから正式開始サーバーへすぐ移れる？ | 当初、先行アクセスのプレイヤーは先行サーバー同士に制限されます |
| 最初の料金は？ | 当初は無料。無料期間の終了日は記載されていません |
| 一緒にダンジョンへ行くだけでも移動が必要？ | NCはダンジョンを含むインスタンス型コンテンツがサーバーをまたいで利用可能と説明しています |

条件はまとめて読みましょう。「無料」は当初の料金についての説明で、種族や先行アクセスの制限がなくなる意味ではありません。時刻のない予定日を、日本時間の午前0時開始と考えることもできません。変更は[公式告知]({url})で確認してください。

<GuideVisual id="workflow" />

<h2 id="choose-a-destination">開始前に移動先を決める</h2>

[サーバー一覧](/server)を使い、仲間と地域、種族、正確なサーバー名を合わせましょう。NCの[マッチング説明]({pair})では、自分のサーバーと期間限定で対戦する相手種族のサーバーが区別されています。同じ種族内で移ることは、敵側のサーバーへ移ったり種族を変えたりすることとは別です。

「キャラクターをどこに所属させたいか」と「どのグループ活動に参加したいか」を分けて考えましょう。移動告知はサーバーをまたぐインスタンスについて明記していますが、全てのパーティー、レギオン、オープンワールドの制限を説明しているわけではありません。サーバー名が違うという理由だけで決めず、参加したい活動の条件を確認してください。

<h2 id="prepare-your-information">必要な情報を整理する</h2>

1. 現在の地域、種族、正確なサーバー名を記録します。
2. 仲間と決めた移動先について、種族とアクセス区分も記録します。
3. 移動告知を開き直し、改訂や新しい利用条件の告知を探します。
4. 同じ拠点サーバーで遊ぶ、組織へ参加するなど、移動の目的を具体的に書きます。
5. 機能開始後、移動先選択と確認画面を読んでから確定します。

これは準備用のチェックリストで、ゲーム内の利用条件を断定した一覧ではありません。古いサーバー表に載っていても、選択画面にない移動先が受け入れ可能とは限りません。表示されるキャラクターが予想と違う場合は、[アカウントとクライアント](/steam)を移動したいキャラクターのものと照合しましょう。

<h2 id="unannounced-details">まだ告知されていない詳細</h2>

確認した告知にはメニューの場所、開始時刻、処理時間、クールダウン、地域をまたぐ移動の可否、名前の重複処理、レギオン・メール・取引出品の扱いが記載されていません。無料期間の終了日も不明です。KR/TWのルールや別のNC作品の仕様で補うことはできません。

自分のキャラクターに関係する項目を質問としてまとめておきましょう。機能開始後は、実際の移動に適用される最新の説明と確認メッセージを読みます。当初無料という情報だけを理由に、未確認の移動先やキャラクター条件を省略しないでください。

<h2 id="check-at-opening">開始時に確認すること</h2>

まず[最新の公式告知](https://aion2.plaync.com/en-us/board/notice/list)と[メンテナンス告知](/maintenance)を確認します。機能の開始予定日とメンテナンス予定時間は別の情報です。日付までのカウントダウンが終わっても、移動サービスが稼働した証拠にはなりません。

Global版と自分のアクセス区分に適用される説明を使いましょう。NCが実際の画面と制限を公開した後、本ガイドにも確認済みの操作手順を追加できます。それまでは上の条件で候補を絞り、元の告知を比較用に残してください。

<GuideNext slug="server" />''',
},
'es': {
 'title': 'Transferencia de servidor en AION 2: fecha y reglas de Global',
 'description': 'Prepara tu transferencia de servidor en AION 2 Global: inicio anunciado el 14 de octubre, gratuidad inicial, misma facción y límites del acceso anticipado.',
 'summary': 'NC prevé transferencias en Global desde el 14 de octubre, inicialmente gratuitas y dentro de la misma facción. Al principio, los jugadores de acceso anticipado solo podrán pasar entre esos servidores. Esta guía prepara la elección; el anuncio no incluye un recorrido por el menú de transferencia.',
 'heads': ['Reglas de Global confirmadas', 'Elige el destino antes de la apertura', 'Prepara la información necesaria', 'Detalles que el anuncio no ha publicado', 'Qué revisar cuando se abran las transferencias'],
 'visual': ['Prepara la decisión de transferencia', 'Filtra destinos con las condiciones publicadas y revisa la pantalla real cuando se active la función.', [('Identifica tu servidor actual', 'Anota región, facción y si es un servidor de acceso anticipado.'), ('Comprueba el destino', 'Compara nombre exacto, facción y grupo de acceso con el anuncio.'), ('Revisa al abrirse', 'Lee el aviso actual y la confirmación antes de iniciar el traslado.')]],
 'body': '''El [anuncio de transferencias de Global de NC]({url}) explica el inicio previsto y las restricciones iniciales. Se consultó el 3 de octubre de 2026, antes de la fecha anunciada. No demuestra que la función ya esté disponible, y esta página no inventa un menú, una duración ni un tiempo de espera entre traslados.

<h2 id="confirmed-transfer-rules">Reglas de Global confirmadas</h2>

| Pregunta | Condición publicada |
| --- | --- |
| ¿Cuándo se prevé el inicio? | El 14 de octubre de 2026; el anuncio no da una hora exacta |
| ¿Puede cambiar la facción? | Los traslados anunciados son dentro de la misma facción |
| ¿Puede el acceso anticipado pasar directamente a servidores de lanzamiento público? | Al principio solo se permite trasladarse entre servidores de acceso anticipado |
| ¿Cuál es el coste inicial? | Inicialmente es gratis; no se indica cuándo termina ese periodo |
| ¿Hace falta trasladarse solo para entrar juntos en una mazmorra? | NC indica que el contenido instanciado, incluidas las mazmorras, está disponible entre servidores |

Lee las condiciones juntas. «Gratis» describe el coste inicial; no elimina los límites de facción ni de acceso anticipado. Una fecha sin hora tampoco confirma una apertura a medianoche en tu país. Consulta los cambios en el [aviso oficial]({url}).

<GuideVisual id="workflow" />

<h2 id="choose-a-destination">Elige el destino antes de la apertura</h2>

Acuerda con tu grupo región, facción y nombre exacto usando la [lista de servidores](/server). La [explicación oficial del emparejamiento]({pair}) distingue tu servidor del rival de la otra facción, que puede cambiar con el tiempo. Un traslado dentro de tu facción no equivale a pasar a ese servidor rival ni a cambiar de facción.

Separa dos preguntas: dónde quieres que resida tu personaje y qué actividad de grupo quieres realizar. El anuncio menciona expresamente las instancias entre servidores. No describe todas las restricciones de grupos, organizaciones o mundo abierto; confirma la condición de tu actividad en vez de trasladarte solo porque los nombres de servidor sean distintos.

<h2 id="prepare-your-information">Prepara la información necesaria</h2>

1. Anota la región, facción y nombre exacto del servidor actual.
2. Anota el destino acordado, incluida su facción y grupo de acceso.
3. Vuelve al anuncio y busca una revisión o nuevas condiciones de elegibilidad.
4. Escribe el motivo concreto: compartir servidor habitual, entrar en una organización u otra necesidad.
5. Cuando se active la función, lee el selector de destino y la confirmación antes de aceptar.

Esta es una lista de preparación, no una lista confirmada de requisitos dentro del juego. Que un servidor figure en una tabla antigua no demuestra que acepte traslados si no aparece en el selector. Si los personajes mostrados no son los esperados, compara la [identidad de cuenta y cliente](/steam) con la del personaje que quieres mover.

<h2 id="unannounced-details">Detalles que el anuncio no ha publicado</h2>

El aviso consultado no especifica ruta del menú, hora de apertura, duración del proceso, tiempo entre transferencias, permiso entre regiones, conflictos de nombres ni tratamiento de organizaciones, correo o anuncios del mercado. Tampoco da una fecha final de gratuidad. No rellenes esos huecos con reglas de KR/TW o de otro juego de NC.

Prepara preguntas sobre los detalles que afecten a tu personaje. Al abrirse la función, lee las instrucciones vigentes y los mensajes de confirmación aplicables a tu traslado. La oferta inicial gratuita es información útil, pero no resuelve una condición pendiente del personaje o del destino.

<h2 id="check-at-opening">Qué revisar cuando se abran las transferencias</h2>

Consulta primero los [anuncios oficiales recientes](https://aion2.plaync.com/en-us/board/notice/list) y los [avisos de mantenimiento](/maintenance). La fecha prevista de una función y una ventana de mantenimiento son datos distintos. Que una cuenta atrás llegue a su fecha no demuestra que el servicio de traslado esté funcionando.

Usa instrucciones aplicables a Global y a tu grupo de acceso actual. Cuando NC publique la interfaz y los límites reales, esta guía podrá añadir los pasos confirmados. Hasta entonces, utiliza las condiciones para elegir candidatos y conserva el aviso original como referencia.

<GuideNext slug="server" />''',
},
'de': {
 'title': 'AION 2 Servertransfer: Termin, kostenlose Phase und Global-Regeln',
 'description': 'Bereite den Global-Servertransfer vor: angekündigter Start am 14. Oktober, kostenlose Anfangsphase, gleiche Fraktion und Einschränkungen für Advanced Access.',
 'summary': 'NC plant Global-Servertransfers ab dem 14. Oktober, zunächst kostenlos und innerhalb derselben Fraktion. Advanced-Access-Spieler sind anfangs auf Advanced-Access-Server beschränkt. Dies ist ein Vorbereitungs-Guide; die Ankündigung enthält keine Anleitung für das Transfermenü.',
 'heads': ['Bestätigte Global-Transferregeln', 'Wähle das Ziel vor dem Start', 'Bereite deine Angaben vor', 'Noch nicht veröffentlichte Einzelheiten', 'Was du beim Start prüfen solltest'],
 'visual': ['Bereite die Transferentscheidung vor', 'Grenze Ziele anhand der veröffentlichten Bedingungen ein und prüfe das tatsächliche Transferfenster nach dem Start.', [('Aktuellen Server bestimmen', 'Notiere Region, Fraktion und ob es ein Advanced-Access-Server ist.'), ('Ziel prüfen', 'Vergleiche exakten Servernamen, Fraktion und Zugangspool mit der Ankündigung.'), ('Beim Start erneut prüfen', 'Lies die aktuelle Meldung und Bestätigung vor dem Wechsel.')]],
 'body': '''NCs [Global-Transferankündigung]({url}) nennt einen geplanten Start und anfängliche Beschränkungen. Die Meldung wurde am 3. Oktober 2026 vor dem angekündigten Start geprüft. Sie belegt nicht, dass die Funktion bereits verfügbar ist. Dieser Guide erfindet weder Menüpfad noch Bearbeitungszeit oder Wartezeit zwischen Transfers.

<h2 id="confirmed-transfer-rules">Bestätigte Global-Transferregeln</h2>

| Frage | Veröffentlichte Bedingung |
| --- | --- |
| Wann ist der Start geplant? | 14. Oktober 2026; die Meldung nennt keine genaue Uhrzeit |
| Kann ein Wechsel die Fraktion ändern? | Die angekündigten Wechsel bleiben innerhalb derselben Fraktion |
| Können Advanced-Access-Spieler sofort auf öffentliche Startserver wechseln? | Anfangs sind nur Wechsel zwischen Advanced-Access-Servern möglich |
| Was kostet der Wechsel anfangs? | Zunächst kostenlos; ein Ende dieser Phase ist nicht genannt |
| Brauchen Freunde einen Transfer nur für gemeinsame Dungeons? | NC nennt serverübergreifende instanzierte Inhalte einschließlich Dungeons |

Lies die Bedingungen gemeinsam. „Kostenlos“ beschreibt die Anfangskosten und hebt die Fraktions- und Zugangsbeschränkungen nicht auf. Ein Datum ohne Uhrzeit belegt auch keinen Start um Mitternacht in deinem Land. Prüfe spätere Änderungen in der [offiziellen Meldung]({url}).

<GuideVisual id="workflow" />

<h2 id="choose-a-destination">Wähle das Ziel vor dem Start</h2>

Einigt euch mithilfe der [Serverliste](/server) auf Region, Fraktion und exakten Servernamen. NCs [Matchmaking-Erklärung]({pair}) unterscheidet den Heimatserver vom vorübergehend zugewiesenen Gegner der anderen Fraktion. Ein Wechsel innerhalb deiner Fraktion ist kein Wechsel auf diesen Gegnerserver oder in dessen Fraktion.

Trenne zwei Fragen: Wo soll dein Charakter beheimatet sein, und welche Gruppenaktivität willst du spielen? Die Transfermeldung nennt ausdrücklich serverübergreifende Instanzen. Sie erklärt jedoch nicht jede Gruppen-, Organisations- oder Open-World-Beschränkung. Prüfe die Bedingung deiner konkreten Aktivität, statt allein wegen unterschiedlicher Servernamen umzuziehen.

<h2 id="prepare-your-information">Bereite deine Angaben vor</h2>

1. Notiere aktuelle Region, Fraktion und genauen Servernamen.
2. Notiere das vereinbarte Ziel einschließlich Fraktion und Zugangspool.
3. Öffne die Transfermeldung erneut und suche eine Überarbeitung oder neue Teilnahmebedingungen.
4. Halte den konkreten Grund fest: gleicher Heimatserver, Beitritt zu einer Organisation oder ein anderes Ziel.
5. Lies beim Start die tatsächliche Zielauswahl und Bestätigung vor dem Abschluss.

Dies ist eine Vorbereitungsliste und keine bestätigte Liste von Bedingungen im Spiel. Ein Eintrag in einer alten Servertabelle belegt keine Transferfreigabe, wenn das Ziel in der Auswahl fehlt. Bei unerwarteten Charakteren vergleiche die [Konto- und Clientidentität](/steam) mit dem Charakter, den du bewegen willst.

<h2 id="unannounced-details">Noch nicht veröffentlichte Einzelheiten</h2>

Die geprüfte Meldung nennt keinen Menüpfad, genaue Startzeit, Bearbeitungsdauer, Transferabstand, erlaubten Regionswechsel, Umgang mit Namenskonflikten oder Regeln zu Organisationsmitgliedschaft, Post und Marktangeboten. Auch das Ende der kostenlosen Phase ist nicht angegeben. Fülle diese Lücken nicht mit KR/TW-Regeln oder Annahmen aus einem anderen NC-Spiel.

Sammle Fragen zu den Einzelheiten, die deinen Charakter betreffen. Lies nach dem Funktionsstart die aktuellen Anweisungen und Bestätigungen für deinen Wechsel. Eine kostenlose Anfangsphase ist eine nützliche Information, löst aber keine ungeklärte Ziel- oder Charakterbedingung.

<h2 id="check-at-opening">Was du beim Start prüfen solltest</h2>

Prüfe zuerst die neuesten [offiziellen Ankündigungen](https://aion2.plaync.com/en-us/board/notice/list) und [Wartungsmeldungen](/maintenance). Der geplante Funktionsstart und ein Wartungsfenster sind unterschiedliche Angaben. Ein abgelaufener Countdown belegt nicht, dass der Transferservice arbeitet.

Verwende die für Global und deinen Zugangspool geltenden Anweisungen. Sobald NC die tatsächliche Oberfläche und Einschränkungen veröffentlicht, kann dieser Guide die bestätigte Bedienfolge ergänzen. Nutze bis dahin die Bedingungen für eine Vorauswahl und behalte die ursprüngliche Meldung zum Vergleich.

<GuideNext slug="server" />''',
},
}

for locale, entry in DATA.items():
    directory = ROOT / 'src' / 'content' / locale
    paths = [directory / f'{SLUG}.mdx', directory / f'{SLUG}.json']
    assert not any(path.exists() for path in paths), 'Refusing to overwrite an existing guide'
    body = entry['body'].format(url=URL, pair=PAIR)
    paths[0].write_text(body + '\n', encoding='utf-8')
    title, caption, steps = entry['visual']
    meta = {key: entry[key] for key in ('title', 'description', 'summary')}
    meta['toc'] = [{'id': section_id, 'title': label} for section_id, label in zip(IDS, entry['heads'])]
    meta['visuals'] = {'workflow': {'title': title, 'caption': caption, 'steps': [{'label': label, 'description': text} for label, text in steps]}}
    meta['inlineNext'] = ['server']
    paths[1].write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

shared = {'slug': SLUG, 'keyword': 'aion 2 server transfer', 'checkedAt': '2026-10-03', 'revision': '2026-10-03.seo-1',
          'regions': ['Global'], 'related': ['server', 'maintenance', 'spacetime-rift'], 'sources': [
              {'id': 'transfer-announcement', 'title': 'Information on Server Transfer', 'url': URL, 'kind': 'official', 'region': 'Global', 'publishedAt': '2026-09-30', 'version': 'Global announcement checked 2026-10-03; interface and exact opening hour not supplied'},
              {'id': 'server-matchmaking', 'title': 'Advanced Access Server Matchmaking', 'url': PAIR, 'kind': 'official', 'region': 'Global', 'publishedAt': '2026-09-29', 'version': 'Global announcement updated 2026-10-02; archived server relationships'},
          ]}
path = ROOT / 'src' / 'content' / 'article-data' / f'{SLUG}.json'
assert not path.exists()
path.write_text(json.dumps(shared, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Created four complete server-transfer preparation guides with sourced, bounded conditions.')
