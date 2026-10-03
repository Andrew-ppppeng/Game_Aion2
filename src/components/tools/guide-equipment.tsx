import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {toolMessages} from '@/i18n/tool-messages';
import {itemCards} from '@/lib/aion2/data';
import {ItemDetails} from './item-details';

export function GuideEquipment({locale, slug}: {locale: Locale; slug: string}) {
  const m = toolMessages[locale];
  const items = itemCards(locale, slug);
  return <section className="game-tool" data-equipment-cards={slug}>
    <h3>{m.itemsTitle}</h3><p className="tool-note">{m.itemsNote}</p>
    <div className="item-grid">{items.slice(0, 2).map((entry) => <ItemDetails key={entry.data!.id} item={entry.data!} meta={entry.meta} locale={locale} />)}</div>
    {items.length > 2 && <details className="tool-details"><summary>{m.moreItems} ({items.length - 2})</summary><div className="item-grid">{items.slice(2).map((entry) => <ItemDetails key={entry.data!.id} item={entry.data!} meta={entry.meta} locale={locale} />)}</div></details>}
    <Link href="/tools/character" className="tool-link">{m.openCharacter} →</Link>
  </section>;
}
