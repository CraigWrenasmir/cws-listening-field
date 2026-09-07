import assert from 'node:assert/strict';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import vm from 'node:vm';
import {parseHTML,DOMParser} from 'linkedom';
import {buildListeningPaths} from '../src/listening-paths.js';
const root=new URL('../',import.meta.url);
const html=await readFile(new URL('index.html',root),'utf8'),source=await readFile(new URL('src/app.js',root),'utf8');
const data=JSON.parse(await readFile(new URL('library.json',root),'utf8'));
const {window,document}=parseHTML(html),audio=document.querySelector('#lf-audio'),canvas=document.querySelector('#lf-canvas');
const errors=[],frames=new Map();let nextFrame=0,width=1024,time=0,paused=true,src='',duration=0,ended=false,rejectPlay=false,playGate=null;
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
audio.play=async()=>{if(playGate)await playGate;if(rejectPlay)throw new Error('Playback denied');paused=false;audio.dispatchEvent(new window.Event('play'));};audio.pause=()=>{paused=true;audio.dispatchEvent(new window.Event('pause'));};
const location={hash:process.env.CWS_TEST_HASH||''},historyCalls=[],history={replaceState(a,b,url){location.hash=url;historyCalls.push(['replace',url]);},pushState(a,b,url){location.hash=url;historyCalls.push(['push',url]);}};
window.scrollTo=()=>{};window.HTMLElement.prototype.scrollIntoView=()=>{};
const colours={'--lf-ink':'#213b3c','--lf-lower':'#75898b','--lf-copper':'#965432','--lf-tenor':'#526e58','--lf-paper':'#f1f2ed'};
let observer;
class ResizeObserver{constructor(callback){this.callback=callback;observer=this;}observe(){queueMicrotask(()=>this.callback());}}
const sandbox={document,window,DOMParser,location,history,ResizeObserver,devicePixelRatio:1,console:{error:e=>errors.push(e.message)},matchMedia:()=>({matches:true,addEventListener(){}}),getComputedStyle:el=>({color:el.style.color,getPropertyValue:key=>colours[key]}),requestAnimationFrame:fn=>{frames.set(++nextFrame,fn);return nextFrame;},fetch:async url=>{try{const body=await readFile(new URL(url,root),'utf8');return {ok:true,json:async()=>JSON.parse(body),text:async()=>body};}catch{return {ok:false};}}};
sandbox.buildListeningPaths=buildListeningPaths;
vm.createContext(sandbox);vm.runInContext(source.replace("import {buildListeningPaths} from './listening-paths.js';",''),sandbox);
const settle=async()=>{for(let i=0;i<8;i++)await new Promise(resolve=>setImmediate(resolve));};
const until=async condition=>{for(let i=0;i<100;i++){if(condition())return;await new Promise(resolve=>setTimeout(resolve,10));}throw new Error('Timed out waiting for async UI');};
const tick=()=>{const callbacks=[...frames.values()];frames.clear();callbacks.forEach(fn=>fn());};
const click=(selector,extra={})=>{const el=document.querySelector(selector);assert(el,'Missing element '+selector);const event=new window.Event('click');Object.assign(event,extra);el.dispatchEvent(event);};
await until(()=>document.querySelectorAll('[data-work]').length===data.length||errors.length);tick();assert.deepEqual(errors,[]);assert.equal(document.querySelectorAll('[data-work]').length,data.length);
assert(audio.paused,'Loading the site must not autoplay');
const home=()=>!document.querySelector('#lf-overview').hidden;
const route=hash=>{location.hash=hash;window.dispatchEvent(new window.Event('hashchange'));};
const initialPiece=data.find(p=>'#'+p.slug===location.hash);
assert.equal(home(),!initialPiece);
if(initialPiece){assert.equal(document.querySelector('#lf-title').textContent,initialPiece.title);assert.equal(src,initialPiece.audio);}
else assert.equal(src,'','Overview should not load a recording');
assert.equal(historyCalls.length,0,'Initial load must preserve the incoming address');
assert.equal(document.querySelectorAll('[data-contour]').length,data.length,'The collection drawing must include every work');
assert.equal(document.querySelector('#lf-header').hidden,home());
assert.equal(document.querySelector('#lf-colophon').hidden,home());
assert.equal(document.querySelector('#lf-enter-kinship').getAttribute('href'),'kinship.html');
assert.equal(document.querySelectorAll('#lf-overview a').length,1,'Entrance must have only the Kinship link');
assert.equal(document.querySelectorAll('#lf-overview p, #lf-overview button, #lf-overview figcaption').length,0,'Entrance must have no explanation or extra controls');
if(process.argv.includes('--routing-only')){assert.deepEqual(errors,[]);console.log('Initial route passed: '+(location.hash||'overview'));process.exit(0);}
click('[data-work="1"]');click('#lf-play');await settle();tick();assert(!home());assert(!audio.paused);assert(!document.querySelector('#lf-header').hidden);
click('#lf-home');tick();assert(home());assert(audio.paused);assert.equal(location.hash,'#overview');assert(document.querySelector('#lf-header').hidden);assert(document.querySelector('#lf-colophon').hidden);
time=duration;ended=true;audio.dispatchEvent(new window.Event('ended'));assert(home(),'An old ended event must not leave the entrance');
route('#'+data[1].slug);await settle();tick();assert(!home());assert.equal(document.querySelector('#lf-title').textContent,'Velvet Estuary');assert(audio.paused);
click('#lf-score-toggle');await until(()=>document.querySelector('#lf-score-body .lf-score-page'));click('#lf-play');await settle();click('#lf-home');assert(home());assert(audio.paused);
route('#'+data[1].slug);await settle();tick();assert(document.querySelector('#lf-score-shell').hidden);assert(!document.querySelector('#lf-field').hidden);assert(audio.paused);
route('');assert(home());route('#'+data[1].slug);assert(!home(),'Back and forward must reopen even the same selected piece');route('#unrecognised');assert(home());assert(audio.paused);
for(let i=0;i<data.length;i++){
 const p=data[i];click(`[data-work="${i}"]`);await settle();tick();
 assert.equal(document.querySelector('#lf-title').textContent,p.title);assert.equal(location.hash,'#'+p.slug);assert.equal(document.querySelector('#lf-download-pdf').getAttribute('href'),p.pdf);assert.equal(duration,p.duration);
 const extraVoices=['inner','tenor'].map(kind=>{const event=p.events.find(e=>e.v===kind);assert.equal(document.querySelector('#lf-'+kind+'-legend').hidden,!event);return event;}).filter(Boolean);
 const voiceProbes=extraVoices.map(e=>e.s+Math.min(.1,(e.e-e.s)/2));
 const soundingAt=time=>p.events.filter(e=>e.s<=time&&time<e.e);
 click('#lf-play');await settle();audio.currentTime=20;tick();assert(!audio.paused);assert(document.querySelector('#lf-time').textContent.startsWith('0:20 /'));
 const initial=canvas.dataset.orientation;click('[data-rotate="1"]');tick();assert.notEqual(canvas.dataset.orientation,initial);assert.equal(audio.currentTime,20);assert(!audio.paused);
 for(const time of voiceProbes){audio.currentTime=time;tick();assert.equal(drawings.filter(d=>d.includes('opacity="0.12"')).length,new Set(soundingAt(time).map(e=>e.v||e.h)).size,'Each sounding voice needs its own playback glow');}
 click('#lf-score-toggle');await until(()=>document.querySelector('#lf-score-body .lf-score-page'));const last=p.events.find(e=>e.ps.length>1)||p.events.at(-1);audio.currentTime=last.s+.1;tick();
 assert(document.querySelector('#lf-score-body').querySelector(`[id="${last.id}"].lf-now`),'Selected score event is not highlighted: '+p.title+'; body='+document.querySelector('#lf-score-body').innerHTML.slice(0,180)+'; highlighted='+document.querySelectorAll('.lf-now').length+'; errors='+errors.join(','));
 assert(document.querySelector('#lf-score-title').textContent===p.title);
 for(const time of voiceProbes){audio.currentTime=time;tick();for(const e of soundingAt(time))assert(document.querySelector('#lf-score-body').querySelector(`[id="${e.id}"].lf-now`),'An independent voice is missing its score highlight');}
 const tied=document.querySelector('#lf-score-body [id*="-tie-"]');
 if(tied){const event=p.events.find(e=>e.id===tied.getAttribute('data-event'));assert(event,'Tie fragment needs a sounded-event mapping');audio.currentTime=event.e-.1;tick();assert(tied.classList.contains('lf-now'),'Tied continuation must remain highlighted to its notated release');}
 click('#lf-play');click('#lf-score-toggle');tick();
}
const orientation=canvas.dataset.orientation.split(',').map(Number);for(const axis of [0,1,2]){for(let i=0;i<12;i++)click(`[data-rotate="${axis}"]`);const now=canvas.dataset.orientation.split(',').map(Number);assert(Math.abs(Math.abs(now.reduce((n,x,i)=>n+x*orientation[i],0))-1)<.00001);}
click('#lf-kinship');tick();assert.equal(document.querySelector('#lf-kinship').getAttribute('aria-pressed'),'true');
await mkdir(new URL('work/qa-ui/',root),{recursive:true});
for(const size of [1024,360,320]){width=size;observer.callback();tick();const {height}=canvas.getBoundingClientRect();await writeFile(new URL(`work/qa-ui/kinship-${size}.svg`,root),`<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${height}"><rect width="100%" height="100%" fill="#f1f2ed"/>${drawings.join('')}</svg>`);assert(drawings.some(x=>x.includes(data.at(-1).title.split(' ')[0])));}
const routes=buildListeningPaths(data),queue=routes[0].order.map(i=>data[i]);
assert.deepEqual([...document.querySelectorAll('#lf-path-route option')].map(el=>el.value),routes.map(route=>route.id));
assert.equal(document.querySelector('#lf-path-route').value,routes[0].id);
assert.equal(document.querySelector('#lf-path-description').textContent,routes[0].description);
assert.equal(new Set(queue.map(p=>p.op)).size,data.length);
assert.deepEqual([...document.querySelectorAll('[data-path]')].map(el=>el.textContent),queue.map(p=>p.title));
const title=()=>document.querySelector('#lf-title').textContent;
const finish=()=>{time=duration;ended=true;paused=true;audio.dispatchEvent(new window.Event('pause'));audio.dispatchEvent(new window.Event('ended'));};
click('#lf-playlist-toggle');await settle();assert.equal(title(),queue[0].title);assert(!audio.paused);assert.equal(document.querySelector('#lf-next').textContent,queue[1].title+' →');
click('#lf-play');assert(audio.paused);assert.equal(title(),queue[0].title);click('#lf-next');await settle();assert.equal(title(),queue[1].title);assert(audio.paused,'Skipping while paused should remain paused');
click('#lf-play');click('#lf-next');await settle();assert.equal(title(),queue[2].title);assert(!audio.paused);click('#lf-prev');await settle();assert.equal(title(),queue[1].title);assert(!audio.paused);
click('#lf-playlist-toggle');assert(audio.paused);assert.equal(document.querySelector('#lf-playlist-toggle').getAttribute('aria-pressed'),'false');
click('#lf-score-toggle');click('#lf-playlist-toggle');await settle();
const heard=[];
for(let position=0;position<queue.length;position++){
 const p=queue[position];await until(()=>document.querySelector('#lf-score-title').textContent===p.title&&document.querySelector('#lf-score-body .lf-score-page'));
 assert.equal(title(),p.title);assert(!audio.paused);heard.push(p.op);assert.equal(document.querySelector('#lf-download-pdf').getAttribute('href'),p.pdf);assert.equal(location.hash,'#'+p.slug);
 assert.equal(document.querySelector('#lf-counter').textContent,String(position+1).padStart(2,'0')+' / '+String(data.length).padStart(2,'0'));
 assert.equal(document.querySelector(`[data-path="${position}"]`).getAttribute('aria-current'),'true');
 const event=p.events[0];audio.currentTime=event.s+.1;tick();assert(document.querySelector(`[id="${event.id}"].lf-now`),'Playlist score must follow the current piece');
 finish();await settle();tick();
}
assert.deepEqual(heard,queue.map(p=>p.op));assert(audio.paused);assert.equal(title(),queue.at(-1).title);assert.equal(document.querySelector('#lf-playlist-toggle').getAttribute('aria-pressed'),'false');assert(document.querySelector('#lf-path-status').textContent.startsWith(routes[0].title+' complete'));
finish();await settle();assert.equal(title(),queue.at(-1).title,'End of playlist must not loop');
click('#lf-playlist-toggle');await settle();rejectPlay=true;finish();await settle();assert.equal(title(),queue[1].title);assert(audio.paused);assert(!document.querySelector('#lf-audio-error').hidden);assert.equal(document.querySelector('#lf-playlist-toggle').getAttribute('aria-pressed'),'true');
rejectPlay=false;click('#lf-play');await settle();assert(!audio.paused);assert(document.querySelector('#lf-audio-error').hidden);assert.equal(title(),queue[1].title);
click('[data-work="4"]');await settle();assert.equal(title(),data[4].title);assert(audio.paused);assert.equal(document.querySelector('#lf-playlist-toggle').getAttribute('aria-pressed'),'false');finish();await settle();assert.equal(title(),data[4].title,'Individual listening must not auto-advance');
click('[data-path="3"]');await settle();assert.equal(title(),queue[3].title);assert(!audio.paused);finish();await settle();assert.equal(title(),queue[4].title);click('#lf-playlist-toggle');
click('#lf-score-toggle');
const selectRoute=id=>{
 const select=document.querySelector('#lf-path-route');
 // Linkedom clears the current selection even when setting another option
 // false, so clear first and then perform the native select's single choice.
 for(const option of select.querySelectorAll('option'))option.selected=false;
 select.querySelector('[value="'+id+'"]').selected=true;
 select.dispatchEvent(new window.Event('change'));
};
for(const route of routes.slice(1)){
 selectRoute(route.id);assert(audio.paused,'Selecting a route must not autoplay');
 assert.equal(document.querySelector('#lf-path-description').textContent,route.description);
 assert.deepEqual([...document.querySelectorAll('[data-path]')].map(el=>Number(el.dataset.opus)),route.order.map(i=>data[i].op));
 click('#lf-playlist-toggle');await settle();
 for(const [position,index] of route.order.entries()){
  assert.equal(title(),data[index].title);assert(!audio.paused);assert.equal(src,data[index].audio);
  assert.equal(document.querySelector('#lf-download-pdf').getAttribute('href'),data[index].pdf);
  assert.equal(document.querySelector(`[data-path="${position}"]`).getAttribute('aria-current'),'true');
  if(position<route.order.length-1)assert.equal(document.querySelector('#lf-next').textContent,data[route.order[position+1]].title+' →');
  finish();await settle();
 }
 assert(audio.paused);assert(document.querySelector('#lf-path-status').textContent.startsWith(route.title+' complete'));
 const last=title();finish();await settle();assert.equal(title(),last,'No route should loop after completion');
}
click('#lf-playlist-toggle');await settle();audio.currentTime=8;
const beforeChange=title();selectRoute('distant');
assert(audio.paused);assert.equal(audio.currentTime,8);assert.equal(title(),beforeChange);assert.equal(document.querySelector('#lf-playlist-toggle').getAttribute('aria-pressed'),'false');
click('#lf-play');await settle();assert(!audio.paused);finish();await settle();assert.equal(title(),beforeChange,'Resuming the individual work must not continue the cancelled route');
click('#lf-playlist-toggle');await settle();assert.equal(title(),data[routes.find(r=>r.id==='distant').order[0]].title,'Play route must begin at its first work');
click('#lf-play');click('#lf-next');await settle();assert(audio.paused,'A paused skip must follow the new route and stay paused');
assert.equal(title(),data[routes.find(r=>r.id==='distant').order[1]].title);
selectRoute('branches');
let releasePlay;playGate=new Promise(resolve=>releasePlay=resolve);
click('#lf-playlist-toggle');selectRoute('generations');releasePlay();playGate=null;await settle();
assert(audio.paused,'A delayed play request must not restart audio after changing routes');
assert.equal(document.querySelector('#lf-playlist-toggle').getAttribute('aria-pressed'),'false');
assert.deepEqual(errors,[]);console.log('UI integration passed: all catalogue works, score highlights and five complete listening routes; route changes, pause/resume, skips, queue previews, final stop, manual selection, rejected and delayed playback. Media playback is simulated; MP3 decoding is checked separately.');
