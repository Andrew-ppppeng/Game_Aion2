import type {MetadataRoute} from 'next';
import {routing} from '@/i18n/routing';
import {languageAlternates, localePath, site} from '@/lib/site';
import {topics} from '@/lib/topics';
import {getArticle} from '@/lib/articles';
import {curatedIds} from '@/lib/aion2/data';
export default function sitemap(): MetadataRoute.Sitemap {
  return routing.locales.flatMap((locale) => [
    {url: `${site.url}${localePath(locale)}`, alternates: {languages: languageAlternates()}},
    {url: `${site.url}${localePath(locale, '/tools/character')}`, alternates: {languages: languageAlternates('/tools/character')}},
    ...['/tools', '/tools/compare', '/tools/budget', '/tools/calendar', ...curatedIds.map((id) => `/database/items/${id}`)].map((path) => ({url: `${site.url}${localePath(locale, path)}`, alternates: {languages: languageAlternates(path)}})),
    ...topics.flatMap((topic) => {
      const article = getArticle(locale, topic.slug);
      return article ? [{url: `${site.url}${localePath(locale, `/${topic.slug}`)}`, lastModified: article.data.checkedAt, alternates: {languages: languageAlternates(`/${topic.slug}`)}}] : [];
    }),
  ]);
}
