import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {decodeLibrary,EVENT_FIELDS} from '../src/library-format.js';
const raw=JSON.parse(await readFile(new URL('../library.json',import.meta.url),'utf8'));
const data=decodeLibrary(raw),catalog=JSON.parse(await readFile(new URL('../data/catalog.json',import.meta.url),'utf8'));
let count=0;
for(const p of data){
 const source=catalog.find(s=>s.op===p.op);
 const expected=source.events.map(e=>({id:e.id,h:e.hand,b:e.offset,d:e.duration,p:Math.max(...e.pitches),ps:e.pitches,s:e.seconds,e:e.end_seconds,...(e.voice?{v:e.voice}:{})}));
 assert.deepEqual(p.events,expected,`Every event field must match the source for Op. ${p.op}`);
 count+=expected.length;
}
// Keep the original tuple transport and legacy object catalogues readable.
const packed=data.map(p=>({...p,event_format:'tuple-v1',events:p.events.map(e=>EVENT_FIELDS.filter(k=>Object.hasOwn(e,k)).map(k=>e[k]))}));
assert.deepEqual(decodeLibrary(packed),data);
assert.deepEqual(decodeLibrary(data),data);

// These explicit rows cover both hands, unordered/duplicate chord pitches,
// untouched fractional timing, optional voices and a noncanonical full ID.
const compact=[{op:12,title:'Transport fixture',audio:'unchanged.mp3',event_format:'tuple-v2',events:[
 [[3,0],0,8.333333333333334,0.6666666666666666,[72,60,72],4.123456789,4.765432101],
 [[4,17],1,12,2,[48],6.2,7.8,'tenor'],
 ['cws012-rh-m04-n002',0,13,0.25,[75,67],7.9,8.123456789,'inner'],
]}];
const expectedCompact=[{op:12,title:'Transport fixture',audio:'unchanged.mp3',events:[
 {id:'cws12-rh-m3-n0',h:'rh',b:8.333333333333334,d:0.6666666666666666,p:72,ps:[72,60,72],s:4.123456789,e:4.765432101},
 {id:'cws12-lh-m4-n17',h:'lh',b:12,d:2,p:48,ps:[48],s:6.2,e:7.8,v:'tenor'},
 {id:'cws012-rh-m04-n002',h:'rh',b:13,d:0.25,p:75,ps:[75,67],s:7.9,e:8.123456789,v:'inner'},
]}];
const compactSnapshot=structuredClone(compact);
assert.deepEqual(decodeLibrary(compact),expectedCompact);
assert.deepEqual(compact,compactSnapshot,'Decoding must not modify its input');
assert.deepEqual(decodeLibrary([data[0],packed[1],...compact]),[data[0],data[1],...expectedCompact]);
const invalidCompact=row=>decodeLibrary([{op:12,event_format:'tuple-v2',events:[row]}]);
for(const length of [0,6,9])assert.throws(()=>invalidCompact(Array(length).fill(0)),/Invalid/);
for(const id of [[1],[-1,0],[0,0],[1,-1],[1,0.5],[1,Number.MAX_SAFE_INTEGER+1],null,42]){
 assert.throws(()=>invalidCompact([id,0,0,1,[60],0,1]),/Invalid/);
}
for(const hand of [-1,2,'rh',null])assert.throws(()=>invalidCompact(['id',hand,0,1,[60],0,1]),/Invalid/);
for(const pitches of [[],60,null,[60,'64'],[Infinity]])assert.throws(()=>invalidCompact(['id',0,0,1,pitches,0,1]),/Invalid/);
assert.throws(()=>decodeLibrary([{op:0,event_format:'tuple-v2',events:[[[1,0],0,0,1,[60],0,1]]}]),/Invalid/);
assert.throws(()=>decodeLibrary([{event_format:'tuple-v3',events:[]}]),/Unsupported/);
for(const format of ['tuple-v1','tuple-v2'])assert.throws(()=>decodeLibrary([{event_format:format,events:null}]),/Invalid/);
for(const length of [0,7,10])assert.throws(()=>decodeLibrary([{event_format:'tuple-v1',events:[Array(length).fill(0)]}]),/Invalid/);
assert.throws(()=>decodeLibrary({}),/Invalid/);
console.log(`Lossless catalogue transport verified: ${data.length} pieces, ${count} events; all IDs, pitches, voices and timing values match source.`);
