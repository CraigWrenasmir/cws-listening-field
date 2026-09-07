import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {parseHTML} from 'linkedom';
import {layoutKinship} from '../src/kinship-layout.js';
import {mountKinship,startKinship} from '../src/kinship.js';
const root=new URL('../',import.meta.url),data=JSON.parse(await readFile(new URL('library.json',root),'utf8'));
const html=await readFile(new URL('kinship.html',root),'utf8'),layout=layoutKinship(data);
assert.deepEqual(layout.nodes.map(p=>p.op),data.map(p=>p.op));
assert.deepEqual(layout.links,data.filter(p=>p.parent!=null).map(p=>({source:p.parent,target:p.op})), 'Only documented parent relationships may be drawn');
assert.deepEqual(layoutKinship(data),layout,'Layout must be reproducible');
assert.throws(()=>layoutKinship([{op:1,parent:2}]),/Missing/);
assert.throws(()=>layoutKinship([{op:1,parent:2},{op:2,parent:1}]),/Cyclic/);
for(const node of layout.nodes){assert(Number.isFinite(node.x+node.y));assert(node.x>=40&&node.x<=1160&&node.y>=40&&node.y<=740,'Every node must fit the initial map');}
for(let i=0;i<layout.nodes.length;i++)for(let j=i+1;j<layout.nodes.length;j++)assert(Math.hypot(layout.nodes[i].x-layout.nodes[j].x,layout.nodes[i].y-layout.nodes[j].y)>20,'Opus points must remain distinct');
for(const portrait of [false,true]){
 const {document,window}=parseHTML(html),container=document.getElementById('cws-kinship'),svg=document.getElementById('kf-map');
 let rect={left:0,top:0,width:portrait?360:1200,height:portrait?600:780},resize;
 svg.getBoundingClientRect=()=>rect;const captures=new Set();svg.setPointerCapture=id=>captures.add(id);svg.hasPointerCapture=id=>captures.has(id);svg.releasePointerCapture=id=>captures.delete(id);
 window.ResizeObserver=class{constructor(callback){resize=callback;}observe(){}};
 window.Element.prototype.focus=function(){this.dispatchEvent(new window.Event('focus'));};
 const send=(target,type,extra={})=>{const event=new window.Event(type,{bubbles:true,cancelable:true});Object.assign(event,extra);target.dispatchEvent(event);return event;};
 const click=id=>send(document.getElementById(id),'click');
 mountKinship(container,data);
 const all=()=>[...document.querySelectorAll('[data-opus]')],edges=()=>[...document.querySelectorAll('[data-parent]')];
 assert.equal(all().length,data.length);assert.equal(edges().length,layout.links.length);
 assert.equal(document.querySelectorAll('audio').length,0,'Kinship must not autoplay or preload a recording');
 assert.equal(svg.getAttribute('viewBox'),portrait?'0 0 780 1200':'0 0 1200 780');
 for(const p of data){const link=document.querySelector(`[data-opus="${p.op}"]`);assert.equal(link.getAttribute('href'),'index.html#'+p.slug);assert(link.getAttribute('aria-label').includes(p.title));send(link,'focus');assert(document.getElementById('kf-selected').textContent.includes(p.title));
  const expected=[];let ancestor=p;while(ancestor.parent!=null){expected.push(ancestor.op);ancestor=data.find(n=>n.op===ancestor.parent);}
  assert.deepEqual(edges().filter(el=>el.classList.contains('is-lineage')).map(el=>Number(el.dataset.child)).sort((a,b)=>a-b),expected.sort((a,b)=>a-b));
 }
 click('kf-zoom-in');click('kf-zoom-in');click('kf-zoom-in');assert(Number(svg.dataset.zoom)>2);assert.equal(svg.querySelectorAll('.kf-name').length,0,'Zoom must not add crowded titles to the map');assert.equal(svg.querySelectorAll('.kf-node text').length,data.length,'Only opus numbers should be drawn');assert.equal(all().length,data.length);assert.equal(edges().length,layout.links.length,'Zoom must never filter relationships');
 const hovered=document.querySelector('[data-opus="2"]');send(hovered,'pointerenter',{pointerType:'mouse'});assert(document.getElementById('kf-selected').textContent.includes('Velvet Estuary'));assert(hovered.querySelector('title').textContent.includes('Velvet Estuary'));assert(!send(hovered,'click',{pointerType:'mouse',detail:1}).defaultPrevented,'Mouse click should open the work');
 const touched=document.querySelector('[data-opus="3"]');send(touched,'pointerdown',{button:0,pointerId:8,pointerType:'touch',clientX:160,clientY:240});send(touched,'pointerup',{pointerId:8,pointerType:'touch'});assert(send(touched,'click',{detail:1}).defaultPrevented,'Touch must preview before opening, including browsers without click pointerType');assert(document.getElementById('kf-selected').textContent.includes(data[2].title));assert.equal(document.getElementById('kf-selected').getAttribute('href'),'index.html#'+data[2].slug);assert(!send(document.getElementById('kf-selected'),'click',{pointerType:'touch',detail:1}).defaultPrevented,'The selected title opens on touch');assert(!send(touched,'click',{detail:0}).defaultPrevented,'Keyboard activation must remain a direct link');
 const beforePan=svg.getAttribute('viewBox');send(svg,'pointerdown',{button:0,pointerId:1,clientX:160,clientY:240});send(svg,'pointermove',{pointerId:1,clientX:195,clientY:280});send(svg,'pointerup',{pointerId:1,clientX:195,clientY:280});assert.notEqual(svg.getAttribute('viewBox'),beforePan);assert(send(svg,'click').defaultPrevented,'A drag must not open a piece');assert(!send(svg,'click').defaultPrevented,'An ordinary click must remain a link');
 click('kf-fit');assert.equal(svg.dataset.zoom,'1.000');assert.equal(svg.querySelectorAll('.kf-name').length,0);assert.equal(all().length,data.length);
 send(svg,'wheel',{deltaY:-300,clientX:180,clientY:300});assert(Number(svg.dataset.zoom)>1);click('kf-fit');
 send(svg,'pointerdown',{button:0,pointerId:2,clientX:120,clientY:220});send(svg,'pointerdown',{button:0,pointerId:3,clientX:240,clientY:220});send(svg,'pointermove',{pointerId:3,clientX:300,clientY:220});assert(Number(svg.dataset.zoom)>1,'Pinch must zoom');send(svg,'pointercancel',{pointerId:2});send(svg,'pointercancel',{pointerId:3});click('kf-fit');
 const beforeKey=document.querySelector('.is-current').dataset.opus;send(svg,'keydown',{key:'ArrowLeft'});if(document.querySelector('.is-current').dataset.opus===beforeKey)send(svg,'keydown',{key:'ArrowRight'});assert.notEqual(document.querySelector('.is-current').dataset.opus,beforeKey,'Keyboard arrows must reach another work');
 send(svg,'keydown',{key:'+'});assert(Number(svg.dataset.zoom)>1);send(svg,'keydown',{key:'0'});assert.equal(svg.dataset.zoom,'1.000');
 rect={left:0,top:0,width:portrait?1200:360,height:portrait?780:600};resize();assert.equal(svg.getAttribute('viewBox'),portrait?'0 0 1200 780':'0 0 780 1200');assert.equal(all().length,data.length);assert.equal(edges().length,layout.links.length);
}
const failure=parseHTML(html).document;await startKinship(failure,async()=>({ok:false}));assert(!failure.getElementById('kf-error').hidden);
console.log(`Kinship passed: ${data.length} works, ${layout.links.length} exact ancestry links, all points within initial view, distinct positions, stable layout, direct links, lineage selection, landscape/portrait, zoom/pan/pinch/keyboard/reset, and loading failure. DOM harness; no browser rendering test.`);
