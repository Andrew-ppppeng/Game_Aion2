import type {Metadata} from 'next';
import {ArrowLeft, ArrowRight, BookOpen, ChevronRight, Feather} from 'lucide-react';
import {hasLocale} from 'next-intl';
import {setRequestLocale} from 'next-intl/server';
import {notFound} from 'next/navigation';
import {Link} from '@/i18n/navigation';
import {routing} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {getPageTitle, getTopic, legalSlugs, topics} from '@/lib/topics';
import {languageAlternates, localePath, site} from '@/lib/site';
import {getArticle} from '@/lib/articles';
import {ArticlePage} from '@/components/article-page';
import {SiteInfoPage} from '@/components/site-info-page';
import {shareImagePath} from '@/lib/share-images';

type Props = {params: Promise<{locale: string; slug: string}>};
export function generateStaticParams() {return [...topics.map((topic) => topic.slug), ...legalSlugs].map((slug) => ({slug}));}

export async function generateMetadata({params}: Props): Promise<Metadata> {
  const {locale, slug} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  const m = getSiteMessages(locale);
  const title = getPageTitle(slug, m);
  if (!title) notFound();
  const article = getArticle(locale, slug);
  if (article) return {
    title: {absolute: article.metadata.title}, description: article.metadata.description,
    robots: {index: true, follow: true},
    alternates: {canonical: localePath(locale, `/${slug}`), languages: languageAlternates(`/${slug}`)},
    openGraph: {type: 'article', title: article.metadata.title, description: article.metadata.description, url: localePath(locale, `/${slug}`), siteName: m.footer.aboutTitle, modifiedTime: article.data.checkedAt, images: [{url: `${site.url}${shareImagePath(locale, slug, article.metadata.title, article.data.revision)}`, width: 1200, height: 630, alt: article.metadata.title}]},
    twitter: {card: 'summary_large_image', title: article.metadata.title, description: article.metadata.description, images: [shareImagePath(locale, slug, article.metadata.title, article.data.revision)]},
  };
  if (slug === 'privacy-policy' || slug === 'terms-of-service') {
    const descriptions = {
      en: ['How AION 2 Wiki handles local browser data, analytics and external services.', 'AION 2 Wiki editorial policy, source checks, corrections and terms of use.'],
      ja: ['AION 2 Wikiのブラウザ保存データ、アクセス解析、外部サービスに関する説明。', 'AION 2 Wikiの編集方針、出典確認、訂正と利用規約。'],
      es: ['Cómo AION 2 Wiki trata los datos locales del navegador, las estadísticas y los servicios externos.', 'Política editorial, comprobación de fuentes, correcciones y condiciones de AION 2 Wiki.'],
      de: ['Wie AION 2 Wiki lokale Browserdaten, Analysen und externe Dienste behandelt.', 'Redaktionsrichtlinien, Quellenprüfung, Korrekturen und Nutzungsbedingungen von AION 2 Wiki.'],
    };
    return {title, description: descriptions[locale][slug === 'privacy-policy' ? 0 : 1], robots: {index: false, follow: true}, alternates: {canonical: localePath(locale, `/${slug}`), languages: languageAlternates(`/${slug}`)}};
  }
  return {title: `${title} · ${m.ui.comingSoon}`, description: m.ui.placeholderDescription, robots: {index: false, follow: true}, alternates: {canonical: localePath(locale, `/${slug}`)}};
}

export default async function TopicPage({params}: Props) {
  const {locale, slug} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  setRequestLocale(locale);
  const m = getSiteMessages(locale);
  const title = getPageTitle(slug, m);
  if (!title) notFound();
  if (getArticle(locale, slug)) return <ArticlePage locale={locale} slug={slug} />;
  if (slug === 'privacy-policy' || slug === 'terms-of-service') return <SiteInfoPage locale={locale} slug={slug} />;
  const topic = getTopic(slug);
  return <div className="placeholder-page">
    <nav className="breadcrumbs" aria-label={m.ui.navLabel}><Link href="/">{m.ui.home}</Link><ChevronRight size={13} aria-hidden="true" /><span>{title}</span></nav>
    <div className="placeholder-content" data-page-status="planned"><span className="placeholder-icon"><Feather size={42} strokeWidth={1} aria-hidden="true" /></span><span className="eyebrow">{topic ? m.categories[topic.category] : m.footer.aboutTitle}</span><h1>{title}</h1><span className="placeholder-badge"><span aria-hidden="true" />{m.ui.comingSoon}</span><p>{m.ui.placeholderDescription}</p><Link href="/" className="button button-primary"><ArrowLeft size={15} aria-hidden="true" />{m.ui.backHome}</Link>{slug !== 'guide' && topic && <Link href="/guide" className="text-link"><BookOpen size={14} aria-hidden="true" />{m.topics.guide}<ArrowRight size={13} aria-hidden="true" /></Link>}</div>
  </div>;
}
