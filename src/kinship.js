import {layoutKinship} from './kinship-layout.js';

export function mountKinship(root,data){
 const document=root.ownerDocument,q=selector=>root.querySelector(selector),svg=q('#kf-map');
 const layout=layoutKinship(data),byOp=new Map(data.map(p=>[p.op,p]));
 let portrait=svg.getBoundingClientRect().height>svg.getBoundingClientRect().width;
 const points=new Map(layout.nodes.map(p=>[p.op,portrait?{...p,x:p.y,y:p.x}:{...p}]));
 let baseWidth=portrait?780:1200,baseHeight=portrait?1200:780;
 const anchors=new Map(),edges=new Map(),svgNS='http://www.w3.org/2000/svg';
 const view={x:0,y:0,width:baseWidth,height:baseHeight};let selected=null,scale=1,suppressClick=false,drag=null,pinch=null,touchOpus=null;
 const pointers=new Map();
 function element(tag,attributes={},text){const node=document.createElementNS(svgNS,tag);for(const [key,value] of Object.entries(attributes))node.setAttribute(key,String(value));if(text!==undefined)node.textContent=text;return node;}
 function updateView(){
  view.x=Math.min(baseWidth-view.width,Math.max(0,view.x));view.y=Math.min(baseHeight-view.height,Math.max(0,view.y));
  svg.setAttribute('viewBox',`${view.x} ${view.y} ${view.width} ${view.height}`);svg.dataset.zoom=scale.toFixed(3);
  q('#kf-zoom-out').disabled=scale<=1;q('#kf-zoom-in').disabled=scale>=6;
 }
 function screenPoint(x,y){
  const rect=svg.getBoundingClientRect(),ratio=Math.min(rect.width/view.width,rect.height/view.height)||1;
  return {x:view.x+(x-rect.left-(rect.width-view.width*ratio)/2)/ratio,y:view.y+(y-rect.top-(rect.height-view.height*ratio)/2)/ratio,ratio};
 }
 function zoomTo(next,anchor={x:view.x+view.width/2,y:view.y+view.height/2}){
  next=Math.max(1,Math.min(6,next));const factor=scale/next;
  view.x=anchor.x-(anchor.x-view.x)*factor;view.y=anchor.y-(anchor.y-view.y)*factor;view.width*=factor;view.height*=factor;scale=next;updateView();
 }
 function fit(){scale=1;Object.assign(view,{x:0,y:0,width:baseWidth,height:baseHeight});updateView();q('#kf-status').textContent='All '+data.length+' works visible';}
 function select(op,focus=false){
  if(selected!==null){anchors.get(selected).classList.remove('is-current');anchors.get(selected).setAttribute('tabindex','-1');}
  selected=op;const piece=byOp.get(op),anchor=anchors.get(op),point=points.get(op);
  anchor.classList.add('is-current');anchor.setAttribute('tabindex','0');
  const lineage=new Set();let ancestor=piece;
  while(ancestor.parent!=null){lineage.add(ancestor.op);ancestor=byOp.get(ancestor.parent);}
  for(const [child,path] of edges)path.classList.toggle('is-lineage',lineage.has(child));
  const link=q('#kf-selected');link.replaceChildren();const number=document.createElement('span');number.textContent='CWS Op. '+piece.op;link.append(number,document.createTextNode(piece.title+' ↗'));link.setAttribute('href','index.html#'+piece.slug);link.hidden=false;
  if(focus){
   if(point.x<view.x+28||point.x>view.x+view.width-28||point.y<view.y+28||point.y>view.y+view.height-28){view.x=point.x-view.width/2;view.y=point.y-view.height/2;updateView();}
   anchor.focus({preventScroll:true});q('#kf-status').textContent='CWS Op. '+piece.op+', '+piece.title;
  }
 }
 for(const link of layout.links){
  const a=points.get(link.source),b=points.get(link.target),dx=b.x-a.x,dy=b.y-a.y;
  const path=element('path',{'data-parent':link.source,'data-child':link.target,d:`M${a.x},${a.y} Q${(a.x+b.x)/2-dy*.07},${(a.y+b.y)/2+dx*.07} ${b.x},${b.y}`});
  edges.set(link.target,path);q('#kf-connections').append(path);
 }
 for(const point of points.values()){
  const piece=byOp.get(point.op),parent=byOp.get(piece.parent),label='CWS Op. '+piece.op+', '+piece.title;
  const anchor=element('a',{href:'index.html#'+piece.slug,class:'kf-node','data-opus':piece.op,transform:`translate(${point.x},${point.y})`,tabindex:'-1','aria-label':label+(parent?'; musical parent: '+parent.title:'; origin of the collection')});
  anchor.append(element('title',{},label),element('circle',{class:'kf-hit',r:14}),element('circle',{class:'kf-point',r:piece.parent==null?5:3.6}),element('text',{class:'kf-number',x:8,y:-7},String(piece.op).padStart(3,'0')));
  anchor.addEventListener('pointerenter',event=>{if(event.pointerType!=='touch'&&!drag)select(piece.op);});anchor.addEventListener('focus',()=>select(piece.op));
  anchors.set(piece.op,anchor);q('#kf-works').append(anchor);
 }
 q('#kf-count').textContent=data.length+' works';q('#kf-range').textContent=String(data[0].op).padStart(3,'0')+' — '+String(data.at(-1).op).padStart(3,'0');
 q('#kf-zoom-in').addEventListener('click',()=>zoomTo(scale*1.4));q('#kf-zoom-out').addEventListener('click',()=>zoomTo(scale/1.4));q('#kf-fit').addEventListener('click',fit);
 svg.addEventListener('wheel',event=>{event.preventDefault();zoomTo(scale*Math.exp(-event.deltaY*.002),screenPoint(event.clientX,event.clientY));},{passive:false});
 svg.addEventListener('keydown',event=>{
  if(event.key==='+'||event.key==='='){event.preventDefault();zoomTo(scale*1.4);return;}
  if(event.key==='-'){event.preventDefault();zoomTo(scale/1.4);return;}
  if(event.key==='0'){event.preventDefault();fit();return;}
  const direction={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]}[event.key];if(!direction)return;
  event.preventDefault();const origin=points.get(selected);let nearest=null,best=Infinity;
  for(const point of points.values()){const dx=point.x-origin.x,dy=point.y-origin.y,forward=dx*direction[0]+dy*direction[1];if(forward<=.1)continue;const sideways=Math.abs(dx*direction[1]-dy*direction[0]),cost=Math.hypot(dx,dy)+sideways*2;if(cost<best){nearest=point;best=cost;}}
  if(nearest)select(nearest.op,true);
 });
 function gesture(){const [a,b]=[...pointers.values()];return {distance:Math.max(1,Math.hypot(b.x-a.x,b.y-a.y)),x:(a.x+b.x)/2,y:(a.y+b.y)/2};}
 svg.addEventListener('pointerdown',event=>{
  if(event.button!==0)return;pointers.set(event.pointerId,{x:event.clientX,y:event.clientY});
  const node=event.target.closest?.('[data-opus]');touchOpus=event.pointerType==='touch'&&node?Number(node.dataset.opus):null;
  if(pointers.size===1){drag={id:event.pointerId,x:event.clientX,y:event.clientY,moved:false};suppressClick=false;}
  else if(pointers.size===2){pinch=gesture();drag.moved=true;suppressClick=true;for(const id of pointers.keys())svg.setPointerCapture(id);}
 });
 svg.addEventListener('pointermove',event=>{
  if(!pointers.has(event.pointerId))return;pointers.set(event.pointerId,{x:event.clientX,y:event.clientY});
  if(pointers.size===2&&pinch){const next=gesture();zoomTo(scale*next.distance/pinch.distance,screenPoint(next.x,next.y));pinch=next;return;}
  if(!drag||drag.id!==event.pointerId)return;const dx=event.clientX-drag.x,dy=event.clientY-drag.y;
  if(!drag.moved&&Math.hypot(dx,dy)<=5)return;
  if(!drag.moved){drag.moved=true;svg.setPointerCapture(event.pointerId);}
  const ratio=screenPoint(event.clientX,event.clientY).ratio;view.x-=dx/ratio;view.y-=dy/ratio;drag.x=event.clientX;drag.y=event.clientY;suppressClick=true;svg.classList.add('is-dragging');updateView();
 });
 function endPointer(event){
  if(event.type==='pointercancel')touchOpus=null;
  if(!pointers.has(event.pointerId))return;pointers.delete(event.pointerId);
  if(svg.hasPointerCapture(event.pointerId))svg.releasePointerCapture(event.pointerId);
  if(pointers.size===1){const [id,p]=[...pointers.entries()][0];drag={id,x:p.x,y:p.y,moved:true};pinch=null;}
  else if(!pointers.size){drag=null;pinch=null;svg.classList.remove('is-dragging');}
 }
 svg.addEventListener('pointerup',endPointer);svg.addEventListener('pointercancel',endPointer);svg.addEventListener('lostpointercapture',endPointer);
 svg.addEventListener('click',event=>{
  if(suppressClick){event.preventDefault();event.stopPropagation();suppressClick=false;touchOpus=null;return;}
  const node=event.target.closest?.('[data-opus]');
  // Touch has no hover: reveal the title first, then open through its footer link.
  // Ordinary mouse clicks and keyboard activation remain direct opus links.
  if(node&&(event.pointerType==='touch'||touchOpus===Number(node.dataset.opus)&&event.detail!==0)){event.preventDefault();select(Number(node.dataset.opus));}
  touchOpus=null;
 },true);
 const Observer=document.defaultView.ResizeObserver;
 if(Observer)new Observer(()=>{
  const rect=svg.getBoundingClientRect(),next=rect.height>rect.width;if(next===portrait)return;
  portrait=next;baseWidth=portrait?780:1200;baseHeight=portrait?1200:780;
  for(const original of layout.nodes){const point=points.get(original.op);point.x=portrait?original.y:original.x;point.y=portrait?original.x:original.y;anchors.get(point.op).setAttribute('transform',`translate(${point.x},${point.y})`);}
  for(const {source,target} of layout.links){const a=points.get(source),b=points.get(target),dx=b.x-a.x,dy=b.y-a.y;edges.get(target).setAttribute('d',`M${a.x},${a.y} Q${(a.x+b.x)/2-dy*.07},${(a.y+b.y)/2+dx*.07} ${b.x},${b.y}`);}
  fit();
 }).observe(svg);
 fit();select(data[0].op);
}

export async function startKinship(document,fetcher=fetch){
 const root=document.getElementById('cws-kinship');
 try{const response=await fetcher('library.json');if(!response.ok)throw new Error('Catalogue unavailable');const data=await response.json();if(!data.length)throw new Error('Empty catalogue');mountKinship(root,data);}
 catch(error){root.querySelector('#kf-error').hidden=false;}
}
if(typeof document!=='undefined')startKinship(document);
