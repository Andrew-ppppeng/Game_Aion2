import type {Metadata} from 'next';
import {ArrowLeft, ArrowRight, BookOpen, ChevronRight, Feather} from 'lucide-react';
import {hasLocale} from 'next-intl';
import {setRequestLocale} from 'next-intl/server';
import {notFound} from 'next/navigation';
import {Link} from '@/i18n/navigation';
import {routing} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {getPageTitle, getTopic, legalSlugs, topics} from '@/lib/topics';
import {localePath} from '@/lib/site';

type Props = {params: Promise<{locale: string; slug: string}>};
export function generateStaticParams() {return [...topics.map((topic) => topic.slug), ...legalSlugs].map((slug) => ({slug}));}

export async function generateMetadata({params}: Props): Promise<Metadata> {
  const {locale, slug} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  const m = getSiteMessages(locale);
  const title = getPageTitle(slug, m);
  if (!title) notFound();
  return {title: `${title} · ${m.ui.comingSoon}`, description: m.ui.placeholderDescription, robots: {index: false, follow: true}, alternates: {canonical: localePath(locale, `/${slug}`)}};
}

export default async function PlannedPage({params}: Props) {
  const {locale, slug} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  setRequestLocale(locale);
  const m = getSiteMessages(locale);
  const title = getPageTitle(slug, m);
  if (!title) notFound();
  const topic = getTopic(slug);
  return <div className="placeholder-page">
    <nav className="breadcrumbs" aria-label={m.ui.navLabel}><Link href="/">{m.ui.home}</Link><ChevronRight size={13} aria-hidden="true" /><span>{title}</span></nav>
    <div className="placeholder-content" data-page-status="planned"><span className="placeholder-icon"><Feather size={42} strokeWidth={1} aria-hidden="true" /></span><span className="eyebrow">{topic ? m.categories[topic.category] : m.footer.aboutTitle}</span><h1>{title}</h1><span className="placeholder-badge"><span aria-hidden="true" />{m.ui.comingSoon}</span><p>{m.ui.placeholderDescription}</p><Link href="/" className="button button-primary"><ArrowLeft size={15} aria-hidden="true" />{m.ui.backHome}</Link>{slug !== 'guide' && topic && <Link href="/guide" className="text-link"><BookOpen size={14} aria-hidden="true" />{m.topics.guide}<ArrowRight size={13} aria-hidden="true" /></Link>}</div>
  </div>;
}
