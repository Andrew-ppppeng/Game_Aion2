import 'server-only';
import type {Metadata} from 'next';
import {hasLocale} from 'next-intl';
import {setRequestLocale} from 'next-intl/server';
import {notFound} from 'next/navigation';
import {routing} from '@/i18n/routing';
import type {Locale} from '@/i18n/routing';
import {languageAlternates, localePath, site} from '@/lib/site';
export function platformLocale(value: string): Locale {
  if (!hasLocale(routing.locales, value)) notFound();
  setRequestLocale(value); return value;
}
export function platformMetadata(locale: Locale, path: string, title: string, description: string, index = true): Metadata {
  return {title, description, robots: {index: index && process.env.VERCEL_ENV !== 'preview', follow: true},
    alternates: {canonical: localePath(locale, path), languages: languageAlternates(path)},
    openGraph: {type: 'website', title, description, url: localePath(locale, path), siteName: site.name}, twitter: {card: 'summary_large_image', title, description}};
}
