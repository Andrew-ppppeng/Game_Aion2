import {chromium} from '@playwright/test';
import {writeFile} from 'node:fs/promises';
const output = new URL('./',import.meta.url);
const browser = await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
const page = await browser.newPage({viewport:{width:1440,height:1000}});
const responses=[];
page.on('response',async(response)=>{
 if(!response.url().includes('/guide/') && !response.url().includes('/guidebook/'))return;
 try {
  const body=await response.text();
  responses.push({url:response.url(),status:response.status(),length:body.length});
  if(response.url().includes('/guide/'))await writeFile(new URL('official-guide-browser.json',output),body);
 }catch{}
});
await page.goto('https://aion2.plaync.com/ko-kr/guidebook/view?title=%EC%8A%A4%ED%82%AC',{waitUntil:'domcontentloaded',timeout:45000});
await page.waitForTimeout(5000);
await writeFile(new URL('official-guide-browser.html',output),await page.content());
console.log(JSON.stringify({responses,title:await page.title(),text:(await page.locator('body').innerText()).slice(-16000),images:await page.locator('#ncGuidebookTemplate img').evaluateAll(nodes=>nodes.map(n=>({src:n.src,width:n.naturalWidth,height:n.naturalHeight})))},null,2));
await page.screenshot({path:new URL('official-guide-browser.png',output).pathname.replace(/^\/(\w:)/,'$1'),fullPage:true});
await browser.close();
