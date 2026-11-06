// Hands: two wooden hands play a study, drawn as an engraved plate. The
// fingering and motion come from the Mechanical Pianist's planner, run in a
// worker on the study's own MIDI; the hands are a Blender model built to the
// planner's hand measurements; the plate is drawn from the scene each frame.
import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {DRACOLoader} from 'three/addons/loaders/DRACOLoader.js';
import {decodeLibrary} from './library-format.js';
import * as LIVE from './hands/live.js?v=1';

const q=s=>document.querySelector(s);
const PAGE=document.querySelector('#cws-hands').dataset.page||'hands';
const PITCH=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
const WHITE_PITCH=0.0235,WHITE_GAP=0.0011,WHITE_LENGTH=0.15,WHITE_FRONT_HEIGHT=0.0215,BLACK_WIDTH=0.0128,BLACK_LENGTH=0.095,BLACK_HEIGHT=0.0122,KEY_DIP=0.010,PIVOT_Z=-0.255;
const probe=document.createElement('span');probe.style.display='none';q('#cws-hands').appendChild(probe); // inside the section that defines the palette
const cssColor=n=>{probe.style.color=`var(${n})`;return new THREE.Color(getComputedStyle(probe).color);};
const fmt=s=>{s=Math.max(0,s|0);return `${Math.floor(s/60)}:${String(s%60).padStart(2,'0')}`;};
const reducedMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;

// ---------- library and planning
let library=[],study=null,data=null,spec=null,audio=null;
let playing=false,t=0,lastWall=0,speed=1,loadToken=0;
const planned=new Map();
let worker=null;
function planStudy(piece){
 if(planned.has(piece.op))return planned.get(piece.op);
 const job=(async()=>{
  const response=await fetch(piece.midi);if(!response.ok)throw new Error('MIDI unavailable');
  const bytes=await response.arrayBuffer();
  if(!worker)worker=new Worker('src/hands/planner.js?v=1',{type:'module'});
  return new Promise((resolve,reject)=>{
   const onMessage=e=>{
    if(e.data.progress!==undefined){status(`${e.data.label}… ${Math.round(e.data.progress*100)}%`);return;}
    worker.removeEventListener('message',onMessage);
    if(e.data.ok)resolve(e.data.result);else reject(new Error(e.data.error));
   };
   worker.addEventListener('message',onMessage);
   worker.postMessage({bytes,name:piece.slug+'.mid'},[bytes]);
  });
 })();
 planned.set(piece.op,job);job.catch(()=>planned.delete(piece.op));
 return job;
}
function status(text){q('#hf-status').textContent=text;}

async function load(op,writeHistory=true){
 const piece=library.find(p=>p.op===op);if(!piece)return;
 const token=++loadToken;
 stop();study=piece;data=null;replaying=false;root.classList.remove('is-replay');q('#hf-sound').querySelector('[value=recording]').disabled=false;if(q('#hf-sound').value==='recording')q('#hf-sound').value='recording';
 q('#hf-opus').textContent='CWS Op. '+piece.op+' · '+(piece.series_label||'First Studies');
 q('#hf-name').textContent=piece.title;
 q('#hf-stamp').textContent=piece.stamp;
 q('#hf-pick').value=piece.op;
 q('#hf-player').href='index.html#'+piece.slug;
 q('#hf-kin').textContent=piece.parent?`Motif ${piece.motif.pitches.join(' ')} (${piece.motif.hand==='rh'?'right':'left'} hand), inherited from Op. ${piece.parent}`:`Motif ${piece.motif.pitches.join(' ')} (${piece.motif.hand==='rh'?'right':'left'} hand), root of the line`;
 document.title=piece.title+' · Hands · The Listening Field';
 if(writeHistory&&location.hash.slice(1)!==piece.slug)history.pushState(null,'','#'+piece.slug);
 q('#hf-play').disabled=true;q('#hf-play').textContent='Planning…';q('#hf-time').textContent='0:00 / '+fmt(piece.duration);
 status('Reading the score and choosing hands and fingers…');
 if(audio)audio.pause();audio=new Audio(piece.audio);audio.preload='auto';
 try{
  const result=await planStudy(piece);
  if(token!==loadToken)return;
  data=result;markMotif();buildKeys();t=0;
  status(`${data.notes.length} notes · fingered and planned in your browser in ${(data.planningMs/1000).toFixed(1)} s`);
  q('#hf-play').disabled=false;q('#hf-play').textContent='Play';
 }catch(err){
  if(token!==loadToken)return;
  status('');q('#hf-error').textContent='The hands could not plan this study: '+err.message;q('#hf-error').hidden=false;
 }
}
function markMotif(){
 const hand=study.motif.hand==='rh'?'R':'L';
 const seq=study.motif.pitches.map(p=>PITCH.indexOf(p.replace('b','#')));
 const notes=data.notes.filter(n=>n.hand===hand).sort((a,b)=>a.start-b.start||a.midi-b.midi);
 for(const n of data.notes)n.motif=false;
 const onsets=[];
 for(const n of notes){const o=onsets[onsets.length-1];if(o&&Math.abs(o.start-n.start)<0.02){if(n.midi>o.midi)onsets[onsets.length-1]=n;}else onsets.push(n);}
 for(let i=0;i+seq.length<=onsets.length;i++)if(seq.every((pc,k)=>onsets[i+k].midi%12===pc)){for(let k=0;k<seq.length;k++)onsets[i+k].motif=true;i+=seq.length-1;}
}

// ---------- scene
const cv=q('#hf-stage');
THREE.ColorManagement.enabled=false;
const renderer=new THREE.WebGLRenderer({canvas:cv,antialias:false,alpha:false,preserveDrawingBuffer:true}); // so a still can be read back after a draw
renderer.outputColorSpace=THREE.LinearSRGBColorSpace;
const scene=new THREE.Scene();
const ASPECT=14/5;
const camera=new THREE.PerspectiveCamera(19,ASPECT,0.05,5);
scene.add(new THREE.HemisphereLight(0xffffff,0x777766,1.2));
const keyLight=new THREE.DirectionalLight(0xffffff,2.2);keyLight.position.set(-0.6,1.0,0.5);scene.add(keyLight);
const fillLight=new THREE.DirectionalLight(0xffffff,0.5);fillLight.position.set(0.5,0.4,-0.3);scene.add(fillLight);

