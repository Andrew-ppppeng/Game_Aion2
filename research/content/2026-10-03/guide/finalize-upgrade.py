import collections
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[4]
OWNED = ['guide', 'gathering', 'leveling', 'map', 'character-creation', 'presets', 'download']
terms = json.loads((pathlib.Path(__file__).parent / 'localization-terms.json').read_text(encoding='utf-8'))

def localize(value, locale):
    if isinstance(value, dict):
        return {key: localize(item, locale) for key, item in value.items()}
    if isinstance(value, list):
        return [localize(item, locale) for item in value]
    if isinstance(value, str):
        for term, replacement in terms.get(locale, {}).items():
            value = re.sub(r'(?<![A-Za-z])' + re.escape(term) + r'(?![A-Za-z])', replacement, value)
    return value

for slug in OWNED:
    plan_path = ROOT / 'research/content/2026-10-03' / slug / 'upgrade-plan.json'
    plan = json.loads(plan_path.read_text(encoding='utf-8'))
    for locale in ['ja', 'es']:
        plan['locales'][locale] = localize(plan['locales'][locale], locale)
        mdx_path = ROOT / 'src/content' / locale / (slug + '.mdx')
        body = mdx_path.read_text(encoding='utf-8')
        original_urls = collections.Counter(re.findall(r'\]\(([^)]+)\)', body))
        body = localize(body, locale)
        assert collections.Counter(re.findall(r'\]\(([^)]+)\)', body)) == original_urls
        mdx_path.write_text(body, encoding='utf-8')
        meta_path = ROOT / 'src/content' / locale / (slug + '.json')
        metadata = json.loads(meta_path.read_text(encoding='utf-8'))
        metadata.update(plan['locales'][locale]['metadata'])
        meta_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    baseline = None
    for locale in ['en', 'ja', 'es', 'de']:
        body = (ROOT / 'src/content' / locale / (slug + '.mdx')).read_text(encoding='utf-8')
        metadata = json.loads((ROOT / 'src/content' / locale / (slug + '.json')).read_text(encoding='utf-8'))
        assert '\ufffd' not in body and '???' not in body
        assert '\ufffd' not in json.dumps(metadata, ensure_ascii=False) and '???' not in json.dumps(metadata, ensure_ascii=False)
        headings = re.findall(r'<h2 id="([^"]+)"', body)
        assert headings == [item['id'] for item in metadata['toc']]
        assert 3 <= len(metadata['visuals']['workflow']['steps']) <= 5
        assert body.count('<GuideVisual id="topic" />') == 1
        assert body.count('<GuideVisual id="workflow" />') == 1
        assert body.count('<GuideNext ') == 1
        assert body.count('<GuideChecklist />') == (1 if slug in ['guide', 'download'] else 0)
        if slug == 'leveling':
            assert body.count('<GuideFaction faction="elyos">') == 1
            assert body.count('<GuideFaction faction="asmodians">') == 1
            assert body.count('</GuideFaction>') == 2
            assert body.index('</GuideFaction>') < body.index('<GuideFaction faction="asmodians">')
        tables = [len(re.findall(r'(?<!\\)\|', line)) for line in body.splitlines() if line.startswith('|')]
        result = (headings, collections.Counter(re.findall(r'\]\(([^)]+)\)', body)), tables,
                  metadata['visuals']['topic']['assetId'], len(metadata['visuals']['workflow']['steps']),
                  [item['id'] for item in metadata.get('checklist', {}).get('items', [])])
        assert baseline is None or result == baseline, f'{slug}/{locale}: cross-locale structure mismatch'
        baseline = result
    print(f'PASS {slug}: four locales, headings/links/tables/visuals/checklists/encoding')
