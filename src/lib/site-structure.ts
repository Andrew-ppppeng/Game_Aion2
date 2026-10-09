import type {TopicSlug} from './topics';

export const sectionIds = ['tools', 'guides', 'classes', 'resources'] as const;
export type SectionId = typeof sectionIds[number];
export const sectionPaths: Record<SectionId, string> = {tools: '/tools', guides: '/guides', classes: '/classes', resources: '/resources'};

export const sectionGroups = {
  tools: [
    {id: 'toolGuides', topics: ['notmeter', 'database']},
  ],
  guides: [
    {id: 'gettingStarted', topics: ['guide', 'settings', 'character-creation', 'presets', 'races']},
    {id: 'progression', topics: ['leveling', 'gear-progression', 'daily-weekly-checklist', 'gathering', 'crafting']},
    {id: 'explorationCombat', topics: ['map', 'wings', 'pvp', 'spacetime-rift', 'macro-guide']},
    {id: 'currency', topics: ['monetization']},
  ],
  classes: [
    {id: 'classSelection', topics: ['classes', 'tier-list', 'builds', 'cleric-build']},
    {id: 'classDetails', topics: ['templar', 'gladiator', 'assassin', 'ranger', 'sorcerer', 'spiritmaster', 'cleric', 'chanter']},
  ],
  resources: [
    {id: 'installation', topics: ['download', 'steam']},
    {id: 'servers', topics: ['server', 'maintenance', 'server-transfer', 'player-count']},
    {id: 'rewards', topics: ['code', 'twitch-drops']},
  ],
} as const satisfies Record<SectionId, readonly {id: string; topics: readonly TopicSlug[]}[]>;

export type SectionGroupId = typeof sectionGroups[SectionId][number]['id'];
export const sectionByTopic = Object.fromEntries(sectionIds.flatMap((section) => sectionGroups[section].flatMap((group) => group.topics.map((slug) => [slug, section])))) as Record<TopicSlug, SectionId>;
export const newPublicPaths = ['/tools', '/guides', '/resources', '/tools/growth-checklist'] as const;

export function sectionForPath(path: string): SectionId | undefined {
  const pathname = path.split(/[?#]/)[0].replace(/^\/(en|ja|es|de)(?=\/|$)/, '') || '/';
  if (pathname === '/tools' || pathname.startsWith('/tools/')) return 'tools';
  if (pathname === '/guides') return 'guides';
  if (pathname === '/resources' || pathname === '/beginner-videos') return 'resources';
  return sectionByTopic[pathname.slice(1) as TopicSlug];
}

export const playerToolLinks = [
  {id: 'growth', href: '/tools/growth-checklist'},
  {id: 'character', href: '/tools/character'},
  {id: 'budget', href: '/monetization#material-budget'},
  {id: 'starter', href: '/guide#starter-checklist'},
  {id: 'session', href: '/daily-weekly-checklist#starter-checklist'},
] as const;

// Operational links already used by the corresponding published guides.
// NotMeter stays a setup guide until desktop compatibility is confirmed.
export const externalToolLinks = [
  {id: 'map', name: 'Aion2T Interactive Map', href: 'https://aion2t.com/map', guide: '/map'},
  {id: 'database', name: 'gaming.tools', href: 'https://aion2.gaming.tools/items', guide: '/database'},
  {id: 'planner', name: 'gaming.tools Build Planner', href: 'https://aion2.gaming.tools/build-planner', guide: '/builds#talent-calculator'},
  {id: 'meter', name: 'NotMeter', href: null, guide: '/notmeter'},
] as const;