// the old piano: every key worn by its own history, the same every visit
let keyGroup=null,keyMeshes=new Map();
const KEY_WHITE=new THREE.MeshStandardMaterial({color:0xe4ddc8,roughness:0.75});
const KEY_BLACK=new THREE.MeshStandardMaterial({color:0x2a2a2e,roughness:0.5});
const KEY_PRESS=new THREE.MeshStandardMaterial({color:0x0000ff,roughness:0.6});
const KEY_MOTIF=new THREE.MeshStandardMaterial({color:0xff0000,roughness:0.6});
function rng(seed){let a=seed*2654435761>>>0;return()=>{a=(a+0x6D2B79F5)>>>0;let x=a;x=Math.imul(x^(x>>>15),x|1);x^=x+Math.imul(x^(x>>>7),x|61);return((x^(x>>>14))>>>0)/4294967296;};}
function oldKey(k){
 const r=rng(k.midi+1),black=k.black;
 const w=black?BLACK_WIDTH:WHITE_PITCH-WHITE_GAP,h=black?BLACK_HEIGHT+0.004:WHITE_FRONT_HEIGHT,L=black?BLACK_LENGTH:WHITE_LENGTH;
 const g=new THREE.BoxGeometry(w,h,L,4,2,black?10:16);
 const top=black?h-0.002:0,zFront=black?-WHITE_LENGTH+BLACK_LENGTH:0;
 g.translate(0,black?BLACK_HEIGHT/2-0.002:-h/2,(black?-WHITE_LENGTH+BLACK_LENGTH/2:-L/2)-PIVOT_Z);
 const pos=g.attributes.position,v=new THREE.Vector3();
 const chips=[];
 const nFront=black?(r()<0.55?1:0)+(r()<0.3?1:0):(r()<0.38?1:0)+(r()<0.12?1:0);
 for(let i=0;i<nFront;i++)chips.push({x:(i===0?(r()<0.5?-1:1):(chips[0].x>0?-1:1))*w/2,z:zFront-PIVOT_Z,rad:(black?0.004:0.005)+r()*0.008,depth:0.003+r()*0.006});
 if(r()<(black?0.35:0.15))chips.push({x:(r()<0.5?-1:1)*w/2,z:zFront-PIVOT_Z-(0.02+r()*(black?0.06:0.09)),rad:0.003+r()*0.006,depth:0.002+r()*0.004});
 if(black&&r()<0.25)chips.push({x:0,z:zFront-PIVOT_Z,rad:0.006+r()*0.006,depth:0.004+r()*0.005});
 const capLoss=black?r()*0.0035:0,lean=black?(r()-0.5)*0.08:(r()-0.5)*0.02;
 const hollow=black?0.0008+r()*0.0012:0.0012+r()*0.0014,n1=r()*100,n2=r()*100,grainAmp=black?0.00035:0.0005;
 for(let i=0;i<pos.count;i++){
  v.fromBufferAttribute(pos,i);
  const onTop=Math.abs(v.y-top)<1e-4;
  if(onTop){
   const zz=v.z+PIVOT_Z,u=Math.max(0,Math.min(1,(zz-(zFront-0.06))/0.06));
   v.y-=hollow*u*(1-Math.pow(Math.abs(v.x)/(w/2),2));
   v.y+=grainAmp*Math.sin(v.x*900+n1)*Math.cos(zz*350+n2)+grainAmp*0.6*Math.sin(zz*1300+n2*3);
   if(black){v.y-=capLoss;const front=Math.max(0,1-(zFront-zz)/0.02);v.y-=0.0025*front*front;}
  }
  if(black&&!onTop&&v.y>top-0.012)v.y-=capLoss;
  for(const c of chips){const dz=Math.hypot(v.x-c.x,v.z-c.z);if(dz<c.rad&&v.y>top-0.012){const tt=1-dz/c.rad;v.y-=c.depth*tt;v.x-=Math.sign(c.x||1)*c.rad*0.35*tt;}}
  pos.setXYZ(i,v.x,v.y,v.z);
 }
 pos.needsUpdate=true;g.computeVertexNormals();
 g.rotateY((r()-0.5)*(black?0.03:0.012));g.rotateZ(lean);
 g.userData.restDip=r()<(black?0.45:0.35)?r()*(black?0.3:0.22):0;
 g.userData.black=black;
 return g;
}
let keysBuilt=false;
function buildKeys(keyboard=data.keyboard){
 if(keyGroup)scene.remove(keyGroup);
 keyGroup=new THREE.Group();keyMeshes=new Map();keysBuilt=true;
 for(const k of keyboard){const m=new THREE.Mesh(oldKey(k),k.black?KEY_BLACK:KEY_WHITE);m.position.set(k.x,0,PIVOT_Z);keyGroup.add(m);keyMeshes.set(k.midi,m);}
 const CASE=new THREE.MeshStandardMaterial({color:0xd8d2c4,roughness:0.7});
 const fb=new THREE.Mesh(new THREE.BoxGeometry(1.4,0.05,0.03),CASE);fb.position.set(0,0.012,-WHITE_LENGTH-0.015);keyGroup.add(fb);
 const slip=new THREE.Mesh(new THREE.BoxGeometry(1.4,0.012,0.012),CASE);slip.position.set(0,-WHITE_FRONT_HEIGHT-0.006,0);keyGroup.add(slip);
 const bed=new THREE.Mesh(new THREE.BoxGeometry(1.4,0.01,0.5),CASE);bed.position.set(0,-WHITE_FRONT_HEIGHT-0.012,0.1);keyGroup.add(bed);
 scene.add(keyGroup);
}

// the hands: the model once, cloned, the left mirrored; posed as the planner's rig poses them
const m4=new THREE.Matrix4();
const setRot=(o,m)=>{m4.set(m[0],m[1],m[2],0,m[3],m[4],m[5],0,m[6],m[7],m[8],0,0,0,0,1);o.quaternion.setFromRotationMatrix(m4);};
const mul=(a,b)=>{const o=new Array(9);for(let r=0;r<3;r++)for(let c=0;c<3;c++)o[r*3+c]=a[r*3]*b[c]+a[r*3+1]*b[3+c]+a[r*3+2]*b[6+c];return o;};
const rotX=a=>{const c=Math.cos(a),s=Math.sin(a);return[1,0,0,0,c,-s,0,s,c];};
const rotY=a=>{const c=Math.cos(a),s=Math.sin(a);return[c,0,s,0,1,0,-s,0,c];};
const rotZ=a=>{const c=Math.cos(a),s=Math.sin(a);return[c,-s,0,s,c,0,0,0,1];};
const flex=a=>rotX(-a);
const rigs={};
class Rig{
 constructor(template,hand){
  this.root=template.clone(true);this.root.name=hand;this.node={};
  this.root.traverse(o=>{if(o.name)this.node[o.name]=o;});
  const h=this.node.Hand;if(h&&h!==this.root){h.position.set(0,0,0);h.quaternion.identity();}
  this.root.scale.set(hand==='R'?1:-1,1,1);
  this.qa=new THREE.Quaternion();this.qb=new THREE.Quaternion();
  scene.add(this.root);
 }
 apply(h){
  const p=h.pose;this.root.position.set(h.wrist[0],h.wrist[1],h.wrist[2]);
  setRot(this.node.Palm,p.rot);setRot(this.node.Forearm,p.fa);
  this.qa.copy(this.node.Forearm.quaternion);this.qb.copy(this.node.Palm.quaternion);
  this.node.WristRing2.quaternion.slerpQuaternions(this.qa,this.qb,0.33);
  this.node.WristRing1.quaternion.slerpQuaternions(this.qa,this.qb,0.66);
  this.node.WristCore.quaternion.slerpQuaternions(this.qa,this.qb,0.82);
  spec.fingers.forEach((f,i)=>{const s=p.f[i];setRot(this.node[`F${f.id}_0`],mul(rotY(f.baseYaw+s[0]),flex(s[1])));setRot(this.node[`F${f.id}_1`],flex(s[2]));setRot(this.node[`F${f.id}_2`],flex(s[3]));});
  const tb=mul(mul(rotY(spec.thumb.baseYaw),rotX(spec.thumb.basePitch)),rotZ(spec.thumb.opposition));
  setRot(this.node.T_0,mul(mul(mul(rotY(p.t[0]),tb),rotZ(p.t[1])),flex(p.t[2])));setRot(this.node.T_1,flex(p.t[3]));setRot(this.node.T_2,flex(p.t[4]));
 }
}

