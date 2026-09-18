"""Imaginary Ensembles, Op. 291–320: individually authored two-hand piano works."""
PIECES=[]

def ensemble(*,op,title,key,fifths,meter,bpm,parent,source,motif,rh,lh,description,technical,tempos,phrases,sections,pedal=None,**extras):
    """Shared engraving defaults only; pitches, rhythms and forms are explicit."""
    n=len(rh.strip().splitlines());beats=int(meter.split('/')[0])*4/int(meter.split('/')[1])
    assert len(lh.strip().splitlines())==n and len(tempos)==n
    p=dict(op=op,title=title,key=key,fifths=fifths,meter=meter,bpm=bpm,parent_opus=parent,ancestry=source,motif=motif,rh=rh,lh=lh,
      description=description,difficulty='Advanced chamber study',technical_note=technical,
      technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),
      system_starts=list(range(1,n+1,2)),page_starts=list(range(9,n+1,8)),
      engraving=dict(spacing_system=19,spacing_staff=19,pedal_offset_y=610),
      sections=sections,lower_sections={1:'p'},words={1:'cantabile'},slurs=phrases,lower_phrases=[],hairpins=[],tempo_changes={},group=3,final_fermata=False,
      performance=dict(rubato=tempos,phrase_arcs=[[(a-1)*beats,b*beats,3] for a,b in phrases],lower_entries=[],pedal_lift=.2,gate=.97,note='Authored breathing, changing dialogue and independent voicing; no random timing.'),pedal_spans=pedal or [])
    p.update(extras)
    if p.get('meters'):
        lengths=[int(m.split('/')[0])*4/int(m.split('/')[1]) for m in p['meters']];assert len(lengths)==n
        offsets=[sum(lengths[:i]) for i in range(n+1)]
        p['performance']['phrase_arcs']=[[offsets[a-1],offsets[b],3] for a,b in phrases]
    PIECES.append(p)
    return p

ensemble(op=291,title='Alder Parlour',key='d',fifths=-1,meter='4/4',bpm=54,parent=251,
 source=dict(source_opus=251,source_hand='rh',source_start_beat=.5,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),
 motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['D','F','E','A']),
 description='A cello-like lower voice asks the first question alone. The upper voice answers a bar late, gradually borrowing the bass rhythm. A flat-side conversation opens into warmer sixths; the first question returns under a changed reply and the lower voice takes the final word.',
 technical='Let each hand finish its own sentence. The exposed lower line needs connected finger legato without a heavy bass attack. Voice the upper sixths softly; the few pedal spans colour arrivals without filling the written gaps.',
 rh='''R:4
R:1 A4:1 C5:1 E5:1
D5:2 C5:1 A4:1
G4:1 F4:1 E4:1 R:1
R:2 A4:.5 C5:.5 D5:1
F5:1 E5:.5 D5:.5 C5:2
Bb4:1 A4:1 G4:2
F4:2 R:2
D5:1 F5:1 E5:1 A4:1
C5:2 D5:1 E5:1
F5:1 A5:.5 G5:.5 F5:1 D5:1
C5:2 A4:1 R:1
Bb4:2 D5:1 F5:1
Eb5:1 D5:1 C5:2
Ab4:1 C5:.5 D5:.5 Eb5:2
D5:2 R:2
F4+D5:2 E4+C5:1 D4+Bb4:1
E4+C5:1 F4+D5:1 G4+E5:2
A4+F5:2 G4+E5:1 F4+D5:1
E4+C5:2 R:2
R:1 A4:1 C5:1 E5:1
D5:2 F5:1 E5:1
C5:1 A4:1 G4:1 F4:1
E4:2 R:2
D5:1 C5:.5 A4:.5 F4:2
E4:1 G4:1 A4:2
F4+A4:3 R:1
R:4''',
 lh='''D3:1 F3:1 E3:1 A3:1
G3:2 F3:1 E3:1
Bb2:1 D3:1 F3:2
A2:2 C#3:1 R:1
D3:1 F3:1 E3:1 A3:1
G3:1 Bb3:1 A3:2
G3:1 F3:1 E3:1 C3:1
D3:2 A2:1 R:1
Bb2:2 F3:1 G3:1
A3:1 G3:1 F3:2
D3:2 E3:1 F3:1
G3:1 E3:1 A2:1 R:1
Bb2:1 D3:1 F3:1 A3:1
C3:2 G3:2
Ab2:2 Eb3:1 G3:1
Bb2:1 F3:1 R:2
D3:2 A3:1 G3:1
C3:1 E3:1 G3:2
F3:2 C3:1 D3:1
A2:2 E3:1 R:1
D3:1 F3:1 E3:1 A3:1
Bb3:1 A3:1 G3:1 F3:1
C3:1 G3:1 E3:1 D3:1
A2:2 C#3:1 R:1
Bb2:2 F3:1 A3:1
C3:1 E3:1 G3:2
D3:2 A2:1 R:1
D3:1 F3:.5 E3:.5 D3:2''',
 tempos=[54,54,53,50,54,55,53,49,55,56,57,52,53,54,52,48,55,56,57,51,54,55,53,49,52,51,48,50],
 phrases=[(2,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,27)],
 sections={1:'p',9:'mp',13:'p',17:'mp',21:'p',25:'pp'},lower_sections={1:'mp',3:'p',5:'mp',9:'p',13:'mp',17:'p',21:'mp',25:'pp',28:'p'},
 lower_phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28)],
 hairpins=[('crescendo',17,19),('diminuendo',22,24)],
 pedal=[[32,33.7],[48,49.7],[64,65.7],[72,73.7],[96,97.7],[104,105.7]])

