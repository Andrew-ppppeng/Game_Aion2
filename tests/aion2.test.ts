import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {test} from 'node:test';
import {budget, calendarFile, characterId, compareStats, DataError, eventStatus, formatStat, plainName, positiveInteger, readRegion, validateCharacterInfo, validateEquipment, validateItem, validateSearch} from '../src/lib/aion2/model.ts';
import type {EventRecord, Item} from '../src/lib/aion2/types.ts';

const json = (path: string) => JSON.parse(readFileSync(new URL(path, import.meta.url), 'utf8'));
const items = json('../src/content/game-data/items.json');
const events: EventRecord[] = json('../src/content/game-data/events.json');
const cleric = json('./fixtures/cleric.json');
const chanter = json('./fixtures/chanter.json');

test('published examples retain all four localized labels and verified numeric agreement', () => {
  assert.ok(items.length >= 20 && items.length <= 50);
  assert.equal(new Set(items.map((r: {id: number}) => r.id)).size, items.length);
  for (const record of items) {
    let signature;
    for (const locale of ['en', 'ja', 'es', 'de']) {
      const item = validateItem(record.locales[locale].item, record.id);
      assert.equal(item.enchantLevel, 0);
      const numeric = JSON.stringify(item.mainStats.map((s) => [s.id, s.value, s.minValue, s.extra]));
      signature ??= numeric;
      assert.equal(numeric, signature);
      for (const region of ['nae', 'naw', 'eu', 'la']) {
        const meta = record.regionChecks[region][locale];
        assert.equal(meta.valid, true);
        assert.equal(new URL(meta.sourceUrl).searchParams.get('region'), region);
        assert.ok(Number.isFinite(Date.parse(meta.fetchedAt)));
        assert.equal(meta.gameVersion, null);
      }
      assert.equal(record.regionChecks.as[locale].valid, false);
      assert.equal(record.regionChecks.as[locale].reason, 'empty-response');
    }
  }
});

test('actual public character responses validate; missing or malformed responses cannot reach rendering', () => {
  for (const fixture of [cleric, chanter]) {
    const p = fixture.character.data.info.profile;
    assert.equal(validateCharacterInfo(fixture.character.data.info, p.characterId, p.serverId).profile.characterName, p.characterName);
    assert.ok(validateEquipment(fixture.character.data.equipment).equipment.equipmentList.length);
    assert.equal(validateItem(fixture.item.data, fixture.item.data.id).id, fixture.item.data.id);
    assert.throws(() => validateCharacterInfo(fixture.character.data.info, p.characterId, p.serverId + 1), /character-unavailable/);
  }
  assert.throws(() => validateItem(null, 1), /invalid-data/);
  assert.throws(() => validateItem({id: 1, name: '', mainStats: []}, 1), /invalid-item/);
  assert.throws(() => validateEquipment({equipment: {equipmentList: {}}}), /invalid-data/);
  const broken = structuredClone(cleric.character.data.info);
  broken.daevanion.boardList = {};
  assert.throws(() => validateCharacterInfo(broken, broken.profile.characterId, broken.profile.serverId), /invalid-data/);
});

test('inputs preserve Unicode names, normalize encoded IDs, and reject region guessing or URL injection', () => {
  const cid = cleric.character.data.info.profile.characterId;
  assert.equal(characterId(encodeURIComponent(cid)), cid);
  assert.equal(plainName('<em>テスト</em> &amp; Hero'), 'テスト & Hero');
  for (const value of ['asia', 'kr', '', 'invalid']) assert.throws(() => readRegion(value), /invalid-region/);
  for (const value of ['https://example.com', '../admin', 'short', '%invalid']) assert.throws(() => characterId(value), /invalid-input/);
  for (const value of ['1e2', '-1', '0', '9007199254740992']) assert.throws(() => positiveInteger(value), /invalid-input/);
  const data = validateSearch({list: [{characterId: encodeURIComponent(cid), name: '<em>Testa</em>', level: 45, serverId: 2102, serverName: 'Zikel', pcId: 32}], pagination: {page: 1, size: 20, total: 1, endPage: 1}});
  assert.equal(data.list[0].characterId, cid);
  assert.equal(data.list[0].name, 'Testa');
  assert.throws(() => validateSearch({list: [], pagination: {page: '1'}}), /invalid-data/);
});

test('real new-player responses preserve empty title, pet and wing slots without rejecting the character', () => {
  const info = json('./fixtures/asia-new-character-info.json');
  const equipment = json('./fixtures/asia-new-character-equipment.json');
  assert.ok(info.title.titleList.some((t: {name: string | null}) => t.name === null));
  const value = validateCharacterInfo(info, info.profile.characterId, info.profile.serverId);
  assert.equal(value.profile.characterName, info.profile.characterName);
  assert.equal(validateEquipment(equipment).petwing?.pet?.name, null);
  const invalid = structuredClone(info);
  invalid.title.titleList[0].name = {unexpected: true};
  assert.throws(() => validateCharacterInfo(invalid, invalid.profile.characterId, invalid.profile.serverId), /invalid-data/);
});

