import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import path from 'node:path';
import {assetRanges,scoreEditions,isExternalAsset,localAssetPath} from './asset-paths.mjs';
export async function verifyExternalAssets(root){
 const git=args=>execFileSync('git',args,{cwd:root,encoding:'utf8'}).trim();
 const policies=[...assetRanges,...scoreEditions],tags=new Map();
 for(const p of policies){if(tags.has(p.tag))continue;
  const commit=git(['rev-parse',`refs/tags/${p.tag}`]);
  const remote=git(['ls-remote','--tags','origin',`refs/tags/${p.tag}`]).split(/\s/)[0];
  assert.equal(remote,commit,'Publish immutable music tag before catalogue: '+p.tag);
  const tree=new Map(git(['ls-tree','-r',p.tag]).split('\n').map(line=>{const [meta,name]=line.split('\t');return [name,meta.split(' ')[2]];}));
  tags.set(p.tag,{commit,tree});
 }
 const format=git(['rev-parse','--show-object-format']);
 const catalogue=JSON.parse(await readFile(path.join(root,'library.json'),'utf8'));
 const volumes=JSON.parse(await readFile(path.join(root,'downloads/volumes.json'),'utf8'));
 const urls=[...new Set([...catalogue.flatMap(p=>[p.audio,p.pdf,p.midi,p.xml,...p.scores]),...volumes.map(v=>v.pdf_url).filter(Boolean)].filter(isExternalAsset))];
 let next=0;
 await Promise.all(Array.from({length:4},async()=>{
  while(next<urls.length){
   const url=urls[next++],relative=localAssetPath(url),local=await readFile(path.join(root,relative));
   const policy=policies.find(p=>url.startsWith(p.prefix));assert(policy);
   assert.equal(createHash(format).update(`blob ${local.length}\0`).update(local).digest('hex'),tags.get(policy.tag).tree.get(relative),'Music changed after immutable tag: '+relative);
   const response=await fetch(url,{signal:AbortSignal.timeout(60000)});assert.equal(response.status,200,'Unavailable external asset: '+url);
   const remote=Buffer.from(await response.arrayBuffer());
   assert.equal(createHash('sha256').update(remote).digest('hex'),createHash('sha256').update(local).digest('hex'),'Published music differs: '+relative);
  }
 }));
 return {tags:[...tags].map(([tag,{commit}])=>({tag,commit})),assets:urls.length};
}
