"""Focused check for the newly authored localized documents before registration."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
REPORT = []
for slug in ['wings', 'database', 'global-changes']:
    baseline = None
    for locale in ['en', 'ja', 'es', 'de']:
        base = ROOT / 'src' / 'content' / locale
        meta = json.loads((base / (slug + '.json')).read_text(encoding='utf-8'))
        body = (base / (slug + '.mdx')).read_text(encoding='utf-8')
        ids = re.findall(r'<h2 id="([a-z0-9-]+)">', body)
        assert ids == [row['id'] for row in meta['toc']] and len(ids) >= 4
        assert len(body) > (900 if locale == 'ja' else 1800)
        assert '\ufffd' not in body + json.dumps(meta, ensure_ascii=False)
        assert re.findall(r'<GuideNext slug="([a-z0-9-]+)" />', body) == meta['inlineNext']
        assert re.findall(r'<GuideVisual id="([a-z0-9-]+)" />',body) == list(meta['visuals'])
        assert len(meta['visuals']['workflow']['steps']) == 4
        assert meta['summary'] != meta['quickAnswer']
        assert not re.search(r'\bTODO\b|\bTBD\b|^# ',body,re.M)
        assert not re.search(r'^Sources\s*$|>Sources<|Image source|according to|unverified',body,re.I|re.M)
        shape = {
            'ids': ids,
            'components': re.findall(r'<Guide[^>]+>',body),
            'links': sorted(re.findall(r'\]\(([^)]+)\)',body)),
            'htmlLinks': re.findall(r'<a href="([^"]+)">',body),
            'tables': [row.count('|') for row in body.splitlines() if row.startswith('|')],
        }
        if baseline is None:
            baseline = shape
        else:
            assert shape == baseline, (slug, locale, shape, baseline)
        REPORT.append({'slug':slug,'locale':locale,'bodyCharacters':len(body),'sections':len(ids),'status':'passed'})
    data = json.loads((ROOT / 'src/content/article-data' / (slug + '.json')).read_text(encoding='utf-8'))
    assert data['slug'] == slug and 'Global' in data['regions']
    assert len(data['related']) >= 2 and len(data['sources']) >= 2
    assert len({row['id'] for row in data['sources']}) == len(data['sources'])
    assert all(row['url'].startswith('https://') and row['version'] for row in data['sources'])
    if slug == 'wings':
        for locale in ['en','ja','es','de']:
            body = (ROOT/'src/content'/locale/'wings.mdx').read_text(encoding='utf-8')
            assert not re.search(r'enhancement panel|upgrade cost|owned.*level|強化画面|panel.*mejora|Verbesserungsfenster',body,re.I)
target = OUT / 'localized-content-check.json'
with target.open('x',encoding='utf-8') as handle:
    json.dump(REPORT,handle,ensure_ascii=False,indent=2)
print('PASS: 12 localized pages; stable anchors, links, tables and visual placements; valid internal evidence')
