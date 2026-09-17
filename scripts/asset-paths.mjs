import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const policy=JSON.parse(readFileSync(new URL('../data/asset_distribution.json',import.meta.url),'utf8'));
export const assetRanges=policy.ranges.map(r=>({...r,prefix:`https://raw.githubusercontent.com/${policy.repository}/${r.tag}/`}));
export const scoreEditions=(policy.volume_score_editions||[]).map(r=>({...r,prefix:`https://raw.githubusercontent.com/${policy.repository}/${r.tag}/`}));
for(let i=0;i<assetRanges.length;i++){const r=assetRanges[i];assert(Number.isInteger(r.first_opus)&&r.first_opus<=r.last_opus);assert(!i||assetRanges[i-1].last_opus<r.first_opus);assert(/^[a-z0-9-]+$/.test(r.tag));}
export const firstExternalOpus=assetRanges[0].first_opus;
export const assetPrefixes=[...new Set([...assetRanges,...scoreEditions].map(r=>r.prefix))];
export const isExternalAsset=url=>assetPrefixes.some(prefix=>url.startsWith(prefix));
function validateRelative(relative){assert(!relative.includes('..')&&!relative.startsWith('/')&&!relative.includes(':')&&!relative.includes('\\')&&!relative.includes('%'),'Unrecognised asset path: '+relative);assert(relative.startsWith('pieces/')||relative.startsWith('downloads/'),'Unexpected asset location: '+relative);return relative;}
export function publicAssetPath(relative){
 validateRelative(relative);
 if(relative.startsWith('downloads/')){const edition=scoreEditions.find(e=>e.path===relative);assert(edition,'Unknown score edition');return edition.prefix+relative;}
 const match=relative.match(/^pieces\/CWS_Op_(\d+)_/);assert(match,'Missing opus in piece path');
 const range=assetRanges.find(r=>r.first_opus<=Number(match[1])&&Number(match[1])<=r.last_opus);assert(range,'Configure an immutable asset range for opus '+match[1]);
 return range.prefix+relative;
}
export function localAssetPath(url){
 const prefix=assetPrefixes.find(prefix=>url.startsWith(prefix));
 const relative=validateRelative(prefix?url.slice(prefix.length):url);
 if(prefix)assert.equal(url,publicAssetPath(relative),'Asset belongs to a different immutable edition');
 return relative;
}
