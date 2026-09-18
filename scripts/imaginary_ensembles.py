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

ensemble(op=301,title='Amber Sidewalk',key='F',fifths=-1,meter='4/4',bpm=64,parent=296,
 source=dict(source_opus=296,source_hand='lh',source_start_beat=0,source_end_beat=4,source_pitches=['F','E','D','C'],transposition_semitones=0),motif=dict(hand='rh',start_beat=.5,end_beat=4,pitches=['F','E','D','C']),
 description='A late-entering F-major song leans into soft blue thirds and offbeat chord replies. The melody becomes increasingly conversational, then opens into a four-bar written cadenza. A reharmonised return remembers the opening with fewer notes and a quiet sixth.',
 technical='Keep the dotted turns supple and the LH shell chords lighter than the melody. The cadenza is fully measured: triplets and semiquavers must retain their written proportions while the larger phrase breathes. Clear pedal before each solo rest.',
 rh='''R:.5 F5:.75 E5:.25 D5:.5 C5:2
A4:.75 C5:.25 Eb5:.5 E5:.5 F5:1 R:1
G5:1 F5:.5 D5:.5 C5:1 A4:1
Ab4:.5 A4:.5 C5:2 R:1
R:1 D5:.75 F5:.25 A5:1 G5:1
F5:.5 E5:.5 Eb5:.5 D5:.5 C5:2
Bb4:.75 D5:.25 F5:1 E5:.5 D5:.5 C5:1
A4:2 G4:1 R:1
C5:1 Eb5:.5 E5:.5 G5:1 F5:1
D5:.75 F5:.25 A5:.5 G5:.5 E5:2
Eb5:.5 D5:.5 C5:1 A4:.75 C5:.25 D5:1
G4:2 R:2
A4+C5:1 C5+E5:.5 D5+F5:.5 C5+E5:2
Bb4+D5:1 A4+C5:.5 G4+Bb4:.5 F4+A4:2
Ab4+C5:.75 A4+C5:.25 C5+F5:1 Bb4+E5:2
A4+D5:2 G4+C5:1 R:1
F5:1/3 G5:1/3 A5:1/3 C6:.5 A5:.5 G5:.5 F5:.5 E5:1
D5:1/3 F5:1/3 Ab5:1/3 C6:.5 Bb5:.5 Ab5:.5 G5:.5 F5:1
G4:.25 Bb4:.25 C5:.25 Db5:.25 D5:.25 F5:.25 G5:.25 A5:.25 A5:1 G5:1
G5:.75 E5:.25 D5:.5 C5:.5 Bb4:.5 A4:.5 G4:.5 R:.5
R:.5 F5:.75 E5:.25 D5:.5 C5:2
A4:1 C5:.5 E5:.5 F5:1 D5:1
Bb4:.75 D5:.25 F5:1 E5:.5 D5:.5 C5:1
Ab4:.5 A4:.5 G4:2 R:1
F4:1 A4:1 C5:2
D5:.75 C5:.25 A4:1 G4:2
Ab4:.5 A4:.5 C5:1 G4:1 R:1
F4+D5:3 R:1''',
 lh='''F3:1 R:.5 A3+E4:.5 R:1 G3+C4:1
D3:1 F3+C4:1 R:.5 A3+C4:1.5
Bb2:1 F3+A3:2 G3:1
C3:1 E3+Bb3:1 R:2
D3:1 R:.5 F3+C4:.5 A3:1 C4:1
G3:1 Bb3:1 E3+A3:2
C3:1 E3+Bb3:1 G3:1 Bb3:1
F3:2 C3:1 R:1
A2:1 E3+G3:1 C4:1 G3:1
D3:1 F3+C4:2 E3:1
G3:1 B3:1 F3+A3:2
C3:2 R:2
F3:1 A3:1 E3:1 G3:1
Bb2:1 D3:1 F3:1 A3:1
Ab2:1 Eb3+Gb3:1 G3+Bb3:2
C3:1 E3+Bb3:1 G3:1 R:1
F2+C3:4
R:4
R:4
C3+Bb3:2 R:2
D3:1 A3+C4:1 R:.5 F3+A3:1.5
G3:1 B3+D4:1 A3+C4:2
C3:1 E3+Bb3:2 G3:1
F3:1 A3:1 C3:1 R:1
Bb2:2 F3+A3:2
G2:1 D3+F3:1 E3+G3:2
C3:1 E3+Bb3:1 G3:1 R:1
F3+A3:3 R:1''',
 tempos=[64,66,65,61,66,68,65,61,67,69,66,60,65,66,64,59,62,67,72,58,64,66,65,60,62,61,58,56],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28)],sections={1:'p',5:'mp',9:'mp',13:'p',17:'mp',19:'mf',21:'p',25:'pp'},lower_sections={1:'p',9:'mp',13:'p',17:'pp',21:'p',25:'pp'},
 tuplet_spans=[dict(hand='rh',start_beat=s,end_beat=s+1,actual=3,normal=2,stem='down') for s in [64,68]],
 pedal=[[0,1.8],[8,10.8],[16,17.8],[32,33.8],[48,49.8],[56,57.8],[64,67.8],[76,77.8],[80,81.8],[96,98.8],[108,110.8]])

ensemble(op=302,title='Juniper Wharf',key='Bb',fifths=-2,meter='3/4',bpm=66,parent=301,
 source=dict(source_opus=301,source_hand='rh',source_start_beat=.5,source_end_beat=4,source_pitches=['F','E','D','C'],transposition_semitones=5),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['Bb','A','G','F']),
 description='A slow three-time song drifts across the bar lines above spare jazz voicings. The lower hand unexpectedly takes a two-bar treble-register solo while the upper hand falls silent. A suspended return gathers warmth, then leaves the final melody suspended over a major seventh.',
 technical='Keep the tied melody independent of the sparse bass chords. The short LH cadenza is written in treble clef and played entirely by that hand while the RH rests. Return to the bass register during the written long note, then restore the original gentle pulse.',
 rh='''Bb4:.75 A4:.25 G4:.5 F4:1.5
D5:1 F5:.5 A5:1.5~
A5:1 G5:.5 F5:.5 D5:1
Eb5:2 R:1
R:.5 C5:.5 Eb5:.5 G5:1.5
F5:.75 E5:.25 Eb5:.5 D5:1.5
C5:1 A4:.5 G4:.5 F4:1
G4:2 R:1
D5+F5:1 C5+Eb5:.5 Bb4+D5:1.5
A4+C5:1 Bb4+D5:.5 C5+Eb5:1.5
Db5+F5:1 C5+Eb5:.5 Bb4+Db5:1.5
A4+C5:2 R:1
R:3
R:3
G5:1 F5:.5 D5:.5 C5:1
A4:2 R:1
Bb4:.75 A4:.25 G4:.5 F4:1.5
D5:1 F5:.5 G5:1.5~
G5:1 A5:.5 Bb5:.5 A5:1
F5:2 Eb5:1
D5:.5 F5:.5 A5:.5 G5:.5 F5:1
Eb5:1 D5:.5 C5:.5 Bb4:1
A4:2 C5:1~
C5:2 R:1
D5:1 C5:.5 Bb4:.5 G4:1
F4:.75 G4:.25 A4:.5 C5:1.5
Bb4:1 D5:1 F5:1
Eb5:1 D5:.5 C5:.5 A4:1
Bb4+D5:2 A4+C5:1
D5:2 R:1''',
 lh='''Bb2:1 F3+A3:1.5 R:.5
G3:1 Bb3+D4:1 C4:1
C3:1 G3+Bb3:2
F3:1 A3+Eb4:1 R:1
Eb3:1 Bb3+D4:1 G3:1
A2:1 E3+G3:2
D3:1 F3+C4:1 E3:1
G3:1 B3+F4:1 R:1
Bb2:1 F3+A3:2
Eb3:1 G3+C4:2
Db3:1 Ab3+C4:2
F3:1 A3+Eb4:1 R:1
C4:.25 D4:.25 Eb4:.25 E4:.25 F4:.5 G4:.5 A4:1
Bb4:.25 A4:.25 G4:.25 F4:.25 E4:.5 C4:.5 A3:1
Eb3:1 G3+Bb3:2
F3:1 A3+Eb4:1 R:1
G3:1 D4:1 Bb3:1
Eb3:1 G3+Bb3:2
C3:1 G3+Bb3:2
F3:1 A3+Eb4:2
Bb2:1 F3+A3:2
Eb3:1 G3+Bb3:2
F3:1 A3+Eb4:2
Bb2:1 F3:1 R:1
G3:1 Bb3+D4:2
C3:1 E3+Bb3:2
F3:1 A3+C4:2
Eb3:1 G3+Bb3:2
C3:1 G3+Bb3:2
Bb2+F3+A3:2 R:1''',
 tempos=[66,67,66,61,65,66,64,60,64,66,63,58,55,58,62,59,65,66,68,65,67,65,62,58,63,64,65,61,59,57],
 phrases=[(1,4),(5,8),(9,12),(15,16),(17,20),(21,24),(25,28),(29,30)],sections={1:'p',5:'mp',9:'p',15:'mp',17:'p',21:'mp',25:'p',29:'pp'},lower_sections={1:'p',9:'mp',13:'mf',15:'p',21:'mp',25:'p',29:'pp'},
 lower_phrases=[(13,14)],clef_changes={'lh':{1:'bass',13:'treble',15:'bass'}},
 pedal=[[0,2.3],[6,8.8],[12,14.8],[24,26.8],[30,32.8],[42,44.8],[48,50.8],[54,56.8],[60,62.8],[72,74.8],[87,88.8]])

ensemble(op=303,title='Copper Fen',key='e',fifths=1,meter='5/4',bpm=70,parent=295,
 source=dict(source_opus=295,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['B','D','C#','F#'],transposition_semitones=5),motif=dict(hand='rh',start_beat=0,end_beat=2,pitches=['E','G','F#','B']),
 description='An E-minor improvisation walks unevenly through five beats. Offbeat shell chords support a melody that alternates clipped questions and long answers. Three quintuplet flourishes momentarily loosen the ground; the return introduces Dorian brightness before an open minor ninth.',
 technical='Keep the five-beat pulse audible beneath the displaced chords. The three five-in-four eighth-note figures are measured across two quarter beats and should lead into the longer notes. Avoid overholding the chord replies through written gaps.',
 rh='''E5:.5 G5:.5 F#5:.5 B4:.5 D5:2 C5:1
B4:.75 D5:.25 F#5:1 E5:2 R:1
G5:1 F#5:.5 E5:.5 D5:1 B4:2
A4:1 C5:.5 B4:.5 A4:1 F#4:1 R:1
R:.5 E5:.5 G5:.75 A5:.25 B5:1 A5:1 G5:1
F#5:1 E5:.5 D5:.5 C5:1 A4:2
B4:1 D5:1 F#5:1 A5:1 G5:1
E5:3 R:2
G4+B4:1 B4+D5:1 A4+C5:.5 G4+B4:.5 F#4+A4:2
E4+G4:2 F#4+A4:1 G4+B4:2
A4+C5:.75 B4+D5:.25 D5+F#5:1 C5+E5:1 B4+D5:2
A4+C5:2 F#4+B4:1 R:2
E5:2/5 G5:2/5 A5:2/5 B5:2/5 D6:2/5 C6:1 B5:1 G5:1
D5:2/5 E5:2/5 G5:2/5 A5:2/5 C6:2/5 B5:1 A5:1 G5:1
C5:2/5 E5:2/5 F#5:2/5 A5:2/5 B5:2/5 A5:1 G5:1 E5:1
F#5:.75 G5:.25 A5:.5 B5:.5 A5:1 F#5:1 E5:1
E5:.5 G5:.5 F#5:.5 B4:.5 D5:2 C#5:1
B4:1 D5:.5 F#5:.5 E5:2 R:1
A4:1 C#5:.5 E5:.5 G5:1 F#5:2
D5:1 B4:1 A4:1 F#4:1 R:1
E5:1 D5:.5 B4:.5 G4:2 A4:1
B4:1 D5:.5 F#5:.5 E5:2 D5:1
C#5:1 B4:1 A4:1 F#4:1 R:1
G4+B4+F#5:3 R:2''',
 lh='''E3:1.5 B3+D4:1 R:1 G3+B3:1.5
D3:2 A3+C4:1.5 R:.5 F#3+A3:1
C3:1 G3+B3:2 F#3+A3:1 E3:1
B2:1 F#3+A3:2 D#3:1 R:1
E3:1 G3+D4:1.5 R:.5 B3:2
A2:2 E3+G3:1 C4:1 E3:1
D3:1 F#3+C4:2 A3:1 B3:1
E3+B3:3 R:2
C3:2 G3+B3:1 A3:1 F#3:1
D3:1 A3+C4:1 F#3:1 E3+G3:2
A2:1 E3+G3:2 B3:1 A3:1
B2:1 F#3+A3:2 R:2
E2+B2:3~ E2+B2:2
C3+G3:3~ C3+G3:2
A2+E3:3~ A2+E3:2
B2:2 F#3+A3:2 E3:1
C#3:1 G3+B3:2 A3:1 G3:1
D3:1 F#3+C4:2 E3:1 R:1
A2:2 E3+G3:1 C#4:1 E3:1
B2:1 F#3+A3:2 D#3:1 R:1
C3:2 G3+B3:1 A3:1 G3:1
D3:1 A3+C4:2 F#3:1 E3:1
B2:1 F#3+A3:2 D#3:1 R:1
E3+B3:3 R:2''',
 tempos=[70,72,71,66,73,74,72,66,69,71,72,65,66,69,73,67,70,72,73,66,68,69,65,62],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],sections={1:'p',5:'mp',9:'p',13:'mp',15:'mf',17:'p',21:'pp'},lower_sections={1:'p',5:'mp',9:'p',13:'pp',17:'p',21:'pp'},
 tuplet_spans=[dict(hand='rh',start_beat=s,end_beat=s+2,actual=5,normal=4,stem='down',show_number='both') for s in [60,65,70]],
 pedal=[[0,2.3],[10,12.8],[20,22.3],[40,42.8],[60,64.8],[65,69.8],[70,74.8],[80,82.8],[100,102.8],[115,117.8]])