ensemble(op=292,title='Lilac Embassy',key='Eb',fifths=-3,meter='6/4',bpm=66,parent=278,
 source=dict(source_opus=278,source_hand='rh',source_voice='upper',source_start_beat=96,source_end_beat=102,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),
 motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=6,pitches=['Eb','D','C','Bb']),
 description='Two long-breathed lines meet in E-flat. A third voice enters in the middle, at first answering quietly and then redirecting the harmony towards A-flat. It leaves before the reprise, whose final phrase is shared between the original two speakers.',
 technical='Sustain the upper RH line while the inner fingers carry a separate sentence. Keep that moving voice below the melody and hear the bass as another line. The full right hand remains within an octave; clear pedal at each marked release.',
 rh='''Eb5:2 D5:1 C5:1 Bb4:2
G4:2 Bb4:1 C5:2 D5:1
F5:3 Eb5:1 D5:2
C5:2 Bb4:2 R:2
Ab4:3 C5:1 Eb5:2
D5:2 F5:1 Eb5:2 C5:1
Bb4:2 G4:1 Ab4:1 Bb4:2
G4:4 R:2
Bb4:3 C5:3
D5:2 C5:1 Bb4:3
Eb5:3 D5:3
C5:4 Bb4:2
Ab4:3 Bb4:3
C5:3 D5:3
Eb5:2 D5:2 C5:2
Bb4:3 R:3
Eb5:2 D5:1 C5:1 Bb4:2
G4:1 Bb4:1 C5:2 Eb5:2
F5:2 Eb5:1 D5:1 C5:2
Bb4:3 R:3
R:2 Ab4:1 Bb4:1 C5:2
Bb4:2 G4:1 F4:1 Eb4:2
R:3 G4:1 Bb4:2
Eb5:3 R:3''',
 rh_inner='''R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
Eb4:1 G4:1 F4:1 Eb4:1 G4:1 Ab4:1
F4:1 Ab4:1 G4:1 F4:1 G4:1 A4:1
G4:1 Bb4:1 Ab4:1 F4:1 A4:1 C5:1
Eb4:1 G4:1 Bb4:1 Ab4:1 G4:1 F4:1
C4:1 Eb4:1 F4:1 D4:1 F4:1 G4:1
Eb4:1 G4:1 Ab4:1 F4:1 A4:1 C5:1
G4:1 Bb4:1 F4:1 Ab4:1 Eb4:1 G4:1
D4:1 F4:1 Ab4:1 G4:2 R:1
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6''',
 lh='''Eb3:3 G3:1 F3:2
C3:2 Eb3:1 G3:2 Bb3:1
Ab3:2 F3:1 D3:1 Bb2:2
Eb3:1 G3:1 F3:2 R:2
Ab2:2 Eb3:1 G3:1 Ab3:2
Bb2:2 F3:2 A3:2
Eb3:2 G3:1 F3:1 D3:2
Eb3:3 Bb2:1 R:2
C3:3 G3:3
Bb2:2 F3:1 Ab3:3
Ab2:3 Eb3:3
G2:2 D3:2 E3:2
F3:2 Ab3:1 Eb3:3
Ab2:3 Bb2:3
C3:2 Bb2:2 Ab2:2
Bb2:3 Eb3:2 R:1
C3:2 Eb3:1 G3:1 Ab3:2
Ab2:2 Eb3:2 G3:2
Bb2:2 D3:1 F3:1 Ab3:2
Eb3:2 G3:1 R:3
Ab3:2 G3:1 F3:1 Eb3:2
Bb2:2 D3:1 F3:1 G3:2
Eb3:1 G3:1 F3:1 Bb3:3
Eb3:3 Bb2:1 Eb3:2''',
 tempos=[66,67,68,63,65,67,66,61,66,67,68,65,65,67,68,62,65,67,66,61,63,62,61,60],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],sections={1:'p',5:'mp',9:'p',13:'mp',17:'p',21:'pp'},lower_sections={1:'p',5:'mp',9:'pp',13:'p',17:'p',21:'mp',24:'pp'},
 hidden_voice_rests={'inner':list(range(1,9))+list(range(17,25))},
 voice_phrases=[dict(voice='inner',start_beat=48,end_beat=72,swell=3),dict(voice='inner',start_beat=72,end_beat=95,swell=4)],
 lower_phrases=[(1,4),(5,8),(17,20),(21,24)],
 engraving=dict(spacing_system=21,spacing_staff=23,pedal_offset_y=670),
 pedal=[[0,2.8],[24,26.8],[48,50.8],[60,62.8],[72,74.8],[96,98.8],[120,121.8],[138,140.8]])

