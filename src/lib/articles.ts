import type {Locale} from '@/i18n/routing';
import type {TopicSlug} from './topics';
import {getTopic} from './topics';
import type {ArticleData, ArticleEntry} from './article-types';
import data_guide from '@/content/article-data/guide.json';
import data_gathering from '@/content/article-data/gathering.json';
import data_leveling from '@/content/article-data/leveling.json';
import data_classes from '@/content/article-data/classes.json';
import data_chanter from '@/content/article-data/chanter.json';
import data_tier_list from '@/content/article-data/tier-list.json';
import data_map from '@/content/article-data/map.json';
import data_code from '@/content/article-data/code.json';
import data_character_creation from '@/content/article-data/character-creation.json';
import data_presets from '@/content/article-data/presets.json';
import data_pvp from '@/content/article-data/pvp.json';
import data_spacetime_rift from '@/content/article-data/spacetime-rift.json';
import data_builds from '@/content/article-data/builds.json';
import data_cleric_build from '@/content/article-data/cleric-build.json';
import data_twitch_drops from '@/content/article-data/twitch-drops.json';
import data_server from '@/content/article-data/server.json';
import data_maintenance from '@/content/article-data/maintenance.json';
import data_steam from '@/content/article-data/steam.json';
import data_download from '@/content/article-data/download.json';
import data_monetization from '@/content/article-data/monetization.json';
import meta_en_guide from '@/content/en/guide.json';
import meta_en_gathering from '@/content/en/gathering.json';
import meta_en_leveling from '@/content/en/leveling.json';
import meta_en_classes from '@/content/en/classes.json';
import meta_en_chanter from '@/content/en/chanter.json';
import meta_en_tier_list from '@/content/en/tier-list.json';
import meta_en_map from '@/content/en/map.json';
import meta_en_code from '@/content/en/code.json';
import meta_en_character_creation from '@/content/en/character-creation.json';
import meta_en_presets from '@/content/en/presets.json';
import meta_en_pvp from '@/content/en/pvp.json';
import meta_en_spacetime_rift from '@/content/en/spacetime-rift.json';
import meta_en_builds from '@/content/en/builds.json';
import meta_en_cleric_build from '@/content/en/cleric-build.json';
import meta_en_twitch_drops from '@/content/en/twitch-drops.json';
import meta_en_server from '@/content/en/server.json';
import meta_en_maintenance from '@/content/en/maintenance.json';
import meta_en_steam from '@/content/en/steam.json';
import meta_en_download from '@/content/en/download.json';
import meta_en_monetization from '@/content/en/monetization.json';
import meta_ja_guide from '@/content/ja/guide.json';
import meta_ja_gathering from '@/content/ja/gathering.json';
import meta_ja_leveling from '@/content/ja/leveling.json';
import meta_ja_classes from '@/content/ja/classes.json';
import meta_ja_chanter from '@/content/ja/chanter.json';
import meta_ja_tier_list from '@/content/ja/tier-list.json';
import meta_ja_map from '@/content/ja/map.json';
import meta_ja_code from '@/content/ja/code.json';
import meta_ja_character_creation from '@/content/ja/character-creation.json';
import meta_ja_presets from '@/content/ja/presets.json';
import meta_ja_pvp from '@/content/ja/pvp.json';
import meta_ja_spacetime_rift from '@/content/ja/spacetime-rift.json';
import meta_ja_builds from '@/content/ja/builds.json';
import meta_ja_cleric_build from '@/content/ja/cleric-build.json';
import meta_ja_twitch_drops from '@/content/ja/twitch-drops.json';
import meta_ja_server from '@/content/ja/server.json';
import meta_ja_maintenance from '@/content/ja/maintenance.json';
import meta_ja_steam from '@/content/ja/steam.json';
import meta_ja_download from '@/content/ja/download.json';
import meta_ja_monetization from '@/content/ja/monetization.json';
import meta_es_guide from '@/content/es/guide.json';
import meta_es_gathering from '@/content/es/gathering.json';
import meta_es_leveling from '@/content/es/leveling.json';
import meta_es_classes from '@/content/es/classes.json';
import meta_es_chanter from '@/content/es/chanter.json';
import meta_es_tier_list from '@/content/es/tier-list.json';
import meta_es_map from '@/content/es/map.json';
import meta_es_code from '@/content/es/code.json';
import meta_es_character_creation from '@/content/es/character-creation.json';
import meta_es_presets from '@/content/es/presets.json';
import meta_es_pvp from '@/content/es/pvp.json';
import meta_es_spacetime_rift from '@/content/es/spacetime-rift.json';
import meta_es_builds from '@/content/es/builds.json';
import meta_es_cleric_build from '@/content/es/cleric-build.json';
import meta_es_twitch_drops from '@/content/es/twitch-drops.json';
import meta_es_server from '@/content/es/server.json';
import meta_es_maintenance from '@/content/es/maintenance.json';
import meta_es_steam from '@/content/es/steam.json';
import meta_es_download from '@/content/es/download.json';
import meta_es_monetization from '@/content/es/monetization.json';
import meta_de_guide from '@/content/de/guide.json';
import meta_de_gathering from '@/content/de/gathering.json';
import meta_de_leveling from '@/content/de/leveling.json';
import meta_de_classes from '@/content/de/classes.json';
import meta_de_chanter from '@/content/de/chanter.json';
import meta_de_tier_list from '@/content/de/tier-list.json';
import meta_de_map from '@/content/de/map.json';
import meta_de_code from '@/content/de/code.json';
import meta_de_character_creation from '@/content/de/character-creation.json';
import meta_de_presets from '@/content/de/presets.json';
import meta_de_pvp from '@/content/de/pvp.json';
import meta_de_spacetime_rift from '@/content/de/spacetime-rift.json';
import meta_de_builds from '@/content/de/builds.json';
import meta_de_cleric_build from '@/content/de/cleric-build.json';
import meta_de_twitch_drops from '@/content/de/twitch-drops.json';
import meta_de_server from '@/content/de/server.json';
import meta_de_maintenance from '@/content/de/maintenance.json';
import meta_de_steam from '@/content/de/steam.json';
import meta_de_download from '@/content/de/download.json';
import meta_de_monetization from '@/content/de/monetization.json';

