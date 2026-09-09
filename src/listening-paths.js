// Every route is a deterministic permutation of the catalogue, not a filter.
export function buildListeningPaths(data){
 if(!data.length)throw new Error('Empty catalogue');
 const byOp=new Map(data.map((p,i)=>[p.op,i]));
 if(byOp.size!==data.length)throw new Error('Duplicate opus');
 const ordered=data.map((_,i)=>i).sort((a,b)=>data[a].op-data[b].op);
 const children=data.map(()=>[]),roots=[];
 for(const i of ordered){
  if(data[i].parent==null)roots.push(i);
  else{if(!byOp.has(data[i].parent))throw new Error('Missing musical parent');children[byOp.get(data[i].parent)].push(i);}
 }
 const branches=[],levels=[],seen=new Set();
 function visit(i,level){
  if(seen.has(i))throw new Error('Cyclic musical ancestry');
  seen.add(i);levels[i]=level;branches.push(i);[...children[i]].reverse().forEach(child=>visit(child,level+1));
 }
 roots.forEach(i=>visit(i,0));
 if(seen.size!==data.length)throw new Error('Cyclic musical ancestry');
 const generations=[...roots];
 for(let p=0;p<generations.length;p++)generations.push(...children[generations[p]]);

 // A virtual root also gives separate ancestry trees a finite distance.
 const adjacent=Array.from({length:data.length+1},()=>[]);
 ordered.forEach(i=>{
  const parent=data[i].parent==null?data.length:byOp.get(data[i].parent);
  adjacent[i].push(parent);adjacent[parent].push(i);
 });
 const distances=ordered.reduce((all,start)=>{
  const distance=Array(adjacent.length).fill(Infinity),queue=[start];distance[start]=0;
  for(let p=0;p<queue.length;p++)for(const next of adjacent[queue[p]])if(distance[next]===Infinity){distance[next]=distance[queue[p]]+1;queue.push(next);}
  all[start]=distance;return all;
 },[]);
 function walk(start,cost){
  const remaining=new Set(ordered),path=[start];remaining.delete(start);
  while(remaining.size){
   const current=path.at(-1);let next,best=Infinity;
   for(const candidate of remaining){const value=cost(current,candidate);if(value<best){best=value;next=candidate;}}
   path.push(next);remaining.delete(next);
  }
  return path;
 }
 const deepest=ordered.reduce((best,i)=>levels[i]>levels[best]?i:best,ordered[0]);
 const distant=walk(deepest,(a,b)=>-distances[a][b]);

 // Pitch distribution and sounded-note density are musical proxies, not
 // an assessment of mood or a promise that two recordings sound alike.
 const profiles=data.map(p=>{
  const pitches=p.events.flatMap(e=>e.ps),count=pitches.length||1;
  const mean=pitches.reduce((n,pitch)=>n+pitch,0)/count;
  const spread=Math.sqrt(pitches.reduce((n,pitch)=>n+(pitch-mean)**2,0)/count);
  const colour=Array(12).fill(0);pitches.forEach(pitch=>colour[pitch%12]++);
  const norm=Math.hypot(...colour)||1;
  return {mean,spread,colour:colour.map(n=>n/norm),density:Math.log2(1+p.note_onsets*60/Math.max(1,p.performance))};
 });
 const drift=walk(byOp.get(2)??ordered[0],(a,b)=>{
  const x=profiles[a],y=profiles[b];
  return ((x.mean-y.mean)/12)**2+.5*((x.spread-y.spread)/12)**2+(x.density-y.density)**2+.75*(1-x.colour.reduce((n,v,i)=>n+v*y.colour[i],0));
 });
 const editorial=[...new Set([1,3,2,4,5,...ordered.map(i=>data[i].op).filter(op=>op>=7),6].filter(op=>byOp.has(op)).map(op=>byOp.get(op)))];
 const routes=[
  {id:'branches',title:'Follow the branches',description:'Stay with each musical family, exploring newer branches before returning to older ones.',order:branches},
  {id:'generations',title:'Generations',description:'Hear the roots, then their children, then each succeeding generation across the family tree.',order:generations},
  {id:'distant',title:'Distant relations',description:'Begin deep in the tree, then leap to the most distant unheard relative at each turn.',order:distant},
  {id:'drift',title:'Gentle drift',description:'Begin with Velvet Estuary, then move between similar registers, note densities and pitch colours.',order:drift},
  {id:'light',title:'A walk towards light',description:'The original sequence, opening with Moss Atlas and closing in the warmth of Willow Transit.',order:editorial}
 ];
 for(const route of routes)if(route.order.length!==data.length||new Set(route.order).size!==data.length)throw new Error('Incomplete listening route');
 return routes;
}
