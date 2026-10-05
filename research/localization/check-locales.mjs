import {chromium} from '@playwright/test';
import {mkdir, writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';

const output = new URL('./2026-10-02/', import.meta.url);
await mkdir(output, {recursive: true});
const browser = await chromium.launch({headless: true, executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe'});
try {
  const results = await Promise.allSettled(['en-us', 'ja-jp', 'es-es', 'de-de'].map(async (locale) => {
    const page = await browser.newPage({viewport: {width: 1440, height: 1000}});
    const resources = [];
    page.on('response', (response) => {
      if (response.request().resourceType() === 'script' || response.headers()['content-type']?.includes('json')) resources.push({url: response.url(), status: response.status()});
    });
    const url = `https://aion2.plaync.com/${locale}/about/index`;
    await page.goto(url, {waitUntil: 'domcontentloaded', timeout: 45000});
    await page.waitForLoadState('networkidle', {timeout: 15000}).catch(() => {});
    const data = await page.evaluate(() => ({title: document.title, url: location.href, text: document.body.innerText, images: [...document.images].map((image) => ({alt: image.alt, src: image.currentSrc})), links: [...document.querySelectorAll('a[href]')].map((a) => ({text: a.textContent?.trim(), href: a.href}))}));
    await writeFile(new URL(`${locale}.json`, output), JSON.stringify({checkedAt: '2026-10-02', region: 'Global', ...data, resources}, null, 2));
    await writeFile(new URL(`${locale}.html`, output), await page.content());
    await page.screenshot({path: fileURLToPath(new URL(`${locale}.png`, output)), fullPage: true});
    await page.close();
    return {locale, title: data.title, text: data.text.slice(0, 8500), resources: resources.slice(-12)};
  }));
  console.log(JSON.stringify(results, null, 2));
} finally {await browser.close();}
