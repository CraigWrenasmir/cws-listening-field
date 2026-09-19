"""Elastic Time, CWS Op. 331–340."""
from weather_common import make_study
PIECES=[]
def study(**kwargs):
    p=make_study(**kwargs);PIECES.append(p);return p

study(op=331,title='Willow Hesitation',key='Eb',fifths=-3,meter='4/4',bpm=52,parent=321,
 source=dict(source_opus=321,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['Eb','D','C','Bb']),
 description='An E-flat song leans against a quiet three-three-two current. The melody begins to cross its bar lines, briefly finding triplet figures against the unchanged ground. The last return arrives late; the accompaniment gradually sheds its repeated attacks and leaves the phrase suspended on a ninth.',
 technical='Keep the short repeating ground soft while carrying the melody across its accents. Four written triplet groups briefly contradict the accompaniment. Release the pedal at the shared silences and let the final ninth remain light.',
 rh='''Eb5:1 D5:.5 C5:.5 Bb4:2
G4:1 Bb4:1 C5:1 D5:1
F5:1.5 Eb5:.5 D5:1 C5:1~
C5:1 Bb4:2 R:1
Ab4:1 C5:1 Bb4:1 G4:1
F4:1 G4:1 Bb4:1 R:1
R:.5 Eb5:1 D5:.5 C5:.5 Bb4:1.5
G4:1 Bb4:.5 C5:.5 D5:1 Eb5:1~
Eb5:1 F5:1/3 G5:1/3 F5:1/3 Eb5:1 D5:1
C5:2 Bb4:1 R:1
Ab4:1 Bb4:1/3 C5:1/3 D5:1/3 Eb5:1 D5:1
C5:1 Bb4:1 G4:1 R:1
Ab4:2 C5:1 Eb5:1
F5:1 G5:1/3 Ab5:1/3 G5:1/3 F5:1 Eb5:1
D5:1 F5:1/3 G5:1/3 F5:1/3 Eb5:1 D5:1
C5:1 Eb5:1 D5:1 Bb4:1
Ab4:1 G4:1 F4:1 A4:1
Bb4:3 R:1
R:1 Eb5:1 D5:.5 C5:.5 Bb4:1
G4:1 Bb4:1 C5:1 D5:1
F5:1.5 Eb5:.5 D5:1 C5:1
Bb4:1 Ab4:1 G4:1 F4:1
G4:2 Eb4:1 F4:1
F4:3 R:1''',
 lh='''Eb3:.75 G3:.75 Bb3:.5 G3:.75 Bb3:.75 G3:.5
C3:.75 Eb3:.75 G3:.5 Eb3:.75 G3:.75 Eb3:.5
F3:.75 Ab3:.75 C4:.5 Ab3:.75 C4:.75 F3:.5
Bb2:.75 D3:.75 Ab3:.5 F3:1 R:1
Ab2:.75 C3:.75 Eb3:.5 C3:.75 Eb3:.75 C3:.5
Bb2:.75 D3:.75 F3:.5 Ab3:1 R:1
Eb3:.75 G3:.75 Bb3:.5 G3:.75 Bb3:.75 G3:.5
C3:.75 Eb3:.75 G3:.5 Eb3:.75 G3:.75 Eb3:.5
F3:.75 Ab3:.75 C4:.5 Ab3:.75 C4:.75 F3:.5
Bb2:.75 D3:.75 Ab3:.5 F3:1 R:1
Ab2:.75 C3:.75 Eb3:.5 C3:.75 Eb3:.75 C3:.5
G2:.75 B2:.75 F3:.5 D3:1 R:1
Ab2:.75 C3:.75 Eb3:.5 C3:.75 Eb3:.75 C3:.5
Db3:.75 F3:.75 Ab3:.5 F3:.75 Ab3:.75 F3:.5
Bb2:.75 D3:.75 F3:.5 D3:.75 F3:.75 D3:.5
C3:.75 Eb3:.75 G3:.5 Eb3:.75 G3:.75 Eb3:.5
F3:.75 Ab3:.75 C4:.5 F3:.75 A3:.75 F3:.5
Bb2:1 D3+Ab3:2 R:1
C3:.75 Eb3:.75 G3:.5 Eb3:.75 G3:.75 Eb3:.5
Ab2:.75 C3:.75 G3:.5 C3:.75 Eb3:.75 C3:.5
F3:1 Ab3+C4:1 Bb2:1 D3+Ab3:1
Eb3:1 G3+Bb3:1 Ab2:1 C3+Eb3:1
Bb2+D3+Ab3:2 Eb3+G3+Bb3:2
Eb3+G3+Bb3:3 R:1''',
 tempos=[52,53,52,50,52,50,52,53,54,51,53,50,54,56,54,53,52,50,52,53,52,51,50,49],
 phrases=[(1,4),(5,6),(7,10),(11,12),(13,16),(17,18),(19,22),(23,24)],sections={1:'p',7:'mp',13:'mp',14:'mf',17:'p',19:'p',23:'pp'},lower_sections={1:'pp',13:'p',19:'pp'},
 tuplet_spans=[dict(hand='rh',start_beat=s,end_beat=s+1,actual=3,normal=2,stem='down') for s in [33,41,53,57]],
 pedal=[[i*4+.05,i*4+(2.85 if i in [3,5,9,11,17,23] else 3.85)] for i in range(24)],hairpins=[('crescendo',13,14),('diminuendo',15,18)])
