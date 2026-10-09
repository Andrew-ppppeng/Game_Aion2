import assert from 'node:assert/strict';
import {test} from 'node:test';
import {readFile} from 'node:fs/promises';
import {completedGrowth, decodeGrowth, emptyGrowth, growthGoals, isGrowthProgress, starterGoalLinks, toggleGrowth} from '../src/lib/growth-checklist.ts';
import {sectionByTopic, sectionForPath, sectionGroups, sectionIds} from '../src/lib/site-structure.ts';
import {structureMessages} from '../src/i18n/structure-messages.ts';

const starterIds = Object.keys(starterGoalLinks);
test('first visit inherits valid starter goals without accepting unknown or duplicate IDs', () => {
  assert.deepEqual(decodeGrowth(null, JSON.stringify([starterIds[0], starterIds[0], 'unknown', 7]), starterIds).completedIds, [starterIds[0]]);
  assert.deepEqual(decodeGrowth('{broken', '{broken', starterIds), emptyGrowth);
  for (const raw of ['null', '[]', '{"schemaVersion":2}', '{"schemaVersion":1,"templateRevision":1,"completedIds":[null]}']) assert.deepEqual(decodeGrowth(raw, null, starterIds), emptyGrowth);
});
test('saved growth is independent of the starter list and reset stays empty', () => {
  const updated = toggleGrowth(emptyGrowth, 'manual-loop', true);
  assert.deepEqual(decodeGrowth(JSON.stringify(updated), JSON.stringify(starterIds), starterIds), updated);
  assert.deepEqual(decodeGrowth(JSON.stringify(emptyGrowth), JSON.stringify(starterIds), starterIds), emptyGrowth);
  assert.deepEqual(toggleGrowth(updated, 'manual-loop', false), emptyGrowth);
});
test('revised templates retain earlier completion IDs but count only current goals', () => {
  const previous = {schemaVersion: 1 as const, templateRevision: 1, completedIds: ['retired-goal', 'manual-loop', 'manual-loop']};
  const next = toggleGrowth(previous, 'campaign-route', true);
  assert.ok(isGrowthProgress(next));
  assert.ok(next.completedIds.includes('retired-goal'));
  assert.deepEqual([...completedGrowth(next, growthGoals.map((goal) => goal.id))].sort(), ['campaign-route', 'manual-loop']);
});
test('every published article has exactly one main section and localized titles', async () => {
  const published = JSON.parse(await readFile(new URL('../content-topics.json', import.meta.url), 'utf8'));
  const slugs = published.categories.flatMap((group: {keywords: string[]}) => group.keywords.map((keyword) => keyword.replace(/^aion 2 /, '').replaceAll(' ', '-'))).sort();
  const mapped = sectionIds.flatMap((section) => sectionGroups[section].flatMap((group) => [...group.topics]));
  assert.equal(mapped.length, new Set(mapped).size);
  assert.deepEqual([...mapped].sort(), slugs);
  for (const slug of slugs) assert.equal(sectionForPath(`/${slug}`), sectionByTopic[slug as keyof typeof sectionByTopic]);
  assert.equal(sectionForPath('/ja/tools/growth-checklist?ignored=1#goal'), 'tools');
  assert.equal(sectionForPath('/beginner-videos'), 'resources');
  assert.equal(sectionForPath('/unknown'), undefined);
  for (const locale of ['en', 'ja', 'es', 'de'] as const) {
    for (const section of sectionIds) assert.ok(structureMessages[locale].sections[section].title);
    const guide = JSON.parse(await readFile(new URL(`../src/content/${locale}/guide.json`, import.meta.url), 'utf8'));
    assert.deepEqual(guide.checklist.items.map((item: {id: string}) => item.id), starterIds);
    assert.equal(guide.checklist.items.length + growthGoals.length, 12);
    for (const goal of growthGoals) assert.ok(structureMessages[locale].growth.tasks[goal.id].condition);
  }
});
test('all growth guide links retain actual published chapter anchors', async () => {
  for (const href of [...Object.values(starterGoalLinks), ...growthGoals.map((goal) => goal.href)]) {
    const [slug, anchor] = href.slice(1).split('#');
    for (const locale of ['en', 'ja', 'es', 'de']) {
      const body = await readFile(new URL(`../src/content/${locale}/${slug}.mdx`, import.meta.url), 'utf8');
      if (anchor) assert.ok(body.includes(`id="${anchor}"`), `${locale}: ${href}`);
    }
  }
});
