// Hands: two wooden hands play a study, drawn as an engraved plate. The
// fingering and motion come from the Mechanical Pianist's planner, run in a
// worker on the study's own MIDI; the hands are a Blender model built to the
// planner's hand measurements; the plate is drawn from the scene each frame.
import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {DRACOLoader} from 'three/addons/loaders/DRACOLoader.js';
import {decodeLibrary} from './library-format.js';

const q=s=>document.querySelector(s);
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
 stop();study=piece;data=null;
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
const renderer=new THREE.WebGLRenderer({canvas:cv,antialias:false,alpha:false});
renderer.outputColorSpace=THREE.LinearSRGBColorSpace;
const scene=new THREE.Scene();
const camera=new THREE.PerspectiveCamera(30,16/9,0.05,5);
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
function buildKeys(){
 if(keyGroup)scene.remove(keyGroup);
 keyGroup=new THREE.Group();keyMeshes=new Map();
 for(const k of data.keyboard){const m=new THREE.Mesh(oldKey(k),k.black?KEY_BLACK:KEY_WHITE);m.position.set(k.x,0,PIVOT_Z);keyGroup.add(m);keyMeshes.set(k.midi,m);}
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
function makeTargets(){
 const dpr=Math.min(2,window.devicePixelRatio||1);
 W=Math.max(2,Math.round(cv.clientWidth*dpr));H=Math.max(2,Math.round(cv.clientWidth*9/16*dpr));
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
 if(!data||!rigs.R)return;
 const f=frameAt(t);
 rigs.R.apply(f.R);rigs.L.apply(f.L);
 const dip=new Map();for(let i=0;i<f.dips.length;i+=2)dip.set(f.dips[i]+21,f.dips[i+1]);
 const sounding=new Map();for(const n of data.notes)if(n.start<=t&&t<n.keyEnd)sounding.set(n.midi,n);
 for(const [midi,m] of keyMeshes){const d=Math.max(dip.get(midi)||0,m.geometry.userData.restDip);m.rotation.x=-d*KEY_DIP/(-PIVOT_Z);const n=sounding.get(midi);m.material=n?(n.motif?KEY_MOTIF:KEY_PRESS):(m.geometry.userData.black?KEY_BLACK:KEY_WHITE);}
 const cx=(f.L.wrist[0]+f.R.wrist[0])/2,spread=Math.abs(f.L.wrist[0]-f.R.wrist[0]);
 const want=new THREE.Vector3(cx,0.50+spread*0.35,0.40+spread*0.3),wantAt=new THREE.Vector3(cx,0,0);
 const ease=reducedMotion?1:0.03;camPos.lerp(want,ease);camTarget.lerp(wantAt,ease);
 camera.position.copy(camPos);camera.lookAt(camTarget);camera.aspect=16/9;camera.updateProjectionMatrix();
 scene.overrideMaterial=null;renderer.setRenderTarget(colorRT);renderer.setClearColor(0xffffff,1);renderer.render(scene,camera);
 scene.overrideMaterial=normalMat;renderer.setRenderTarget(normalRT);renderer.render(scene,camera);scene.overrideMaterial=null;
 const u=plateMat.uniforms;u.tColor.value=colorRT.texture;u.tNormal.value=normalRT.texture;u.tDepth.value=colorRT.depthTexture;
 u.res.value.set(W,H);u.paper.value=cssColor('--hf-paper');u.ink.value=cssColor('--hf-ink');u.copper.value=cssColor('--hf-copper');
 u.mode.value={plate:0,wash:1,timber:2}[q('#hf-look').value];
 renderer.setRenderTarget(null);renderer.render(quadScene,quadCam);
 q('#hf-time').textContent=`${fmt(t)} / ${fmt(data.duration)}`;
 q('#hf-progress').value=Math.round(1000*t/data.duration);
 q('#hf-progress').setAttribute('aria-valuetext',fmt(t)+' of '+fmt(data.duration));
}

// ---------- transport
function loop(now){
 if(playing&&data){if(audio&&!audio.paused&&isFinite(audio.currentTime))t=audio.currentTime;else t+=((now-lastWall)/1000)*speed;if(t>=data.duration){t=data.duration;stop();}}
 lastWall=now;draw();requestAnimationFrame(loop);
}
function start(){if(!data)return;playing=true;lastWall=performance.now();q('#hf-play').textContent='Pause';if(audio){audio.currentTime=t;audio.playbackRate=speed;audio.play().catch(()=>{});}}
function stop(){playing=false;if(data)q('#hf-play').textContent='Play';if(audio)audio.pause();}
q('#hf-play').addEventListener('click',()=>playing?stop():start());
q('#hf-restart').addEventListener('click',()=>{t=0;if(audio)audio.currentTime=0;});
q('#hf-progress').addEventListener('input',e=>{if(!data)return;t=(e.target.value/1000)*data.duration;if(audio)audio.currentTime=t;});
q('#hf-speed').addEventListener('change',e=>{speed=+e.target.value;if(audio)audio.playbackRate=speed;});
q('#hf-pick').addEventListener('change',e=>load(+e.target.value));
window.addEventListener('resize',makeTargets);
document.addEventListener('keydown',e=>{if(!data||e.target.tagName==='SELECT'||e.target.tagName==='INPUT')return;if(e.code==='Space'){e.preventDefault();playing?stop():start();}if(e.key==='ArrowRight')t=Math.min(data.duration,t+(e.shiftKey?1:1/30));if(e.key==='ArrowLeft')t=Math.max(0,t-(e.shiftKey?1:1/30));});
window.addEventListener('hashchange',()=>{const p=library.find(x=>x.slug===location.hash.slice(1));if(p&&p!==study)load(p.op,false);});

(async()=>{
 try{
  const [catalogue,handSpec,gltf]=await Promise.all([
   fetch('library.json').then(r=>r.json()).then(decodeLibrary),
   fetch('src/hands/hand_spec.json').then(r=>r.json()),
   (()=>{const loader=new GLTFLoader();const draco=new DRACOLoader();draco.setDecoderPath('https://unpkg.com/three@0.186.1/examples/jsm/libs/draco/');loader.setDRACOLoader(draco);return loader.loadAsync('src/hands/wooden_hand.glb?v=1');})(),
  ]);
  library=catalogue;spec=handSpec;
  const sel=q('#hf-pick');
  for(const p of library){const o=document.createElement('option');o.value=p.op;o.textContent=`Op. ${p.op} · ${p.title}`;sel.appendChild(o);}
  gltf.scene.traverse(o=>{if(o.isMesh)o.material.side=THREE.FrontSide;});
  rigs.R=new Rig(gltf.scene,'R');rigs.L=new Rig(gltf.scene,'L');
  makeTargets();
  const params=new URLSearchParams(location.search);
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
