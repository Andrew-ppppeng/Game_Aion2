import type {Locale} from './routing';

const en = {
  onThisPage: 'On this page', quickAnswer: 'Quick answer', checkedAt: 'Updated',
  related: 'Continue your journey', readGuide: 'Read guide', backTop: 'Back to top',
  author: 'AION 2 Wiki editorial team',
};
type ArticleMessages = {[K in keyof typeof en]: string};

export const articleMessages = {
  en,
  ja: {
    onThisPage: '目次', quickAnswer: 'まず確認したいこと', checkedAt: '更新日',
    related: '関連ガイド', readGuide: 'ガイドを読む', backTop: 'ページ上部へ',
    author: 'AION 2 Wiki 編集チーム',
  },
  es: {
    onThisPage: 'En esta página', quickAnswer: 'Respuesta rápida', checkedAt: 'Actualizado',
    related: 'Guías relacionadas', readGuide: 'Leer guía', backTop: 'Volver arriba',
    author: 'Equipo editorial de AION 2 Wiki',
  },
  de: {
    onThisPage: 'Auf dieser Seite', quickAnswer: 'Kurz erklärt', checkedAt: 'Aktualisiert',
    related: 'Weiterführende Guides', readGuide: 'Guide lesen', backTop: 'Nach oben',
    author: 'AION 2 Wiki Redaktion',
  },
} satisfies Record<Locale, ArticleMessages>;
