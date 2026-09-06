from pathlib import Path
import json, math, argparse, xml.etree.ElementTree as ET
from new_pieces import NEW_PIECES
from dream_pieces import DREAM_PIECES
from datetime import datetime
from zoneinfo import ZoneInfo
from music21 import stream, note, chord, meter, key, clef, tempo, dynamics, expressions, layout, metadata, instrument, spanner, articulations, bar, duration, tie

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'pieces'
WORK=ROOT/'work'
WORK.mkdir(exist_ok=True)
STYLE=json.loads((ROOT/'data/library_style.json').read_text())

# Each row is one bar. Durations are quarter-note units, including in 6/8.
# These are individually specified compositions, not random generation.
PIECES=[dict(op=1,title='Moss Atlas',key='d',fifths=-1,meter='3/4',bpm=66,tempo='Quietly, with warmth',
 subtitle='A path remembered by its moss',
 description='A four-note thought crosses a quiet landscape. The answering line gradually rises towards it; the return settles into D minor without a hard dominant cadence.',
 rh='''
D5:1 F5:.5 E5:.5 A4:1
C5:1 A4:1 F4:1
A4:1.5 G4:.5 E4:1
G4:1 E4:.5 F4:.5 G4:1
A4:1 Bb4:.5 A4:.5 D5:1
F5:1 E5:1 D5:1
C5:1 A4:.5 G4:.5 F4:1
E4:2 R:.5 A4:.5
D5:1 F5:.5 E5:.5 A4:1
C5:1.5 D5:.5 F5:1
E5:1 D5:.5 C5:.5 A4:1
Bb4:.5 A4:.5 G4:1 E4:1
A4:1 C5:1 E5:1
D5:1 G5:.5 E5:.5 C5:1
D5:1.5 Bb4:.5 A4:1
E5:1 C#5:.5 B4:.5 A4:1
F5:1 E5:.5 D5:.5 C5:1
E5:1 C5:1 A4:1
Bb4:1 A4:.5 G4:.5 D5:1
C#5:1 E5:1 A4:1
D5:1 F5:.5 E5:.5 A4:1
C5:1 A4:1 F4:1
G4:1 E4:1 C4:1
D4:3
''',
 lh='''
D3:1.5 A3:.5 F3:1
Bb2:1 F3:.5 G3:.5 A3:1
A2:1 E3:1 C3:1
C3:1 G3:.5 A3:.5 E3:1
G2:1 D3:1 F3:1
F3:1 A3:.5 G3:.5 F3:1
G2:1 D3:1 A3:1
A2:1 E3:1 C#3:1
D3:1.5 A3:.5 F3:1
Bb2:1 F3:1 A3:1
G3:1 Bb3:1 F3:1
A2:1 E3:.5 F3:.5 C#3:1
F3:1 E3:1 C3:1
E3:1 G3:1 A3:1
G3:1 D3:.5 E3:.5 F3:1
A2:1 E3:1 G3:1
Bb2:1 F3:1 A3:1
A2:1 E3:.5 F3:.5 C3:1
G2:1 D3:1 F3:1
A2:1 G3:1 E3:1
D3:1 A3:1 F3:1
Bb2:1 F3:1 A3:1
C3:1 G3:1 E3:1
D3+F3:3
''',
 sections={1:'p',9:'mp',13:'mp',17:'p',21:'pp'},
 words={1:'Let the two lines sing; pedal lightly, changing each bar.',9:'a little nearer',17:'receding',23:'poco rit.'},
 slurs=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24)],
 hairpins=[('crescendo',5,7),('diminuendo',7,8),('crescendo',13,15),('diminuendo',15,16),('diminuendo',21,24)],
 tempo_changes={23:62,24:56},group=4),
 dict(op=2,title='Velvet Estuary',key='F',fifths=-1,meter='6/8',bpm=78,tempo='Gently flowing',
 subtitle='The tide returns a borrowed melody',
 description='The shared D-F-E-A figure appears in the left hand beneath a warmer, rocking upper voice. Relative-major light surrounds a minor centre; the hands exchange fragments rather than repeating a single accompaniment.',
 rh='''
A4:1.5 C5:1.5
D5:1 C5:.5 A4:1.5
G4:1 A4:.5 C5:1 E5:.5
D5:1 C5:.5 G4:1.5
A4:.5 C5:.5 D5:.5 F5:1 E5:.5
D5:1 C5:.5 A4:1.5
G4:1.5 F4:1 E4:.5
F4:2.5 R:.5
A4:1.5 F4:.5 G4:.5 A4:.5
Bb4:1 A4:.5 F4:1.5
E4:.5 G4:.5 A4:.5 C5:1 B4:.5
A4:1.5 G4:1 E4:.5
F4:.5 A4:.5 C5:.5 D5:1 C5:.5
Bb4:1 A4:.5 F4:1.5
G4:.5 A4:.5 Bb4:.5 G4:1 E4:.5
F4:2.5 R:.5
D5:1 F5:.5 E5:.5 A4:1
C5:1.5 A4:.5 G4:.5 F4:.5
E4:.5 G4:.5 C5:.5 B4:1 A4:.5
G4:1.5 E4:1.5
F4:1 A4:.5 C5:1 D5:.5
C5:1 A4:.5 G4:1 E4:.5
F4:1.5 G4:1 E4:.5
F4:3
''',
 lh='''
D3:.5 F3:.5 E3:.5 A2:1.5
Bb2:1.5 D3:1 F3:.5
A2:1.5 E3:.5 F3:.5 G3:.5
C3:1.5 E3:1.5
D3:1.5 A3:.5 G3:.5 E3:.5
Bb2:.5 D3:.5 F3:.5 A3:1.5
C3:.5 E3:.5 G3:.5 Bb3:1.5
F3:1.5 A3:1.5
F3:1 E3:.5 D3:.5 F3:.5 E3:.5
D3:1.5 A2:1.5
C3:1.5 E3:1.5
E3:.5 F3:.5 G3:.5 C3:1.5
D3:1.5 F3:.5 E3:.5 D3:.5
Bb2:.5 D3:.5 F3:.5 A3:1.5
C3:1.5 Bb2:1.5
F3:1.5 R:1.5
D3:1.5 F3:1 E3:.5
Bb2:1.5 D3:.5 E3:.5 F3:.5
C3:1.5 E3:1.5
E3:.5 F3:.5 G3:.5 C3:1.5
D3:.5 F3:.5 E3:.5 A2:1.5
C3:1.5 E3:1.5
Bb2:1.5 C3:1.5
F3+A3:3
''',
 sections={1:'p',9:'mp',17:'p',21:'pp'},
 words={1:'Two gentle pulses per bar; pedal sparingly.',9:'the lower voice a little clearer',17:'like a recollection',23:'poco rit.'},
 slurs=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24)],
 hairpins=[('crescendo',3,5),('diminuendo',5,8),('crescendo',11,13),('diminuendo',13,16),('diminuendo',21,24)],
 tempo_changes={23:73,24:66},group=4),
 dict(op=3,title='Orchard Static',key='a',fifths=0,meter='4/4',bpm=62,tempo='Spacious, gently luminous',
 subtitle='An orchard heard through an empty room',
 description='The four-note ancestor is turned over: E-C-D-A. Long notes make room for a second voice. A brief Dorian inflection gives the central passage a little light before the opening returns more quietly.',
 rh='''
E5:2 C5:1 D5:.5 A4:.5
B4:1 C5:1 E5:2
G5:1 E5:1 D5:1 B4:1
C5:2 A4:1 R:1
E5:1 C5:1 D5:.5 E5:.5 A4:1
F5:1 E5:1 C5:2
D5:1 B4:1 A4:1 G4:1
A4:3 R:1
C5:1 D5:1 E5:2
F#5:1 E5:1 D5:1 B4:1
E5:1 D5:.5 C5:.5 B4:1 A4:1
G4:2 E4:1 R:1
A4:1 C5:.5 B4:.5 E5:2
D5:1 C5:1 A4:2
B4:1 D5:1 C5:1 G4:1
A4:3 R:1
E5:2 C5:1 D5:.5 A4:.5
B4:1 C5:1 E5:2
D5:1 B4:1 G4:1 E4:1
A4:4
''',
 lh='''
A2:2 E3:1 C3:1
F3:1 A3:1 G3:1 E3:1
C3:1 G3:1 E3:1 G3:1
F3:1 E3:1 A2:2
A2:1 E3:1 G3:1 C3:1
F3:1 A3:1 G3:1 E3:1
G2:1 D3:1 F3:1 E3:1
A2:1 E3:1 C3:1 B2:1
A2:1 E3:1 C3:2
D3:2 F#3:1 A3:1
E3:1 A3:1 G3:1 E3:1
C3:1 G3:1 C4:1 B3:1
A3:1 C4:.5 B3:.5 E3:2
F3:1 E3:1 C3:1 A2:1
G2:1 D3:1 E3:1 G3:1
A2:1 E3:1 C3:1 R:1
A2:2 E3:1 C3:1
F3:1 A3:1 G3:1 E3:1
G2:1 D3:1 B2:1 C3:1
A2+C3:4
''',
 sections={1:'p',5:'mp',9:'mp',13:'p',17:'pp'},
 words={1:'Let held notes ring; keep the moving voice unhurried.',9:'a little light',13:'as if from another room',19:'poco rit.'},
 slurs=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20)],
 hairpins=[('crescendo',5,6),('diminuendo',7,8),('crescendo',9,10),('diminuendo',11,12),('diminuendo',17,20)],
 tempo_changes={19:57,20:51},group=4)
]

