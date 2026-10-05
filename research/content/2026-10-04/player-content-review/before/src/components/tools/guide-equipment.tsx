import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {toolMessages} from '@/i18n/tool-messages';
import {itemCards} from '@/lib/aion2/data';
import {ItemDetails} from './item-details';
import {MoreEquipment} from '../guide-interactions';

export function GuideEquipment({locale, slug}: {locale: Locale; slug: string}) {
  const m = toolMessages[locale];
  const items = itemCards(locale, slug);
  return <section className="game-tool" data-equipment-cards={slug}>
    <h3>{m.itemsTitle}</h3><p className="tool-note">{m.itemsNote}</p>
    <div className="item-grid">{items.slice(0, 2).map((entry) => <ItemDetails key={entry.data!.id} item={entry.data!} meta={entry.meta} locale={locale} />)}</div>
    {items.length > 2 && <><MoreEquipment locale={locale} slug={slug} count={items.length - 2} /><noscript><ul>{items.slice(2).map((entry) => <li key={entry.data!.id}><a href={entry.meta!.sourceUrl} target="_blank" rel="noopener noreferrer">{entry.data!.name}</a></li>)}</ul></noscript></>}
    <Link href="/tools/character" className="tool-link">{m.openCharacter} →</Link>
  </section>;
}
