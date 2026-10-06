import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {videoMessages} from '@/i18n/video-messages';
import {featuredVideos, videosForArticle} from '@/lib/beginner-videos';
import {VideoCard} from './video-card';

export function VideoRecommendations({locale, slug}: {locale: Locale; slug?: string}) {
  const videos = slug ? videosForArticle(slug) : featuredVideos();
  if (!videos.length) return null;
  const m = videoMessages[locale];
  return <section className={slug ? 'article-video-section' : 'content-section video-home-section'} aria-labelledby={slug ? 'recommended-videos-title' : 'home-videos-title'}>
    <div className="section-heading"><h2 id={slug ? 'recommended-videos-title' : 'home-videos-title'}>{slug ? m.recommended : m.homeTitle}</h2><Link href="/beginner-videos">{m.browse}</Link></div>
    <div className="video-grid">{videos.map((video) => <VideoCard key={video.id} video={video} locale={locale} topic={slug} />)}</div>
  </section>;
}