PIECES.extend(NEW_PIECES)
PIECES.extend(DREAM_PIECES)

def parse_rows(s):
    rows=[]
    for row in s.strip().splitlines():
        events=[]
        for tok in row.split():
            pitches,dur=tok.split(':')
            if dur.endswith('~'):pitches+='~';dur=dur[:-1]
            events.append((pitches,float(dur)))
        rows.append(events)
    return rows


def make_score(p):
    sc=stream.Score(id=f'CWS_Op_{p["op"]}')
    md=metadata.Metadata()
    md.title=p['title']
    md.movementName=p['title']
    md.movementNumber=f'CWS Op. {p["op"]}'
    sc.insert(0,md)
    all_events=[]
    parts=[]
    refs={}
    bpb=float(meter.TimeSignature(p['meter']).barDuration.quarterLength)
    for hand in ['rh','lh']:
        held=None
        part=stream.PartStaff(id=hand)
        inst=instrument.Piano()
        inst.partName='Piano' if hand=='rh' else ''
        inst.partAbbreviation=''
        part.insert(0,inst)
        part.partName='Piano' if hand=='rh' else ''
        rows=parse_rows(p[hand])
        assert len(rows)==len(parse_rows(p['rh']))
        for mi,row in enumerate(rows,1):
            assert abs(sum(d for _,d in row)-bpb)<1e-8,(p['title'],hand,mi,row)
            m=stream.Measure(number=mi)
            if mi==1:
                m.insert(0,meter.TimeSignature(p['meter']))
                m.insert(0,key.KeySignature(p['fifths']))
                m.insert(0,clef.TrebleClef() if hand=='rh' else clef.BassClef())
            if hand=='rh':
                if mi==1:
                    compound=p['meter'] in ('6/8','9/8','12/8')
                    beat=duration.Duration(1.5 if compound else 1)
                    mm=tempo.MetronomeMark(number=p['bpm']/(1.5 if compound else 1),referent=beat)
                    mm.placement='above'
                    m.insert(0,mm)
                if mi in p['sections']:
                    dyn=dynamics.Dynamic(p['sections'][mi]); dyn.placement='below';m.insert(0,dyn)
                if mi in p['words'] and p['words'][mi] in ('poco rit.','poco rubato','a tempo'):
                    word=expressions.TextExpression(p['words'][mi]); word.placement='above'; word.style.fontStyle='italic';word.style.fontSize=10
                    m.insert(0,word)
                if (mi-1)%p['group']==0:
                    m.insert(0,layout.SystemLayout(isNew=True))
            offset=0
            refs[(hand,mi)]=[]
            for ei,(ps,dur) in enumerate(row):
                sustain=ps.endswith('~');ps=ps.rstrip('~')
                if ps=='R': n=note.Rest(quarterLength=dur)
                elif '+' in ps: n=chord.Chord(ps.split('+'),quarterLength=dur)
                else: n=note.Note(ps,quarterLength=dur)
                n.id=f'cws{p["op"]}-{hand}-m{mi}-n{ei+1}'
                if held:
                    assert ps!='R' and [x.midi for x in n.pitches]==held['pitches'],('Invalid tie',p['op'],hand,mi,ei)
                    n.id=held['id']+f'-tie-{mi}-{ei+1}'
                    n.tie=tie.Tie('continue' if sustain else 'stop')
                elif sustain:n.tie=tie.Tie('start')
                if p['op']>=7 and isinstance(n,chord.Chord):
                    for pi,cn in enumerate(n.notes):cn.id=n.id+f'-pitch-{pi+1}'
                if ps!='R':
                    refs[(hand,mi)].append(n)
                    pitches=[x.midi for x in n.pitches]
                    if held:
                        held['duration']+=dur
                        event=held
                    else:
                        event=dict(id=n.id,hand=hand,bar=mi,offset=(mi-1)*bpb+offset,duration=dur,pitches=pitches,spellings=[x.nameWithOctave for x in n.pitches])
                        all_events.append(event)
                    held=event if sustain else None
                else:assert not sustain
                m.append(n)
                offset+=dur
            if mi==len(rows):
                refs[(hand,mi)][-1].expressions.append(expressions.Fermata())
                m.rightBarline=bar.Barline('final')
            part.append(m)
        assert held is None,('Unclosed tie',p['op'],hand)
        parts.append(part)
    for start,end in p['slurs']:
        seq=[n for mi in range(start,end+1) for n in refs[('rh',mi)]]
        if seq:
            sl=spanner.Slur(seq[0],seq[-1]);sl.placement='above';parts[0].insert(0,sl)
    # The lower voice gets a phrase arc at its prominent entries.
    lower_phrases=p.get('lower_phrases',[(1,2),(9,10),(17,18)] if p['op']==2 else ([(9,10),(13,14)] if p['op']==3 else [(5,6),(13,14)]))
    for start,end in lower_phrases:
        seq=[n for mi in range(start,end+1) for n in refs[('lh',mi)]]
        sl=spanner.Slur(seq[0],seq[-1]);sl.placement='below';parts[1].insert(0,sl)
    for kind,start,end in p['hairpins']:
        hp=(dynamics.Crescendo if kind=='crescendo' else dynamics.Diminuendo)(refs[('rh',start)][0],refs[('rh',end)][0]);hp.placement='below';parts[0].insert(0,hp)
    for part in parts: sc.insert(0,part)
    sc.insert(0,layout.StaffGroup(parts,symbol='brace',barTogether=True))
    sc.insert(0,layout.ScoreLayout(scalingMillimeters=7,scalingTenths=40))
    return sc,all_events


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--opus',type=int,nargs='+');args=parser.parse_args()
    prior={p['op']:p for p in json.loads((ROOT/'data/catalog.json').read_text())} if (ROOT/'data/catalog.json').exists() else {}
    selected=[p for p in PIECES if args.opus is None or p['op'] in args.opus]
    selected_ops={p['op'] for p in selected}
    catalog=[p for op,p in prior.items() if op not in selected_ops]
    times_path=ROOT/'data/composition_times.json'
    times={p['opus']:p for p in json.loads(times_path.read_text())} if times_path.exists() else {}
    for p in selected:
        folder=OUT/f'CWS_Op_{p["op"]:03d}_{p["title"].replace(" ","_")}'
        folder.mkdir(parents=True,exist_ok=True)
        stem=folder.name
        sc,events=make_score(p)
        xmlpath=folder/(stem+'.musicxml')
        sc.write('musicxml',fp=xmlpath)
        tree=ET.parse(xmlpath)
        root=tree.getroot()
        # Exporter boilerplate is replaced with a clear credit. The catalogue belongs to CWS;
        # the work is explicitly a first AI-assisted compositional study.
        ident=root.find('identification')
        enc=ident.find('encoding') if ident is not None else None
        if enc is not None:
            sw=ET.SubElement(enc,'software');sw.text='CWS Library - first studies with Maple (AI)'
        # Split tied fragments need distinct notation IDs, but remain one sounded onset.
        seen={}
        for n in root.findall('.//part/measure/note'):
            nid=n.get('id')
            if nid:
                seen[nid]=seen.get(nid,0)+1
                if seen[nid]>1:n.set('id',f'{nid}-segment-{seen[nid]}')
            # music21 resets slur numbers for each PartStaff; give the lower
            # staff a disjoint range so consumers never join the two hands.
            if n.findtext('staff')=='2':
                for slur in n.findall('notations/slur'):
                    slur.set('number',str(int(slur.get('number','1'))+8))
            for fermata in n.findall('notations/fermata'):
                fermata.set('type','upright')
        # Only standard tempo directions belong on the printed score. This also
        # removes any tempo adjective automatically inferred by the exporter.
        for measure in root.findall('.//part/measure'):
            for direction in list(measure.findall('direction')):
                for dt in list(direction.findall('direction-type')):
                    for words in list(dt.findall('words')):
                        if words.text not in ('poco rit.','poco rubato','a tempo'):dt.remove(words)
                    if not len(dt):direction.remove(dt)
                if direction.find('direction-type') is None:measure.remove(direction)
        if ident is not None:
            for creator in list(ident.findall('creator')):
                if creator.get('type')=='composer':ident.remove(creator)
        tree.write(xmlpath,encoding='utf-8',xml_declaration=True)
        onset_count=sum(len(e['pitches']) for e in events)
        assert onset_count<=256
        bpb=float(meter.TimeSignature(p['meter']).barDuration.quarterLength)
        entry=dict(prior.get(p['op'],{}))
        entry.update({k:v for k,v in p.items() if k not in ('rh','lh','slurs','subtitle','tempo','words')})
        for field in ['subtitle','tempo','words']:entry.pop(field,None)
        # Keep the existing performance metadata when only engraving changes.
        old_events={e['id']:e for e in prior.get(p['op'],{}).get('events',[])}
        for event in events:
            old=old_events.get(event['id'],{})
            if all(old.get(k)==event[k] for k in ['offset','duration','pitches']):
                for field in ['seconds','end_seconds','velocity']:
                    if field in old:event[field]=old[field]
        if p['op'] not in times:
            now=datetime.now(ZoneInfo(STYLE['composition_timezone']))
            times[p['op']]=dict(opus=p['op'],composition_time=now.isoformat(timespec='seconds'),composition_stamp=now.strftime(STYLE['composition_stamp_format']),source='Recorded when the first score was saved.')
        record=times[p['op']]
        entry.update(folder=folder.name,stem=stem,bars=len(parse_rows(p['rh'])),beats_per_bar=bpb,note_onsets=onset_count,events=events,
                     version=STYLE['format_version'],note_limit=256,page_limit=4,
                     composition_time=record['composition_time'],composition_stamp=record['composition_stamp'],composition_time_source=record['source'])
        (folder/(stem+'.json')).write_text(json.dumps(entry,indent=2)+'\n')
        catalog.append(entry)
        print(p['title'],len(parse_rows(p['rh'])),'bars;',onset_count,'sounded pitch onsets')
    catalog.sort(key=lambda p:p['op'])
    (ROOT/'data/catalog.json').write_text(json.dumps(catalog,indent=2)+'\n')
    times_path.write_text(json.dumps(list(times.values()),indent=2)+'\n')

if __name__=='__main__':main()