ensemble(op=293,title='Reed Colonnade',key='a',fifths=0,meter='3/4',bpm=62,parent=291,
 source=dict(source_opus=291,source_hand='lh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=7),
 motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','C','B','E']),
 description='A short upward question passes through a seven-bar dialogue. Neither hand keeps a regular accompaniment: one continues while the other pauses, and their phrases briefly overlap. A more animated C-major exchange leads to a shared answer whose bass is changed on its final return.',
 technical='Carry the three-beat pulse through rests without turning it into a waltz accompaniment. Allow tied upper notes to outlast the lower replies. The closing sixths should sound like two voices agreeing, not an accented chord sequence.',
 rh='''A4:1 C5:.5 B4:.5 E5:1
D5:1 B4:1 R:1
C5:2 E5:1~
E5:2 R:1
R:1 G4:.5 A4:.5 C5:1
B4:1 A4:.5 G4:.5 E4:1
A4:2 R:1
R:3
B4:.5 C5:.5 E5:1 G5:1
F5:1 E5:.5 D5:.5 C5:1
B4:2 R:1
A4:3
G4:.5 C5:.5 E5:.5 G5:.5 A5:1
G5:1 E5:.5 D5:.5 C5:1
F5:1 A5:.5 G5:.5 E5:1
D5:1 C5:1 R:1
R:1 E5:.5 F5:.5 G5:1
E5:1 D5:.5 C5:.5 B4:1
C5:2 B4:1
A4:2 R:1
A4:1 C5:.5 B4:.5 E5:1
D5:2 C5:1
B4:1 G4:1 A4:1
C5:2 R:1
B4:1 A4:1 G#4:1
A4:2 R:1
C5+E5:2 B4+D5:1
A4+C5:1 G4+B4:1 E4+A4:1
D4+G4:1 E4+A4:2
R:3''',
 lh='''A2:2 E3:1
R:1 G3:.5 A3:.5 C4:1
F3:1 E3:1 D3:1
C3:1 E3:.5 G3:.5 B3:1
A3:2 G3:1
E3:1 C3:1 B2:1
A2:1 C3:.5 B2:.5 E3:1
D3:1 B2:1 A2:1
R:1 C3:1 E3:1
D3:1 F3:.5 A3:.5 G3:1
E3:1 G3:.5 F3:.5 E3:1
A2:2 R:1
C3:2 G3:1
E3:1 G3:.5 A3:.5 C4:1
D3:2 A3:1
F3:1 A3:.5 G3:.5 E3:1
D3:1 F3:1 A3:1
G3:2 E3:1
F3:1 E3:1 D3:1
E3:1 B2:1 R:1
F3:2 C3:1
D3:1 F3:1 A3:1
E3:1 G3:1 F3:1
C3:1 E3:1 R:1
B2:1 E3:1 D3:1
C3:1 B2:1 R:1
F3:2 E3:1
D3:1 E3:1 C3:1
B2:1 A2:2
A3:1 C4:.5 B3:.5 A3:1''',
 tempos=[62,61,60,59,62,63,59,60,63,64,60,58,67,68,68,63,67,66,63,59,62,63,61,58,60,58,59,58,56,60],
 phrases=[(1,3),(5,7),(9,12),(13,16),(17,20),(21,24),(25,26),(27,29)],
 sections={1:'p',9:'mp',13:'mf',17:'mp',21:'p',27:'pp'},lower_sections={1:'pp',2:'p',7:'mp',9:'p',13:'mp',17:'mf',21:'p',27:'pp',30:'p'},
 lower_phrases=[(2,4),(5,8),(9,12),(13,16),(17,20),(21,26),(27,30)],
 pedal=[[6,7.8],[33,34.8],[36,37.8],[54,55.8],[78,79.8],[84,86.7]])

ensemble(op=294,title='Willow Consulate',key='G',fifths=1,meter='6/8',bpm=76,parent=288,
 source=dict(source_opus=288,source_hand='rh',source_start_beat=48,source_end_beat=51,source_pitches=['G','F#','E','D'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['G','F#','E','D']),
 description='A light upper voice leaves spaces for a nimble bassoon-like reply. Two unequal conversations lead to a minor-coloured central duet, then the upper voice takes over the bass rhythm. The final exchange gathers into a bright chord rather than dissolving.',
 technical='Keep the paired compound beats elastic and the lower replies articulate. Upper held tones and bass eighth notes need different touch. The short ascending gestures are prepared by rests; the final chord retains the pulse.',
 rh='''G5:.5 F#5:.5 E5:.5 D5:1.5
B4:1.5 R:1.5
R:.5 D5:.5 G5:1 B5:1
A5:1 G5:.5 F#5:1 E5:.5
D5:1.5 R:1.5
G5:1 A5:.5 B5:1 A5:.5
G5:1.5 E5:1 D5:.5
B4:1.5 R:1.5
R:1.5 E5:.5 F#5:.5 G5:.5
A5:1 G5:.5 F#5:1 E5:.5
D5:1 B4:.5 A4:.5 G4:1
A4:1.5 B4:1.5
E5:.5 G5:.5 B5:.5 A5:1 G5:.5
F#5:1.5 E5:1 D5:.5
C5:1 B4:.5 A4:1 G4:.5
F#4:1.5 R:1.5
B4:1 E5:.5 G5:1 F#5:.5
E5:1 D5:.5 B4:1 A4:.5
C5:1.5 B4:1 A4:.5
B4:2 R:1
G4:.5 B4:.5 D5:.5 E5:1 F#5:.5
G5:1 F#5:.5 E5:.5 D5:1
C5:.5 E5:.5 G5:.5 A5:1 G5:.5
F#5:1.5 R:1.5
G5:.5 F#5:.5 E5:.5 D5:1.5
B4:1.5 D5:1 G5:.5
A5:1 B5:.5 G5:1 E5:.5
D5:1.5 R:1.5
B4+D5:1 G4+B4:.5 A4+C5:1 B4+D5:.5
C5+E5:1.5 B4+D5:1 A4+C5:.5
G4+B4:1 A4+C5:.5 B4+D5:1 A4+C5:.5
G4+B4+D5:1.5 R:1.5''',
 lh='''G3:1.5 B3:1 A3:.5
G3:.5 B3:.5 D4:.5 C4:1 B3:.5
E3:1.5 G3:1.5
D3:1.5 A3:1 G3:.5
F#3:.5 A3:.5 C4:.5 B3:1 A3:.5
G3:1.5 D3:1.5
C3:1 G3:.5 A3:1 B3:.5
D3:.5 F#3:.5 A3:.5 G3:1 D3:.5
E3:.5 G3:.5 B3:.5 C4:1 B3:.5
A3:1.5 D3:1.5
G2:1.5 D3:1 E3:.5
F#3:1 A3:.5 G3:1 D3:.5
E3:1.5 B2:1.5
D3:1 F#3:.5 G3:1 A3:.5
C3:1.5 E3:1.5
B2:.5 D#3:.5 F#3:.5 A3:1 F#3:.5
E3:1.5 G3:1.5
C3:1 G3:.5 E3:1 D3:.5
A2:1.5 E3:1 F#3:.5
B2:1 F#3:1 R:1
G3:1.5 R:1.5
R:.5 B3:.5 D4:.5 C4:1 B3:.5
C4:1.5 E3:1.5
D3:.5 F#3:.5 A3:.5 C4:1 A3:.5
E3:1.5 G3:1 F#3:.5
C3:1 E3:.5 G3:1 B3:.5
D3:1.5 F#3:1 A3:.5
G3:.5 B3:.5 A3:.5 G3:1 D3:.5
G2:1.5 D3:1.5
C3:1.5 E3:1.5
D3:1 A3:.5 F#3:1 D3:.5
G2+D3:1.5 R:1.5''',
 tempos=[76,77,78,78,75,77,76,72,75,77,75,73,76,77,75,72,77,78,76,71,78,79,80,74,76,77,78,74,76,77,78,78],
 phrases=[(1,2),(3,5),(6,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32)],sections={1:'p',9:'mp',13:'p',17:'mp',21:'mf',25:'p',29:'mp',32:'mf'},
 lower_sections={1:'p',2:'mp',3:'p',5:'mp',6:'p',8:'mp',13:'p',16:'mp',17:'p',21:'pp',22:'mf',25:'p',28:'mp',32:'mf'},
 lower_phrases=[(1,2),(3,5),(6,8),(9,12),(13,16),(17,20),(22,24),(25,28),(29,32)],pedal=[[36,37.3],[48,49.3],[87,88.3]])

ensemble(op=295,title='Myrtle Rotunda',key='b',fifths=2,meter='5/4',bpm=64,parent=291,
 source=dict(source_opus=291,source_hand='lh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=-3),motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['B','D','C#','F#']),
 description='A five-beat conversation circles B minor, then makes room for a tenor voice over held bass notes. The melody gradually learns the tenor rhythm. A warmer D-major window is followed by an abbreviated return, ending in a quiet B-major sonority.',
 technical='Keep the five beats grouped flexibly across the phrase. In the central trio, sustain the LH bass with one finger while the tenor moves above it; neither line may be replaced by pedal. Balance the final change of third without increasing volume.',
 rh='''B4:2 D5:1 C#5:1 F#5:1
E5:2 D5:1 B4:2
A4:1 C#5:1 E5:2 D5:1
C#5:3 R:2
D5:2 F#5:1 A5:2
G5:1 F#5:1 E5:1 C#5:2
D5:2 B4:1 A4:1 F#4:1
G4:2 F#4:1 R:2
B4:3 C#5:2
D5:2 F#5:1 E5:2
C#5:3 D5:2
E5:2 D5:1 B4:2
D5:3 E5:2
F#5:2 E5:1 D5:2
C#5:2 B4:1 A4:2
F#4:3 R:2
D5:1 F#5:1 A5:1 G5:2
F#5:2 E5:1 D5:2
E5:1 G5:1 F#5:1 D5:2
C#5:3 R:2
B4:2 D5:1 C#5:1 F#5:1
E5:1 D5:1 B4:1 A4:2
G4:2 B4:1 D5:2
C#5:2 B4:1 A#4:2
B4+D#5:3 C#5+E5:2
B4+D#5+F#5:3~ B4+D#5+F#5:2''',
 lh='''B2:2 F#3:1 A3:2
G3:2 E3:1 D3:2
A2:2 E3:1 G3:2
F#2:2 C#3:1 R:2
D3:3 A3:2
C#3:2 G3:1 A3:2
B2:2 F#3:1 D3:2
E3:2 C#3:1 R:2
B2:3~ B2:2
D3:3~ D3:2
C#3:3~ C#3:2
E3:3~ E3:2
G2:3~ G2:2
D3:3~ D3:2
E3:3~ E3:2
F#2:3 R:2
D3:2 A3:1 B3:2
G3:2 D3:1 F#3:2
C#3:2 G3:1 A3:2
F#2:2 C#3:1 R:2
G2:2 D3:1 F#3:2
E3:2 G3:1 F#3:2
E3:1 G3:1 B3:1 A3:2
F#3:2 C#3:1 E3:2
G#2:3 F#2:2
B2+F#3:3~ B2+F#3:2''',
 lh_upper='''R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
F#3:1 A3:1 G#3:1 F#3:2
A3:2 B3:1 A3:1 F#3:1
E3:1 G#3:1 B3:1 A3:2
G3:2 B3:1 D4:2
B2:1 D3:1 F#3:1 E3:2
F#3:2 A3:1 B3:2
G3:1 B3:1 A3:1 G3:2
A#2:1 C#3:1 E3:1 R:2
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5''',
 tempos=[64,65,64,60,66,67,64,59,63,65,64,62,64,66,63,58,68,69,67,60,63,64,62,60,58,56],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,26)],sections={1:'p',5:'mp',9:'p',13:'mp',17:'mf',21:'p',25:'pp'},
 lower_sections={1:'p',5:'mp',9:'p',13:'mp',17:'p',21:'mp',25:'pp'},
 hidden_voice_rests={'tenor':list(range(1,9))+list(range(17,27))},
 voice_phrases=[dict(voice='tenor',start_beat=40,end_beat=60,swell=3),dict(voice='tenor',start_beat=60,end_beat=78,swell=3)],
 page_starts=[9,19],engraving=dict(spacing_system=17,spacing_staff=21,pedal_offset_y=640),
 pedal=[[0,1.8],[20,22.8],[40,42.8],[60,62.8],[80,81.8],[100,101.8],[120,122.8],[125,129.8]])

ensemble(op=296,title='Fern Balcony',key='F',fifths=-1,meter='4/4',bpm=52,parent=292,
 source=dict(source_opus=292,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=6,source_pitches=['Eb','D','C','Bb'],transposition_semitones=2),motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['F','E','D','C']),
 description='A low falling phrase receives an almost canonic answer one bar later. The two voices share a narrow, warm register before the upper line opens out. A six-bar chromatic conversation changes the meaning of the return, which settles on an open D-minor seventh.',
 technical='Keep both lines equally vocal and distinguish their overlapping phrase endings. The middle-register upper melody must stay clear of the left hand. Use the rests as breaths; later dyads require a gentle top voice.',
 rh='''R:4
F4:1 E4:1 D4:1 C4:1
A4:2 G4:1 F4:1
E4:1 G4:1 C5:2
Bb4:2 A4:1 G4:1
F4:1 A4:.5 C5:.5 D5:2
C5:2 Bb4:1 G4:1
A4:3 R:1
F4+A4:2 G4+Bb4:2
A4+C5:3 G4+Bb4:1
F4+A4:1 E4+G4:1 D4+F4:2
E4+G4:2 R:2
Ab4:1 G4:1 F4:1 Eb4:1
D4:2 F4:1 Ab4:1
G4:2 B4:1 D5:1
C5:1 Bb4:1 A4:2
G4:1 F4:.5 E4:.5 D4:2
E4:2 G4:1 R:1
F4:1 E4:1 D4:1 C4:1
A4:2 G4:1 F4:1
E4:1 G4:1 Bb4:2
A4:1 G4:1 F4:1 E4:1
F4:2 A4:1 C5:1
F4+C5:4''',
 lh='''F3:1 E3:1 D3:1 C3:1
A2:2 C3:1 E3:1
D3:1 F3:1 A3:2
C3:2 E3:1 G3:1
Bb2:1 D3:1 F3:2
A2:2 E3:1 F3:1
G3:1 F3:1 E3:1 D3:1
C3:2 F3:1 R:1
D3:1 F3:1 E3:1 A3:1
G3:2 F3:1 E3:1
Bb2:2 F3:1 D3:1
C3:1 E3:1 R:2
F3:2 Ab3:1 C4:1
Bb2:1 D3:1 F3:2
G2:2 D3:1 F3:1
C3:1 E3:1 G3:2
Bb2:2 D3:1 F3:1
C3:2 E3:1 R:1
D3:2 A3:1 G3:1
F3:1 E3:1 D3:1 C3:1
G2:2 D3:1 F3:1
C3:1 E3:1 G3:2
Bb2:1 F3:1 E3:1 C3:1
D3+A3:4''',
 tempos=[52,53,54,53,52,54,52,48,51,53,51,47,50,51,53,54,52,47,51,52,51,50,48,46],
 phrases=[(2,4),(5,8),(9,12),(13,18),(19,22),(23,24)],sections={1:'p',9:'mp',13:'p',15:'mp',19:'p',23:'pp'},lower_sections={1:'mp',2:'p',9:'mp',13:'p',19:'p',20:'mp',23:'pp'},
 lower_phrases=[(1,4),(5,8),(9,12),(13,18),(19,22),(23,24)],
 pedal=[[8,9.8],[16,17.8],[32,33.8],[48,49.8],[56,57.8],[72,73.8],[92,95.8]])