ensemble(op=304,title='Moss Slipway',key='Db',fifths=-5,meter='4/4',bpm=52,parent=297,
 source=dict(source_opus=297,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['Db','C','Bb','Ab'],transposition_semitones=0),motif=dict(hand='rh',start_beat=20,end_beat=24,pitches=['Db','C','Bb','Ab']),
 description='A D-flat improvisation begins halfway into a thought. Chromatic neighbours soften the melody before its borrowed descending phrase finally appears. A brief flourish moves from one hand to the other; the return is reduced to a few chord tops and a warm major ninth.',
 technical='Give the late entries and chromatic approaches a natural spoken shape. Match the tone of the two alternating semiquaver flourishes while keeping the resting hand silent. Project the top line of the final chords without thickening the sound.',
 rh='''R:1 Ab4:.75 C5:.25 Eb5:2
Db5:1 C5:.5 Bb4:.5 Ab4:2
F4:.5 Fb4:.5 Eb4:1 Ab4:2
Gb4:1 Bb4:.5 Db5:.5 C5:1 Bb4:1
Ab4:2 R:2
Db5:.75 C5:.25 Bb4:.5 Ab4:2.5
F5:1 Eb5:.5 Db5:.5 C5:2
Bb4:.75 Db5:.25 F5:1 Eb5:1 C5:1
Ab4:2 Gb4:1 R:1
F4+Ab4:1 Ab4+Db5:1 Bb4+Eb5:2
Ab4:.25 Bb4:.25 C5:.25 Db5:.25 Eb5:.25 F5:.25 Gb5:.25 Ab5:.25 F5:2
R:4
Db5+F5:1 C5+Eb5:1 Bb4+Db5:2
Ab4+C5:1 Gb4+Bb4:1 F4+Ab4:2
Fb4+Ab4:1 Gb4+Bb4:.5 Ab4+Cb5:.5 Bb4+Db5:2
Ab4+C5:2 R:2
Db5:1 C5:.5 Bb4:.5 Ab4:2
F4:1 Ab4:.5 C5:.5 Eb5:2
Db5:1 Bb4:1 Ab4:.75 Gb4:.25 F4:1
F4+Ab4+Eb5:3 R:1''',
 lh='''Bb2:1 F3+Ab3:1.5 R:.5 Db3+F3:1
Eb3:1 Bb3+Db4:1 Ab3:2
Ab2:1 Eb3+Gb3:2 Db3:1
Gb2:1 Db3+F3:1 Eb3:1 Ab3:1
Db3:2 R:2
Bb2:1 F3+Ab3:2 C3:1
Gb2:1 Db3+F3:2 Ab3:1
Eb3:1 Bb3+Db4:2 Gb3:1
Ab2:1 Eb3+Gb3:1 C3:1 R:1
Db3:2 Ab3+C4:2
Bb2+F3:4
Eb3:.25 Gb3:.25 Ab3:.25 A3:.25 Bb3:.25 Db4:.25 C4:.25 Bb3:.25 Ab3:2
Gb3:1 Bb3:1 Db3+F3:2
Eb3:1 Bb3+Db4:1 Ab3:2
Cb3:1 Gb3+Bb3:1 Eb3:1 Gb3:1
Ab2:1 Eb3+Gb3:1 R:2
Bb2:1 F3+Ab3:1 Db3:2
Eb3:1 Bb3+Db4:2 Ab3:1
Gb2:1 Db3+F3:1 Ab2:1 Eb3+Gb3:1
Db3+Ab3:3 R:1''',
 tempos=[52,54,51,53,48,53,55,54,49,52,58,56,54,53,51,47,51,53,49,46],
 phrases=[(1,5),(6,9),(10,11),(13,16),(17,20)],sections={1:'p',6:'mp',10:'p',11:'mf',13:'mp',17:'p',20:'pp'},lower_sections={1:'p',6:'mp',10:'p',12:'mf',13:'p',17:'pp'},
 lower_phrases=[(12,12)],page_starts=[9,15],
 pedal=[[0,1.8],[8,10.8],[20,22.8],[24,26.8],[40,43.8],[48,49.8],[56,57.8],[64,65.8],[76,78.8]])

ensemble(op=305,title='Hazel Switchyard',key='A',fifths=3,meter='3/4',bpm=68,parent=294,
 source=dict(source_opus=294,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['G','F#','E','D'],transposition_semitones=2),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','G#','F#','E']),
 description='A compact jazz conversation tilts into a left-hand current of seven notes across three beats. The melody floats above that uneven ground before the hands exchange short chromatic questions. A brighter reprise gives way to one unaccompanied fragment.',
 technical='Practise the four seven-against-six groups slowly, hearing the three-quarter pulse through the whole bar. Keep the sustained melody above their shimmer. The returning offbeat chords need a lighter touch than the solo line.',
 rh='''A4:.5 G#4:.5 F#4:1 E4:1
C#5:1 B4:.5 A4:.5 G#4:1
F#4:.75 A4:.25 C#5:1 B4:1
G#4:2 R:1
E5:1 D#5:.5 C#5:.5 B4:1
A4:1 C5:.5 C#5:.5 E5:1
D5:1 C#5:.5 B4:.5 A4:1
G#4:1 F#4:1 R:1
A4:3
B4:2 A4:1
C#5:3
D5:2 B4:1
R:1 A4:.5 C#5:.5 E5:1
D5:.75 F5:.25 F#5:1 E5:1
C#5:1 B4:.5 A4:.5 G#4:1
F#4:2 R:1
R:3
E4:.5 F#4:.5 G#4:1 B4:1
C5:.5 C#5:.5 E5:1 D5:1
B4:1 G#4:1 R:1
A4+C#5:1 G#4+B4:1 F#4+A4:1
E4+G#4:1 F#4+A4:.5 G#4+B4:.5 A4+C#5:1
B4+D5:1 A4+C#5:1 G#4+B4:1
F#4+A4:2 R:1
A4:.5 G#4:.5 F#4:1 E4:1
C#5:1 B4:.5 A4:.5 F#4:1
G#4+B4:2 R:1
A4:1 G#4:.5 F#4:.5 E4:1''',
 lh='''A2:1 E3+G#3:1 C#3:1
F#2:1 C#3+E3:1 R:1
D3:1 F#3+A3:1 B3:1
E3:1 G#3+D4:1 R:1
C#3:1 G#3+B3:1 E3:1
F#3:1 A3+C#4:1 R:1
D3:1 F#3+B3:1 E3:1
E3+B3:2 R:1
A2:3/7 C#3:3/7 E3:3/7 G#3:3/7 F#3:3/7 E3:3/7 C#3:3/7
F#2:3/7 A2:3/7 C#3:3/7 E3:3/7 D3:3/7 C#3:3/7 A2:3/7
D3:3/7 F#3:3/7 A3:3/7 C#4:3/7 B3:3/7 A3:3/7 F#3:3/7
E3:3/7 G#3:3/7 B3:3/7 D4:3/7 C#4:3/7 B3:3/7 G#3:3/7
F#3:1 A3+C#4:1 R:1
B2:1 F#3+A3:1 D3:1
E3:1 G#3+B3:1 E3:1
F#3+C#4:2 R:1
D3:.5 F#3:.5 A3:.5 C4:.5 C#4:1
B3:1 G#3:1 E3:1
A2:1 E3+G3:1 C#3:1
E3:1 G#3+D4:1 R:1
F#3:1 A3+C#4:1 R:1
C#3:1 G#3+B3:1 E3:1
D3:1 F#3+A3:1 E3:1
B2:1 F#3+A3:1 R:1
A2:1 E3+G#3:1 C#3:1
D3:1 F#3+A3:1 B3:1
E3:1 G#3+D4:1 R:1
R:3''',
 tempos=[68,69,70,64,70,72,70,63,66,68,70,66,71,73,70,65,69,70,73,65,72,74,71,66,69,70,65,68],
 phrases=[(1,4),(5,8),(9,12),(13,16),(18,20),(21,24),(25,28)],sections={1:'p',5:'mp',9:'p',13:'mp',18:'p',21:'mf',25:'p'},lower_sections={1:'p',9:'pp',13:'p',17:'mp',21:'p',25:'pp'},lower_phrases=[(17,20)],
 tuplet_spans=[dict(hand='lh',start_beat=s,end_beat=s+3,actual=7,normal=6,stem='up',show_number='both') for s in [24,27,30,33]],
 pedal=[[0,1.8],[12,13.8],[24,26.8],[27,29.8],[30,32.8],[33,35.8],[60,61.8],[72,73.8]])

