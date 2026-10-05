import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import sharp from 'sharp';
const root=new URL('./',import.meta.url);
const repo=new URL('../../../../',root);
const records=JSON.parse(await readFile(new URL('skill-icon-sources-final.json',root),'utf8'));
const checked=[];
for(const record of records){
 if(record.error)throw new Error(record.skillId);
 const src=`/media/skills/${record.skillId}.webp`;
 const image=await readFile(new URL(`public${src}`,repo));
 const meta=await sharp(image).metadata();
 if(meta.format!=='webp'||meta.width<32||meta.height<32)throw new Error(`Invalid icon ${src}`);
 checked.push({id:record.skillId,src,width:meta.width,height:meta.height,sourceUrl:record.sourceUrl,originalUrl:record.originalUrl,region:record.region,version:record.version,checkedAt:record.checkedAt,sha256:createHash('sha256').update(image).digest('hex')});
}
await writeFile(new URL('src/content/skill-icons.json',repo),JSON.stringify(checked,null,2)+'\n');
console.log(`Validated and recorded ${checked.length} exact skill images.`);
