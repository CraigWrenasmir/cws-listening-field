"""Quiet Virtuosity, CWS Op. 361–370. Individually authored piano studies."""
from weather_common import make_study
PIECES=[]
def study(**kwargs):
    p=make_study(**kwargs);PIECES.append(p);return p

p=study(op=361,title='Camellia Filigree',key='f',fifths=-4,meter='5/4',bpm=60,parent=223,
 source=dict(source_opus=223,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['D','C','A','G'],transposition_semitones=3),motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['F','Eb','C','Bb']),
 description='A falling song acquires a quieter companion in double thirds. The companion changes the harmony beneath the remembered upper notes, then steps out alone for four bars. A longer paired answer opens into sixths and climbs through a single soft high point. Its last gesture becomes a plain melody again, with the bass withdrawing before the final upper note.',
 technical='Voice the upper edge of the double notes without hardening either attack. Recognise the lower partner when it is exposed alone in bars 13–16. Balance the wider sixths and brief paired runs at the same quiet touch; keep the final single line continuous after the bass releases.',
 rh='''F5:1 Eb5:.5 C5:.5 Bb4:3
Db5:2 C5:1 Ab4:2
G4:1 Bb4:1 C5:1 Eb5:2
Db5:1 C5:.5 Bb4:.5 Ab4:1 G4:2
F4:1 Ab4:1 G4:1 F4:2
Db5+F5:1 C5+Eb5:.5 Ab4+C5:.5 G4+Bb4:3
Bb4+Db5:2 Ab4+C5:1 F4+Ab4:2
E4+G4:1 G4+Bb4:1 Ab4+C5:1 C5+Eb5:2
Bb4+Db5:1 Ab4+C5:.5 G4+Bb4:.5 F4+Ab4:1 Eb4+G4:2
Db4+F4:1 F4+Ab4:1 Eb4+G4:1 Db4+F4:2
Eb4+G4:.5 F4+Ab4:.5 G4+Bb4:.5 Ab4+C5:.5 Bb4+Db5:1 Ab4+C5:2
G4+Bb4:1 F4+Ab4:1 Eb4+G4:1 F4+Ab4:1 R:1
Db5:1 C5:.5 Ab4:.5 G4:3
Bb4:2 Ab4:1 F4:2
E4:1 G4:1 Ab4:1 C5:2
Bb4:1 Ab4:.5 G4:.5 F4:1 Eb4:2
Db5+F5:1 C5+Eb5:.5 Ab4+C5:.5 D4+Bb4:3
Bb4+Db5:1 Ab4+C5:1 F4+Ab4:1 G4+Bb4:2
G4+C5:.5 Ab4+Db5:.5 Bb4+Eb5:1 Ab4+F5:1 G4+Eb5:2
F4+Db5:1 Eb4+C5:1 Db4+Bb4:1 C4+Ab4:2
Bb3+G4:1 C4+Ab4:.5 Db4+Bb4:.5 Eb4+C5:1 F4+Db5:2
Eb4+C5:1 F4+Db5:1 G4+Eb5:.5 Ab4+F5:.5 G4+Eb5:2
F4+Db5:.5 G4+Eb5:.5 Ab4+F5:1 Bb4+G5:1 Ab4+F5:2
G4+Eb5:1 F4+Db5:1 Eb4+C5:1 Db4+Bb4:2
C4+Ab4:1 Db4+Bb4:1 Eb4+C5:1 F4+Ab4:1 R:1
G4:1 Bb4:.5 Ab4:.5 Eb5:2 C5:1
Db5:1 C5:.5 Bb4:.5 Ab4:1 G4:2
F4:2 Ab4:1 G4:1 F4:1''',
 lh='''Bb2:2 F3:1 G3:2
Db3:2 Ab3:1 F3:2
Eb3:2 Bb3:1 G3:2
Db3:2 Ab3:1 Eb3:2
F3:2 C3:1 F3:2
Bb2:2 F3:1 G3:2
Db3:2 Ab3:1 Bb3:2
C3:2 G3:1 Bb3:2
Db3:2 Ab3:1 Bb3:2
F3:2 C3:1 Db3:2
Eb3:2 Bb3:1 G3:2
F3:2 C3:1 F3:1 R:1
Db3+Ab3:5
Gb2+Db3:5
C3+G3:5
Eb3+Bb3:5
Bb2:2 F3:1 G3:2
Gb2:1 Db3:1 F3:1 Bb3:2
Eb3:2 Bb3:1 G3:2
Db3:2 Ab3:1 F3:2
Eb3:2 Bb2:1 Eb3:2
Ab2:1 Eb3:1 G3:1 C4:2
Db3:2 Ab3:1 F3:2
Eb3:1 Bb3:1 Ab3:1 F3:2
Ab2:1 Eb3:1 G3:1 F3:1 R:1
Eb3:2 Bb3:1 G3:2
Db3:2 Ab3:1 Eb3:2
F3:2 C3:2 R:1''',
 tempos=[60,61,62,61,59,60,61,62,61,59,62,60,59,60,61,59,60,62,63,61,62,64,65,62,60,60,61,61],
 phrases=[(1,5),(6,12),(13,16),(17,20),(21,25),(26,28)],lower_phrases=[(1,5),(6,10),(11,12),(17,20),(21,25),(26,28)],
 sections={1:'p',6:'p',13:'mp',17:'p',21:'mp',24:'p',26:'pp'},lower_sections={1:'pp',6:'pp',13:'pp',17:'pp',21:'p',25:'pp'},
 pedal=[[i*5+.05,i*5+(3.8 if i in [11,24,27] else 4.8)] for i in range(28)],hairpins=[('crescendo',6,9),('diminuendo',10,12),('crescendo',21,23),('diminuendo',24,25)])

