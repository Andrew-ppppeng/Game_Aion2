import assert from 'node:assert/strict';
import {execFile} from 'node:child_process';
import {existsSync} from 'node:fs';
import {mkdir, readFile} from 'node:fs/promises';
import {join} from 'node:path';
import {promisify} from 'node:util';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const deployment = process.env.QA_VERCEL_DEPLOYMENT;
const run = promisify(execFile);
const cli = process.env.VERCEL_CLI_PATH || join(process.env.APPDATA || '', 'npm', 'node_modules', 'vercel', 'dist', 'vc.js');
const archive = new URL(`../.qa/live-api-${new Date().toISOString().replace(/[:.]/g, '-')}/`, import.meta.url);
if (deployment) {assert.ok(existsSync(cli), 'Set VERCEL_CLI_PATH to the installed Vercel CLI'); await mkdir(archive, {recursive: true});}
let requestCount = 0;
const get = async (path) => {
  let response, result;
  if (deployment) {
    const bodyFile = new URL(`${++requestCount}.json`, archive);
    const headersFile = new URL(`${requestCount}.headers`, archive);
    const {fileURLToPath} = await import('node:url');
    const {stdout} = await run(process.execPath, [cli, 'curl', path, '--deployment', deployment, '--', '--silent', '--output', fileURLToPath(bodyFile), '--dump-header', fileURLToPath(headersFile), '--write-out', '%{http_code}'], {timeout: 75000, maxBuffer: 1024 * 1024});
    const rawHeaders = await readFile(headersFile, 'utf8');
    const last = rawHeaders.split(/\r?\n\r?\n/).filter((block) => /^HTTP\//.test(block)).at(-1);
    const headers = new Headers();
    for (const line of last?.split(/\r?\n/) || []) {
      const index = line.indexOf(':');
      if (index > 0) headers.append(line.slice(0, index), line.slice(index + 1).trim());
    }
    response = {status: Number(stdout.trim().slice(-3)), headers};
    result = JSON.parse(await readFile(bodyFile, 'utf8'));
  } else {
    response = await fetch(base + path, {signal: AbortSignal.timeout(60000)});
    result = await response.json();
  }
  assert.equal(response.headers.get('x-robots-tag'), 'noindex, nofollow');
  assert.match(response.headers.get('cache-control'), /no-store/);
  return {response, ...result};
};
const character = '8iCddEXDDnuEC1Z-27KJQFh1WE-LrCLGFXYvv_9qwb8=';
for (const region of ['nae', 'naw', 'eu', 'la', 'as']) {
  const meta = await get(`/api/aion2/meta?region=${region}`);
  assert.equal(meta.response.status, 200);
  assert.ok(meta.data.servers.length);
  const search = await get(`/api/aion2/characters/search?region=${region}&q=Test&page=1`);
  assert.equal(search.response.status, 200, `${region}: ${search.error?.code}`);
  assert.ok(Array.isArray(search.data.list));
  assert.ok(search.data.list.length <= 20);
  console.log(`PASS: ${region} search and server metadata`);
}
const filtered = await get('/api/aion2/characters/search?region=nae&q=Test&class=Cleric&serverId=2102');
assert.equal(filtered.response.status, 200, filtered.error?.code);
assert.ok(filtered.data.list.every((c) => c.serverId === 2102 && [29, 30, 31, 32].includes(c.pcId)), 'Official search honors class and server filters');
const path = `/api/aion2/characters/${encodeURIComponent(character)}?region=nae&serverId=2102`;
const [profile, simultaneous] = await Promise.all([get(path), get(path)]);
assert.equal(profile.response.status, 200, profile.error?.code);
assert.equal(simultaneous.response.status, 200, simultaneous.error?.code);
assert.equal(profile.meta.fetchedAt, simultaneous.meta.fetchedAt, 'Simultaneous character reads share the same source fetch');
assert.equal(profile.data.info.profile.serverId, 2102);
assert.ok(profile.data.equipment.equipment.equipmentList.length);
const repeat = await get(path);
assert.equal(repeat.meta.freshness, 'cached');
const slot = profile.data.equipment.equipment.equipmentList[0];
const item = await get(`/api/aion2/characters/${encodeURIComponent(character)}/equipment/${slot.slotPos}?region=nae&serverId=2102`);
assert.equal(item.response.status, 200, item.error?.code);
assert.equal(item.data.id, slot.id);
const template = await get(`/api/aion2/items/${slot.id}?region=nae&enchantLevel=0`);
assert.equal(template.response.status, 200);
assert.equal(template.data.enchantLevel, 0);
const upgraded = await get(`/api/aion2/items/${slot.id}?region=nae&enchantLevel=1`);
assert.equal(upgraded.response.status, 200, upgraded.error?.code);
assert.equal(upgraded.data.enchantLevel, 1);
for (const locale of ['ja', 'es', 'de']) {
  const localized = await get(`${path}&locale=${locale}`);
  assert.equal(localized.response.status, 200, `${locale}: ${localized.error?.code}`);
  assert.equal(localized.meta.locale, locale);
  assert.equal(localized.data.info.profile.characterId, character);
}
for (const [url, code] of [
  ['/api/aion2/characters/search?q=', 400],
  ['/api/aion2/characters/search?q=Test&region=kr', 400],
  ['/api/aion2/items/1?region=nae', 404],
  ['/api/aion2/items/110730048?region=as', 503],
  ['/api/aion2/items/110730048?enchantLevel=99', 400],
]) {
  const value = await get(url);
  assert.equal(value.response.status, code, url);
  assert.equal(value.data, null);
  assert.ok(value.error.code);
}
console.log('PASS: live four-language public character, simultaneous/cache reads, actual equipped item, +0/+1 templates and input/region errors.');
