import assert from 'node:assert/strict';
import {parseHTML} from 'linkedom';
import {createFavourites,mountFavourites,FAVOURITES_KEY} from '../src/favourites.js';
const data=[{op:2,title:'Velvet Estuary',slug:'cws-op-002-velvet-estuary'},{op:170,title:'Camellia Threshold',slug:'cws-op-170-camellia-threshold'}];
const disk=new Map();let blocked=false;
function browser(){const {window,document}=parseHTML('<main></main>');Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:key=>{if(blocked)throw Error('Denied');return disk.get(key)??null;},setItem:(key,value)=>{if(blocked)throw Error('Quota');disk.set(key,value);}}});return {window,document};}
let {window,document}=browser();let store=createFavourites(window,data);assert(store.persistent);assert(!store.has(2));
store.toggle(2);assert.deepEqual(JSON.parse(disk.get(FAVOURITES_KEY)),[2]);
const reload=createFavourites(browser().window,data);assert(reload.has(2),'Saved work survives a fresh page');
store.toggle(170);assert.deepEqual(JSON.parse(disk.get(FAVOURITES_KEY)),[2,170]);
reload.toggle(2);assert.deepEqual(JSON.parse(disk.get(FAVOURITES_KEY)),[170],'A stale tab merges latest stored choices before toggling');
let notified=0;store.subscribe(()=>notified++);const event=new window.Event('storage');event.key=FAVOURITES_KEY;window.dispatchEvent(event);assert(!store.has(2)&&store.has(170));assert.equal(notified,1);
let chosen=null;const panel=mountFavourites(document.querySelector('main'),data,store,p=>chosen=p.op);assert(panel.querySelector('summary').textContent.includes('1'));assert(panel.querySelector('a').textContent.includes('Camellia'));panel.querySelector('a').click();assert.equal(chosen,170);
panel.querySelector('button').click();assert(!store.has(170));assert.deepEqual(JSON.parse(disk.get(FAVOURITES_KEY)),[]);assert(!panel.querySelector('.cws-saved-empty').hidden);assert.equal(panel.querySelectorAll('li').length,0);
disk.set(FAVOURITES_KEY,'broken json');assert(!createFavourites(browser().window,data).has(2));disk.set(FAVOURITES_KEY,JSON.stringify([2,2,'170',170,999,null,{}]));const clean=createFavourites(browser().window,data);assert(clean.has(2)&&clean.has(170));clean.toggle(170);assert.deepEqual(JSON.parse(disk.get(FAVOURITES_KEY)),[2]);
blocked=true;clean.toggle(170);assert(clean.has(2)&&clean.has(170));assert(!clean.persistent,'A write failure retains the choice for this visit');
({window,document}=browser());const temporary=createFavourites(window,data);assert(!temporary.persistent);temporary.toggle(2);assert(temporary.has(2));temporary.toggle(170);assert(temporary.has(2)&&temporary.has(170));const tempPanel=mountFavourites(document.querySelector('main'),data,temporary);assert(tempPanel.textContent.includes('this visit only'));temporary.toggle(2);assert(!temporary.has(2)&&temporary.has(170));
blocked=false;disk.clear();window.dispatchEvent(Object.assign(new window.Event('storage'),{key:null}));assert(!temporary.has(170),'Clearing browser storage updates saved state');
console.log('Favourites passed: persistence, removal, stale-tab merge, storage events/clear, malformed data, valid IDs, denied storage, quota fallback and saved-list navigation.');