p=study(op=362,title='Yarrow Continuum',key='c',fifths=-3,meter='9/8',bpm=63,parent=226,
 source=dict(source_opus=226,source_hand='rh',source_start_beat=7,source_end_beat=8,source_pitches=['D','F','A','C'],transposition_semitones=-2),motif=dict(hand='rh',start_beat=0,end_beat=1,pitches=['C','Eb','G','Bb']),
 description='A single continuous ribbon passes between the hands inside its phrases. The first journey rises and falls through minor-seventh colours; a slower bass song then opens space around the same flowing impulse. The returning ribbon changes its route and the positions of its handovers. A final plain phrase lets the minor landscape open into a quiet major arrival.',
 technical='Match the tone of the final note in one hand to the first in the other, preserving the written sixteenth-note stream without overlap. Use each hand’s rests to reposition; the left hand often shares the treble register. Let the slower bass song sing between the two long passages, and clear the pedal at each written change.',
 rh='''C5:.25 Eb5:.25 G5:.25 Bb5:.25 Ab5:.25 G5:.25 F5:.25 Eb5:.25 D5:.25 R:2.25
R:2.25 Eb5:.25 F5:.25 Ab5:.25 G5:.25 F5:.25 Eb5:.25 Db5:.25 C5:.25 Ab4:.25
Bb4:.25 C5:.25 Eb5:.25 F5:.25 G5:.25 Ab5:.25 G5:.25 F5:.25 Eb5:.25 R:2.25
R:2.25 F5:.25 G5:.25 Bb5:.25 Ab5:.25 G5:.25 F5:.25 Eb5:.25 Db5:.25 Bb4:.25
C5:.25 Eb5:.25 G5:.25 Ab5:.25 G5:.25 Eb5:.25 C5:.25 Bb4:.25 Ab4:.25 R:2.25
R:2.25 C5:.25 Db5:.25 F5:.25 Eb5:.25 Db5:.25 C5:.25 Bb4:.25 Ab4:.25 F4:.25
G4:.25 Bb4:.25 D5:.25 F5:.25 Eb5:.25 D5:.25 C5:.25 Bb4:.25 A4:.25 R:2.25
R:2.25 Bb4:.25 C5:.25 E5:.25 D5:.25 C5:.25 Bb4:.25 A4:.25 G4:.25 E4:.25
F4:.25 Ab4:.25 C5:.25 Eb5:.25 D5:.25 C5:.25 Bb4:.25 Ab4:.25 G4:.25 R:2.25
Ab4+C5:3 R:1.5
G4+Bb4:4.5
F4+Ab4:3 R:1.5
F4+A4:4.5
G4+B4:3 R:1.5
G4+C5:4.5
F4+Ab4:3 R:1.5
R:1.5 C5:.25 Eb5:.25 G5:.25 F5:.25 Eb5:.25 Db5:.25 C5:.25 Bb4:.25 Ab4:.25 G4:.25 Eb4:.25 C4:.25
Db4:.25 F4:.25 Ab4:.25 C5:.25 Db5:.25 Eb5:.25 R:3
R:2 D5:.25 F5:.25 A5:.25 G5:.25 F5:.25 Eb5:.25 D5:.25 C5:.25 Bb4:.25 G4:.25
A4:.25 C5:.25 E5:.25 G5:.25 A5:.25 G5:.25 E5:.25 C5:.25 B4:.25 A4:.25 R:2
R:1.5 Bb4:.25 Ab4:.25 G4:.25 F4:.25 Eb4:.25 C4:.25 Eb4:.25 G4:.25 Bb4:.25 C5:.25 D5:.25 Eb5:.25
F5:.25 Eb5:.25 C5:.25 Ab4:.25 G4:.25 Ab4:.25 R:3
R:2.25 Ab5:.25 G5:.25 F5:.25 Eb5:.25 D5:.25 C5:.25 Bb4:.25 G4:.25 Eb4:.25
F4:.25 A4:.25 C5:.25 Eb5:.25 F5:.25 G5:.25 A5:.25 G5:.25 F5:.25 R:2.25
R:1.5 F5:.25 Eb5:.25 D5:.25 C5:.25 Ab4:.25 G4:.25 F4:.25 D4:.25 C4:.25 D4:.25 F4:.25 Ab4:.25
G4:.25 B4:.25 D5:.25 F5:.25 G5:.25 F5:.25 R:3
E4:.5 G4:.5 C5:1 B4:.5 A4:.5 G4:1.5
F4:1 E4:.5 D4:.5 C4:2 R:.5''',
 lh='''R:2.25 C5:.25 Bb4:.25 G4:.25 Eb4:.25 D4:.25 Eb4:.25 G4:.25 Bb4:.25 C5:.25
Db5:.25 C5:.25 Ab4:.25 F4:.25 Eb4:.25 F4:.25 Ab4:.25 C5:.25 Db5:.25 R:2.25
R:2.25 D5:.25 C5:.25 Bb4:.25 G4:.25 F4:.25 G4:.25 Bb4:.25 C5:.25 D5:.25
Eb5:.25 Db5:.25 Bb4:.25 G4:.25 F4:.25 G4:.25 Bb4:.25 Db5:.25 Eb5:.25 R:2.25
R:2.25 G4:.25 F4:.25 Eb4:.25 C4:.25 Bb3:.25 C4:.25 Eb4:.25 G4:.25 Ab4:.25
Bb4:.25 Ab4:.25 F4:.25 Db4:.25 C4:.25 Db4:.25 F4:.25 Ab4:.25 Bb4:.25 R:2.25
R:2.25 G4:.25 F4:.25 D4:.25 Bb3:.25 A3:.25 Bb3:.25 D4:.25 F4:.25 G4:.25
A4:.25 G4:.25 E4:.25 C4:.25 B3:.25 C4:.25 E4:.25 G4:.25 A4:.25 R:2.25
R:2.25 F4:.25 Eb4:.25 C4:.25 Ab3:.25 G3:.25 Ab3:.25 C4:.25 Eb4:.25 F4:.25
F4:1 Ab3:.5 G3:.5 C4:2 Db4:.5
Eb4:1 Db4:.5 C4:.5 Bb3:1 G3:1.5
Ab3:1 C4:1 Bb3:.5 Ab3:.5 F3:1.5
G3:.5 Bb3:.5 D4:1 C4:1 Bb3:1.5
A3:1 C4:.5 B3:.5 E4:1 D4:1.5
C4:1 Bb3:1 G3:.5 F3:.5 Eb3:1.5
F3:1 Ab3:.5 G3:.5 C4:1 R:1.5
Ab3:.25 C4:.25 Eb4:.25 G4:.25 Ab4:.25 Bb4:.25 R:3
R:1.5 F5:.25 Eb5:.25 Db5:.25 C5:.25 Bb4:.25 Ab4:.25 F4:.25 Eb4:.25 Db4:.25 C4:.25 Ab3:.25 F3:.25
G3:.25 Bb3:.25 D4:.25 F4:.25 G4:.25 A4:.25 Bb4:.25 C5:.25 R:2.5
R:2.5 G4:.25 E4:.25 C4:.25 B3:.25 A3:.25 B3:.25 C4:.25 E4:.25
F4:.25 Ab4:.25 C5:.25 Eb5:.25 D5:.25 C5:.25 R:3
R:1.5 Bb4:.25 C5:.25 Db5:.25 Eb5:.25 Db5:.25 C5:.25 Bb4:.25 Ab4:.25 G4:.25 F4:.25 Eb4:.25 Db4:.25
C4:.25 Eb4:.25 G4:.25 Bb4:.25 C5:.25 D5:.25 Eb5:.25 F5:.25 G5:.25 R:2.25
R:2.25 Eb5:.25 D5:.25 C5:.25 Bb4:.25 A4:.25 G4:.25 F4:.25 Eb4:.25 C4:.25
D4:.25 F4:.25 Ab4:.25 C5:.25 D5:.25 Eb5:.25 R:3
R:1.5 D5:.25 B4:.25 A4:.25 G4:.25 F4:.25 D4:.25 C4:.25 B3:.25 A3:.25 B3:.25 D4:.25 F4:.25
C4:2 G3:1 E3:1.5
F3:1 G3:1 C3:1.5 R:1''',
 tempos=[63,64,65,64,63,64,65,64,62,61,62,60,63,64,62,60,64,65,66,67,65,64,66,67,65,64,62,62],
 phrases=[(1,4),(5,9),(10,16),(17,20),(21,26),(27,28)],lower_phrases=[(1,4),(5,9),(10,12),(13,16),(17,20),(21,26),(27,28)],
 sections={1:'p',5:'mp',9:'p',10:'pp',17:'p',21:'mp',25:'p',27:'pp'},lower_sections={1:'p',5:'mp',9:'p',10:'mp',13:'p',17:'p',21:'mp',25:'p',27:'pp'},
 pedal=sorted([[i*4.5+j+.05,i*4.5+j+1.3] for i in list(range(9))+list(range(16,26)) for j in [0,1.5,3]]+[[i*4.5+.05,i*4.5+(2.8 if i==15 else 4.3)] for i in range(9,16)]+[[117.05,121.3],[121.55,124.8]]),
 hairpins=[('crescendo',1,3),('diminuendo',7,8),('crescendo',17,19),('diminuendo',24,26)],clef_changes={'lh':{1:'treble',10:'bass',17:'treble',27:'bass'}})
