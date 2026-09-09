export const FAVOURITES_KEY='cws-listening-field:favourites:v1';
export const leafIcon='<svg class="cws-leaf" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 3C9 3 3 7 5 14c2 7 14 5 15-11Z"/><path d="M3 21 15 9"/></svg>';

export function createFavourites(win,data){
 const valid=new Set(data.map(p=>p.op)),listeners=new Set();let saved=new Set(),persistent=true;
 function read(){try{const raw=win.localStorage.getItem(FAVOURITES_KEY);let value;try{value=JSON.parse(raw??'[]');}catch{value=[];}saved=new Set(Array.isArray(value)?value.filter(n=>Number.isInteger(n)&&valid.has(n)):[]);persistent=true;}catch{persistent=false;}}
 function notify(){for(const fn of listeners)fn();}
 read();
 const onStorage=e=>{if(e.key===FAVOURITES_KEY||e.key===null){read();notify();}};
 win.addEventListener('storage',onStorage);
 return {has:op=>saved.has(op),get persistent(){return persistent;},
  toggle(op){if(!valid.has(op))return;if(persistent)read();saved.has(op)?saved.delete(op):saved.add(op);try{win.localStorage.setItem(FAVOURITES_KEY,JSON.stringify([...saved].sort((a,b)=>a-b)));persistent=true;}catch{persistent=false;}notify();},
  subscribe(fn){listeners.add(fn);return()=>listeners.delete(fn);},
  destroy(){win.removeEventListener('storage',onStorage);listeners.clear();}
 };
}
export function updateLeaf(button,piece,store){
 const saved=store.has(piece.op);button.innerHTML=leafIcon+'<span>'+(saved?'Saved':'Save')+'</span>';
 button.setAttribute('aria-pressed',String(saved));button.setAttribute('aria-label',(saved?'Remove ':'Save ')+piece.title+(saved?' from favourites':' to favourites'));button.title=button.getAttribute('aria-label');
}
export function mountFavourites(container,data,store,onChoose){
 const doc=container.ownerDocument,details=doc.createElement('details'),summary=doc.createElement('summary'),note=doc.createElement('p'),list=doc.createElement('ul'),empty=doc.createElement('p');
 details.className='cws-favourites';note.className='cws-saved-note';empty.textContent='Tap a leaf beside a piece to keep it here.';empty.className='cws-saved-empty';list.className='cws-saved-list';details.append(summary,note,empty,list);container.append(details);
 function render(){
  const pieces=data.filter(p=>store.has(p.op));summary.innerHTML=leafIcon+'Favourites <span class="cws-saved-count">'+pieces.length+'</span>';
  note.textContent=store.persistent?'Saved in this browser.':'Saved for this visit only. Browser storage is unavailable.';
  empty.hidden=pieces.length>0;list.replaceChildren();
  for(const p of pieces){const item=doc.createElement('li'),link=doc.createElement('a'),remove=doc.createElement('button');link.href='index.html#'+p.slug;link.textContent='Op. '+p.op+' · '+p.title;link.dataset.savedOp=p.op;if(onChoose)link.addEventListener('click',e=>{e.preventDefault();onChoose(p);});remove.type='button';remove.className='cws-leaf-button';updateLeaf(remove,p,store);remove.addEventListener('click',()=>{store.toggle(p.op);summary.focus();});item.append(link,remove);list.append(item);}
 }
 store.subscribe(render);render();return details;
}
