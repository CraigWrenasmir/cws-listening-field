import {cp,mkdir,rm,writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const root=fileURLToPath(new URL('../',import.meta.url));
const out=path.join(root,'dist');
await mkdir(out,{recursive:true});
for(const name of ['index.html','src','library.json','pieces','downloads','licenses'])await cp(path.join(root,name),path.join(out,name),{recursive:true});
await writeFile(path.join(out,'.nojekyll'),'');
console.log('Static site built in dist/. Upload its contents to the chosen host.');
