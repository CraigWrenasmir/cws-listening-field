import {cp,mkdir,rm,readFile,readdir} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import assert from 'node:assert/strict';
import {publicationFiles,SITE_LIMIT} from './site-distribution.mjs';
const root=fileURLToPath(new URL('../',import.meta.url)),out=path.join(root,'dist');
const files=await publicationFiles(root),bytes=files.reduce((sum,f)=>sum+f.bytes,0);
assert(bytes<SITE_LIMIT,'Review distribution before publishing');
// Clear generated output so removed or externally hosted assets cannot linger.
await rm(out,{recursive:true,force:true});
for(const f of files){const target=path.join(out,f.path);await mkdir(path.dirname(target),{recursive:true});await cp(path.join(root,f.path),target);}
const catalog=JSON.parse(await readFile(path.join(out,'library.json'),'utf8'));
for(const p of catalog)for(const f of [p.pdf,p.audio,p.midi,p.xml,...p.scores])assert((await readFile(path.join(out,f))).length>0,'Missing runtime asset: '+f);
async function count(dir){let n=0;for(const d of await readdir(dir,{withFileTypes:true}))n+=d.isDirectory()?await count(path.join(dir,d.name)):1;return n;}
assert.equal(await count(out),files.length);
console.log(`Built ${files.length} verified public files in dist/: ${(bytes/1024/1024).toFixed(1)} MiB. Source metadata remains in the repository and complete volume downloads.`);
