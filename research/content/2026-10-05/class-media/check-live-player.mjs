import {chromium} from '@playwright/test';
import {writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
const output=new URL('./',import.meta.url);
const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
const context=await browser.newContext({viewport:{width:1440,height:1000}});
await context.route('**/api/analytics',route=>route.fulfill({status:204}));
const page=await context.newPage();
await page.goto('http://localhost:3004/templar',{waitUntil:'networkidle'});
await page.locator('.class-video-play').click();
const frame=await page.locator('.class-video iframe').contentFrame();
let result;
try{
 await frame.locator('.html5-video-player').waitFor({timeout:20000});
 await page.waitForTimeout(5000);
 result=await frame.locator('body').evaluate(body=>({text:body.innerText,video:Array.from(body.querySelectorAll('video')).map(v=>({paused:v.paused,time:v.currentTime,readyState:v.readyState,error:v.error?.code})),errors:Array.from(body.querySelectorAll('.ytp-error-content-wrap')).map(e=>e.textContent)}));
}catch(error){result={error:error.message,frames:page.frames().map(f=>f.url())};}
await page.locator('.class-video').screenshot({path:fileURLToPath(new URL('live-player.png',output))});
await writeFile(new URL('live-player-check.json',output),JSON.stringify(result,null,2));
console.log(JSON.stringify(result,null,2));
await browser.close();
