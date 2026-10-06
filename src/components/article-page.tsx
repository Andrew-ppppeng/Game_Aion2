import {ArrowRight, ChevronRight, BookOpen} from 'lucide-react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {articleMessages} from '@/i18n/article-messages';
import {getArticle} from '@/lib/articles';
import {getTopic} from '@/lib/topics';
import {localePath, site} from '@/lib/site';
import {CouponCard} from './coupon-card';
import {ArticleToc} from './article-toc';
import {GuideVisual} from './guide-visual';
import {GuideChecklist, GuideFilter, ClassFinder, EventTimers, BudgetPlanner} from './guide-interactions';
import {ArticleNext} from './article-next';
import {guideAssets} from '@/lib/guide-assets';
import {nextGuides} from '@/lib/reading-paths';
import {guideMessages} from '@/i18n/guide-messages';
import type {ComponentProps, ReactNode} from 'react';
import {GuideTable} from './guide-table';
import {GuideEquipment} from './tools/guide-equipment';
import {gameEvents} from '@/lib/aion2/data';
import {shareImagePath} from '@/lib/share-images';
import {GuideSkillList, GuideSkillFocus, type ClassId} from './guide-skill-list';
import {GuideSkillMap} from './guide-skill-map';
import {GuideClassVideo, GuideClassVideos} from './guide-class-video';
import {GuideBuildMaps} from './guide-build-visuals';
import classIdentities from '@/content/class-identities.json';
import {VideoRecommendations} from './video-recommendations';

