import type {Locale} from '@/i18n/routing';
import {Link} from '@/i18n/navigation';
import {getSiteMessages} from '@/i18n/messages';
import {AnalyticsPreference} from './analytics-preference';
import {FeedbackTemplate} from './feedback-template';

const information = {
  en: {
    privacySummary: 'Your checklists, saved characters and material plans stay in this browser. Our usage statistics collect limited daily totals, with controls below.',
    privacy: [
      ['local-data', 'What stays in your browser', 'Checklists, character bookmarks and material budgets use local browser storage. They persist until you remove them in the tool or clear this site’s browser data. They do not sync between devices. Character bookmarks may include the name, ID, server and region you choose to save.'],
      ['usage-statistics', 'Usage statistics and retention', 'When enabled, usage statistics record page paths without query strings, language, predefined actions and targets, and grouped Core Web Vitals results. We do not include character names or IDs, search text, budget contents or a user identifier. Daily aggregate counters expire after 35 days. First-visit and last-visit times stay locally in your browser to identify a return within 1–7 days; no cross-site cookie is used.'],
      ['privacy-controls', 'Your choices', 'The control below disables usage statistics on this browser. Do Not Track and Global Privacy Control also disable collection. You can clear local data through your browser’s site-data settings; that also removes saved tools and preferences.'],
      ['requests-and-services', 'Public lookups and technical requests', 'Character searches send the region, search or character identifier needed to obtain public game data through our server to NC’s public service. Query responses are cached separately from usage statistics: searches for up to 1 minute and character profiles for up to 60 minutes including stale fallback. An IP-derived hash limits public-tool requests in a 1-minute quota window. Hosting services also handle network request information to deliver the site; their technical log retention is governed by their configuration, not the 35-day statistics limit.'],
      ['external-services', 'Links and feedback', 'Official game sites, Steam, maps and other linked services apply their own policies when you visit them. This site does not request your NC password. The correction template below stays on your device; copying it does not send a report. If a contact link is available, your message is handled by that selected external service.'],
    ],
    termsSummary: 'AION 2 Wiki is an independent fan guide maintained by the AION 2 Wiki editorial team. This page explains how we maintain articles and handle corrections.',
    terms: [
      ['editorial-policy', 'Editorial responsibility and sources', 'The AION 2 Wiki editorial team is responsible for this site’s guides and translations. We prioritize official game notices, Steam and official Discord; player demonstrations are identified as such. Articles retain source links, the check date, region and version context. We separate Global, KR and TW information and mark conflicts or unverified details instead of presenting them as confirmed rules.'],
      ['maintenance-policy', 'How updates are maintained', 'Each article’s checked date describes its evidence review, not continuous testing or live server monitoring. Time-sensitive tables and timers use dated announcements. When an update changes a rule, we revise the affected claim, retain its source context and keep the four language versions aligned. Build examples retain the source player’s progression and regional limits.'],
      ['terms-of-use', 'Using the guides and tools', 'Use the guides as sourced starting points and compare their dated instructions with your current game client before spending resources. This site is not operated or endorsed by NC. Game artwork and trademarks belong to their respective owners. Public-data tools do not provide account access; do not enter passwords or private account information into them.'],
    ],
    corrections: 'Corrections and contact',
    correctionsBody: 'Include the page, region, client or patch date, the statement to correct and an official source or reproducible example. Avoid account secrets or other players’ private information. The template is prepared locally and is not submitted by this site.',
    contact: 'Open feedback contact',
    unconfigured: 'A feedback contact has not been configured. You can copy this template for the maintainer; nothing is sent automatically.',
    templateLabel: 'Correction template', copy: 'Copy correction template', copied: 'Template copied. No report was sent.', select: 'Template selected. Copy it using your browser.',
    template: 'Page URL:\nRegion (Global / KR / TW):\nClient version or patch date:\nStatement to correct:\nProposed correction:\nSource URL / reproducible steps:\n',
  },
  ja: {
    privacySummary: 'チェックリスト、保存キャラクター、素材計画はこのブラウザに保存します。利用統計は限定した日別集計で、下の設定から変更できます。',
    privacy: [
      ['local-data', 'ブラウザに保存する情報', 'チェックリスト、キャラクターのブックマーク、素材予算はブラウザのローカル保存を使用します。ツールで削除するか、このサイトの保存データを消すまで残り、端末間では同期しません。キャラクターのブックマークには、保存を選んだ名前・ID・サーバー・地域が含まれる場合があります。'],
      ['usage-statistics', '利用統計と保存期間', '有効な場合、クエリ文字列を含まないページパス、言語、定義済みの操作と対象、区分化したCore Web Vitalsを記録します。キャラクター名・ID、検索文、予算の内容、ユーザー識別子は含めません。日別の集計カウンターは35日後に失効します。初回と前回の訪問時刻はブラウザ内に保存して1～7日内の再訪を判断し、サイト間Cookieは使用しません。'],
      ['privacy-controls', '変更できる設定', '下の設定で、このブラウザの利用統計を無効にできます。Do Not TrackとGlobal Privacy Controlも収集を無効にします。ブラウザのサイトデータ設定でローカル情報を消すと、保存したツール情報と設定も消えます。'],
      ['requests-and-services', '公開情報の検索と技術的な通信', 'キャラクター検索では、公開ゲーム情報を取得するための地域・検索文字列・キャラクターIDを当サイトのサーバー経由でNCの公開サービスへ送信します。結果のキャッシュは利用統計と別で、検索は最大1分、キャラクター情報は古い結果の代替を含め最大60分です。IP由来のハッシュは公開ツールの1分間の通信制限に使います。ホスティングも配信のために通信情報を扱い、技術ログの保存期間は事業者の設定に従います。統計の35日制限とは別です。'],
      ['external-services', '外部リンクとフィードバック', '公式ゲームサイト、Steam、地図などへ移動すると、そのサービスの方針が適用されます。当サイトはNCのパスワードを求めません。訂正テンプレートは端末内にとどまり、コピーしても報告は送信されません。連絡先リンクがある場合は、選んだ外部サービスがメッセージを扱います。'],
    ],
    termsSummary: 'AION 2 WikiはAION 2 Wiki編集チームが管理する独立したファンガイドです。記事の更新方針と訂正方法を説明します。',
    terms: [
      ['editorial-policy', '編集責任と出典', 'AION 2 Wiki編集チームがガイドと翻訳を担当します。公式ゲーム告知、Steam、公式Discordを優先し、プレイヤーの実演はその種類を明示します。記事には出典リンク、確認日、地域、バージョンの背景を残します。Global・KR・TWを分け、相違や未確認事項を確定ルールとして扱いません。'],
      ['maintenance-policy', '更新方針', '記事の確認日は資料を確認した日で、継続的なゲーム内検証やサーバーの常時監視を意味しません。期限付きの表やタイマーは日時付き告知に基づきます。ルールが変わった場合は出典の背景を保って該当箇所を修正し、4言語を揃えます。ビルド例には元のプレイヤーの育成段階と地域の条件を残します。'],
      ['terms-of-use', 'ガイドとツールの利用', 'ガイドを出典付きの起点として使い、資源を消費する前に現在のクライアントと照合してください。当サイトはNCの運営・公認サイトではありません。ゲーム画像や商標は各権利者に帰属します。公開情報ツールはアカウントへのアクセスを提供せず、パスワードや非公開のアカウント情報を入力する必要はありません。'],
    ],
    corrections: '訂正と連絡', correctionsBody: 'ページ、地域、クライアントまたはパッチの日付、訂正箇所、公式出典や再現例を記入してください。アカウントの秘密や他のプレイヤーの非公開情報は含めないでください。テンプレートは端末内で準備し、このサイトからは送信しません。',
    contact: 'フィードバックの連絡先を開く', unconfigured: '連絡先はまだ設定されていません。管理者に伝えるためにテンプレートをコピーできます。自動送信は行いません。',
    templateLabel: '訂正テンプレート', copy: '訂正テンプレートをコピー', copied: 'コピーしました。報告は送信していません。', select: 'テンプレートを選択しました。ブラウザでコピーしてください。',
    template: 'ページURL:\n地域（Global / KR / TW）:\nクライアント版またはパッチ日:\n訂正する記述:\n訂正案:\n出典URL / 再現手順:\n',
  },
  es: {
    privacySummary: 'Tus listas, personajes guardados y planes de materiales permanecen en este navegador. Las estadísticas recogen totales diarios limitados y se controlan abajo.',
    privacy: [
      ['local-data', 'Datos que permanecen en tu navegador', 'Las listas, los favoritos de personajes y los presupuestos usan almacenamiento local. Permanecen hasta que los eliminas en la herramienta o borras los datos de este sitio en el navegador. No se sincronizan entre dispositivos. Los favoritos pueden incluir el nombre, ID, servidor y región que elijas guardar.'],
      ['usage-statistics', 'Estadísticas y conservación', 'Cuando están activadas, las estadísticas registran rutas sin parámetros de consulta, idioma, acciones y destinos predefinidos y resultados agrupados de Core Web Vitals. No incluyen nombres ni IDs de personajes, búsquedas, contenido de presupuestos ni identificadores de usuario. Los contadores diarios caducan a los 35 días. Las fechas de primera y última visita permanecen en el navegador para detectar un regreso en 1–7 días; no usamos cookies entre sitios.'],
      ['privacy-controls', 'Tus opciones', 'El control inferior desactiva las estadísticas en este navegador. Do Not Track y Global Privacy Control también desactivan la recogida. Puedes borrar los datos locales desde los ajustes del navegador; esto elimina también las herramientas y preferencias guardadas.'],
      ['requests-and-services', 'Consultas públicas y solicitudes técnicas', 'Las búsquedas de personajes envían la región, búsqueda o identificador necesario mediante nuestro servidor al servicio público de NC. La caché es independiente de las estadísticas: las búsquedas se conservan hasta 1 minuto y los perfiles hasta 60 minutos, incluida la alternativa de datos antiguos. Un hash derivado de la IP limita las consultas públicas en ventanas de 1 minuto. El alojamiento procesa información de red para servir el sitio; sus registros técnicos dependen de la configuración del proveedor, no del límite estadístico de 35 días.'],
      ['external-services', 'Enlaces y comentarios', 'Los sitios oficiales, Steam, los mapas y otros servicios enlazados aplican sus propias políticas cuando los visitas. Este sitio no pide tu contraseña de NC. La plantilla de corrección permanece en tu dispositivo; copiarla no envía un informe. Si hay enlace de contacto, el servicio externo elegido gestiona tu mensaje.'],
    ],
    termsSummary: 'AION 2 Wiki es una guía independiente de aficionados mantenida por el equipo editorial de AION 2 Wiki. Esta página explica las actualizaciones y correcciones.',
    terms: [
      ['editorial-policy', 'Responsabilidad editorial y fuentes', 'El equipo editorial de AION 2 Wiki es responsable de las guías y traducciones. Priorizamos avisos oficiales, Steam y Discord oficial; identificamos las demostraciones de jugadores. Conservamos enlaces, fecha de revisión, región y contexto de versión. Separamos Global, KR y TW y señalamos conflictos o datos sin verificar en vez de presentarlos como reglas confirmadas.'],
      ['maintenance-policy', 'Mantenimiento de las guías', 'La fecha de revisión indica una comprobación de fuentes, no pruebas continuas ni vigilancia del servidor en directo. Las tablas y temporizadores dependen de avisos fechados. Si cambia una regla, revisamos la afirmación afectada, conservamos su contexto y alineamos los cuatro idiomas. Los builds mantienen los límites de progresión y región del jugador fuente.'],
      ['terms-of-use', 'Uso de guías y herramientas', 'Usa las guías como punto de partida documentado y compara sus instrucciones fechadas con tu cliente antes de gastar recursos. NC no opera ni respalda este sitio. El arte y las marcas pertenecen a sus titulares. Las herramientas de datos públicos no dan acceso a cuentas; no introduzcas contraseñas ni información privada en ellas.'],
    ],
    corrections: 'Correcciones y contacto', correctionsBody: 'Incluye página, región, versión o fecha de parche, afirmación que corregir y fuente oficial o ejemplo reproducible. Evita secretos de cuentas e información privada de otros jugadores. La plantilla se prepara localmente y este sitio no la envía.',
    contact: 'Abrir contacto para comentarios', unconfigured: 'No hay un contacto configurado. Puedes copiar la plantilla para el responsable; no se envía nada automáticamente.',
    templateLabel: 'Plantilla de corrección', copy: 'Copiar plantilla de corrección', copied: 'Plantilla copiada. No se envió ningún informe.', select: 'Plantilla seleccionada. Cópiala con tu navegador.',
    template: 'URL de la página:\nRegión (Global / KR / TW):\nVersión del cliente o fecha del parche:\nAfirmación que corregir:\nCorrección propuesta:\nURL de fuente / pasos para reproducir:\n',
  },
  de: {
    privacySummary: 'Checklisten, gespeicherte Charaktere und Materialpläne bleiben in diesem Browser. Unsere Nutzungsstatistik erfasst begrenzte Tagessummen; die Einstellungen stehen unten.',
    privacy: [
      ['local-data', 'Daten in deinem Browser', 'Checklisten, Charakterfavoriten und Materialbudgets verwenden lokalen Browserspeicher. Sie bleiben bis zur Entfernung im Tool oder bis du die Website-Daten löschst und werden nicht zwischen Geräten synchronisiert. Favoriten können den von dir gespeicherten Namen, die ID, den Server und die Region enthalten.'],
      ['usage-statistics', 'Statistik und Speicherdauer', 'Wenn aktiviert, erfasst die Statistik Seitenpfade ohne Suchparameter, Sprache, vordefinierte Aktionen und Ziele sowie gruppierte Core-Web-Vitals-Ergebnisse. Charakternamen oder IDs, Suchtexte, Budgetinhalte und Nutzerkennungen sind ausgeschlossen. Tageszähler verfallen nach 35 Tagen. Erst- und Letztbesuchszeiten bleiben lokal zur Erkennung einer Rückkehr innerhalb von 1–7 Tagen; es gibt keinen websiteübergreifenden Cookie.'],
      ['privacy-controls', 'Deine Einstellungen', 'Die Einstellung unten deaktiviert die Nutzungsstatistik in diesem Browser. Do Not Track und Global Privacy Control deaktivieren sie ebenfalls. Browser-Einstellungen ermöglichen das Löschen lokaler Website-Daten; dadurch verschwinden auch gespeicherte Tools und Einstellungen.'],
      ['requests-and-services', 'Öffentliche Abfragen und technische Anfragen', 'Charaktersuchen senden erforderliche Region, Suche oder Charakterkennung über unseren Server an NCs öffentlichen Dienst. Antworten werden getrennt von der Statistik zwischengespeichert: Suchen bis zu 1 Minute, Profile einschließlich veralteter Ersatzdaten bis zu 60 Minuten. Ein aus der IP abgeleiteter Hash begrenzt öffentliche Abfragen in einem 1-Minuten-Fenster. Hosting verarbeitet Netzwerkinformationen zur Auslieferung; technische Logfristen folgen der Anbieterkonfiguration und nicht der 35-Tage-Statistikfrist.'],
      ['external-services', 'Links und Rückmeldungen', 'Offizielle Spielseiten, Steam, Karten und andere verlinkte Dienste wenden beim Besuch ihre eigenen Richtlinien an. Diese Website fragt nicht nach deinem NC-Passwort. Die Korrekturvorlage bleibt auf deinem Gerät; Kopieren sendet keinen Bericht. Ist ein Kontaktlink verfügbar, verarbeitet der gewählte externe Dienst deine Nachricht.'],
    ],
    termsSummary: 'AION 2 Wiki ist ein unabhängiger Fanguide des AION 2 Wiki-Redaktionsteams. Hier erklären wir Artikelpflege und Korrekturen.',
    terms: [
      ['editorial-policy', 'Redaktionelle Verantwortung und Quellen', 'Das AION 2 Wiki-Redaktionsteam verantwortet Guides und Übersetzungen. Wir priorisieren offizielle Spielmeldungen, Steam und den offiziellen Discord; Spielerdemonstrationen sind entsprechend gekennzeichnet. Quellenlinks, Prüfdatum, Region und Versionskontext bleiben erhalten. Global, KR und TW werden getrennt; Konflikte und unbestätigte Angaben werden als solche markiert.'],
      ['maintenance-policy', 'Artikelpflege', 'Das Prüfdatum bezeichnet eine Quellenprüfung, keine fortlaufenden Spieltests oder Live-Serverüberwachung. Zeitabhängige Tabellen und Timer beruhen auf datierten Meldungen. Ändert sich eine Regel, überarbeiten wir die betroffene Aussage, erhalten den Quellenkontext und gleichen die vier Sprachen ab. Builds behalten die Fortschritts- und Regionsgrenzen ihrer Spielervorlage.'],
      ['terms-of-use', 'Guides und Tools verwenden', 'Nutze die Guides als belegten Ausgangspunkt und gleiche datierte Anweisungen vor dem Ressourceneinsatz mit deinem aktuellen Client ab. NC betreibt oder bestätigt diese Website nicht. Spielgrafiken und Marken gehören ihren jeweiligen Rechteinhabern. Öffentliche Datentools gewähren keinen Kontozugang; gib dort keine Passwörter oder privaten Kontodaten ein.'],
    ],
    corrections: 'Korrekturen und Kontakt', correctionsBody: 'Nenne Seite, Region, Clientversion oder Patchdatum, die zu korrigierende Aussage und eine offizielle Quelle oder ein reproduzierbares Beispiel. Vermeide Kontogeheimnisse und private Daten anderer Spieler. Die Vorlage wird lokal vorbereitet und von dieser Website nicht verschickt.',
    contact: 'Rückmeldungskontakt öffnen', unconfigured: 'Ein Rückmeldungskontakt ist noch nicht eingerichtet. Du kannst die Vorlage für den Betreiber kopieren; nichts wird automatisch gesendet.',
    templateLabel: 'Korrekturvorlage', copy: 'Korrekturvorlage kopieren', copied: 'Vorlage kopiert. Kein Bericht wurde gesendet.', select: 'Vorlage ausgewählt. Kopiere sie mit deinem Browser.',
    template: 'Seiten-URL:\nRegion (Global / KR / TW):\nClientversion oder Patchdatum:\nZu korrigierende Aussage:\nVorgeschlagene Korrektur:\nQuellen-URL / Reproduktionsschritte:\n',
  },
};

