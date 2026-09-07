import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {buildListeningPaths} from '../src/listening-paths.js';
const piece=(op,parent,pitch=60)=>({op,parent,events:[{ps:[pitch]}],note_onsets:1,performance:30});
const tree=[piece(1,null),piece(2,1),piece(3,1),piece(4,2),piece(5,2),piece(6,3)];
const orders=data=>Object.fromEntries(buildListeningPaths(data).map(route=>[route.id,route.order.map(i=>data[i].op)]));
assert.deepEqual(orders(tree).branches,[1,3,6,2,5,4],'Descendants stay together; newest sibling branches come first');
assert.deepEqual(orders(tree).generations,[1,2,3,4,5,6],'Every generation precedes its children');
assert.deepEqual(orders(tree).distant,[4,6,5,3,2,1],'Take the greatest remaining tree distance, breaking ties by opus');
const tones=[piece(1,null,48),piece(2,1,72),piece(3,1,84),piece(4,2,72)];
assert.deepEqual(orders(tones).drift,[2,4,3,1],'Matching pitch and density should precede more distant registers');
const single=[piece(7,null)];
for(const route of buildListeningPaths(single))assert.deepEqual(route.order,[0]);
const forest=[...tree,piece(7,null),piece(8,7)];
for(const route of buildListeningPaths(forest))assert.equal(new Set(route.order).size,forest.length);
assert.throws(()=>buildListeningPaths([]),/Empty/);
assert.throws(()=>buildListeningPaths([piece(1,null),piece(1,null)]),/Duplicate/);
assert.throws(()=>buildListeningPaths([piece(1,2)]),/Missing/);
assert.throws(()=>buildListeningPaths([piece(1,2),piece(2,1)]),/Cyclic/);

const data=JSON.parse(await readFile(new URL('../library.json',import.meta.url),'utf8'));
const routes=buildListeningPaths(data),expected=data.map(p=>p.op).sort((a,b)=>a-b);
for(const route of routes){
 assert.deepEqual(route.order.map(i=>data[i].op).sort((a,b)=>a-b),expected,route.title+' must include every work once');
 assert.notDeepEqual(route.order.map(i=>data[i].op),expected,route.title+' must offer a non-chronological sequence');
}
assert.equal(new Set(routes.map(route=>route.order.join(','))).size,routes.length,'Every route must be distinct');
assert.deepEqual(orders([...data].reverse()),orders(data),'Input file order must not change listening order');
assert.deepEqual(orders(data).light,[1,3,2,4,5,...data.filter(p=>p.op>=7).map(p=>p.op),6],'Preserve the original editorial walk');
const grown=[...data,piece(Math.max(...expected)+1,data.at(-1).op)];
for(const route of buildListeningPaths(grown))assert.equal(new Set(route.order).size,grown.length,'Future additions join every route automatically');
console.log(`Listening routes passed: five distinct complete ${data.length}-work sequences, exact ancestry traversals, musical drift, deterministic ties and catalogue growth.`);
