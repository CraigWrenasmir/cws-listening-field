import assert from 'node:assert/strict';
import {readFile,mkdtemp,rm} from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {tmpdir} from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {publicationFiles,SITE_LIMIT} from './site-distribution.mjs';
const root=fileURLToPath(new URL('../',import.meta.url));
const git=(args,options={})=>execFileSync('git',args,{cwd:root,encoding:'utf8',...options}).trim();
assert.equal(git(['status','--porcelain']),'','Commit the reviewed source before preparing publication');
const source=git(['rev-parse','HEAD']),files=await publicationFiles(root);
assert(files.reduce((s,f)=>s+f.bytes,0)<SITE_LIMIT);
const tracked=new Map(git(['ls-tree','-r',source]).split('\n').map(line=>{const [meta,name]=line.split('\t');return [name,meta.split(' ')[2]];}));
const entries=[],objectFormat=git(['rev-parse','--show-object-format']);
for(const f of files){
 const built=await readFile(path.join(root,'dist',f.path));
 assert(built.equals(await readFile(path.join(root,f.path))),'Stale build: '+f.path);
 const oid=createHash(objectFormat).update(`blob ${built.length}\0`).update(built).digest('hex');assert.equal(oid,tracked.get(f.path),'Uncommitted publication file: '+f.path);
 entries.push(`100644 ${oid}\t${f.path}`);
}
const remote=git(['ls-remote','--heads','origin','refs/heads/gh-pages']).split(/\s/)[0];
if(remote)git(['fetch','origin','gh-pages']);
const temporary=await mkdtemp(path.join(tmpdir(),'cws-pages-'));
let commit;
try{
 const env={...process.env,GIT_INDEX_FILE:path.join(temporary,'index')};
 git(['read-tree','--empty'],{env});git(['update-index','--index-info'],{env,input:entries.join('\n')+'\n'});
 const tree=git(['write-tree'],{env});
 commit=git(['commit-tree',tree,...(remote?['-p',remote]:[]),'-m',`Publish Listening Field from ${source}`]);
}finally{await rm(temporary,{recursive:true,force:true});}
if(process.argv.includes('--publish')){
 const volumes=JSON.parse(await readFile(path.join(root,'downloads/volumes.json'),'utf8'));
 for(const v of volumes.filter(v=>v.zip_url)){
  const response=await fetch(v.zip_url,{signal:AbortSignal.timeout(60000)});assert.equal(response.status,200,'Release archive must be available before publication');
  const bytes=Buffer.from(await response.arrayBuffer()),local=await readFile(path.join(root,v.zip));
  assert.equal(createHash('sha256').update(bytes).digest('hex'),createHash('sha256').update(local).digest('hex'),'Release archive differs: '+v.number);
 }
 // Both refs must advance safely together; never force either branch.
 git(['push','--atomic','origin',`${source}:refs/heads/main`,`${commit}:refs/heads/gh-pages`]);
}
console.log(JSON.stringify({sourceCommit:source,pagesCommit:commit,files:files.length,published:process.argv.includes('--publish')},null,2));
