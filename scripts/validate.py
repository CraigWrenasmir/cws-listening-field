from pathlib import Path
import json, xml.etree.ElementTree as ET, collections, subprocess, argparse, re
import mido
from music21 import converter, note, chord
from music21.pitch import Pitch
from pypdf import PdfReader
from meter_plan import bar_plan
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pieces';WORK=ROOT/'work'
cat=json.loads((ROOT/'data/catalog.json').read_text());report=[]
parser=argparse.ArgumentParser();parser.add_argument('--opus',type=int,nargs='+');args=parser.parse_args()
# Compare score onsets at the exported MIDI resolution. This also represents
# triplet thirds exactly on the 960-tick grid, without float equality errors.
def onset_tick(beat):return round(float(beat)*960)
for p in cat:
 if args.opus is not None and p['op'] not in args.opus:continue
 d=OUT/p['folder'];stem=p['stem'];r=ET.parse(d/(stem+'.musicxml')).getroot()
 pages=len(PdfReader(d/(stem+'.pdf')).pages)
 assert 1<=pages<=4
 assert {f.name for f in d.glob(stem+'_page_*.svg')}=={f'{stem}_page_{i}.svg' for i in range(1,pages+1)},('SVG page set differs from PDF',p['op'])
 metres,bar_lengths,bar_starts,total_beats=bar_plan(p)
 if p.get('meters'):
  assert p['bar_beats']==bar_lengths and p['bar_offsets']==bar_starts and p['total_beats']==total_beats
  for event in p['events']:
   i=event['bar']-1
   assert bar_starts[i]<=event['offset']<bar_starts[i]+bar_lengths[i]
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
     score_count+=1;actual.append((onset_tick(n.offset),cn.pitch.midi))
 expected=[(onset_tick(e['offset']),pi) for e in p['events'] for pi in e['pitches']]
 assert collections.Counter(actual)==collections.Counter(expected),('MusicXML pitch/onset mismatch',stem)
 assert score_count==p['note_onsets']<=256
 mid=mido.MidiFile(d/(stem+'.mid'));midi_notes=[];midi_metres=[]
 for tr in mid.tracks:
  tick=0;active={}
  for msg in tr:
   tick+=msg.time
   if msg.type=='time_signature':midi_metres.append((onset_tick(tick/mid.ticks_per_beat),f'{msg.numerator}/{msg.denominator}'))
   if msg.type=='note_on' and msg.velocity>0:
    assert (msg.channel,msg.note) not in active
    active[(msg.channel,msg.note)]=tick
    midi_notes.append((onset_tick(tick/mid.ticks_per_beat),msg.note))
   if msg.type=='note_off' or (msg.type=='note_on' and msg.velocity==0):
    assert (msg.channel,msg.note) in active
    del active[(msg.channel,msg.note)]
  assert not active
 assert collections.Counter(midi_notes)==collections.Counter(expected),('MIDI pitch/onset mismatch',stem)
 expected_meters=[(onset_tick(bar_starts[i]),signature) for i,signature in enumerate(metres) if i==0 or signature!=metres[i-1]]
 assert midi_metres==expected_meters,('MIDI metre change mismatch',p['op'],midi_metres,expected_meters)
 if p.get('pedal_spans'):
  expected_pedal=[(onset_tick(start),onset_tick(end)) for start,end in p['pedal_spans']]
  for channel in [0,1]:
   actual_pedal=[];down=None
   for tr in mid.tracks:
    tick=0
    for message in tr:
     tick+=message.time
     if message.type=='control_change' and message.control==64 and message.channel==channel:
      if message.value>=64 and down is None:down=onset_tick(tick/mid.ticks_per_beat)
      elif message.value<64 and down is not None:actual_pedal.append((down,onset_tick(tick/mid.ticks_per_beat)));down=None
   assert down is None and actual_pedal==expected_pedal,('MIDI pedal span mismatch',p['op'],channel,actual_pedal)
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
  fragment=[e for e in ancestor['events'] if e['hand']==a['source_hand'] and (not a.get('source_voice') or e.get('voice')==a['source_voice']) and a['source_start_beat']<=e['offset']<a['source_end_beat']][:4]
  source_classes=[Pitch(n).pitchClass for n in a['source_pitches']]
  assert [max(e['pitches'])%12 for e in fragment]==source_classes,('Ancestor fragment mismatch',p['op'])
  child_classes=[Pitch(n).pitchClass for n in p['motif']['pitches']]
  assert [(n+a['transposition_semitones'])%12 for n in source_classes]==child_classes,('Ancestral interval mismatch',p['op'])
  motif=p['motif'];child=[e for e in p['events'] if e['hand']==motif['hand'] and (not motif.get('voice') or e.get('voice')==motif['voice']) and motif['start_beat']<=e['offset']<motif['end_beat']][:4]
  assert [max(e['pitches'])%12 for e in child]==child_classes,('Child fragment mismatch',p['op'])
 if p['op']>=7:
  notation_voices=collections.defaultdict(set);voice_labels=collections.defaultdict(set)
  durations=collections.defaultdict(float);source_events={e['id']:e for e in p['events']}
  for measure in r.findall('.//part/measure'):
   if measure.find('attributes/divisions') is not None:voice_divisions=int(measure.findtext('attributes/divisions'))
   for n in measure.findall('note'):
    if n.find('rest') is not None:continue
    staff=n.findtext('staff','1');xml_voice=n.findtext('voice');notation_voices[staff].add(xml_voice)
    match=re.match(r'(cws\d+-(?:rh|lh)-m\d+-n\d+)',n.get('id',''));assert match
    event=source_events[match[1]];voice_labels[(staff,xml_voice)].add(event.get('voice','single'))
    assert staff==('1' if event['hand']=='rh' else '2'),('Notated event moved to wrong hand',p['op'],event['id'])
    pitch=n.find('pitch');midi=(int(pitch.findtext('octave'))+1)*12+dict(C=0,D=2,E=4,F=5,G=7,A=9,B=11)[pitch.findtext('step')]+int(pitch.findtext('alter','0'))
    durations[(event['id'],midi)]+=int(n.findtext('duration'))/voice_divisions
  expected_durations={(e['id'],pitch):e['duration'] for e in p['events'] for pitch in e['pitches']}
  assert durations.keys()==expected_durations.keys()
  for key,value in expected_durations.items():assert abs(durations[key]-value)<1/960,('Notated sustain differs',p['op'],key)
  if p.get('voice_structure'):
   expected_labels=sorted((voice,) for voices in p['voice_structure'].values() for voice in voices)
   assert sorted(tuple(v) for v in voice_labels.values())==expected_labels,('Notated voice assignments differ',p['op'],voice_labels)
   for hand,voices in p['voice_structure'].items():
    staff='1' if hand=='rh' else '2'
    assert len(notation_voices[staff])==len(voices),('Missing independent notated voices',p['op'],staff,notation_voices)
    if len(voices)>1:assert None not in notation_voices[staff]
    assert {e.get('voice') for e in p['events'] if e['hand']==hand}==set(voices)
 if p.get('lower_sections'):
  actual_dynamics=[]
  for measure in r.findall('.//part/measure'):
   for direction in measure.findall('direction'):
    dynamic=direction.find('direction-type/dynamics')
    if dynamic is not None:
     assert len(dynamic)==1
     actual_dynamics.append((direction.findtext('staff','1'),int(measure.get('number')),dynamic[0].tag))
  expected_dynamics=[(staff,int(bar),value) for staff,changes in [('1',p['sections']),('2',p['lower_sections'])] for bar,value in changes.items()]
  assert sorted(actual_dynamics)==sorted(expected_dynamics),('Printed staff dynamics differ',p['op'])
  note_velocities={}
  for track in mid.tracks:
   tick=0
   for message in track:
    tick+=message.time
    if message.type=='note_on' and message.velocity>0:note_velocities[(message.channel,tick,message.note)]=message.velocity
  for event in p['events']:
   changes={int(k):v for k,v in (p['lower_sections'] if event['hand']=='lh' else p['sections']).items()}
   dynamic=changes[max(k for k in changes if k<=event['bar'])]
   assert event.get('notated_dynamic')==dynamic,('Performed staff dynamic differs',p['op'],event['id'])
   channel=0 if event['hand']=='rh' else 1
   for pitch in event['pitches']:
    expected_velocity=event['velocity']-(4 if p.get('performance') and len(event['pitches'])>1 and pitch<max(event['pitches']) else 0)
    assert note_velocities[(channel,onset_tick(event['offset']),pitch)]==expected_velocity,('MIDI voicing differs',p['op'],event['id'])
 if p.get('voice_phrases'):
  starts={};slur_pairs=[]
  notes=r.findall('.//part/measure/note')
  for n in notes:
   for slur in n.findall('notations/slur'):
    pair_key=(n.findtext('staff','1'),slur.get('number','1'))
    if slur.get('type')=='start':starts[pair_key]=n.get('id')
    elif slur.get('type')=='stop':
     assert pair_key in starts,('Unmatched voice phrase slur',p['op'])
     slur_pairs.append((starts.pop(pair_key),n.get('id')))
  for phrase in p['voice_phrases']:
   events=sorted([e for e in p['events'] if e.get('voice')==phrase['voice'] and phrase['start_beat']<=e['offset']<phrase['end_beat']],key=lambda e:e['offset'])
   assert events[0]['offset']==phrase['start_beat'] and events[-1]['offset']+events[-1]['duration']==phrase['end_beat']
   last=events[-1]['id']
   end_notes=[n for n in notes if n.find('chord') is None and (n.get('id')==last or n.get('id','').startswith(last+'-tie-'))]
   assert (events[0]['id'],end_notes[-1].get('id')) in slur_pairs,('Independent voice phrase slur differs',p['op'],phrase)
 if p.get('hidden_voice_rests'):
  expected_hidden={f'cws{p["op"]}-{hand}-m{bar}-n1001':(staff,voice) for voice,bars in p['hidden_voice_rests'].items() for hand,staff in [('rh','1') if voice=='inner' else ('lh','2')] for bar in bars}
  hidden=[n for n in r.findall('.//part/measure/note') if n.get('print-object')=='no']
  assert {n.get('id') for n in hidden}==set(expected_hidden),('Nonprinting voice rests differ',p['op'])
  for n in hidden:
   staff,voice=expected_hidden[n.get('id')]
   assert n.find('rest') is not None and n.findtext('staff','1')==staff,('Hidden rest is not on its declared staff',p['op'],n.get('id'))
   assert voice_labels[(staff,n.findtext('voice'))]=={voice},('Hidden rest is not in its declared additional voice',p['op'],n.get('id'))
 # Verify exact bar length independently from raw MusicXML timeline/backup/chord handling.
 pedal_directions=[];notated_signature=None;notated_meters=[]
 for measure in r.findall('.//part/measure'):
  mi=int(measure.get('number'))-1
  cursor=0;max_end=0;voice_durations=collections.Counter()
  signatures={f'{t.findtext("beats")}/{t.findtext("beat-type")}' for t in measure.findall('attributes/time')}
  if signatures:
   assert len(signatures)==1,('Hands have conflicting metres',p['op'],mi+1,signatures)
   signature=signatures.pop()
   if signature!=notated_signature:notated_meters.append((onset_tick(bar_starts[mi]),signature))
   notated_signature=signature
  assert notated_signature==metres[mi],('Printed metre mismatch',p['op'],mi+1,notated_signature,metres[mi])
  for el in measure:
   if el.tag=='attributes' and el.find('divisions') is not None:divisions=int(el.findtext('divisions'))
   elif el.tag=='backup':cursor-=int(el.findtext('duration'))
   elif el.tag=='forward':cursor+=int(el.findtext('duration'))
   elif el.tag=='direction' and el.find('direction-type/pedal') is not None:
    direction=el.find('direction-type/pedal')
    beat=bar_starts[mi]+(cursor+float(el.findtext('offset','0')))/divisions
    pedal_directions.append((onset_tick(beat),direction.get('type'),el.findtext('staff','1')))
   elif el.tag=='note':
    dur=int(el.findtext('duration','0'))
    if p.get('hidden_voice_rests') and el.get('print-object')=='no':assert dur==bar_lengths[mi]*divisions,('Hidden rest must fill its bar',p['op'],el.get('id'))
    if el.find('chord') is None:
     cursor+=dur;voice_durations[(el.findtext('staff','1'),el.findtext('voice','1'))]+=dur
    max_end=max(max_end,cursor)
  assert max_end==bar_lengths[mi]*divisions,(stem,measure.get('number'),max_end)
  if p.get('meters'):assert all(value==bar_lengths[mi]*divisions for value in voice_durations.values()),('Independent bar duration mismatch',p['op'],mi+1,voice_durations)
 assert notated_meters==expected_meters,('Printed metre changes differ',p['op'],notated_meters,expected_meters)
 if p.get('pedal_spans'):
  expected_marks=sorted((onset_tick(beat),kind,'2') for span in p['pedal_spans'] for beat,kind in zip(span,['start','stop']))
  assert sorted(pedal_directions)==expected_marks,('Printed pedal span mismatch',p['op'],pedal_directions,expected_marks)
  svg_ns='{http://www.w3.org/2000/svg}'
  rendered_pedals=set()
  for svg in d.glob(stem+'_page_*.svg'):
   for group in ET.parse(svg).getroot().findall('.//'+svg_ns+'g[@class="pedal"]'):
    if len(group):rendered_pedals.add(group.get('id'))
  assert None not in rendered_pedals and len(rendered_pedals)==len(p['pedal_spans']),('Pedal span omitted by engraving',p['op'],len(rendered_pedals),len(p['pedal_spans']))
 if p.get('clef_changes'):
  actual_clefs=collections.defaultdict(list)
  for measure in r.findall('.//part/measure'):
   for mark in measure.findall('attributes/clef'):
    actual_clefs[mark.get('number','1')].append((int(measure.get('number')),mark.findtext('sign'),mark.findtext('line')))
  for hand,staff in [('rh','1'),('lh','2')]:
   changes={1:'treble' if hand=='rh' else 'bass'}
   changes.update({int(bar):name for bar,name in p['clef_changes'].get(hand,{}).items()})
   expected_clefs=[(bar,'G' if name=='treble' else 'F','2' if name=='treble' else '4') for bar,name in sorted(changes.items())]
   assert actual_clefs[staff]==expected_clefs,('Printed clef change mismatch',p['op'],hand,actual_clefs[staff],expected_clefs)
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
 tuplets=collections.Counter()
 for n in r.findall('.//note'):
  modification=n.find('time-modification')
  if modification is not None:
   tuplets[(n.findtext('staff','1'),int(modification.findtext('actual-notes')),int(modification.findtext('normal-notes')))]+=1
 for hand in p.get('tuplet_hands',[]):
  assert tuplets[('1' if hand=='rh' else '2',3,2)]>0,('Missing notated triplets',p['op'],hand)
 for group in p.get('tuplet_groups',[]):
  key=('1' if group['hand']=='rh' else '2',group['actual'],group['normal'])
  assert tuplets[key]==group['count'],('Notated tuplet count mismatch',p['op'],group,tuplets[key])
 for number,spec in enumerate(p.get('tuplet_spans',[]),1):
  group=sorted([e for e in p['events'] if e['hand']==spec['hand'] and (not spec.get('voice') or e.get('voice')==spec['voice']) and spec['start_beat']<=e['offset']<spec['end_beat']-1e-8],key=lambda e:e['offset'])
  assert len(group)==spec['actual']
  xml_notes={n.get('id'):n for n in r.findall('.//part/measure/note') if n.get('id')}
  for i,event in enumerate(group):
   n=xml_notes[event['id']]
   assert n.findtext('type')==n.findtext('time-modification/normal-type')=='eighth'
   assert n.find('dot') is None and n.find('time-modification/normal-dot') is None
   assert int(n.findtext('time-modification/actual-notes'))==spec['actual'] and int(n.findtext('time-modification/normal-notes'))==spec['normal']
   assert n.findtext('stem')==spec.get('stem','down')
   assert [(b.get('number'),b.text) for b in n.findall('beam')]==[('1','begin' if i==0 else 'end' if i==len(group)-1 else 'continue')]
   marks=n.findall('notations/tuplet')
   expected=[('start',str(number))] if i==0 else [('stop',str(number))] if i==len(group)-1 else []
   assert [(t.get('type'),t.get('number')) for t in marks]==expected,('Tuplet bracket span',p['op'],event['id'])
   if i==0:assert marks[0].get('bracket')=='yes' and marks[0].get('placement')==spec.get('placement','above')
   if i==0:assert marks[0].get('show-number')==spec.get('show_number','actual')
 for spec in p.get('beam_spans',[]):
  step,levels={'eighth':(.5,1),'16th':(.25,2),'32nd':(.125,3)}[spec['note_type']]
  group=sorted([e for e in p['events'] if e['hand']==spec['hand'] and (not spec.get('voice') or e.get('voice')==spec['voice']) and spec['start_beat']<=e['offset']<spec['end_beat']-1e-8],key=lambda e:e['offset'])
  assert len(group)>=2 and abs(spec['end_beat']-spec['start_beat']-len(group)*step)<1e-8
  xml_notes={n.get('id'):n for n in r.findall('.//part/measure/note') if n.get('id')}
  for i,event in enumerate(group):
   n=xml_notes[event['id']]
   assert len(event['pitches'])==1 and abs(event['offset']-spec['start_beat']-i*step)<1e-8 and abs(event['duration']-step)<1e-8
   assert n.findtext('type')==spec['note_type'] and n.findtext('stem')==spec['stem'] and n.find('time-modification') is None and n.find('dot') is None and n.find('tie') is None
   mark='begin' if i==0 else 'end' if i==len(group)-1 else 'continue'
   assert [(b.get('number'),b.text) for b in n.findall('beam')]==[(str(j+1),mark) for j in range(levels)],('Explicit beam group',p['op'],event['id'])
 for crossing in p.get('polyrhythms',[]):
  start=crossing['start_beat'];end=crossing['end_beat']
  for hand in ['rh','lh']:
   count=crossing[hand+'_notes'];step=(end-start)/count
   notes=sorted([e for e in p['events'] if e['hand']==hand and start<=e['offset']<end-1e-8],key=lambda e:e['offset'])
   assert len(notes)==count,('Polyrhythm note count',p['op'],crossing,hand)
   for i,e in enumerate(notes):assert abs(e['offset']-(start+i*step))<1/960 and abs(e['duration']-step)<1/960,('Polyrhythm alignment',p['op'],hand,e['id'])
 stats={}
 limits=p.get('technique_limits',dict(chord_span=7,melodic_leap=12,rapid_leap=7))
 crossings=p.get('hand_crossings',[])
 transition_leaps=[]
 if p['op']>=21:
  assert p.get('difficulty') and p.get('technical_note') and p.get('technique_limits'),('Document the technical review',p['op'])
 for hand in ['rh','lh']:
  evs=sorted([e for e in p['events'] if e['hand']==hand],key=lambda e:e['offset'])
  pitches=[pi for e in evs for pi in e['pitches']]
  leaps=[];rapid=[]
  for voice in set(e.get('voice','single') for e in evs):
   line=[e for e in evs if e.get('voice','single')==voice]
   for prev,curr in zip(line,line[1:]):
    leap=min(abs(a-b) for a in prev['pitches'] for b in curr['pitches']);leaps.append(leap)
    if curr['offset']-prev['offset']<=.5:rapid.append(leap)
    if crossings:
     allowed=limits['melodic_leap']
     for crossing in crossings:
      for boundary,rest in [(crossing['start_beat'],crossing['rest_before']),(crossing['end_beat']+crossing['rest_after'],crossing['rest_after'])]:
       if abs(curr['offset']-boundary)<1e-8 and prev['offset']+prev['duration']<=boundary-rest+1e-8:
        allowed=max(allowed,crossing.get('max_transition_leap',allowed))
     assert leap<=allowed,('Wide leap needs review',stem,hand,prev['id'],curr['id'],leap,allowed)
     if leap>limits['melodic_leap']:transition_leaps.append(dict(hand=hand,voice=voice,from_beat=prev['offset'],to_beat=curr['offset'],rest_beats=curr['offset']-prev['offset']-prev['duration'],semitones=leap))
  stats[hand]=dict(low=min(pitches),high=max(pitches),maximum_melodic_leap_semitones=max(leaps),maximum_eighth_note_leap_semitones=max(rapid,default=0),maximum_simultaneous_span_semitones=max(max(e['pitches'])-min(e['pitches']) for e in evs))
  assert stats[hand]['maximum_simultaneous_span_semitones']<=limits['chord_span'],('Hand span needs review',p['op'],hand,stats[hand],limits)
  if p['op']>=7:
   assert stats[hand]['maximum_eighth_note_leap_semitones']<=limits['rapid_leap'],('Rapid leap needs review',stem,hand,stats[hand],limits)
   if not crossings:assert stats[hand]['maximum_melodic_leap_semitones']<=limits['melodic_leap'],('Wide leap needs review',stem,hand,stats[hand],limits)
 previous_end=-1
 for crossing in crossings:
  start,end=crossing['start_beat'],crossing['end_beat']
  before,after=crossing['rest_before'],crossing['rest_after']
  assert before>0 and after>0 and 0<=start-before<start<end<end+after<total_beats
  assert start-before>=previous_end,('Overlapping hand-crossing transitions',p['op'])
  previous_end=end+after
  for left,right in [(start-before,start),(end,end+after)]:
   assert not any(e['offset']<right-1e-8 and e['offset']+e['duration']>left+1e-8 for e in p['events']),('Hand-crossing transition needs written silence',p['op'],left,right)
  for hand,label in [('rh','m.d.'),('lh','m.s.')]:
   assert any(e['hand']==hand and abs(e['offset']-start)<1e-8 for e in p['events'])
   for boundary in [start,end+after]:
    bar=next((i+1 for i,t in enumerate(bar_starts) if abs(t-boundary)<1e-8),None)
    assert bar and p.get('hand_labels',{}).get(hand,{}).get(str(bar))==label,('Missing hand label at register exchange',p['op'],hand,boundary)
 if p.get('hand_labels'):
  expected_labels=sorted((int(bar),'1' if hand=='rh' else '2',label) for hand,labels in p['hand_labels'].items() for bar,label in labels.items())
  actual_labels=[]
  for measure in r.findall('.//part/measure'):
   for direction in measure.findall('direction'):
    for word in direction.findall('direction-type/words'):
     if word.text in ('m.d.','m.s.'):actual_labels.append((int(measure.get('number')),direction.findtext('staff','1'),word.text))
  assert sorted(actual_labels)==expected_labels,('Printed hand labels',p['op'],actual_labels,expected_labels)
 # Check the declared hand order using full notated durations.
 for beat in sorted(set(e['offset'] for e in p['events'])):
  active={h:[pi for e in p['events'] if e['hand']==h and e['offset']<=beat<e['offset']+e['duration'] for pi in e['pitches']] for h in ['rh','lh']}
  crossed=any(c['start_beat']<=beat<c['end_beat'] for c in crossings)
  lower,upper=('rh','lh') if crossed else ('lh','rh')
  if active['rh'] and active['lh']:assert min(active[upper])>=max(active[lower]),('Hand order',stem,beat,active)
  if p.get('voice_structure') or crossings:
   for hand,pitches in active.items():
    assert len(pitches)==len(set(pitches)),('Overlapping same-hand pitch',p['op'],beat,hand,pitches)
    if pitches:
     span=max(pitches)-min(pitches)
     assert span<=limits['chord_span'],('Polyphonic hand span needs review',p['op'],beat,hand,span)
     stats[hand]['maximum_simultaneous_span_semitones']=max(stats[hand]['maximum_simultaneous_span_semitones'],span)
   assert not set(active['rh'])&set(active['lh']),('Both hands need the same key',p['op'],beat)
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_name,sample_rate,channels','-of','json',str(d/(stem+'.mp3'))]))
 assert abs(float(probe['format']['duration'])-p['duration_seconds'])<.1
 report.append(dict(piece=p['title'],opus=p['op'],score_pages=pages,bars=p['bars'],pitch_onsets=score_count,audio_seconds=p['duration_seconds'],hands=stats,checks='PASS: score/MIDI pitches and onset times, bar lengths, unique note IDs, slur endpoints, MIDI releases, hand separation, chord spans, PDF page count, audio duration'))
 report[-1]['midi_highlight_timing_error_seconds']=round(timing_error,7)
 if p['op']>=21:report[-1]['technical_review']=dict(difficulty=p['difficulty'],limits=limits,note=p['technical_note'])
 if tuplets:report[-1]['notated_tuplet_notes']={':'.join(map(str,k)):v for k,v in tuplets.items()}
 if p.get('pedal_spans'):report[-1]['verified_notated_and_midi_pedal_spans']=p['pedal_spans']
 if p.get('voice_structure'):report[-1]['verified_independent_voices']=p['voice_structure']
 if p.get('lower_sections'):report[-1]['verified_staff_dynamics']={'rh':p['sections'],'lh':p['lower_sections']}
 if p.get('voice_phrases'):report[-1]['verified_voice_phrases']=p['voice_phrases']
 if p.get('hidden_voice_rests'):report[-1]['verified_nonprinting_voice_rests']=p['hidden_voice_rests']
 if p.get('polyrhythms'):report[-1]['verified_polyrhythm_spans']=p['polyrhythms']
 if p.get('tuplet_spans'):report[-1]['verified_tuplet_brackets']=p['tuplet_spans']
 if p.get('beam_spans'):report[-1]['verified_beam_groups']=p['beam_spans']
 if p.get('clef_changes'):report[-1]['verified_clef_changes']=p['clef_changes']
 if crossings:report[-1]['verified_hand_crossings']=crossings
 if transition_leaps:report[-1]['verified_transition_leaps']=transition_leaps
 if p.get('hand_labels'):report[-1]['verified_hand_labels']=p['hand_labels']
 if p.get('meters'):report[-1]['verified_meter_changes']=[dict(beat=tick/960,meter=signature) for tick,signature in expected_meters]
 if p['op']>=7:
  patterns=[]
  for measure in range(1,p['bars']+1):patterns.append(tuple((e['offset']-bar_starts[measure-1],e['duration'],len(e['pitches'])) for e in p['events'] if e['hand']=='lh' and e['bar']==measure))
  report[-1]['musical_review_support']=dict(whole_piece_duplicate_or_transposition=False,left_hand_rhythm_patterns=len(set(patterns)),left_hand_most_frequent_pattern_bars=collections.Counter(patterns).most_common(1)[0][1],sounded_pitches_per_minute=round(p['note_onsets']/p['performance_seconds']*60,1),note='These structural checks do not establish artistic quality or replace listening feedback.')
 print(json.dumps(report[-1]))
report_path=ROOT/'data/validation.json'
old=json.loads(report_path.read_text()) if report_path.exists() else []
replaced={r['opus'] for r in report}
merged=sorted([r for r in old if r['opus'] not in replaced]+report,key=lambda r:r['opus'])
report_path.write_text(json.dumps(merged,indent=2)+'\n')
(WORK/'validation.json').write_text(json.dumps(merged,indent=2)+'\n')
