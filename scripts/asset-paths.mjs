import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const policy=JSON.parse(readFileSync(new URL('../data/asset_distribution.json',import.meta.url),'utf8'));
export const firstExternalOpus=policy.first_external_opus;
export const assetTag=policy.tag;
export const assetPrefix=`https://raw.githubusercontent.com/${policy.repository}/${policy.tag}/`;
export function localAssetPath(url){
 const relative=url.startsWith(assetPrefix)?url.slice(assetPrefix.length):url;
 assert(!relative.includes('..')&&!relative.startsWith('/')&&!relative.includes(':'),'Unrecognised asset URL: '+url);
 assert(relative.startsWith('pieces/')||relative.startsWith('downloads/'),'Unexpected asset location: '+url);
 return relative;
}
export function publicAssetPath(relative){localAssetPath(relative);return assetPrefix+relative;}
