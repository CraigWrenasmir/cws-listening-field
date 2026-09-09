import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {publicationFiles,releaseURL,SITE_LIMIT} from './site-distribution.mjs';
const root=fileURLToPath(new URL('../',import.meta.url)),files=await publicationFiles(root),paths=new Set(files.map(f=>f.path));
const pieces=JSON.parse(await readFile(new URL('../library.json',import.meta.url),'utf8'));
const volumes=JSON.parse(await readFile(new URL('../downloads/volumes.json',import.meta.url),'utf8'));
for(const p of pieces)for(const f of [p.audio,p.pdf,p.midi,p.xml,...p.scores])assert(paths.has(f),f);
for(const f of ['CNAME','.nojekyll','index.html','kinship.html','library.json','data/series.json','downloads/index.html','downloads/volumes.json'])assert(paths.has(f));
assert(!paths.has('data/catalog.json'));assert(!files.some(f=>f.path.startsWith('pieces/')&&f.path.endsWith('.json')));
for(const v of volumes){assert(paths.has(v.pdf));if(v.number<=10){assert(paths.has(v.zip));assert(!v.zip_url);}else{assert.equal(v.zip_url,releaseURL(v));assert(!paths.has(v.zip));}}
assert(files.reduce((s,f)=>s+f.bytes,0)<SITE_LIMIT);
console.log(`Publication distribution passed: all ${pieces.length} works and original download URLs retained; new volume archives use exact owned-repository Release URLs.`);
