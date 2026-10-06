import type {Locale} from '@/i18n/routing';
import {Link} from '@/i18n/navigation';
import {getSiteMessages} from '@/i18n/messages';
import {site} from '@/lib/site';
import {AnalyticsPreference} from './analytics-preference';
import {FeedbackTemplate} from './feedback-template';

const information = {
  en: {
    privacySummary: 'Your checklists, saved characters and material plans stay in this browser. We use daily aggregate statistics and Google Analytics, with controls below.',
    privacy: [
      ['local-data', 'What stays in your browser', 'Checklists, character bookmarks and material budgets use local browser storage. They persist until you remove them in the tool or clear this site’s browser data. They do not sync between devices. Character bookmarks may include the name, ID, server and region you choose to save.'],
      ['usage-statistics', 'Aggregate statistics and retention', 'When enabled, our daily aggregate statistics record page paths without query strings, language, predefined actions and targets, and grouped Core Web Vitals results. These counters do not include character names or IDs, search text, budget contents or a user identifier, and expire after 35 days. First-visit and last-visit times stay locally in your browser to identify a return within 1–7 days.'],
      ['google-analytics', 'Google Analytics', 'When statistics are enabled, we also use Google Analytics 4 to measure visits, traffic sources and interactions. Google Analytics may use first-party cookies and process page URLs, browser and device details, and network information. Its retention settings are separate from our 35-day aggregate counters. The control below also disables Google Analytics.'],
      ['privacy-controls', 'Your choices', 'The control below disables usage statistics on this browser. Do Not Track and Global Privacy Control also disable collection. You can clear local data through your browser’s site-data settings; that also removes saved tools and preferences.'],
      ['requests-and-services', 'Public lookups and technical requests', 'Character searches send the region, search or character identifier needed to obtain public game data through our server to NC’s public service. Query responses are cached separately from usage statistics: searches for up to 1 minute and character profiles for up to 60 minutes including stale fallback. An IP-derived hash limits public-tool requests in a 1-minute quota window. Hosting services also handle network request information to deliver the site; their technical log retention is governed by their configuration, not the 35-day statistics limit.'],
      ['external-services', 'Links and feedback', 'Official game sites, Steam, maps and other linked services apply their own policies when you visit them. This site does not request your NC password. The correction template below stays on your device; copying it does not send a report. If a contact link is available, your message is handled by that selected external service.'],
    ],
    termsSummary: 'AION 2 Wiki is an independent fan guide maintained by the AION 2 Wiki editorial team. This page explains how we maintain articles and handle corrections.',
    terms: [
      ['editorial-policy', 'Editorial responsibility and sources', 'The AION 2 Wiki editorial team maintains guides for the Steam release and their translations. Game facts prioritize official notices, Steam and official Discord. Source links, dates and version context remain in internal research records.'],
      ['maintenance-policy', 'How updates are maintained', 'We update affected guides when game rules change and keep the four language versions aligned. The date at the top records the article update. Event tables and timers show scheduled event windows.'],
      ['terms-of-use', 'Using the guides and tools', 'Use the guides as sourced starting points and compare their dated instructions with your current game client before spending resources. This site is not operated or endorsed by NC. Game artwork and trademarks belong to their respective owners. Public-data tools do not provide account access; do not enter passwords or private account information into them.'],
    ],
    corrections: 'Corrections and contact',
    correctionsBody: 'Include the page, region, client or patch date, the statement to correct and an official source or reproducible example. Avoid account secrets or other players’ private information. The template is prepared locally and is not submitted by this site.',
    contact: 'Open feedback contact',
    templateLabel: 'Correction template', copy: 'Copy correction template', copied: 'Template copied. No report was sent.', select: 'Template selected. Copy it using your browser.',
    template: 'Page URL:\nSteam server region and server:\nClient version or patch date:\nStatement to correct:\nProposed correction:\nSource URL / reproducible steps:\n',
  },
  ja: {
    privacySummary: 'チェックリスト、保存キャラクター、素材計画はこのブラウザに保存します。日別集計とGoogle Analyticsを使用し、下の設定から変更できます。',
    privacy: [
      ['local-data', 'ブラウザに保存する情報', 'チェックリスト、キャラクターのブックマーク、素材予算はブラウザのローカル保存を使用します。ツールで削除するか、このサイトの保存データを消すまで残り、端末間では同期しません。キャラクターのブックマークには、保存を選んだ名前・ID・サーバー・地域が含まれる場合があります。'],
      ['usage-statistics', '日別集計と保存期間', '有効な場合、当サイトの日別集計ではクエリ文字列を含まないページパス、言語、定義済みの操作と対象、区分化したCore Web Vitalsを記録します。この集計にキャラクター名・ID、検索文、予算の内容、ユーザー識別子は含めず、35日後に失効します。初回と前回の訪問時刻はブラウザ内に保存して1～7日内の再訪を判断します。'],
      ['google-analytics', 'Google Analytics', '統計が有効な場合、Google Analytics 4で訪問、流入元、操作も測定します。Google AnalyticsはファーストパーティCookieを使用し、ページURL、ブラウザや端末の情報、通信情報を処理する場合があります。保存期間は当サイトの日別集計の35日とは別の設定です。下の設定でGoogle Analyticsも無効にできます。'],
      ['privacy-controls', '変更できる設定', '下の設定で、このブラウザの利用統計を無効にできます。Do Not TrackとGlobal Privacy Controlも収集を無効にします。ブラウザのサイトデータ設定でローカル情報を消すと、保存したツール情報と設定も消えます。'],
      ['requests-and-services', '公開情報の検索と技術的な通信', 'キャラクター検索では、公開ゲーム情報を取得するための地域・検索文字列・キャラクターIDを当サイトのサーバー経由でNCの公開サービスへ送信します。結果のキャッシュは利用統計と別で、検索は最大1分、キャラクター情報は古い結果の代替を含め最大60分です。IP由来のハッシュは公開ツールの1分間の通信制限に使います。ホスティングも配信のために通信情報を扱い、技術ログの保存期間は事業者の設定に従います。統計の35日制限とは別です。'],
      ['external-services', '外部リンクとフィードバック', '公式ゲームサイト、Steam、地図などへ移動すると、そのサービスの方針が適用されます。当サイトはNCのパスワードを求めません。訂正テンプレートは端末内にとどまり、コピーしても報告は送信されません。連絡先リンクがある場合は、選んだ外部サービスがメッセージを扱います。'],
    ],
    termsSummary: 'AION 2 WikiはAION 2 Wiki編集チームが管理する独立したファンガイドです。記事の更新方針と訂正方法を説明します。',
    terms: [
      ['editorial-policy', '編集責任と出典', 'AION 2 Wiki編集チームがSteam版のガイドと翻訳を管理します。ゲーム情報は公式告知、Steam、公式Discordを優先します。出典リンク、日付、バージョンは内部研究記録に保存します。'],
      ['maintenance-policy', '更新方針', 'ゲームのルールが変わった場合は該当ガイドを更新し、4言語の内容を揃えます。ページ上部の日付は記事の更新日です。イベント表とタイマーは予定された開催期間を表示します。'],
      ['terms-of-use', 'ガイドとツールの利用', 'ガイドを出典付きの起点として使い、資源を消費する前に現在のクライアントと照合してください。当サイトはNCの運営・公認サイトではありません。ゲーム画像や商標は各権利者に帰属します。公開情報ツールはアカウントへのアクセスを提供せず、パスワードや非公開のアカウント情報を入力する必要はありません。'],
    ],
    corrections: '訂正と連絡', correctionsBody: 'ページ、地域、クライアントまたはパッチの日付、訂正箇所、公式出典や再現例を記入してください。アカウントの秘密や他のプレイヤーの非公開情報は含めないでください。テンプレートは端末内で準備し、このサイトからは送信しません。',
    contact: 'フィードバックの連絡先を開く',
    templateLabel: '訂正テンプレート', copy: '訂正テンプレートをコピー', copied: 'コピーしました。報告は送信していません。', select: 'テンプレートを選択しました。ブラウザでコピーしてください。',
    template: 'ページURL:\nSteamのサーバー地域とサーバー名:\nクライアント版またはパッチ日:\n訂正する記述:\n訂正案:\n出典URL / 再現手順:\n',
  },
  es: {
    privacySummary: 'Tus listas, personajes guardados y planes de materiales permanecen en este navegador. Usamos totales diarios y Google Analytics, con controles abajo.',
    privacy: [
      ['local-data', 'Datos que permanecen en tu navegador', 'Las listas, los favoritos de personajes y los presupuestos usan almacenamiento local. Permanecen hasta que los eliminas en la herramienta o borras los datos de este sitio en el navegador. No se sincronizan entre dispositivos. Los favoritos pueden incluir el nombre, ID, servidor y región que elijas guardar.'],
      ['usage-statistics', 'Totales diarios y conservación', 'Cuando están activados, nuestros totales diarios registran rutas sin parámetros de consulta, idioma, acciones y destinos predefinidos y resultados agrupados de Core Web Vitals. Estos contadores no incluyen nombres ni IDs de personajes, búsquedas, contenido de presupuestos ni identificadores de usuario, y caducan a los 35 días. Las fechas de primera y última visita permanecen en el navegador para detectar un regreso en 1–7 días.'],
      ['google-analytics', 'Google Analytics', 'Con las estadísticas activadas, también usamos Google Analytics 4 para medir visitas, fuentes de tráfico e interacciones. Google Analytics puede usar cookies propias y procesar URL de páginas, datos del navegador y dispositivo e información de red. Su conservación se configura por separado de nuestros contadores de 35 días. El control inferior también desactiva Google Analytics.'],
      ['privacy-controls', 'Tus opciones', 'El control inferior desactiva las estadísticas en este navegador. Do Not Track y Global Privacy Control también desactivan la recogida. Puedes borrar los datos locales desde los ajustes del navegador; esto elimina también las herramientas y preferencias guardadas.'],
      ['requests-and-services', 'Consultas públicas y solicitudes técnicas', 'Las búsquedas de personajes envían la región, búsqueda o identificador necesario mediante nuestro servidor al servicio público de NC. La caché es independiente de las estadísticas: las búsquedas se conservan hasta 1 minuto y los perfiles hasta 60 minutos, incluida la alternativa de datos antiguos. Un hash derivado de la IP limita las consultas públicas en ventanas de 1 minuto. El alojamiento procesa información de red para servir el sitio; sus registros técnicos dependen de la configuración del proveedor, no del límite estadístico de 35 días.'],
      ['external-services', 'Enlaces y comentarios', 'Los sitios oficiales, Steam, los mapas y otros servicios enlazados aplican sus propias políticas cuando los visitas. Este sitio no pide tu contraseña de NC. La plantilla de corrección permanece en tu dispositivo; copiarla no envía un informe. Si hay enlace de contacto, el servicio externo elegido gestiona tu mensaje.'],
    ],
    termsSummary: 'AION 2 Wiki es una guía independiente de aficionados mantenida por el equipo editorial de AION 2 Wiki. Esta página explica las actualizaciones y correcciones.',
    terms: [
      ['editorial-policy', 'Responsabilidad editorial y fuentes', 'El equipo editorial de AION 2 Wiki mantiene las guías de la versión de Steam y sus traducciones. Los datos del juego priorizan los avisos oficiales, Steam y Discord oficial. Los enlaces, fechas y versiones se conservan en registros internos.'],
      ['maintenance-policy', 'Mantenimiento de las guías', 'Actualizamos las guías afectadas cuando cambian las reglas del juego y mantenemos alineados los cuatro idiomas. La fecha superior indica la actualización del artículo. Las tablas y los temporizadores muestran los periodos programados de los eventos.'],
      ['terms-of-use', 'Uso de guías y herramientas', 'Usa las guías como punto de partida documentado y compara sus instrucciones fechadas con tu cliente antes de gastar recursos. NC no opera ni respalda este sitio. El arte y las marcas pertenecen a sus titulares. Las herramientas de datos públicos no dan acceso a cuentas; no introduzcas contraseñas ni información privada en ellas.'],
    ],
    corrections: 'Correcciones y contacto', correctionsBody: 'Incluye página, región, versión o fecha de parche, afirmación que corregir y fuente oficial o ejemplo reproducible. Evita secretos de cuentas e información privada de otros jugadores. La plantilla se prepara localmente y este sitio no la envía.',
    contact: 'Abrir contacto para comentarios',
    templateLabel: 'Plantilla de corrección', copy: 'Copiar plantilla de corrección', copied: 'Plantilla copiada. No se envió ningún informe.', select: 'Plantilla seleccionada. Cópiala con tu navegador.',
    template: 'URL de la página:\nRegión y servidor de Steam:\nVersión del cliente o fecha del parche:\nAfirmación que corregir:\nCorrección propuesta:\nURL de fuente / pasos para reproducir:\n',
  },
  de: {
    privacySummary: 'Checklisten, gespeicherte Charaktere und Materialpläne bleiben in diesem Browser. Wir verwenden Tagesstatistiken und Google Analytics, mit Einstellungen unten.',
    privacy: [
      ['local-data', 'Daten in deinem Browser', 'Checklisten, Charakterfavoriten und Materialbudgets verwenden lokalen Browserspeicher. Sie bleiben bis zur Entfernung im Tool oder bis du die Website-Daten löschst und werden nicht zwischen Geräten synchronisiert. Favoriten können den von dir gespeicherten Namen, die ID, den Server und die Region enthalten.'],
      ['usage-statistics', 'Tagesstatistik und Speicherdauer', 'Wenn aktiviert, erfassen unsere Tagesstatistiken Seitenpfade ohne Suchparameter, Sprache, vordefinierte Aktionen und Ziele sowie gruppierte Core-Web-Vitals-Ergebnisse. Diese Zähler enthalten keine Charakternamen oder IDs, Suchtexte, Budgetinhalte oder Nutzerkennungen und verfallen nach 35 Tagen. Erst- und Letztbesuchszeiten bleiben lokal zur Erkennung einer Rückkehr innerhalb von 1–7 Tagen.'],
      ['google-analytics', 'Google Analytics', 'Bei aktivierter Statistik verwenden wir auch Google Analytics 4 für Besuche, Zugriffsquellen und Interaktionen. Google Analytics kann eigene Cookies verwenden und Seiten-URLs, Browser- und Gerätedaten sowie Netzwerkinformationen verarbeiten. Die Speicherdauer wird getrennt von unseren 35-Tage-Zählern eingestellt. Die Einstellung unten deaktiviert auch Google Analytics.'],
      ['privacy-controls', 'Deine Einstellungen', 'Die Einstellung unten deaktiviert die Nutzungsstatistik in diesem Browser. Do Not Track und Global Privacy Control deaktivieren sie ebenfalls. Browser-Einstellungen ermöglichen das Löschen lokaler Website-Daten; dadurch verschwinden auch gespeicherte Tools und Einstellungen.'],
      ['requests-and-services', 'Öffentliche Abfragen und technische Anfragen', 'Charaktersuchen senden erforderliche Region, Suche oder Charakterkennung über unseren Server an NCs öffentlichen Dienst. Antworten werden getrennt von der Statistik zwischengespeichert: Suchen bis zu 1 Minute, Profile einschließlich veralteter Ersatzdaten bis zu 60 Minuten. Ein aus der IP abgeleiteter Hash begrenzt öffentliche Abfragen in einem 1-Minuten-Fenster. Hosting verarbeitet Netzwerkinformationen zur Auslieferung; technische Logfristen folgen der Anbieterkonfiguration und nicht der 35-Tage-Statistikfrist.'],
      ['external-services', 'Links und Rückmeldungen', 'Offizielle Spielseiten, Steam, Karten und andere verlinkte Dienste wenden beim Besuch ihre eigenen Richtlinien an. Diese Website fragt nicht nach deinem NC-Passwort. Die Korrekturvorlage bleibt auf deinem Gerät; Kopieren sendet keinen Bericht. Ist ein Kontaktlink verfügbar, verarbeitet der gewählte externe Dienst deine Nachricht.'],
    ],
    termsSummary: 'AION 2 Wiki ist ein unabhängiger Fanguide des AION 2 Wiki-Redaktionsteams. Hier erklären wir Artikelpflege und Korrekturen.',
    terms: [
      ['editorial-policy', 'Redaktionelle Verantwortung und Quellen', 'Das Redaktionsteam von AION 2 Wiki pflegt Guides zur Steam-Fassung und deren Übersetzungen. Spielinformationen beruhen vorrangig auf offiziellen Meldungen, Steam und dem offiziellen Discord. Quellenlinks, Daten und Versionsangaben bleiben in internen Forschungsaufzeichnungen.'],
      ['maintenance-policy', 'Artikelpflege', 'Bei geänderten Spielregeln aktualisieren wir die betroffenen Guides und gleichen alle vier Sprachen ab. Das Datum oben bezeichnet die Artikelaktualisierung. Ereignistabellen und Timer zeigen die geplanten Veranstaltungszeiten.'],
      ['terms-of-use', 'Guides und Tools verwenden', 'Nutze die Guides als belegten Ausgangspunkt und gleiche datierte Anweisungen vor dem Ressourceneinsatz mit deinem aktuellen Client ab. NC betreibt oder bestätigt diese Website nicht. Spielgrafiken und Marken gehören ihren jeweiligen Rechteinhabern. Öffentliche Datentools gewähren keinen Kontozugang; gib dort keine Passwörter oder privaten Kontodaten ein.'],
    ],
    corrections: 'Korrekturen und Kontakt', correctionsBody: 'Nenne Seite, Region, Clientversion oder Patchdatum, die zu korrigierende Aussage und eine offizielle Quelle oder ein reproduzierbares Beispiel. Vermeide Kontogeheimnisse und private Daten anderer Spieler. Die Vorlage wird lokal vorbereitet und von dieser Website nicht verschickt.',
    contact: 'Rückmeldungskontakt öffnen',
    templateLabel: 'Korrekturvorlage', copy: 'Korrekturvorlage kopieren', copied: 'Vorlage kopiert. Kein Bericht wurde gesendet.', select: 'Vorlage ausgewählt. Kopiere sie mit deinem Browser.',
    template: 'Seiten-URL:\nSteam-Serverregion und Server:\nClientversion oder Patchdatum:\nZu korrigierende Aussage:\nVorgeschlagene Korrektur:\nQuellen-URL / Reproduktionsschritte:\n',
  },
};

export function SiteInfoPage({locale, slug}: {locale: Locale; slug: 'privacy-policy' | 'terms-of-service'}) {
  const m = getSiteMessages(locale);
  const info = information[locale];
  const privacy = slug === 'privacy-policy';
  const title = privacy ? m.footer.privacyPolicy : m.footer.termsOfService;
  const contact = `mailto:${site.feedbackEmail}`;
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
        <p>{info.contact}: <a href={contact} data-feedback-contact>{site.feedbackEmail}</a></p>
        <FeedbackTemplate template={info.template} label={info.templateLabel} copyLabel={info.copy} copiedLabel={info.copied} selectLabel={info.select} />
      </section>
    </div>
  </article>;
}
