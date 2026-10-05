import type {Locale} from './routing';

const en = {
  sourceContext: 'Version and verification scope',
  onThisPage: 'On this page', quickAnswer: 'Quick answer', checkedAt: 'Last reviewed',
  regionalNote: 'Global is the main edition. KR and TW examples are labelled in the guide; rules can differ between regions and updates.',
  sources: 'Sources', sourceIntro: 'Official announcements and clearly identified player reports used for this guide. Source titles retain their original language.',
  related: 'Continue your journey', readGuide: 'Read guide', backTop: 'Back to top',
  official: 'Official', player: 'Player report', community: 'Community', tool: 'Third-party tool',
  mixed: 'Multiple regions', publishedAt: 'Published', snapshot: 'Information reviewed on the date above. Follow the linked official announcements for later changes.',
};

type ArticleMessages = {[K in keyof typeof en]: string};

export const articleMessages = {
  en,
  ja: {
    sourceContext: '版と確認範囲',
    onThisPage: '目次', quickAnswer: 'まず確認したいこと', checkedAt: '最終確認日',
    regionalNote: '主にGlobal版を対象としています。KR・TW版の事例は本文に明記しています。地域やアップデートにより仕様が異なる場合があります。',
    sources: '参考資料', sourceIntro: '公式告知と、出典を明記したプレイヤーの報告を参考にしています。資料名は原文のまま掲載しています。',
    related: '関連ガイド', readGuide: 'ガイドを読む', backTop: 'ページ上部へ',
    official: '公式', player: 'プレイヤーの報告', community: 'コミュニティ', tool: '外部ツール',
    mixed: '複数地域', publishedAt: '公開日', snapshot: '上記の日付に確認した情報です。その後の変更はリンク先の公式告知をご確認ください。',
  },
  es: {
    sourceContext: 'Versión y alcance de la verificación',
    onThisPage: 'En esta página', quickAnswer: 'Respuesta rápida', checkedAt: 'Última revisión',
    regionalNote: 'La edición principal es Global. Los ejemplos de KR y TW están identificados en la guía; las reglas pueden variar según la región y la actualización.',
    sources: 'Fuentes', sourceIntro: 'Esta guía utiliza anuncios oficiales e informes de jugadores con su procedencia indicada. Los títulos de las fuentes se conservan en su idioma original.',
    related: 'Guías relacionadas', readGuide: 'Leer guía', backTop: 'Volver arriba',
    official: 'Oficial', player: 'Informe de un jugador', community: 'Comunidad', tool: 'Herramienta externa',
    mixed: 'Varias regiones', publishedAt: 'Publicado', snapshot: 'Información revisada en la fecha indicada arriba. Consulta los anuncios oficiales enlazados para conocer los cambios posteriores.',
  },
  de: {
    sourceContext: 'Version und Prüfumfang',
    onThisPage: 'Auf dieser Seite', quickAnswer: 'Kurz erklärt', checkedAt: 'Zuletzt geprüft',
    regionalNote: 'Im Mittelpunkt steht die Global-Version. Beispiele aus KR und TW sind im Guide gekennzeichnet; Regeln können je nach Region und Update abweichen.',
    sources: 'Quellen', sourceIntro: 'Dieser Guide verwendet offizielle Ankündigungen und eindeutig gekennzeichnete Spielerberichte. Quellentitel bleiben in ihrer Originalsprache.',
    related: 'Weiterführende Guides', readGuide: 'Guide lesen', backTop: 'Nach oben',
    official: 'Offiziell', player: 'Spielerbericht', community: 'Community', tool: 'Externes Tool',
    mixed: 'Mehrere Regionen', publishedAt: 'Veröffentlicht', snapshot: 'Die Informationen wurden am oben genannten Datum geprüft. Spätere Änderungen findest du in den verlinkten offiziellen Ankündigungen.',
  },
} satisfies Record<Locale, ArticleMessages>;