test('fixed template comparison counts enhancement once and excludes random rolls and breakthrough', () => {
  const base: Item = {id: 1, name: 'Test template', grade: 'Normal', equipLevel: 1, enchantLevel: 0, mainStats: [
    {id: 'attack', name: 'Attack', minValue: '100', value: '200', extra: '20'},
    {id: 'chance', name: 'Chance', value: '10%'},
    {id: 'breakthrough', name: 'Breakthrough', value: '100', extra: '30', exceed: true},
    {id: 'unknown', name: 'Unknown units', value: '1 second'},
  ], subStats: [{id: 'random', name: 'Random', value: '999'}]};
  const next: Item = {...base, id: 2, mainStats: [
    {id: 'attack', name: 'Attack', minValue: '150', value: '230', extra: '50'},
    {id: 'chance', name: 'Chance', value: '12.5%'},
    {id: 'breakthrough', name: 'Breakthrough', value: '100', extra: '40', exceed: true},
    {id: 'unknown', name: 'Unknown units', value: '2 seconds'},
    {id: 'added', name: 'Absent in current item', value: '50'},
  ]};
  assert.deepEqual(compareStats(base, next), [{id: 'attack', name: 'Attack', min: 80, max: 60, unit: 'points'}, {id: 'chance', name: 'Chance', min: 2.5, max: 2.5, unit: 'percent'}]);
  assert.equal(formatStat(base.mainStats[0]), '100–200 (+20)');
  assert.equal(formatStat(base.mainStats[2]), '30');
  const mace = items.find((r: {id: number}) => r.id === 110730048).locales.en.item;
  const starter = items.find((r: {id: number}) => r.id === 110760001).locales.en.item;
  assert.ok(compareStats(starter, mace).some((r) => r.max !== 0), 'Two real mace templates have useful differences');
});

test('UTC event boundaries, pending schedules, DST conversion and calendars remain exact', () => {
  const event = events.find((e) => e.id === 'launch-transition-20261005')!;
  assert.equal(eventStatus(event, Date.parse('2026-10-05T04:59:59Z')), 'upcoming');
  assert.equal(eventStatus(event, Date.parse(event.startAt!)), 'ongoing');
  assert.equal(eventStatus(event, Date.parse(event.endAt!)), 'ended');
  const pending = events.find((e) => e.id === 'war-for-atreia-2-20261007')!;
  assert.equal(eventStatus(pending, Date.parse('2026-10-08T12:00:00Z')), 'unconfirmed');
  assert.equal(calendarFile(pending, pending.titles.en), null);
  assert.equal(calendarFile({...event, endAt: 'invalid'}, 'invalid'), null);
  const calendar = calendarFile(event, 'Name, with; punctuation\nand a newline')!;
  assert.match(calendar, /DTSTART:20261005T050000Z\r\n/);
  assert.match(calendar, /DTEND:20261005T130000Z\r\n/);
  assert.match(calendar, /SUMMARY:Name\\, with\\; punctuation\\nand a newline/);
  const coupon = events.find((e) => e.deadlineOnly)!;
  assert.equal(eventStatus(coupon, Date.parse(coupon.endAt!)), 'ended');
  assert.doesNotMatch(calendarFile(coupon, coupon.titles.en)!, /DTEND/);
  const hour = (date: string) => new Intl.DateTimeFormat('en', {timeZone: 'Europe/Berlin', hour: '2-digit', hourCycle: 'h23'}).format(new Date(date));
  assert.equal(hour('2026-10-24T05:00:00Z'), '07');
  assert.equal(hour('2026-10-26T05:00:00Z'), '06');
});

test('material budget rounds attempts up, respects owned materials and rejects incomplete or unsafe numbers', () => {
  assert.deepEqual(budget(5, 2, 10, [{quantity: 4, owned: 5, price: 2.5}, {quantity: 1, owned: 99, price: 0}]), {attempts: 3, rows: [{required: 12, missing: 7, cost: 17.5}, {required: 3, missing: 0, cost: 0}], total: 47.5});
  for (const args of [[0, 1, 0], [1, 0, 0], [1, 1, -1], [NaN, 1, 0], [1.5, 1, 0]]) assert.throws(() => budget(args[0], args[1], args[2], []), DataError);
  assert.throws(() => budget(1e9, 1, 1, [{quantity: 1e9, owned: 0, price: 1}]), /invalid-input/);
});