ensemble(op=297,title='Birch Salon',key='Db',fifths=-5,meter='3/2',bpm=58,parent=296,
 source=dict(source_opus=296,source_hand='lh',source_start_beat=0,source_end_beat=4,source_pitches=['F','E','D','C'],transposition_semitones=-4),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Db','C','Bb','Ab']),
 description='A compact, broad-breathed duet in D-flat. The descending song is answered by rising thirds; a brief turn towards the flat seventh changes the room colour. The return compresses the earlier dialogue and leaves the final upper note above an open fifth.',
 technical='Feel three spacious half-note beats while shaping the shorter notes as speech. Balance chord tops against the lower line, and keep the chromatic flat-side passage legato. The final release is measured silence.',
 rh='''Db5:1 C5:1 Bb4:1 Ab4:3
F4:2 Ab4:1 Db5:1 Eb5:2
F5:2 Eb5:1 Db5:1 Bb4:2
Ab4:3 R:3
R:2 Gb4:1 Bb4:1 Db5:2
C5:2 Bb4:1 Ab4:1 F4:2
Ab4+Db5:2 Bb4+Eb5:2 C5+F5:2
Bb4+Eb5:3 Ab4+Db5:1 Gb4+Bb4:2
F4+Ab4:2 Eb4+Gb4:1 Db4+F4:1 Eb4+Gb4:2
F4+Ab4:3 R:3
Cb5:2 Bb4:1 Ab4:1 Gb4:2
Eb4:2 Gb4:1 Bb4:1 Ab4:2
Db5:1 C5:1 Bb4:1 Ab4:3
F4:2 Ab4:1 Db5:1 Eb5:2
F5:2 Eb5:1 Db5:1 C5:2
Db5:4 R:2''',
 lh='''Db3:3 Ab3:3
Bb2:2 F3:1 Ab3:1 Bb3:2
Gb3:2 Db3:1 Eb3:1 F3:2
Ab2:1 C3:1 Eb3:1 Gb3:2 R:1
Gb3:2 F3:1 Eb3:1 Db3:2
Ab2:2 Eb3:1 Gb3:1 Ab3:2
F3:2 Gb3:2 Ab3:2
Bb2:3 F3:1 Gb3:2
Ab2:2 C3:1 Db3:1 Eb3:2
Db3:2 Ab2:1 R:3
Cb3:2 Eb3:1 Gb3:1 Ab3:2
Gb2:2 Db3:1 Eb3:1 F3:2
Bb2:3 F3:3
Gb2:2 Db3:1 F3:1 Ab3:2
Ab2:2 Eb3:1 Gb3:1 Eb3:2
Ab2+Eb3:4 R:2''',
 tempos=[58,59,60,55,57,58,60,61,59,54,56,57,58,59,56,54],
 phrases=[(1,4),(5,6),(7,10),(11,12),(13,16)],sections={1:'p',5:'pp',7:'mp',11:'p',13:'p',16:'pp'},lower_sections={1:'p',4:'mp',5:'p',7:'pp',11:'mp',13:'p',16:'pp'},
 lower_phrases=[(1,4),(5,6),(7,10),(11,12),(13,16)],
 pedal=[[0,2.8],[12,13.8],[36,37.8],[42,44.8],[60,61.8],[72,74.8],[90,93.8]])

