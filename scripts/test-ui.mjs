import assert from 'node:assert/strict';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import vm from 'node:vm';
import {parseHTML,DOMParser} from 'linkedom';
const root=new URL('../',import.meta.url);
const html=await readFile(new URL('index.html',root),'utf8'),source=await readFile(new URL('src/app.js',root),'utf8');
const data=JSON.parse(await readFile(new URL('library.json',root),'utf8'));
const {window,document}=parseHTML(html),audio=document.querySelector('#lf-audio'),canvas=document.querySelector('#lf-canvas');
const errors=[],frames=new Map();let nextFrame=0,width=1024,time=0,paused=true,src='',duration=0,ended=false;
let drawings=[],path='',styleStack=[];
const escape=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
const context={globalAlpha:1,strokeStyle:'#213b3c',fillStyle:'#213b3c',lineWidth:1,font:'12px Georgia',textAlign:'center',
 clearRect(){drawings=[];},setTransform(){},save(){styleStack.push({globalAlpha:this.globalAlpha,strokeStyle:this.strokeStyle,fillStyle:this.fillStyle,lineWidth:this.lineWidth,font:this.font,textAlign:this.textAlign});},restore(){Object.assign(this,styleStack.pop());},beginPath(){path='';},
 moveTo(x,y){assert(Number.isFinite(x+y));path+=`M${x.toFixed(2)},${y.toFixed(2)} `;},lineTo(x,y){assert(Number.isFinite(x+y));path+=`L${x.toFixed(2)},${y.toFixed(2)} `;},bezierCurveTo(...v){assert(v.every(Number.isFinite));path+='C'+v.map(x=>x.toFixed(2)).join(',')+' ';},
 arc(x,y,r,a,b){assert(Number.isFinite(x+y+r));path+=`M${x-r},${y}a${r},${r} 0 1,0 ${r*2},0a${r},${r} 0 1,0 ${-r*2},0 `;},
 stroke(){drawings.push(`<path d="${path}" fill="none" stroke="${this.strokeStyle}" stroke-width="${this.lineWidth}" opacity="${this.globalAlpha}"/>`);},fill(){drawings.push(`<path d="${path}" fill="${this.fillStyle}" opacity="${this.globalAlpha}"/>`);},
 fillText(text,x,y){assert(Number.isFinite(x+y));drawings.push(`<text x="${x}" y="${y}" text-anchor="middle" font-family="Georgia" font-size="${parseFloat(this.font)}" fill="${this.fillStyle}" opacity="${this.globalAlpha}">${escape(text)}</text>`);}
};
canvas.getContext=()=>context;
canvas.getBoundingClientRect=()=>({left:0,top:0,width,height:document.querySelector('#lf-field').classList.contains('is-family')?(width<620?590:660):(width<620?340:510)});
canvas.setPointerCapture=()=>{};canvas.releasePointerCapture=()=>{};
Object.defineProperties(audio,{currentTime:{get:()=>time,set:v=>{time=Number(v);ended=false;}},paused:{get:()=>paused},duration:{get:()=>duration},ended:{get:()=>ended},readyState:{get:()=>4},src:{get:()=>src,set:v=>{src=v;time=0;ended=false;duration=data.find(p=>p.audio===v).duration;queueMicrotask(()=>audio.dispatchEvent(new window.Event('loadedmetadata')));}}});
audio.play=async()=>{paused=false;audio.dispatchEvent(new window.Event('play'));};audio.pause=()=>{paused=true;audio.dispatchEvent(new window.Event('pause'));};
const location={hash:''},history={replaceState(a,b,url){location.hash=url;}};
const colours={'--lf-ink':'#213b3c','--lf-lower':'#75898b','--lf-copper':'#965432','--lf-paper':'#f1f2ed'};
let observer;
class ResizeObserver{constructor(callback){this.callback=callback;observer=this;}observe(){queueMicrotask(()=>this.callback());}}
const sandbox={document,window,DOMParser,location,history,ResizeObserver,devicePixelRatio:1,console:{error:e=>errors.push(e.message)},matchMedia:()=>({matches:true,addEventListener(){}}),getComputedStyle:el=>({color:el.style.color,getPropertyValue:key=>colours[key]}),requestAnimationFrame:fn=>{frames.set(++nextFrame,fn);return nextFrame;},fetch:async url=>{try{const body=await readFile(new URL(url,root),'utf8');return {ok:true,json:async()=>JSON.parse(body),text:async()=>body};}catch{return {ok:false};}}};
vm.createContext(sandbox);vm.runInContext(source,sandbox);
const settle=async()=>{for(let i=0;i<8;i++)await new Promise(resolve=>setImmediate(resolve));};
const until=async condition=>{for(let i=0;i<100;i++){if(condition())return;await new Promise(resolve=>setTimeout(resolve,10));}throw new Error('Timed out waiting for async UI');};
const tick=()=>{const callbacks=[...frames.values()];frames.clear();callbacks.forEach(fn=>fn());};
const click=(selector,extra={})=>{const el=document.querySelector(selector);assert(el,'Missing element '+selector);const event=new window.Event('click');Object.assign(event,extra);el.dispatchEvent(event);};
await until(()=>document.querySelectorAll('[data-work]').length===6||errors.length);tick();assert.deepEqual(errors,[]);assert.equal(document.querySelectorAll('[data-work]').length,6);
assert.equal(document.querySelector('#lf-title').textContent,'Velvet Estuary');
for(let i=0;i<data.length;i++){
 const p=data[i];click(`[data-work="${i}"]`);await settle();tick();
 assert.equal(document.querySelector('#lf-title').textContent,p.title);assert.equal(location.hash,'#'+p.slug);assert.equal(document.querySelector('#lf-download-pdf').getAttribute('href'),p.pdf);assert.equal(duration,p.duration);
 click('#lf-play');await settle();audio.currentTime=20;tick();assert(!audio.paused);assert(document.querySelector('#lf-time').textContent.startsWith('0:20 /'));
 const initial=canvas.dataset.orientation;click('[data-rotate="1"]');tick();assert.notEqual(canvas.dataset.orientation,initial);assert.equal(audio.currentTime,20);assert(!audio.paused);
 click('#lf-score-toggle');await until(()=>document.querySelector('#lf-score-body .lf-score-page'));const last=p.events.find(e=>e.ps.length>1);audio.currentTime=last.s+.1;tick();
 assert(document.querySelector('#lf-score-body').querySelector(`[id="${last.id}"].lf-now`),'Final dyad is not highlighted: '+p.title+'; body='+document.querySelector('#lf-score-body').innerHTML.slice(0,180)+'; highlighted='+document.querySelectorAll('.lf-now').length+'; errors='+errors.join(','));
 assert(document.querySelector('#lf-score-title').textContent===p.title);
 click('#lf-play');click('#lf-score-toggle');tick();
}
const orientation=canvas.dataset.orientation.split(',').map(Number);for(const axis of [0,1,2]){for(let i=0;i<12;i++)click(`[data-rotate="${axis}"]`);const now=canvas.dataset.orientation.split(',').map(Number);assert(Math.abs(Math.abs(now.reduce((n,x,i)=>n+x*orientation[i],0))-1)<.00001);}
click('#lf-kinship');tick();assert.equal(document.querySelector('#lf-kinship').getAttribute('aria-pressed'),'true');
await mkdir(new URL('work/qa-ui/',root),{recursive:true});
for(const size of [1024,360,320]){width=size;observer.callback();tick();const {height}=canvas.getBoundingClientRect();await writeFile(new URL(`work/qa-ui/kinship-${size}.svg`,root),`<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${height}"><rect width="100%" height="100%" fill="#f1f2ed"/>${drawings.join('')}</svg>`);assert(drawings.some(x=>x.includes('Tidal')));}
assert.deepEqual(errors,[]);console.log('UI integration passed for all six works: catalogue selection, deep links, complete timelines beyond 15 seconds, rotation during playback, final-chord highlighting, score toggles, 360-degree rotation, and family layout. Media playback is simulated here; MP3 decoding is checked separately.');
