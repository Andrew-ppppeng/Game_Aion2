import type {Metadata} from 'next';
import {hasLocale} from 'next-intl';
import {setRequestLocale} from 'next-intl/server';
import {notFound} from 'next/navigation';
import {routing} from '@/i18n/routing';
import {Link} from '@/i18n/navigation';
import {videoMessages} from '@/i18n/video-messages';
import {languageAlternates, localePath, site} from '@/lib/site';
import {beginnerVideos} from '@/lib/beginner-videos';
import {VideoLibrary} from '@/components/video-library';
import {structureMessages} from '@/i18n/structure-messages';
import {getSiteMessages} from '@/i18n/messages';

type Props = {params: Promise<{locale: string}>};
export async function generateMetadata({params}: Props): Promise<Metadata> {
  const {locale} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  const m = videoMessages[locale];
  return {title: m.title, description: m.intro, robots: {index: true, follow: true}, alternates: {canonical: localePath(locale, '/beginner-videos'), languages: languageAlternates('/beginner-videos')}};
}
export default async function VideoPage({params}: Props) {
  const {locale} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  setRequestLocale(locale);
  const m = videoMessages[locale];
  const schema = {'@context': 'https://schema.org', '@type': 'CollectionPage', name: m.title, url: `${site.url}${localePath(locale, '/beginner-videos')}`, mainEntity: {'@type': 'ItemList', itemListElement: beginnerVideos.map((v, i) => ({'@type': 'ListItem', position: i + 1, name: v.titles[locale], url: `https://www.youtube.com/watch?v=${v.id}`}))}};
  return <article className="article-page video-library-page"><header className="article-header"><nav className="breadcrumbs"><Link href="/">{getSiteMessages(locale).ui.home}</Link><span> / </span><Link href="/resources">{structureMessages[locale].sections.resources.title}</Link><span> / </span><span>{m.title}</span></nav><h1>{m.title}</h1><p>{m.intro}</p></header><VideoLibrary locale={locale} /><script type="application/ld+json" dangerouslySetInnerHTML={{__html: JSON.stringify(schema).replace(/</g, '\\u003c')}} /></article>;
}
