import Image from 'next/image';
import {ArrowRight, Download, Expand, Sparkles} from 'lucide-react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import skills from '@/content/class-skills.json';
import maps from '@/content/class-skill-maps.json';
import identities from '@/content/class-identities.json';
import {classMediaMessages} from '@/i18n/class-media-messages';
import type {ClassId} from './guide-skill-list';

type StateNode = {label: Record<Locale, string>};
type MapNode = string | StateNode;

export function GuideSkillMap({locale, classId}: {locale: Locale; classId: ClassId}) {
  const m = classMediaMessages[locale];
  const identity = identities.find(({id}) => id === classId)!;
  const png = `/media/guides/skill-map-${classId}-${locale}.png`;
  function node(item: MapNode, index: number) {
    if (typeof item !== 'string') return <div className="skill-map-state" key={index}><Sparkles size={25} aria-hidden="true" /><strong>{item.label[locale]}</strong></div>;
    const skill = skills[classId].find(({id}) => id === item)!;
    return <Link key={item} href={`/${classId}#${skill.kind === 'active' ? `skill-${item}` : 'all-skills'}`} className="skill-map-node" data-map-skill={item}>
      <Image src={`/media/skills/${item}.webp`} width={52} height={52} alt="" unoptimized />
      <span><strong>{skill.names[locale]}</strong>{locale !== 'en' && skill.names[locale] !== skill.names.en && <small lang="en">{skill.names.en}</small>}</span>
    </Link>;
  }
  return <figure className="skill-map" data-skill-map={classId}>
    <figcaption className="skill-map-heading"><Image src={`/media/guides/emblem-${classId}.webp`} width={44} height={46} alt="" unoptimized /><div><span className="eyebrow">{identity.names[locale]}</span><strong>{m.mapTitle}</strong></div></figcaption>
    <p className="skill-map-hint">{m.mapHint}</p>
    <div className="skill-map-rows">{maps[classId].map((row, index) => <div key={index} className={`skill-map-row ${row.kind}`} data-map-kind={row.kind}>
      <div className="skill-map-nodes">{row.sources.map(node)}</div>
      <div className="skill-map-connection"><span>{m[row.kind as 'trigger' | 'specialization' | 'response' | 'resource']}</span><ArrowRight size={36} strokeWidth={1.4} aria-hidden="true" /><p>{row.caption[locale]}</p></div>
      <div className="skill-map-nodes">{row.targets.map(node)}</div>
    </div>)}</div>
    <div className="skill-map-actions"><a href={png} target="_blank" rel="noopener"><Expand size={15} aria-hidden="true" />{m.fullImage}</a><a href={png} download><Download size={15} aria-hidden="true" />{m.download}</a></div>
  </figure>;
}
