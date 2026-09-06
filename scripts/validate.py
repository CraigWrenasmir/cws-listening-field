from pathlib import Path
import json, xml.etree.ElementTree as ET, collections, subprocess, argparse
import mido
from music21 import converter, note, chord
from music21.pitch import Pitch
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pieces';WORK=ROOT/'work'
cat=json.loads((ROOT/'data/catalog.json').read_text());report=[]
parser=argparse.ArgumentParser();parser.add_argument('--opus',type=int,nargs='+');args=parser.parse_args()
for p in cat:
 if args.opus is not None and p['op'] not in args.opus:continue
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
 # Check audible clock time independently by integrating the actual MIDI tempo
 # messages. The score player must follow rubato and tied onsets exactly.
 seconds=0;heard=collections.defaultdict(list);planned=collections.defaultdict(list)
 for message in mid:
  seconds+=message.time
  if message.type=='note_on' and message.velocity>0:heard[(message.channel,message.note)].append(seconds)
 for event in p['events']:
  for pitch in event['pitches']:planned[(0 if event['hand']=='rh' else 1,pitch)].append(event['seconds'])
 assert heard.keys()==planned.keys(),('MIDI time-map voices',stem)
 timing_error=0
 for voice,starts in planned.items():
  assert len(starts)==len(heard[voice])
  timing_error=max(timing_error,max(abs(a-b) for a,b in zip(sorted(starts),sorted(heard[voice]))))
 assert timing_error<.003,('Audio/highlight clock drift',stem,timing_error)
 def fingerprint(piece):
  ordered=sorted(piece['events'],key=lambda e:(e['offset'],e['hand']))
  origin=ordered[0]['pitches'][0]
  return [(e['hand'],e['offset'],e['duration'],tuple(pi-origin for pi in e['pitches'])) for e in ordered]
 if p['op']>=7:
  signature=fingerprint(p)
  for earlier in cat:
   if earlier['op']<p['op']:assert signature!=fingerprint(earlier),('Whole-piece duplicate or transposition',p['op'],earlier['op'])
 # Documented fragments are checked against both the ancestor and the child.
 # Octave placement may change; the declared transposition relates pitch classes.
 if p.get('ancestry'):
  a=p['ancestry'];ancestor=next(x for x in cat if x['op']==a['source_opus'])
  assert a['source_opus']==p['parent_opus']<p['op']
  fragment=[e for e in ancestor['events'] if e['hand']==a['source_hand'] and a['source_start_beat']<=e['offset']<a['source_end_beat']][:4]
  source_classes=[Pitch(n).pitchClass for n in a['source_pitches']]
  assert [max(e['pitches'])%12 for e in fragment]==source_classes,('Ancestor fragment mismatch',p['op'])
  child_classes=[Pitch(n).pitchClass for n in p['motif']['pitches']]
  assert [(n+a['transposition_semitones'])%12 for n in source_classes]==child_classes,('Ancestral interval mismatch',p['op'])
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
 limits=p.get('technique_limits',dict(chord_span=7,melodic_leap=12,rapid_leap=7))
 if p['op']>=21:
  assert p.get('difficulty') and p.get('technical_note') and p.get('technique_limits'),('Document the technical review',p['op'])
 for hand in ['rh','lh']:
  evs=sorted([e for e in p['events'] if e['hand']==hand],key=lambda e:e['offset'])
  pitches=[pi for e in evs for pi in e['pitches']]
  leaps=[min(abs(a-b) for a in prev['pitches'] for b in curr['pitches']) for prev,curr in zip(evs,evs[1:])]
  rapid=[leap for leap,prev,curr in zip(leaps,evs,evs[1:]) if curr['offset']-prev['offset']<=.5]
  stats[hand]=dict(low=min(pitches),high=max(pitches),maximum_melodic_leap_semitones=max(leaps),maximum_eighth_note_leap_semitones=max(rapid,default=0),maximum_simultaneous_span_semitones=max(max(e['pitches'])-min(e['pitches']) for e in evs))
  assert stats[hand]['maximum_simultaneous_span_semitones']<=limits['chord_span'],('Hand span needs review',p['op'],hand,stats[hand],limits)
  if p['op']>=7:
   assert stats[hand]['maximum_eighth_note_leap_semitones']<=limits['rapid_leap'],('Rapid leap needs review',stem,hand,stats[hand],limits)
   assert stats[hand]['maximum_melodic_leap_semitones']<=limits['melodic_leap'],('Wide leap needs review',stem,hand,stats[hand],limits)
 # Ensure hands do not cross, using notated durations (not the shorter demo release).
 for beat in sorted(set(e['offset'] for e in p['events'])):
  active={h:[pi for e in p['events'] if e['hand']==h and e['offset']<=beat<e['offset']+e['duration'] for pi in e['pitches']] for h in ['rh','lh']}
  if active['rh'] and active['lh']:assert min(active['rh'])>=max(active['lh']),(stem,beat,active)
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_name,sample_rate,channels','-of','json',str(d/(stem+'.mp3'))]))
 assert abs(float(probe['format']['duration'])-p['duration_seconds'])<.1
 report.append(dict(piece=p['title'],opus=p['op'],score_pages=pages,bars=p['bars'],pitch_onsets=score_count,audio_seconds=p['duration_seconds'],hands=stats,checks='PASS: score/MIDI pitches and onset times, bar lengths, unique note IDs, slur endpoints, MIDI releases, hand separation, chord spans, PDF page count, audio duration'))
 report[-1]['midi_highlight_timing_error_seconds']=round(timing_error,7)
 if p['op']>=21:report[-1]['technical_review']=dict(difficulty=p['difficulty'],limits=limits,note=p['technical_note'])
 if p['op']>=7:
  patterns=[]
  for measure in range(1,p['bars']+1):patterns.append(tuple((e['offset']%p['beats_per_bar'],e['duration'],len(e['pitches'])) for e in p['events'] if e['hand']=='lh' and e['bar']==measure))
  report[-1]['musical_review_support']=dict(whole_piece_duplicate_or_transposition=False,left_hand_rhythm_patterns=len(set(patterns)),left_hand_most_frequent_pattern_bars=collections.Counter(patterns).most_common(1)[0][1],sounded_pitches_per_minute=round(p['note_onsets']/p['performance_seconds']*60,1),note='These structural checks do not establish artistic quality or replace listening feedback.')
 print(json.dumps(report[-1]))
report_path=ROOT/'data/validation.json'
old=json.loads(report_path.read_text()) if report_path.exists() else []
replaced={r['opus'] for r in report}
merged=sorted([r for r in old if r['opus'] not in replaced]+report,key=lambda r:r['opus'])
report_path.write_text(json.dumps(merged,indent=2)+'\n')
(WORK/'validation.json').write_text(json.dumps(merged,indent=2)+'\n')
