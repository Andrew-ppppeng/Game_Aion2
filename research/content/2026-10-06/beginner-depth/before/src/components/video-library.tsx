'use client';
import {useState} from 'react';
import type {Locale} from '@/i18n/routing';
import {videoMessages} from '@/i18n/video-messages';
import {beginnerVideos, type VideoStage} from '@/lib/beginner-videos';
import {VideoCard} from './video-card';

export function VideoLibrary({locale}: {locale: Locale}) {
  const [stage, setStage] = useState<VideoStage | 'all'>('all');
  const m = videoMessages[locale];
  const visible = beginnerVideos.filter((video) => stage === 'all' || video.stage === stage);
  return <>
    <div className="video-filters" role="group" aria-label={m.filter}>{(['all', 'start', 'gear'] as const).map((value) => <button key={value} type="button" aria-pressed={stage === value} onClick={() => setStage(value)}>{m[value]}</button>)}</div>
    <p className="video-count" role="status">{visible.length} {m.count}</p>
    <div className="video-grid">{visible.map((video) => <VideoCard key={video.id} video={video} locale={locale} />)}</div>
  </>;
}