ensemble(op=306,title='Iris Backwater',key='g',fifths=-2,meter='6/4',bpm=62,parent=298,
 source=dict(source_opus=298,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','C','A','G'],transposition_semitones=5),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['G','F','D','C']),
 description='A long minor-key ballad moves in phrases of three, five and six bars. The melody stretches across an unhurried bass, then falls silent for an ascending left-hand soliloquy. Its return has lighter harmony and ends on the sixth, leaving a little daylight in the water.',
 technical='Shape the long melody independently of each bass arrival. The left-hand treble solo should sing without added pedal haze. Preserve the rests at the phrase ends and the clear top notes of the returning chord pairs.',
 rh='''G4:1 F4:1 D4:2 C4:2
D4:2 G4:1 A4:1 Bb4:2
A4:2 F4:2 R:2
R:1 D5:2 C5:1 Bb4:2
A4:1 C5:.5 D5:.5 F5:2 Eb5:2
D5:3 C5:1 A4:2
Bb4:2 G4:1 F4:1 Eb4:2
D4:3 R:3
G4:2 Bb4:1 D5:3
C5:2 Eb5:1 G5:2 F5:1
D5:1 F5:.5 Eb5:.5 D5:1 C5:1 Bb4:2
A4:2 F#4:2 R:2
R:6
R:6
G4+Bb4:2 F4+A4:1 D4+G4:3
Eb4+G4:2 G4+Bb4:1 A4+C5:3
Bb4+D5:3 A4+C5:1 G4+Bb4:2
F4+A4:1 Eb4+G4:1 D4+F4:2 R:2
G4:1 A4:.5 Bb4:.5 D5:2 C5:2
Bb4:2 A4:1 G4:3
F4:2 D4:1 Eb4:1 G4:2
A4:3 Bb4:1 D5:2
C5:1 A4:1 G4:2 F4:1 D4:1
G4+Bb4+E5:4 R:2''',
 lh='''G2:2 D3:1 F3:2 Bb3:1
Eb3:2 Bb3+D4:1 G3:3
F3:2 A3+C4:2 R:2
Bb2:1 F3+A3:2 C3:1 D3:2
Eb3:2 G3+Bb3:2 A3:2
F3:1 A3+Eb4:2 C4:1 D3:2
C3:2 G3+Bb3:1 F3:1 Eb3:2
D3:2 A3+C4:1 R:3
G2:2 D3+F3:2 Bb3:2
Ab3:2 C4+Eb4:2 Bb3:2
G3:2 Bb3+D4:1 Eb3:1 F3:2
D3:2 A3+C4:2 R:2
D4:.5 F4:.5 G4:1 Bb4:.5 A4:.5 G4:1 F4:2
Eb4:1 G4:.5 A4:.5 Bb4:1 D5:.5 C5:.5 A4:1 F#4:1
G3:2 D4:1 Bb3:3
C3:2 G3:1 Bb3:3
Eb3:2 Bb3:1 F3:1 G3:2
F3:2 A3+C4:2 R:2
Eb3:2 Bb3+D4:2 G3:2
C3:2 G3+Bb3:2 E3:2
D3:2 A3+C4:2 Bb3:2
Eb3:3 G3:1 Bb3:2
F3:2 A3+C4:2 D3:2
G2+D3:4 R:2''',
 tempos=[62,64,59,61,64,65,61,56,64,66,68,59,66,68,61,63,65,58,63,62,60,63,61,57],
 phrases=[(1,3),(4,8),(9,12),(15,19),(20,24)],lower_phrases=[(13,14)],sections={1:'p',4:'mp',9:'mf',15:'p',19:'mp',24:'pp'},lower_sections={1:'pp',4:'p',9:'mp',13:'mf',15:'p',20:'pp'},clef_changes={'lh':{1:'bass',13:'treble',15:'bass'}},
 pedal=[[0,2.8],[18,20.8],[30,32.8],[48,51.8],[54,57.8],[84,86.8],[90,92.8],[114,117.8],[126,128.8],[138,141.8]])

ensemble(op=307,title='Linden Signal',key='Eb',fifths=-3,meter='4/4',bpm=76,parent=299,
 source=dict(source_opus=299,source_hand='rh',source_start_beat=0,source_end_beat=2.5,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),motif=dict(hand='rh',start_beat=.5,end_beat=4,pitches=['Eb','D','C','Bb']),
 description='A quick, soft signal travels between melody and clipped jazz chords. Three bars of unaccompanied semiquavers briefly enlarge the space; their last turn becomes the answering bass figure. The reprise is interrupted once more, and ends with a small, decisive reply.',
 technical='Keep the semiquaver cadenza even enough to read but shaped as one sentence. Release the short chords together and let the melody remain distinct from the accompanying replies. The final rest is part of the cadence.',
 rh='''R:.5 Eb5:.5 D5:1 C5:1 Bb4:1
G4:1 Bb4:.5 C5:.5 D5:1 F5:1
Eb5:1 D5:.5 C5:.5 Bb4:1 R:1
G4+Bb4+D5:1 R:1 F4+A4+C5:1 R:1
C5:.75 Eb5:.25 G5:1 F5:.5 Eb5:.5 D5:1
Bb4:1 Db5:.5 D5:.5 F5:2
Eb5:1 C5:.5 Bb4:.5 Ab4:1 G4:1
F4+Ab4+C5:2 R:2
Eb4:.25 F4:.25 G4:.25 Bb4:.25 C5:.25 D5:.25 Eb5:.25 F5:.25 G5:.5 F5:.5 Eb5:1
D5:.25 Eb5:.25 F5:.25 Ab5:.25 G5:.25 F5:.25 Eb5:.25 D5:.25 C5:.5 Bb4:.5 Ab4:1
G4:.25 Ab4:.25 A4:.25 Bb4:.25 D5:.25 C5:.25 Bb4:.25 Ab4:.25 G4:1 R:1
R:4
Bb4+Eb5:1 Ab4+D5:1 G4+C5:1 F4+Bb4:1
Eb4+G4:1 R:.5 F4+Ab4:.5 G4+Bb4:2
Ab4+C5:1 G4+Bb4:.5 F4+Ab4:.5 Eb4+G4:1 R:1
D4+F4+A4:2 R:2
R:.5 Eb5:.5 D5:1 C5:1 Bb4:1
G4:1 Bb4:.5 D5:.5 F5:1 Eb5:1
C5:1 Ab4:1 Bb4:.5 G4:.5 F4:1
G4+Bb4+D5:1 R:3
R:2 G4:.5 Bb4:.5 C5:1
D5:1 F5:.5 Eb5:.5 C5:1 Ab4:1
G4:1 Bb4:.5 D5:.5 Eb5:1 F5:1
G4+Bb4+Eb5:1 R:3''',
 lh='''Eb3:1 Bb3+D4:1 R:1 G3+Bb3:1
C3:1 G3+Bb3:1 F3:1 R:1
Ab2:1 Eb3+G3:1 Bb2:1 F3+Ab3:1
Eb3:1 R:1 D3:1 R:1
Ab2:1 Eb3+G3:2 Bb3:1
Bb2:1 F3+Ab3:1 D3:2
C3:1 G3+Bb3:1 Ab3:1 Eb3:1
Bb2:1 F3+Ab3:1 R:2
R:4
R:4
R:4
Eb3:.5 G3:.5 Bb3:.5 C4:.5 Db4:.5 C4:.5 Bb3:1
Ab3:1 F3:1 Eb3:1 D3:1
C3:1 G3+Bb3:1 Eb3:2
F3:1 C4:1 Ab3:1 R:1
Bb2:1 F3+Ab3:1 R:2
Eb3:1 Bb3+D4:1 R:1 G3+Bb3:1
C3:1 G3+Bb3:1 Ab3:1 F3:1
Bb2:1 F3+Ab3:1 D3:1 F3:1
Eb3:1 R:3
C3:.5 Eb3:.5 G3:1 Bb3:1 Ab3:1
F3:1 A3+Eb4:1 Bb3:1 F3:1
Bb2:1 F3+Ab3:1 C3:1 D3:1
Eb3+Bb3:1 R:3''',
 tempos=[76,78,75,72,79,80,77,70,82,84,79,77,78,79,76,70,76,78,75,69,74,77,79,76],phrases=[(1,3),(5,8),(9,11),(13,16),(17,19),(21,24)],lower_phrases=[(12,12),(21,23)],sections={1:'p',4:'mp',5:'p',9:'mf',13:'mp',17:'p',21:'pp',24:'mp'},lower_sections={1:'pp',4:'mp',5:'p',12:'mf',13:'p',17:'pp',21:'mp',24:'mp'},
 pedal=[[0,1.8],[16,18.8],[48,49.8],[52,54.8],[64,65.8],[84,85.8]])

ensemble(op=308,title='Reed Atrium',key='f#',fifths=3,meter='4/4',bpm=60,parent=303,
 source=dict(source_opus=303,source_hand='rh',source_start_beat=0,source_end_beat=2,source_pitches=['E','G','F#','B'],transposition_semitones=2),motif=dict(hand='rh',start_beat=.5,end_beat=4,pitches=['F#','A','G#','C#']),
 description='A quiet F-sharp-minor improvisation changes the length of its breath: four beats, four, three, then five. The bass interrupts the first thought, the melody answers with a small quintuplet flourish, and the final page loosens the same idea into a Dorian afterglow.',
 technical='Let the changing metre follow the sentence rather than accenting every new bar. Balance the offbeat chord replies against the single line. The quintuplet occupies precisely two quarter beats; its continuation should remain relaxed.',
 rh='''R:.5 F#4:.5 A4:.75 G#4:.25 C#5:2
B4:1 A4:.5 G#4:.5 E4:2
F#4:1 A4:1 B4:1
C#5:2 B4:1 G#4:1 R:1
A4:1 C#5:.5 E5:.5 D5:2
C#5:1 B4:.5 A4:.5 G#4:2
F#4:2 R:1
R:2 E4:1 G#4:1 B4:1
C#5:1 E5:1 F#5:2
E5:1 D5:.5 C#5:.5 B4:1 A4:1
G#4:2 R:1
C#5:2/5 D5:2/5 E5:2/5 F#5:2/5 G#5:2/5 A5:1 E5:1 C#5:1
B4+D5:1 A4+C#5:1 G#4+B4:2
F#4+A4:1 E4+G#4:1 D4+F#4:2
E4+G#4:1 F#4+A4:1 G#4+B4:1
A4+C#5:2 R:1 G#4:1 E4:1
F#4:1 A4:.5 G#4:.5 C#5:2
B4:1 D#5:1 E5:1 C#5:1
A4:1 G#4:1 F#4:1
E4:2 G#4:1 B4:1 R:1
C#5:1 B4:.5 A4:.5 G#4:2
F#4:2 E4:1 D#4:1
G#4:1 A4:1 C#5:1
F#4+A4+C#5:3 R:2''',
 lh='''F#2:1 C#3+E3:1.5 R:.5 A3:1
D3:1 A3+C#4:1 E3:2
B2:1 F#3+A3:1 E3:1
C#3:2 G#3+B3:1 E#3:1 R:1
D3:1 A3+C#4:1 B3:2
E3:1 G#3+D4:1 B3:2
F#3:1 C#4:1 R:1
D3:.5 F#3:.5 A3:1 C4:1 B3:1 G#3:1
A2:1 E3+G#3:1 C#3:2
D3:1 A3+C#4:2 E3:1
C#3:1 G#3+B3:1 R:1
F#3+C#4:3~ F#3+C#4:2
B2:1 F#3+A3:1 E3:2
D3:1 A3+C#4:1 F#3:2
E3:1 B3+D4:1 C#4:1
F#3:2 R:1 E3:1 C#3:1
F#2:1 C#3+E3:2 A3:1
B2:1 F#3+A3:1 G#3:1 E3:1
D#3:1 A3+C#4:1 B3:1
E3:2 B3+D4:1 G#3:1 R:1
D3:1 A3+C#4:1 B3:2
B2:1 F#3+A3:1 G#3:1 A3:1
C#3:1 G#3+B3:1 E#3:1
F#3+C#4:3 R:2''',
 meters=['4/4','4/4','3/4','5/4']*6,tempos=[60,62,61,58,64,63,57,61,65,66,59,67,63,62,64,58,61,64,65,60,61,59,62,57],
 phrases=[(1,4),(5,7),(8,12),(13,16),(17,20),(21,24)],lower_phrases=[(8,8)],sections={1:'p',5:'mp',8:'p',9:'mp',12:'mf',13:'mp',17:'p',21:'pp'},lower_sections={1:'pp',5:'p',8:'mp',9:'p',12:'pp',13:'p',17:'pp'},tuplet_spans=[dict(hand='rh',start_beat=43,end_beat=45,actual=5,normal=4,stem='down',show_number='both')],
 pedal=[[0,2.3],[16,17.8],[32,33.8],[43,47.8],[48,49.8],[64,66.8],[80,81.8],[91,93.8]])

ensemble(op=309,title='Saffron Overpass',key='C',fifths=0,meter='7/8',bpm=74,parent=300,
 source=dict(source_opus=300,source_hand='rh',source_voice='upper',source_start_beat=6,source_end_beat=12,source_pitches=['C','B','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3.5,pitches=['C','B','A','G']),
 description='Seven eighths become a lightly lopsided jazz dance. A descending signal is interrupted by bright sixths and dry chord replies; the central passage strips away the bass, then rebuilds the pulse from the other hand. The last phrase opens onto a major sixth and ninth.',
 technical='Keep the uneven pulse supple, with the long group changing its expressive weight. The brief solo bars need the same underlying momentum as the chord passages. Voice the upper notes of the sixths without accenting every chord.',
 rh='''C5:1 B4:.5 A4:1 G4:1
E5:1.5 D5:.5 B4:.5 G4:1
A4:.5 C5:.5 E5:1 D5:1 R:.5
B4:1 G4:1 E4:1 R:.5
F4+A4:1 G4+B4:.5 A4+C5:1 B4+D5:1
C5+E5:1.5 B4+D5:.5 A4+C5:.5 G4+B4:1
F4+A4:1 E4+G4:1 D4+F4:1 R:.5
E4+G4+B4:2 R:1.5
G4:.5 A4:.5 Bb4:.5 B4:1 D5:1
E5:1 G5:.5 F5:1 D5:1
C5:.5 B4:.5 A4:.5 G4:1 E4:1
F4:1 A4:1 C5:1 R:.5
D5:.25 E5:.25 F5:.25 G5:.25 A5:.5 G5:.5 E5:.5 D5:1
C5:.5 A4:.5 G4:.5 E4:1 R:1
R:3.5
R:3.5
A4+C5:1 B4+D5:.5 C5+E5:1 D5+F5:1
E5+G5:1.5 D5+F5:.5 C5+E5:.5 B4+D5:1
A4+C5:1 G4+B4:1 F4+A4:1 R:.5
E4+G4+B4:2 R:1.5
C5:1 B4:.5 A4:1 G4:1
E5:1.5 D5:.5 C5:.5 A4:1
F4:1 A4:.5 C5:1 E5:1
D5:1 B4:1 G4:1 R:.5
A4:1 C5:.5 D5:1 F5:1
E5:1 D5:.5 B4:1 G4:1
A4:1 B4:.5 C5:.5 D5:.5 E5:1
E4+A4+D5:3 R:.5''',
 lh='''C3:1 G3+B3:.5 R:.5 E3+G3:1 R:.5
A2:1 E3+G3:.5 C3:1 D3:1
F3:1 C4:1 A3:1 R:.5
G3:1 B3+D4:1 F3:1 R:.5
D3:1 A3+C4:.5 R:.5 F3+A3:1 R:.5
G3:1 B3+F4:.5 D4:1 G3:1
A2:1 E3+G3:1 B3:1 R:.5
C3:1 G3:1 R:1.5
Eb3:1 Bb3:.5 G3:1 F3:1
F3:1 A3+C4:.5 E3:1 D3:1
C3:1 G3+B3:.5 A3:1 E3:1
D3:1 A3+C4:1 F3:1 R:.5
R:3.5
R:3.5
F3:.5 A3:.5 C4:.5 E4:1 D4:1
B3:.5 A3:.5 G3:.5 E3:1 D3:1
F3:1 C4:.5 R:.5 A3:1 R:.5
G3:1 D4:.5 B3:1 G3:1
A3:1 E3:1 F3:1 R:.5
C3:1 G3:1 R:1.5
C3:1 G3+B3:.5 R:.5 E3+G3:1 R:.5
A2:1 E3+G3:.5 C3:1 D3:1
F3:1 C4:.5 A3:1 G3:1
G3:1 B3+D4:1 F3:1 R:.5
D3:1 A3+C4:.5 E3:1 F3:1
G3:1 B3+D4:.5 F3:1 E3:1
F3:1 C4:.5 G3:1 B3:1
C3+G3:3 R:.5''',
 tempos=[74,76,77,72,76,78,76,70,78,80,78,74,82,78,76,75,79,81,78,71,75,77,79,73,77,78,80,74],phrases=[(1,4),(5,8),(9,12),(13,14),(17,20),(21,24),(25,28)],lower_phrases=[(15,16)],sections={1:'p',5:'mp',9:'p',13:'mf',17:'mp',21:'p',25:'mf'},lower_sections={1:'pp',5:'p',9:'pp',15:'mf',17:'p',21:'pp',25:'mp'},page_starts=[9,19],engraving=dict(spacing_system=17,spacing_staff=19,pedal_offset_y=610),
 pedal=[[0,1.3],[14,15.3],[28,29.3],[56,57.3],[70,71.3],[94.5,97.3]])

ensemble(op=310,title='Velvet Passage',key='d',fifths=-1,meter='4/4',bpm=58,parent=291,
 source=dict(source_opus=291,source_hand='lh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['D','F','E','A']),
 description='The first conversation returns as a through-composed nocturnal passage. A bass question gathers a broken upper melody, opens into a sequence of quiet solo chords, and then exchanges roles with a rising lower line. The broadest agreement arrives late; the melody walks away alone.',
 technical='Maintain the difference between bass solo, melody and chord choir. Connect the chord tops with the fingers where possible, without sustaining through the written gaps. The late crescendo needs room to expand while the final single line stays unforced.',
 rh='''R:4
R:2 C5:1 F5:1
E5:1 D5:.5 C5:.5 A4:2
G4:1 A4:.75 C5:.25 E5:2
D5:2 R:2
F5:1 E5:.5 D5:.5 C5:1 A4:1
Bb4:2 A4:1 F4:1
E4:1 G4:.5 A4:.5 C5:2
D5:1 F5:.5 A5:.5 G5:1 E5:1
F5:2 C5:1 A4:1
G4:1 Bb4:.5 D5:.5 C5:1 A4:1
G4:2 R:2
R:1 A4:1 C5:1 E5:1
F4+A4+D5:1 E4+G4+C5:1 D4+F4+Bb4:2
Eb4+G4+Bb4:1 F4+Ab4+C5:1 G4+Bb4+D5:2
F4+A4+C5:2 R:2
R:4
R:2 A4:1 C5:1
D5:2 E5:.5 F5:.5 A5:1
G5:1 E5:1 D5:1 R:1
F4+D5:1 E4+C5:1 D4+Bb4:2
E4+C5:1 F4+D5:.5 G4+E5:.5 A4+F5:2
Bb4+G5:1 A4+F5:1 G4+E5:1 F4+D5:1
E4+C5:2 D4+Bb4:1 R:1
F4+A4+D5:2 G4+Bb4+E5:2
A4+C5+F5:1 G4+Bb4+E5:1 F4+A4+D5:2
E4+G4+C5:1 F4+A4+D5:1 E4+G4+C#5:1 R:1
F4+A4+D5:2 R:2
R:1 A4:.5 C5:.5 D5:1 F5:1
E5:1 D5:.5 C5:.5 A4:2
G4:1 A4:1 C5:1 E5:1
D5:2 F5:1 E5:.5 D5:.5''',
 lh='''D3:1 F3:1 E3:1 A3:1
G3:2 E3:1 C3:1
Bb2:1 F3+A3:1 D3:2
C3:1 G3+Bb3:1 E3:2
D3:2 R:2
Bb2:1 F3+A3:1 C3:1 F3:1
G2:1 D3+F3:2 Bb3:1
A2:1 E3+G3:1 C#3:2
D3:1 A3+C4:1 E3:1 G3:1
F3:1 C4:1 D3:2
Eb3:1 Bb3+D4:1 F3:1 G3:1
C3:1 G3+Bb3:1 R:2
A2:1 E3+G3:1 Bb3:1 A3:1
R:4
R:4
R:4
Bb2:.5 D3:.5 F3:1 A3:.5 C4:.5 D4:1
C4:.5 A3:.5 G3:1 F3:1 E3:1
D3:1 F3:.5 A3:.5 C4:1 B3:1
E3:1 G3:.5 A3:.5 C#4:1 R:1
D3:1 F3:1 E3:1 A3:1
G3:1 Bb3:1 A3:1 C4:1
G3:1 D3:1 C3:1 F3:1
A2:1 E3+G3:1 Bb3:1 R:1
Bb2+F3:2 C3+G3:2
D3+A3:1 C3+G3:1 Bb2+F3:2
A2+E3:1 Bb2+F3:1 A2+E3:1 R:1
D3+A3:2 R:2
Bb2:1 F3+A3:1 C3:1 D3:1
C3:1 G3+Bb3:1 F3:2
A2:1 E3+G3:1 C#3:1 E3:1
R:4''',
 tempos=[58,59,60,62,55,61,59,62,65,63,60,54,58,56,58,53,62,63,66,58,62,64,67,60,63,65,60,55,58,60,61,58],phrases=[(2,5),(6,12),(13,16),(18,20),(21,24),(25,28),(29,32)],lower_phrases=[(1,5),(17,20),(21,24)],sections={1:'p',6:'mp',9:'mf',13:'p',18:'mp',21:'mp',25:'f',29:'p'},lower_sections={1:'mp',3:'p',6:'pp',9:'p',13:'pp',17:'mf',21:'mp',25:'mf',29:'pp'},hairpins=[('crescendo',21,23),('diminuendo',26,28)],
 pedal=[[8,10.8],[20,21.8],[32,33.8],[52,53.8],[56,57.8],[80,81.8],[88,89.8],[96,97.8],[98,99.8],[104,104.8],[108,109.8],[112,113.8]])

ensemble(op=311,title='Elm Proscenium',key='a',fifths=0,meter='6/4',bpm=70,parent=293,
 source=dict(source_opus=293,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','C','B','E'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['A','C','B','E']),
 description='A solitary call in A minor opens a small concerto. A broad chord choir answers, a running solo presses forward, and a cadenza briefly suspends the ensemble. The bass then takes the foreground before the opening call returns in a larger, warmer frame.',
 technical='Distinguish the solo touch from the fuller chord answers. Keep the semiquaver cadenza supple over held bass fifths, then bring the exposed left-hand phrase forward. The large dynamic return should retain a singing top line.',
 rh='''A4:1 C5:1 B4:1 E5:3
C5+E5+A5:2 B4+D5+G5:2 A4+C5+F5:2
G4+B4+E5:2 F4+A4+D5:2 E4+G#4+B4:1 R:1
R:2 E4:1 A4:1 C5:1 B4:1
C5+E5:2 D5+F5:1 E5+G5:3
D5+F5:2 C5+E5:1 B4+D5:3
A4+C5:1 B4+D5:1 C5+E5:2 B4+D5:2
G#4+B4:2 A4+C5:2 R:2
A4:.5 C5:.5 E5:.5 G5:.5 E5:1 D5:.5 C5:.5 B4:1 A4:1
G4:.5 B4:.5 D5:.5 F5:.5 E5:1 D5:1 C5:2
F4:.5 A4:.5 C5:.5 E5:.5 D5:1 C5:.5 B4:.5 A4:2
G#4:.5 B4:.5 D5:.5 E5:.5 G#5:1 F5:1 E5:2
C5:1 E5:.5 G5:.5 A5:2 G5:1 E5:1
D5:1 F5:.5 A5:.5 G5:2 E5:1 C5:1
B4:.5 D5:.5 F5:1 E5:1 C5:1 A4:1 B4:1
G#4:2 B4:1 E5:1 R:2
A4:.25 B4:.25 C5:.25 E5:.25 G5:.25 A5:.25 G5:.25 E5:.25 D5:2 C5:2
B4:.25 C5:.25 D5:.25 F5:.25 A5:.25 G5:.25 F5:.25 D5:.25 C5:2 A4:2
G4:.25 A4:.25 B4:.25 C5:.25 D5:.25 E5:.25 F5:.25 G5:.25 E5:2 B4:2
C5:1 B4:.5 A4:.5 G#4:2 R:2
R:6
R:3 E4:1 G4:1 B4:1
C5:2 E5:1 D5:1 B4:2
A4:3 R:3
A4+C5+E5:2 C5+E5+G5:1 B4+D5+F5:3
A4+C5+E5:2 G4+B4+D5:1 F4+A4+C5:3
E4+G#4+B4:1 F4+A4+C5:1 G4+B4+D5:2 A4+C5+E5:2
G#4+B4+E5:2 A4+C5+E5:2 R:2
A4:1 C5:1 B4:1 E5:3
D5:2 C5:1 A4:1 G4:2
F4:1 A4:.5 C5:.5 E5:2 D5:1 B4:1
A4+C5+E5:4 R:2''',
 lh='''R:6
A2+E3:2 G2+D3:2 F2+C3:2
E2+B2:2 D2+A2:2 E2+B2:1 R:1
A2:1 C3:1 E3:2 G3:1 E3:1
F3:2 C4:1 A3:3
G3:2 D4:1 B3:3
F3:1 G3:1 A3:2 B3:2
E3:2 A2:2 R:2
A2:1 E3:1 C4:2 B3:1 G3:1
G2:1 D3:1 B3:2 A3:1 F3:1
F2:1 C3:1 A3:2 G3:1 E3:1
E2:1 B2:1 G#3:2 B3:1 G#3:1
F3:1 C4:1 A3:2 G3:1 E3:1
D3:1 A3:1 F3:2 G3:1 A3:1
B2:1 F3:1 A3:2 G3:1 F3:1
E3:2 B3:1 G#3:1 R:2
A2+E3:3~ A2+E3:3
D3+A3:3~ D3+A3:3
G2+D3:3~ G2+D3:3
E3+B3:4 R:2
F3:.5 A3:.5 C4:1 E4:2 D4:1 C4:1
B3:1 A3:.5 G3:.5 E3:1 F3:1 G3:2
A3:1 C4:1 B3:1 G3:1 E3:2
A2:3 R:3
F2+C3:2 G2+D3:1 D3+A3:3
A2+E3:2 G2+D3:1 F2+C3:3
E2+B2:1 F2+C3:1 G2+D3:2 A2+E3:2
E3+B3:2 A2+E3:2 R:2
F3:2 C4:1 A3:3
D3:2 A3:1 F3:1 E3:2
B2:1 F3+A3:1 E3:2 G#3:1 B3:1
A2+E3:4 R:2''',
 tempos=[70,72,68,69,70,72,74,66,76,78,77,79,80,78,76,68,78,80,82,66,70,72,74,65,72,74,76,67,69,70,68,64],phrases=[(1,3),(4,8),(9,12),(13,16),(17,20),(22,24),(25,28),(29,32)],lower_phrases=[(4,8),(21,24)],sections={1:'p',2:'mf',4:'p',5:'mp',9:'mp',13:'mf',17:'mf',22:'p',25:'f',29:'p'},lower_sections={1:'pp',2:'mf',4:'mp',5:'p',9:'pp',13:'p',17:'pp',21:'mf',25:'mf',29:'pp'},hairpins=[('crescendo',9,13),('diminuendo',14,16)],
 pedal=[[6,7.8],[8,9.8],[10,11.8],[24,26.8],[48,50.8],[72,74.8],[96,101.8],[102,107.8],[108,113.8],[144,145.8],[162,163.8],[168,170.8],[186,189.8]])

ensemble(op=312,title='Willow Amphitheatre',key='G',fifths=1,meter='3/4',bpm=84,parent=305,
 source=dict(source_opus=305,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','G#','F#','E'],transposition_semitones=-2),motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=3,pitches=['G','F#','E','D']),
 description='A bright triple-time concertino places a dancing solo against a spare pizzicato-like bass. A third voice enters under the sustained melody, turning the centre into a small chamber ensemble. The opening returns with a fuller reply and a crisp, open-air conclusion.',
 technical='Keep the moving inner right-hand voice separate from the held top notes. Use finger substitution where comfortable and avoid pressing the upper sustain. The quick outer sections should be buoyant, with short bass releases and clear phrase lifts.',
 rh='''G4:.5 F#4:.5 E4:1 D4:1
B4:1 D5:.5 E5:.5 G5:1
F#5:1 E5:.5 D5:.5 B4:1
A4:1 C5:1 D5:1
G4+B4+D5:1 R:.5 A4+C5+E5:.5 B4+D5+G5:1
A4+C5+F#5:1 G4+B4+E5:1 F#4+A4+D5:1
E4+G4+C5:1 F#4+A4+D5:1 G4+B4+E5:1
F#4+A4+D5:2 R:1
G4:.5 B4:.5 D5:.5 E5:.5 F#5:.5 G5:.5
A5:.5 G5:.5 E5:1 D5:1
B4:.5 D5:.5 F#5:.5 G5:.5 E5:1
C5:1 B4:.5 A4:.5 G4:1
E4:.5 G4:.5 B4:.5 D5:.5 C5:1
A4:.5 C5:.5 E5:.5 F#5:.5 D5:1
B4:1 A4:.5 G4:.5 F#4:1
D4:1 G4:1 R:1
G5:3
A5:3
B5:2 A5:1
A5:2 G5:1
G5:3
F#5:2 E5:1
D5:1 E5:1 F#5:1
G5:2 R:1
G5:.5 F#5:.5 E5:1 D5:1
B4:1 D5:.5 E5:.5 G5:1
F#5:1 D5:.5 B4:.5 A4:1
G4:2 R:1
G4+B4+D5:1 A4+C5+E5:1 B4+D5+G5:1
A4+C5+F#5:1 G4+B4+E5:1 F#4+A4+D5:1
G4:.5 A4:.5 B4:.5 D5:.5 E5:.5 F#5:.5
G4+B4+E5:1 R:2''',
 rh_inner='''R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
G4:.5 B4:.5 D5:1 B4:1
C5:.5 E5:.5 G5:1 E5:1
D5:.5 F#5:.5 G5:1 F#5:1
C5:1 D5:1 E5:1
B4:.5 D5:.5 E5:1 D5:1
A4:1 B4:.5 C5:.5 D5:1
G4:1 A4:1 C5:1
B4:1 D5:1 R:1
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3''',
 lh='''G2:1 D3:1 R:1
E3:1 B3:1 G3:1
C3:1 G3:1 A3:1
D3:1 A3:1 R:1
G2+D3:1 R:.5 A2+E3:.5 B2+F#3:1
D3+A3:1 C3+G3:1 B2+F#3:1
C3+G3:1 D3+A3:1 E3+B3:1
D3+A3:2 R:1
G3:1 D4:1 B3:1
F#3:1 A3:1 D3:1
E3:1 B3:1 G3:1
C3:1 G3:1 E3:1
A2:1 E3:1 G3:1
D3:1 A3:1 F#3:1
G3:1 E3:1 C3:1
D3:1 G2:1 R:1
E3+B3:3
A2+E3:3
G3+D4:3
F#3+C4:3
E3+B3:3
D3+A3:3
C3+G3:2 D3:1
G3:2 R:1
E3:1 B3:1 G3:1
C3:1 G3:1 E3:1
D3:1 A3:1 F#3:1
G2:2 R:1
G2+D3:1 A2+E3:1 B2+F#3:1
D3+A3:1 C3+G3:1 B2+F#3:1
C3:1 D3:1 F#3:1
G2+D3:1 R:2''',
 tempos=[84,86,85,81,86,88,87,80,89,91,90,85,88,90,86,78,80,82,84,81,82,80,83,77,84,86,85,79,88,89,91,86],phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32)],sections={1:'p',5:'mf',9:'mp',17:'p',25:'mp',29:'f'},lower_sections={1:'pp',5:'mf',9:'p',17:'pp',25:'p',29:'mf'},hidden_voice_rests={'inner':list(range(1,17))+list(range(25,33))},voice_phrases=[dict(voice='inner',start_beat=48,end_beat=60,swell=4),dict(voice='inner',start_beat=60,end_beat=71,swell=3)],engraving=dict(spacing_system=19,spacing_staff=23,pedal_offset_y=610),
 pedal=[[12,12.8],[48,50.8],[51,53.8],[54,56.8],[57,59.8],[60,62.8],[63,65.8],[84,84.8]])

ensemble(op=313,title='Alder Pavilion',key='Eb',fifths=-3,meter='6/4',bpm=48,parent=292,
 source=dict(source_opus=292,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=6,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Eb','D','C','Bb']),
 description='A concerto made entirely from chords and dyads. A quiet choir presents the descending theme; high pairs then answer with more air between them. The lower register briefly speaks alone, and a flat-side middle casts the melody in a different light before its spacious return.',
 technical='Hear the moving voices inside each chord, especially the descending top line. Prepare lateral moves during the written rests and keep each attack unified. Pedal changes follow the harmony; do not carry resonance across the larger silences.',
 rh='''G4+Bb4+Eb5:2 F4+Ab4+D5:1 Eb4+G4+C5:1 D4+F4+Bb4:2
Eb4+G4+C5:2 F4+Ab4+D5:2 G4+Bb4+Eb5:2
Ab4+C5+F5:3 G4+Bb4+Eb5:1 F4+Ab4+D5:2
Eb4+G4+C5:2 D4+F4+Bb4:2 R:2
G4+Eb5:1 R:1 Bb4+G5:1 F4+D5:3
Ab4+F5:2 G4+Eb5:1 R:1 F4+D5:2
Eb4+C5:1 G4+Eb5:1 F4+D5:2 D4+Bb4:2
Eb4+C5:3 R:3
R:6
R:6
Gb4+Bb4+Eb5:2 F4+Ab4+Db5:2 Eb4+Gb4+Bb4:2
E4+G4+B4:2 F4+Ab4+C5:2 G4+Bb4+D5:2
Ab4+Cb5+Eb5:2 Gb4+Bb4+Db5:1 F4+Ab4+Cb5:3
Gb4+Bb4+Db5:2 F4+Ab4+C5:1 Eb4+G4+Bb4:3
D4+F4+A4:1 Eb4+G4+Bb4:1 F4+Ab4+C5:2 G4+Bb4+D5:2
Ab4+C5+Eb5:2 F4+Ab4+D5:2 R:2
G4+Bb4+Eb5:2 F4+Ab4+D5:1 Eb4+G4+C5:1 D4+F4+Bb4:2
Eb4+G4+C5:2 G4+Bb4+Eb5:2 Bb4+Eb5+G5:2
Ab4+C5+F5:2 G4+Bb4+Eb5:1 F4+Ab4+D5:3
Eb4+G4+C5:2 D4+F4+Bb4:2 R:2
G4+Eb5:2 F4+D5:2 Eb4+C5:2
D4+Bb4:2 F4+D5:1 G4+Eb5:3
Ab4+F5:1 G4+Eb5:1 F4+D5:2 D4+Bb4:2
G4+Bb4+D5:4 R:2''',
 lh='''Eb3+Bb3:2 Bb2+F3:1 Ab2+Eb3:1 G2+D3:2
C3+G3:2 Bb2+F3:2 Eb3+Bb3:2
F3+C4:3 Eb3+Bb3:1 Bb2+F3:2
Ab2+Eb3:2 Bb2+F3:2 R:2
C3+G3:1 R:1 Eb3+Bb3:1 Bb2+F3:3
F3+C4:2 Eb3+Bb3:1 R:1 D3+A3:2
Ab2+Eb3:1 C3+G3:1 Bb2+F3:2 G2+D3:2
C3+G3:3 R:3
Ab2+Eb3:2 Bb2+F3:1 C3+G3:3
Db3+Ab3:2 Eb3+Bb3:2 Gb3+Db4:2
Eb3+Bb3:2 Db3+Ab3:2 Gb2+Db3:2
C3+G3:2 F3+C4:2 Bb2+F3:2
Ab2+Eb3:2 Gb2+Db3:1 Fb2+Cb3:3
Eb2+Bb2:2 Ab2+Eb3:1 C3+G3:3
D3+A3:1 Eb3+Bb3:1 F3+C4:2 Bb2+F3:2
Ab2+Eb3:2 Bb2+F3:2 R:2
Eb3+Bb3:2 Bb2+F3:1 Ab2+Eb3:1 G2+D3:2
C3+G3:2 Eb3+Bb3:2 G3+D4:2
F3+C4:2 Eb3+Bb3:1 Bb2+F3:3
Ab2+Eb3:2 Bb2+F3:2 R:2
C3+G3:2 Bb2+F3:2 Ab2+Eb3:2
G2+D3:2 Bb2+F3:1 C3+G3:3
F3+C4:1 Eb3+Bb3:1 Bb2+F3:2 G2+D3:2
Eb3+Bb3:4 R:2''',
 tempos=[48,49,50,46,51,50,49,45,48,50,49,51,47,49,52,46,49,51,50,46,48,49,47,43],phrases=[(1,4),(5,8),(11,12),(13,16),(17,20),(21,24)],lower_phrases=[(9,10)],sections={1:'mp',5:'p',11:'mp',13:'p',17:'f',21:'pp'},lower_sections={1:'p',5:'pp',9:'mf',11:'p',13:'pp',17:'mf',21:'pp'},
 pedal=[[0,1.8],[2,2.8],[3,3.8],[4,5.8],[6,7.8],[8,9.8],[10,11.8],[24,24.8],[26,26.8],[27,29.8],[48,49.8],[51,53.8],[72,73.8],[75,77.8],[96,97.8],[98,98.8],[99,99.8],[100,101.8],[120,121.8],[138,141.8]])

ensemble(op=314,title='Bracken Terrace',key='Bb',fifths=-2,meter='9/8',bpm=90,parent=302,
 source=dict(source_opus=302,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['Bb','A','G','F'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4.5,pitches=['Bb','A','G','F']),
 description='A lilting concertino in nine-eight trades a wide singing melody for a rippling lower part. Chordal refrains briefly gather the voices together; a darker solo episode then dissolves into a quick shared cadenza. The last refrain is brighter and shorter than the first.',
 technical='Feel three large pulses in each bar. Keep the lower arpeggios light beneath the melody and retain their direction through changes of hand position. The alternating cadenza needs matched tone and precise rests rather than overlapping pedal.',
 rh='''Bb4:1 A4:.5 G4:1.5 F4:1.5
D5:1.5 F5:.5 Eb5:.5 D5:.5 C5:1.5
Bb4:1.5 A4:.5 G4:.5 F4:.5 Eb4:1.5
D4:1 F4:.5 A4:1.5 R:1.5
Bb4:3 D5:1.5
C5:1.5 Eb5:1.5 G5:1.5
F5:1.5 D5:1 A4:.5 Bb4:1.5
A4:3 R:1.5
Bb4+D5+F5:1.5 A4+C5+Eb5:1.5 G4+Bb4+D5:1.5
F4+A4+C5:1.5 G4+Bb4+D5:1 A4+C5+Eb5:.5 Bb4+D5+F5:1.5
C5+Eb5+G5:1.5 Bb4+D5+F5:1.5 A4+C5+Eb5:1.5
G4+Bb4+D5:1.5 F4+A4+C5:1.5 R:1.5
D5:.5 F5:.5 G5:.5 Bb5:1.5 A5:.5 G5:.5 F5:.5
Eb5:1.5 D5:.5 C5:.5 Bb4:.5 A4:1.5
G4:.5 Bb4:.5 D5:.5 F5:1.5 Eb5:1.5
D5:1 C5:.5 A4:1.5 R:1.5
Bb4:.25 C5:.25 D5:.25 Eb5:.25 F5:.25 G5:.25 A5:.5 G5:.5 F5:.5 D5:1.5
R:4.5
Eb5:.25 F5:.25 G5:.25 A5:.25 Bb5:.25 A5:.25 G5:.5 F5:.5 Eb5:.5 C5:1.5
R:4.5
Bb4+D5+F5:1.5 C5+Eb5+G5:1.5 D5+F5+Bb5:1.5
C5+Eb5+A5:1.5 Bb4+D5+G5:1.5 A4+C5+F5:1.5
G4+Bb4+Eb5:1.5 A4+C5+F5:1.5 Bb4+D5+G5:1.5
A4+C5+F5:3 R:1.5
Bb4:1 A4:.5 G4:1.5 F4:1.5
D5:1.5 C5:.5 Bb4:.5 A4:.5 G4:1.5
F4:1 A4:.5 Bb4:.5 C5:.5 D5:.5 F5:1.5
Bb4+D5+G5:1.5 R:3''',
 lh='''Bb2:1.5 F3:1 D3:.5 A3:1.5
Eb3:1.5 Bb3:1 G3:.5 F3:1.5
G2:1.5 D3:1 Bb3:.5 C4:1.5
F3:1.5 C4:1.5 R:1.5
Bb2:.5 D3:.5 F3:.5 A3:.5 F3:.5 D3:.5 C3:.5 F3:.5 A3:.5
Eb3:.5 G3:.5 Bb3:.5 D4:.5 Bb3:.5 G3:.5 F3:.5 Bb3:.5 D4:.5
Bb3:.5 F3:.5 D3:.5 F3:.5 A3:.5 C4:.5 Bb3:.5 G3:.5 Eb3:.5
F3:1.5 C4:1.5 R:1.5
Bb2+F3:1.5 F2+C3:1.5 G2+D3:1.5
F2+C3:1.5 G2+D3:1 A2+E3:.5 Bb2+F3:1.5
Eb3+Bb3:1.5 D3+A3:1.5 C3+G3:1.5
Eb3+Bb3:1.5 F3+C4:1.5 R:1.5
G3:1.5 D4:1.5 Bb3:1.5
C3:1.5 G3:1.5 E3:1.5
Eb3:1.5 Bb3:1.5 G3:1.5
F3:1.5 C4:1.5 R:1.5
R:4.5
Bb3:.25 A3:.25 G3:.25 F3:.25 Eb3:.25 D3:.25 C3:.5 Eb3:.5 G3:.5 Bb3:1.5
R:4.5
A3:.25 G3:.25 F3:.25 Eb3:.25 D3:.25 C3:.25 Bb2:.5 D3:.5 F3:.5 A3:1.5
Bb2+F3:1.5 C3+G3:1.5 D3+A3:1.5
F3+C4:1.5 Eb3+Bb3:1.5 D3+A3:1.5
C3+G3:1.5 D3+A3:1.5 Eb3+Bb3:1.5
F3+C4:3 R:1.5
G3:1.5 D4:1.5 Bb3:1.5
Eb3:1.5 Bb3:1.5 G3:1.5
F3:1.5 C4:1.5 A3:1.5
Bb2+F3:1.5 R:3''',
 tempos=[90,92,91,85,94,96,95,86,92,94,96,87,91,93,92,84,98,100,101,96,96,98,97,88,90,92,94,91],phrases=[(1,4),(5,8),(9,12),(13,16),(17,17),(19,19),(21,24),(25,28)],lower_phrases=[(18,18),(20,20)],sections={1:'p',5:'mp',9:'mf',13:'p',17:'mf',21:'f',25:'p'},lower_sections={1:'pp',5:'p',9:'mf',13:'pp',18:'mf',21:'mf',25:'pp'},page_starts=[9,19],engraving=dict(spacing_system=17,spacing_staff=19,pedal_offset_y=610),
 pedal=[[0,2.8],[18,22.3],[22.5,26.8],[36,37.3],[40.5,41.8],[54,56.8],[90,91.3],[94.5,95.8],[108,110.8]])

ensemble(op=315,title='Lilac Causeway',key='Db',fifths=-5,meter='3/2',bpm=58,parent=304,
 source=dict(source_opus=304,source_hand='rh',source_start_beat=20,source_end_beat=24,source_pitches=['Db','C','Bb','Ab'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Db','C','Bb','Ab']),
 description='Broad three-two phrases cross a narrower five-beat causeway. In that middle span a tenor line begins beneath the soloist, drawing the harmony towards the lower register. The broad metre returns with a fuller ensemble and settles into a high, unresolved ninth.',
 technical='Treat the metre change as a change of stride, without hurrying the shorter bars. Sustain the left-hand bass while articulating its independent tenor. Keep the long right-hand line audible through the chordal return and clear each pedal release.',
 rh='''Db5:2 C5:1 Bb4:1 Ab4:2
F5:3 Eb5:1 C5:2
Bb4:2 Db5:1 F5:1 Eb5:2
C5:2 Ab4:2 R:2
Ab4+Db5:2 Bb4+Eb5:1 C5+F5:3
Bb4+Eb5:2 Ab4+Db5:1 Gb4+C5:3
F4+Bb4:2 Eb4+Ab4:2 Db4+Gb4:2
C4+F4:2 Eb4+Ab4:2 R:2
Db5:.5 F5:.5 Ab5:1 Gb5:1 F5:2
Eb5:1 Gb5:.5 Ab5:.5 C6:1 Bb5:1 Ab5:1
F5:.5 Eb5:.5 Db5:1 C5:1 Bb4:2
Ab4:1 C5:.5 Eb5:.5 Gb5:1 F5:1 R:1
F5:3 Eb5:2
Db5:2 C5:1 Bb4:2
Ab4:2 Bb4:1 Db5:2
C5:2 Ab4:1 R:2
F4+Ab4+Db5:2 G4+Bb4+Eb5:1 Ab4+C5+F5:3
Gb4+Bb4+Eb5:2 F4+Ab4+Db5:1 Eb4+Gb4+C5:3
Db4+F4+Bb4:2 Eb4+Gb4+C5:2 F4+Ab4+Db5:2
Eb4+Gb4+C5:2 F4+Ab4+Db5:2 R:2
Db5:2 C5:1 Bb4:1 Ab4:2
F5:3 Eb5:1 Db5:2
C5:1 Bb4:1 Ab4:2 F4:1 Ab4:1
Eb5:4 R:2''',
 lh='''Ab2:3 Eb3:1 G3:2
Db3:2 Ab3+C4:1 F3:3
Gb3:2 Db4:1 Bb3:1 Ab3:2
Eb3:2 Bb3+Db4:2 R:2
Db3:2 Ab3:1 F3:3
Gb2:2 Db3:1 Bb3:3
Eb3:2 Bb3:2 Gb3:2
Ab2:2 Eb3:2 R:2
Bb2:1 F3:1 Ab3:1 Db4:2
Ab3:1 C4:1 Eb4:1 Db4:1 Bb3:1
Gb3:1 Db4:1 Bb3:1 Ab3:2
Eb3:1 Bb3:1 Gb3:1 Ab3:1 R:1
Db3:3~ Db3:2
Bb2:3~ Bb2:2
Gb2:3~ Gb2:2
Ab2:3 R:2
Db3+Ab3:2 Eb3+Bb3:1 F3+C4:3
Gb3+Db4:2 F3+C4:1 Eb3+Bb3:3
Bb2+F3:2 Ab2+Eb3:2 Db3+Ab3:2
Ab2+Eb3:2 Db3+Ab3:2 R:2
Bb2:2 F3+Ab3:1 Db4:3
Gb3:2 Db4:1 Bb3:1 Ab3:2
Eb3:2 Bb3+Db4:1 Ab3:1 Gb3:2
Db3+Ab3:4 R:2''',
 lh_upper='''R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:5
R:5
R:5
R:5
Ab3:1 Bb3:1 C4:1 Bb3:1 Ab3:1
F3:1 G3:1 Ab3:1 Gb3:1 F3:1
Bb2:1 Db3:1 Eb3:1 F3:1 Db3:1
C3:1 Eb3:1 Gb3:1 R:2
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6''',
 meters=['3/2']*8+['5/4']*8+['3/2']*8,tempos=[58,60,61,55,59,61,60,54,66,68,67,60,59,61,62,55,60,62,64,56,58,60,57,53],phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],sections={1:'p',5:'mp',9:'mf',13:'p',17:'f',21:'pp'},lower_sections={1:'pp',5:'p',9:'pp',13:'mp',17:'mf',21:'pp'},hidden_voice_rests={'tenor':list(range(1,13))+list(range(17,25))},voice_phrases=[dict(voice='tenor',start_beat=68,end_beat=83,swell=4),dict(voice='tenor',start_beat=83,end_beat=86,swell=2)],engraving=dict(spacing_system=19,spacing_staff=23,pedal_offset_y=610),
 pedal=[[0,2.8],[12,14.8],[24,26.8],[48,50.8],[68,72.8],[73,77.8],[78,82.8],[88,89.8],[106,107.8],[112,114.8],[130,133.8]])

ensemble(op=316,title='Cedar Forum',key='b',fifths=2,meter='4/4',bpm=58,parent=295,
 source=dict(source_opus=295,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['B','D','C#','F#'],transposition_semitones=0),motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['B','D','C#','F#']),
 description='Four voices debate a compact B-minor theme. The middle pair fall silent for a flowing duet, then return with contrary motion. A lower-register conversation leads to a final gathering in which the theme is gentler and its last harmony quietly brightened.',
 technical='Practise each of the four voices as a separate line before combining the hands. Keep every held note alive while its neighbour moves, without relying on continuous pedal. The complete reach of either hand remains within an octave.',
 rh='''B4:1 D5:1 C#5:1 F#5:1
E5:2 D5:1 B4:1
C#5:1 E5:1 D5:1 A4:1
B4:2 A4:1 F#4:1
G4:1 B4:1 D5:2
C#5:2 B4:1 A4:1
G4:1 A4:1 B4:1 D5:1
C#5:2 B4:1 R:1
F#4:.5 A4:.5 B4:.5 D5:.5 F#5:1 E5:1
D5:.5 C#5:.5 B4:.5 A4:.5 F#4:1 E4:1
G4:.5 B4:.5 D5:.5 F#5:.5 E5:1 C#5:1
A4:1 G4:1 F#4:1 R:1
B4:2 C#5:1 D5:1
E5:2 D5:1 C#5:1
F#5:2 E5:1 D5:1
C#5:2 B4:2
F#4:4
G4:2 A4:2
B4:2 D5:1 C#5:1
B4:2 A4:1 R:1
B4:1 D5:1 C#5:1 F#5:1
E5:2 D5:1 B4:1
A4:1 C#5:1 B4:1 A4:1
B4:2 R:2''',
 rh_inner='''D4:1 F#4:1 E4:1 A4:1
G4:1 B4:1 A4:1 F#4:1
E4:1 G4:1 F#4:1 D4:1
F#4:1 E4:1 D4:1 B3:1
B3:1 D4:1 F#4:1 A4:1
E4:1 G4:1 F#4:1 E4:1
D4:1 E4:1 F#4:1 A4:1
G4:1 E4:1 F#4:1 R:1
R:4
R:4
R:4
R:4
D4:1 F#4:1 A4:1 B4:1
G4:1 A4:1 B4:1 G4:1
A4:1 C#5:1 B4:1 A4:1
G4:1 E4:1 F#4:1 D4:1
R:4
R:4
R:4
R:4
D4:1 F#4:1 E4:1 A4:1
G4:1 B4:1 A4:1 F#4:1
D4:1 E4:1 F#4:1 E4:1
D#4+F#4:2 R:2''',
 lh='''B2:4
E3:4
A2:4
B2:2 F#2:2
G2:4
A2:4
E3:2 G2:2
F#2:2 B2:1 R:1
B2:1 F#3:1 A3:2
D3:1 A3:1 F#3:2
E3:1 B3:1 G3:2
F#3:1 C#4:1 A#3:1 R:1
B2:4
E3:4
D3:2 A2:2
F#2:2 B2:2
B2:4
E3:4
G2:2 E3:2
F#3:2 B2:1 R:1
G2:4
E3:4
F#2:2 F#3:2
B2:2 R:2''',
 lh_upper='''F#3:1 A3:1 G3:1 F#3:1
G3:1 B3:1 D4:1 B3:1
E3:1 G3:1 F#3:1 E3:1
D3:1 E3:1 C#3:1 A#2:1
B2:1 D3:1 F#3:1 E3:1
C#3:1 E3:1 G3:1 F#3:1
G3:1 B3:1 D3:1 F#3:1
A#2:1 C#3:1 D3:1 R:1
R:4
R:4
R:4
R:4
F#3:1 G3:1 A3:1 F#3:1
G3:1 B3:1 D4:1 C#4:1
F#3:1 A3:1 G3:1 E3:1
A#2:1 C#3:1 D3:1 F#3:1
D3:.5 F#3:.5 A3:1 G3:1 F#3:1
G3:.5 B3:.5 D4:1 C#4:1 B3:1
B2:1 D3:1 G3:1 F#3:1
A#3:1 G#3:1 F#3:1 R:1
B2:1 D3:1 E3:1 F#3:1
G3:1 B3:1 D4:1 B3:1
A#2:1 C#3:1 A3:1 G3:1
F#3:2 R:2''',
 tempos=[58,60,61,57,59,61,63,55,66,68,67,58,61,63,65,59,60,62,64,56,59,61,58,54],phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],sections={1:'mp',9:'mf',13:'mp',17:'pp',21:'p'},lower_sections={1:'p',9:'pp',13:'p',17:'mf',21:'p'},hidden_voice_rests={'inner':list(range(9,13))+list(range(17,21)),'tenor':list(range(9,13))},voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=3) for a,b in [(0,16),(16,31),(48,64),(80,94)]]+[dict(voice='tenor',start_beat=a,end_beat=b,swell=4) for a,b in [(0,16),(16,31),(48,64),(64,79),(80,94)]],engraving=dict(spacing_system=20,spacing_staff=27,pedal_offset_y=740),
 pedal=[[0,1.8],[16,17.8],[32,34.8],[48,49.8],[64,65.8],[80,81.8],[92,93.8]])

ensemble(op=317,title='Sorrel Theatre',key='f',fifths=-4,meter='4/4',bpm=66,parent=306,
 source=dict(source_opus=306,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['G','F','D','C'],transposition_semitones=-2),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['F','Eb','C','Bb']),
 description='A minor-key concerto plays with two simultaneous senses of time. The soloist pours five notes across the accompaniment’s two beats, then lends that fluid motion to the left hand. A chordal centre gathers the conflicting pulses before a spare final recollection.',
 technical='Hear the 5:4 groups across two quarter beats without forcing accents on individual notes. Practise their alignment against the other hand slowly. Preserve the same singing tone when the running part changes hands and keep the thicker refrain transparent.',
 rh='''F5:1 Eb5:1 C5:1 Bb4:1
Ab4:1 C5:.5 Eb5:.5 G5:2
F5:2 Eb5:1 C5:1
Bb4:1 Ab4:1 G4:1 R:1
Ab4+C5+F5:2 G4+Bb4+Eb5:2
F4+Ab4+Db5:1 G4+Bb4+Eb5:1 Ab4+C5+F5:2
Bb4+Db5+G5:1 Ab4+C5+F5:1 G4+Bb4+Eb5:1 F4+Ab4+Db5:1
E4+G4+C5:2 R:2
F4:2/5 Ab4:2/5 C5:2/5 Eb5:2/5 F5:2/5 G5:2/5 F5:2/5 Eb5:2/5 C5:2/5 Ab4:2/5
Db5:2/5 Eb5:2/5 F5:2/5 Ab5:2/5 G5:2/5 F5:2/5 Eb5:2/5 Db5:2/5 C5:2/5 Bb4:2/5
Eb5:2/5 F5:2/5 G5:2/5 Bb5:2/5 Ab5:2/5 G5:2/5 F5:2/5 Eb5:2/5 Db5:2/5 C5:2/5
Bb4:2/5 C5:2/5 Db5:2/5 E5:2/5 G5:2/5 F5:2/5 E5:2/5 Db5:2/5 C5:2/5 Bb4:2/5
Ab4:4
Bb4:2 C5:2
Db5:3 C5:1
Bb4:2 G4:1 R:1
Ab4+C5+F5:2 Bb4+Db5+G5:1 C5+Eb5+Ab5:1
Bb4+Db5+G5:1 Ab4+C5+F5:1 G4+Bb4+Eb5:2
F4+Ab4+Db5:2 G4+Bb4+Eb5:2
Ab4+C5+F5:2 R:2
F5:.5 Eb5:.5 Db5:.5 C5:.5 Bb4:1 Ab4:1
G4:.5 Bb4:.5 C5:.5 Db5:.5 E5:2
F5:1 G5:.5 Ab5:.5 G5:1 Eb5:1
C5:2 Bb4:1 R:1
F5:1 Eb5:1 C5:1 Bb4:1
Ab4:1 C5:.5 Eb5:.5 F5:2
G5:1 Eb5:1 C5:1 Bb4:1
Ab4:2 R:2
R:2 G4:.5 Ab4:.5 C5:1
Db5:1 C5:.5 Bb4:.5 Ab4:2
G4:1 Bb4:1 C5:1 E5:1
F5:2 R:2''',
 lh='''F3:2 C4:1 Ab3:1
Eb3:1 Bb3+Db4:1 G3:2
Db3:1 Ab3+C4:1 F3:2
C3:1 G3+Bb3:1 E3:1 R:1
F2+C3:2 Eb2+Bb2:2
Db3+Ab3:1 Eb3+Bb3:1 F3+C4:2
G3+Db4:1 F3+C4:1 Eb3+Bb3:1 Db3+Ab3:1
C3+G3:2 R:2
F3:1 C4:1 Ab3:1 G3:1
Db3:1 Ab3:1 F3:1 Eb3:1
Eb3:1 Bb3:1 G3:1 F3:1
C3:1 G3:1 Bb3:1 E3:1
F3:2/5 Ab3:2/5 C4:2/5 Eb4:2/5 Db4:2/5 C4:2/5 Ab3:2/5 G3:2/5 F3:2/5 Eb3:2/5
Db3:2/5 F3:2/5 Ab3:2/5 C4:2/5 Bb3:2/5 Ab3:2/5 G3:2/5 F3:2/5 Eb3:2/5 Db3:2/5
Eb3:2/5 G3:2/5 Bb3:2/5 Db4:2/5 C4:2/5 Bb3:2/5 Ab3:2/5 G3:2/5 F3:2/5 Eb3:2/5
C3:2/5 E3:2/5 G3:2/5 Bb3:2/5 Ab3:2/5 G3:1 R:1
F2+C3:2 G2+D3:1 Ab2+Eb3:1
Db3+Ab3:1 C3+G3:1 Bb2+F3:2
Db3+Ab3:2 Eb3+Bb3:2
F3+C4:2 R:2
Db3:1 Ab3:1 F3:1 Eb3:1
C3:1 G3:1 Bb3:1 E3:1
F3:1 C4:1 Ab3:1 G3:1
Bb2:1 F3+Ab3:1 Db3:1 R:1
F3:2 C4:1 Ab3:1
Db3:1 Ab3+C4:1 F3:2
Eb3:1 Bb3+Db4:1 G3:1 Eb3:1
F3:2 R:2
Db3:.5 F3:.5 Ab3:1 C4:1 Bb3:1
Eb3:1 Bb3+Db4:1 Ab3:2
C3:1 G3+Bb3:1 E3:1 G3:1
F3+C4:2 R:2''',
 tempos=[66,68,67,62,68,70,72,63,70,72,74,68,67,69,71,62,72,74,73,65,68,70,72,64,66,68,67,61,64,66,65,60],phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32)],lower_phrases=[(13,16),(29,31)],sections={1:'p',5:'mf',9:'mf',13:'p',17:'f',21:'mp',25:'p',29:'pp'},lower_sections={1:'pp',5:'mf',9:'pp',13:'mf',17:'mf',21:'p',25:'pp',29:'p'},
 tuplet_spans=[dict(hand='rh',start_beat=s,end_beat=s+2,actual=5,normal=4,stem='down',show_number='both') for s in range(32,48,2)]+[dict(hand='lh',start_beat=s,end_beat=s+2,actual=5,normal=4,stem='up',show_number='both') for s in range(48,62,2)],
 pedal=[[0,1.8],[16,17.8],[32,33.8],[40,41.8],[48,49.8],[56,57.8],[64,65.8],[72,73.8],[96,97.8],[124,125.8]])

