import type {Metadata} from 'next';
import {hasLocale} from 'next-intl';
import {setRequestLocale} from 'next-intl/server';
import {notFound} from 'next/navigation';
import {Link} from '@/i18n/navigation';
import {routing} from '@/i18n/routing';
import {toolMessages} from '@/i18n/tool-messages';
import {getSiteMessages} from '@/i18n/messages';
import {languageAlternates, localePath, site} from '@/lib/site';
import {shareImagePath} from '@/lib/share-images';
import {curatedIds, snapshotItem, snapshotMeta} from '@/lib/aion2/data';
import {characterId, positiveInteger, readRegion} from '@/lib/aion2/model';
import {regions} from '@/lib/aion2/types';
import {CharacterTool} from '@/components/tools/character-tool';

type Props = {params: Promise<{locale: string}>; searchParams: Promise<Record<string, string | string[] | undefined>>};
export async function generateMetadata({params, searchParams}: Props): Promise<Metadata> {
  const {locale} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  const query = await searchParams;
  const m = toolMessages[locale];
  const preview = process.env.VERCEL_ENV === 'preview';
  return {title: m.characterTitle, description: m.characterIntro, robots: {index: !preview && !Object.keys(query).length, follow: true},
    openGraph: {type: 'website', title: m.characterTitle, description: m.characterIntro, url: localePath(locale, '/tools/character'), siteName: site.name, images: [{url: shareImagePath(locale, 'character', m.characterTitle), width: 1200, height: 630, alt: m.characterTitle}]},
    twitter: {card: 'summary_large_image', title: m.characterTitle, description: m.characterIntro, images: [shareImagePath(locale, 'character', m.characterTitle)]},
    alternates: {canonical: localePath(locale, '/tools/character'), languages: languageAlternates('/tools/character')}};
}
export default async function CharacterPage({params, searchParams}: Props) {
  const {locale} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  setRequestLocale(locale);
  const query = await searchParams;
  const m = toolMessages[locale];
  let initialCharacter;
  if (typeof query.cid === 'string' && typeof query.serverId === 'string') {
    try {initialCharacter = {id: characterId(query.cid), serverId: positiveInteger(query.serverId), region: readRegion(typeof query.region === 'string' ? query.region : null)};} catch {initialCharacter = undefined;}
  }
  const metadata = Object.fromEntries(regions.map((region) => [region, snapshotMeta(region, locale).data!])) as Parameters<typeof CharacterTool>[0]['metadata'];
  const candidates = curatedIds.map((id) => snapshotItem(id, locale).data!);
  return <div className="tools-page"><nav className="breadcrumbs"><Link href="/">{getSiteMessages(locale).ui.home}</Link><span> / </span><span>{m.characterTitle}</span></nav>
    <header className="article-header"><span className="eyebrow">Global</span><h1>{m.characterTitle}</h1><p>{m.characterIntro}</p></header>
    <CharacterTool locale={locale} metadata={metadata} candidates={candidates} initialCharacter={initialCharacter} />
  </div>;
}
