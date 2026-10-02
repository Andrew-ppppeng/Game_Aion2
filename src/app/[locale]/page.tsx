import type {Metadata} from 'next';
import {hasLocale} from 'next-intl';
import {setRequestLocale} from 'next-intl/server';
import {notFound} from 'next/navigation';
import {routing, type Locale} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {languageAlternates, localePath, site} from '@/lib/site';
import HomeContent from '@/content/home.mdx';

type Props = {params: Promise<{locale: string}>};
const ogLocales: Record<Locale, string> = {en: 'en_US', ja: 'ja_JP', es: 'es_ES', de: 'de_DE'};

export async function generateMetadata({params}: Props): Promise<Metadata> {
  const {locale} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  const messages = getSiteMessages(locale);
  const m = messages.metadata;
  return {
    title: {absolute: m.title}, description: m.description,
    keywords: m.keywords.split(',').map((keyword) => keyword.trim()),
    alternates: {canonical: localePath(locale), languages: languageAlternates()},
    robots: {index: true, follow: true},
    openGraph: {type: 'website', title: m.title, description: m.description, siteName: messages.footer.aboutTitle, url: localePath(locale), locale: ogLocales[locale], alternateLocale: routing.locales.filter((language) => language !== locale).map((language) => ogLocales[language]), images: [{url: '/media/hero.jpg', width: 1438, height: 810, alt: messages.home.hero.title}]},
    twitter: {card: 'summary_large_image', title: m.title, description: m.description, images: ['/media/hero.jpg']},
  };
}

export default async function HomePage({params}: Props) {
  const {locale} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  setRequestLocale(locale);
  const m = getSiteMessages(locale);
  const structuredData = {'@context': 'https://schema.org', '@type': 'WebSite', name: m.footer.aboutTitle, url: `${site.url}${localePath(locale)}`, inLanguage: locale, description: m.metadata.description};
  return <><script type="application/ld+json" dangerouslySetInnerHTML={{__html: JSON.stringify(structuredData).replace(/</g, '\\u003c')}} /><HomeContent /></>;
}
