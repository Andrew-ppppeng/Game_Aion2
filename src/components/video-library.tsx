'use client';
import {useState} from 'react';
import type {Locale} from '@/i18n/routing';
import {videoMessages} from '@/i18n/video-messages';
import {beginnerVideos, videoCategories, videoMatches, type VideoCategory} from '@/lib/beginner-videos';
import {VideoCard} from './video-card';

export function VideoLibrary({locale}: {locale: Locale}) {
  const [category, setCategory] = useState<VideoCategory | 'all'>('all');
  const [query, setQuery] = useState('');
  const [hideClasses, setHideClasses] = useState(false);
  const m = videoMessages[locale];
  const visible = beginnerVideos.filter((video) => (category === 'all' || video.category === category) && (!hideClasses || video.category !== 'class') && videoMatches(video, query, locale));
  return <>
    <div className="video-search"><label htmlFor="video-search">{m.search}</label><input id="video-search" type="search" value={query} placeholder={m.searchPlaceholder} onChange={(event) => setQuery(event.target.value)} /><label className="video-class-toggle"><input type="checkbox" checked={hideClasses} onChange={(event) => {setHideClasses(event.target.checked); if (event.target.checked && category === 'class') setCategory('all');}} />{m.hideClasses}</label></div>
    <div className="video-filters" role="group" aria-label={m.filter}>{(['all', ...videoCategories] as const).filter((value) => !hideClasses || value !== 'class').map((value) => <button key={value} type="button" data-category={value} aria-pressed={category === value} onClick={() => setCategory(value)}>{value === 'all' ? m.all : m.categories[value]}</button>)}</div>
    <p className="video-count" role="status">{visible.length} {m.count}</p>
    {!visible.length && <p className="video-empty">{m.empty}<button type="button" onClick={() => {setQuery(''); setCategory('all'); setHideClasses(false);}}>{m.reset}</button></p>}
    <div className="video-grid">{visible.map((video) => <VideoCard key={video.id} video={video} locale={locale} />)}</div>
  </>;
}