ensemble(op=298,title='Sedge Cloister',key='d',fifths=-1,meter='4/4',bpm=60,parent=270,
 source=dict(source_opus=270,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','C','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','C','A','G']),
 description='The voices speak in groups of two full bars and one shortened bar. A hushed D-minor opening becomes a close-register exchange, with the lower hand briefly moving into treble clef. The return remembers that conversation in a lower register and closes with a single shared breath.',
 technical='Keep the quarter-note pulse through each 4/4-to-3/4 change. The central LH treble-clef passage remains in the left hand. Maintain separate phrase lengths and leave the repeated short-bar silences unpedalled.',
 rh='''D5:1 C5:1 A4:1 G4:1
F4:2 A4:1 C5:1
B4:2 R:1
A4:.5 C5:.5 D5:1 F5:2
E5:1 D5:.5 C5:.5 A4:2
G4:2 R:1
Bb4:1 D5:1 F5:1 E5:1
D5:2 C5:1 A4:1
G4:1 F4:1 R:1
E4:1 G4:1 Bb4:2
A4:1 C5:1 E5:2
D5:2 R:1
D5:1 F5:1 E5:1 A4:1
C5:1 B4:1 A4:1 G4:1
F4:1 E4:1 D4:1
G4:.5 B4:.5 D5:1 F5:2
E5:1 D5:1 C5:1 B4:1
A4:2 R:1
D5:1 C5:1 A4:1 G4:1
F4:2 A4:1 D5:1
C5:2 R:1
Bb4:1 A4:.5 G4:.5 F4:2
E4:1 G4:1 A4:2
D4+F4+A4:2 R:1''',
 lh='''D3:2 A3:1 F3:1
C3:1 E3:1 G3:2
G2:1 D3:1 R:1
F3:2 A3:1 G3:1
C3:2 E3:1 G3:1
A2:1 E3:1 R:1
Bb2:2 F3:1 G3:1
A3:1 G3:1 F3:2
D3:1 A2:1 R:1
C3:2 G3:1 F3:1
A2:1 E3:1 G3:2
D3:1 F3:1 R:1
D4:1 F4:1 E4:1 A3:1
C4:1 E4:1 D4:1 B3:1
A3:1 C4:1 B3:1
G3:1 B3:1 D4:1 F4:1
E4:1 D4:1 C4:1 A3:1
A3:1 E4:1 G3:1
Bb2:2 F3:1 A3:1
D3:1 F3:1 A3:2
C3:1 G3:1 R:1
G2:2 D3:1 F3:1
A2:1 E3:1 C#3:2
D3+A3:2 R:1''',
 meters=['4/4','4/4','3/4']*8,
 tempos=[60,61,57,61,62,57,63,62,58,59,61,56,65,66,64,67,65,60,60,61,57,58,56,58],
 phrases=[(1,3),(4,6),(7,9),(10,12),(13,15),(16,18),(19,21),(22,24)],sections={1:'p',7:'mp',10:'pp',13:'mf',16:'mp',19:'p',22:'pp'},
 lower_sections={1:'p',7:'mp',10:'p',13:'mf',19:'p',22:'pp'},
 lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,15),(16,18),(19,21),(22,24)],
 clef_changes={'lh':{1:'bass',13:'treble',19:'bass'}},
 pedal=[[0,1.8],[22,23.8],[33,34.8],[66,67.8],[77,78.8],[85,86.8]])

