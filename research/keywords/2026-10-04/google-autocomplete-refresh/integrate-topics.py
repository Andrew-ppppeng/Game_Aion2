import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
LOCALES = ['en', 'ja', 'es', 'de']
NEW_TOPICS = {
    'wings': ('wings and flight', 'wingsAndFlight', ['builds', 'pvp']),
    'database': ('databases', 'databases', ['map', 'builds']),
    'global-changes': ('regional differences', 'regionalDifferences', ['guide', 'monetization']),
}
LABELS = {
    'en': {'categories': ['Wings & flight', 'Databases', 'Regional differences'], 'topics': ['Wings', 'Database', 'Global changes']},
    'ja': {'categories': ['ウイングと飛行', 'データベース', '地域・バージョンの違い'], 'topics': ['ウイング', 'データベース', 'Global版の変更点']},
    'es': {'categories': ['Alas y vuelo', 'Bases de datos', 'Diferencias regionales'], 'topics': ['Alas', 'Base de datos', 'Cambios de Global']},
    'de': {'categories': ['Flügel und Flug', 'Datenbanken', 'Regionale Unterschiede'], 'topics': ['Flügel', 'Datenbank', 'Global-Änderungen']},
}

def read_json(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))

def write_json(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def replace_once(text, old, new):
    assert text.count(old) == 1, f'Unique integration marker: {old}'
    return text.replace(old, new, 1)

# Publish only after every new localized body, metadata and evidence record exists.
for slug in NEW_TOPICS:
    shared = read_json(f'src/content/article-data/{slug}.json')
    assert shared['slug'] == slug and shared['keyword'] == 'aion 2 ' + slug.replace('-', ' ')
    assert len(shared['sources']) >= 2
    for locale in LOCALES:
        meta = read_json(f'src/content/{locale}/{slug}.json')
        body = (ROOT / f'src/content/{locale}/{slug}.mdx').read_text(encoding='utf-8')
        assert len(meta['toc']) >= 4 and len(body) > (900 if locale == 'ja' else 1800)

manifest = read_json('content-topics.json')
old_slugs = [keyword.removeprefix('aion 2 ').replace(' ', '-') for group in manifest['categories'] for keyword in group['keywords']]
assert len(old_slugs) == 28 and all(slug not in old_slugs for slug in NEW_TOPICS)
with (OUT / 'before-content-topics.json').open('x', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

articles_path = ROOT / 'src/lib/articles.ts'
articles = articles_path.read_text(encoding='utf-8')
anchor = "import data_gladiator from '@/content/article-data/gladiator.json';"
articles = replace_once(articles, anchor, anchor + '\n' + '\n'.join(f"import data_{slug.replace('-', '_')} from '@/content/article-data/{slug}.json';" for slug in NEW_TOPICS))
for locale in LOCALES:
    anchor = f"import meta_{locale}_gladiator from '@/content/{locale}/gladiator.json';"
    articles = replace_once(articles, anchor, anchor + '\n' + '\n'.join(f"import meta_{locale}_{slug.replace('-', '_')} from '@/content/{locale}/{slug}.json';" for slug in NEW_TOPICS))
    anchor = f"    'gladiator': {{metadata: meta_{locale}_gladiator, load: () => import('@/content/{locale}/gladiator.mdx')}},"
    additions = '\n'.join(f"    '{slug}': {{metadata: meta_{locale}_{slug.replace('-', '_')}, load: () => import('@/content/{locale}/{slug}.mdx')}}," for slug in NEW_TOPICS)
    articles = replace_once(articles, anchor, anchor + '\n' + additions)
anchor = "  'gladiator': data_gladiator,"
articles = replace_once(articles, anchor, anchor + '\n' + '\n'.join(f"  '{slug}': data_{slug.replace('-', '_')}," for slug in NEW_TOPICS))
articles_path.write_text(articles, encoding='utf-8')

topics_path = ROOT / 'src/lib/topics.ts'
topics = topics_path.read_text(encoding='utf-8')
anchor = "  macros: 'macros',"
topics = replace_once(topics, anchor, anchor + '\n' + '\n'.join(f"  '{category}': '{category_id}'," for category, category_id, _ in NEW_TOPICS.values()))
topics_path.write_text(topics, encoding='utf-8')

paths_path = ROOT / 'src/lib/reading-paths.ts'
paths = paths_path.read_text(encoding='utf-8')
anchor = "  'macro-guide': ['builds', 'notmeter'], 'server-transfer': ['server', 'maintenance'],"
additions = '\n'.join(f"  '{slug}': {json.dumps(targets)}," for slug, (_, _, targets) in NEW_TOPICS.items()).replace('"', "'")
paths = replace_once(paths, anchor, anchor + '\n' + additions)
paths_path.write_text(paths, encoding='utf-8')

for locale in LOCALES:
    ui = read_json(f'src/messages/{locale}.json')
    for i, (slug, (_, category_id, _)) in enumerate(NEW_TOPICS.items()):
        assert slug not in ui['topics'] and category_id not in ui['categories']
        ui['topics'][slug] = LABELS[locale]['topics'][i]
        ui['categories'][category_id] = LABELS[locale]['categories'][i]
    write_json(f'src/messages/{locale}.json', ui)

for slug, (category, _, _) in NEW_TOPICS.items():
    manifest['categories'].append({'category': category, 'keywords': ['aion 2 ' + slug.replace('-', ' ')]})
write_json('content-topics.json', manifest)

# Human decisions: categories and synonym merging are specified explicitly.
selected = read_json('research/keywords/2026-10-04/similarweb-low-kd/selected-keywords.json')['groups']
keyword_categories = {
    'aion 2 max level': 'guide',
    'aion 2 dps meter': 'damage meters',
    'aion 2 global changes': 'regional differences',
    'aion 2 how to play on taiwan server': 'installation and controls',
    'aion 2 private server': 'servers',
    'aion 2 global server': 'servers',
    'aion 2 console release': 'platforms',
    'aion 2 how to play': 'guide',
    'aion 2 new class': 'class selection',
    'aion 2 eu release date': 'release schedule',
    'aion 2 class change': 'class selection',
    'aion 2 gathering map': 'maps',
    'aion 2 talent calculator': 'builds and skills',
    'aion 2 what does quna do': 'monetization and trading',
    'aion 2 how many players per server': 'servers',
    'aion 2 eu server location': 'servers',
    'aion 2 raid 2026': 'dungeons and raids',
    'aion 2 taiwan discord': 'community',
    'aion 2 fishing release': 'fishing',
    'aion 2 are maps connected to aion 1': 'maps',
    'aion 2 can i use vpn and connect to japan to play': 'regional availability',
    'aion 2 how much do i have to p2w in global release': 'monetization and trading',
    'aion 2 classes': 'class selection',
    'aion 2 wings': 'wings and flight',
    'aion 2 database': 'databases',
    'aion 2 specs': 'installation and controls',
}
assert set(keyword_categories) == {group['keyword'] for group in selected} | {'aion 2 classes', 'aion 2 wings', 'aion 2 database', 'aion 2 specs'}
aliases = {'aion 2 specs': 'aion 2 system requirements'}
library = read_json('keywords.json')
original_keywords = [keyword for group in library['categories'] for keyword in group['keywords']]
assert len(original_keywords) == 63
with (OUT / 'before-keywords.json').open('x', encoding='utf-8') as f:
    json.dump(library, f, ensure_ascii=False, indent=2)
by_category = {group['category']: group for group in library['categories']}
seen = set(original_keywords)
added = []
for raw, category in keyword_categories.items():
    canonical = aliases.get(raw, raw)
    if canonical in seen:
        continue
    assert re.fullmatch(r'aion 2 [a-z0-9]+(?: [a-z0-9]+)*', canonical)
    if category not in by_category:
        group = {'category': category, 'keywords': []}
        library['categories'].append(group)
        by_category[category] = group
    by_category[category]['keywords'].append(canonical)
    seen.add(canonical)
    added.append(canonical)
assert set(original_keywords) <= seen and len(seen) == 87
# Preserve the existing compact category-array formatting.
category_blocks = ['    {\n      "category": ' + json.dumps(group['category']) + ',\n      "keywords": ' + json.dumps(group['keywords'], ensure_ascii=False) + '\n    }' for group in library['categories']]
extra = ',\n'.join('  ' + json.dumps(key) + ': ' + json.dumps(value, ensure_ascii=False, indent=2).replace('\n', '\n  ') for key, value in library.items() if key != 'categories')
(ROOT / 'keywords.json').write_text('{\n  "categories": [\n' + ',\n'.join(category_blocks) + '\n  ],\n' + extra + '\n}\n', encoding='utf-8')
write_json(str((OUT / 'integration-result.json').relative_to(ROOT)), {'oldTopics': len(old_slugs), 'newTopics': list(NEW_TOPICS), 'publishedTopics': 31, 'localizedArticles': 124, 'originalKeywords': 63, 'addedCanonicalKeywords': added, 'canonicalKeywordCount': 87, 'synonyms': aliases, 'historicalPriority20': 'preserved unchanged'})
print('Integrated 31 topics / 124 localized articles; library 87 canonical keywords (24 additions, specs merged with system requirements).')
