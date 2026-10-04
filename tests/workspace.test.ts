import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {test} from 'node:test';
import {decodeBuild, emptyWorkspace, encodeBuild, mergeWorkspace, validBuild, validWorkspace, withRecent, type Build} from '../src/lib/aion2/workspace.ts';
import {parseBackup} from '../src/lib/aion2/backup.ts';
import {validateBoard} from '../src/lib/aion2/nodes.ts';
import {validateItem, compareStats} from '../src/lib/aion2/model.ts';
const plan: Build = {id: 'one', name: '装備 · Überfall', region: 'eu', items: [{slot: 'Main hand', itemId: 110760001, enchantLevel: 3}]};
test('shared plans round-trip Unicode and reject malformed or excessive payloads', () => {
  assert.deepEqual(decodeBuild(encodeBuild(plan)), plan);
  for (const value of ['%', '!!!!', 'a'.repeat(12001), 'e30']) assert.throws(() => decodeBuild(value));
  assert.equal(validBuild({...plan, items: [...plan.items, ...plan.items]}), false);
  assert.equal(validBuild({...plan, items: [{...plan.items[0], enchantLevel: 31}]}), false);
  assert.equal(validBuild({...plan, favorites: [{id: 1, region: 'eu'}]}), false, 'shared plans cannot carry private workspace fields');
});
test('imports preserve existing completion and keep regional identities separate', () => {
  const current = {...emptyWorkspace, goals: [{id: 1, region: 'eu' as const, done: true}]};
  const merged = mergeWorkspace(current, {...emptyWorkspace, goals: [{id: 1, region: 'eu', done: false}, {id: 1, region: 'nae', done: false}]});
  assert.deepEqual(merged.goals, [{id: 1, region: 'eu', done: true}, {id: 1, region: 'nae', done: false}]);
  assert.throws(() => mergeWorkspace(current, {version: 2}));
  assert.equal(current.goals[0].done, true);
});
test('recent items are deduplicated per region and bounded', () => {
  let state = emptyWorkspace;
  for (let id = 1; id <= 35; id++) state = withRecent(state, {id, region: 'nae'});
  state = withRecent(state, {id: 35, region: 'nae'});
  assert.equal(state.recent.length, 30); assert.equal(state.recent[0].id, 35);
  state = withRecent(state, {id: 35, region: 'eu'}); assert.equal(state.recent[1].region, 'nae');
});
test('workspace input rejects bad regions, unsafe numeric data and save limits', () => {
  assert.equal(validWorkspace(emptyWorkspace), true);
  assert.equal(validWorkspace({...emptyWorkspace, favorites: [{id: 1, region: 'kr'}]}), false);
  assert.equal(validWorkspace({...emptyWorkspace, tasks: [{id: '1', text: 'a\n', done: false}]}), false);
  assert.equal(validWorkspace({...emptyWorkspace, builds: Array(31).fill(plan)}), false);
  assert.equal(validWorkspace({...emptyWorkspace, goals: [{id: Number.MAX_SAFE_INTEGER + 1, region: 'eu', done: false}]}), false);
});
test('backup only accepts supported tool keys and validated legacy values', () => {
  assert.deepEqual(parseBackup(emptyWorkspace).workspace, emptyWorkspace);
  const value = {format: 'aion2-backup', version: 1, workspace: emptyWorkspace, tools: {'aion2-region-v1': 'eu', 'aion2-budget-v1': {mode:'craft',goal:'2',yield:'1',fee:'0',rows:[{name:'Ore',quantity:'1',owned:'0',price:'12'}]}}};
  assert.equal(parseBackup(value).tools['aion2-region-v1'], 'eu');
  assert.throws(() => parseBackup({...value, tools: {'aion2-region-v1': 'tw'}}));
  assert.throws(() => parseBackup({...value, tools: {'arbitrary-key': 'secret'}}));
});
test('node data matches its character board and rejects mismatched or duplicate nodes', () => {
  const raw = JSON.parse(readFileSync(new URL('./fixtures/board.json', import.meta.url), 'utf8'));
  const data = validateBoard(raw, 11); assert.ok(data.nodeList.length > 100);
  assert.throws(() => validateBoard(raw, 12));
  assert.throws(() => validateBoard({nodeList: [raw.nodeList[0], raw.nodeList[0]]}, 11));
  assert.throws(() => validateBoard({nodeList: [{...raw.nodeList[0], row: Infinity}]}, 11));
});
test('real +1 template retains enhancement attributes and compares with the same +0 item', () => {
  const enhanced = validateItem(JSON.parse(readFileSync(new URL('./fixtures/enhancement-mace-1.json', import.meta.url), 'utf8')), 110730048);
  const items = JSON.parse(readFileSync(new URL('../src/content/game-data/items.json', import.meta.url), 'utf8'));
  const base = validateItem(items.find((i: {id: number}) => i.id === enhanced.id).locales.en.item, enhanced.id);
  assert.equal(enhanced.enchantLevel, 1); assert.ok(compareStats(base, enhanced).some((s) => s.max > 0));
});