function feedbackContact() {
  const value = process.env.NEXT_PUBLIC_FEEDBACK_URL?.trim();
  if (!value) return undefined;
  try {
    const url = new URL(value);
    if (url.protocol === 'https:' && url.hostname && !url.username && !url.password) return url.href;
    if (url.protocol === 'mailto:' && url.pathname.includes('@')) return url.href;
  } catch {}
  return undefined;
}

export function SiteInfoPage({locale, slug}: {locale: Locale; slug: 'privacy-policy' | 'terms-of-service'}) {
  const m = getSiteMessages(locale);
  const info = information[locale];
  const privacy = slug === 'privacy-policy';
  const title = privacy ? m.footer.privacyPolicy : m.footer.termsOfService;
  const contact = feedbackContact();
  return <article className="article-page site-info-page" data-page-status="site-info">
    <nav className="breadcrumbs" aria-label={m.ui.navLabel}><Link href="/">{m.ui.home}</Link><span> / </span><span>{title}</span></nav>
    <header className="article-header"><span className="eyebrow">AION 2 Wiki</span><h1>{title}</h1><p>{privacy ? info.privacySummary : info.termsSummary}</p></header>
    <div className="article-body">
      {(privacy ? info.privacy : info.terms).map(([id, heading, body]) => <section key={id}>
        <h2 id={id}>{heading}</h2><p>{body}</p>
        {id === 'privacy-controls' && <AnalyticsPreference locale={locale} />}
      </section>)}
      <section>
        <h2 id="corrections">{info.corrections}</h2><p>{info.correctionsBody}</p>
        {contact ? <p><a href={contact} rel="noopener noreferrer">{info.contact}</a></p> : <p>{info.unconfigured}</p>}
        <FeedbackTemplate template={info.template} label={info.templateLabel} copyLabel={info.copy} copiedLabel={info.copied} selectLabel={info.select} />
      </section>
    </div>
  </article>;
}
