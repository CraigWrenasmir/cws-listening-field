"""Publish catalogue metadata and downloadable collections from checked piece assets."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET,argparse
from pypdf import PdfReader
from collection_volumes import build_volumes
ROOT=Path(__file__).resolve().parents[1]
cat=json.loads((ROOT/'data/catalog.json').read_text())
parser=argparse.ArgumentParser();parser.add_argument('--opus',type=int,nargs='+');args=parser.parse_args()
legacy={1:dict(parent_opus=None,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['D','F','E','A'])),2:dict(parent_opus=1,motif=dict(hand='lh',start_beat=0,end_beat=3,pitches=['D','F','E','A'])),3:dict(parent_opus=1,motif=dict(hand='rh',start_beat=48,end_beat=52,pitches=['A','C','B','E']))}
manifest=[]
for p in cat:
 parent=p.get('parent_opus',legacy.get(p['op'],{}).get('parent_opus'))
 motif=p.get('motif',legacy.get(p['op'],{}).get('motif'))
 folder=ROOT/'pieces'/p['folder'];stem=p['stem'];prefix=f'pieces/{p["folder"]}/{stem}'
 assert all((folder/(stem+ext)).is_file() for ext in ['.pdf','.mp3','.mid','.musicxml'])
 pages=len(PdfReader(folder/(stem+'.pdf')).pages)
 scores=[f'{prefix}_page_{i}.svg' for i in range(1,pages+1)]
 assert all((ROOT/s).is_file() for s in scores)
 # music21 does not propagate a Chord object's id to its individual MusicXML
 # notes. Give the corresponding engraved chord group the event id so every
 # pitch in the final dyad follows the same performance highlight.
 if args.opus is None or p['op'] in args.opus:
  parsed=[ET.parse(ROOT/s) for s in scores]
  chord_groups=[g for tree in parsed for g in tree.getroot().iter() if g.get('class')=='chord']
  if p['op']<7:
   chord_events=sorted([e for e in p['events'] if len(e['pitches'])>1],key=lambda e:(e['bar'],0 if e['hand']=='rh' else 1,e['offset']))
   assert len(chord_groups)==len(chord_events),'Explicit chord mapping required'
   for g,e in zip(chord_groups,chord_events):g.set('id',e['id'])
  else:
   event_ids={e['id'] for e in p['events']};assigned=set()
   for tree in parsed:
    for g in tree.getroot().iter():
     if g.get('class') not in ('note','chord'):continue
     source_id=g.get('id','')
     if g.get('class')=='chord':
      members=[n.get('id','') for n in g.iter() if n.get('class')=='note']
      source_id=members[0] if members else source_id
     match=re.match(r'(cws\d+-(?:rh|lh)-m\d+-n\d+)',source_id)
     if match and match[1] in event_ids:
      event_id=match[1];g.set('data-event',event_id)
      if event_id not in assigned:
       g.set('id',event_id);assigned.add(event_id)
   assert assigned==event_ids,('Unmapped score events',p['op'],event_ids-assigned)
  for tree,s in zip(parsed,scores):
   text=ET.tostring(tree.getroot(),encoding='unicode')
   text=re.sub(r'@font-face\s*\{[^}]*\}','',text)
   (ROOT/s).write_text(text)
 entry=dict(op=p['op'],title=p['title'],slug=f'cws-op-{p["op"]:03d}-'+p['title'].lower().replace(' ','-'),stamp=p['composition_stamp'],beats=p['bars']*p['beats_per_bar'],duration=p['duration_seconds'],performance=p['performance_seconds'],audio=prefix+'.mp3',pdf=prefix+'.pdf',midi=prefix+'.mid',xml=prefix+'.musicxml',scores=scores,parent=parent,motif=motif,note_onsets=p['note_onsets'],pages=pages,
  events=[dict(id=e['id'],h=e['hand'],b=e['offset'],d=e['duration'],p=max(e['pitches']),ps=e['pitches'],s=e['seconds'],e=e['end_seconds']) for e in p['events']])
 manifest.append(entry)
(ROOT/'library.json').write_text(json.dumps(manifest,separators=(',',':'))+'\n')
volumes=build_volumes(ROOT,cat,args.opus)
readme=ROOT/'README.md'
if readme.exists():
 text=readme.read_text()
 table='## Catalogue\n\n| Opus | Piece | Metre | Sounded notes | PDF | Recording |\n|---|---|---|---:|---|---|\n'
 for p in cat:
  prefix=f'pieces/{p["folder"]}/{p["stem"]}'
  table+=f'| CWS Op. {p["op"]} | {p["title"]} | {p["meter"]} | {p["note_onsets"]} | [Score]({prefix}.pdf) | [MP3]({prefix}.mp3) |\n'
 table+='\n[Download the collected volumes](downloads/index.html): up to 24 works per volume, with a score PDF and a complete archive of recordings, MIDI, MusicXML and notation.\n\n'
 text=re.sub(r'## Catalogue\n.*?(?=## Run the gallery)',lambda _:table,text,flags=re.S)
 text=text.replace('all six works','all catalogue works')
 readme.write_text(text)
print(f'Prepared {len(manifest)} works in {len(volumes)} download volumes, with {sum(v["pages"] for v in volumes)} score pages.')