ensemble(op=299,title='Clover Antechamber',key='Eb',fifths=-3,meter='5/8',bpm=80,parent=292,
 source=dict(source_opus=292,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=6,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=2.5,pitches=['Eb','D','C','Bb']),
 description='A brief, quick-witted exchange in five eighths. One speaker favours short pairs while the other lengthens the last syllable. A few dotted turns bring the first hint of the following jazz group; the final two phrases agree on an open added-ninth colour.',
 technical='Keep the changing two-plus-three and three-plus-two inflections within a single flowing pulse. The bass answers should not become a repeated accompaniment. Release the short rests cleanly and let the final two-handed sonority speak lightly.',
 rh='''Eb5:.5 D5:.5 C5:.5 Bb4:1
G4:.75 Bb4:.25 C5:.5 Eb5:1
F5:1 Eb5:.5 D5:.5 C5:.5
Bb4:.5 G4:.5 F4:.5 Eb4:.5 R:.5
R:1 Bb4:.5 D5:.5 F5:.5
Eb5:1 D5:.5 C5:1
Ab4:.75 C5:.25 D5:.5 F5:1
Eb5:.5 C5:.5 Bb4:.5 G4:1
F4:.5 Ab4:.5 Bb4:.5 D5:.5 C5:.5
Bb4:1.5 R:1
G4+Bb4:1 Ab4+C5:.5 Bb4+D5:1
C5+Eb5:.75 Bb4+D5:.25 Ab4+C5:.5 G4+Bb4:1
F4+Ab4:.5 G4+Bb4:.5 Ab4+C5:.5 Bb4+D5:1
C5+Eb5:1.5 R:1
C5:.5 Eb5:.5 G5:.5 F5:1
Eb5:.75 D5:.25 C5:.5 A4:1
Bb4:.5 D5:.5 F5:.5 Eb5:.5 C5:.5
D5:1.5 R:1
R:.5 Eb5:.5 D5:.5 C5:.5 Bb4:.5
G4:1 Bb4:.5 C5:1
Ab4:.75 C5:.25 Eb5:.5 F5:1
Eb5:1 D5:.5 C5:.5 Bb4:.5
G4:.5 Bb4:.5 D5:.5 C5:.5 Ab4:.5
Bb4:1.5 R:1
Eb5:.5 F5:.5 G5:.5 F5:1
Eb5:.75 D5:.25 C5:.5 Bb4:1
G4:.5 Bb4:.5 C5:.5 D5:.5 Eb5:.5
F4+Bb4:2 R:.5''',
 lh='''Eb3:1 Bb3:.5 G3:1
C3:1 G3:.5 Bb3:1
Ab3:.5 F3:.5 D3:.5 Bb2:1
Eb3:.5 G3:.5 F3:.5 Eb3:.5 R:.5
Bb2:.5 D3:.5 F3:.5 Ab3:1
C3:.5 Eb3:.5 G3:.5 Bb3:1
Ab3:1 F3:.5 D3:1
Eb3:1 G3:.5 Bb3:1
Ab3:.5 F3:.5 D3:.5 F3:.5 G3:.5
Bb2:1.5 R:1
Eb3:1 G3:.5 Bb3:1
Ab3:1 F3:.5 D3:1
Bb2:1 F3:.5 Ab3:1
Eb3:1.5 R:1
C3:1 G3:.5 Bb3:1
F3:.75 A3:.25 C4:.5 Eb4:1
D4:.5 Bb3:.5 Ab3:.5 F3:.5 Eb3:.5
Bb2:1.5 R:1
Eb3:.5 G3:.5 Bb3:.5 Ab3:.5 G3:.5
C3:1 G3:.5 Bb3:1
F3:1 Ab3:.5 C4:1
Bb3:.5 G3:.5 F3:.5 D3:1
Eb3:1 G3:.5 Ab3:1
Bb2:1.5 R:1
C3:1 G3:.5 Bb3:1
Ab3:.5 F3:.5 Eb3:.5 C3:1
Bb2:.5 D3:.5 F3:.5 Ab3:.5 G3:.5
Eb3+G3:2 R:.5''',
 tempos=[80,81,82,78,79,82,83,81,80,76,82,83,84,78,82,84,82,77,80,81,82,81,79,75,81,82,80,78],
 phrases=[(1,4),(5,10),(11,14),(15,18),(19,24),(25,28)],sections={1:'p',5:'mp',11:'p',15:'mf',19:'p',25:'mp',28:'pp'},
 lower_sections={1:'p',5:'mp',11:'pp',15:'p',16:'mf',19:'mp',25:'p',28:'pp'},
 lower_phrases=[(1,4),(5,10),(11,14),(15,18),(19,24),(25,28)],page_starts=[9,19],
 pedal=[[25,25.8],[35,35.8],[60,60.8],[67.5,69.3]])

