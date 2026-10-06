import records from '@/content/beginner-videos.json';
import type {Locale} from '@/i18n/routing';

export type VideoStage = 'start' | 'gear';
export type BeginnerVideo = {
  id: string; originalTitle: string; channel: string; publishedAt: string;
  durationSeconds: number; language: 'en'; stage: VideoStage; cover: string;
  topics: string[]; titles: Record<Locale, string>; reasons: Record<Locale, string>;
};
export const beginnerVideos = records as BeginnerVideo[];
export function videosForArticle(slug: string) {
  return beginnerVideos.filter((video) => video.topics.includes(slug)).slice(0, 2);
}
export function youtubeUrl(id: string) {return `https://www.youtube.com/watch?v=${id}`;}
