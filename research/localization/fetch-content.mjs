import {readFile, writeFile} from 'node:fs/promises';
const output = new URL('./2026-10-02/', import.meta.url);
await Promise.all(['en-us', 'ja-jp', 'es-es', 'de-de'].map(async (locale) => {
  const data = JSON.parse(await readFile(new URL(`${locale}.json`, output), 'utf8'));
  const source = data.resources.find((resource) => resource.url.includes('/conti/getContent?service=aion2global&alias=about-')).url;
  const response = await fetch(source, {signal: AbortSignal.timeout(20000)});
  const text = await response.text();
  await writeFile(new URL(`${locale}-content.json`, output), text);
  console.log(JSON.stringify({locale, source, status: response.status, length: text.length, preview: text.slice(0, 1000)}));
}));
