import type {MetadataRoute} from 'next';
import {routing} from '@/i18n/routing';
import {languageAlternates, localePath, site} from '@/lib/site';
export default function sitemap(): MetadataRoute.Sitemap {
  return routing.locales.map((locale) => ({url: `${site.url}${localePath(locale)}`, alternates: {languages: languageAlternates()}}));
}