ensemble(op=300,title='Orchid Assembly',key='C',fifths=0,meter='6/4',bpm=66,parent=292,
 source=dict(source_opus=292,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=6,source_pitches=['Eb','D','C','Bb'],transposition_semitones=-3),motif=dict(hand='rh',voice='upper',start_beat=6,end_beat=12,pitches=['C','B','A','G']),
 description='The opening lower voice calls a small ensemble into being. A delayed upper answer grows into an extended duet; two new middle voices then create an eight-bar quartet. After its crest the extra voices leave, and the original pair finds a more spacious common ending.',
 technical='Give the four central lines separate direction while keeping both hands within an octave at every held instant. The RH melody stays above its moving inner voice; the LH tenor sings over sustained bass. Finger legato, restrained pedal and carefully weighted chord tops are essential.',
 rh='''R:5 G4:1
C5:2 B4:1 A4:1 G4:2
E5:3 D5:1 C5:2
B4:2 A4:2 R:2
G4:1 C5:1 E5:2 D5:2
F5:2 E5:1 D5:1 C5:2
B4:3 D5:1 E5:2
C5:4 R:2
A4:2 C5:1 E5:3
D5:2 F5:1 A5:3
G5:2 E5:1 C5:1 B4:2
A4:3 G4:1 R:2
C5:1 E5:1 G5:2 A5:2
G5:2 F5:1 E5:1 D5:2
F5:1 A5:1 G5:2 E5:2
D5:3 C5:1 R:2
E5:3 D5:3
C5:3 E5:3
F5:2 E5:2 D5:2
B4:3 C5:3
G5:3 F5:3
E5:3 D5:3
C5:2 B4:2 A4:2
G4:4 R:2
C5:2 B4:1 A4:1 G4:2
E5:2 D5:1 C5:1 A4:2
F5:2 E5:1 D5:1 C5:2
B4:3 R:3
E4+G4:2 G4+C5:2 A4+D5:2
G4+C5:3 F4+A4:1 E4+G4:2
D4+F4:2 E4+G4:2 F4+A4:2
E4+G4+C5:4 R:2''',
 rh_inner='''R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
G4:1 C5:1 B4:1 F4:1 A4:1 C5:1
E4:1 G4:1 B4:1 G4:1 C5:1 B4:1
A4:1 C5:1 G4:1 B4:1 F4:1 A4:1
D4:1 F4:1 A4:1 E4:1 G4:1 B4:1
B4:1 D5:1 E5:1 A4:1 C5:1 D5:1
G4:1 B4:1 C5:1 F4:1 A4:1 C5:1
E4:1 G4:1 D4:1 F4:1 C4:1 E4:1
D4:1 F4:1 E4:1 D4:1 R:2
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6''',
 lh='''C3:1 E3:1 D3:1 G3:3
A3:2 G3:1 E3:1 C3:2
F3:2 A3:1 G3:1 E3:2
G2:2 D3:1 F3:1 R:2
E3:3 G3:1 A3:2
D3:2 F3:1 A3:1 C4:2
G3:2 B3:1 A3:1 G3:2
C3:3 E3:1 R:2
F3:2 A3:1 G3:1 E3:2
D3:3 A3:1 C4:2
E3:2 G3:1 A3:1 G3:2
C3:2 G3:1 E3:1 R:2
A2:3 E3:3
D3:2 A3:1 G3:1 F3:2
F3:2 C4:1 B3:1 A3:2
G3:2 D3:1 E3:1 R:2
C3:6
A2:6
F3:6
G2:6
E3:6
F3:6
D3:6
G2:4 R:2
A2:2 E3:1 G3:1 C4:2
F3:2 A3:1 G3:1 E3:2
D3:2 A3:1 F3:1 E3:2
G2:2 D3:1 R:3
C3:2 E3:1 G3:1 B3:2
A3:2 F3:1 D3:1 C3:2
G2:2 D3:2 G3:2
C3+G3:4 R:2''',
 lh_upper='''R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
E3:1 G3:1 A3:1 E3:1 G3:1 B3:1
C3:1 E3:1 G3:1 F3:1 E3:1 C3:1
A3:1 C4:1 B3:1 A3:1 G3:1 A3:1
B2:1 D3:1 F3:1 C3:1 E3:1 G3:1
G3:1 B3:1 D4:1 C4:1 B3:1 G3:1
A3:1 C4:1 D4:1 A3:1 G3:1 A3:1
F3:1 A3:1 G3:1 F3:1 E3:1 F3:1
B2:1 D3:1 F3:1 E3:1 R:2
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6''',
 tempos=[66,66,67,63,68,69,67,62,66,68,67,62,70,71,72,65,68,69,70,68,72,73,69,63,65,66,65,60,63,62,60,58],
 phrases=[(2,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32)],sections={1:'p',5:'mp',9:'p',13:'mp',17:'mp',21:'mf',25:'p',29:'pp'},lower_sections={1:'mp',2:'p',5:'mp',9:'p',13:'mp',17:'p',21:'mp',25:'p',29:'pp'},
 hidden_voice_rests={v:list(range(1,17))+list(range(25,33)) for v in ['inner','tenor']},
 voice_phrases=[dict(voice=v,start_beat=a,end_beat=b,swell=3) for v in ['inner','tenor'] for a,b in [(96,120),(120,142)]],
 lower_phrases=[(1,4),(5,8),(9,12),(13,16),(25,28),(29,32)],
 engraving=dict(spacing_system=22,spacing_staff=26,pedal_offset_y=720),
 hairpins=[('crescendo',17,21),('diminuendo',22,24)],
 pedal=[[12,13.8],[24,26.8],[48,49.8],[72,74.8],[96,98.8],[108,110.8],[120,122.8],[132,133.8],[144,145.8],[168,169.8],[186,189.8]])
