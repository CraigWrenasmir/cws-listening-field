import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import path from 'node:path';
import {assetTag,assetPrefix,localAssetPath} from './asset-paths.mjs';
export async function verifyExternalAssets(root){
 const git=args=>execFileSync('git',args,{cwd:root,encoding:'utf8'}).trim();
 const tag=git(['rev-parse',`refs/tags/${assetTag}`]);
 const remote=git(['ls-remote','--tags','origin',`refs/tags/${assetTag}`]).split(/\s/)[0];
 assert.equal(remote,tag,'The immutable music tag must be published before the catalogue');
 const tree=new Map(git(['ls-tree','-r',assetTag]).split('\n').map(line=>{const [meta,name]=line.split('\t');return [name,meta.split(' ')[2]];}));
 const format=git(['rev-parse','--show-object-format']);
 const catalogue=JSON.parse(await readFile(path.join(root,'library.json'),'utf8'));
 const urls=[...new Set(catalogue.flatMap(p=>[p.audio,p.pdf,p.midi,p.xml,...p.scores]).filter(u=>u.startsWith(assetPrefix)))];
 let next=0;
 await Promise.all(Array.from({length:4},async()=>{
  while(next<urls.length){
   const url=urls[next++],relative=localAssetPath(url),local=await readFile(path.join(root,relative));
   assert.equal(createHash(format).update(`blob ${local.length}\0`).update(local).digest('hex'),tree.get(relative),'Music changed after its immutable tag: '+relative);
   const response=await fetch(url,{signal:AbortSignal.timeout(60000)});assert.equal(response.status,200,'Unavailable piece asset: '+url);
   const remote=Buffer.from(await response.arrayBuffer());
   assert.equal(createHash('sha256').update(remote).digest('hex'),createHash('sha256').update(local).digest('hex'),'Published music differs: '+relative);
  }
 }));
 return {tag,assetTag,assets:urls.length};
}
