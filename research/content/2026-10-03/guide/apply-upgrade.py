import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
OWNED = {'guide', 'gathering', 'leveling', 'map', 'character-creation', 'presets', 'download'}
slug = sys.argv[1]
assert slug in OWNED
plan_path = ROOT / 'research/content/2026-10-03' / slug / 'upgrade-plan.json'
plan = json.loads(plan_path.read_text(encoding='utf-8'))

def heading(body, anchor):
    match = re.search(r'<h2 id="' + re.escape(anchor) + r'">[^<]+</h2>', body)
    assert match, anchor
    return match

for locale in ['en', 'ja', 'es', 'de']:
    content_dir = ROOT / 'src/content' / locale
    mdx_path = content_dir / (slug + '.mdx')
    metadata_path = content_dir / (slug + '.json')
    body = mdx_path.read_text(encoding='utf-8')
    assert '<GuideVisual' not in body, f'{locale}/{slug}: upgrade already applied'
    language_plan = plan['locales'][locale]
    for replacement in language_plan.get('replaceFirstParagraph', []):
        match = heading(body, replacement['anchor'])
        rest = body[match.end():]
        paragraph = re.search(r'\n\s*\n([^\n]+(?:\n(?!\s*\n)[^\n]+)*)', rest)
        assert paragraph and '](' not in paragraph.group(1), 'Keep all original source links'
        begin = match.end() + paragraph.start(1)
        end = match.end() + paragraph.end(1)
        body = body[:begin] + replacement['text'] + body[end:]
    for insertion in language_plan['insertions']:
        match = heading(body, insertion['anchor'])
        if insertion['position'] == 'afterHeading':
            point = match.end()
        elif insertion['position'] == 'sectionEnd':
            following = re.search(r'<h2 id="', body[match.end():])
            point = match.end() + following.start() if following else len(body)
        else:
            raise ValueError(insertion['position'])
        body = body[:point].rstrip() + '\n\n' + insertion['text'].strip() + '\n\n' + body[point:].lstrip()
    if slug == 'leveling':
        for anchor, following, faction in [
            ('elyos-route', 'asmodian-route', 'elyos'),
            ('asmodian-route', 'dungeon-checkpoints', 'asmodians'),
        ]:
            begin = heading(body, anchor).start()
            end = heading(body, following).start()
            section = body[begin:end].strip()
            body = body[:begin] + f'<GuideFaction faction="{faction}">\n\n' + section + '\n\n</GuideFaction>\n\n' + body[end:]
    body = body.rstrip() + '\n\n' + plan['next'] + '\n'
    metadata = json.loads(metadata_path.read_text(encoding='utf-8'))
    metadata.update(language_plan['metadata'])
    mdx_path.write_text(body, encoding='utf-8')
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

data_path = ROOT / 'src/content/article-data' / (slug + '.json')
data = json.loads(data_path.read_text(encoding='utf-8'))
data['checkedAt'] = '2026-10-03'
data['revision'] = '2026-10-03.1'
for update in plan.get('sourceUpdates', []):
    source = next(item for item in data['sources'] if item['id'] == update['id'])
    source.update({key: value for key, value in update.items() if key != 'id'})
for source in plan.get('sources', []):
    assert source['id'] not in [item['id'] for item in data['sources']]
    data['sources'].append(source)
data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{slug}: upgraded all four locales; original heading IDs retained')