study(op=332,title='Clover Pendulum',key='G',fifths=1,meter='6/4',bpm=62,parent=327,
 source=dict(source_opus=327,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['G','F#','E','D'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['G','F#','E','D']),
 description='Three spacious bass steps support a long G-major song. In the central span four dotted pulses move beneath three equal melodic notes, so the two hands meet only at the bar line. The final return enlarges the bass to two gestures and finishes a bar earlier than the opening suggests.',
 technical='Maintain the six-quarter span through the central four-against-three passage. Keep the melody singing and the dotted bass quiet; the final two-pulse ground should feel broader without an abrupt tempo change.',
 rh='''G5:1 F#5:.5 E5:.5 D5:4
B4:2 D5:2 E5:2
F#5:3 E5:1 D5:1 C5:1
B4:4 R:2
C5:2 E5:2 G5:2
F#5:2 E5:2 D5:2
A4:2 C5:2 B4:1 A4:1
D5:4 R:2
G5:2 F#5:2 E5:2
D5:2 B4:2 D5:2
E5:2 F#5:2 A5:2
G5:3 R:3
B5:2 A5:2 D6:2
C6:2 B5:2 A5:2
G5:2 E5:2 C5:2
F#5:3 D5:1 R:2
G5:1 F#5:.5 E5:.5 D5:4
B4:2 D5:2 E5:2
F#5:3 E5:1 D5:1 C5:1
B4:4 R:2
C5:2 B4:2 A4:2
G4:2 A4:2 F#4:2
G4:4 R:2''',
 lh='''G2:2 B2+D3:2 F#3:2
E3:2 G3+B3:2 D3:2
D3:2 F#3+A3:2 C3:2
G2:2 B2+D3:2 R:2
C3:2 E3+G3:2 B2:2
D3:2 F#3+A3:2 C3:2
A2:2 C3+E3:2 D3+F#3:2
D3:2 F#3+A3:2 R:2
G2:1.5 B2+D3:1.5 D3:1.5 B2+F#3:1.5
E3:1.5 G3+B3:1.5 B2:1.5 G3+B3:1.5
C3:1.5 E3+G3:1.5 A2:1.5 C3+E3:1.5
D3:1.5 F#3+A3:1.5 R:3
G3:1.5 B3+D4:1.5 F#3:1.5 A3+C4:1.5
E3:1.5 G3+B3:1.5 D3:1.5 F#3+A3:1.5
C3:1.5 E3+G3:1.5 A2:1.5 C3+E3:1.5
D3:1.5 F#3+C4:1.5 A3:1 R:2
E3+G3+B3:3 D3+F#3+A3:3
C3+E3+G3:3 B2+D3+G3:3
A2+C3+E3:3 D3+F#3+A3:3
G2+B2+D3:4 R:2
C3+E3+G3:3 A2+C3+E3:3
D3+F#3+A3:3 D3+F#3+C4:3
G2+B2+D3:4 R:2''',
 tempos=[62,63,62,60,62,63,62,60,62,62,62,60,64,63,62,60,62,63,62,60,61,60,58],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,23)],sections={1:'p',9:'mp',13:'mf',15:'mp',17:'p',21:'pp'},lower_sections={1:'pp',9:'pp',13:'p',17:'pp'},hairpins=[('crescendo',9,11),('diminuendo',13,16)],
 pedal=[[i*6+.05,i*6+(2.85 if i==11 else 3.85 if i in [3,7,15,19,22] else 5.8)] for i in range(23)])
