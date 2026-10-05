import {chromium} from '@playwright/test';
import {writeFile} from 'node:fs/promises';
import {existsSync} from 'node:fs';
const out='research/content/2026-10-04/races-player-depth/faction-research';
const chrome='C:/Program Files/Google/Chrome/Application/chrome.exe';
const browser=await chromium.launch({headless:true,executablePath:existsSync(chrome)?chrome:undefined});
const routes=[
  ['global-two-worlds','https://aion2.ncsoft.jp/en/teaser','Global'],
  ['kr-expedition-guide','https://aion2.plaync.com/ko-kr/guidebook/view?title=%EC%9B%90%EC%A0%95','KR'],
  ['global-guidebook-index','https://aion2.plaync.com/en-us/guidebook/index','Global'],
];
const manifest=[];
try {
  for(const [slug,url,region] of routes){
    const context=await browser.newContext({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
    const page=await context.newPage();
    const pending=[];
    const responses=[];
    page.on('response',response=>{
      if(/conti\/getContent|api-[^/]*(?:guide|community)|\/guidebook\//.test(response.url()) && /json/.test(response.headers()['content-type']??'')){
        const promise=(async()=>{
          const body=await response.text();
          const name=`${slug}-api-${responses.length}.json`;
          responses.push({url:response.url(),status:response.status(),file:name});
          await writeFile(`${out}/${name}`,body);
        })().catch(error=>responses.push({url:response.url(),error:String(error)}));
        pending.push(promise);
      }
    });
    const startedAt=new Date().toISOString();
    let status,error;
    try {
      const response=await page.goto(url,{waitUntil:'networkidle',timeout:25000});
      status=response.status();
      await writeFile(`${out}/${slug}-rendered.txt`,await page.locator('body').innerText());
      await writeFile(`${out}/${slug}-rendered.html`,await page.content());
    } catch(e){error=String(e);}
    await Promise.allSettled(pending);
    manifest.push({slug,url,region,retrievedAt:startedAt,status,finalUrl:page.url(),error,responses});
    await context.close();
  }
} finally {await browser.close();}
await writeFile(`${out}/browser-manifest.json`,JSON.stringify(manifest,null,2));
console.log(JSON.stringify(manifest,null,2));
