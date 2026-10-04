import type {TopicSlug} from './topics';

export const nextGuides: Record<TopicSlug, [TopicSlug, TopicSlug]> = {
  guide: ['leveling', 'builds'], gathering: ['map', 'monetization'], leveling: ['map', 'builds'],
  classes: ['builds', 'tier-list'], chanter: ['builds', 'pvp'], 'tier-list': ['classes', 'builds'],
  map: ['gathering', 'leveling'], code: ['twitch-drops', 'presets'],
  'character-creation': ['guide', 'presets'], presets: ['character-creation', 'monetization'],
  pvp: ['spacetime-rift', 'server'], 'spacetime-rift': ['pvp', 'map'],
  builds: ['chanter', 'cleric-build'], 'cleric-build': ['builds', 'pvp'],
  'twitch-drops': ['code', 'presets'], server: ['classes', 'character-creation'],
  maintenance: ['download', 'steam'], steam: ['download', 'server'],
  download: ['server', 'classes'], monetization: ['presets', 'builds'],
  notmeter: ['builds', 'classes'],
  'player-count': ['server', 'maintenance'],
  gladiator: ['builds', 'tier-list'], ranger: ['builds', 'pvp'],
  spiritmaster: ['builds', 'pvp'], races: ['server', 'character-creation'],
  'macro-guide': ['builds', 'notmeter'], 'server-transfer': ['server', 'maintenance'],
};