// ---------- the plate: edges from depth and normals, hatching from light
const normalMat=new THREE.MeshNormalMaterial();
let W=2,H=2,colorRT,normalRT;
function makeTargets(width,height){
 const dpr=Math.min(2,window.devicePixelRatio||1);
 W=width||Math.max(2,Math.round(cv.clientWidth*dpr));H=height||Math.max(2,Math.round(cv.clientWidth/ASPECT*dpr));
 renderer.setSize(W,H,false);
 colorRT?.dispose();normalRT?.dispose();
 colorRT=new THREE.WebGLRenderTarget(W,H,{depthTexture:new THREE.DepthTexture(W,H,THREE.UnsignedIntType)});
 normalRT=new THREE.WebGLRenderTarget(W,H);
}
const quadScene=new THREE.Scene(),quadCam=new THREE.OrthographicCamera(-1,1,1,-1,0,1);
const plateMat=new THREE.ShaderMaterial({
 uniforms:{tColor:{value:null},tNormal:{value:null},tDepth:{value:null},res:{value:new THREE.Vector2()},paper:{value:new THREE.Color()},ink:{value:new THREE.Color()},copper:{value:new THREE.Color()},near:{value:0.05},far:{value:5},mode:{value:0}},
 vertexShader:`varying vec2 vUv; void main(){ vUv = uv; gl_Position = vec4(position.xy, 0.0, 1.0); }`,
 fragmentShader:`
  precision highp float;
  varying vec2 vUv;
  uniform sampler2D tColor, tNormal, tDepth; uniform vec2 res; uniform vec3 paper, ink, copper; uniform float near, far; uniform int mode;
  float lin(float z){ float zn = 2.0 * z - 1.0; return 2.0 * near * far / (far + near - zn * (far - near)); }
  float depthAt(vec2 uv){ return lin(texture2D(tDepth, uv).x); }
  float lum(vec3 c){ return dot(c, vec3(0.299, 0.587, 0.114)); }
  void main(){
   vec2 px = 1.0 / res;
   vec4 col = texture2D(tColor, vUv);
   vec3 n = texture2D(tNormal, vUv).xyz * 2.0 - 1.0;
   float d = depthAt(vUv);
   float de = 0.0, ne = 0.0;
   for (int i = 0; i < 4; i++) {
    vec2 o = (i == 0) ? vec2(px.x, 0.0) : (i == 1) ? vec2(-px.x, 0.0) : (i == 2) ? vec2(0.0, px.y) : vec2(0.0, -px.y);
    float dd = depthAt(vUv + o);
    de += clamp(abs(dd - d) / max(d * 0.012, 0.002), 0.0, 1.0);
    vec3 nn = texture2D(tNormal, vUv + o).xyz * 2.0 - 1.0;
    ne += 1.0 - dot(n, nn);
   }
   float edge = clamp(de * 0.9 + ne * 1.4, 0.0, 1.0);
   bool background = d > far * 0.9;
   if (background) edge = 0.0;
   float L = lum(col.rgb);
   vec2 sp = gl_FragCoord.xy;
   float h1 = step(0.55, fract((sp.x + sp.y) / 7.0));
   float h2 = step(0.55, fract((sp.x - sp.y) / 7.0));
   float h3 = step(0.6, fract((sp.x * 0.5 + sp.y) / 9.0));
   float hatch = 0.0;
   if (L < 0.62) hatch = max(hatch, 1.0 - h1);
   if (L < 0.40) hatch = max(hatch, 1.0 - h2);
   if (L < 0.22) hatch = max(hatch, 1.0 - h3);
   if (background) hatch = 0.0;
   bool pressed = col.b > 0.6 && col.r < 0.25 && col.g < 0.25;
   bool motif = col.r > 0.6 && col.g < 0.25 && col.b < 0.25;
   vec3 tint = motif ? copper : ink;
   vec3 c = paper;
   if (mode == 2) { c = background ? paper : col.rgb; c = mix(c, ink, edge * 0.85); }
   else {
    float wash = (mode == 1 && !background) ? (1.0 - L) * 0.28 : 0.0;
    float hatchWeight = (mode == 1) ? 0.55 : 0.8;
    c = mix(c, tint, wash);
    c = mix(c, tint, hatch * hatchWeight * (motif ? 1.0 : 0.85));
    c = mix(c, tint, edge);
    if (pressed || motif) c = mix(c, tint, 0.35 + 0.35 * hatch);
   }
   gl_FragColor = vec4(c, 1.0);
  }`,
});
quadScene.add(new THREE.Mesh(new THREE.PlaneGeometry(2,2),plateMat));

const frameAt=t=>data.frames[Math.min(data.frames.length-1,Math.max(0,Math.round(t*data.rate)))];
const camTarget=new THREE.Vector3(0,0,0),camPos=new THREE.Vector3(0,0.5,0.4);
let needsDraw=true;
function draw(){
 if(!rigs.R||!keysBuilt)return;
 let f,sounding;
 if(free.on){f=live.frame();sounding=live.sounding;}
 else{if(!data)return;f=frameAt(t);sounding=new Map();for(const n of data.notes)if(n.start<=t&&t<n.keyEnd)sounding.set(n.midi,n);}
 rigs.R.apply(f.R);rigs.L.apply(f.L);
 const dip=new Map();for(let i=0;i<f.dips.length;i+=2)dip.set(f.dips[i]+21,f.dips[i+1]);
 for(const [midi,m] of keyMeshes){const d=Math.max(dip.get(midi)||0,m.geometry.userData.restDip);m.rotation.x=-d*KEY_DIP/(-PIVOT_Z);const n=sounding.get(midi);m.material=n?(n.motif?KEY_MOTIF:KEY_PRESS):(m.geometry.userData.black?KEY_BLACK:KEY_WHITE);}
 const cx=(f.L.wrist[0]+f.R.wrist[0])/2,spread=Math.abs(f.L.wrist[0]-f.R.wrist[0]);
 // the frame: the keyboard along the top edge, the wrists in the middle, the forearms leaving the bottom
 const want=new THREE.Vector3(cx,0.46+spread*0.3,0.40+spread*0.25),wantAt=new THREE.Vector3(cx,0.0,0.01);
 const ease=reducedMotion?1:0.03;camPos.lerp(want,ease);camTarget.lerp(wantAt,ease);
 camera.position.copy(camPos);camera.lookAt(camTarget);camera.aspect=ASPECT;camera.updateProjectionMatrix();
 scene.overrideMaterial=null;renderer.setRenderTarget(colorRT);renderer.setClearColor(0xffffff,1);renderer.render(scene,camera);
 scene.overrideMaterial=normalMat;renderer.setRenderTarget(normalRT);renderer.render(scene,camera);scene.overrideMaterial=null;
 const u=plateMat.uniforms;u.tColor.value=colorRT.texture;u.tNormal.value=normalRT.texture;u.tDepth.value=colorRT.depthTexture;
 u.res.value.set(W,H);u.paper.value=cssColor('--hf-paper');u.ink.value=cssColor('--hf-ink');u.copper.value=cssColor('--hf-copper');
 u.mode.value={plate:0,wash:1,timber:2}[q('#hf-look').value];
 renderer.setRenderTarget(null);renderer.render(quadScene,quadCam);
 if(!free.on&&data){
  q('#hf-time').textContent=`${fmt(t)} / ${fmt(data.duration)}`;
  q('#hf-progress').value=Math.round(1000*t/data.duration);
  q('#hf-progress').setAttribute('aria-valuetext',fmt(t)+' of '+fmt(data.duration));
 }
}