p['performance']['lower_entries']=[[40.5,54],[58.5,70.5]]

p=study(op=363,title='Laurel Inlay',key='g',fifths=-2,meter='4/4',bpm=57,parent=222,
 source=dict(source_opus=222,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=4,source_pitches=['E','G','F#','B'],transposition_semitones=3),motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=4,pitches=['G','Bb','A','D']),
 description='A middle song first appears inside a three-voice texture, then continues alone when its companions fall silent. On returning, it sustains a longer sentence while the upper voice becomes lighter and more ornate. The ornament rises towards one high point while staying within the occupied hand’s reach. The opening spacing returns with changed bass harmony, and all three voices finally release together.',
 technical='Sustain and phrase the middle voice independently beneath the lighter upper figures. Keep the ornaments within the written whole-hand span while the inner notes remain held. The unaccompanied middle passage establishes the tone to retain later; the closing G remains tied across the last three bars until the coordinated release.',
 rh='''F5:2 R:1 F5:.5 G5:.5
Eb5:1 F5:.5 G5:.5 F5:1 Eb5:1
E5:1 F5:1 D5:1 C5:1
D5:1 Eb5:.5 F5:.5 F5:2
G5:1 F5:1 Eb5:1 D5:1
Eb5:1 D5:1 C5:1 A4:1
Bb4:3 R:1
R:4
R:4
R:4
R:4
R:4
D5:.25 F5:.25 Eb5:.25 D5:.25 Bb4:1 D5:.5 F5:.5 E5:.5 D5:.5
C5:.25 D5:.25 Eb5:.25 D5:.25 C5:1 A4:.5 C5:.5 D5:.5 A4:.5
Bb4:.25 C5:.25 Db5:.25 C5:.25 Bb4:1 D5:.5 Eb5:.5 F5:.5 D5:.5
C5:.25 D5:.25 Eb5:.25 D5:.25 F5:1 E5:.5 F5:.5 G5:.5 E5:.5
F5:.25 G5:.25 Ab5:.25 G5:.25 F5:1 Eb5:.5 D5:.5 C5:.5 Bb4:.5
Bb4:.25 C5:.25 D5:.25 C5:.25 E5:1 D5:.5 F5:.5 G5:.5 F5:.5
E5:.25 F5:.25 G5:.25 F5:.25 E5:1 G5:.5 A5:.5 Bb5:.5 G5:.5
A5:.25 Bb5:.25 C6:.25 Bb5:.25 A5:1 G5:.5 F5:.5 E5:.5 D5:.5
C5:.25 D5:.25 Eb5:.25 D5:.25 C5:1 Bb4:.5 C5:.5 Db5:.5 Bb4:.5
A4:.25 Bb4:.25 C5:.25 Bb4:.25 A4:1 C5:.5 D5:.5 Eb5:.5 C5:.5
D5:.25 Eb5:.25 F5:.25 Eb5:.25 D5:1 C5:.5 Bb4:.5 Bb4:1
C5:.5 Bb4:.5 D5:1 Bb4:1 R:1
F5:2 R:1 F5:.5 G5:.5
Eb5:1 F5:.5 G5:.5 F5:1 Eb5:1
E5:1 F5:1 D5:1 C5:1
D5:1 Eb5:.5 F5:.5 F5:2
G5:1 F5:1 Eb5:1 D5:1
Eb5:1 D5:1 C5:1 Bb4:1
A4:1 Bb4:1 D5:2
Bb4:3 R:1''',
 rh_inner='''G4:1 Bb4:1 A4:1 D5:1
C5:1 Bb4:.5 A4:.5 G4:2
A4:1 C5:1 Bb4:1 F4:1
G4:1 A4:.5 Bb4:.5 D5:2
Eb5:1 D5:1 C5:1 Bb4:1
A4:2 G4:1 F#4:1
G4:3 R:1
G4:1 A4:.5 Bb4:.5 D5:2
C5:1 Bb4:1 A4:2
F4:1 A4:1 C5:1 Bb4:1
A4:1 G4:1 F#4:1 A4:1
G4:3 R:1
G4:2 Bb4:2
A4:1 G4:1 D4:2
Eb4:2 G4:2
F4:1 A4:1 C5:2
Bb4:2 A4:1 G4:1
E4:1 G4:1 Bb4:2
A4:2 C5:2
D5:1 C5:1 Bb4:1 A4:1
G4:1 F4:1 Eb4:2
D4:1 F#4:1 A4:2
C5:1 Bb4:.5 A4:.5 G4:2
F#4:1 A4:1 G4:1 R:1
G4:1 Bb4:1 A4:1 D5:1
C5:1 Bb4:.5 A4:.5 G4:2
A4:1 C5:1 Bb4:1 F4:1
G4:1 A4:.5 Bb4:.5 D5:2
Eb5:1 D5:1 C5:1 Bb4:1
A4:1 G4:1 F#4:1 G4:1~
G4:4~
G4:3 R:1''',
 lh='''G3+D4:4
Eb3+Bb3:4
F3+C4:4
Bb2+F3:4
Eb3+Bb3:4
D3+A3:4
G3:3 R:1
R:4
R:4
R:4
R:4
R:4
G3+D4:4
D3+A3:4
Eb3+Bb3:4
F3+C4:4
Bb2+F3:4
C3+G3:4
F3+C4:4
Bb2+F3:4
Eb3+Bb3:4
D3+A3:4
Eb3+Bb3:4
D3:1 D3+A3:1 G3:1 R:1
Bb2+F3:4
Eb3+Bb3:4
F3+C4:4
G3+D4:4
C3+G3:4
D3+A3:4
Eb3+Bb3:2 D3+A3:2
G3+D4:3 R:1''',
 tempos=[57,58,59,58,60,58,56,57,58,59,58,56,58,59,60,61,60,59,61,63,61,60,59,57,57,58,59,58,60,58,57,57],
 phrases=[(1,7),(13,18),(19,24),(25,29),(30,32)],lower_phrases=[(1,7),(13,18),(19,24),(25,29),(30,32)],
 voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=3) for a,b in [(0,27),(28,47),(48,72),(72,95),(96,116),(116,127)]],
 sections={1:'p',8:'p',13:'pp',19:'mp',21:'p',25:'p',30:'pp'},lower_sections={1:'pp',13:'pp',19:'p',25:'pp',30:'pp'},
 pedal=sorted([[i*4+.05,i*4+(2.8 if i in [6,11,23,31] else 3.8)] for i in range(32) if i not in [14,15]]+[[56.05,57.8],[58.05,59.8],[60.05,61.8],[62.05,63.8]]),hairpins=[('crescendo',13,17),('diminuendo',21,24)],
 page_starts=[7,13,19,25,31],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=680))
p['performance']['inner_entries']=[[0,27],[28,47],[48,95],[96,127]]

