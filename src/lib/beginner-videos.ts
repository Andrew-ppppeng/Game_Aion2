import records from '@/content/beginner-videos.json';
import type {Locale} from '@/i18n/routing';

export const videoCategories = ['basics', 'first-day', 'settings', 'leveling', 'level-45', 'gear', 'crafting', 'week-one', 'mistakes', 'class'] as const;
export type VideoCategory = typeof videoCategories[number];
export type BeginnerVideo = {
  id: string; originalTitle: string; channel: string; publishedAt: string;
  durationSeconds: number; language: 'en'; category: VideoCategory; cover: string;
  startSeconds: number; featuredRank?: number; articleStarts: Partial<Record<string, number>>;
  chapters: {seconds: number; labels: Record<Locale, string>}[];
  topics: string[]; titles: Record<Locale, string>; reasons: Record<Locale, string>;
};
export const beginnerVideos = records as BeginnerVideo[];
export function videosForArticle(slug: string) {
  return beginnerVideos.filter((video) => video.topics.includes(slug)).slice(0, 3);
}
export function featuredVideos() {
  return beginnerVideos.filter((video) => video.featuredRank !== undefined).sort((a, b) => a.featuredRank! - b.featuredRank!).slice(0, 6);
}
export function youtubeUrl(id: string, seconds = 0) {return `https://www.youtube.com/watch?v=${id}${seconds > 0 ? `&t=${seconds}s` : ''}`;}
export function videoMatches(video: BeginnerVideo, query: string, locale: Locale) {
  const haystack = [video.titles[locale], video.reasons[locale], video.originalTitle, video.channel, ...video.topics, ...video.chapters.map((c) => c.labels[locale])].join(' ').normalize('NFKC').toLocaleLowerCase(locale);
  return query.normalize('NFKC').toLocaleLowerCase(locale).trim().split(/\s+/).every((term) => haystack.includes(term));
}
