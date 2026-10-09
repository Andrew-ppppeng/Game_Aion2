import {hasLocale} from 'next-intl';
import {setRequestLocale} from 'next-intl/server';
import {notFound} from 'next/navigation';
import {Link} from '@/i18n/navigation';
import {routing} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {structureMessages} from '@/i18n/structure-messages';
import {getArticle} from '@/lib/articles';
import {sectionMetadata} from '@/lib/section-metadata';
import {growthGoals, starterGoalLinks, type GrowthGoal} from '@/lib/growth-checklist';
import {GrowthChecklist} from '@/components/tools/growth-checklist';
import {localePath, site} from '@/lib/site';
type Props = {params: Promise<{locale: string}>};
export async function generateMetadata({params}: Props) {const {locale} = await params; if (!hasLocale(routing.locales, locale)) notFound(); return sectionMetadata(locale, 'tools', true);}
export default async function Page({params}: Props) {
  const {locale} = await params; if (!hasLocale(routing.locales, locale)) notFound(); setRequestLocale(locale);
  const m = structureMessages[locale];
  const starter = getArticle(locale, 'guide')!.metadata.checklist!.items;
  const goals: GrowthGoal[] = [
    ...starter.map((item) => ({...item, stage: 0, condition: '', href: starterGoalLinks[item.id as keyof typeof starterGoalLinks]})),
    ...growthGoals.map((goal) => ({...goal, ...m.growth.tasks[goal.id]})),
  ];
  const schema = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'WebApplication', name: m.growth.title, description: m.growth.intro, inLanguage: locale, applicationCategory: 'UtilitiesApplication', operatingSystem: 'Web browser', url: `${site.url}${localePath(locale, '/tools/growth-checklist')}`},
    {'@type': 'BreadcrumbList', itemListElement: [{name: getSiteMessages(locale).ui.home, href: '/'}, {name: m.sections.tools.title, href: '/tools'}, {name: m.growth.title, href: '/tools/growth-checklist'}].map((item, index) => ({'@type': 'ListItem', position: index + 1, name: item.name, item: `${site.url}${localePath(locale, item.href)}`}))},
  ]};
  return <article className="tools-page growth-page">
    <script type="application/ld+json" dangerouslySetInnerHTML={{__html: JSON.stringify(schema).replace(/</g, '\\u003c')}} />
    <nav className="breadcrumbs" aria-label={getSiteMessages(locale).ui.navLabel}><Link href="/">{getSiteMessages(locale).ui.home}</Link><span aria-hidden="true">/</span><Link href="/tools">{m.sections.tools.title}</Link><span aria-hidden="true">/</span><span>{m.growth.title}</span></nav>
    <header className="article-header"><h1>{m.growth.title}</h1><p>{m.growth.intro}</p></header><p className="directory-intro">{m.growth.note}</p>
    <noscript><p className="tool-note">{m.growth.noScript}</p></noscript>
    <GrowthChecklist locale={locale} goals={goals} />
    <section className="growth-support" aria-labelledby="growth-support-title"><h2 id="growth-support-title">{m.growth.support}</h2><div>{['gear-progression', 'gathering', 'crafting', 'daily-weekly-checklist'].map((slug) => <Link key={slug} href={`/${slug}`}>{getArticle(locale, slug)!.metadata.title}</Link>)}<Link href="/monetization#material-budget">{m.tools.budget.title}</Link></div></section>
  </article>;
}
