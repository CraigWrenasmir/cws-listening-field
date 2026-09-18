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
// Exercise the packed path even when the current checked-in catalogue is legacy.
const packed=data.map(p=>({...p,event_format:'tuple-v1',events:p.events.map(e=>EVENT_FIELDS.filter(k=>Object.hasOwn(e,k)).map(k=>e[k]))}));
assert.deepEqual(decodeLibrary(packed),data);
assert.deepEqual(decodeLibrary(data),data);
assert.throws(()=>decodeLibrary([{event_format:'tuple-v2',events:[]}]),/Unsupported/);
for(const length of [0,7,10])assert.throws(()=>decodeLibrary([{event_format:'tuple-v1',events:[Array(length).fill(0)]}]),/Invalid/);
assert.throws(()=>decodeLibrary({}),/Invalid/);
console.log(`Lossless catalogue transport verified: ${data.length} pieces, ${count} events; all IDs, pitches, voices and timing values match source.`);
