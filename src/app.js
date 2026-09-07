
(async function(){
const root=document.getElementById('cws-listening-field');
const response=await fetch('library.json');
if(!response.ok)throw new Error('Catalogue unavailable');
const data=await response.json();
const q=(s)=>root.querySelector(s),canvas=q('#lf-canvas'),ctx=canvas.getContext('2d'),audio=q('#lf-audio');
const state={overview:true,selected:Math.min(1,data.length-1),kinship:false,score:false,playlist:false,density:17,relief:1.0};
let w=0,h=0,frame=0,camera=1,zoom=0,drag=null,lastActive=[];
const norm=q=>{const n=Math.hypot(...q);return q.map(x=>x/n);};
function multiply(a,b){const [x,y,z,s]=a,[u,v,w,t]=b;return norm([s*u+x*t+y*w-z*v,s*v-x*w+y*t+z*u,s*w+x*v-y*u+z*t,s*t-x*u-y*v-z*w]);}
function axisTurn(axis,angle){const s=Math.sin(angle/2),q=[0,0,0,Math.cos(angle/2)];q[axis]=s;return q;}
let orientation=multiply(axisTurn(1,.24),axisTurn(0,-.27));
let matrix=[],geometry=new Map(),radius=1;
function updateRotation(){
 const [x,y,z,s]=orientation;
 matrix=[1-2*(y*y+z*z),2*(x*y-z*s),2*(x*z+y*s),2*(x*y+z*s),1-2*(x*x+z*z),2*(y*z-x*s),2*(x*z-y*s),2*(y*z+x*s),1-2*(x*x+y*y)];
 canvas.dataset.orientation=orientation.map(v=>v.toFixed(6)).join(',');
}
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const trackKinds=data.map(p=>['upper','bass',...['inner','tenor'].filter(kind=>p.events.some(e=>e.v===kind))]);
const tracks=data.map((p,index)=>trackKinds[index].map(kind=>p.events.filter(e=>kind==='upper'?e.h==='rh'&&e.v!=='inner':kind==='bass'?e.h==='lh'&&e.v!=='tenor':e.v===kind).sort((a,b)=>a.b-b.b)));
const voiceLayouts={upper:[70,12,19],bass:[51,-10,-19],inner:[70,1,0],tenor:[57,-1,-4]};
const voicePaletteKeys={upper:'ink',bass:'lower',inner:'copper',tenor:'tenor'};
const range=data.map(p=>[p.title,p.motif.pitches.join(' · ')]);
const byOp=new Map(data.map((p,i)=>[p.op,i]));
// An editorial walk: root and sibling, then Velvet Estuary's branch, ending in C major.
// Later descendants extend the walk before Willow Transit's warm close.
const listeningPath=[...new Set([...([1,3,2,4,5,...data.filter(p=>p.op>=7).map(p=>p.op),6].filter(op=>byOp.has(op)).map(op=>byOp.get(op))),...data.map((_,i)=>i)])];
let playbackRequest=0;
const depth=(p,seen=new Set())=>{if(!p.parent||seen.has(p.op)||!byOp.has(p.parent))return 0;seen.add(p.op);return 1+depth(data[byOp.get(p.parent)],seen);};
const levels=data.map(p=>depth(p));
// The entrance is a collective drawing: one contour per work, using its
// actual upper-voice pitches and normalised musical time. No random scenery.
function prepareOverview(){
 const svgNS='http://www.w3.org/2000/svg';
 data.forEach((p,index)=>{
  const layer=index/Math.max(1,data.length-1),path=document.createElementNS(svgNS,'path');
  const coordinates=[];
  for(let sample=0;sample<=160;sample++){
   const t=sample/160,theta=-2.6+t*5.2,pitch=traceValue(index,0,t);
   const radius=160+layer*112+(pitch-72)*1.15;
   const x=390+Math.cos(theta)*radius*1.09;
   const y=230+Math.sin(theta)*radius*.57+layer*79-(pitch-72)*1.45;
   coordinates.push((sample?'L':'M')+x.toFixed(2)+','+y.toFixed(2));
  }
  path.setAttribute('d',coordinates.join(' '));path.setAttribute('data-contour',p.op);
  if(p.op===2||index===data.length-1)path.setAttribute('class','lf-atlas-accent');
  q('#lf-atlas-lines').append(path);
 });
 const totalMinutes=Math.round(data.reduce((sum,p)=>sum+p.duration,0)/60);
 const listeningTime=totalMinutes>=60?Math.floor(totalMinutes/60)+' hr '+totalMinutes%60+' min':totalMinutes+' min';
 q('#lf-overview-stats').replaceChildren();
 for(const text of [data.length+' piano studies',listeningTime+' of listening','Scores & recordings to keep']){const span=document.createElement('span');span.textContent=text;q('#lf-overview-stats').append(span);}
 q('#lf-atlas-range').textContent=String(data[0].op).padStart(3,'0')+' — '+String(data.at(-1).op).padStart(3,'0');
 q('#lf-overview-walk-length').textContent=data.length+' pieces · '+listeningTime;
 q('#lf-latest-title').textContent=data.at(-1).title;q('#lf-latest-opus').textContent='CWS Op. '+data.at(-1).op+' · Latest addition';
 for(const id of ['lf-begin','lf-overview-playlist','lf-overview-family','lf-overview-latest'])q('#'+id).disabled=false;
}
let family=[];
function refreshFamily(){
 let visible=data.map((_,i)=>i);
 if(data.length>6){
  const near=[state.selected];let parent=data[state.selected].parent;
  for(let step=0;step<2&&byOp.has(parent);step++){const index=byOp.get(parent);near.push(index);parent=data[index].parent;}
  const children=visible.filter(i=>data[i].parent===data[state.selected].op);
  const siblings=visible.filter(i=>data[i].parent===data[state.selected].parent&&i!==state.selected).sort((a,b)=>Math.abs(a-state.selected)-Math.abs(b-state.selected));
  visible=[...new Set([...near,...children,...siblings])].slice(0,6).sort((a,b)=>a-b);
 }
 const first=Math.min(...visible.map(i=>levels[i])),last=Math.max(...visible.map(i=>levels[i]));
 family=data.map(()=>null);
 for(const i of visible){const peers=visible.filter(j=>levels[j]===levels[i]);family[i]={x:(peers.indexOf(i)+1)/(peers.length+1),y:data.length<=6?.11+levels[i]*.30:.13+(levels[i]-first)/Math.max(1,last-first)*.64};}
 q('#lf-kinship-label').textContent=data.length>6?'Nearby musical relatives':'Shared phrases';
}
const names=data.map(p=>p.title);
function tone(){const s=getComputedStyle(root);return {ink:s.getPropertyValue('--lf-ink').trim(),lower:s.getPropertyValue('--lf-lower').trim(),copper:s.getPropertyValue('--lf-copper').trim(),tenor:s.getPropertyValue('--lf-tenor').trim(),paper:s.getPropertyValue('--lf-paper').trim()};}
// Resolve light-dark() through computed color before drawing into canvas.
const probe=document.createElement('span');probe.style.cssText='position:absolute;width:0;height:0;visibility:hidden';root.appendChild(probe);
function color(v){probe.style.color=v;return getComputedStyle(probe).color;}
let palette={};function updatePalette(){const t=tone();Object.keys(t).forEach(k=>palette[k]=color(t[k]));}
function traceValue(index,hand,t){
 const events=tracks[index][hand],beat=t*data[index].beats;
 let i=0;while(i<events.length-1 && events[i+1].b<=beat)i++;
 const a=events[i],b=events[Math.min(i+1,events.length-1)];
 const f=b.b===a.b?0:Math.min(1,Math.max(0,(beat-a.b)/(b.b-a.b)));
 const eased=f*f*(3-2*f);return a.p+(b.p-a.p)*eased;
}
function modelPoint(index,hand,t,thread){
 const pitch=traceValue(index,hand,t),[base,radialShift,depthShift]=voiceLayouts[trackKinds[index][hand]];
 const theta=-2.68+t*5.15;
 const radial=133+(pitch-base)*2.5*state.relief+radialShift+thread*2.25;
 // Musical time folds around an open arc. Pitch and hand separate the lines in depth.
 const x=Math.cos(theta)*radial*1.4+Math.sin(t*Math.PI*2)*13;
 const y=-(Math.sin(theta)*radial*.72+(t-.5)*47+(pitch-base)*.8);
 const z=(pitch-base)*4.3*state.relief+depthShift+thread*1.65*Math.sin(theta*1.5)+12*Math.sin(t*Math.PI*2);
 return [x,y,z];
}
function project(p,cx,cy,scale){
 const [x,y,z]=p,m=matrix;
 const rx=m[0]*x+m[1]*y+m[2]*z,ry=m[3]*x+m[4]*y+m[5]*z,rz=m[6]*x+m[7]*y+m[8]*z;
 const perspective=1000/(1000-rz);
 return [cx+rx*scale*perspective,cy-ry*scale*perspective,rz,perspective];
}
function point(index,hand,t,thread,cx,cy,scale){return project(modelPoint(index,hand,t,thread),cx,cy,scale);}
function rebuildGeometry(){
 radius=1;geometry.clear();
 // The norm is convex along each thread offset: the two outside threads
 // bound every inner thread. Compute their radius without storing the catalogue.
 data.forEach((_,index)=>{for(let hand=0;hand<tracks[index].length;hand++)for(const thread of [-Math.floor(state.density/2),Math.floor(state.density/2)])for(let i=0;i<=240;i++)radius=Math.max(radius,Math.hypot(...modelPoint(index,hand,i/240,thread)));});
 radius/=Math.sqrt(1-(radius/1000)**2);
}
function geometryFor(index){
 if(!geometry.has(index)){
  const curves=[];
  for(let hand=tracks[index].length-1;hand>=0;hand--)for(let thread=-Math.floor(state.density/2);thread<=Math.floor(state.density/2);thread++){
   const points=[];
   for(let i=0;i<=240;i++)points.push(modelPoint(index,hand,i/240,thread));
   curves.push({hand,thread,points});
  }
  geometry.set(index,curves);if(geometry.size>12)geometry.delete(geometry.keys().next().value);
 }
 return geometry.get(index);
}
function strokePath(index,hand,thread,cx,cy,scale,t0=0,t1=1){
 ctx.beginPath();const samples=Math.max(16,Math.round((t1-t0)*350));
 for(let j=0;j<=samples;j++){const t=t0+(t1-t0)*j/samples,p=point(index,hand,t,thread,cx,cy,scale);j?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]);}
 ctx.stroke();
}
function active(index,hand,seconds){return tracks[index][hand].find(e=>e.s<=seconds && seconds<e.e);}
function drawWork(index,cx,cy,scale,opacity){
 const chosen=index===state.selected;
 ctx.save();ctx.globalAlpha=opacity;
 const segments=[];
 for(const curve of geometryFor(index)){
  const pts=curve.points.map(p=>project(p,cx,cy,scale));
  for(let start=0;start<240;start+=30){
   const points=pts.slice(start,start+31),depth=points.reduce((sum,p)=>sum+p[2],0)/points.length;
   segments.push({points,depth,hand:curve.hand,thread:curve.thread});
  }
 }
 segments.sort((a,b)=>a.depth-b.depth);
 for(const segment of segments){
  ctx.strokeStyle=palette[voicePaletteKeys[trackKinds[index][segment.hand]]];
  ctx.lineWidth=segment.thread===0?1.05:.65;
  ctx.globalAlpha=opacity*(segment.thread===0?.82:.43)*(.76+.24*Math.max(-1,Math.min(1,segment.depth/180)));
  ctx.beginPath();segment.points.forEach((p,j)=>j?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));ctx.stroke();
 }
 if(state.kinship && zoom>.85){
  const motif=data[index].motif,hand=trackKinds[index].indexOf(motif.voice||(motif.hand==='lh'?'bass':'upper')),from=motif.start_beat/data[index].beats,to=motif.end_beat/data[index].beats;
  ctx.strokeStyle=palette.copper;ctx.globalAlpha=1;ctx.lineWidth=2.2;strokePath(index,hand,0,cx,cy,scale,from,to);
  const midpoint=point(index,hand,(from+to)/2,0,cx,cy,scale);ctx.beginPath();ctx.arc(midpoint[0],midpoint[1],3,0,Math.PI*2);ctx.fillStyle=palette.copper;ctx.fill();
  ctx.fillStyle=chosen?palette.ink:palette.lower;ctx.globalAlpha=1;ctx.textAlign='center';ctx.font=(w<500?'14px':'18px')+' Georgia';
  if(w<500){names[index].split(' ').forEach((word,i)=>ctx.fillText(word,cx,cy+radius*scale+19+i*17));}else{ctx.fillText(names[index],cx,cy+radius*scale+25);}
  ctx.font='12px monospace';ctx.fillStyle=palette.copper;ctx.fillText(range[index][1],cx,cy+radius*scale+(w<500?55:44));
 }
 if(chosen && audio.currentTime>0 && audio.currentTime<data[index].performance){
  for(let hand=0;hand<tracks[index].length;hand++){
   const e=active(index,hand,audio.currentTime);if(!e)continue;
   const t=e.b/data[index].beats;const pt=point(index,hand,t,0,cx,cy,scale);
   ctx.globalAlpha=.12;ctx.fillStyle=palette.copper;ctx.beginPath();ctx.arc(pt[0],pt[1],13*pt[3],0,Math.PI*2);ctx.fill();
   ctx.globalAlpha=1;ctx.beginPath();ctx.arc(pt[0],pt[1],3.6*pt[3],0,Math.PI*2);ctx.fill();
  }
 }
 ctx.restore();
}
function renderField(){
 ctx.clearRect(0,0,w,h);
 const spacing=w<600?w*.99:w*.67;
 const center=w/2;
 const baseScale=Math.min(w*.43,h*.405)/radius;
 const familyRadius=Math.min(w/8,h*.082),familyScale=familyRadius/radius;
 if(zoom>.1){
  ctx.save();ctx.strokeStyle=palette.lower;ctx.globalAlpha=.35*zoom;ctx.lineWidth=.8;
  data.forEach((p,i)=>{if(!p.parent||!byOp.has(p.parent))return;const a=family[byOp.get(p.parent)],b=family[i];if(!a||!b)return;const ax=a.x*w,ay=a.y*h+familyRadius+(w<500?66:53),bx=b.x*w,by=b.y*h-familyRadius-7;ctx.beginPath();ctx.moveTo(ax,ay);ctx.bezierCurveTo(ax,(ay+by)/2,bx,(ay+by)/2,bx,by);ctx.stroke();});ctx.restore();
 }
 for(let i=0;i<data.length;i++){
  if(!family[i]&&zoom>.1)continue;
  const galleryX=center+(i-camera)*spacing;
  const node=family[i]||{x:.5,y:.46};
  let cx=galleryX+(node.x*w-galleryX)*zoom,cy=h*.46+(node.y*h-h*.46)*zoom;
  let scale=baseScale+(familyScale-baseScale)*zoom;
  const op=state.kinship?1:(i===state.selected?1:.13);
  if(cx+radius*scale>0&&cx-radius*scale<w)drawWork(i,cx,cy,scale,op);
 }
 if(zoom<.15){
  ctx.fillStyle=palette.lower;ctx.textAlign='center';ctx.font='11px monospace';ctx.globalAlpha=.85;
  ctx.fillText(String(state.selected+1).padStart(3,'0'),w/2,h-18);ctx.globalAlpha=1;
 }
}
function syncScore(){
 const ids=new Set(data[state.selected].events.filter(e=>e.s<=audio.currentTime&&audio.currentTime<e.e).map(e=>e.id));
 lastActive.forEach(el=>el.classList.remove('lf-now'));lastActive=[];
 if(state.score){ids.forEach(id=>{q('#lf-score-body').querySelectorAll('[id="'+id+'"],[data-event="'+id+'"]').forEach(el=>{el.classList.add('lf-now');lastActive.push(el);});});}
}
function animate(){
 frame=0;
 if(state.overview)return;
 const targetCamera=state.selected,targetZoom=state.kinship?1:0;
 if(reduced.matches){camera=targetCamera;zoom=targetZoom;}else{camera+=(targetCamera-camera)*.13;zoom+=(targetZoom-zoom)*.13;}
 if(Math.abs(camera-targetCamera)<.001)camera=targetCamera;if(Math.abs(zoom-targetZoom)<.001)zoom=targetZoom;
 renderField();
 if(!audio.paused){updateClock();syncScore();}
 if(camera!==targetCamera || zoom!==targetZoom || !audio.paused)frame=requestAnimationFrame(animate);
}
function kick(){if(!frame)frame=requestAnimationFrame(animate);}
function resize(){const r=canvas.getBoundingClientRect();if(!r.width)return;w=r.width;h=r.height;const dpr=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);ctx.setTransform(dpr,0,0,dpr,0,0);updatePalette();kick();}
const scoreCache=new Map();let scoreRequest=0;
function formatTime(seconds){const n=Math.max(0,Math.floor(seconds||0));return Math.floor(n/60)+':'+String(n%60).padStart(2,'0');}
function trackLength(){return Number.isFinite(audio.duration)?audio.duration:data[state.selected].duration;}
function updateClock(){const duration=trackLength();q('#lf-time').textContent=formatTime(audio.currentTime)+' / '+formatTime(duration);q('#lf-progress').max=duration;q('#lf-progress').value=Math.min(audio.currentTime,duration);q('#lf-progress').setAttribute('aria-valuetext',formatTime(audio.currentTime)+' of '+formatTime(duration));}
function updateNavigation(){
 const order=state.playlist?listeningPath:data.map((_,i)=>i),position=order.indexOf(state.selected);
 q('#lf-prev').textContent=position>0?'← '+names[order[position-1]]:'Beginning';q('#lf-prev').disabled=position===0;
 q('#lf-next').textContent=position<order.length-1?names[order[position+1]]+' →':'End of collection';q('#lf-next').disabled=position===order.length-1;
 q('#lf-counter').textContent=String(position+1).padStart(2,'0')+' / '+String(order.length).padStart(2,'0');
 q('#lf-playlist-toggle').textContent=state.playlist?'End playlist':'Play collection';q('#lf-playlist-toggle').disabled=false;q('#lf-playlist-toggle').setAttribute('aria-pressed',String(state.playlist));
 q('#lf-path-status').textContent=state.playlist?`${audio.paused?'Paused':'Listening'} · ${position+1} of ${order.length} · ${names[state.selected]}`:`${listeningPath.length} pieces · ${formatTime(data.reduce((n,p)=>n+p.duration,0))} · Play once, from beginning to end.`;
 root.querySelectorAll('[data-path]').forEach(el=>el.setAttribute('aria-current',String(state.playlist&&Number(el.dataset.path)===position)));
}
async function playSelected(){
 const request=++playbackRequest;
 if(audio.ended||audio.currentTime>=trackLength()-.05)audio.currentTime=0;
 q('#lf-audio-error').hidden=true;
 try{await audio.play();if(state.overview)audio.pause();}catch(error){if(request===playbackRequest){q('#lf-audio-error').textContent='Playback could not start. Press Play to try this piece again.';q('#lf-audio-error').hidden=false;updateNavigation();}}
}
function followPath(position){
 if(position<0||position>=listeningPath.length)return;
 state.playlist=true;choose(listeningPath[position],true);playSelected();
}
function move(direction){
 const order=state.playlist?listeningPath:data.map((_,i)=>i),position=order.indexOf(state.selected)+direction;
 if(position<0||position>=order.length)return;
 const continuePlaying=state.playlist&&!audio.paused;
 choose(order[position],state.playlist);if(continuePlaying)playSelected();
}
async function showScore(){
 const request=++scoreRequest;
 q('#lf-field').hidden=state.score;q('#lf-title-section').hidden=state.score;q('#lf-score-shell').hidden=!state.score;
 q('#lf-score-toggle').textContent=state.score?'Return to field':'Open score';q('#lf-score-toggle').setAttribute('aria-pressed',String(state.score));q('#lf-kinship').hidden=state.score;
 if(state.score){
  const selected=state.selected,p=data[selected];q('#lf-score-title').textContent=p.title;q('#lf-score-opus').textContent='CWS Op. '+p.op;q('#lf-score-stamp').textContent=p.stamp;q('#lf-score-body').textContent='Loading score…';
  try{
   if(!scoreCache.has(p.op)){const pages=await Promise.all(p.scores.map(async url=>{const response=await fetch(url);if(!response.ok)throw new Error('Score unavailable');return response.text();}));scoreCache.set(p.op,pages);}
   if(request!==scoreRequest||!state.score||selected!==state.selected)return;
   q('#lf-score-body').replaceChildren();
   for(const text of scoreCache.get(p.op)){const doc=new DOMParser().parseFromString(text,'image/svg+xml');if(doc.querySelector('parsererror'))throw new Error('Invalid score');const page=document.createElement('div');page.className='lf-score-page';const svg=document.importNode(doc.documentElement,true);svg.setAttribute('role','img');svg.setAttribute('aria-label',p.title+' piano score');page.append(svg);q('#lf-score-body').append(page);}
   syncScore();
  }catch(error){if(request===scoreRequest)q('#lf-score-body').textContent='The score could not load. You can download its PDF below the player.';}
 }else{resize();}
}
function closeIndex(){q('#lf-index').hidden=true;q('#lf-index-toggle').setAttribute('aria-expanded','false');}
function showOverview(writeHistory=true){
 playbackRequest++;scoreRequest++;state.overview=true;state.playlist=false;state.score=false;state.kinship=false;
 q('#lf-kinship').setAttribute('aria-pressed','false');q('#lf-kinship-label').hidden=true;q('#lf-drag-label').hidden=false;q('#lf-field').classList.remove('is-family');
 audio.pause();lastActive.forEach(el=>el.classList.remove('lf-now'));lastActive=[];
 q('#lf-overview').hidden=false;q('#lf-piece').hidden=true;closeIndex();
 q('#lf-overview-link').setAttribute('aria-current','page');
 root.querySelectorAll('[data-work]').forEach(el=>el.setAttribute('aria-current','false'));
 document.title='The Listening Field · CWS First Studies';
 if(writeHistory&&location.hash!=='#overview')history.pushState(null,'','#overview');
 q('#lf-announcement').textContent='Collection overview · '+data.length+' piano studies';
 if(writeHistory)q('#lf-overview-title').focus({preventScroll:true});
}
function choose(index,keepPlaylist=false,writeHistory=true){
 if(index<0||index>=data.length)return;
 const fromOverview=state.overview;state.overview=false;
 q('#lf-overview').hidden=true;q('#lf-piece').hidden=false;q('#lf-overview-link').removeAttribute('aria-current');closeIndex();
 playbackRequest++;state.playlist=keepPlaylist;
 audio.pause();state.selected=index;audio.src=data[index].audio;q('#lf-play').textContent='Play';q('#lf-play').disabled=false;q('#lf-play').setAttribute('aria-label','Play '+names[index]);q('#lf-audio-error').hidden=true;
 refreshFamily();
 q('#lf-title').textContent=names[index];q('#lf-opus').textContent='CWS Op. '+data[index].op;q('#lf-stamp').textContent=data[index].stamp;
 q('#lf-inner-legend').hidden=!trackKinds[index].includes('inner');
 q('#lf-tenor-legend').hidden=!trackKinds[index].includes('tenor');
 updateNavigation();q('#lf-time').textContent='0:00 / '+formatTime(data[index].duration);q('#lf-progress').value=0;q('#lf-progress').max=data[index].duration;q('#lf-progress').setAttribute('aria-valuetext','0:00 of '+formatTime(data[index].duration));
 [['pdf','pdf'],['audio','audio'],['midi','midi'],['xml','xml']].forEach(([id,field])=>{q('#lf-download-'+id).href=data[index][field];});
 if(writeHistory&&location.hash.slice(1)!==data[index].slug)history[keepPlaylist&&!fromOverview?'replaceState':'pushState'](null,'','#'+data[index].slug);
 document.title=names[index]+' · CWS Op. '+data[index].op+' · The Listening Field';
 root.querySelectorAll('[data-work]').forEach(el=>el.setAttribute('aria-current',String(Number(el.dataset.work)===index)));
 q('#lf-announcement').textContent='Selected '+names[index]+', CWS Op. '+data[index].op;
 canvas.setAttribute('aria-label','Rotatable three-dimensional contours of the right-hand and left-hand notes of '+names[index]+'. Drag to rotate freely, or use the Turn, Tilt and Roll buttons.');
 if(state.score||fromOverview)showScore();
 if(fromOverview){q('#lf-title').setAttribute('tabindex','-1');q('#lf-title').focus({preventScroll:true});window.scrollTo({top:0,behavior:'instant'});resize();}
 kick();
}
q('#lf-play').addEventListener('click',()=>{
 if(audio.paused){playSelected();}else{playbackRequest++;audio.pause();}
});
audio.addEventListener('play',()=>{if(state.overview){audio.pause();return;}q('#lf-play').textContent='Pause';q('#lf-play').setAttribute('aria-label','Pause '+names[state.selected]);updateNavigation();kick();});
audio.addEventListener('pause',()=>{q('#lf-play').textContent='Play';q('#lf-play').setAttribute('aria-label','Play '+names[state.selected]);updateNavigation();});
audio.addEventListener('loadedmetadata',updateClock);
audio.addEventListener('error',()=>{if(state.overview)return;q('#lf-audio-error').textContent='The recording could not load. Select the piece again to retry, or skip to another piece.';q('#lf-audio-error').hidden=false;});
audio.addEventListener('ended',()=>{
 if(state.overview||!audio.ended)return;
 updateClock();lastActive.forEach(el=>el.classList.remove('lf-now'));lastActive=[];
 if(state.playlist){
  const next=listeningPath.indexOf(state.selected)+1;
  if(next<listeningPath.length){followPath(next);return;}
  state.playlist=false;updateNavigation();q('#lf-path-status').textContent='Walk complete · '+listeningPath.length+' pieces · Thank you for listening.';
 }
 q('#lf-play').textContent='Play';q('#lf-play').setAttribute('aria-label','Play '+names[state.selected]);kick();
});
q('#lf-playlist-toggle').addEventListener('click',()=>{
 if(state.playlist){playbackRequest++;state.playlist=false;audio.pause();updateNavigation();}else{followPath(0);}
});
q('#lf-path-summary').textContent='Explore the listening order · '+listeningPath.length+' works';
listeningPath.forEach((index,position)=>{
 const item=document.createElement('li'),button=document.createElement('button');button.type='button';button.dataset.path=position;button.textContent=names[index];button.setAttribute('aria-label','Play playlist from '+names[index]);button.addEventListener('click',()=>followPath(position));item.append(button);q('#lf-path-order').append(item);
});
q('#lf-progress').addEventListener('input',()=>{if(audio.readyState>0){audio.currentTime=Number(q('#lf-progress').value);updateClock();syncScore();kick();}});
q('#lf-score-toggle').addEventListener('click',()=>{state.score=!state.score;showScore();});
q('#lf-kinship').addEventListener('click',()=>{state.kinship=!state.kinship;q('#lf-kinship').setAttribute('aria-pressed',String(state.kinship));q('#lf-kinship-label').hidden=!state.kinship;q('#lf-drag-label').hidden=state.kinship;q('#lf-field').classList.toggle('is-family',state.kinship);resize();});
q('#lf-prev').addEventListener('click',()=>move(-1));q('#lf-next').addEventListener('click',()=>move(1));
q('#lf-index-toggle').addEventListener('click',()=>{const open=q('#lf-index').hidden;q('#lf-index').hidden=!open;q('#lf-index-toggle').setAttribute('aria-expanded',String(open));});
for(const id of ['lf-home','lf-overview-link'])q('#'+id).addEventListener('click',event=>{event.preventDefault();showOverview();window.scrollTo({top:0,behavior:'instant'});});
q('#lf-browse').addEventListener('click',()=>{q('#lf-index').hidden=false;q('#lf-index-toggle').setAttribute('aria-expanded','true');q('#lf-index-toggle').focus();q('#lf-index-toggle').scrollIntoView({block:'start'});});
q('#lf-begin').addEventListener('click',()=>{choose(byOp.get(2)??0);playSelected();});
q('#lf-overview-playlist').addEventListener('click',()=>followPath(0));
q('#lf-overview-family').addEventListener('click',()=>{choose(byOp.get(2)??0);state.kinship=true;q('#lf-kinship').setAttribute('aria-pressed','true');q('#lf-kinship-label').hidden=false;q('#lf-drag-label').hidden=true;q('#lf-field').classList.add('is-family');resize();q('#lf-piece').scrollIntoView({block:'start'});});
q('#lf-overview-latest').addEventListener('click',()=>{choose(data.length-1);q('#lf-piece').scrollIntoView({block:'start'});});
data.forEach((p,i)=>{
 const button=document.createElement('button');button.type='button';button.dataset.work=i;
 const op=document.createElement('span');op.textContent=String(p.op).padStart(2,'0');const title=document.createElement('span');title.className='lf-index-title';title.textContent=p.title;const duration=document.createElement('span');duration.textContent=formatTime(p.duration);
 button.append(op,title,duration);q('#lf-index').append(button);
});
q('#lf-work-count').textContent=String(data.length).padStart(2,'0')+' WORKS';
root.querySelectorAll('[data-work]').forEach(el=>el.addEventListener('click',()=>{choose(Number(el.dataset.work));q('#lf-index').hidden=true;q('#lf-index-toggle').setAttribute('aria-expanded','false');}));
function trackball(e){
 const rect=canvas.getBoundingClientRect(),r=Math.min(w,h)*.42;
 const x=(e.clientX-rect.left-w/2)/r,y=-(e.clientY-rect.top-h*.46)/r,d=x*x+y*y;
 return norm([x,y,d<=.5?Math.sqrt(1-d):.5/Math.sqrt(d)]);
}
function between(a,b){
 const cross=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],dot=a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
 if(dot<-.999999){const other=Math.abs(a[0])<.9?[1,0,0]:[0,1,0];return norm([a[1]*other[2]-a[2]*other[1],a[2]*other[0]-a[0]*other[2],a[0]*other[1]-a[1]*other[0],0]);}
 return norm([...cross,1+dot]);
}
canvas.addEventListener('pointerdown',e=>{if(drag||e.button!==0)return;drag={id:e.pointerId,point:trackball(e),x:e.clientX,y:e.clientY,moved:false};canvas.setPointerCapture(e.pointerId);});
canvas.addEventListener('pointermove',e=>{
 if(!drag||drag.id!==e.pointerId)return;
 if(Math.hypot(e.clientX-drag.x,e.clientY-drag.y)>4)drag.moved=true;
 const next=trackball(e);orientation=multiply(between(drag.point,next),orientation);drag.point=next;updateRotation();kick();
});
canvas.addEventListener('pointerup',e=>{
 if(!drag||drag.id!==e.pointerId)return;const click=!drag.moved;drag=null;canvas.releasePointerCapture(e.pointerId);
 if(click&&state.kinship){const rect=canvas.getBoundingClientRect(),x=e.clientX-rect.left,y=e.clientY-rect.top;let nearest=-1,best=Infinity;family.forEach((p,i)=>{if(!p)return;const distance=Math.hypot(x-p.x*w,y-p.y*h);if(distance<best){best=distance;nearest=i;}});if(best<Math.min(w/7,h*.13))choose(nearest);}
});
canvas.addEventListener('lostpointercapture',()=>drag=null);canvas.addEventListener('pointercancel',()=>drag=null);
root.querySelectorAll('[data-rotate]').forEach(button=>button.addEventListener('click',e=>{
 const axis=Number(button.dataset.rotate);orientation=multiply(axisTurn(axis,(e.shiftKey?-1:1)*Math.PI/6),orientation);updateRotation();kick();
 q('#lf-announcement').textContent=button.textContent+' rotated 30 degrees'+(e.shiftKey?' in reverse':'');
}));
new ResizeObserver(resize).observe(canvas);matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{updatePalette();kick();});
window.addEventListener('hashchange',()=>{const i=data.findIndex(p=>p.slug===location.hash.slice(1));if(i>=0){if(state.overview||i!==state.selected)choose(i,false,false);}else showOverview(false);});
const initial=data.findIndex(p=>p.slug===location.hash.slice(1));
prepareOverview();updateRotation();rebuildGeometry();if(initial>=0)choose(initial,false,false);else showOverview(false);resize();
})().catch(error=>{document.getElementById('lf-load-error').hidden=false;console.error(error);});
