import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir, readFile, writeFile} from 'node:fs/promises';
import {chromium, expect} from '@playwright/test';
import {fileURLToPath} from 'node:url';
const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const json = async (path) => JSON.parse(await readFile(new URL(`../${path}`, import.meta.url), 'utf8'));
const items = await json('src/content/game-data/items.json');
const fixture = await json('tests/fixtures/cleric.json');
const board = await json('tests/fixtures/board.json');
const enhanced = await json('tests/fixtures/enhancement-mace-1.json');
const output = new URL('../.qa/platform/', import.meta.url); await mkdir(output, {recursive: true});
await writeFile(new URL('result.json',output),JSON.stringify({passed:false,status:'running',checkedAt:new Date().toISOString()}));
const browser = await chromium.launch({headless:true, executablePath: process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync('C:/Program Files/Google/Chrome/Application/chrome.exe') ? 'C:/Program Files/Google/Chrome/Application/chrome.exe' : undefined)});
const context = await browser.newContext({viewport:{width:390,height:844}, permissions:['clipboard-read','clipboard-write']});
const page = await context.newPage(); const errors = []; let itemMode = 'normal'; const requests = [];
await context.addInitScript(() => {if (!localStorage.getItem('aion2-budget-v1')) localStorage.setItem('aion2-budget-v1', JSON.stringify({mode:'craft',goal:'2',yield:'1',fee:'0',rows:[{name:'Ore',quantity:'1',owned:'0',price:'12'}]}));});
page.on('pageerror', (error) => errors.push(error.message));
await context.route('**/api/aion2/**', async (route) => {
  const url = new URL(route.request().url()); const locale = url.searchParams.get('locale') || 'en';
  const respond = (body, status=200) => route.fulfill({status,contentType:'application/json',body:JSON.stringify(body)});
  if (url.pathname.includes('/boards/')) return respond({data:board,meta:null,error:null});
  if (url.pathname.includes('/items/')) {
    requests.push(url.href);
    if (itemMode === 'busy') return respond({data:null,meta:null,error:{code:'rate-limited'}},429);
    if (itemMode === 'slow') await new Promise((resolve) => setTimeout(resolve, 500));
    const item = url.searchParams.get('enchantLevel') === '1' ? enhanced : items.find((i) => i.id === Number(url.pathname.split('/').at(-1))).locales[locale].item;
    return respond({data:item,meta:null,error:null});
  }
  if (url.pathname.endsWith('/meta')) return respond({data:null,meta:null,error:null});
  if (url.pathname.includes('/characters/')) return respond(fixture.character);
  throw new Error(`Unexpected request ${url.pathname}`);
});
const path = (locale, slug) => `${base}${locale === 'en' ? '' : `/${locale}`}/${slug}`;
const overflow = async () => assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth+1), 'mobile page fits');
const labels = {
 en:{search:'Search the wiki',favorite:'Save item',goal:'Set upgrade goal',task:'Task',add:'Add',name:'Plan name',create:'Create plan',slot:'Equipment slot label',items:'Items',addItem:'Add item to plan',share:'Copy plan link',savePlan:'Save this plan',export:'Export backup',import:'Import backup',invalid:'This backup is invalid or too large. Your saved plans were kept.'},
 ja:{search:'Wikiを検索',favorite:'アイテムを保存',goal:'強化目標に設定',task:'タスク',add:'追加',name:'計画名',create:'計画を作成',slot:'装備枠のラベル',items:'アイテム',addItem:'計画に装備を追加',share:'計画リンクをコピー',savePlan:'この計画を保存',export:'バックアップを書き出す',import:'バックアップを読み込む',invalid:'無効または大きすぎるバックアップです。保存済みの計画は保持されています。'},
 es:{search:'Buscar en la wiki',favorite:'Guardar objeto',goal:'Añadir objetivo de mejora',task:'Tarea',add:'Añadir',name:'Nombre del plan',create:'Crear plan',slot:'Etiqueta de la ranura',items:'Objetos',addItem:'Añadir objeto al plan',share:'Copiar enlace del plan',savePlan:'Guardar este plan',export:'Exportar copia',import:'Importar copia',invalid:'La copia no es válida o es demasiado grande. Se conservaron tus planes.'},
 de:{search:'Wiki durchsuchen',favorite:'Gegenstand speichern',goal:'Verbesserungsziel setzen',task:'Aufgabe',add:'Hinzufügen',name:'Planname',create:'Plan erstellen',slot:'Bezeichnung des Ausrüstungsplatzes',items:'Gegenstände',addItem:'Gegenstand zum Plan hinzufügen',share:'Planlink kopieren',savePlan:'Diesen Plan speichern',export:'Sicherung exportieren',import:'Sicherung importieren',invalid:'Sicherung ungültig oder zu groß. Deine Pläne wurden beibehalten.'},
};
try {
 for (const locale of ['en','ja','es','de']) {
  const m = labels[locale]; await page.goto(path(locale,'database')); await expect(page.locator('[data-catalogue-item]')).toHaveCount(22); await overflow();
  await page.getByRole('button',{name:m.search,exact:true}).click(); await expect(page.getByRole('dialog')).toBeVisible();
  await page.getByRole('dialog').getByRole('searchbox').fill(String(items[0].id)); await expect(page.getByRole('dialog').locator('.search-results a')).toHaveCount(1);
  await page.keyboard.press('Escape'); await expect(page.getByRole('dialog')).not.toBeVisible();
  await page.keyboard.press('Control+k'); await expect(page.getByRole('dialog')).toBeVisible(); await page.keyboard.press('Escape');
  const catalogue = page.locator('[data-catalogue]'); await catalogue.getByRole('searchbox').fill(String(items[0].id)); await expect(page.locator('[data-catalogue-item]')).toHaveCount(1);
  const card = page.locator('[data-catalogue-item]').first();
  if (locale === 'en') {await card.getByRole('button',{name:m.favorite,exact:true}).click(); await card.getByRole('button',{name:m.goal,exact:true}).click();}
  await card.locator('.catalogue-item-heading').click(); await expect(page.locator('[data-item-view]')).toBeVisible(); await overflow();
  const state = await page.evaluate(() => JSON.parse(localStorage.getItem('aion2-workspace-v1'))); assert.equal(state.favorites.length,1); assert.equal(state.recent.length,1); assert.equal(state.goals.length,1);
  if (locale === 'en') {await page.getByLabel('Enhancement',{exact:true}).selectOption('1'); await page.getByRole('button',{name:'Inspect',exact:true}).click(); await expect(page.locator('[data-item-view] h4')).toContainText('+1');}
  await page.goto(path(locale,'workspace')); await page.getByLabel(m.task,{exact:true}).fill(`Task ${locale}`); await page.getByRole('button',{name:m.add,exact:true}).click();
  await page.getByLabel(m.name,{exact:true}).fill(`装備 · Überfall ${locale}`); await page.getByRole('button',{name:m.create,exact:true}).click();
  await page.getByLabel(m.items,{exact:true}).selectOption(String(items[0].id)); await page.getByLabel(m.slot,{exact:true}).fill('Main hand'); await page.getByRole('button',{name:m.addItem,exact:true}).click();
  await page.getByRole('button',{name:m.share,exact:true}).click(); const url = await page.evaluate(() => navigator.clipboard.readText()); assert.ok(url.includes('#plan=')); assert.ok(!url.includes('Task'));
  const [download] = await Promise.all([page.waitForEvent('download'),page.getByRole('button',{name:m.export,exact:true}).click()]); const backup = JSON.parse(await readFile(await download.path(),'utf8')); assert.equal(backup.workspace.favorites.length,1); assert.ok(backup.workspace.builds.length); assert.equal(backup.tools['aion2-budget-v1'].rows[0].name,'Ore');
  const before = await page.evaluate(() => localStorage.getItem('aion2-workspace-v1'));
  await page.getByLabel(m.import,{exact:true}).setInputFiles({name:'bad.json',mimeType:'application/json',buffer:Buffer.from('{"version":2}')}); await expect(page.getByText(m.invalid,{exact:true})).toBeVisible(); assert.equal(await page.evaluate(() => localStorage.getItem('aion2-workspace-v1')),before);
  const other = await browser.newContext({viewport:{width:390,height:844}}); const shared = await other.newPage(); await shared.goto(url); await expect(shared.getByRole('button',{name:m.savePlan,exact:true})).toBeVisible(); await shared.getByRole('button',{name:m.savePlan,exact:true}).click(); const imported = await shared.evaluate(() => JSON.parse(localStorage.getItem('aion2-workspace-v1'))); assert.equal(imported.builds.length,1); assert.equal(imported.favorites.length,0); assert.equal(imported.tasks.length,0);
  await shared.getByLabel(m.import,{exact:true}).setInputFiles({name:'backup.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(backup))}); await expect.poll(() => shared.evaluate(() => JSON.parse(localStorage.getItem('aion2-workspace-v1')).favorites.length)).toBe(1); assert.equal(await shared.evaluate(() => JSON.parse(localStorage.getItem('aion2-budget-v1')).rows[0].name),'Ore'); assert.ok((await shared.evaluate(() => JSON.parse(localStorage.getItem('aion2-workspace-v1')).tasks.length)) > 0); await other.close();
  await overflow(); await page.screenshot({path:fileURLToPath(new URL(`workspace-${locale}.png`,output)),fullPage:true});
 }
 await page.goto(path('en','database')); await page.getByLabel('Game region',{exact:true}).selectOption('as'); await expect(page.getByText('Equipment data is unavailable for this region.',{exact:true})).toBeVisible(); await expect(page.locator('[data-catalogue-item]')).toHaveCount(0);
 await page.goto(path('en','workspace')); assert.ok(await page.getByLabel('Game region',{exact:true}).locator('option').filter({hasText:/^as$/}).evaluate((option) => option.disabled), 'Unavailable regions cannot create equipment plans');
 await page.goto(path('en',`tools/compare?first=${items[0].id}&second=${items[1].id}`)); await page.getByRole('button',{name:'Compare',exact:true}).click(); await expect(page.locator('[data-equipment-compare] .item-card')).toHaveCount(2); assert.equal(requests.length,3); await overflow();
 itemMode='busy'; await page.getByRole('button',{name:'Compare',exact:true}).click(); await expect(page.locator('[data-equipment-compare]').getByRole('alert')).toContainText('wait'); await expect(page.locator('[data-equipment-compare] .item-card')).toHaveCount(0);
 itemMode='slow'; await page.getByRole('button',{name:'Compare',exact:true}).click(); await page.getByLabel('Game region',{exact:true}).selectOption('as'); await page.waitForTimeout(700); await expect(page.locator('[data-equipment-compare] .item-card')).toHaveCount(0);
 await page.goto(path('en',`tools/character?${new URLSearchParams({cid:fixture.character.data.info.profile.characterId,serverId:String(fixture.character.data.info.profile.serverId),region:'eu'})}`));
 await page.getByRole('button',{name:'Save character snapshot',exact:true}).click(); await page.getByRole('button',{name:'Save character snapshot',exact:true}).click(); await expect(page.locator('[data-character-history]')).toContainText('Previous save');
 await page.locator('.character-board').first().getByRole('button').click(); await expect(page.locator('.node-cell').first()).toBeVisible(); await page.locator('.node-cell').first().click(); await expect(page.locator('.node-detail')).toBeVisible(); await overflow();
 const blocked = await browser.newContext({viewport:{width:390,height:844}}); await blocked.addInitScript(() => {Object.defineProperty(Storage.prototype,'setItem',{value(){throw new DOMException('Denied','SecurityError');}});}); const blockedPage = await blocked.newPage(); await blockedPage.goto(path('en','database')); await blockedPage.locator('[data-catalogue-item]').first().getByRole('button',{name:'Save item',exact:true}).click(); await expect(blockedPage.getByText('Browser storage is unavailable. Changes last only for this session; export a backup before closing.',{exact:true})).toBeVisible(); await blocked.close();
 await page.setViewportSize({width:1440,height:1000}); await page.goto(path('en','database')); await page.getByLabel('Game region',{exact:true}).selectOption('nae'); await page.screenshot({path:fileURLToPath(new URL('database-desktop.png',output)),fullPage:true}); await overflow();
 const sitemap = await (await page.request.get(`${base}/sitemap.xml`)).text(); assert.ok(sitemap.includes(`/database/items/${items[0].id}`)); assert.ok(!sitemap.includes('/workspace'));
 const personal = await (await page.request.get(path('en','workspace'))).text(); assert.ok(personal.includes('noindex')); const queried = await (await page.request.get(path('en','tools/compare?first=1'))).text(); assert.ok(queried.includes('noindex'));
 assert.deepEqual(errors,[]); await writeFile(new URL('result.json',output),JSON.stringify({passed:true,locales:4,itemRequests:requests.length,checkedAt:new Date().toISOString()},null,2)); console.log('Platform flows passed: 4 locales, mobile/desktop, backups, sharing, regions, request errors, history, nodes, storage and SEO.');
} catch (error) {
 await writeFile(new URL('result.json',output),JSON.stringify({passed:false,error:error.message,checkedAt:new Date().toISOString()},null,2));
 await page.screenshot({path:fileURLToPath(new URL('failure.png',output)),fullPage:true});
 await writeFile(new URL('failure.txt',output), `${await page.locator('body').innerText()}\n${await page.evaluate(() => localStorage.getItem('aion2-workspace-v1'))}\n${errors.join('\n')}`);
 throw error;
} finally {await browser.close();}