export async function ArticlePage({locale, slug}: {locale: Locale; slug: string}) {
  const article = getArticle(locale, slug);
  const topic = getTopic(slug);
  if (!article || !topic) return null;
  const {metadata, data} = article;
  const {default: Content} = await article.load();
  const m = getSiteMessages(locale);
  const a = articleMessages[locale];
  const reviewed = new Intl.DateTimeFormat(locale, {dateStyle: 'long', timeZone: 'UTC'}).format(new Date(`${data.checkedAt}T00:00:00Z`));
  const url = `${site.url}${localePath(locale, `/${slug}`)}`;
  const next = [...new Set([...nextGuides[topic.slug], ...data.related])].filter((target) => !metadata.inlineNext?.includes(target)).slice(0, 2);
  const recommended = new Set([...next, ...(metadata.inlineNext || [])]);
  const classAssets = guideAssets.filter((asset) => asset.id.startsWith('class-') || asset.id.startsWith('emblem-')).map(({id, src, width, height}) => ({id, src, width, height}));
  const components = {
    table: (props: ComponentProps<'table'>) => <GuideTable {...props} tierComparison={slug === 'tier-list'} />,
    GuideVisual: ({id}: {id: string}) => {
      const visual = metadata.visuals?.[id];
      if (!visual) throw new Error(`Missing guide visual: ${locale}/${slug}/${id}`);
      return <GuideVisual id={id} visual={visual} locale={locale} />;
    },
    GuideChecklist: () => {
      if (!metadata.checklist) throw new Error(`Missing checklist: ${locale}/${slug}`);
      return <GuideChecklist {...metadata.checklist} slug={slug} locale={locale} />;
    },
    GuideClasses: () => <ClassFinder locale={locale} assets={classAssets} />,
    GuideSkillList: ({classId}: {classId: ClassId}) => <GuideSkillList locale={locale} classId={classId} />,
    GuideSkillFocus: ({classId}: {classId: ClassId}) => <GuideSkillFocus locale={locale} classId={classId} />,
    GuideSkillMap: ({classId}: {classId: ClassId}) => <GuideSkillMap locale={locale} classId={classId} />,
    GuideClassVideo: ({classId}: {classId: ClassId}) => <GuideClassVideo locale={locale} classId={classId} />,
    GuideClassVideos: () => <GuideClassVideos locale={locale} />,
    GuideBuildMaps: () => <GuideBuildMaps locale={locale}>{classIdentities.map(({id}) => <GuideSkillMap key={id} locale={locale} classId={id as ClassId} />)}</GuideBuildMaps>,
    GuideFaction: ({faction, children}: {faction: string; children: ReactNode}) => <div data-faction-section={faction}>{children}</div>,
    GuideRegion: ({region, children}: {region: string; children: ReactNode}) => <div data-region-section={region}>{children}</div>,
    GuideNext: ({slug: target}: {slug: string}) => <ArticleNext locale={locale} slug={target} inline />,
    GuideEquipment: () => <GuideEquipment locale={locale} slug={slug} />,
    GuideTimers: () => <EventTimers locale={locale} events={gameEvents.filter((event) => event.topics.includes(slug))} initialNow={Date.now()} />,
    GuideBudget: () => <BudgetPlanner locale={locale} />,
  };
  const structuredData = {
    '@context': 'https://schema.org', '@graph': [
      {'@type': 'Article', headline: metadata.title, description: metadata.description, inLanguage: locale, url, dateModified: data.checkedAt, mainEntityOfPage: url,
        author: {'@type': 'Organization', name: 'AION 2 Wiki editorial team', url: `${site.url}${localePath(locale, '/terms-of-service')}#editorial-policy`},
        image: `${site.url}${shareImagePath(locale, slug, metadata.title, data.revision)}`,
      },
      {'@type': 'BreadcrumbList', itemListElement: [
        {'@type': 'ListItem', position: 1, name: m.ui.home, item: `${site.url}${localePath(locale)}`},
        {'@type': 'ListItem', position: 2, name: metadata.title, item: url},
      ]},
    ],
  };
  return <article className="article-page" data-page-status="published" data-article-slug={slug} data-article-revision={data.revision}>
    <script type="application/ld+json" dangerouslySetInnerHTML={{__html: JSON.stringify(structuredData).replace(/</g, '\\u003c')}} />
    <nav className="breadcrumbs" aria-label={m.ui.navLabel}><Link href="/">{m.ui.home}</Link><ChevronRight size={13} aria-hidden="true" /><span>{m.topics[topic.slug]}</span></nav>
    <header className="article-header" id="article-top">
      <span className="eyebrow">{m.categories[topic.category]}</span>
      <h1>{metadata.title}</h1>
      <div className="article-meta">{data.edition && data.edition !== 'Global' && <span data-article-edition>{data.edition}</span>}<span>{a.checkedAt}: <time dateTime={data.checkedAt}>{reviewed}</time></span><Link href="/terms-of-service#editorial-policy" data-article-author>{a.author}</Link></div>
      <div className="article-answer"><span>{a.quickAnswer}</span><p>{metadata.quickAnswer}</p></div>
    </header>
    <div className="article-layout">
      <ArticleToc sections={metadata.toc} title={a.onThisPage} locale={locale} />
      <div className="article-main">
        {slug === 'code' && <div className="article-coupon"><CouponCard /></div>}
        {(slug === 'leveling' || slug === 'server') && <GuideFilter kind={slug === 'leveling' ? 'faction' : 'region'} locale={locale} />}
        <div className="article-body"><Content components={components} /></div>
        <VideoRecommendations locale={locale} slug={slug} />
        <section className="article-next-section" aria-label={guideMessages[locale].next}>{next.map((target) => <ArticleNext key={target} locale={locale} slug={target} />)}</section>
        <section className="article-related" aria-labelledby="related-title"><h2 id="related-title"><BookOpen size={18} aria-hidden="true" />{a.related}</h2><div>{data.related.filter((related) => !recommended.has(related)).map((related) => {
          const relatedArticle = getArticle(locale, related);
          return relatedArticle ? <Link href={`/${related}`} key={related}><span>{m.topics[related]}</span><ArrowRight size={15} aria-hidden="true" /></Link> : null;
        })}</div></section>
        <a href="#article-top" className="article-back-top">{a.backTop} ↑</a>
      </div>
    </div>
  </article>;
}
