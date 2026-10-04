import {readFile} from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';
import {ImageResponse} from 'next/og';
import {hasLocale} from 'next-intl';
import {routing} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {toolMessages} from '@/i18n/tool-messages';
import {getArticle} from '@/lib/articles';
import {getTopic} from '@/lib/topics';
import {site} from '@/lib/site';
import assets from '@/content/guide-assets.json';

export const runtime = 'nodejs';

const fallbackAssets: Record<string, string> = {
  guide: 'world-elyos',
  maps: 'world-elyos',
  classSelection: 'class-gladiator',
  buildsAndSkills: 'class-cleric',
  characterCustomization: 'style-shop-global-filters',
  codes: 'coupon-rewards-global',
  twitchRewards: 'twitch-white-headset',
  servers: 'steam-fortress',
  platforms: 'steam-crystal-cavern',
  installationAndControls: 'steam-crystal-cavern',
  monetizationAndTrading: 'steam-party-encounter',
  damageMeters: 'steam-party-encounter',
  playerStatistics: 'steam-party-encounter',
  factions: 'world-asmodians',
  macros: 'macro-global-editor',
  pvp: 'steam-fortress',
};

type Props = {params: Promise<{locale: string; slug: string}>};

export async function GET(_request: Request, {params}: Props) {
  const {locale, slug} = await params;
  if (!hasLocale(routing.locales, locale)) return new Response('Not found', {status: 404});
  const article = getArticle(locale, slug);
  const topic = getTopic(slug);
  const character = slug === 'character';
  if (!article && !character) return new Response('Not found', {status: 404});
  const m = getSiteMessages(locale);
  const title = article ? article.metadata.title : toolMessages[locale].characterTitle;
  const edition = article?.data.edition || 'Global';
  const label = topic ? m.categories[topic.category] : toolMessages[locale].characterTitle;
  const featured = article && Object.values(article.metadata.visuals || {}).find((visual) => visual.assetId)?.assetId;
  const asset = assets.find(({id}) => id === (featured || (topic && fallbackAssets[topic.category]) || 'class-gladiator'))!;
  const mediaPath = asset.desktopSrc || asset.src;
  // Satori accepts PNG/JPEG data URLs, but does not decode our WebP class art.
  const media = await sharp(await readFile(path.join(process.cwd(), 'public', mediaPath))).resize(440, 630, {fit: 'cover'}).png().toBuffer();
  const source = `data:image/png;base64,${media.toString('base64')}`;
  const fonts = locale === 'ja' ? [{name: 'Noto Share JP', data: await readFile(path.join(process.cwd(), 'public/fonts/aion2-share-ja.woff')), weight: 600 as const, style: 'normal' as const}] : undefined;

  return new ImageResponse(
    <div style={{width: '100%', height: '100%', display: 'flex', background: '#0b1422', color: '#f2f4f6', fontFamily: locale === 'ja' ? 'Noto Share JP' : 'geist'}}>
      <div style={{width: 760, height: '100%', display: 'flex', flexDirection: 'column', padding: '58px 58px 48px', justifyContent: 'space-between'}}>
        <div style={{display: 'flex', fontSize: 28, color: '#d7b878'}}>{site.name}</div>
        <div style={{display: 'flex', flexDirection: 'column', gap: 24}}>
          <div style={{display: 'flex', fontSize: 24, color: '#aec1d7'}}>{label}</div>
          <div style={{display: 'flex', fontSize: locale === 'ja' ? 48 : 58, lineHeight: 1.15, fontWeight: locale === 'ja' ? 600 : 400, letterSpacing: '-1px'}}>{title}</div>
        </div>
        <div style={{display: 'flex', fontSize: 22, color: '#aec1d7'}}>{edition} · {locale.toUpperCase()} · {slug}</div>
      </div>
      {/* Already sourced game art or a real guide capture; never fabricated UI. */}
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={source} alt="" width={440} height={630} style={{objectFit: 'cover', objectPosition: 'center', opacity: 0.85}} />
    </div>,
    {width: 1200, height: 630, fonts, headers: {'Cache-Control': 'public, max-age=86400, s-maxage=86400, stale-while-revalidate=604800'}},
  );
}