p=study(op=364,title='Heather Murmur',key='b',fifths=2,meter='4/4',bpm=56,parent=264,
 source=dict(source_opus=264,source_hand='lh',source_start_beat=30,source_end_beat=32,source_pitches=['F','C','Ab','G'],transposition_semitones=6),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['B','F#','D','C#']),
 description='Two short questions are accompanied by quiet repeated keys and real gaps between their attacks. A longer singing answer replaces the repetitions with spacious bass motion. Two still harmonies redirect the return, whose repeated tones change beneath an expanding melody. The murmuring stops before the final sentence, leaving a few bass notes and then an unaccompanied close.',
 technical='Give each repeated key a clear release at a quiet level, using the written rests to reset the touch. Keep the upper phrase continuous across those lower interruptions. The central answer should have a different legato weight; after the repeated layer stops, let the final single line carry its own pulse.',
 rh='''B4:1 F#4:.5 D4:.5 C#4:2
D4:1 F#4:.5 A4:.5 G4:1 F#4:1
E4:1 D4:1 R:2
A4:1 E4:.5 C#4:.5 B3:2
C#4:1 E4:.5 G4:.5 F#4:1 E4:1
D4:1 C#4:1 R:2
B4:2 A4:1 F#4:1
G4:1 F#4:.5 E4:.5 D4:2
E4:1 G4:1 B4:2
A4:1 C#5:.5 B4:.5 A4:1 F#4:1
G4:1 A4:1 B4:1 D5:1
C#5:1 B4:1 A4:.5 G4:.5 F#4:1
E4:1 F#4:.5 G4:.5 A4:2
G4:1 F#4:1 E4:1 D4:1
C#4:1 E4:1 D4:1 R:1
F#4+A4:4
E4+G4:2 R:2
A4:1 E4:.5 C#4:.5 B3:2
D4:1 F#4:.5 A4:.5 G4:1 F#4:1
E4:1 G4:.5 B4:.5 A4:1 G4:1
F#4:1 A4:.5 C#5:.5 B4:1 A4:1
G4:1 F#4:1 E4:1 R:1
F#4:1 G4:.5 A4:.5 B4:2
A4:1 G4:1 F#4:.5 E4:.5 D4:1
E4:1 G4:1 F#4:2
D4:1 F#4:.5 A4:.5 G4:2
F#4:1 E4:1 D4:1 C#4:1
D4:1 C#4:1 B3:2''',
 lh='''F#3:.25 F#3:.25 F#3:.25 F#3:.25 R:.5 F#3:.25 F#3:.25 F#3:.25 F#3:.25 R:.5 F#3:.5 R:.5
G3:.5 R:.5 G3:.25 G3:.25 G3:.25 G3:.25 R:.5 G3:.5 R:1
D3+F#3:2 R:2
E3:.25 E3:.25 E3:.25 E3:.25 E3:.25 E3:.25 R:.5 E3:.25 E3:.25 E3:.25 E3:.25 R:1
F#3:.5 R:.5 F#3:.25 F#3:.25 F#3:.25 F#3:.25 R:.5 F#3:.5 R:1
B2+F#3:2 R:2
B2:1 F#3:1 A3:2
G2:1 D3:1 F#3:2
E3:2 B3:1 G3:1
F#3:2 C#4:1 A3:1
G3:2 D4:1 B3:1
A2:1 E3:1 G3:2
D3:2 A3:1 F#3:1
E3:2 B3:1 G3:1
F#3:1 A3:1 B3:1 R:1
D3:4
C3:2 R:2
E3:.25 E3:.25 E3:.25 E3:.25 R:.5 E3:.25 E3:.25 E3:.25 E3:.25 R:.5 E3:.5 R:.5
G3:.5 R:.5 G3:.25 G3:.25 G3:.25 G3:.25 R:.5 G3:.5 R:1
E3:.25 E3:.25 E3:.25 E3:.25 E3:.25 E3:.25 R:.5 E3:.25 E3:.25 E3:.25 E3:.25 R:1
F#3:.25 F#3:.25 F#3:.25 F#3:.25 R:1 F#3:.25 F#3:.25 F#3:.25 F#3:.25 R:1
G3:.25 G3:.25 G3:.25 G3:.25 R:1 B3:1 R:1
B2:2 F#3:2
G3:2 D3:1 R:1
R:4
R:4
R:4
R:4''',
 tempos=[56,57,55,56,57,55,57,58,59,60,59,58,57,56,55,56,55,56,57,58,57,55,56,57,56,57,56,56],
 phrases=[(1,3),(4,6),(7,11),(12,15),(18,22),(23,28)],lower_phrases=[(7,11),(12,15),(23,24)],
 sections={1:'p',4:'p',7:'mp',10:'mf',13:'mp',16:'p',18:'pp',23:'p',25:'pp'},lower_sections={1:'pp',7:'pp',10:'p',13:'pp',16:'pp',18:'pp',23:'pp'},
 pedal=[[i*4+.05,i*4+(2.8 if i==14 else 3.8)] for i in range(6,16)]+[[64.05,65.8],[88.05,91.8],[92.05,95.8]],hairpins=[('crescendo',7,9),('diminuendo',12,15),('diminuendo',25,28)])

p=study(op=365,title='Magnolia Equilibrium',key='e',fifths=1,meter='3/2',bpm=55,parent=257,
 source=dict(source_opus=257,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['D','F','E','A'],transposition_semitones=2),motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=6,pitches=['E','G','F#','B']),
 description='An inner song moves beneath held chord tones in a quiet minor chorale. A bare duet then separates the melody from its surrounding harmony. The second chorale begins more brightly, visits a lowered-seventh region and brings the original minor phrase into new bass harmony. Its final descent finds C major, where one inner note remains tied while the outer chord is renewed and then released.',
 technical='Keep the inner line legato beneath the held upper pairs, balancing three notes within the right hand’s checked reach. Clear each written pedal change without losing the finger-held melody. The bare duet should retain that tone; at the close, hold the inner C across the chord renewal and release all voices together.',
 rh='''B4+D5:4 D5+F#5:2
C5+E5:4 A4+C5:2
G4+B4:2 F#4+A4:1 G4+B4:1 A4+C5:2
B4+D5:3 A4+C5:1 G4+B4:2
A4+C5:2 C5+E5:2 A4+D5:2
A4+C5:2 G4+B4:3 R:1
R:6
R:6
R:6
R:6
R:6
D5+F#5:4 F#5+A5:2
E5+G5:4 C5+E5:2
B4+D5:2 A4+C5:1 B4+D5:1 C5+E5:2
D5+F5:2 C5+E5:2 A4+C5:2
B4+D5:4 D5+F#5:2
C5+E5:4 A4+C5:2
A4+C5:2 C5+E5:2 A4+D5:2
G4+B4:2 F4+A4:1 E4+G4:1 B4+D5:2
A4+C5:2 G4+B4:2 E4+G4:2
E4+G4:4 R:2''',
 rh_inner='''E4:2 G4:1 F#4:1 B4:2
A4:2 G4:1 F#4:1 E4:2~
E4:2 D#4:1 E4:1 F#4:2
G4:3 F#4:1 E4:2
F#4:2 A4:1 G4:1 F#4:2~
F#4:2 E4:3 R:1
E4:2 F#4:1 G4:1 B4:2
A4:1 G4:1 F#4:2 D4:2
E4:1 G4:1 F#4:1 A4:1 G4:2
F#4:1 E4:1 D#4:1 F#4:1 B4:2
A4:2 G4:1 F#4:1 E4:1 R:1
G4:2 B4:1 A4:1 D5:2
C5:2 B4:1 A4:1 G4:2
G4:2 F#4:1 G4:1 A4:2
Bb4:2 A4:1 G4:1 F4:2
E4:2 G4:1 F#4:1 B4:2
A4:2 G4:1 F#4:1 E4:2
F4:2 A4:1 G4:1 F4:2
E4:2 D4:1 C4:1 G4:2
F4:2 E4:1 D4:1 C4:2~
C4:4 R:2''',
 lh='''E3+B3:6
C3+G3:6
B2+F#3:2 B2+F#3:1 E3+B3:1 D3+A3:2
G2+D3:3 D3+A3:1 E3+B3:2
D3+A3:2 A2+E3:2 D3+A3:2
B2+F#3:2 E3+B3:3 R:1
C3:2 G3:1 B3:1 E3:2
D3:2 A3:1 F#3:1 B2:2
C3:1 E3:1 A3:2 B3:1 G3:1
B2:1 F#3:1 A3:1 G3:1 F#3:2
C3:1 D3:1 B2:1 D#3:1 E3:1 R:1
G3+D4:6
E3+B3:6
D3+A3:3 G3+D4:1 F3+C4:2
Bb2+F3:2 C3+G3:2 D3+A3:2
C3+G3:6
A2+E3:6
D3+A3:6
G2+D3:2 G2+D3:2 C3+G3:2
F2+C3:2 G2+D3:2 C3+G3:2
C3+G3:4 R:2''',
 tempos=[55,56,55,54,56,54,55,56,57,56,54,56,57,58,57,56,55,56,55,54,54],
 phrases=[(1,6),(12,15),(16,21)],lower_phrases=[(1,6),(7,11),(12,15),(16,21)],
 voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=3) for a,b in [(0,35),(36,65),(66,90),(90,124)]],
 sections={1:'p',7:'p',12:'mp',16:'p',21:'pp'},lower_sections={1:'pp',7:'p',12:'p',16:'pp',21:'pp'},
 pedal=sorted([[i*6+a+.05,i*6+b-.2] for i,spans in enumerate([
 [(0,4),(4,6)],[(0,4),(4,6)],[(0,2),(2,3),(3,4),(4,6)],[(0,3),(3,4),(4,6)],[(0,2),(2,4),(4,6)],[(0,2),(2,5)],
 [(0,6)],[(0,6)],[(0,6)],[(0,6)],[(0,5)],
 [(0,4),(4,6)],[(0,4),(4,6)],[(0,2),(2,3),(3,4),(4,6)],[(0,2),(2,4),(4,6)],[(0,4),(4,6)],[(0,4),(4,6)],[(0,2),(2,4),(4,6)],[(0,2),(2,3),(3,4),(4,6)],[(0,2),(2,4),(4,6)],[(0,4)]]) for a,b in spans]),
 hairpins=[('crescendo',12,14),('diminuendo',18,20)],page_starts=[7,13,19],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=680))
