import assert from 'node:assert/strict';
import {readFile,stat} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
const root=new URL('../',import.meta.url),data=JSON.parse(await readFile(new URL('library.json',root),'utf8'));
assert(data.length>=6);assert.equal(new Set(data.map(p=>p.op)).size,data.length);assert.equal(new Set(data.map(p=>p.slug)).size,data.length);
for(const p of data){
 assert(p.duration>15&&p.performance<p.duration);assert(p.pages>=1&&p.pages<=4);assert(p.note_onsets<=256);assert(/^\d{14}$/.test(p.stamp));
 assert.equal(p.events.reduce((n,e)=>n+e.ps.length,0),p.note_onsets);
 if(p.parent)assert(data.some(a=>a.op===p.parent));
 const visited=new Set();let parent=p;while(parent?.parent){assert(!visited.has(parent.op),'Cyclic musical ancestry');visited.add(parent.op);parent=data.find(a=>a.op===parent.parent);}
 const scoreText=(await Promise.all(p.scores.map(url=>readFile(new URL(url,root),'utf8')))).join('\n');
 for(const e of p.events){assert(e.s>=0&&e.e>e.s&&e.e<=p.performance+.1);assert(scoreText.includes('id="'+e.id+'"'),'Missing score note '+e.id);}
 const motif=p.events.filter(e=>e.h===p.motif.hand&&e.b>=p.motif.start_beat&&e.b<p.motif.end_beat).slice(0,4);
 const pitchClass={C:0,'C#':1,D:2,Eb:3,E:4,F:5,'F#':6,G:7,Ab:8,A:9,Bb:10,B:11};
 assert.deepEqual(motif.map(e=>e.p%12),p.motif.pitches.map(n=>pitchClass[n]),'Motif mismatch in '+p.title);
 for(const file of [p.audio,p.pdf,p.midi,p.xml,...p.scores]){assert(!file.includes('..'));assert((await stat(new URL(file,root))).size>0);}
}
const html=await readFile(new URL('index.html',root),'utf8'),js=await readFile(new URL('src/app.js',root),'utf8');
const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);assert.equal(new Set(ids).size,ids.length);
for(const [,id] of js.matchAll(/q\('#([^']+)'\)/g))assert(ids.includes(id),'Missing DOM element '+id);
assert(!/window\.openai|globalThis\.Tweak|Play excerpt|0:15/.test(js));
for(const [,link] of html.matchAll(/(?:href|src)="([^"]+)"/g)){if(!link.startsWith('http'))assert((await stat(new URL(link,root))).size>=0);}
console.log(`Checked ${data.length} pieces: score IDs, complete playback timelines, note ceilings, family motifs, downloads and page controls.`);