ensemble(op=318,title='Birch Observatory',key='E',fifths=4,meter='6/4',bpm=50,parent=305,
 source=dict(source_opus=305,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','G#','F#','E'],transposition_semitones=7),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['E','D#','C#','B']),
 description='An exposed upper line seems to watch a distant ensemble assembling below. Its quiet E-major call passes into the bass, expands into a brief full chordal response, then moves into a luminous duet with both hands in treble. The close leaves a single high note above an open fifth.',
 technical='Give the high register a rounded tone rather than a percussive glitter. Prepare the left-hand clef changes during its phrase releases. Project the melody through the central chords, then reduce the weight as both hands enter the treble register.',
 rh='''E5:2 D#5:1 C#5:1 B4:2
G#5:3 F#5:1 D#5:2
F#5:1 G#5:.5 A5:.5 B5:2 A5:1 G#5:1
F#5:2 E5:2 R:2
R:2 G#4+B4:1 A4+C#5:1 B4+D#5:2
C#5+E5:2 B4+D#5:1 G#4+C#5:3
A4+C#5:1 B4+D#5:1 C#5+E5:2 D#5+F#5:2
B4+E5:3 R:3
G#4+B4+E5:2 B4+D#5+F#5:1 C#5+E5+G#5:3
B4+D#5+F#5:2 A4+C#5+E5:1 G#4+B4+D#5:3
F#4+A4+C#5:2 G#4+B4+D#5:2 A4+C#5+E5:2
G#4+B4+E5:4 R:2
B5:2 A5:1 G#5:3
F#5:2 G#5:1 A5:1 B5:2
C#6:2 B5:1 A5:1 G#5:2
F#5:2 E5:2 R:2
E5:2 D#5:1 C#5:1 B4:2
G#5:3 F#5:1 E5:2
D#5:1 F#5:1 G#5:1 B5:1 C#6:1 D#6:1
E6:4 R:2''',
 lh='''R:6
R:6
R:6
R:6
E3:2 D#3:1 C#3:1 B2:2
A2:2 E3:1 G#3:3
F#3:2 C#4:1 B3:1 A3:2
E3:3 R:3
E2+B2:2 B2+F#3:1 C#3+G#3:3
G#2+D#3:2 A2+E3:1 B2+F#3:3
F#2+C#3:2 G#2+D#3:2 A2+E3:2
E3+B3:4 R:2
G#4:1 B4:1 D#5:1 C#5:1 B4:1 A4:1
D#4:1 F#4:1 A4:1 G#4:1 F#4:2
E4:1 G#4:1 B4:1 D#5:1 C#5:1 B4:1
A4:1 F#4:1 E4:2 R:2
C#3:2 G#3+B3:1 E3:3
A2:2 E3+G#3:1 C#4:1 B3:2
F#3:2 C#4:1 B3:1 A3:1 F#3:1
E3+B3:4 R:2''',
 tempos=[50,52,54,47,50,51,53,46,54,56,55,48,51,53,55,47,50,52,51,46],phrases=[(1,4),(5,8),(9,12),(13,16),(17,20)],lower_phrases=[(5,8),(13,16)],sections={1:'pp',5:'p',9:'f',13:'pp',17:'p',20:'pp'},lower_sections={1:'pp',5:'mf',9:'mf',13:'p',17:'pp'},clef_changes={'lh':{1:'bass',13:'treble',17:'bass'}},page_starts=[9,15],
 pedal=[[24,26.8],[30,32.8],[48,49.8],[50,50.8],[51,53.8],[66,69.8],[72,74.8],[84,86.8],[96,98.8],[114,117.8]])

ensemble(op=319,title='Myrtle Belvedere',key='c',fifths=-3,meter='5/4',bpm=60,parent=316,
 source=dict(source_opus=316,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4,source_pitches=['B','D','C#','F#'],transposition_semitones=1),motif=dict(hand='lh',voice='bass',start_beat=0,end_beat=5,pitches=['C','Eb','D','G']),
 description='The lower voice becomes the soloist in a five-beat elegy. Brief upper chords listen, interrupt and eventually answer. A tenor line grows over sustained bass notes in the middle, making the left hand its own small ensemble; the final sentence belongs to the original bass alone.',
 technical='Let the bass melody lead without becoming heavy. In the three-voice passage, sustain the bass with one finger while shaping the tenor independently. Place the upper replies gently and honour their written silences.',
 rh='''R:5
Eb4+G4+C5:1 R:2 R:2
R:2 F4+Ab4+D5:1 G4+Bb4+Eb5:2
D4+F4+B4:2 R:3
R:1 G4:1 C5:1 Eb5:2
D5:2 C5:1 Bb4:2
Ab4:1 C5:.5 D5:.5 F5:2 Eb5:1
D5:2 B4:1 R:2
C5:1 Eb5:1 D5:1 G5:2
F5:1 Eb5:.5 D5:.5 C5:1 Bb4:2
Ab4:1 C5:1 D5:.5 Eb5:.5 G5:2
F5:2 D5:1 B4:1 R:1
Eb4+G4+C5:2 F4+Ab4+D5:1 G4+Bb4+Eb5:2
F4+Ab4+D5:1 Eb4+G4+C5:1 D4+F4+Bb4:3
C4+Eb4+Ab4:2 D4+F4+Bb4:1 Eb4+G4+C5:2
D4+F4+B4:3 R:2
Eb4+G4+C5:3 D4+F4+Bb4:2
Eb4+G4+C5:2 F4+Ab4+D5:1 G4+Bb4+Eb5:2
Ab4+C5+F5:3 G4+Bb4+Eb5:2
F4+Ab4+D5:2 D4+F4+B4:1 R:2
C5:2 Eb5:1 D5:2
F5:2 Eb5:1 C5:2
D5:1 C5:1 Bb4:1 Ab4:1 G4:1
Eb4+G4+C5:3 R:2
R:5
R:5
R:5
R:5''',
 lh='''C3:1 Eb3:1 D3:1 G3:2
F3:1 Ab3:.5 G3:.5 Eb3:1 D3:2
C3:1 D3:.5 Eb3:.5 F3:1 Ab3:1 G3:1
D3:2 B2:1 R:2
C3:1 Eb3:1 G3:1 Bb3:2
Ab3:1 F3:1 Eb3:1 D3:2
F3:.5 G3:.5 Ab3:1 C4:1 Bb3:1 Ab3:1
G3:1 F3:1 D3:1 R:2
Ab2:2 Eb3+G3:1 C4:2
Bb2:1 F3+Ab3:1 D3:1 Eb3:2
F3:1 C4:1 Ab3:1 G3:2
G2:1 D3+F3:1 B2:1 D3:1 R:1
C3+G3:2 D3+A3:1 Eb3+Bb3:2
Ab2+Eb3:1 G2+D3:1 Bb2+F3:3
Ab2+Eb3:2 Bb2+F3:1 C3+G3:2
G2+D3:3 R:2
C3:3~ C3:2
Ab2:3~ Ab2:2
F3:3~ F3:2
G2:3 R:2
Ab2:3~ Ab2:2
Bb2:3~ Bb2:2
G2:3~ G2:2
C3:3 R:2
C3:1 Eb3:1 D3:1 G3:2
F3:2 Eb3:1 D3:1 C3:1
Bb2:1 D3:1 F3:1 Ab3:1 G3:1
C3:3 R:2''',
 lh_upper='''R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
R:5
G3:1 Bb3:1 Ab3:1 G3:1 F3:1
C3:1 Eb3:1 G3:1 F3:1 Eb3:1
Ab3:1 C4:1 Eb4:1 D4:1 C4:1
B2:1 D3:1 F3:1 R:2
C3:1 Eb3:1 G3:1 F3:1 Eb3:1
D3:1 F3:1 Ab3:1 G3:1 F3:1
B2:1 D3:1 F3:1 Eb3:1 D3:1
Eb3:1 G3:1 Bb3:1 R:2
R:5
R:5
R:5
R:5''',
 tempos=[60,62,63,57,61,63,65,57,64,66,67,59,63,65,66,58,60,62,64,57,61,63,60,56,59,60,61,56],phrases=[(3,4),(5,8),(9,12),(13,16),(17,20),(21,24)],lower_phrases=[(1,4),(5,8),(25,28)],sections={1:'pp',5:'p',9:'mf',13:'f',17:'p',21:'pp'},lower_sections={1:'mf',9:'pp',13:'mf',17:'mp',25:'p'},hidden_voice_rests={'tenor':list(range(1,17))+list(range(25,29))},voice_phrases=[dict(voice='tenor',start_beat=a,end_beat=b,swell=4) for a,b in [(80,95),(95,98),(100,118)]],page_starts=[9,19],engraving=dict(spacing_system=17,spacing_staff=23,pedal_offset_y=650),
 pedal=[[0,1.8],[20,22.8],[40,42.8],[60,61.8],[80,84.8],[85,89.8],[90,94.8],[100,104.8],[105,109.8],[110,114.8]])

ensemble(op=320,title='Orchid Confluence',key='d',fifths=-1,meter='6/4',bpm=64,parent=310,
 source=dict(source_opus=310,source_hand='lh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),motif=dict(hand='lh',voice='bass',start_beat=0,end_beat=6,pitches=['D','F','E','A']),
 description='The batch closes with a meeting of its three worlds: a private bass conversation, an increasingly free solo, and a four-voice ensemble. Their agreement opens into fuller chords before a final cadenza. The returning minor theme gradually acquires a major third, ending with a warm sixth and ninth.',
 technical='Plan the large arc across the solo, quartet and chordal sections. Keep each of the four central voices independent, and practise the two cadenza bars without pedal before adding their late bass replies. Let the major-third change near the end sound like a gradual clearing.',
 rh='''R:5 A4:1
C5:2 D5:1 F5:1 E5:2
D5:1 C5:1 A4:2 G4:1 F4:1
E4:2 G4:1 A4:1 R:2
F4+A4+D5:2 G4+Bb4+E5:1 A4+C5+F5:3
G4+Bb4+E5:2 F4+A4+D5:1 E4+G4+C5:3
D4+F4+Bb4:2 E4+G4+C5:2 F4+A4+D5:2
E4+G4+C#5:2 F4+A4+D5:2 R:2
D5:3 C5:3
Bb4:2 A4:1 G4:3
A4:3 C5:1 D5:2
E5:2 C#5:2 R:2
D5:.5 F5:.5 A5:1 G5:.5 F5:.5 E5:1 D5:1 C5:1
Bb4:.5 D5:.5 F5:1 E5:.5 D5:.5 C5:1 A4:2
G4:.5 Bb4:.5 D5:1 F5:.5 E5:.5 D5:1 C5:1 A4:1
G4:1 E4:1 A4:2 R:2
D5:3 F5:3
E5:3 G5:3
F5:3 A5:3
E5:3 G5:3
D5:3 F5:3
C5:3 E5:3
D5:2 C5:2 A4:2
A4:3 R:3
F4+A4+D5:2 A4+C5+F5:1 G4+Bb4+E5:3
F4+A4+D5:2 E4+G4+C5:1 D4+F4+Bb4:3
E4+G4+C5:1 F4+A4+D5:1 G4+Bb4+E5:2 A4+C5+F5:2
E4+G4+C#5:2 F4+A4+D5:2 R:2
D5:.25 E5:.25 F5:.25 A5:.25 G5:.25 F5:.25 E5:.25 D5:.25 C5:2 A4:2
Bb4:.25 C5:.25 D5:.25 F5:.25 E5:.25 D5:.25 C5:.25 Bb4:.25 A4:2 G4:2
F4:1 A4:.5 C5:.5 D5:2 E5:1 F5:1
E5:1 C#5:1 A4:2 R:2
F4+D5:2 E4+C5:1 D4+Bb4:1 E4+C5:2
F4+D5:2 G4+E5:1 A4+F5:3
G4+E5:2 F4+D5:1 E4+C5:1 D4+Bb4:2
E4+C#5:2 F#4+D5:2 R:2
D5:2 F#5:1 E5:1 A5:2
G5:2 E5:1 C#5:1 B4:2
A4:1 B4:1 C#5:1 D5:1 E5:1 F#5:1
F#4+B4+E5:3 R:3''',
 lh='''D3:2 F3:1 E3:1 A3:2
G3:2 Bb3:1 A3:1 E3:2
F3:1 G3:1 A3:2 Bb3:1 G3:1
A2:2 E3:1 C#3:1 R:2
D3+A3:2 E3+B3:1 F3+C4:3
C3+G3:2 Bb2+F3:1 A2+E3:3
Bb2+F3:2 C3+G3:2 D3+A3:2
A2+E3:2 D3+A3:2 R:2
Bb2:.5 D3:.5 F3:1 A3:.5 C4:.5 D4:1 C4:1 A3:1
G3:.5 Bb3:.5 C4:1 D4:.5 C4:.5 Bb3:1 A3:2
F3:.5 A3:.5 C4:1 E4:.5 D4:.5 C4:1 Bb3:1 G3:1
A3:1 G3:1 E3:2 R:2
Bb2:2 F3+A3:1 Bb3:3
G2:2 D3+F3:1 Bb3:3
C3:2 G3+Bb3:1 E3:3
A2:2 E3+G3:2 R:2
D3:3~ D3:3
C3:3~ C3:3
F3:3~ F3:3
E3:3~ E3:3
Bb2:3~ Bb2:3
A2:3~ A2:3
G2:2 A2:2 Bb2:2
D3:3 R:3
Bb2+F3:2 C3+G3:1 D3+A3:3
G2+D3:2 A2+E3:1 Bb2+F3:3
C3+G3:1 D3+A3:1 E3+B3:2 F3+C4:2
A2+E3:2 D3+A3:2 R:2
R:3 R:2 Bb3:1
R:3 R:2 A3:1
G3:2 D3:1 E3:1 A2:2
E3:1 G3:1 C#4:2 R:2
D3:2 F3:1 E3:1 A3:2
Bb3:2 A3:1 G3:3
C3:2 G3:1 E3:1 F3:2
A2:2 D3:2 R:2
D3:2 F#3:1 E3:1 A3:2
B2:2 F#3+A3:1 E3:1 G3:2
A2:1 E3:1 G3:1 B3:1 A3:1 G3:1
D3+A3:3 R:3''',
 rh_inner='\n'.join(['R:6']*16+['F4:1 A4:1 C5:1 A4:1 C5:1 D5:1','G4:1 B4:1 D5:1 B4:1 D5:1 E5:1','A4:1 C5:1 E5:1 C5:1 E5:1 F5:1','G4:1 B4:1 D5:1 B4:1 D5:1 E5:1','F4:1 A4:1 C5:1 A4:1 C5:1 D5:1','E4:1 G4:1 B4:1 G4:1 B4:1 C5:1','F4:1 A4:1 E4:1 G4:1 D4:1 F4:1','C4:1 E4:1 F#4:1 R:3']+['R:6']*16),
 lh_upper='\n'.join(['R:6']*16+['F3:1 A3:1 B3:1 A3:1 G3:1 F3:1','E3:1 G3:1 B3:1 A3:1 G3:1 E3:1','A3:1 C4:1 E4:1 D4:1 C4:1 A3:1','G3:1 B3:1 D4:1 C4:1 B3:1 G3:1','D3:1 F3:1 A3:1 G3:1 F3:1 D3:1','C3:1 E3:1 G3:1 F3:1 E3:1 C3:1','Bb2:1 D3:1 C3:1 E3:1 D3:1 F3:1','F3:1 A3:1 B3:1 R:3']+['R:6']*16),
 tempos=[64,65,66,60,66,68,69,60,66,68,70,61,72,74,73,62,64,66,68,67,65,64,62,58,69,71,73,62,74,72,70,60,64,66,65,59,63,64,62,58],phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32),(33,36),(37,40)],lower_phrases=[(1,4),(9,12),(33,36)],sections={1:'p',5:'mf',9:'pp',13:'mf',17:'mp',21:'p',25:'f',29:'mf',33:'p',37:'mp',40:'p'},lower_sections={1:'mp',5:'mf',9:'mf',13:'pp',17:'p',21:'pp',25:'mf',29:'p',33:'mp',37:'p'},hidden_voice_rests={'inner':list(range(1,17))+list(range(25,41)),'tenor':list(range(1,17))+list(range(25,41))},voice_phrases=[dict(voice=v,start_beat=a,end_beat=b,swell=3) for v in ['inner','tenor'] for a,b in [(96,120),(120,141)]],engraving=dict(spacing_system=20,spacing_staff=27,pedal_offset_y=740),
 pedal=[[0,2.8],[24,25.8],[30,31.8],[48,50.8],[72,74.8],[96,98.8],[102,104.8],[108,110.8],[114,116.8],[120,122.8],[126,128.8],[144,145.8],[156,156.8],[192,194.8],[216,218.8],[234,236.8]])