// ---------- transport
function loop(now){
 if(playing&&data&&!free.on){const prev=t;if(audio&&!audio.paused&&isFinite(audio.currentTime))t=audio.currentTime;else t+=((now-lastWall)/1000)*speed;if(replaying||soundIsSynth())piano.schedule(prev,t);if(t>=data.duration){t=data.duration;stop();}}
 lastWall=now;draw();requestAnimationFrame(loop);
}
function start(){if(!data||free.on)return;playing=true;lastWall=performance.now();q('#hf-play').textContent='Pause';if(replaying||soundIsSynth())piano.init();if(audio){audio.muted=soundIsSynth();audio.currentTime=t;audio.playbackRate=speed;audio.play().catch(()=>{});}}
function stop(){playing=false;if(data)q('#hf-play').textContent='Play';if(audio)audio.pause();piano.allOff();}
q('#hf-play').addEventListener('click',()=>playing?stop():start());
q('#hf-restart').addEventListener('click',()=>{t=0;if(audio)audio.currentTime=0;});
q('#hf-progress').addEventListener('input',e=>{if(!data)return;t=(e.target.value/1000)*data.duration;if(audio)audio.currentTime=t;});
q('#hf-speed').addEventListener('change',e=>{speed=+e.target.value;if(audio)audio.playbackRate=speed;});
q('#hf-pick').addEventListener('change',e=>load(+e.target.value));
window.addEventListener('resize',()=>{if(!exporting)makeTargets();});
document.addEventListener('keydown',e=>{if(e.target.tagName==='SELECT'||e.target.tagName==='INPUT'||e.target.tagName==='BUTTON'&&e.code!=='Space')return;if(free.on){freeKey(e,true);return;}if(!data)return;if(e.code==='Space'){e.preventDefault();playing?stop():start();}if(e.key==='ArrowRight')t=Math.min(data.duration,t+(e.shiftKey?1:1/30));if(e.key==='ArrowLeft')t=Math.max(0,t-(e.shiftKey?1:1/30));});
window.addEventListener('hashchange',()=>{const p=library.find(x=>x.slug===location.hash.slice(1));if(p&&p!==study)load(p.op,false);});

