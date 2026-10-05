'use client';

import Image from 'next/image';
import {useId, useState} from 'react';
import {ExternalLink, Play} from 'lucide-react';
import type {Locale} from '@/i18n/routing';
import identities from '@/content/class-identities.json';
import media from '@/content/class-videos.json';
import {classMediaMessages} from '@/i18n/class-media-messages';
import type {ClassId} from './guide-skill-list';

export function GuideClassVideo({locale, classId}: {locale: Locale; classId: ClassId}) {
  const [playing, setPlaying] = useState(false);
  const m = classMediaMessages[locale];
  const video = media[classId];
  const identity = identities.find(({id}) => id === classId)!;
  const title = `${identity.names[locale]} — ${m.videoTitle}`;
  return <figure className="class-video" data-class-video={classId}>
    <div className="class-video-screen">{playing ? <iframe
      src={`https://www.youtube-nocookie.com/embed/${video.videoId}?autoplay=1&rel=0&playsinline=1`}
      title={title} allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowFullScreen referrerPolicy="strict-origin-when-cross-origin" />
      : <button type="button" className="class-video-play" onClick={() => setPlaying(true)} aria-label={`${m.play}: ${identity.names[locale]}`}>
        <Image src={video.poster} width={video.width} height={video.height} alt={title} sizes="(max-width: 640px) 100vw, 560px" />
        <span className="class-video-play-mark"><Play size={30} fill="currentColor" aria-hidden="true" /></span>
        <span className="class-video-play-label">{m.play}</span>
      </button>}
    </div>
    <figcaption><strong>{title}</strong><p>{m.videoHint}</p><a href={`https://www.youtube.com/watch?v=${video.videoId}`} target="_blank" rel="noopener noreferrer">{m.watch}<ExternalLink size={13} aria-hidden="true" /></a></figcaption>
  </figure>;
}

export function GuideClassVideos({locale}: {locale: Locale}) {
  const [classId, setClassId] = useState<ClassId>('gladiator');
  const id = useId();
  const m = classMediaMessages[locale];
  return <div className="class-video-gallery" data-video-gallery>
    <label htmlFor={id}>{m.classSelect}<select id={id} value={classId} onChange={(event) => setClassId(event.target.value as ClassId)}>{identities.map((entry) => <option key={entry.id} value={entry.id}>{entry.names[locale]}</option>)}</select></label>
    <GuideClassVideo key={classId} locale={locale} classId={classId} />
  </div>;
}
