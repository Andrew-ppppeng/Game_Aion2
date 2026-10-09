import {ArrowRight, ArrowUpRight} from 'lucide-react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {structureMessages} from '@/i18n/structure-messages';
import {videoMessages} from '@/i18n/video-messages';
import {getArticle} from '@/lib/articles';
import {externalToolLinks, playerToolLinks, sectionGroups, sectionPaths, type SectionId} from '@/lib/site-structure';
import {localePath, site} from '@/lib/site';

export function SectionDirectory({locale, section, compact = false}: {locale: Locale; section: SectionId; compact?: boolean}) {
  const m = structureMessages[locale];
  const groups = compact ? sectionGroups[section].filter((group) => group.id === 'classSelection') : sectionGroups[section];
  const entries = groups.flatMap((group) => group.topics.filter((slug) => !(compact && slug === 'classes')).flatMap((slug) => {
    const article = getArticle(locale, slug);
    return article ? [{slug, title: article.metadata.title}] : [];
  }));
  const items = [...(section === 'tools' ? playerToolLinks.map((tool) => ({title: m.tools[tool.id].title, href: tool.href})) : []), ...entries.map((entry) => ({title: entry.title, href: `/${entry.slug}`})), ...(section === 'resources' ? [{title: videoMessages[locale].title, href: '/beginner-videos'}] : [])];
  const schema = {'@context': 'https://schema.org', '@type': 'CollectionPage', name: m.sections[section].title, url: `${site.url}${localePath(locale, sectionPaths[section])}`, mainEntity: {'@type': 'ItemList', itemListElement: items.map((entry, index) => ({'@type': 'ListItem', position: index + 1, name: entry.title, url: `${site.url}${localePath(locale, entry.href)}`}))}};
  return <div className={`section-directory${compact ? ' compact' : ''}`} data-section-directory={section}>
    {groups.map((group) => <section key={group.id} aria-labelledby={`directory-${group.id}`}>
      <h2 id={`directory-${group.id}`}>{m.groups[group.id]}</h2>
      <div className="directory-grid">{group.topics.filter((slug) => !(compact && slug === 'classes')).map((slug) => {
        const article = getArticle(locale, slug);
        return article ? <Link key={slug} href={`/${slug}`} className="directory-card" data-directory-topic={slug}><h3>{article.metadata.title}</h3><p>{article.metadata.summary}</p><span>{m.readGuide}<ArrowRight size={15} aria-hidden="true" /></span></Link> : null;
      })}</div>
    </section>)}
    {section === 'resources' && <section aria-labelledby="directory-videos"><h2 id="directory-videos">{videoMessages[locale].title}</h2><Link href="/beginner-videos" className="directory-card"><h3>{videoMessages[locale].title}</h3><p>{videoMessages[locale].intro}</p><span>{m.allTopics}<ArrowRight size={15} aria-hidden="true" /></span></Link></section>}
    {!compact && <script type="application/ld+json" dangerouslySetInnerHTML={{__html: JSON.stringify(schema).replace(/</g, '\\u003c')}} />}
  </div>;
}

export function ToolsDirectory({locale}: {locale: Locale}) {
  const m = structureMessages[locale];
  return <>
    <section className="section-directory" aria-labelledby="own-tools-title"><h2 id="own-tools-title">{m.ownTools}</h2><div className="directory-grid">{playerToolLinks.map((tool) => <Link key={tool.id} href={tool.href} className="directory-card" data-player-tool={tool.id}><h3>{m.tools[tool.id].title}</h3><p>{m.tools[tool.id].description}</p><span>{m.allTopics}<ArrowRight size={15} aria-hidden="true" /></span></Link>)}</div></section>
    <section className="section-directory external-directory" aria-labelledby="external-tools-title"><h2 id="external-tools-title">{m.externalTools}</h2><p className="directory-intro">{m.externalNote}</p><div className="directory-grid">{externalToolLinks.map((tool) => <article key={tool.id} className="directory-card" data-external-tool={tool.id}><span className="tool-badge">{m.external}</span><h3>{tool.name}</h3><p>{m.externalDescriptions[tool.id]}</p><div className="directory-actions">{tool.href && <a href={tool.href} target="_blank" rel="noopener noreferrer">{m.openExternal}<ArrowUpRight size={15} aria-hidden="true" /></a>}<Link href={tool.guide}>{m.readGuide}<ArrowRight size={15} aria-hidden="true" /></Link></div></article>)}</div></section>
    <SectionDirectory locale={locale} section="tools" />
  </>;
}
