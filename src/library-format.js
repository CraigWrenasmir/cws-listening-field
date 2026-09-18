// Fixed field order removes repeated JSON keys without rounding musical timing.
export const EVENT_FIELDS=['id','h','b','d','p','ps','s','e','v'];
export function decodeLibrary(data){
 if(!Array.isArray(data))throw new Error('Invalid catalogue');
 return data.map(piece=>{
  if(piece.event_format===undefined)return piece;
  if(piece.event_format!=='tuple-v1')throw new Error('Unsupported catalogue event format');
  const {event_format,...rest}=piece;
  return {...rest,events:piece.events.map(row=>{
   if(!Array.isArray(row)||(row.length!==8&&row.length!==9))throw new Error('Invalid catalogue event');
   return Object.fromEntries(row.map((value,index)=>[EVENT_FIELDS[index],value]));
  })};
 });
}