p=study(op=333,title='Sedge Undercurrent',key='d',fifths=-1,meter='5/4',bpm=56,parent=322,
 source=dict(source_opus=322,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['D','F','E','A'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=5,pitches=['D','F','E','A']),
 description='The left hand carries a low minor song while upper chords change every three beats across five-beat bars. Their points of agreement move through the phrase. A more active middle passage disturbs that equilibrium; the final return retains the melody while its upper chord changes become still.',
 technical='Voice the lower song clearly without making it heavy. Follow the tied upper chords through bar lines: their three-beat pulse is independent of the five-beat melody. The middle passage asks for measured lower-hand turns and quiet upper releases.',
 rh='''F4+A4:3 E4+G4:2~
E4+G4:1 F4+A4:3 G4+Bb4:1~
G4+Bb4:2 F4+A4:3
E4+G4:3 F4+A4:2~
F4+A4:1 E4+G4:3 E4+A4:1~
E4+A4:2 R:3
F4+A4:3 E4+G4:2~
E4+G4:1 F4+A4:3 G4+Bb4:1~
G4+Bb4:2 F4+A4:3
E4+G4:3 F4+A4:2~
F4+A4:1 G4+Bb4:3 A4+C5:1~
A4+C5:2 R:3
G4+Bb4:2 A4+C5:1 Bb4+D5:2
A4+C5:2 G4+Bb4:1 F4+A4:2
E4+G4:2 F4+A4:1 G4+Bb4:2
E4+A4:3 R:2
F4+A4:5
E4+G4:5
G4+Bb4:5
F4+A4:5
E4+G4:3 F4+A4:2
E4+A4:3 R:2
F4+A4:3 E4+G4:2
F4+A4:4 R:1''',
 lh='''D3:1 F3:1 E3:1 A3:2
G3:1 F3:1 E3:1 D3:2
C3:1 E3:1 G3:1 Bb3:2
A3:1 G3:1 F3:1 E3:1 D3:1
Bb2:1 D3:1 F3:1 E3:1 C#3:1
A2:2 R:3
D3:1 F3:.5 E3:.5 A3:2 G3:1
F3:1 G3:.5 F3:.5 E3:1 D3:2
C3:1 E3:.5 F3:.5 G3:1 Bb3:2
A3:1 G3:.5 A3:.5 F3:1 E3:1 D3:1
Bb2:1 D3:1 F3:1 G3:1 A3:1
C4:2 R:3
Bb3:1 A3:.5 G3:.5 F3:1 G3:1 D4:1
C4:1 Bb3:.5 A3:.5 G3:1 F3:1 E3:1
D3:1 F3:.5 E3:.5 D3:1 C3:1 Bb2:1
A2:1 C#3:1 E3:1 R:2
D3:1 F3:1 E3:1 A3:2
G3:1 F3:1 E3:1 D3:2
C3:1 E3:1 G3:1 Bb3:2
A3:1 G3:1 F3:1 E3:1 D3:1
Bb2:1 D3:1 F3:1 E3:1 C#3:1
A2:3 R:2
D3:2 F3:1 E3:2
D3:4 R:1''',
 tempos=[56,57,56,57,56,53,56,57,58,57,58,54,59,58,56,53,56,57,56,56,55,53,53,51],
 phrases=[],lower_phrases=[(1,6),(7,12),(13,16),(17,22),(23,24)],sections={1:'pp',13:'p',17:'pp'},lower_sections={1:'p',7:'mp',13:'mf',15:'mp',17:'p',23:'pp'},
 pedal=[[i*5+.05,i*5+(1.85 if i in [5,11] else 2.85 if i in [15,21] else 3.85 if i==23 else 4.85)] for i in range(24)])
p['performance']['lower_entries']=[[0,120]]
p['performance']['phrase_arcs']=[[0,30,4],[30,60,4],[60,80,5],[80,110,4],[110,120,2]]
study(op=334,title='Iris Driftway',key='Db',fifths=-5,meter='9/8',bpm=60,parent=326,
 source=dict(source_opus=326,source_hand='lh',source_start_beat=0,source_end_beat=4,source_pitches=['Db','C','Bb','Ab'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4.5,pitches=['Db','C','Bb','Ab']),
 description='A five-bar song drifts over unequal bass gestures. Four quintuplet figures shorten its remembered intervals into a different current, followed by a plain return supported by a different bass. A low final question preserves a trace of that restlessness.',
 technical='Place each five-note group evenly across two quarter beats while keeping the surrounding compound pulse unforced. Distinguish the longer melody from the bass gestures; the final question is quiet and remains in tempo.',
 rh='''Db5:1 C5:.5 Bb4:.5 Ab4:2.5
F4:1.5 Ab4:1 Bb4:.5 C5:1.5
Eb5:2 Db5:.5 C5:1 Bb4:1
Ab4:1.5 Gb4:1.5 F4:1.5
Eb4:1 F4:.5 Ab4:1.5 R:1.5
Bb4:1.5 Db5:1.5 F5:1.5
Eb5:1.5 Db5:.5 C5:1 Bb4:1.5
Ab4:3 R:1.5
Db5:2/5 Eb5:2/5 F5:2/5 Eb5:2/5 Db5:2/5 C5:1.5 Bb4:1
C5:2/5 Db5:2/5 Eb5:2/5 F5:2/5 Eb5:2/5 Db5:1.5 Ab4:1
Bb4:2/5 C5:2/5 Db5:2/5 Eb5:2/5 F5:2/5 Gb5:1.5 F5:1
Eb5:2/5 F5:2/5 Gb5:2/5 F5:2/5 Eb5:2/5 C5:1 R:1.5
Db5:1 C5:.5 Bb4:.5 Ab4:2.5
F4:1.5 Ab4:1 Bb4:.5 C5:1.5
Eb5:2 Db5:.5 C5:1 Bb4:1
Ab4:1.5 Gb4:1.5 F4:1.5
Eb4:1 F4:.5 Ab4:1.5 R:1.5
Bb4:1.5 Ab4:1.5 F4:1.5
Gb4:1.5 Bb4:1 Ab4:.5 Gb4:1.5
F4:1.5 Eb4:1.5 Db4:1.5
F4:1.5 Eb4:1.5 Ab4:1.5
Eb4:3 R:1.5''',
 lh='''Db3:.5 Ab3:1 F3:.5 Eb3:1 Ab2:1.5
Bb2:.5 F3:1 Db3:.5 Ab2:1 F3:1.5
Gb2:.5 Db3:1 Bb2:.5 Eb3:1 Gb3:1.5
Ab2:.5 Eb3:1 C3:.5 Db3:1 Ab2:1.5
Db3:.5 F3:1 Ab3:1.5 R:1.5
Gb2:.5 Db3:1 Bb2:.5 Db3:1 F3:1.5
Eb3:.5 Bb3:1 Eb3:.5 Ab2:1 Eb3:1.5
Ab2:.5 C3:1 Gb3:1.5 R:1.5
Bb2:.5 F3:1 Db3:.5 Ab2:1 F3:1.5
Db3:.5 Ab3:1 F3:.5 Eb3:1 Ab2:1.5
Gb2:.5 Db3:1 Bb2:.5 Db3:1 Gb3:1.5
Ab2:.5 Eb3:1 Gb3:.5 C3:1 R:1.5
Bb2:.5 F3:1 Db3:.5 Ab2:1 F3:1.5
Gb2:.5 Db3:1 Bb2:.5 Db3:1 F3:1.5
Eb3:.5 Bb3:1 Eb3:.5 Ab2:1 Eb3:1.5
Db3:.5 Ab3:1 F3:.5 Eb3:1 Ab2:1.5
Db3:.5 F3:1 Ab3:1.5 R:1.5
Gb2:1.5 Bb2+Db3:1.5 F3:1.5
Cb3:1.5 Eb3+Gb3:1.5 Bb2:1.5
Db3:1.5 F3+Ab3:1.5 Ab2:1.5
Gb2+Bb2+Db3:1.5 Ab2+C3+Gb3:1.5 Db3+F3+Ab3:1.5
Db3+F3+Ab3:3 R:1.5''',
 tempos=[60,61,60,60,57,61,60,57,62,63,64,58,60,61,60,60,57,60,59,58,58,57],
 phrases=[(1,5),(6,8),(9,12),(13,17),(18,20),(21,22)],sections={1:'p',6:'mp',9:'mp',11:'mf',12:'p',13:'p',18:'pp'},lower_sections={1:'pp',9:'p',13:'pp'},
 tuplet_spans=[dict(hand='rh',start_beat=s,end_beat=s+2,actual=5,normal=4,stem='down',show_number='both') for s in [36,40.5,45,49.5]],
 pedal=[[i*4.5+.05,i*4.5+(2.85 if i in [4,7,11,16,21] else 4.3)] for i in range(22)])
p=study(op=335,title='Alder Sway',key='A',fifths=3,meter='3/4',bpm=58,parent=324,
 source=dict(source_opus=324,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','G#','F#','E'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','G#','F#','E']),
 description='A quiet dance rocks in two dotted gestures against three melodic beats. A shortened bar leaves it briefly unbalanced; later two expanded bars allow its descending phrase to linger. The last dance retains these memories in a softened, compact conclusion.',
 technical='Keep the dotted accompaniment independent of the three-beat melody. Count the isolated 2/4 and 4/4 bars without abrupt changes of pulse. Shape the upper line through its syncopations and keep the bass from accenting every bar.',
 rh='''A5:1 G#5:.5 F#5:.5 E5:1
C#5:1 E5:1 F#5:1
B5:1 A5:1 G#5:1
F#5:2 E5:1
D5:1 F#5:.5 E5:.5 C#5:1
B4:1 D5:1 C#5:.5 B4:.5
E5:1 R:1
R:.5 A5:1 G#5:.5 F#5:.5 E5:.5
C#5:.5 E5:1 F#5:.5 A5:1
G#5:1 F#5:.5 E5:.5 D5:1
C#5:1 E5:.5 F#5:.5 G#5:1
B5:1 C#6:.5 B5:.5 A5:1
G5:2 F5:1 E5:1
D5:1 C5:1 B4:1 R:1
A5:1 G#5:.5 F#5:.5 E5:1
C#5:1 E5:1 F#5:1
B5:1 A5:1 G#5:1
F#5:2 E5:1
D5:1 F#5:.5 E5:.5 C#5:1
B4:1 D5:1 C#5:.5 B4:.5
E5:1 R:1
D5:1 C#5:1 B4:1
A4:1 B4:1 G#4:1
A4:2 R:1''',
 lh='''A2+E3:1.5 C#3+G#3:1.5
F#2+C#3:1.5 A2+E3:1.5
D3+A3:1.5 E3+B3:1.5
B2+F#3:1.5 E3+G#3:1.5
D3+A3:1.5 F#2+C#3:1.5
B2+F#3:1.5 E3+G#3:1.5
E3+B3:1 R:1
A2+E3:1.5 C#3+G#3:1.5
F#2+C#3:1.5 A2+E3:1.5
D3+A3:1.5 E3+B3:1.5
A2+E3:1.5 C#3+G#3:1.5
F#3+A3:1.5 E3+G#3:1.5
C3+E3+G3:2 A2+C3+E3:2
D3+F3+A3:2 E3+G#3:1 R:1
F#2+C#3:1.5 A2+E3:1.5
D3+A3:1.5 C#3+G#3:1.5
B2+F#3:1.5 E3+B3:1.5
D3+A3:1.5 E3+G#3:1.5
D3+A3:1.5 F#2+C#3:1.5
B2+F#3:1.5 E3+G#3:1.5
E3+B3:1 R:1
D3+F#3+A3:1.5 B2+D3+F#3:1.5
E3+G#3+B3:1.5 E3+G#3+D4:1.5
A2+C#3+E3:2 R:1''',
 meters=['3/4']*6+['2/4']+['3/4']*5+['4/4']*2+['3/4']*6+['2/4']+['3/4']*3,
 tempos=[58,59,60,59,58,57,55,58,60,59,61,62,58,55,58,59,60,59,58,57,55,57,56,54],
 phrases=[(1,4),(5,7),(8,10),(11,14),(15,18),(19,21),(22,24)],sections={1:'p',8:'mp',11:'mf',12:'f',13:'mp',15:'p',22:'pp'},lower_sections={1:'pp',11:'p',15:'pp'},hairpins=[('crescendo',8,12),('diminuendo',13,14)])
lengths=[int(m.split('/')[0])*4/int(m.split('/')[1]) for m in p['meters']]
offsets=[sum(lengths[:i]) for i in range(25)]
p['pedal_spans']=[[offsets[i]+.05,offsets[i+1]-(1.15 if i in [6,13,20,23] else .15)] for i in range(24)]

study(op=336,title='Myrtle Interval',key='F',fifths=-1,meter='4/4',bpm=55,parent=323,
 source=dict(source_opus=323,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['F','E','D','C'],transposition_semitones=0),motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['F','E','D','C']),
 description='A descending song grows around a quieter voice entering after the beat. A seven-bar opening gives way to a five-bar ascent; the inner line then becomes more mobile while the upper song lengthens. The last eight bars gradually draw the three voices into alignment, ending with a small rising question.',
 technical='Hold each upper duration while placing the inner voice softly, especially where its half notes cross the bar line. Keep the bass spacious and distinguish the middle voice from the singing top. Release each tied inner note exactly where its next written note begins.',
 rh='''F5:1 E5:.5 D5:.5 C5:2
D5:2 E5:1 F5:1
G5:3 F5:1
E5:2 D5:1 C5:1
Bb4:2 C5:2
D5:1 E5:1 F5:2
E5:3 R:1
F5:2 A5:2
G5:1 A5:1 Bb5:2
C6:3 Bb5:1
A5:2 G5:1 F5:1
E5:3 R:1
F5:2 E5:1 D5:1
C5:4
D5:2 E5:1 F5:1
G5:3 F5:1
E5:2 D5:1 C5:1
Bb4:2 C5:2
D5:1 E5:1 F5:2
E5:3 R:1
F5:3 E5:1
D5:3 C5:1
Bb4:2 D5:2
C5:2 E5:2
F5:4
E5:2 D5:2
C5:3 R:1
G5:4''',
 rh_inner='''R:1 A4:2 G4:1~
G4:1 Bb4:2 A4:1~
A4:1 C5:2 Bb4:1~
Bb4:1 A4:2 G4:1
F4:3 G4:1
Bb4:3 A4:1
G4:3 R:1
R:1 C5:2 D5:1~
D5:1 F5:2 E5:1~
E5:1 G5:2 F5:1~
F5:1 E5:2 C5:1
Bb4:3 R:1
A4:1 Bb4:1 A4:1 G4:1
G4:1 A4:1 Bb4:1 A4:1
Bb4:1 A4:1 G4:1 A4:1
C5:1 Bb4:1 A4:1 C5:1
Bb4:1 A4:1 G4:2
F4:2 G4:2
Bb4:2 A4:2
G4:3 R:1
A4:4
F4:4
G4:4
Bb4:4
A4:4
G4:2 Bb4:2
A4:3 R:1
C5+E5:4''',
 lh='''F3:2 C4:2
Bb2:2 F3:2
G3:2 D4:2
C3:2 G3:2
Bb2:2 F3:2
G3:2 Bb3:2
C3:2 G3:1 R:1
D3:2 A3:2
Eb3:2 Bb3:2
Ab2:2 Eb3:2
Db3:2 Ab3:2
C3:2 G3:1 R:1
D3:2 A3:2
A2:2 E3:2
Bb2:2 F3:2
G3:2 D4:2
C3:2 G3:2
Bb2:2 F3:2
G3:2 Bb3:2
C3:2 G3:1 R:1
D3+A3:4
Bb2+F3:4
Eb3+Bb3:4
C3+G3:4
F3+C4:4
G3+D4:2 C3+G3:2
F3+C4:3 R:1
F3+A3:4''',
 tempos=[55,56,57,56,55,56,53,55,56,58,56,53,55,55,56,57,56,55,56,53,54,54,55,54,53,53,52,52],
 phrases=[(1,7),(8,12),(13,20),(21,24),(25,28)],sections={1:'p',8:'mp',10:'mf',12:'p',13:'p',21:'pp'},lower_sections={1:'pp',8:'p',13:'pp'},
 voice_phrases=[dict(voice='inner',start_beat=1,end_beat=27,swell=-2),dict(voice='inner',start_beat=29,end_beat=47,swell=-2),dict(voice='inner',start_beat=48,end_beat=79,swell=2)],
 pedal=[[i*4+.05,i*4+(2.85 if i in [6,11,19,26] else 3.8)] for i in range(28)],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=680))

p=study(op=337,title='Reed Tidelock',key='b',fifths=2,meter='7/8',bpm=52,parent=328,
 source=dict(source_opus=328,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['B','D','C#','F#'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['B','D','C#','F#']),
 description='Even melodic steps spill across a seven-eighth ground, repeatedly arriving between its bass gestures. A central six-eighth passage gathers both hands into a gentle rocking motion. When the uneven ground returns, the melody carries longer memories of that stillness and closes without a final flourish.',
 technical='Follow the tied quarter-beat pulse across the opening seven-eighth bars without accenting the tie continuations. Keep the change into 6/8 at the same quarter-note speed. In the return, sustain the longer line while the uneven lower gestures remain supple.',
 rh='''B4:1 D5:1 C#5:1 F#5:.5~
F#5:.5 E5:1 D5:1 C#5:1
B4:1 A4:1 C#5:1 E5:.5~
E5:.5 D5:1 C#5:1 B4:1
A4:1 C#5:1 E5:1 G5:.5~
G5:.5 F#5:1 E5:1 D5:1
C#5:1 B4:1 A#4:1 C#5:.5~
C#5:.5 B4:2 R:1
D5:1 F#5:1 A5:1 G5:.5~
G5:.5 F#5:1 E5:1 D5:1
C#5:1 E5:1 G5:1 B5:.5~
B5:.5 A5:1 G5:1 F#5:1
E5:1 G5:1 A5:1 C6:.5~
C6:.5 B5:1 A5:1 G5:1
F#5:1 E5:1 C#5:1 A#4:.5~
A#4:.5 B4:2 R:1
D5:1.5 C#5:.5 B4:1
A4:1.5 F#4:1.5
G4:1.5 B4:.5 D5:1
C#5:1.5 A4:1.5
B4:1.5 D5:.5 F#5:1
E5:1.5 D5:1.5
C#5:1.5 A#4:.5 C#5:1
B4:2 R:1
B4:1 D5:1 C#5:1 F#5:.5~
F#5:2 E5:.5 D5:1
C#5:1 E5:1 G5:1 F#5:.5~
F#5:2 E5:.5 D5:1
B4:2 A4:.5 C#5:1
E5:2 D5:.5 B4:1
C#5:1 B4:1 A#4:1 C#5:.5
B4:2.5 R:1''',
 lh='''B2:1 F#3:.5 D3:1 A2:.5 B2:.5
G2:1 D3:.5 B2:1 F#3:.5 D3:.5
A2:1 E3:.5 C#3:1 G3:.5 C#3:.5
F#2:1 C#3:.5 A2:1 E3:.5 C#3:.5
E3:1 B3:.5 G3:1 D3:.5 B2:.5
G2:1 D3:.5 B2:1 F#3:.5 D3:.5
F#2:1 C#3:.5 E3:1 A#2:.5 C#3:.5
B2:1 D3+F#3:1.5 R:1
D3:1 A3:.5 F#3:1 C#3:.5 A2:.5
G2:1 D3:.5 B2:1 F#3:.5 D3:.5
A2:1 E3:.5 C#3:1 G3:.5 C#3:.5
E3:1 B3:.5 G3:1 D3:.5 B2:.5
C3:1 G3:.5 E3:1 B2:.5 G2:.5
G2:1 D3:.5 B2:1 F#3:.5 D3:.5
F#2:1 C#3:.5 E3:1 A#2:.5 C#3:.5
B2:1 D3+F#3:1.5 R:1
G2:1.5 B2+D3:1.5
D3:1.5 F#3+A3:1.5
E3:1.5 G3+B3:1.5
A2:1.5 C#3+E3:1.5
G2:1.5 B2+D3:1.5
E3:1.5 G3+B3:1.5
F#2:1.5 A#2+E3:1.5
B2+D3+F#3:2 R:1
B2:1 F#3:.5 D3:1 A2:.5 B2:.5
G2:1 D3:.5 B2:1 F#3:.5 D3:.5
A2:1 E3:.5 C#3:1 G3:.5 C#3:.5
E3:1 B3:.5 G3:1 D3:.5 B2:.5
G2:1 D3:.5 B2:1 F#3:.5 D3:.5
A2:1 E3:.5 C#3:1 G3:.5 C#3:.5
F#2:1 C#3:.5 E3:1 A#2:.5 C#3:.5
B2+D3+F#3:2.5 R:1''',
 meters=['7/8']*16+['6/8']*8+['7/8']*8,
 tempos=[52,53,54,53,54,53,52,50,54,55,56,55,57,55,53,50,51,52,53,52,53,52,51,49,52,53,54,53,52,52,51,50],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32)],sections={1:'p',9:'mp',13:'mf',17:'pp',25:'p',29:'pp'},lower_sections={1:'pp',9:'p',17:'pp'},hairpins=[('crescendo',9,13),('diminuendo',14,16)])
