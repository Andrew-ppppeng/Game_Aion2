import {ArrowRight} from 'lucide-react';
import type {Locale} from '@/i18n/routing';
import {guideMessages} from '@/i18n/guide-messages';
import {getGuideAsset} from '@/lib/guide-assets';
import type {GuideVisualData} from '@/lib/article-types';
import {GuideImage} from './guide-image';

export function GuideVisual({id, visual, locale}: {id: string; visual: GuideVisualData; locale: Locale}) {
  const m = guideMessages[locale];
  if (visual.assetId) {
    const asset = getGuideAsset(visual.assetId);
    return <figure className="guide-figure" data-visual-id={id} data-asset-id={asset.id}>
      <GuideImage src={asset.src} width={asset.width} height={asset.height} alt={visual.alt || visual.caption} locale={locale} />
      <figcaption><p>{visual.caption}</p></figcaption>
    </figure>;
  }
  return <figure className={`guide-diagram${visual.rows ? ' comparison' : ''}`} data-visual-id={id} aria-label={visual.title}>
    <figcaption><span className="eyebrow">{m.illustration}</span><strong>{visual.title}</strong><p>{visual.caption}</p></figcaption>
    {visual.steps && <ol>{visual.steps.map((step, index) => <li key={`${id}-${index}`}><span className="diagram-number" aria-hidden="true">{index + 1}</span><div><strong>{step.label}</strong><p>{step.description}</p></div>{index < visual.steps!.length - 1 && <ArrowRight className="diagram-arrow" size={17} aria-hidden="true" />}</li>)}</ol>}
    {visual.rows && <div className="comparison-grid">{visual.rows.map((row) => <div key={row.label} className="comparison-row"><strong>{row.label}</strong><div>{row.values.map((value, index) => <span key={index}><small>{visual.columns?.[index]}</small><b>{value}</b></span>)}</div></div>)}</div>}
  </figure>;
}
