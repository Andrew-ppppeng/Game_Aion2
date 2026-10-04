import published from '../../content-topics.json';
import type {SiteMessages} from '@/i18n/messages';

export type TopicSlug = keyof SiteMessages['topics'];
export type CategoryId = keyof SiteMessages['categories'];

const categoryIds: Record<string, CategoryId> = {
  guide: 'guide',
  'class selection': 'classSelection',
  maps: 'maps',
  codes: 'codes',
  'character customization': 'characterCustomization',
  pvp: 'pvp',
  'builds and skills': 'buildsAndSkills',
  'twitch rewards': 'twitchRewards',
  servers: 'servers',
  platforms: 'platforms',
  'installation and controls': 'installationAndControls',
  'monetization and trading': 'monetizationAndTrading',
  'damage meters': 'damageMeters',
  'player statistics': 'playerStatistics',
  factions: 'factions',
  macros: 'macros',
  'wings and flight': 'wingsAndFlight',
  'databases': 'databases',
  'regional differences': 'regionalDifferences',
};

export type Topic = {
  id: TopicSlug;
  slug: TopicSlug;
  keyword: string;
  category: CategoryId;
};

export const topicGroups = published.categories.map(({category, keywords}) => {
  const id = categoryIds[category];
  if (!id) throw new Error(`Unmapped category: ${category}`);

  return {
    id,
    category,
    topics: keywords.map((keyword): Topic => {
      const slug = keyword.replace(/^aion 2 /, '').replaceAll(' ', '-') as TopicSlug;
      return {id: slug, slug, keyword, category: id};
    }),
  };
});

export const topics = topicGroups.flatMap((group) => group.topics);

export function getTopic(slug: string) {
  return topics.find((topic) => topic.slug === slug);
}

export const legalSlugs = ['privacy-policy', 'terms-of-service'] as const;

export function getPageTitle(slug: string, messages: SiteMessages): string | undefined {
  const topic = getTopic(slug);
  if (topic) return messages.topics[topic.slug];
  if (slug === 'privacy-policy') return messages.footer.privacyPolicy;
  if (slug === 'terms-of-service') return messages.footer.termsOfService;
}