(async()=>{
 try{
  const [catalogue,handSpec,gltf]=await Promise.all([
   PAGE==='free'?Promise.resolve(null):fetch('library.json').then(r=>r.json()).then(decodeLibrary),
   fetch('src/hands/hand_spec.json').then(r=>r.json()),
   (()=>{const loader=new GLTFLoader();const draco=new DRACOLoader();draco.setDecoderPath('https://unpkg.com/three@0.186.1/examples/jsm/libs/draco/');loader.setDRACOLoader(draco);return loader.loadAsync('src/hands/wooden_hand.glb?v=1');})(),
  ]);
  library=catalogue||[];spec=handSpec;
  const sel=q('#hf-pick');
  for(const p of library){const o=document.createElement('option');o.value=p.op;o.textContent=`Op. ${p.op} · ${p.title}`;sel.appendChild(o);}
  gltf.scene.traverse(o=>{if(o.isMesh)o.material.side=THREE.FrontSide;});
  rigs.R=new Rig(gltf.scene,'R');rigs.L=new Rig(gltf.scene,'L');
  makeTargets();
  const params=new URLSearchParams(location.search);
  if(PAGE==='free'){setFree(true);requestAnimationFrame(loop);const shared=location.hash.match(/^#r=([A-Za-z0-9_-]+)$/);if(shared){try{showPerformance(unb64u(shared[1]),'shared.mid','Shared recording','A shared recording');}catch{status('That shared link could not be read.');}}return;}
  const fromHash=library.find(p=>p.slug===location.hash.slice(1));
  const op=fromHash?fromHash.op:+(params.get('op')||library[0].op);
  await load(op,false);
  if(params.has('t'))t=+params.get('t');
  if(params.has('look'))q('#hf-look').value=params.get('look');
  requestAnimationFrame(loop);
 }catch(err){
  q('#hf-error').textContent='The hands could not load: '+err.message;q('#hf-error').hidden=false;
 }
})();


// ====================================================================
// Free play: an on-screen keyboard, the computer keyboard or a MIDI
// keyboard drives the hands live. Fingering is chosen note by note (the
// planner's whole-piece solver cannot see the future here); the hands move
// as little as they can and keep their fingers in order. A recording can be
// saved as MIDI or handed to the planner for properly fingered hands.
// ====================================================================
const free={on:false};
let replaying=false;
const root=q('#cws-hands');
const KEY_BY_MIDI=new Map(LIVE.KEYS.map(k=>[k.midi,k]));

// ---------- the live hands
function newHand(h){return {h,sx:h==='R'?1:-1,x:h==='R'?0.16:-0.22,y:0.064,z:0.10,tx:h==='R'?0.16:-0.22,tz:0.10,fingers:[null,null,null,null,null,null],since:[0,0,0,0,0,0]};}
const I9=[1,0,0,0,1,0,0,0,1];
const rotXm=a=>{const c=Math.cos(a),s=Math.sin(a);return[1,0,0,0,c,-s,0,s,c];};
const rotYm=a=>{const c=Math.cos(a),s=Math.sin(a);return[c,0,s,0,1,0,-s,0,c];};
const mul3=(a,b)=>{const o=new Array(9);for(let r=0;r<3;r++)for(let c=0;c<3;c++)o[r*3+c]=a[r*3]*b[c]+a[r*3+1]*b[3+c]+a[r*3+2]*b[6+c];return o;};
const live={
 hands:{L:newHand('L'),R:newHand('R')},
 dips:new Map(),held:new Map(),sounding:new Map(),last:0,counter:0,
 contact(midi){const k=KEY_BY_MIDI.get(midi);const z=k.playZ;return {k,x:LIVE.contactX(k,z),z};},
 // which finger of this hand would take the key, and what it costs
 best(hand,midi){
  const {x:kx}=this.contact(midi);let best=null;
  for(let f=1;f<=5;f++){
   const tip=LIVE.REST_TIPS[f];const wx=kx-hand.sx*tip[0];
   let cost=Math.abs(wx-hand.x)+(hand.fingers[f]?0.08:0);
   for(let g=1;g<=5;g++){const m=hand.fingers[g];if(!m||g===f)continue;const gx=this.contact(m).x;
    const stretch=Math.abs((gx-wx)*hand.sx-LIVE.REST_TIPS[g][0]);if(stretch>0.02)cost+=(stretch-0.02)*3;
    if(((gx-kx)*hand.sx>0)!==(g>f))cost+=0.06; // keep the fingers in order along the keys
   }
   if(!best||cost<best.cost)best={f,wx,cost};
  }
  return best;
 },
 noteOn(midi,vel=0.7){
  if(!KEY_BY_MIDI.has(midi)||this.held.has(midi))return;
  const L=this.hands.L,R=this.hands.R,{x:kx}=this.contact(midi);
  const bl=this.best(L,midi),br=this.best(R,midi);
  let cl=bl.cost+(midi>=60?0.03:0)+(kx>R.x+0.02?0.25:0),cr=br.cost+(midi<60?0.03:0)+(kx<L.x-0.02?0.25:0);
  const hand=cl<=cr?L:R,b=cl<=cr?bl:br;
  if(hand.fingers[b.f]){this.noteOff(hand.fingers[b.f]);}
  hand.fingers[b.f]=midi;hand.since[b.f]=++this.counter;this.held.set(midi,{hand,f:b.f});
  this.sounding.set(midi,{motif:false});this.retarget(hand);
  piano.noteOn(midi,vel);rec.push('on',midi,vel);
 },
 noteOff(midi){
  const h=this.held.get(midi);if(!h)return;
  h.hand.fingers[h.f]=null;this.held.delete(midi);this.sounding.delete(midi);this.retarget(h.hand);
  piano.noteOff(midi);rec.push('off',midi,0);
 },
 allOff(){for(const midi of [...this.held.keys()])this.noteOff(midi);},
 retarget(hand){
  let n=0,sx=0,sz=0;
  for(let f=1;f<=5;f++){const m=hand.fingers[f];if(!m)continue;const c=this.contact(m);n++;sx+=c.x-hand.sx*LIVE.REST_TIPS[f][0];sz+=c.z-LIVE.REST_TIPS[f][2];}
  if(n){hand.tx=sx/n;hand.tz=Math.max(0.07,Math.min(0.125,sz/n));}
 },
 pose(hand,dt){
  const k=1-Math.exp(-dt/0.045);hand.x+=(hand.tx-hand.x)*k;hand.z+=(hand.tz-hand.z)*k;
  const fingers=[],out=[0,0,0];
  const target=(f)=>{const m=hand.fingers[f];const {k:key,x,z}=this.contact(m);const d=this.dips.get(m)?.v||0;LIVE.keySurfacePoint(key,z,d,out,x);return [(out[0]-hand.x)*hand.sx,out[1]+LIVE.TIP_RADIUS[f]-hand.y,out[2]-hand.z];};
  for(let f=2;f<=5;f++){
   if(hand.fingers[f]){const sol=LIVE.solveFinger(f-2,target(f));fingers.push([sol.abduction,sol.angles[0],sol.angles[1],sol.angles[2]]);}
   else{const r=LIVE.REST_FINGER_POSES[f-2];fingers.push([r.abduction,r.angles[0]*0.8,r.angles[1]*0.8,r.angles[2]*0.8]);}
  }
  let th;
  if(hand.fingers[1]){const sol=LIVE.solveThumb(target(1));th=[sol.swing,sol.twist,sol.angles[0],sol.angles[1],sol.angles[2]];}
  else{const r=LIVE.REST_THUMB_POSE;th=[r.swing,r.twist,r.angles[0],r.angles[1],r.angles[2]];}
  // the forearm points back toward an elbow that trails the hand, as the planner's does
  const ex=hand.sx*0.19+0.5*(hand.x-hand.sx*0.19),dx=hand.sx*(ex-hand.x),dy=0.02,dz=0.36-hand.z,l=Math.hypot(dx,dy,dz);
  const fa=mul3(rotYm(Math.atan2(dx/l,dz/l)),rotXm(-Math.asin(dy/l)));
  return {wrist:[hand.x,hand.y,hand.z],pose:{rot:rotXm(-0.06),fa,f:fingers,t:th}};
 },
 frame(){
  const now=performance.now()/1000,dt=Math.min(0.05,now-(this.last||now));this.last=now;
  for(const [midi,h] of this.held)if(!this.dips.has(midi))this.dips.set(midi,{v:0});
  const dips=[];
  for(const [midi,d] of this.dips){const want=this.held.has(midi)?1:0;const rate=want?dt/0.025:dt/0.085;d.v+=Math.max(-rate,Math.min(rate,want-d.v));if(d.v<=0.001&&!want){this.dips.delete(midi);continue;}dips.push(midi-21,d.v);}
  return {dips,L:this.pose(this.hands.L,dt),R:this.pose(this.hands.R,dt)};
 },
};

// ---------- the sound: several instruments, each a voice that can start and stop at any time on
// any audio context (live now, or offline for an export). The piano is the Mechanical Pianist's.
const INSTRUMENTS={piano:'Piano',epiano:'Electric piano',harpsichord:'Harpsichord',celesta:'Celesta',organ:'Organ',vibes:'Vibraphone'};
const pianoBuffers=new WeakMap(); // per audio context
function pianoBuffer(ctx,midi){let m=pianoBuffers.get(ctx);if(!m){m=new Map();pianoBuffers.set(ctx,m);}if(!m.has(midi))for(const [k,b] of LIVE.synthesizePiano(ctx,[midi]))m.set(k,b);return m.get(midi);}
function voice(ctx,dest,name,midi,vel,at){
 const f=440*Math.pow(2,(midi-69)/12),g=ctx.createGain();g.connect(dest);
 const nodes=[],osc=(type,freq,gain,detune=0)=>{const o=ctx.createOscillator();o.type=type;o.frequency.value=freq;o.detune.value=detune;const og=ctx.createGain();og.gain.value=gain;o.connect(og);og.connect(g);o.start(at);nodes.push(o);return og;};
 const amp=0.15+0.85*vel*vel;
 let release=0.25,sustained=false;
 const decay=(peak,tau,floor=0.0005)=>{g.gain.setValueAtTime(0.0001,at);g.gain.linearRampToValueAtTime(peak,at+0.004);g.gain.setTargetAtTime(floor,at+0.004,tau);};
 switch(name){
  case 'piano':{const src=ctx.createBufferSource();src.buffer=pianoBuffer(ctx,midi);src.connect(g);g.gain.value=amp;src.start(at);nodes.push(src);release=0.28;break;}
  case 'epiano':{osc('sine',f,0.7);osc('sine',f*2,0.25*(1-vel*0.4));osc('sine',f*3.01,0.06);osc('triangle',f,0.12,6);decay(amp*0.9,0.55+1.8*Math.max(0,(90-midi)/60));release=0.18;break;}
  case 'harpsichord':{const lp=ctx.createBiquadFilter();lp.type='lowpass';lp.frequency.value=Math.min(12000,f*9);lp.Q.value=0.7;const o=ctx.createOscillator();o.type='sawtooth';o.frequency.value=f;const o2=ctx.createOscillator();o2.type='square';o2.frequency.value=f;o2.detune.value=3;const og=ctx.createGain();og.gain.value=0.35;const og2=ctx.createGain();og2.gain.value=0.12;o.connect(og);o2.connect(og2);og.connect(lp);og2.connect(lp);lp.connect(g);o.start(at);o2.start(at);nodes.push(o,o2);lp.frequency.setValueAtTime(Math.min(14000,f*12),at);lp.frequency.exponentialRampToValueAtTime(Math.max(300,f*2.5),at+0.6);decay(0.5+0.3*vel,0.45+0.9*Math.max(0,(80-midi)/60));release=0.08;break;}
  case 'celesta':{osc('sine',f,0.8);osc('sine',f*2.76,0.18);osc('sine',f*5.4,0.05);decay(amp*0.9,0.5+1.2*Math.max(0,(96-midi)/60));release=0.3;break;}
  case 'organ':{osc('sine',f,0.5);osc('sine',f*2,0.3);osc('sine',f*3,0.14);osc('sine',f*4,0.08);osc('sine',f*0.5,0.18);g.gain.setValueAtTime(0.0001,at);g.gain.linearRampToValueAtTime(amp*0.5,at+0.03);sustained=true;release=0.09;break;}
  case 'vibes':{const og=osc('sine',f,0.8);osc('sine',f*4,0.08);const lfo=ctx.createOscillator();lfo.frequency.value=5.2;const lg=ctx.createGain();lg.gain.value=0.35;lfo.connect(lg);lg.connect(og.gain);lfo.start(at);nodes.push(lfo);decay(amp*0.9,1.1+2.0*Math.max(0,(96-midi)/60));release=0.35;break;}
 }
 let stopped=false;
 return {stop(when=ctx.currentTime){if(stopped)return;stopped=true;const t0=Math.max(when,at+0.01);g.gain.cancelScheduledValues(t0);g.gain.setValueAtTime(Math.max(0.0001,sustained?amp*0.5:0.5),t0);g.gain.setTargetAtTime(0.0001,t0,release/4);for(const n of nodes)n.stop(t0+release+0.05);},quick(when){if(stopped)return;stopped=true;g.gain.cancelScheduledValues(when);g.gain.setTargetAtTime(0.0001,when,0.01);for(const n of nodes)n.stop(when+0.06);}};
}
const piano={
 ctx:null,master:null,voices:new Map(),sustain:false,pending:new Set(),queue:[],inst:'piano',
 init(){
  if(this.ctx){if(this.ctx.state==='suspended')this.ctx.resume();return;}
  this.ctx=new (window.AudioContext||window.webkitAudioContext)();
  this.master=this.ctx.createGain();this.master.gain.value=0.8;this.master.connect(this.ctx.destination);
  // the piano's buffers: the middle of the keyboard first, a few notes at a time
  const order=[];for(let d=0;d<48;d++){if(60+d<=108)order.push(60+d);if(d&&60-d>=21)order.push(60-d);}
  this.queue=order;const step=()=>{if(!this.queue.length)return;for(const m of this.queue.splice(0,3))pianoBuffer(this.ctx,m);setTimeout(step,8);};step();
 },
 noteOn(midi,vel){this.init();if(!this.ctx)return;const old=this.voices.get(midi);if(old)old.quick(this.ctx.currentTime);this.voices.set(midi,voice(this.ctx,this.master,this.inst,midi,vel,this.ctx.currentTime));this.pending.delete(midi);},
 noteOff(midi){if(this.sustain){this.pending.add(midi);return;}this.kill(midi);},
 kill(midi){const v=this.voices.get(midi);if(!v)return;v.stop(this.ctx.currentTime);this.voices.delete(midi);},
 pedal(down){this.sustain=down;rec.push('pedal',64,down?1:0);if(!down){for(const m of this.pending)this.kill(m);this.pending.clear();}},
 allOff(){for(const m of [...this.voices.keys()])this.kill(m);this.pending.clear();},
 // the planned notes as the clock passes them (replays, opened files, and studies heard on another instrument)
 schedule(prev,now){if(!data)return;for(const n of data.notes){if(n.start>prev&&n.start<=now)this.noteOn(n.midi,n.velocity);if(n.end>prev&&n.end<=now)this.kill(n.midi);}},
 // the whole performance rendered offline, for an export
 async render(sampleRate=48000){
  const dur=data.duration+1.5,octx=new OfflineAudioContext(2,Math.ceil(dur*sampleRate),sampleRate);
  const master=octx.createGain();master.gain.value=0.8;master.connect(octx.destination);
  for(const n of data.notes)voice(octx,master,this.inst,n.midi,n.velocity,n.start).stop(n.end);
  return octx.startRendering();
 },
};
function soundIsSynth(){return q('#hf-sound').value!=='recording';}
function applySound(){
 const v=q('#hf-sound').value;
 if(v!=='recording'){piano.inst=v;q('#hf-inst').value=v;}
 if(audio)audio.muted=v!=='recording';
 if(playing&&!free.on){piano.allOff();}
}
q('#hf-sound').addEventListener('change',applySound);
q('#hf-inst').addEventListener('change',e=>{piano.inst=e.target.value;q('#hf-sound').value=e.target.value;piano.allOff();live.allOff();});

// ---------- recording, as a Standard MIDI File
const rec={
 active:false,t0:0,events:[],
 push(type,midi,v){if(!this.active)return;if(!this.events.length)this.t0=performance.now();this.events.push({t:(performance.now()-this.t0)/1000,type,midi,v});refreshRecording();},
 start(){this.active=true;this.events=[];this.t0=0;refreshRecording();},
 stop(){this.active=false;live.allOff();refreshRecording();},
 bytes(){
  const out=[],vlq=n=>{const b=[n&0x7f];while(n>>=7)b.unshift((n&0x7f)|0x80);return b;},str=s=>[...s].map(c=>c.charCodeAt(0));
  const track=[0,0xff,0x51,3,0x07,0xa1,0x20,0,0xc0,0]; // 120 bpm, piano
  let last=0;
  for(const e of this.events){const tick=Math.round(e.t*960);track.push(...vlq(Math.max(0,tick-last)));last=tick;
   if(e.type==='on')track.push(0x90,e.midi,Math.max(1,Math.round(e.v*127)));else if(e.type==='off')track.push(0x80,e.midi,64);else track.push(0xb0,64,e.v?127:0);}
  const end=(this.events.length?Math.round(this.events[this.events.length-1].t*960):0)+960;track.push(...vlq(end-last),0xff,0x2f,0);
  const be32=n=>[(n>>>24)&255,(n>>>16)&255,(n>>>8)&255,n&255];
  out.push(...str('MThd'),...be32(6),0,0,0,1,(480>>8)&255,480&255,...str('MTrk'),...be32(track.length),...track);
  return new Uint8Array(out);
 },
};
let downloadURL=null;
const b64u=bytes=>btoa(String.fromCharCode(...bytes)).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
const unb64u=str=>Uint8Array.from(atob(str.replace(/-/g,'+').replace(/_/g,'/')),c=>c.charCodeAt(0));
function refreshRecording(){
 const n=rec.events.filter(e=>e.type==='on').length;
 q('#hf-record').textContent=rec.active?`Stop (${n} notes)`:'Record';q('#hf-record').setAttribute('aria-pressed',String(rec.active));
 const have=!rec.active&&n>0;
 q('#hf-replay').disabled=!have;q('#hf-clear').disabled=!have&&!rec.active;
 const a=q('#hf-download');a.hidden=!have;q('#hf-share').hidden=!have;
 if(have){if(downloadURL)URL.revokeObjectURL(downloadURL);downloadURL=URL.createObjectURL(new Blob([rec.bytes()],{type:'audio/midi'}));a.href=downloadURL;}
}
q('#hf-record').addEventListener('click',()=>{piano.init();rec.active?rec.stop():rec.start();});
q('#hf-clear').addEventListener('click',()=>{rec.active=false;rec.events=[];refreshRecording();});
async function planBytes(bytes,name){
 if(!worker)worker=new Worker('src/hands/planner.js?v=1',{type:'module'});
 return new Promise((resolve,reject)=>{const onMessage=e=>{if(e.data.progress!==undefined){status(`${e.data.label}… ${Math.round(e.data.progress*100)}%`);return;}worker.removeEventListener('message',onMessage);e.data.ok?resolve(e.data.result):reject(new Error(e.data.error));};worker.addEventListener('message',onMessage);const buf=bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength);worker.postMessage({bytes:buf,name},[buf]);});
}
// the hands play a performance that has no recording: a replay or an opened MIDI file
async function showPerformance(bytes,name,opus,title){
 setFree(false);
 const token=++loadToken;stop();study=null;data=null;replaying=true;root.classList.add('is-replay');
 const sel=q('#hf-sound');sel.querySelector('[value=recording]').disabled=true;if(sel.value==='recording')sel.value=piano.inst;applySound();
 q('#hf-opus').textContent=opus;q('#hf-name').textContent=title;q('#hf-stamp').textContent=new Date().toISOString().slice(0,19).replace(/[-:T]/g,'');
 q('#hf-kin').textContent='';document.title=title+' · Hands · The Listening Field';
 q('#hf-play').disabled=true;q('#hf-play').textContent='Planning…';status('Choosing hands and fingers…');q('#hf-error').hidden=true;
 if(audio)audio.pause();audio=null;
 try{
  const result=await planBytes(bytes,name);
  if(token!==loadToken)return;
  data=result;for(const n of data.notes)n.motif=false;buildKeys();t=0;
  status(`${data.notes.length} notes · fingered and planned in ${(data.planningMs/1000).toFixed(1)} s`+(data.warnings.length?` · ${data.warnings[0]}`:''));
  q('#hf-play').disabled=false;q('#hf-play').textContent='Play';q('#hf-time').textContent='0:00 / '+fmt(data.duration);
 }catch(err){if(token!==loadToken)return;status('');q('#hf-error').textContent='This could not be planned: '+err.message;q('#hf-error').hidden=false;}
}
q('#hf-replay').addEventListener('click',()=>showPerformance(rec.bytes(),'free-play.mid','Free play','Your recording'));
q('#hf-share').addEventListener('click',async()=>{
 const url=location.origin+location.pathname.replace(/[^/]*$/,'')+'freeplay.html#r='+b64u(rec.bytes());
 if(url.length>60000){status('This recording is too long to share as a link; download the MIDI instead.');return;}
 try{await navigator.clipboard.writeText(url);status('Link copied: anyone who opens it will see the hands play your recording.');}
 catch{history.replaceState(null,'','#r='+b64u(rec.bytes()));status('The address of this page now holds your recording: copy it from the address bar.');}
});

// ---------- opening a MIDI file: the button, or a file dropped on the stage
async function openFile(file){
 if(!file)return;
 const bytes=new Uint8Array(await file.arrayBuffer());
 const title=file.name.replace(/\.midi?$/i,'').replace(/[_-]+/g,' ');
 showPerformance(bytes,file.name,'Opened MIDI file',title);
}
q('#hf-file').addEventListener('change',e=>{openFile(e.target.files[0]);e.target.value='';});
for(const id of ['#hf-open','#hf-open2'])q(id).addEventListener('click',()=>q('#hf-file').click());
for(const ev of ['dragenter','dragover'])document.addEventListener(ev,e=>{if([...e.dataTransfer.types].includes('Files')){e.preventDefault();root.classList.add('is-dropping');}});
document.addEventListener('dragleave',e=>{if(!e.relatedTarget)root.classList.remove('is-dropping');});
document.addEventListener('drop',e=>{root.classList.remove('is-dropping');const f=[...e.dataTransfer.files].find(f=>/\.midi?$/i.test(f.name));if(f){e.preventDefault();openFile(f);}});

// ---------- exporting an MP4: every frame drawn at its exact time and encoded in the browser,
// with the recording or the chosen instrument as the soundtrack
let exporting=false;
async function exportVideo(){
 if(!data||exporting)return;
 if(!('VideoEncoder' in window)||!('AudioEncoder' in window)){status('Exporting video needs a browser with WebCodecs (Chrome or Edge).');return;}
 exporting=true;stop();const btn=q('#hf-export');btn.textContent='Cancel export';let wasT=t;
 let cancelled=false;const cancel=()=>{cancelled=true;};btn.removeEventListener('click',exportVideo);btn.addEventListener('click',cancel);
 const fps=30,Wv=1960,Hv=700,sr=48000;
 try{
  status('Preparing the soundtrack…');
  const {Muxer,ArrayBufferTarget}=await import('https://unpkg.com/mp4-muxer@5.2.1/build/mp4-muxer.mjs');
  // the soundtrack: the recording when there is one and it is chosen, otherwise the instrument
  let track;
  if(study&&!soundIsSynth()){
   const ab=await (await fetch(study.audio)).arrayBuffer();const dctx=new (window.AudioContext||window.webkitAudioContext)();const decoded=await dctx.decodeAudioData(ab);dctx.close();
   const octx=new OfflineAudioContext(2,Math.ceil((data.duration+1.5)*sr),sr);const src=octx.createBufferSource();src.buffer=decoded;src.connect(octx.destination);src.start(0);track=await octx.startRendering();
  }else track=await piano.render(sr);
  const totalFrames=Math.ceil(data.duration*fps),frameUs=1e6/fps;
  const audioCodec=(await AudioEncoder.isConfigSupported({codec:'mp4a.40.2',sampleRate:sr,numberOfChannels:2,bitrate:160000})).supported?'mp4a.40.2':'opus';
  const muxer=new Muxer({target:new ArrayBufferTarget(),video:{codec:'avc',width:Wv,height:Hv},audio:{codec:audioCodec==='opus'?'opus':'aac',sampleRate:sr,numberOfChannels:2},fastStart:'in-memory',firstTimestampBehavior:'offset'});
  const venc=new VideoEncoder({output:(c,m)=>muxer.addVideoChunk(c,m),error:e=>{throw e;}});
  const vcfg={codec:'avc1.640028',width:Wv,height:Hv,bitrate:9e6,framerate:fps};
  if(!(await VideoEncoder.isConfigSupported(vcfg)).supported)vcfg.codec='avc1.4d0028';
  venc.configure(vcfg);
  const aenc=new AudioEncoder({output:(c,m)=>muxer.addAudioChunk(c,m),error:e=>{throw e;}});
  aenc.configure({codec:audioCodec,sampleRate:sr,numberOfChannels:2,bitrate:160000});
  // audio in 1024-frame pieces, planar
  const L=track.getChannelData(0),R=track.getChannelData(1),N=Math.min(track.length,Math.ceil((data.duration+1)*sr));
  for(let i=0;i<N;i+=1024){const n=Math.min(1024,N-i);const buf=new Float32Array(n*2);buf.set(L.subarray(i,i+n),0);buf.set(R.subarray(i,i+n),n);aenc.encode(new AudioData({format:'f32-planar',sampleRate:sr,numberOfFrames:n,numberOfChannels:2,timestamp:Math.round(i/sr*1e6),data:buf}));}
  // video: the stage at export size, every frame at its exact time
  makeTargets(Wv,Hv);
  wasT=t;
  for(let i=0;i<totalFrames;i++){
   if(cancelled)throw new Error('cancelled');
   t=i/fps;draw();
   const frame=new VideoFrame(cv,{timestamp:Math.round(i*frameUs),duration:Math.round(frameUs)});
   venc.encode(frame,{keyFrame:i%(fps*5)===0});frame.close();
   if(i%10===0){status(`Exporting video… ${Math.round(100*i/totalFrames)}%`);while(venc.encodeQueueSize>8)await new Promise(r=>setTimeout(r,5));await new Promise(r=>setTimeout(r,0));}
  }
  status('Finishing the file…');await venc.flush();await aenc.flush();muxer.finalize();
  const blob=new Blob([muxer.target.buffer],{type:'video/mp4'});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=(study?study.slug:q('#hf-name').textContent.toLowerCase().replace(/[^a-z0-9]+/g,'-'))+'-hands.mp4';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),60000);
  status(`Exported ${totalFrames} frames at ${fps} fps, ${Wv}×${Hv}, ${(blob.size/1e6).toFixed(1)} MB`);
 }catch(err){status(err.message==='cancelled'?'Export cancelled.':'The export failed: '+err.message);}
 finally{t=wasT;exporting=false;makeTargets();btn.textContent='Export MP4';btn.removeEventListener('click',cancel);btn.addEventListener('click',exportVideo);draw();}
}
q('#hf-export').addEventListener('click',exportVideo);
function saveStill(){
 if(!rigs.R||!keysBuilt)return;
 const Wv=2800,Hv=1000;makeTargets(Wv,Hv);draw();
 cv.toBlob(blob=>{const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=(study?study.slug:q('#hf-name').textContent.toLowerCase().replace(/[^a-z0-9]+/g,'-'))+(free.on?'':'-'+fmt(t).replace(':','m')+'s')+'-plate.png';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),60000);makeTargets();draw();status(`Saved the plate at ${Wv}×${Hv}.`);},'image/png');
}
for(const id of ['#hf-still','#hf-still2'])q(id).addEventListener('click',saveStill);

