import {existsSync} from 'node:fs';
import {mkdir, readFile, writeFile} from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {chromium, expect} from '@playwright/test';
import {installGameFixtures, readQaJson} from './qa-fixtures.mjs';

const base = (process.env.QA_BASE_URL || 'http://127.0.0.1:3000').replace(/\/$/, '');
const homeOnly = process.argv.includes('--home-only');
const paths = homeOnly ? ['/'] : ['/', '/guide', '/classes', '/map', '/builds', '/tools/character'];
const filename = process.env.QA_PERFORMANCE_OUTPUT || (homeOnly ? 'performance-home.json' : 'performance-after.json');
if (!/^[a-z0-9-]+\.json$/i.test(filename)) throw new Error('Use a plain JSON filename for QA_PERFORMANCE_OUTPUT');
function budget(name, fallback) {
  const value = Number(process.env[name] || fallback);
  if (!Number.isFinite(value) || value <= 0) throw new Error(`${name} must be a positive number`);
  return value;
}
const limits = {
  lcpMs: budget('QA_LCP_BUDGET_MS', 2500), cls: budget('QA_CLS_BUDGET', 0.1),
  totalBytes: budget('QA_TOTAL_BYTES_BUDGET', 700 * 1024), scriptBytes: budget('QA_SCRIPT_BYTES_BUDGET', 220 * 1024),
  eventDurationMs: budget('QA_EVENT_DURATION_BUDGET_MS', 200),
};
const count = Number(process.env.QA_PERFORMANCE_SAMPLES || 3);
if (!Number.isInteger(count) || count < 1 || count > 10) throw new Error('QA_PERFORMANCE_SAMPLES must be an integer from 1 to 10');
const systemChrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const executablePath = process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(systemChrome) ? systemChrome : undefined);
const browser = await chromium.launch({headless: true, executablePath});
const results = [];
const failures = [];
const packageInfo = await readQaJson('package.json');
let gitHead = null;
try {gitHead = execFileSync('git', ['rev-parse', 'HEAD'], {encoding: 'utf8'}).trim();} catch {}
let buildId = null;
try {buildId = (await readFile(new URL(`../${process.env.QA_BUILD_DIR || '.next-review'}/BUILD_ID`, import.meta.url), 'utf8')).trim();} catch {}
const median = (values) => {
  const sorted = values.toSorted((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length % 2 ? sorted[middle] : (sorted[middle - 1] + sorted[middle]) / 2;
};

try {
  // Keep existing guide/classes/map coverage and add the three review targets.
  for (const path of paths) {
    const samples = [];
    for (let sample = 0; sample < count; sample++) {
      const context = await browser.newContext({viewport: {width: 390, height: 844}, reducedMotion: 'reduce'});
      if (process.env.QA_ANALYTICS_OPT_OUT === 'true') await context.addInitScript(() => localStorage.setItem('aion2-analytics-opt-out-v1', 'true'));
      const fixture = await installGameFixtures(context);
      const page = await context.newPage();
      const errors = [];
      page.on('pageerror', (error) => errors.push(error.message));
      const session = await context.newCDPSession(page);
      const transfers = new Map();
      session.on('Network.responseReceived', ({requestId, type, response}) => transfers.set(requestId, {type, url: response.url, status: response.status, bytes: 0}));
      session.on('Network.loadingFinished', ({requestId, encodedDataLength}) => {
        const response = transfers.get(requestId);
        if (response) response.bytes = encodedDataLength;
      });
      await session.send('Network.enable');
      await session.send('Network.setCacheDisabled', {cacheDisabled: true});
      await session.send('Network.emulateNetworkConditions', {offline: false, latency: 150, downloadThroughput: 200000, uploadThroughput: 93750});
      await session.send('Emulation.setCPUThrottlingRate', {rate: 4});
      await page.addInitScript(() => {
        window.guidePerformance = {lcp: 0, cls: 0, events: [], eventTiming: PerformanceObserver.supportedEntryTypes.includes('event')};
        new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) window.guidePerformance.lcp = entry.startTime;
        }).observe({type: 'largest-contentful-paint', buffered: true});
        new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) if (!entry.hadRecentInput) window.guidePerformance.cls += entry.value;
        }).observe({type: 'layout-shift', buffered: true});
        if (window.guidePerformance.eventTiming) new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) if (entry.interactionId) window.guidePerformance.events.push({name: entry.name, startTime: entry.startTime, duration: entry.duration});
        }).observe({type: 'event', buffered: true, durationThreshold: 16});
      });
      const url = `${base}${path}`;
      const navigation = await page.goto(url, {waitUntil: 'networkidle'});
      if (!navigation?.ok()) throw new Error(`${url}: navigation ${navigation?.status()}`);
      // Freeze initial-load metrics before the scripted interaction.
      const load = await page.evaluate(() => {
        const navigation = performance.getEntriesByType('navigation')[0];
        const resources = performance.getEntriesByType('resource');
        return {
          lcpMs: Math.round(window.guidePerformance.lcp), cls: Number(window.guidePerformance.cls.toFixed(4)),
          navigationTransferBytes: navigation.transferSize,
          resourceTimingBytes: navigation.transferSize + resources.reduce((sum, entry) => sum + entry.transferSize, 0),
          loadEventMs: Math.round(navigation.loadEventEnd),
          articleRevision: document.querySelector('[data-article-revision]')?.getAttribute('data-article-revision') || null,
        };
      });
      const network = [...transfers.values()];
      const sum = (type) => network.filter((entry) => !type || entry.type === type).reduce((total, entry) => total + entry.bytes, 0);
      load.htmlBytes = sum('Document');
      load.scriptBytes = sum('Script');
      load.firstPartyScriptBytes = [...transfers.values()].filter((r) => r.type === 'Script' && new URL(r.url).origin === new URL(url).origin).reduce((total, r) => total + r.bytes, 0);
      load.thirdPartyScriptBytes = load.scriptBytes - load.firstPartyScriptBytes;
      load.largestScripts = [...transfers.values()].filter((r) => r.type === 'Script').toSorted((a, b) => b.bytes - a.bytes).slice(0, 5).map(({url, bytes}) => ({url, bytes}));
      load.fixtureResponseBytes = fixture.fulfilled.reduce((total, entry) => total + entry.bytes, 0);
      // Intercepted responses can report zero CDP wire bytes. Count the archived
      // JSON payload in that case so mocked tools do not get a free byte budget.
      load.fixtureTransferAdjustmentBytes = fixture.fulfilled.filter(({url}) => !network.some((entry) => entry.url === url && entry.bytes > 0)).reduce((total, entry) => total + entry.bytes, 0);
      load.totalBytes = sum() + load.fixtureTransferAdjustmentBytes;
      load.requestCount = network.length;
      if (!load.lcpMs || !load.htmlBytes || !load.scriptBytes) throw new Error(`${url}: missing paint or network measurements`);

      let target;
      let ready;
      if (path === '/') {target = page.locator('.mobile-menu-button'); ready = () => expect(page.locator('#mobile-navigation')).toBeVisible();}
      else if (path === '/builds') {target = page.locator('[data-more-equipment] > summary'); ready = () => expect(page.locator('[data-equipment-cards] [data-item-id]')).toHaveCount(22);}
      else if (path === '/tools/character') {
        await page.locator('[data-character-tool] input').first().fill('Testa');
        target = page.locator('[data-character-tool] button[type="submit"]'); ready = () => expect(page.locator('.character-match')).toHaveCount(1);
      } else {target = page.locator('.article-toc-mobile > summary'); ready = () => expect(page.locator('.article-toc-mobile')).toHaveAttribute('open', '');}
      await target.scrollIntoViewIfNeeded();
      await page.evaluate(() => {window.guidePerformance.events = []; window.guidePerformance.interactionStarted = performance.now();});
      await target.click();
      await ready();
      const interactionReadyMs = await page.evaluate(() => Math.round(performance.now() - window.guidePerformance.interactionStarted));
      await page.waitForTimeout(100);
      const interaction = await page.evaluate(() => ({
        eventTimingSupported: window.guidePerformance.eventTiming,
        eventDurationMs: Math.max(0, ...window.guidePerformance.events.map((entry) => entry.duration)),
        eventEntries: window.guidePerformance.events,
      }));
      if (!interaction.eventTimingSupported) throw new Error(`${url}: browser does not support Event Timing`);
      if (errors.length) throw new Error(`${url}: ${errors.join('; ')}`);
      samples.push({sample: sample + 1, measuredAtUtc: new Date().toISOString(), ...load, interaction: {target: await target.getAttribute('class'), readyMs: interactionReadyMs, ...interaction}, fixtureResponses: fixture.fulfilled});
      await context.close();
    }
    const medians = Object.fromEntries(Object.keys(limits).map((key) => [key, median(samples.map((entry) => key === 'eventDurationMs' ? entry.interaction.eventDurationMs : entry[key]))]));
    const violations = Object.entries(limits).filter(([key, limit]) => medians[key] > limit).map(([metric, limit]) => ({metric, observed: medians[metric], limit}));
    for (const violation of violations) failures.push({url: `${base}${path}`, ...violation});
    results.push({url: `${base}${path}`, samples, medians, violations});
    console.log(`${path}: LCP ${medians.lcpMs}ms; CLS ${medians.cls}; HTML+resources ${medians.totalBytes} bytes; scripts ${medians.scriptBytes} bytes; scripted event ${medians.eventDurationMs}ms`);
  }
} catch (error) {
  failures.push({error: error instanceof Error ? error.message : String(error)});
} finally {
  const output = {
    measuredAtUtc: new Date().toISOString(), baseUrl: base,
    environment: {appVersion: packageInfo.version, nextVersion: packageInfo.dependencies.next, node: process.version, chrome: browser.version(), executablePath: executablePath || 'Playwright Chromium', gitHead, buildId},
    conditions: {viewport: '390x844', coldCache: true, latencyMs: 150, downloadBytesPerSecond: 200000, uploadBytesPerSecond: 93750, cpuSlowdown: 4, samples: count, aggregation: 'median per URL', paths, analyticsOptOut: process.env.QA_ANALYTICS_OPT_OUT === 'true'},
    measurementNotes: ['CDP encoded transfer bytes include HTML and all completed initial-load resources.', 'Resource Timing including the navigation is retained as a second transfer measurement.', 'Fixture game API responses avoid live upstream queries. If CDP reports zero wire bytes for an intercepted response, its recorded JSON payload bytes are added to totalBytes as fixtureTransferAdjustmentBytes.', 'Scripted Event Timing is a laboratory interaction measurement, not real-user INP. readyMs includes Playwright and response waiting; it has no INP interpretation.'],
    thresholds: limits, results, failures, passed: failures.length === 0,
  };
  await mkdir(new URL('../.qa/', import.meta.url), {recursive: true});
  await writeFile(new URL(`../.qa/${filename}`, import.meta.url), `${JSON.stringify(output, null, 2)}\n`);
  await browser.close();
  if (failures.length) {console.error(`FAIL: performance check: ${JSON.stringify(failures)}`); process.exitCode = 1;}
  else console.log(`PASS: ${results.length} URLs within all five median performance budgets; .qa/${filename}`);
}
