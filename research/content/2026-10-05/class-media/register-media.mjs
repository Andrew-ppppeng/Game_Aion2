import {readFile,writeFile} from 'node:fs/promises';
import sharp from 'sharp';
const root=new URL('./',import.meta.url);
const repo=new URL('../../../../',root);
const records=JSON.parse(await readFile(new URL('official-class-videos.json',root),'utf8'));
const assets=JSON.parse(await readFile(new URL('src/content/guide-assets.json',repo),'utf8'));
const videos={};
for(const record of records){
 if(record.error||!record.thumbnailUrl)throw new Error(`Missing video ${record.classId}`);
 const filename=`class-${record.classId}-combat.webp`;
 const data=await sharp(await readFile(new URL(`${record.classId}-video.jpg`,root))).resize({width:960,withoutEnlargement:true}).webp({quality:83}).toBuffer({resolveWithObject:true});
 await writeFile(new URL(`public/media/guides/${filename}`,repo),data.data);
 const asset={id:`class-${record.classId}-combat`,src:`/media/guides/${filename}`,width:data.info.width,height:data.info.height,sourceUrl:record.sourceUrl,originalUrl:record.thumbnailUrl,publisher:record.oembed.author_name,region:record.region,version:record.sourceVersion,checkedAt:record.checkedAt,purpose:'video preview',imageLanguage:'none'};
 assets.push(asset);
 videos[record.classId]={videoId:record.videoId,poster:asset.src,width:asset.width,height:asset.height};
}
await writeFile(new URL('src/content/class-videos.json',repo),JSON.stringify(videos,null,2)+'\n');
await writeFile(new URL('src/content/guide-assets.json',repo),JSON.stringify(assets,null,2)+'\n');
console.log(`Registered ${records.length} official class videos and local posters.`);
