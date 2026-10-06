import Image from 'next/image';
import {ArrowUpRight, Play} from 'lucide-react';
import type {Locale} from '@/i18n/routing';
import {videoMessages} from '@/i18n/video-messages';
import {youtubeUrl, type BeginnerVideo} from '@/lib/beginner-videos';

export function VideoCard({video, locale}: {video: BeginnerVideo; locale: Locale}) {
  const m = videoMessages[locale];
  const duration = `${Math.floor(video.durationSeconds / 60)}:${String(video.durationSeconds % 60).padStart(2, '0')}`;
  return <article className="video-card" data-video-id={video.id}>
    <a className="video-card-cover" href={youtubeUrl(video.id)} target="_blank" rel="noopener noreferrer" aria-label={`${m.watch}: ${video.titles[locale]}`} data-analytics="video">
      <Image src={video.cover} alt="" width={480} height={270} sizes="(max-width: 760px) 100vw, 440px" />
      <span className="video-play" aria-hidden="true"><Play size={20} fill="currentColor" /></span><span className="video-duration">{duration}</span>
    </a>
    <div className="video-card-copy"><span className="video-stage">{m[video.stage]}</span><h3>{video.titles[locale]}</h3>
      <p>{video.reasons[locale]}</p><p className="video-details">{video.channel} · {m.english} · <time dateTime={video.publishedAt}>{new Intl.DateTimeFormat(locale, {dateStyle: 'medium', timeZone: 'UTC'}).format(new Date(`${video.publishedAt}T00:00:00Z`))}</time></p>
      <a href={youtubeUrl(video.id)} target="_blank" rel="noopener noreferrer" data-analytics="video">{m.watch}<ArrowUpRight size={14} aria-hidden="true" /></a>
    </div>
  </article>;
}
