import type {Metadata} from 'next';
import type {Locale} from '@/i18n/routing';
import {structureMessages} from '@/i18n/structure-messages';
import {sectionPaths, type SectionId} from './site-structure';
import {languageAlternates, localePath, site} from './site';

export function sectionMetadata(locale: Locale, section: SectionId, growth = false): Metadata {
  const copy = growth ? structureMessages[locale].growth : structureMessages[locale].sections[section];
  const title = copy.title;
  const description = 'intro' in copy ? copy.intro : copy.description;
  const path = growth ? '/tools/growth-checklist' : sectionPaths[section];
  return {
    title, description, robots: {index: process.env.VERCEL_ENV !== 'preview', follow: true},
    alternates: {canonical: localePath(locale, path), languages: languageAlternates(path)},
    openGraph: {type: 'website', title, description, url: localePath(locale, path), siteName: site.name, images: [{url: '/media/hero.jpg', alt: title}]},
    twitter: {card: 'summary_large_image', title, description, images: ['/media/hero.jpg']},
  };
}
