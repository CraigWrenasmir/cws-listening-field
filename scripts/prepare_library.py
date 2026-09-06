"""Publish catalogue metadata and downloadable collections from checked piece assets."""
from pathlib import Path
import json,zipfile,re,xml.etree.ElementTree as ET
from pypdf import PdfWriter,PdfReader
ROOT=Path(__file__).resolve().parents[1]
cat=json.loads((ROOT/'data/catalog.json').read_text())
legacy={1:dict(parent_opus=None,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['D','F','E','A'])),2:dict(parent_opus=1,motif=dict(hand='lh',start_beat=0,end_beat=3,pitches=['D','F','E','A'])),3:dict(parent_opus=1,motif=dict(hand='rh',start_beat=48,end_beat=52,pitches=['A','C','B','E']))}
manifest=[];writer=PdfWriter()
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
 chord_events=sorted([e for e in p['events'] if len(e['pitches'])>1],key=lambda e:(e['bar'],0 if e['hand']=='rh' else 1,e['offset']))
 parsed=[ET.parse(ROOT/s) for s in scores]
 chord_groups=[g for tree in parsed for g in tree.getroot().iter() if g.get('class')=='chord']
 assert len(chord_groups)==len(chord_events),'Explicit chord mapping required for tied/multiple chord engravings'
 for g,e in zip(chord_groups,chord_events):g.set('id',e['id'])
 for tree,s in zip(parsed,scores):tree.write(ROOT/s,encoding='unicode')
 for s in scores:
  # The glyph outlines already carry the notation; remove redundant embedded webfonts.
  path=ROOT/s;text=path.read_text();text=re.sub(r'@font-face\s*\{[^}]*\}','',text);path.write_text(text)
 entry=dict(op=p['op'],title=p['title'],slug=f'cws-op-{p["op"]:03d}-'+p['title'].lower().replace(' ','-'),stamp=p['composition_stamp'],beats=p['bars']*p['beats_per_bar'],duration=p['duration_seconds'],performance=p['performance_seconds'],audio=prefix+'.mp3',pdf=prefix+'.pdf',midi=prefix+'.mid',xml=prefix+'.musicxml',scores=scores,parent=parent,motif=motif,note_onsets=p['note_onsets'],pages=pages,
  events=[dict(id=e['id'],h=e['hand'],b=e['offset'],d=e['duration'],p=max(e['pitches']),ps=e['pitches'],s=e['seconds'],e=e['end_seconds']) for e in p['events']])
 manifest.append(entry);writer.append(str(folder/(stem+'.pdf')),outline_item=f'CWS Op. {p["op"]} - {p["title"]}')
(ROOT/'library.json').write_text(json.dumps(manifest,separators=(',',':'))+'\n')
downloads=ROOT/'downloads';downloads.mkdir(exist_ok=True)
writer.add_metadata({'/Title':'CWS First Studies - Six Piano Pieces','/Author':'CWS Library - studies with Maple (AI)'})
with (downloads/'CWS_First_Studies_Scores.pdf').open('wb') as f:writer.write(f)
with zipfile.ZipFile(downloads/'CWS_First_Studies.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in cat:
  for path in sorted((ROOT/'pieces'/p['folder']).glob('*')):
   if path.is_file():z.write(path,str(path.relative_to(ROOT)))
 for name in ['data/STYLE.md','licenses/Leipzig-OFL.txt','licenses/GeneralUser-GS.txt']:
  z.write(ROOT/name,name)
 z.write(downloads/'CWS_First_Studies_Scores.pdf','CWS_First_Studies_Scores.pdf')
with zipfile.ZipFile(downloads/'CWS_First_Studies.zip') as z:assert z.testzip() is None
print(f'Prepared {len(manifest)} works, {len(writer.pages)} combined score pages, and full downloads.')
