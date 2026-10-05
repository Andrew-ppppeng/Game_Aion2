// Render the actual page components so exported diagrams match the reading view.
import {chromium} from '@playwright/test';
import {mkdir, readFile, writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const base=process.env.QA_BASE_URL || 'http://localhost:3000';
const root=new URL('../',import.meta.url);
const identities=JSON.parse(await readFile(new URL('src/content/class-identities.json',root),'utf8'));
const output=new URL('public/media/guides/',root);
await mkdir(output,{recursive:true});
const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
const context=await browser.newContext({viewport:{width:1800,height:1000},deviceScaleFactor:2,reducedMotion:'reduce'});
await context.route('**/api/analytics',route=>route.fulfill({status:204}));
const page=await context.newPage();
const records=[];
try {
 for(const locale of ['en','ja','es','de']){
  const prefix=locale==='en'?'':`/${locale}`;
  await page.goto(`${base}${prefix}/builds`,{waitUntil:'networkidle'});
  console.log(`Rendering ${locale} diagrams...`);
  await page.addStyleTag({content: '.skill-map, .specialization-tree {width:1080px !important; max-width:none !important; font-family:Arial,"Yu Gothic",sans-serif !important} .skill-map-node strong, .skill-map-state strong {font-size:18px !important} .skill-map-node small {font-size:14px !important} .skill-map-connection > span {font-size:15px !important} .skill-map-connection p {font-size:16px !important} .skill-map-heading {margin-bottom:20px} .skill-map-hint, .skill-map-actions, .specialization-image-link {display:none !important} .specialization-options label strong {font-size:18px !important} .specialization-options label span > span {font-size:16px !important} .specialization-result {font-size:16px !important}'});
  await page.evaluate(()=>document.fonts.ready);
  for(const {id} of identities){
   await page.locator('[data-build-maps] select').selectOption(id);
   const map=page.locator(`[data-build-map-panel="${id}"] [data-skill-map]`);
   await map.locator('img').evaluateAll(async(nodes)=>Promise.all(nodes.map(node=>{node.loading='eager'; return node.decode();})));
   const file=`skill-map-${id}-${locale}.png`;
   const image=await map.screenshot({path:fileURLToPath(new URL(file,output)),animations:'disabled'});
   records.push({file,locale,classId:id,sha256:createHash('sha256').update(image).digest('hex'),region:'Global',version:'Verified client 1.0.21.0 mechanics, author-created diagram; screenshots of site component, not an in-game skill tree',checkedAt:'2026-10-05'});
  }
  const tree=page.locator('[data-specialization-tree]');
  await tree.locator('img').evaluateAll(async(nodes)=>Promise.all(nodes.map(node=>{node.loading='eager'; return node.decode();})));
  // The saved image explains all alternatives; it must not imply a recommended
  // option or claim to preserve the reader's live radio-button selection.
  await tree.evaluate((element)=>{
   element.querySelectorAll('.specialization-options label').forEach((label)=>{
    label.classList.remove('selected');
    label.querySelector('input')?.remove();
    label.querySelector('svg')?.remove();
   });
   element.querySelector('.specialization-result strong')?.remove();
  });
  const file=`specialization-hellfire-${locale}.png`;
  const image=await tree.screenshot({path:fileURLToPath(new URL(file,output)),animations:'disabled'});
  records.push({file,locale,skillId:'15060000',sha256:createHash('sha256').update(image).digest('hex'),region:'Global',version:'Hellfire skill-rank-8 specialization alternatives, client 1.0.21.0; author-created diagram',checkedAt:'2026-10-05'});
 }
 await writeFile(new URL('src/content/class-diagram-images.json',root),JSON.stringify(records,null,2)+'\n');
 console.log(`Exported ${records.length} diagrams from actual localized page components.`);
} finally {await browser.close();}
