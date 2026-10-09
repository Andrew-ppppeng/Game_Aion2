import type {MetadataRoute} from 'next';
import {routing} from '@/i18n/routing';
import {languageAlternates, localePath, site} from '@/lib/site';
import {topics} from '@/lib/topics';
import {getArticle} from '@/lib/articles';
import {newPublicPaths} from '@/lib/site-structure';
export default function sitemap(): MetadataRoute.Sitemap {
  return routing.locales.flatMap((locale) => [
    {url: `${site.url}${localePath(locale)}`, alternates: {languages: languageAlternates()}},
    ...newPublicPaths.map((path) => ({url: `${site.url}${localePath(locale, path)}`, alternates: {languages: languageAlternates(path)}})),
    {url: `${site.url}${localePath(locale, '/tools/character')}`, alternates: {languages: languageAlternates('/tools/character')}},
    {url: `${site.url}${localePath(locale, '/beginner-videos')}`, lastModified: '2026-10-06', alternates: {languages: languageAlternates('/beginner-videos')}},
    ...topics.flatMap((topic) => {
      const article = getArticle(locale, topic.slug);
      return article ? [{url: `${site.url}${localePath(locale, `/${topic.slug}`)}`, lastModified: article.data.checkedAt, alternates: {languages: languageAlternates(`/${topic.slug}`)}}] : [];
    }),
  ]);
}
