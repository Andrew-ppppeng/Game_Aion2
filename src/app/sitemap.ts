import type {MetadataRoute} from 'next';
import {routing} from '@/i18n/routing';
import {languageAlternates, localePath, site} from '@/lib/site';
import {topics} from '@/lib/topics';
import {getArticle} from '@/lib/articles';
export default function sitemap(): MetadataRoute.Sitemap {
  return routing.locales.flatMap((locale) => [
    {url: `${site.url}${localePath(locale)}`, alternates: {languages: languageAlternates()}},
    ...topics.flatMap((topic) => {
      const article = getArticle(locale, topic.slug);
      return article ? [{url: `${site.url}${localePath(locale, `/${topic.slug}`)}`, lastModified: article.data.checkedAt, alternates: {languages: languageAlternates(`/${topic.slug}`)}}] : [];
    }),
  ]);
}
