import {readdir,stat,readFile} from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
export const SITE_LIMIT=950_000_000;
export function releaseURL(v){return `https://github.com/CraigWrenasmir/cws-listening-field/releases/download/volume-${v.number}/CWS_Volume_${String(v.number).padStart(2,'0')}.zip`;}
export async function publicationFiles(root){
 const volumes=JSON.parse(await readFile(path.join(root,'downloads/volumes.json'),'utf8'));
 const external=new Set(volumes.filter(v=>v.zip_url).map(v=>{assert.equal(v.zip_url,releaseURL(v));return v.zip;}));
 const files=[];
 async function walk(relative){
  const absolute=path.join(root,relative),info=await stat(absolute);
  if(info.isDirectory()){for(const name of (await readdir(absolute)).sort())await walk(path.posix.join(relative,name));return;}
  if(external.has(relative)||relative.startsWith('pieces/')&&relative.endsWith('.json'))return;
  assert(info.size<90*1024*1024,'Oversized publication file: '+relative);
  files.push({path:relative,bytes:info.size});
 }
 for(const name of ['.nojekyll','CNAME','index.html','kinship.html','src','library.json','data/series.json','pieces','downloads','licenses'])await walk(name);
 return files;
}
