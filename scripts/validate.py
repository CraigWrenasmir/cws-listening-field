from pathlib import Path
import json, xml.etree.ElementTree as ET, collections, subprocess
import mido
from music21 import converter, note, chord
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pieces';WORK=ROOT/'work'
cat=json.loads((ROOT/'data/catalog.json').read_text());report=[]
for p in cat:
 d=OUT/p['folder'];stem=p['stem'];r=ET.parse(d/(stem+'.musicxml')).getroot()
 ids=[n.get('id') for n in r.findall('.//note') if n.get('id')]
 assert len(ids)==len(set(ids)),('duplicate IDs',stem)
 score=converter.parse(str(d/(stem+'.musicxml')))
 # Tie continuations sustain an existing pitch and must not add an onset.
 score_count=0;actual=[]
 for part in score.parts:
  for n in part.flatten().notes:
   ns=[n] if isinstance(n,note.Note) else list(n.notes)
   for cn in ns:
    if cn.tie is None or cn.tie.type=='start':
     score_count+=1;actual.append((round(float(n.offset),6),cn.pitch.midi))
 expected=[(e['offset'],pi) for e in p['events'] for pi in e['pitches']]
 assert collections.Counter(actual)==collections.Counter(expected),('MusicXML pitch/onset mismatch',stem)
 assert score_count==p['note_onsets']<=256
 mid=mido.MidiFile(d/(stem+'.mid'));midi_notes=[]
 for tr in mid.tracks:
  tick=0;active={}
  for msg in tr:
   tick+=msg.time
   if msg.type=='note_on' and msg.velocity>0:
    assert (msg.channel,msg.note) not in active
    active[(msg.channel,msg.note)]=tick
    midi_notes.append((tick/mid.ticks_per_beat,msg.note))
   if msg.type=='note_off' or (msg.type=='note_on' and msg.velocity==0):
    assert (msg.channel,msg.note) in active
    del active[(msg.channel,msg.note)]
  assert not active
 assert collections.Counter(midi_notes)==collections.Counter(expected),('MIDI pitch/onset mismatch',stem)
 # Verify exact bar length independently from raw MusicXML timeline/backup/chord handling.
 for measure in r.findall('.//part/measure'):
  cursor=0;max_end=0
  for el in measure:
   if el.tag=='attributes' and el.find('divisions') is not None:divisions=int(el.findtext('divisions'))
   elif el.tag=='backup':cursor-=int(el.findtext('duration'))
   elif el.tag=='forward':cursor+=int(el.findtext('duration'))
   elif el.tag=='note':
    dur=int(el.findtext('duration','0'))
    if el.find('chord') is None:cursor+=dur
    max_end=max(max_end,cursor)
  assert max_end==p['beats_per_bar']*divisions,(stem,measure.get('number'),max_end)
 # Every slur must close on the staff where it started.
 opened={}
 for n in r.findall('.//note'):
  for sl in n.findall('notations/slur'):
   sn=sl.get('number')
   if sl.get('type')=='start':
    assert sn not in opened
    opened[sn]=n.findtext('staff')
   elif sl.get('type')=='stop':
    assert opened.pop(sn)==n.findtext('staff')
 assert not opened
 pages=len(PdfReader(d/(stem+'.pdf')).pages)
 assert 1<=pages<=4
 stats={}
 for hand in ['rh','lh']:
  evs=sorted([e for e in p['events'] if e['hand']==hand],key=lambda e:e['offset'])
  pitches=[pi for e in evs for pi in e['pitches']]
  leaps=[min(abs(a-b) for a in prev['pitches'] for b in curr['pitches']) for prev,curr in zip(evs,evs[1:])]
  rapid=[leap for leap,prev,curr in zip(leaps,evs,evs[1:]) if curr['offset']-prev['offset']<=.5]
  stats[hand]=dict(low=min(pitches),high=max(pitches),maximum_melodic_leap_semitones=max(leaps),maximum_eighth_note_leap_semitones=max(rapid,default=0),maximum_simultaneous_span_semitones=max(max(e['pitches'])-min(e['pitches']) for e in evs))
  assert stats[hand]['maximum_simultaneous_span_semitones']<=7
 # Ensure hands do not cross, using notated durations (not the shorter demo release).
 for beat in sorted(set(e['offset'] for e in p['events'])):
  active={h:[pi for e in p['events'] if e['hand']==h and e['offset']<=beat<e['offset']+e['duration'] for pi in e['pitches']] for h in ['rh','lh']}
  if active['rh'] and active['lh']:assert min(active['rh'])>=max(active['lh']),(stem,beat,active)
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_name,sample_rate,channels','-of','json',str(d/(stem+'.mp3'))]))
 assert abs(float(probe['format']['duration'])-p['duration_seconds'])<.1
 report.append(dict(piece=p['title'],opus=p['op'],score_pages=pages,bars=p['bars'],pitch_onsets=score_count,audio_seconds=p['duration_seconds'],hands=stats,checks='PASS: score/MIDI pitches and onset times, bar lengths, unique note IDs, slur endpoints, MIDI releases, hand separation, chord spans, PDF page count, audio duration'))
 print(json.dumps(report[-1]))
(WORK/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