// ---------- the on-screen keyboard and the computer keyboard
let base=48;const pointers=new Map();
function buildScreenKeys(){
 const el=q('#hf-keys');el.textContent='';
 const whites=[];for(let m=base;m<=base+36;m++)if(!KEY_BY_MIDI.get(m)?.black)whites.push(m);
 for(const m of whites){const d=document.createElement('div');d.className='hf-w';d.dataset.midi=m;if(m%12===0){const s=document.createElement('span');s.textContent=LIVE.noteName(m);d.appendChild(s);}el.appendChild(d);}
 for(let m=base;m<=base+36;m++){if(!KEY_BY_MIDI.get(m)?.black)continue;const idx=whites.filter(w=>w<m).length;const d=document.createElement('div');d.className='hf-b';d.dataset.midi=m;d.style.left=(idx/whites.length*100)+'%';el.appendChild(d);}
 q('#hf-oct').textContent=`${LIVE.noteName(base)} to ${LIVE.noteName(base+36)}`;
}
function screenDown(e,el){const m=+el.dataset.midi;if(pointers.get(e.pointerId)===m)return;screenUp(e);pointers.set(e.pointerId,m);el.classList.add('is-down');live.noteOn(m,0.72);}
function screenUp(e){const m=pointers.get(e.pointerId);if(m===undefined)return;pointers.delete(e.pointerId);q('#hf-keys').querySelector(`[data-midi="${m}"]`)?.classList.remove('is-down');live.noteOff(m);}
const keysEl=q('#hf-keys');
keysEl.addEventListener('pointerdown',e=>{const el=e.target.closest('[data-midi]');if(!el)return;e.preventDefault();piano.init();screenDown(e,el);});
keysEl.addEventListener('pointerover',e=>{if(!e.buttons)return;const el=e.target.closest('[data-midi]');if(el)screenDown(e,el);});
for(const ev of ['pointerup','pointercancel'])document.addEventListener(ev,screenUp);
keysEl.addEventListener('pointerleave',screenUp);
q('#hf-oct-down').addEventListener('click',()=>{base=Math.max(24,base-12);buildScreenKeys();});
q('#hf-oct-up').addEventListener('click',()=>{base=Math.min(72,base+12);buildScreenKeys();});
const KEYMAP={KeyA:0,KeyW:1,KeyS:2,KeyE:3,KeyD:4,KeyF:5,KeyT:6,KeyG:7,KeyY:8,KeyH:9,KeyU:10,KeyJ:11,KeyK:12,KeyO:13,KeyL:14,KeyP:15,Semicolon:16,Quote:17};
const typed=new Map();
function freeKey(e,down){
 if(e.repeat)return;
 if(e.code==='Space'){e.preventDefault();piano.pedal(down);return;}
 if(down&&e.code==='KeyZ'){base=Math.max(24,base-12);buildScreenKeys();return;}
 if(down&&e.code==='KeyX'){base=Math.min(72,base+12);buildScreenKeys();return;}
 if(!(e.code in KEYMAP))return;e.preventDefault();
 if(down){piano.init();const m=base+KEYMAP[e.code];typed.set(e.code,m);live.noteOn(m,0.72);q('#hf-keys').querySelector(`[data-midi="${m}"]`)?.classList.add('is-down');}
 else{const m=typed.get(e.code);if(m===undefined)return;typed.delete(e.code);live.noteOff(m);q('#hf-keys').querySelector(`[data-midi="${m}"]`)?.classList.remove('is-down');}
}
document.addEventListener('keyup',e=>{if(free.on)freeKey(e,false);});