p['performance']['inner_entries']=[[0,35],[36,65],[66,124]]

p=study(op=366,title='Bramble Traverse',key='Eb',fifths=-3,meter='5/4',bpm=54,parent=227,
 source=dict(source_opus=227,source_hand='lh',source_start_beat=8,source_end_beat=12,source_pitches=['D','C','A','C'],transposition_semitones=-2),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['C','Bb','G','Bb']),
 description='Three separated calls answer themselves in distant piano registers, with written silence allowing each relocation. A closer, more legato middle passage brings their gestures into conversation. The last distant call is shorter and receives an answer in a new middle register. An exposed two-note sonority closes the piece after the travelling has stopped.',
 technical='Use the written rests to prepare each distant landing before sounding it softly. The large right-hand relocations into bars 2, 5, 8, 18 and 19 each have three quarter beats of preparation; retain that silence and avoid an arrival accent. Keep the compact middle connected, and let the final two-note sonority release together.',
 technique_limits=dict(chord_span=12,melodic_leap=24,rapid_leap=9),
 rh='''C5:1 Bb4:.5 G4:.5 Bb4:1 R:2
R:1 Eb6+G6:2 D6:1 R:1
C6:1 Bb5:1 G5:2 R:1
G5:1 F5:.5 D5:.5 F5:1 R:2
R:1 Bb3+D4:2 C4:1 R:1
D4:1 F4:1 G4:2 R:1
C5:1 Bb4:.5 G4:.5 Bb4:1 R:2
R:1 Db6+F6:2 C6:1 R:1
Bb5:1 Ab5:1 F5:2 R:1
G4:1 Ab4:.5 Bb4:.5 Eb5:2 D5:1
C5:2 Bb4:1 Ab4:2
G4:1 Bb4:1 D5:1 C5:2
Bb4:1 Ab4:.5 G4:.5 F4:1 Eb4:2
F4:1 Ab4:1 C5:2 Bb4:1
Ab4:1 G4:.5 F4:.5 Eb4:1 D4:2
Eb4:1 G4:1 F4:1 Eb4:1 R:1
C5:1 Bb4:.5 G4:.5 Bb4:1 R:2
R:1 D6+F6:1 Eb6:1 R:2
R:1 G4+Bb4:2 Ab4:1 R:1
G4:1 Bb4:1 C5:1 Eb5:2
D5:2 C5:1 Bb4:2
Ab4:1 G4:1 F4:2 R:1
R:1 Eb4:1 F4:1 G4:1 R:1
Bb4:3 R:2''',
 lh='''Eb2+Bb2:2 R:3
R:1 C3+G3:2 Bb2:1 R:1
F2+C3:2 Eb3:2 R:1
G2+D3:2 R:3
R:1 G2+D3:2 F2:1 R:1
Eb3:2 Bb2:2 R:1
C3+G3:2 R:3
R:1 Ab2+Eb3:2 G2:1 R:1
Db3:2 Ab2:2 R:1
Eb3:2 Bb3:1 G3:2
Ab2:1 Eb3:1 G3:1 C4:2
G3:2 D3:1 F3:2
F3:2 C3:1 Ab3:2
Db3:1 Ab3:1 F3:1 Ab2:2
Bb2:1 F3:1 Ab3:1 F3:2
Eb3:2 Bb2:1 Eb3:1 R:1
C3+G3:2 R:3
R:1 Bb2+F3:1 C3:1 R:2
R:1 Eb3+Bb3:2 Db3:1 R:1
C3:2 G3:1 Bb3:2
Bb2:2 F3:1 Ab3:2
Ab2:1 Eb3:1 Bb2:2 R:1
R:1 C3:1 D3:1 Eb3:1 R:1
G3:3 R:2''',
 tempos=[54,54,55,54,54,55,54,54,55,56,57,58,57,58,56,54,54,54,55,56,57,55,54,54],
 phrases=[(1,1),(2,3),(4,4),(5,6),(7,7),(8,9),(10,13),(14,16),(17,17),(18,19),(20,22),(23,24)],lower_phrases=[(2,3),(5,6),(8,9),(10,13),(14,16),(20,22),(23,24)],
 sections={1:'p',2:'pp',4:'p',5:'pp',7:'p',8:'pp',10:'mp',14:'p',17:'p',18:'pp',20:'p',23:'pp'},lower_sections={1:'pp',10:'p',14:'pp',20:'p',23:'pp'},
 pedal=sorted([[i*5+.05,i*5+2.8] for i in [0,3,6,16]]+[[i*5+1.05,i*5+3.8] for i in [1,4,7,18,22]]+[[i*5+.05,i*5+3.8] for i in [2,5,8,15,21]]+[[i*5+.05,i*5+4.8] for i in list(range(9,15))+[19,20]]+[[86.05,87.8],[115.05,117.8]]),hairpins=[('crescendo',10,12),('diminuendo',14,16),('diminuendo',20,22)])

