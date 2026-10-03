import rawAssets from '@/content/guide-assets.json';
import type {GuideAsset} from './article-types';

export const guideAssets = rawAssets as GuideAsset[];
export function getGuideAsset(id: string) {
  const asset = guideAssets.find((entry) => entry.id === id);
  if (!asset) throw new Error(`Unknown guide asset: ${id}`);
  return asset;
}