const sharedData = {
  'guide': data_guide,
  'gathering': data_gathering,
  'leveling': data_leveling,
  'classes': data_classes,
  'chanter': data_chanter,
  'tier-list': data_tier_list,
  'map': data_map,
  'code': data_code,
  'character-creation': data_character_creation,
  'presets': data_presets,
  'pvp': data_pvp,
  'spacetime-rift': data_spacetime_rift,
  'builds': data_builds,
  'cleric-build': data_cleric_build,
  'twitch-drops': data_twitch_drops,
  'server': data_server,
  'maintenance': data_maintenance,
  'steam': data_steam,
  'download': data_download,
  'monetization': data_monetization,
} as Record<TopicSlug, ArticleData>;

const entries: Record<Locale, Record<TopicSlug, ArticleEntry>> = {
  en: {
    'guide': {metadata: meta_en_guide, load: () => import('@/content/en/guide.mdx')},
    'gathering': {metadata: meta_en_gathering, load: () => import('@/content/en/gathering.mdx')},
    'leveling': {metadata: meta_en_leveling, load: () => import('@/content/en/leveling.mdx')},
    'classes': {metadata: meta_en_classes, load: () => import('@/content/en/classes.mdx')},
    'chanter': {metadata: meta_en_chanter, load: () => import('@/content/en/chanter.mdx')},
    'tier-list': {metadata: meta_en_tier_list, load: () => import('@/content/en/tier-list.mdx')},
    'map': {metadata: meta_en_map, load: () => import('@/content/en/map.mdx')},
    'code': {metadata: meta_en_code, load: () => import('@/content/en/code.mdx')},
    'character-creation': {metadata: meta_en_character_creation, load: () => import('@/content/en/character-creation.mdx')},
    'presets': {metadata: meta_en_presets, load: () => import('@/content/en/presets.mdx')},
    'pvp': {metadata: meta_en_pvp, load: () => import('@/content/en/pvp.mdx')},
    'spacetime-rift': {metadata: meta_en_spacetime_rift, load: () => import('@/content/en/spacetime-rift.mdx')},
    'builds': {metadata: meta_en_builds, load: () => import('@/content/en/builds.mdx')},
    'cleric-build': {metadata: meta_en_cleric_build, load: () => import('@/content/en/cleric-build.mdx')},
    'twitch-drops': {metadata: meta_en_twitch_drops, load: () => import('@/content/en/twitch-drops.mdx')},
    'server': {metadata: meta_en_server, load: () => import('@/content/en/server.mdx')},
    'maintenance': {metadata: meta_en_maintenance, load: () => import('@/content/en/maintenance.mdx')},
    'steam': {metadata: meta_en_steam, load: () => import('@/content/en/steam.mdx')},
    'download': {metadata: meta_en_download, load: () => import('@/content/en/download.mdx')},
    'monetization': {metadata: meta_en_monetization, load: () => import('@/content/en/monetization.mdx')},
  },
  ja: {
    'guide': {metadata: meta_ja_guide, load: () => import('@/content/ja/guide.mdx')},
    'gathering': {metadata: meta_ja_gathering, load: () => import('@/content/ja/gathering.mdx')},
    'leveling': {metadata: meta_ja_leveling, load: () => import('@/content/ja/leveling.mdx')},
    'classes': {metadata: meta_ja_classes, load: () => import('@/content/ja/classes.mdx')},
    'chanter': {metadata: meta_ja_chanter, load: () => import('@/content/ja/chanter.mdx')},
    'tier-list': {metadata: meta_ja_tier_list, load: () => import('@/content/ja/tier-list.mdx')},
    'map': {metadata: meta_ja_map, load: () => import('@/content/ja/map.mdx')},
    'code': {metadata: meta_ja_code, load: () => import('@/content/ja/code.mdx')},
    'character-creation': {metadata: meta_ja_character_creation, load: () => import('@/content/ja/character-creation.mdx')},
    'presets': {metadata: meta_ja_presets, load: () => import('@/content/ja/presets.mdx')},
    'pvp': {metadata: meta_ja_pvp, load: () => import('@/content/ja/pvp.mdx')},
    'spacetime-rift': {metadata: meta_ja_spacetime_rift, load: () => import('@/content/ja/spacetime-rift.mdx')},
    'builds': {metadata: meta_ja_builds, load: () => import('@/content/ja/builds.mdx')},
    'cleric-build': {metadata: meta_ja_cleric_build, load: () => import('@/content/ja/cleric-build.mdx')},
    'twitch-drops': {metadata: meta_ja_twitch_drops, load: () => import('@/content/ja/twitch-drops.mdx')},
    'server': {metadata: meta_ja_server, load: () => import('@/content/ja/server.mdx')},
    'maintenance': {metadata: meta_ja_maintenance, load: () => import('@/content/ja/maintenance.mdx')},
    'steam': {metadata: meta_ja_steam, load: () => import('@/content/ja/steam.mdx')},
    'download': {metadata: meta_ja_download, load: () => import('@/content/ja/download.mdx')},
    'monetization': {metadata: meta_ja_monetization, load: () => import('@/content/ja/monetization.mdx')},
  },
  es: {
    'guide': {metadata: meta_es_guide, load: () => import('@/content/es/guide.mdx')},
    'gathering': {metadata: meta_es_gathering, load: () => import('@/content/es/gathering.mdx')},
    'leveling': {metadata: meta_es_leveling, load: () => import('@/content/es/leveling.mdx')},
    'classes': {metadata: meta_es_classes, load: () => import('@/content/es/classes.mdx')},
    'chanter': {metadata: meta_es_chanter, load: () => import('@/content/es/chanter.mdx')},
    'tier-list': {metadata: meta_es_tier_list, load: () => import('@/content/es/tier-list.mdx')},
    'map': {metadata: meta_es_map, load: () => import('@/content/es/map.mdx')},
    'code': {metadata: meta_es_code, load: () => import('@/content/es/code.mdx')},
    'character-creation': {metadata: meta_es_character_creation, load: () => import('@/content/es/character-creation.mdx')},
    'presets': {metadata: meta_es_presets, load: () => import('@/content/es/presets.mdx')},
    'pvp': {metadata: meta_es_pvp, load: () => import('@/content/es/pvp.mdx')},
    'spacetime-rift': {metadata: meta_es_spacetime_rift, load: () => import('@/content/es/spacetime-rift.mdx')},
    'builds': {metadata: meta_es_builds, load: () => import('@/content/es/builds.mdx')},
    'cleric-build': {metadata: meta_es_cleric_build, load: () => import('@/content/es/cleric-build.mdx')},
    'twitch-drops': {metadata: meta_es_twitch_drops, load: () => import('@/content/es/twitch-drops.mdx')},
    'server': {metadata: meta_es_server, load: () => import('@/content/es/server.mdx')},
    'maintenance': {metadata: meta_es_maintenance, load: () => import('@/content/es/maintenance.mdx')},
    'steam': {metadata: meta_es_steam, load: () => import('@/content/es/steam.mdx')},
    'download': {metadata: meta_es_download, load: () => import('@/content/es/download.mdx')},
    'monetization': {metadata: meta_es_monetization, load: () => import('@/content/es/monetization.mdx')},
  },
  de: {
    'guide': {metadata: meta_de_guide, load: () => import('@/content/de/guide.mdx')},
    'gathering': {metadata: meta_de_gathering, load: () => import('@/content/de/gathering.mdx')},
    'leveling': {metadata: meta_de_leveling, load: () => import('@/content/de/leveling.mdx')},
    'classes': {metadata: meta_de_classes, load: () => import('@/content/de/classes.mdx')},
    'chanter': {metadata: meta_de_chanter, load: () => import('@/content/de/chanter.mdx')},
    'tier-list': {metadata: meta_de_tier_list, load: () => import('@/content/de/tier-list.mdx')},
    'map': {metadata: meta_de_map, load: () => import('@/content/de/map.mdx')},
    'code': {metadata: meta_de_code, load: () => import('@/content/de/code.mdx')},
    'character-creation': {metadata: meta_de_character_creation, load: () => import('@/content/de/character-creation.mdx')},
    'presets': {metadata: meta_de_presets, load: () => import('@/content/de/presets.mdx')},
    'pvp': {metadata: meta_de_pvp, load: () => import('@/content/de/pvp.mdx')},
    'spacetime-rift': {metadata: meta_de_spacetime_rift, load: () => import('@/content/de/spacetime-rift.mdx')},
    'builds': {metadata: meta_de_builds, load: () => import('@/content/de/builds.mdx')},
    'cleric-build': {metadata: meta_de_cleric_build, load: () => import('@/content/de/cleric-build.mdx')},
    'twitch-drops': {metadata: meta_de_twitch_drops, load: () => import('@/content/de/twitch-drops.mdx')},
    'server': {metadata: meta_de_server, load: () => import('@/content/de/server.mdx')},
    'maintenance': {metadata: meta_de_maintenance, load: () => import('@/content/de/maintenance.mdx')},
    'steam': {metadata: meta_de_steam, load: () => import('@/content/de/steam.mdx')},
    'download': {metadata: meta_de_download, load: () => import('@/content/de/download.mdx')},
    'monetization': {metadata: meta_de_monetization, load: () => import('@/content/de/monetization.mdx')},
  },
};

export function getArticle(locale: Locale, slug: string) {
  const topic = getTopic(slug);
  if (!topic) return undefined;
  return {...entries[locale][topic.slug], data: sharedData[topic.slug]};
}

export function isArticlePublished(locale: Locale, slug: string) {
  return Boolean(getArticle(locale, slug));
}
