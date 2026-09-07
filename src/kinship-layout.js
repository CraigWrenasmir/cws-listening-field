// Stable, deterministic tree layout. Links come only from catalogue ancestry.
// A relaxed radial tree keeps the long chains apart without hiding short branches.
export function layoutKinship(data){
 const nodes=data.map(p=>({op:p.op,parent:p.parent,x:0,y:0,vx:0,vy:0,children:[]}));
 const byOp=new Map(nodes.map(p=>[p.op,p]));
 if(byOp.size!==nodes.length)throw new Error('Duplicate opus');
 const links=[];
 for(const node of nodes){if(node.parent!=null){const parent=byOp.get(node.parent);if(!parent)throw new Error('Missing musical parent');parent.children.push(node);links.push({source:parent,target:node});}}
 const roots=nodes.filter(p=>p.parent==null),seen=new Set();let leaf=0;
 function plant(node,depth){
  if(seen.has(node.op))throw new Error('Cyclic musical ancestry');seen.add(node.op);node.depth=depth;
  node.children.sort((a,b)=>a.op-b.op).forEach(child=>plant(child,depth+1));
  node.slot=node.children.length?node.children.reduce((sum,p)=>sum+p.slot,0)/node.children.length:leaf++;
 }
 roots.forEach(root=>plant(root,0));if(seen.size!==nodes.length)throw new Error('Cyclic musical ancestry');
 for(const node of nodes){const angle=(node.slot+.5)/Math.max(1,leaf)*Math.PI*2;const radius=35+node.depth*36;node.x=Math.cos(angle)*radius;node.y=Math.sin(angle)*radius;}
 // Bounded relaxation, independent of viewport and animation timing.
 for(let step=0;step<480;step++){
  for(let i=0;i<nodes.length;i++)for(let j=i+1;j<nodes.length;j++){
   const a=nodes[i],b=nodes[j];let dx=a.x-b.x,dy=a.y-b.y;
   if(Math.abs(dx)+Math.abs(dy)<.001){dx=.1;dy=.1;}
   const distance=Math.hypot(dx,dy),force=Math.min(8,1100/(distance*distance));
   const fx=dx/distance*force,fy=dy/distance*force;a.vx+=fx;a.vy+=fy;b.vx-=fx;b.vy-=fy;
  }
  for(const {source:a,target:b} of links){const dx=b.x-a.x,dy=b.y-a.y,distance=Math.hypot(dx,dy)||1;const force=(distance-43)*.035;const fx=dx/distance*force,fy=dy/distance*force;a.vx+=fx;a.vy+=fy;b.vx-=fx;b.vy-=fy;}
  for(const node of nodes){node.vx=(node.vx-node.x*.0006)*.72;node.vy=(node.vy-node.y*.0006)*.72;node.x+=node.vx;node.y+=node.vy;}
 }
 const xs=nodes.map(p=>p.x),ys=nodes.map(p=>p.y),minX=Math.min(...xs),maxX=Math.max(...xs),minY=Math.min(...ys),maxY=Math.max(...ys);
 const scale=Math.min(1070/Math.max(1,maxX-minX),640/Math.max(1,maxY-minY));
 for(const node of nodes){node.x=600+(node.x-(minX+maxX)/2)*scale;node.y=390+(node.y-(minY+maxY)/2)*scale;}
 return {nodes:nodes.map(({op,parent,x,y})=>({op,parent,x,y})),links:links.map(({source,target})=>({source:source.op,target:target.op}))};
}
