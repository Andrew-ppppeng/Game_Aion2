import {chromium} from '@playwright/test';
import {mkdir, writeFile} from 'node:fs/promises';

const output = new URL('./2026-10-02/', import.meta.url);
await mkdir(output, {recursive: true});
const locales = ['en-us', 'ja-jp', 'es-es', 'de-de'];
const browser = await chromium.launch({headless: true, executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe'});
try {
  const results = await Promise.allSettled(locales.map(async (locale) => {
    const page = await browser.newPage();
    const articles = [];
    for (const route of ['board/notice/view?articleId=6abab930eea53f5d6dbcf939', 'board/update/list']) {
      const url = `https://aion2.plaync.com/${locale}/${route}`;
      const responses = [];
      page.on('response', async (response) => {
        if (response.url().startsWith('https://aion2.plaync.com/') && response.headers()['content-type']?.includes('json')) {
          try {responses.push({url: response.url(), status: response.status(), body: await response.json()});} catch {}
        }
      });
      await page.goto(url, {waitUntil: 'domcontentloaded', timeout: 45_000});
      await page.waitForLoadState('networkidle', {timeout: 12_000}).catch(() => {});
      articles.push({source: url, title: await page.title(), text: await page.locator('body').innerText(), responses});
      page.removeAllListeners('response');
    }
    await page.close();
    await writeFile(new URL(`${locale}-extra.json`, output), JSON.stringify({checkedAt: '2026-10-02', region: 'Global', articles}, null, 2));
    return {locale, articles: articles.map(({source, text}) => ({source, text}))};
  }));
  console.log(JSON.stringify(results.map((result) => result.status === 'fulfilled' ? result : {...result, reason: String(result.reason)}), null, 2));
} finally {await browser.close();}