p=study(op=367,title='Marigold Undersong',key='D',fifths=2,meter='6/4',bpm=66,parent=297,
 source=dict(source_opus=297,source_hand='rh',source_start_beat=48,source_end_beat=54,source_pitches=['Ab','F#','F','F#'],transposition_semitones=1),motif=dict(hand='lh',voice='bass',start_beat=0,end_beat=6,pitches=['A','G','F#','G']),
 description='The lower edge of a paired left-hand song carries the phrase while a quieter tenor adds colour. Brief upper replies interrupt it, followed by a longer upper solo. On returning, the low song continues through the interruptions and turns from its major setting towards a minor destination. The paired texture eventually becomes single bass notes; a delayed treble answer completes the release.',
 technical='Balance the lower note of each left-hand pair above its quieter tenor partner. The voices are notated separately to retain their phrase direction and recorded balance. Clear the low-register pedal at each written change. Let the lower melody continue through the upper interruptions, then preserve the silence before the final treble answer.',
 rh='''R:4 E4:1 F#4:1
A4:2 R:4
R:3 A4:1 B4:2
G4:2 R:2 D4:2
F#4:1 E4:1 D4:3 R:1
F#4:1 A4:.5 G4:.5 F#4:1 E4:1 D4:2
G4:2 F#4:1 E4:1 B4:2
A4:1 G4:1 F#4:.5 E4:.5 D4:1 C#4:2
D4:1 E4:.5 F#4:.5 G4:1 F#4:1 E4:1 R:1
R:4 E4:1 F#4:1
A4:1 R:2 G4:1 R:2
R:3 A4:1 Bb4:2
G4:2 R:1 F4:1 R:2
R:2 C5:1 Bb4:1 A4:1 R:1
R:2 A4:2 G4:2
D5:1 C5:.5 Bb4:.5 A4:1 G4:1 F4:2
Eb4:1 G4:1 F4:2 D4:2
C4:1 D4:1 Bb3:3 R:1
R:6
R:4 D4:2
R:6
R:6
R:1 G4:1 A4:.5 Bb4:.5 D5:2 C5:1
Bb4:1 A4:1 G4:3 R:1''',
 lh='''A2:2 G2:1 F#2:1 G2:2
B2:2 A2:1 F#2:1 E2:2
F#2:1 A2:1 B2:2 D3:2
C#3:2 B2:1 A2:1 G2:2
F#2:1 E2:1 D2:3 R:1
R:6
R:6
R:6
R:6
A2:2 G2:1 F#2:1 G2:2
B2:2 A2:1 F#2:1 E2:2
F#2:1 A2:1 B2:2 D3:2
C3:2 Bb2:1 A2:1 G2:2
F2:1 G2:1 A2:2 C3:2
D3:2 C3:1 Bb2:1 A2:2
G2:1 A2:1 Bb2:2 D3:2
C3:2 Bb2:1 A2:1 G2:2
F#2:1 A2:1 G2:3 R:1
G2:2 D3:1 F3:1 Bb2:2
C3:2 Bb2:1 A2:1 G2:2
F#2:1 A2:1 D3:2 C3:2
Bb2:1 A2:1 G2:3 R:1
R:6
R:6''',
 lh_upper='''C#3:2 B2:1 A2:1 B2:2
D3:2 C#3:1 A2:1 G2:2
A2:1 C#3:1 D3:2 F#3:2
E3:2 D3:1 C#3:1 B2:2
A2:1 G2:1 F#2:3 R:1
R:6
R:6
R:6
R:6
C3:2 B2:1 A2:1 B2:2
D3:2 C3:1 A2:1 G2:2
A2:1 C3:1 D3:2 F3:2
Eb3:2 D3:1 C3:1 Bb2:2
A2:1 Bb2:1 C3:2 Eb3:2
F3:2 Eb3:1 D3:1 C3:2
Bb2:1 C3:1 D3:2 F3:2
Eb3:2 D3:1 C3:1 Bb2:2
A2:1 C3:1 Bb2:3 R:1
R:6
R:6
R:6
R:6
R:6
R:6''',hidden_voice_rests={'tenor':[19,20,21,22]},
 tempos=[66,67,68,67,65,67,68,69,66,67,68,69,68,69,70,69,67,65,66,67,66,65,65,65],
 phrases=[(5,9),(16,18),(23,24)],lower_phrases=[(1,5),(10,13),(14,18),(19,22)],
 voice_phrases=[dict(voice='tenor',start_beat=a,end_beat=b,swell=-1) for a,b in [(0,29),(54,78),(78,107)]],
 sections={1:'pp',6:'p',10:'pp',16:'p',19:'pp',23:'pp'},lower_sections={1:'p',6:'pp',10:'mp',14:'p',19:'pp'},
 pedal=sorted([[i*6+a+.05,i*6+b-.2] for i,spans in enumerate([
 [(0,2),(2,3),(3,4),(4,6)],[(0,2),(2,3),(3,4),(4,6)],[(0,1),(1,2),(2,4),(4,6)],[(0,2),(2,3),(3,4),(4,6)],[(0,1),(1,2),(2,5)],
 [(0,2),(2,4),(4,6)],[(0,2),(2,4),(4,6)],[(0,2),(2,4),(4,6)],[(0,2),(2,4),(4,5)],
 [(0,2),(2,3),(3,4),(4,6)],[(0,2),(2,3),(3,4),(4,6)],[(0,1),(1,2),(2,4),(4,6)],[(0,2),(2,3),(3,4),(4,6)],[(0,1),(1,2),(2,4),(4,6)],[(0,2),(2,3),(3,4),(4,6)],[(0,1),(1,2),(2,4),(4,6)],[(0,2),(2,3),(3,4),(4,6)],[(0,1),(1,2),(2,5)],
 [(0,2),(2,3),(3,4),(4,6)],[(0,2),(2,3),(3,4),(4,6)],[(0,1),(1,2),(2,4),(4,6)],[(0,1),(1,2),(2,5)],[(1,3),(3,5),(5,6)],[(0,1),(1,2),(2,5)]]) for a,b in spans]),
 hairpins=[('crescendo',10,12),('diminuendo',16,18)],page_starts=[7,13,19],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=680))
p['performance']['lower_entries']=[[0,29],[54,131]]
p['performance']['phrase_arcs']=[[0,29,3],[30,53,3],[54,78,3],[78,107,3],[108,131,3],[133,143,2]]