// ---------- MIDI keyboards
let midiAccess=null;
async function openMIDI(){
 const el=q('#hf-midi');
 if(!navigator.requestMIDIAccess){el.textContent='MIDI keyboards: not supported by this browser (Chrome, Edge and Firefox can)';return;}
 try{midiAccess=midiAccess||await navigator.requestMIDIAccess();}catch{el.textContent='MIDI keyboards: access was refused';return;}
 const wire=()=>{const names=[];for(const input of midiAccess.inputs.values()){names.push(input.name);input.onmidimessage=m=>{const [st,d1,d2]=m.data;const kind=st&0xf0;if(kind===0x90&&d2>0)live.noteOn(d1,d2/127);else if(kind===0x80||kind===0x90)live.noteOff(d1);else if(kind===0xb0&&d1===64)piano.pedal(d2>=64);};}
  el.textContent=names.length?'MIDI: '+names.join(', '):'MIDI: no keyboard connected';};
 wire();midiAccess.onstatechange=wire;
}

// ---------- the mode
function setFree(on){
 if(on===free.on)return;
 if(on){stop();free.on=true;root.classList.add('is-free');q('#hf-playpanel').hidden=false;q('#hf-free').setAttribute('aria-pressed','true');if(PAGE==='free'){q('#hf-free').hidden=true;q('#hf-opus').textContent='The hands follow';q('#hf-name').textContent='Free play';document.title='Free play · The Listening Field';}
  q('#hf-play').disabled=true;q('#hf-play').textContent='Live';status('Free play: the hands follow whatever you play.');
  buildKeys(LIVE.KEYS);buildScreenKeys();refreshRecording();openMIDI();piano.inst=q('#hf-inst').value;piano.init();live.last=0;}
 else{live.allOff();if(rec.active)rec.stop();free.on=false;root.classList.remove('is-free');q('#hf-playpanel').hidden=true;q('#hf-free').setAttribute('aria-pressed','false');if(PAGE==='free')q('#hf-free').hidden=false;
  if(data){buildKeys();q('#hf-play').disabled=false;q('#hf-play').textContent='Play';status('');}else{q('#hf-play').textContent='Play';}}
}
q('#hf-free').addEventListener('click',()=>setFree(!free.on));
