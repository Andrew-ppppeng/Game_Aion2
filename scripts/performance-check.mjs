import {existsSync} from 'node:fs';
import {mkdir, writeFile} from 'node:fs/promises';
import {chromium} from '@playwright/test';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const filename = process.env.QA_PERFORMANCE_OUTPUT || 'performance-after.json';
if (!/^[a-z0-9-]+\.json$/i.test(filename)) throw new Error('Use a plain JSON filename for QA_PERFORMANCE_OUTPUT');
const systemChrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const executablePath = process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(systemChrome) ? systemChrome : undefined);
const browser = await chromium.launch({headless: true, executablePath});
const results = [];

try {
  for (const slug of ['guide', 'classes', 'map']) {
    const samples = [];
    for (let sample = 0; sample < 3; sample++) {
      const context = await browser.newContext({viewport: {width: 390, height: 844}});
      const page = await context.newPage();
      const session = await context.newCDPSession(page);
      await session.send('Network.enable');
      await session.send('Network.setCacheDisabled', {cacheDisabled: true});
      await session.send('Network.emulateNetworkConditions', {offline: false, latency: 150, downloadThroughput: 200000, uploadThroughput: 93750});
      await session.send('Emulation.setCPUThrottlingRate', {rate: 4});
      await page.addInitScript(() => {
        window.guidePerformance = {lcp: 0, cls: 0};
        new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) window.guidePerformance.lcp = entry.startTime;
        }).observe({type: 'largest-contentful-paint', buffered: true});
        new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) if (!entry.hadRecentInput) window.guidePerformance.cls += entry.value;
        }).observe({type: 'layout-shift', buffered: true});
      });
      await page.goto(`${base}/${slug}`, {waitUntil: 'networkidle'});
      samples.push(await page.evaluate(() => ({
        lcp: Math.round(window.guidePerformance.lcp),
        cls: Number(window.guidePerformance.cls.toFixed(4)),
        bytes: performance.getEntriesByType('resource').reduce((sum, entry) => sum + entry.transferSize, 0),
      })));
      await context.close();
    }
    results.push({slug, samples});
  }
  const output = {conditions: 'Chrome 390x844, cold cache, 150ms latency, 1.6Mbps, CPU4; three samples', byteScope: 'Resource Timing subresources, excluding the HTML document', results};
  await mkdir(new URL('../.qa/', import.meta.url), {recursive: true});
  await writeFile(new URL(`../.qa/${filename}`, import.meta.url), `${JSON.stringify(output, null, 2)}\n`);
  for (const {slug, samples} of results) {
    const median = (key) => samples.map((sample) => sample[key]).sort((a, b) => a - b)[1];
    console.log(`${slug}: median LCP ${median('lcp')}ms, CLS ${median('cls')}, subresource bytes ${median('bytes')}`);
  }
} finally {
  await browser.close();
}