p=study(op=368,title='Juniper Undulation',key='g',fifths=-2,meter='4/4',bpm=56,parent=233,
 source=dict(source_opus=233,source_hand='rh',source_voice='inner',source_start_beat=15,source_end_beat=17.5,source_pitches=['F#','A','Db','A'],transposition_semitones=1),motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['G','Bb','D','Bb']),
 description='Short, quiet rotations in the upper hand surround a slower lower song. The first wave grows across ten bars before the song stands in a stiller texture. Its second wave arrives in a warmer major colour, broadens briefly and stops sooner. The upper hand is left with an unaccompanied sigh after the rotations cease.',
 technical='Keep each written alternation light and close to the keys, without accenting its higher note. Let the left-hand song determine the phrase. Observe the held notes and rests within the fast texture, especially its abbreviated second ending; the final unaccompanied line keeps the same underlying pulse.',
 rh='''D5:.25 G5:.25 D5:.25 G5:.25 D5:.25 G5:.25 D5:.25 G5:.25 F5:1 R:1
C5:.25 F5:.25 C5:.25 F5:.25 C5:.25 F5:.25 C5:.25 F5:.25 Eb5:2
Bb4:.25 Eb5:.25 Bb4:.25 Eb5:.25 Bb4:.25 Eb5:.25 Bb4:.25 Eb5:.25 D5:1 C5:1
A4:.25 D5:.25 A4:.25 D5:.25 Bb4:.25 Eb5:.25 Bb4:.25 Eb5:.25 A4:.25 D5:.25 A4:.25 D5:.25 F#5:1
Bb4:.25 D5:.25 Bb4:.25 D5:.25 C5:.25 Eb5:.25 C5:.25 Eb5:.25 D5:.25 G5:.25 D5:.25 G5:.25 F5:1
Eb5:.25 A5:.25 Eb5:.25 A5:.25 D5:.25 G5:.25 D5:.25 G5:.25 C5:.25 F5:.25 C5:.25 F5:.25 Eb5:1
D5:.25 F5:.25 D5:.25 F5:.25 C5:.25 Eb5:.25 C5:.25 Eb5:.25 Bb4:.25 D5:.25 Bb4:.25 D5:.25 C5:1
A4:.25 C5:.25 A4:.25 C5:.25 Bb4:.25 D5:.25 Bb4:.25 D5:.25 A4:1 G4:1
F#4:.25 A4:.25 F#4:.25 A4:.25 G4:.25 Bb4:.25 G4:.25 Bb4:.25 A4:1 R:1
R:1 Bb4:1 A4:1 G4:1
D5:3 R:1
C5:2 Bb4:2
A4:1 Bb4:1 C5:2
A4:2 F#4:1 R:1
G4:1 Bb4:1 D5:2
C5:2 Bb4:1 A4:1
G4:3 R:1
Eb5:.25 G5:.25 Eb5:.25 G5:.25 Eb5:.25 G5:.25 Eb5:.25 G5:.25 F5:2
D5:.25 F5:.25 D5:.25 F5:.25 D5:.25 F5:.25 D5:.25 F5:.25 Eb5:1 D5:1
C5:.25 Eb5:.25 C5:.25 Eb5:.25 D5:.25 F5:.25 D5:.25 F5:.25 C5:2
Bb4:.25 Eb5:.25 Bb4:.25 Eb5:.25 C5:.25 F5:.25 C5:.25 F5:.25 D5:.25 G5:.25 D5:.25 G5:.25 Ab5:1
G5:.25 Bb5:.25 G5:.25 Bb5:.25 F5:.25 A5:.25 F5:.25 A5:.25 Eb5:.25 G5:.25 Eb5:.25 G5:.25 F5:1
D5:.25 F5:.25 D5:.25 F5:.25 C5:.25 Eb5:.25 C5:.25 Eb5:.25 Bb4:1 A4:1
G4:.25 Bb4:.25 G4:.25 Bb4:.25 F4:.25 A4:.25 F4:.25 A4:.25 G4:1 R:1
Eb4:.25 G4:.25 Eb4:.25 G4:.25 F4:.25 A4:.25 R:2.5
R:1 Bb4:1 A4:.5 G4:.5 F4:1
G4:1 Bb4:.5 C5:.5 D5:2
C5:1 Bb4:.5 A4:.5 G4:2
F4:1 G4:1 A4:1 R:1
Bb4:3 R:1''',
 lh='''G3:.5 Bb3:.5 D4:1 Bb3:2
A3:1 C4:1 Bb3:2
G3:1 F3:.5 G3:.5 A3:2
D3:1 F#3:1 A3:1 C4:1
Bb3:1 A3:.5 G3:.5 F3:2
C4:1 Bb3:1 A3:1 G3:1
Bb3:1 A3:.5 G3:.5 F3:1 Eb3:1
D3:2 E3:1 G3:1
F#3:1 E3:1 D3:1 R:1
G3:2 Bb3:1 D4:1
G3:.5 Bb3:.5 D4:1 Bb3:2
A3:1 C4:1 Bb3:2
G3:1 F3:.5 G3:.5 A3:2
D3:1 F#3:1 A3:1 C4:1
Bb3:2 G3:2
Eb3:2 F3:1 D3:1
G2:3 R:1
Eb3:1 G3:1 Bb3:2
F3:1 A3:1 C4:2
G3:2 Bb3:1 A3:1
Ab3:1 G3:.5 F3:.5 Eb3:2
C4:1 Bb3:1 A3:1 G3:1
F3:1 A3:.5 Bb3:.5 C4:2
Eb3:1 D3:1 C3:1 R:1
Bb2:1.5 R:2.5
R:4
R:4
R:4
R:4
R:4''',
 tempos=[56,57,58,57,58,59,58,57,56,55,56,57,56,55,56,55,55,57,58,59,60,59,57,56,55,55,56,55,55,55],
 phrases=[(1,4),(5,8),(9,10),(11,14),(15,17),(18,21),(22,25),(26,30)],lower_phrases=[(1,4),(5,10),(11,14),(15,17),(18,21),(22,23)],
 sections={1:'pp',5:'p',9:'pp',11:'pp',18:'pp',21:'p',24:'pp',26:'p'},lower_sections={1:'p',5:'mp',9:'p',11:'p',18:'p',21:'mp',24:'p'},
 pedal=sorted([[i*4+.05,i*4+3.8] for i in [0,1,2,4,5,6,9,10,11,12,14,15,17,18,19,20,21,22,26,27]]+[[i*4+.05,i*4+2.8] for i in [8,13,16,23,28,29]]+[[12.05,13.8],[14.05,15.8],[28.05,29.8],[30.05,31.8],[96.05,97.3],[101.05,103.8]]),
 hairpins=[('crescendo',5,6),('diminuendo',7,8),('crescendo',19,20),('diminuendo',22,23)])
p['performance']['lower_entries']=[[0,40],[40,67],[68,97.5]]

