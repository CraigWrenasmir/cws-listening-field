// Fixed field order removes repeated JSON keys without rounding musical timing.
export const EVENT_FIELDS=['id','h','b','d','p','ps','s','e','v'];

// tuple-v2: [id,hand,beat,duration,pitches,start,end,voice?]. The ID may
// be [measure,index] when its exact spelling follows the catalogue convention.
// Hands use 0/1 for rh/lh; the upper pitch is derived from the unchanged array.
function decodeCompactEvent(row,opus){
 if(!Array.isArray(row)||(row.length!==7&&row.length!==8))throw new Error('Invalid catalogue event');
 const [encodedID,hand,b,d,ps,s,e]=row;
 if(hand!==0&&hand!==1)throw new Error('Invalid catalogue hand');
 if(!Array.isArray(ps)||!ps.length||!ps.every(Number.isFinite))throw new Error('Invalid catalogue pitches');
 const h=hand===0?'rh':'lh';
 let id=encodedID;
 if(Array.isArray(encodedID)){
  if(!Number.isSafeInteger(opus)||opus<1||encodedID.length!==2||
    !encodedID.every(Number.isSafeInteger)||encodedID[0]<1||encodedID[1]<0)throw new Error('Invalid catalogue event ID');
  id=`cws${opus}-${h}-m${encodedID[0]}-n${encodedID[1]}`;
 }else if(typeof id!=='string')throw new Error('Invalid catalogue event ID');
 return {id,h,b,d,p:Math.max(...ps),ps,s,e,...(row.length===8?{v:row[7]}:{})};
}

export function decodeLibrary(data){
 if(!Array.isArray(data))throw new Error('Invalid catalogue');
 return data.map(piece=>{
  if(piece.event_format===undefined)return piece;
  if(piece.event_format!=='tuple-v1'&&piece.event_format!=='tuple-v2')throw new Error('Unsupported catalogue event format');
  if(!Array.isArray(piece.events))throw new Error('Invalid catalogue events');
  const {event_format,...rest}=piece;
  return {...rest,events:piece.events.map(row=>{
   if(event_format==='tuple-v2')return decodeCompactEvent(row,piece.op);
   if(!Array.isArray(row)||(row.length!==8&&row.length!==9))throw new Error('Invalid catalogue event');
   return Object.fromEntries(row.map((value,index)=>[EVENT_FIELDS[index],value]));
  })};
 });
}
