import assert from 'node:assert/strict';
import {readFile,stat,readdir} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
const root=new URL('../',import.meta.url),data=JSON.parse(await readFile(new URL('library.json',root),'utf8'));
assert(data.length>=6);assert.equal(new Set(data.map(p=>p.op)).size,data.length);assert.equal(new Set(data.map(p=>p.slug)).size,data.length);
const series=JSON.parse(await readFile(new URL('data/series.json',root),'utf8'));
for(const p of data){
 const rules=series.find(s=>s.first_opus<=p.op&&p.op<=s.last_opus);assert(rules);assert.equal(p.series,rules.id);assert.equal(p.series_label,rules.label);assert.equal(p.note_limit,rules.note_limit);assert.equal(p.page_limit,rules.page_limit);
 assert(p.beats>0);
 assert(p.duration>15&&p.performance<p.duration);assert(p.pages>=1&&p.pages<=rules.page_limit);assert(p.note_onsets<=rules.note_limit);assert(/^\d{14}$/.test(p.stamp));
 assert.equal(p.events.reduce((n,e)=>n+e.ps.length,0),p.note_onsets);
 if(p.parent)assert(data.some(a=>a.op===p.parent));
 const visited=new Set();let parent=p;while(parent?.parent){assert(!visited.has(parent.op),'Cyclic musical ancestry');visited.add(parent.op);parent=data.find(a=>a.op===parent.parent);}
 const scoreText=(await Promise.all(p.scores.map(url=>readFile(new URL(url,root),'utf8')))).join('\n');
 for(const e of p.events){assert(e.b>=0&&e.d>0&&e.b+e.d<=p.beats+.001);assert(e.s>=0&&e.e>e.s&&e.e<=p.performance+.1);assert(scoreText.includes('id="'+e.id+'"'),'Missing score note '+e.id);}
 const motif=p.events.filter(e=>e.h===p.motif.hand&&(!p.motif.voice||e.v===p.motif.voice)&&e.b>=p.motif.start_beat&&e.b<p.motif.end_beat).slice(0,4);
 const pitchClass={Cb:11,C:0,'C#':1,Db:1,D:2,'D#':3,Eb:3,E:4,'E#':5,Fb:4,F:5,'F#':6,Gb:6,G:7,'G#':8,Ab:8,A:9,'A#':10,Bb:10,B:11,'B#':0};
 assert.deepEqual(motif.map(e=>e.p%12),p.motif.pitches.map(n=>pitchClass[n]),'Motif mismatch in '+p.title);
 for(const file of [p.audio,p.pdf,p.midi,p.xml,...p.scores]){assert(!file.includes('..'));assert((await stat(new URL(file,root))).size>0);}
}
for(const [page,script] of [['index.html','src/app.js'],['kinship.html','src/kinship.js']]){
const html=await readFile(new URL(page,root),'utf8'),js=await readFile(new URL(script,root),'utf8');
const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);assert.equal(new Set(ids).size,ids.length);
for(const [,id] of js.matchAll(/q\('#([^']+)'\)/g))assert(ids.includes(id),'Missing DOM element '+id);
assert(!/window\.openai|globalThis\.Tweak|Play excerpt|0:15/.test(js));
for(const [,link] of html.matchAll(/(?:href|src)="([^"]+)"/g)){if(!link.startsWith('http')&&!link.startsWith('#'))assert((await stat(new URL(link,root))).size>=0);}
}
const volumes=JSON.parse(await readFile(new URL('downloads/volumes.json',root),'utf8'));
assert.deepEqual(volumes.flatMap(v=>v.ops),data.map(p=>p.op),'Download volumes must cover the catalogue exactly once');
const downloadPage=await readFile(new URL('downloads/index.html',root),'utf8');
for(const v of volumes){
 assert(v.count>0&&v.count<=24&&v.count===v.ops.length);
 const members=data.filter(p=>v.ops.includes(p.op)),rules=series.find(s=>s.id===v.series);assert(rules);
 assert(members.every(p=>p.series===v.series),'Download volumes must not mix study series');
 assert.equal(v.series_label,rules.label);assert.equal(v.complete,v.count===24||v.last===rules.last_opus);
 assert.equal(v.pages,data.filter(p=>v.ops.includes(p.op)).reduce((n,p)=>n+p.pages,0));
 for(const kind of ['pdf','zip']){
  const bytes=(await stat(new URL(v[kind],root))).size;
  assert.equal(bytes,v[kind+'_bytes']);assert(bytes<90*1024*1024,'Split this download before it reaches the repository file limit');
  assert(downloadPage.includes(v[kind].split('/').at(-1)),'Volume is missing from the download page');
 }
}
for(const [,link] of downloadPage.matchAll(/(?:href|src)="([^"]+)"/g))assert((await stat(new URL(link,new URL('downloads/',root)))).size>=0);
const excluded=new Set(['.git','node_modules','work','dist','.venv','__pycache__','.DS_Store']);
async function siteBytes(directory){let total=0;for(const item of await readdir(directory,{withFileTypes:true})){if(excluded.has(item.name))continue;const url=new URL(item.name+(item.isDirectory()?'/':''),directory);if(item.isDirectory())total+=await siteBytes(url);else if(item.isFile()){const bytes=(await stat(url)).size;assert(bytes<90*1024*1024,'Review oversized repository file: '+item.name);total+=bytes;}}return total;}
const bytes=await siteBytes(root);assert(bytes<950_000_000,'Review distribution before approaching the 1 GB GitHub Pages site limit');
console.log(`Checked ${data.length} pieces: score IDs, complete playback timelines, note ceilings, family motifs, downloads and page controls. ${volumes.length} bounded download volume(s); site footprint ${(bytes/1024/1024).toFixed(1)} MiB.`);
