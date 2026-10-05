import type {ComponentType} from 'react';
import type {MDXProps} from 'mdx/types';
import type {TopicSlug} from './topics';

export type ArticleMetadata = {
  title: string;
  description: string;
  summary: string;
  quickAnswer: string;
  toc: {id: string; title: string}[];
  visuals?: Record<string, GuideVisualData>;
  checklist?: {title: string; items: {id: string; label: string}[]};
  inlineNext?: string[];
};

export type GuideVisualData = {
  specializationTree?: boolean;
  assetId?: string;
  alt?: string;
  title?: string;
  caption: string;
  steps?: {label: string; description: string}[];
  columns?: string[];
  rows?: {label: string; values: string[]}[];
};

export type GuideAsset = {
  id: string;
  src: string;
  desktopSrc?: string;
  width: number;
  height: number;
  sourceUrl: string;
  originalUrl: string;
  publisher: string;
  region: string;
  version: string;
  checkedAt: string;
  purpose: string;
  imageLanguage: string;
};

export type ArticleSource = {
  id: string;
  title: string;
  url: string;
  kind: 'official' | 'player' | 'community' | 'tool';
  region: 'Global' | 'KR' | 'TW' | 'KR/TW' | 'Mixed';
  publishedAt: string | null;
  version: string;
};

export type ArticleData = {
  slug: TopicSlug;
  edition?: 'Global' | 'TW' | 'KR/TW';
  keyword: string;
  checkedAt: string;
  revision: string;
  regions: string[];
  related: TopicSlug[];
  sources: ArticleSource[];
};

export type ArticleEntry = {
  metadata: ArticleMetadata;
  load: () => Promise<{default: ComponentType<MDXProps>}>;
};