p=study(op=369,title='Wisteria Touchstone',key='b',fifths=2,meter='5/4',bpm=63,parent=303,
 source=dict(source_opus=303,source_hand='rh',source_start_beat=5,source_end_beat=10,source_pitches=['B','D','F#','E'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['B','D','F#','E']),
 description='A connected upper song moves past short, unequally spaced chord replies. A second panel transfers the opening melody to the lower hand and gives the upper hand the brief replies, opening a different harmonic route. The two kinds of touch remain independent without sustaining pedal. A last exchange thins to a single low note and written silence.',
 technical='Give the longer melody finger legato while releasing each short reply for its full written rest. The hands exchange these responsibilities at bar 14; avoid lengthening the answering chords to match the song. Keep the final clipped exchange in tempo and let the last single note finish precisely.',
 rh='''B4:.75 D5:.25 F#5:1 E5:2 R:1
A4:1 B4:1 D5:2 C#5:1
E5:2 D5:1 C#5:1 B4:1
A4:1 C#5:.5 D5:.5 E5:2 F#5:1
D5:2 C#5:1 B4:1 R:1
F#5:1 E5:.5 D5:.5 C#5:1 B4:2
A4:2 G4:1 F#4:2
E4:1 F#4:1 A4:2 G4:1
F#4:1 A4:.5 B4:.5 D5:1 C#5:2
E5:2 D5:1 B4:1 A4:1
G4:1 B4:1 D5:2 C5:1
B4:1 A4:1 G4:2 F#4:1
E4:3 R:2
R:1 G4+B4+E5:.5 R:1.5 F#4+A4+D5:.5 R:1.5
R:.5 G4+B4+D5:.5 R:2 F#4+A4+C#5:.5 R:1.5
R:2 G4+B4+E5:.5 R:1 F#4+A4+D5:.5 R:1
R:1 E4+G4+C5:.5 R:2 D4+F4+A4:.5 R:1
R:2.5 E4+G4+B4:.5 R:2
R:1 C4+E4+A4:.5 R:1.5 D4+F#4+A4:.5 R:1.5
R:.5 D4+F4+Bb4:.5 R:2 C4+Eb4+A4:.5 R:1.5
R:2 D4+F4+A4:.5 R:2.5
R:1 C4+E4+G4:.5 R:1.5 B3+D4+F4:.5 R:1.5
R:2 E4+G4+C5:.5 R:1 D4+F4+B4:.5 R:1
R:1 E4+G4+C5:.5 R:3.5
R:1 D4+F4+A4:.5 R:3.5
R:5
R:2 C4+E4:1 R:2
R:5''',
 lh='''E3:.5 R:1 G3+B3+D4:.5 R:1.5 D3:.5 R:1
G3:.5 R:2 B3+D4:.5 R:2
E3:.5 R:1.5 G3+B3:.5 R:1 F#3+A3:.5 R:1
D3:.5 R:1 F#3+A3:.5 R:2 E3:.5 R:.5
B2:.5 R:1.5 F#3+A3:.5 R:2.5
D3:.5 R:2 F#3+A3:.5 R:2
C3:.5 R:1.5 E3+G3:.5 R:1.5 D3:.5 R:.5
A2:.5 R:2 C3+E3:.5 R:2
B2:.5 R:1.5 D3+F#3:.5 R:1 E3+G3:.5 R:1
G2:.5 R:2 B2+D3:.5 R:2
C3:.5 R:1.5 E3+G3:.5 R:2.5
D3:.5 R:2 F#3+A3:.5 R:2
E3:.5 R:4.5
B2:.75 D3:.25 F#3:1 E3:2 R:1
A2:1 B2:1 D3:2 C#3:1
E3:2 D3:1 C#3:1 B2:1
A2:1 C3:.5 D3:.5 E3:2 F3:1
G3:2 F3:1 E3:1 R:1
F#3:1 E3:.5 D3:.5 C3:1 A2:2
Bb2:1 D3:1 F3:2 Eb3:1
D3:1 C3:1 Bb2:2 A2:1
G2:1 B2:1 D3:2 C3:1
E3:2 D3:1 B2:1 A2:1
G2:3 R:2
R:5
R:1.5 C3+G3:.5 R:3
R:5
G3:.5 R:4.5''',
 tempos=[63,64,65,64,62,64,65,64,66,65,64,63,62,63,64,65,64,63,64,65,64,63,63,62,62,62,62,62],
 phrases=[(1,5),(6,9),(10,13)],lower_phrases=[(14,18),(19,24)],
 sections={1:'p',6:'mp',10:'p',14:'pp',19:'p',25:'pp'},lower_sections={1:'pp',6:'p',10:'pp',14:'p',19:'mp',25:'pp'},
 pedal=[],hairpins=[('crescendo',6,8),('diminuendo',10,12)])
p['performance']['lower_entries']=[[65,88],[90,118]]
p['performance']['phrase_arcs']=[[0,24,3],[25,45,3],[45,63,3],[65,88,3],[90,118,3]]

p=study(op=370,title='Acacia Soliloquy',key='F',fifths=-1,meter='4/4',bpm=52,parent=301,
 source=dict(source_opus=301,source_hand='rh',source_start_beat=64,source_end_beat=65.5,source_pitches=['F','G','A','C'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['F','G','A','C']),
 description='A small harmonic frame releases a solitary treble sentence. Measured groups of five, seven and three notes, one brief faster turn and sustained tones shape its changing speech. A single low chord interrupts the sentence and turns it towards a flatter colour before it becomes plain song. The frame returns with a different bass and wider spacing; a short, quiet arrival completes the chapter.',
 technical='Keep the written cadenza proportions precise while allowing its longer notes to breathe within the shared pulse. Prepare each register change during the written silence. Let the single low interruption change the direction of the upper line without turning it into an accent. Retain the final tempo and balance the widely spaced closing sonority softly.',
 rh='''F4:1 G4:1 A4:1 C5:1
Bb4:1 A4:1 G4:1 E4:1
F4:1 A4:1 C5:1 Bb4:1
G4:1 A4:1 G4:1 R:1
F5:2/5 G5:2/5 A5:2/5 C6:2/5 Bb5:2/5 A5:2
G5:2/5 A5:2/5 Bb5:2/5 D6:2/5 C6:2/5 Bb5:1.5 A5:.5
E5:2/5 F5:2/5 G5:2/5 A5:2/5 G5:2/5 F5:2/5 E5:2/5 D5:2/5 C5:2/5 Bb4:2/5
F5:3/7 E5:3/7 D5:3/7 C5:3/7 Bb4:3/7 A4:3/7 G4:3/7 F4:1
Bb4:.125 C5:.125 D5:.125 F5:.125 G5:.125 F5:.125 E5:.125 D5:.125 C5:2 R:1
C5:.25 D5:.25 E5:.25 G5:.25 A5:.25 G5:.25 F5:.25 E5:.25 D5:.25 C5:.25 Bb4:.25 A4:.25 G4:.25 A4:.25 B4:.25 C5:.25
D5:1 Bb4:.5 A4:.5 G4:1 R:1
R:2 F4:1 Ab4:1
Bb4:.5 Ab4:.5 F4:1 Eb4:1 Db4:1
Eb4:1/3 F4:1/3 Ab4:1/3 Bb4:1 C5:2
Db5:1 C5:.5 Bb4:.5 Ab4:2
G4:1 Bb4:.5 A4:.5 G4:1 F4:1
E4:2 G4:1 C5:1
D5:1 C5:1 A4:2
G4:1 F4:1 E4:1 D4:1
E4:3 R:1
F4:1 G4:1 A4:1 C5:1
Bb4:1 A4:1 G4:1 F4:1
E4:1 G4:1 Bb4:1 A4:1
G4:2 E4:1 D4:1
E4:1 G4:1 C5:2
C5:3 R:1''',
 lh='''F2+C3:4
D3+A3:4
Bb2+F3:4
C3+G3:3 R:1
R:4
R:4
R:4
R:4
R:4
R:4
R:4
Db3+F3+Ab3:1 R:3
R:4
R:4
R:4
R:4
R:4
R:4
R:4
R:4
A2+E3:4
D3+A3:4
C3+G3:4
F2+C3:4
C3+G3:2 E3+B3:2
A2+E3:3 R:1''',
 tempos=[52,53,54,52,54,55,56,55,54,56,53,52,54,55,54,53,52,53,52,52,53,54,53,52,52,52],
 phrases=[(1,4),(5,8),(9,11),(12,16),(17,20),(21,26)],lower_phrases=[(1,4),(21,26)],
 sections={1:'p',5:'p',7:'mp',9:'p',12:'pp',14:'p',17:'p',21:'p',26:'pp'},lower_sections={1:'pp',12:'p',21:'pp'},
 tuplet_spans=[dict(hand='rh',start_beat=s,end_beat=s+2,actual=5,normal=4,stem='down',show_number='both') for s in [16,20,24,26]]+[dict(hand='rh',start_beat=28,end_beat=31,actual=7,normal=6,stem='down',show_number='both'),dict(hand='rh',start_beat=52,end_beat=53,actual=3,normal=2,stem='down')],
 pedal=sorted([[i*4+.05,i*4+3.8] for i in [0,1,2,20,21,22,23]]+[[12.05,14.8],[18.05,19.8],[22.05,23.3],[31.05,31.8],[33.05,34.8],[44.05,44.8],[46.05,47.8],[54.05,55.8],[58.05,59.8],[64.05,65.8],[70.05,71.8],[76.05,78.8],[96.05,97.8],[98.05,99.8],[100.05,102.8]]),
 hairpins=[('crescendo',5,6),('diminuendo',7,8),('diminuendo',18,20)])