lengths=[int(m.split('/')[0])*4/int(m.split('/')[1]) for m in p['meters']]
offsets=[sum(lengths[:i]) for i in range(33)]
p['pedal_spans']=[[offsets[i]+.05,offsets[i+1]-(1.15 if i in [7,15,23,31] else .15)] for i in range(32)]

study(op=338,title='Orchid Suspension',key='Ab',fifths=-4,meter='6/4',bpm=58,parent=329,
 source=dict(source_opus=329,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['Ab','G','F','Eb'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Ab','G','F','Eb']),
 description='A broad A-flat song rests over widely spaced bass notes. Its middle opens into five quiet lower-hand ripples, each followed by a long settling interval. The melody later returns in fragments separated by silence; one remembered ripple in the coda leads to an unhurried major seventh.',
 technical='Shape each five-note lower-hand group across exactly two quarter beats, then let its longer notes settle without delaying the next bar. Keep the sustained upper voice light. The shared silences require a full pedal release, while the final major seventh should remain softly voiced.',
 rh='''Ab5:1 G5:1 F5:1 Eb5:3
C5:2 Eb5:1 F5:3
G5:3 F5:1 Eb5:2
Db5:2 F5:2 Ab5:2
G5:3 Eb5:1 R:2
C5+Eb5:2 Db5+F5:2 Eb5+G5:2
F5+Ab5:3 Eb5+G5:1 Db5+F5:2
Eb5+G5:4 R:2
C6:3 Bb5:1 Ab5:2
Bb5:3 Ab5:1 G5:2
F5:2 Ab5:2 Db6:2
Eb6:3 Db6:1 C6:2
Bb5:2 Ab5:2 G5:2
Ab5:2 R:1 G5:1 F5:2
Eb5:3 R:1 C5:2
Eb5:2 R:1 F5:1 G5:2
Ab5:2 G5:1 F5:1 Eb5:2
Db5:3 C5:1 R:2
Bb4:2 Db5:2 F5:2
Eb5:3 Db5:1 C5:2
Db5:2 F5:2 Ab5:2
G5:3 F5:1 Eb5:2
C5:2 Bb4:2 Ab4:2
Bb4:2 C5:2 Eb5:2
G5:6''',
 lh='''Ab2:2 Eb3:2 C3:2
F2:2 C3:2 Ab2:2
Eb3:2 Bb3:2 G3:2
Db3:2 Ab3:2 F3:2
Eb3:2 Bb3:2 R:2
Ab2:2 Eb3:2 C3:2
Db3:2 Ab3:2 F3:2
Eb3:2 Bb3:2 R:2
Ab2:2/5 Bb2:2/5 C3:2/5 Eb3:2/5 C3:2/5 Eb3:2 G3:2
G2:2/5 Bb2:2/5 D3:2/5 Eb3:2/5 D3:2/5 Bb2:2 F3:2
Db3:2/5 Eb3:2/5 F3:2/5 Ab3:2/5 F3:2/5 Db3:2 Ab3:2
Gb2:2/5 Ab2:2/5 Bb2:2/5 Db3:2/5 Eb3:2/5 Db3:2 F3:2
Eb3:2/5 F3:2/5 G3:2/5 Bb3:2/5 G3:2/5 Bb2:2 Db3:2
F2+Ab2+C3:2 R:1 Eb3+G3:3
Ab2+Eb3:3 R:1 C3+G3:2
Db3+Ab3:2 R:1 F3+C4:3
Bb2+F3:2 Eb3+Bb3:2 Ab2+Eb3:2
Db3+Ab3:3 Eb3+G3:1 R:2
Bb2:2 F3:2 Ab3:2
Ab2:2 Eb3:2 C3:2
Db3:2 Ab3:2 F3:2
Eb3:2/5 F3:2/5 G3:2/5 Bb3:2/5 G3:2/5 Bb2:2 Db3:2
F3+Ab3:2 Db3+F3:2 Ab2+Eb3:2
Db3+F3:2 Eb3+G3:2 Ab2+Eb3:2
Ab2+C3+Eb3:6''',
 tempos=[58,59,58,60,56,60,61,56,59,60,61,62,59,57,56,58,59,55,57,58,59,58,56,56,56],
 phrases=[(1,5),(6,8),(9,13),(14,18),(19,22),(23,25)],sections={1:'p',6:'mp',9:'p',11:'mp',12:'mf',14:'pp',19:'p',23:'pp'},lower_sections={1:'pp',9:'pp',14:'pp'},
 tuplet_spans=[dict(hand='lh',start_beat=s,end_beat=s+2,actual=5,normal=4,stem='up',show_number='both') for s in [48,54,60,66,72,126]],
 pedal=sorted([[i*6+.05,i*6+(3.8 if i in [4,7,17] else 5.8)] for i in range(25) if i not in [13,14,15]]+[[78.05,79.8],[81.05,83.8],[84.05,86.8],[88.05,89.8],[90.05,91.8],[93.05,95.8]]),
 hairpins=[('crescendo',9,11),('diminuendo',12,13)],page_starts=[8,14,20],system_starts=[1,3,5,7,8,10,12,14,16,18,20,22,24])

p=study(op=339,title='Birch Crosscurrent',key='e',fifths=1,meter='4/4',bpm=60,parent=330,
 source=dict(source_opus=330,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['E','G','F#','B'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['E','G','F#','B']),
 description='A small E-minor song gradually loosens into different currents: short lower triplets, whole-bar nine-note upper figures, then nine-note bass answers. The original melody finally returns below quiet upper intervals. Its last phrase rises only far enough to leave the harmony open.',
 technical='Keep the quarter pulse internally through each whole-bar 9:8 group. The lower-hand answers carry the same even flow at a different register. Bring the bass melody forward in the final eight bars, allowing the upper intervals to remain a quiet frame.',
 rh='''E5:1 G5:.5 F#5:.5 B5:2
A5:1 G5:1 F#5:2
E5:1 D5:1 C5:2
B4:2 D5:1 E5:1
F#5:1 A5:1 G5:1 F#5:1
E5:3 R:1
G5:2 F#5:1 E5:1
D5:2 F#5:2
A5:2 G5:1 F#5:1
E5:2 G5:2
B5:2 A5:1 G5:1
F#5:2 D#5:1 R:1
E5:4/9 F#5:4/9 G5:4/9 B5:4/9 A5:4/9 G5:4/9 F#5:4/9 E5:4/9 D5:4/9
C5:2 E5:1 G5:1
G5:4/9 A5:4/9 B5:4/9 D6:4/9 C6:4/9 B5:4/9 A5:4/9 G5:4/9 F#5:4/9
E5:2 D5:1 C5:1
F#5:4/9 G5:4/9 A5:4/9 C6:4/9 B5:4/9 A5:4/9 G5:4/9 F#5:4/9 E5:4/9
D5:2 C5:1 B4:1
B4+D5:4
C5+E5:2 B4+D5:2
C5+E5:4
B4+D5:2 A4+C5:2
A4+C5:4
F#4+A4:2 D#4+F#4:1 R:1
G4+B4:4
F#4+A4:4
E4+G4:4
D4+F#4:4
E4+G4:2 F#4+A4:2
D#4+F#4:3 R:1
E4+G4:2 F#4+A4:2
G4+B4:4''',
 lh='''E3:1 B3:1 G3:2
C3:1 G3:1 E3:2
A2:1 E3:1 C3:2
G2:1 D3:1 B2:2
B2:1 F#3:1 D#3:2
E3:2 B2:1 R:1
C3:1/3 D3:1/3 E3:1/3 G3:1 E3:2
D3:1 A3:1 F#3:2
F#2:1/3 A2:1/3 C3:1/3 E3:1 A2:2
E3:1 B3:1 G3:2
A2:1/3 B2:1/3 C3:1/3 E3:1 G3:2
B2:1 F#3:1 D#3:1 R:1
E3:1 G3:1 B3:1 G3:1
C3:1 E3:1 G3:1 B3:1
G2:1 B2:1 D3:1 F#3:1
C3:1 E3:1 G3:1 E3:1
A2:1 C3:1 E3:1 G3:1
B2:1 D#3:1 F#3:1 A3:1
E3:4/9 F#3:4/9 G3:4/9 B3:4/9 A3:4/9 G3:4/9 F#3:4/9 E3:4/9 D3:4/9
C3:1 G3:1 E3:1 B2:1
A2:4/9 B2:4/9 C3:4/9 E3:4/9 D3:4/9 C3:4/9 B2:4/9 A2:4/9 G2:4/9
G2:1 D3:1 B2:1 E3:1
F#2:4/9 G2:4/9 A2:4/9 C3:4/9 B2:4/9 A2:4/9 G2:4/9 F#2:4/9 E2:4/9
B2:1 D#3:1 F#3:1 R:1
E3:1 G3:.5 F#3:.5 B3:2
A3:1 G3:1 F#3:2
E3:1 D3:1 C3:2
B2:2 D3:1 E3:1
F#3:1 A3:1 G3:1 F#3:1
B2:2 D#3:1 R:1
E3:1 G3:1 A3:1 F#3:1
B3:4''',
 tempos=[60,61,60,60,61,58,61,62,62,63,64,59,62,61,64,61,63,60,61,60,61,60,60,57,59,60,59,59,60,57,58,58],
 phrases=[(1,6),(7,12),(13,18),(19,24)],lower_phrases=[(25,30),(31,32)],sections={1:'p',7:'mp',13:'mp',15:'mf',19:'pp',25:'pp'},lower_sections={1:'pp',7:'p',19:'mp',25:'p',31:'pp'},
 tuplet_spans=[dict(hand='lh',start_beat=s,end_beat=s+1,actual=3,normal=2,stem='up') for s in [24,32,40]]+[dict(hand=h,start_beat=s,end_beat=s+4,actual=9,normal=8,stem='down' if h=='rh' else 'up',show_number='both') for h,ss in [('rh',[48,56,64]),('lh',[72,80,88])] for s in ss],
 pedal=[[i*4+.05,i*4+(2.8 if i in [5,11,23,29] else 3.8)] for i in range(32)],page_starts=[9,17,25])
p['performance']['lower_entries']=[[72,96],[96,128]]

p=study(op=340,title='Velvet Isobar',key='Eb',fifths=-3,meter='4/4',bpm=50,parent=331,
 source=dict(source_opus=331,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['Eb','D','C','Bb']),
 description='Willow Hesitation returns above a changed bass and pauses in an empty bar. Its melody expands, passes into the lower hand, and opens into two seven-note flights. A late recollection gradually releases the repeating ground. The last upper notes fall away while the lower harmony remains held.',
 technical='Keep the three-three-two bass supple and the written empty bar fully silent. The lower-hand song needs its own legato and foreground. Place each 7:6 upper group over three quarter beats, then let the broad final recollection release its pulse without an exaggerated slowing.',
 rh='''Eb5:1 D5:.5 C5:.5 Bb4:2
G4:1 Bb4:1 C5:1 D5:1
F5:2 Eb5:1 D5:1
C5:1 Bb4:2 R:1
R:4
R:1 Eb5:1 D5:.5 C5:.5 Bb4:1
G4:1 Bb4:.5 C5:.5 D5:1 Eb5:1
F5:2 G5:1 Ab5:1
G5:1 F5:.5 Eb5:.5 D5:1 C5:1
Eb5:2 F5:1 G5:1
Ab5:1 G5:1 F5:1 D5:1
Eb5:3 R:1
G4+Bb4:4
F4+Ab4:4
Eb4+G4:4
F4+Ab4:2 G4+Bb4:2
F4+A4:4
F4+Ab4:3 R:1
Bb4:1 D5:1 F5:2
Eb5:1 C5:1 G4:2
Ab4:1 C5:1 Eb5:2
F5:3/7 G5:3/7 Ab5:3/7 C6:3/7 Bb5:3/7 Ab5:3/7 G5:3/7 F5:1
Eb5:1 G5:1 Bb5:2
Ab5:3/7 Bb5:3/7 C6:3/7 Eb6:3/7 D6:3/7 C6:3/7 Bb5:3/7 Ab5:1
G5:1 F5:.5 Eb5:.5 D5:1 C5:1
Bb4:1 Ab4:1 G4:1 F4:1
Bb4:3 R:1
R:1 Eb5:1 D5:.5 C5:.5 Bb4:1
G4:1 Bb4:1 C5:1 D5:1
F5:2 Eb5:1 D5:1
C5:1 Bb4:1 Ab4:1 G4:1
Ab4:2 C5:1 Eb5:1
D5:2 C5:1 Bb4:1
G4:2 F4:1 Eb4:1
F4:1 G4:1 Bb4:1 C5:1
Eb5:1 D5:1 R:2''',
 lh='''C3:.75 Eb3:.75 G3:.5 Eb3:.75 G3:.75 Eb3:.5
Ab2:.75 C3:.75 Eb3:.5 C3:.75 Eb3:.75 C3:.5
F3:.75 Ab3:.75 C4:.5 Ab3:.75 C4:.75 F3:.5
Bb2:.75 D3:.75 Ab3:.5 F3:1 R:1
R:4
C3:.75 Eb3:.75 G3:.5 Eb3:.75 G3:.75 Eb3:.5
Ab2:.75 C3:.75 Eb3:.5 C3:.75 Eb3:.75 C3:.5
Db3:.75 F3:.75 Ab3:.5 F3:.75 Ab3:.75 F3:.5
Bb2:.75 D3:.75 F3:.5 Ab3:.75 F3:.75 D3:.5
C3:.75 Eb3:.75 G3:.5 Eb3:.75 G3:.75 Eb3:.5
F3:.75 Ab3:.75 C4:.5 F3:.75 Bb2:.75 D3:.5
Eb3:1 G3+Bb3:2 R:1
Eb3:1 D3:.5 C3:.5 Bb2:2
G2:1 Bb2:1 C3:1 D3:1
Eb3:2 G3:1 Bb3:1
Ab3:1 G3:1 F3:1 Eb3:1
D3:1 C3:1 Bb2:1 A2:1
Bb2:3 R:1
Bb2:1/3 D3:1/3 F3:1/3 Ab3:1 F3:2
C3:1/3 Eb3:1/3 G3:1/3 Bb3:1 G3:2
Ab2:1/3 Bb2:1/3 C3:1/3 Eb3:1 G3:2
Db3:1 F3:1 Ab3:1 F3:1
Eb3:1/3 F3:1/3 G3:1/3 Bb3:1 G3:2
F3:1 Ab3:1 C4:1 Ab3:1
C3:1 Eb3:1 G3:1 Bb2:1
Ab2:1 C3:1 Eb3:1 A2:1
Bb2+D3+Ab3:3 R:1
C3:.75 Eb3:.75 G3:.5 Eb3:.75 G3:.75 Eb3:.5
Ab2:.75 C3:.75 Eb3:.5 C3:.75 Eb3:.75 C3:.5
F3:1 Ab3:1 C4:1 Ab3:1
Bb2:1 D3:1 Ab3:1 F3:1
Ab2:1 C3+Eb3:1 G3:2
Bb2:1 D3+F3:1 Ab3:2
Eb3+G3+Bb3:4
Ab2+C3+Eb3:2 Bb2+D3+Ab3:2
Eb3+G3+Bb3:4''',
 tempos=[50,51,52,49,50,50,51,53,52,52,53,49,50,51,52,51,50,48,52,53,54,55,54,56,53,51,49,50,51,52,51,50,50,49,49,49],
 phrases=[(1,4),(6,9),(10,12),(19,22),(23,27),(28,31),(32,36)],lower_phrases=[(13,18)],sections={1:'p',6:'p',8:'mp',13:'pp',19:'mp',22:'mf',24:'f',25:'mp',28:'p',34:'pp'},lower_sections={1:'pp',13:'p',19:'pp',24:'p',28:'pp'},
 tuplet_spans=[dict(hand='lh',start_beat=s,end_beat=s+1,actual=3,normal=2,stem='up') for s in [72,76,80,88]]+[dict(hand='rh',start_beat=s,end_beat=s+3,actual=7,normal=6,stem='down',show_number='both') for s in [84,92]],
 pedal=[[i*4+.05,i*4+(2.8 if i in [3,11,17,26] else 3.8)] for i in range(36) if i!=4],hairpins=[('crescendo',19,22),('diminuendo',25,27)],
 system_starts=list(range(1,37,2)),page_starts=[9,17,25,33])
p['performance']['lower_entries']=[[48,72]]
