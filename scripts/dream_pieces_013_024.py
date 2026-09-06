"""Individually composed continuation, Op. 13–24. Each row is one bar."""
PIECES=[
dict(op=13,title='Alder Passage',key='e',fifths=1,meter='6/8',bpm=60,
 description='Cloud Causeway\'s opening falls a tone into E-G-A-G. A high, sustained line descends towards a quieter middle register, while the bass answers in short phrases. E minor gives way to C-major sevenths, a brief D-major window and a warm A-minor turn. The return is compressed and lower, as though the path has become familiar in the dark.',
 parent_opus=12,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['E','G','A','G']),
 ancestry=dict(source_opus=12,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['F#','A','B','A'],transposition_semitones=-2),
 rh='''
E5:1 G5:.5 A5:.5 G5:1~
G5:1 F#5:.5 E5:1 B4:.5
D5:1.5 E5:.5 F#5:1~
F#5:1 E5:1 R:1
R:.5 E5:1 G5:.5 D5:1
C5:1.5 B4:.5 G4:1~
G4:.5 A4:.5 C5:1 E5:1
F#5:1 E5:.5 C#5:.5 B4:1
A4:2 R:1
F#4:1 A4:.5 C#5:.5 E5:1~
E5:1 D5:.5 B4:.5 A4:1
G4:1.5 F#4:.5 E4:1
R:.5 G4:.5 B4:1 D5:1~
D5:1 C5:.5 B4:.5 A4:1
E4:1 G4:.5 A4:.5 G4:1~
G4:1 F#4:.5 E4:1 B4:.5
C5:1.5 B4:.5 A4:1
G4:1 B4:.5 D5:.5 F#5:1~
F#5:1 E5:.5 C5:.5 B4:1
A4:1 F#4:.5 D#4:.5 F#4:1
G4:1 F#4:.5 E4:1 B4:.5~
B4:1 F#4+B4:2
''',
 lh='''
E3:1.5 G3+D4:1.5
R:1 B3:1 G3:1
C3:2 E3+B3:1
A3:1 G3:.5 E3:.5 R:1
C3:1 G3+B3:1.5 R:.5
E3:1 D3:1 B2:1
A2:1 C3+G3:2
A3+C#4:1.5 G3:1.5
D3:1 F#3+C#4:1 R:1
D3:2 A3:1~
A3:.5 G3:.5 E3+B3:1.5 R:.5
E3:1.5 B3:1.5
G3:1 D4:1 B3:1
F#3:1 A3+C4:1.5 B2:.5
E3:1 G3+D4:1.5 R:.5
B3:.5 A3:.5 G3:1 E3:1
A2:1.5 E3+G3:1.5
G3:1 B3+D4:1 R:1
C4:1 B3:.5 A3:.5 E3:1
B2:1 A3+D#4:1.5 R:.5
E3:1.5 G3+B3:1 R:.5
E3+G3:3
''',sections={1:'p',5:'pp',10:'mp',13:'p',17:'pp'},words={1:'poco rubato',20:'poco rit.'},
 slurs=[(1,4),(5,9),(10,12),(13,16),(17,19),(20,22)],lower_phrases=[(2,4),(6,9),(10,12),(16,19)],
 hairpins=[('diminuendo',2,4),('crescendo',5,7),('diminuendo',7,9),('diminuendo',10,12),('crescendo',13,14),('diminuendo',17,22)],tempo_changes={},group=4,
 performance=dict(rubato=[60,59,56,53,59,60,62,58,51,61,58,53,59,61,57,55,58,60,56,52,47,41],
  phrase_arcs=[[0,11,3],[12,26,4],[27,35,3],[36,47,4],[48,56,2],[57,66,-2]],
  lower_entries=[[3,12],[15,27],[27,36],[45,57]],pedal_bars=list(range(1,23)),pedal_lift=.21,gate=.99,
  note='The opening stays suspended while the lower voice answers. The middle phrase moves forward briefly; the lower return and six-bar close gradually give up that momentum.')),
dict(op=14,title='Salt Promenade',key='c',fifths=-3,meter='9/8',bpm=66,
 description='A side path from Silt Reverie carries C-E-flat-D-G through a slow nine-beat metre. C-minor ninths open into E-flat and a soft D-flat-major reflection; F and B-flat dominants briefly brighten the middle. The melody crosses the bass at different phrase boundaries, then settles into a widely spaced C-minor added ninth.',
 parent_opus=7,motif=dict(hand='rh',start_beat=0,end_beat=4.5,pitches=['C','Eb','D','G']),
 ancestry=dict(source_opus=7,source_hand='rh',source_start_beat=0,source_end_beat=4.5,source_pitches=['D','F','E','A'],transposition_semitones=-2),
 rh='''
R:.5 C5:1 Eb5:.5 D5:1 G4:1.5
Bb4:2 G4:.5 F4:1 Eb4:1
F4:1 Ab4:.5 C5:1 Eb5:1 D5:1~
D5:1 C5:.5 Ab4:1 G4:1 R:1
G4:1.5 Bb4:.5 D5:1 F5:1.5
Eb5:1.5 Db5:.5 Ab4:1 F4:1.5
G4:1 B4:.5 D5:1 F5:1 Eb5:1~
Eb5:1 D5:.5 C5:1 Bb4:1 R:1
A4:1.5 C5:.5 Eb5:1 G5:1.5
F5:1 D5:.5 C5:1 Ab4:1 Bb4:1~
Bb4:1 G4:.5 F4:1 G4:1 D5:1
C5:1.5 Ab4:.5 G4:1 Eb4:1 R:.5
C5:1 Eb5:.5 D5:1 G4:2
Ab4:1 C5:.5 Eb5:1 D5:1 C5:1~
C5:1 B4:.5 A4:.5 G4:1 F4:.5 D4:1
Eb4:1 G4:1 D4+G4:2.5
''',
 lh='''
C3:1.5 G3+Bb3:1.5 Eb3:1.5
Ab2:1.5 Eb3+G3:2 R:1
F3:2 Ab3+C4:1.5 Eb3:1
Bb2:1 D3+Ab3:2 F3:1 R:.5
Eb3:2 Bb3+D4:1 C4:1.5
Db3:1.5 F3+Ab3:2 R:1
G3:1 F3+B3:1.5 D4:.5 Ab3:1.5
C3:1.5 Eb3+Bb3:2 R:1
F3:1 A3+Eb4:1.5 C4:1 R:1
Bb3:1 Ab3:1 F3:1 D3:1.5
Eb3:1.5 G3+Bb3:1.5 D3:.5 R:1
Ab2:2 Eb3+G3:1.5 C4:1
C3:1.5 Eb3+Bb3:1 G3:1 F3:1~
F3:1 Ab3+C4:2 Eb3:1 R:.5
G3:1 F3+B3:1.5 A3:.5 G3:1.5
C3:1 G3:1 C3+Eb3:2.5
''',sections={1:'p',5:'pp',7:'p',9:'mp',12:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,4),(5,6),(7,8),(9,12),(13,16)],lower_phrases=[(2,4),(6,8),(10,11),(13,16)],
 hairpins=[('crescendo',1,3),('diminuendo',3,4),('diminuendo',5,6),('diminuendo',7,8),('diminuendo',9,12),('diminuendo',14,16)],tempo_changes={},group=3,
 performance=dict(rubato=[66,65,67,60,64,58,66,59,68,65,63,57,62,59,54,45],
  phrase_arcs=[[0,17,4],[18,26,2],[27,35,3],[36,53,4],[54,72,-1]],
  lower_entries=[[4.5,18],[22.5,36],[40.5,49.5],[54,68]],pedal_bars=list(range(1,17)),pedal_lift=.25,gate=.99,
  note='The melody lingers over the new D-flat colour, then opens into the F-dominant phrase. The lower voice briefly leads the B-flat descent; the final bass settles before the upper added ninth.')),
dict(op=15,title='Pearl Footbridge',key='Bb',fifths=-2,meter='3/4',bpm=50,
 description='Salt Promenade\'s second-bar descent is lowered a fourth into F-D-C-B-flat. Here it belongs to a slow B-flat-major song: three-bar breaths give way to a longer five-bar crossing. A G-dominant turn leads through C minor, and borrowed E-flat minor lends a brief blue shade before the final major-ninth warmth.',
 parent_opus=14,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['F','D','C','Bb']),
 ancestry=dict(source_opus=14,source_hand='rh',source_start_beat=4.5,source_end_beat=9,source_pitches=['Bb','G','F','Eb'],transposition_semitones=-5),
 rh='''
F5:1 D5:.5 C5:.5 Bb4:1~
Bb4:1 A4:.5 F4:.5 G4:1
A4:1.5 C5:.5 D5:1
Eb5:1 D5:.5 Bb4:1 C5:.5~
C5:1 Bb4:.5 A4:.5 F4:1
G4:1 Bb4:.5 D5:.5 F5:1~
F5:1 Eb5:1 R:1
D5:1.5 F5:.5 A5:1
G5:1 F5:.5 D5:.5 B4:1
C5:1 Eb5:.5 G5:.5 F5:1~
F5:1 Eb5:.5 D5:.5 C5:1
D5:1.5 Bb4:.5 A4:1
G4:1 Bb4:.5 F5:.5 Eb5:1
Gb5:1 Eb5:.5 Db5:.5 Bb4:1~
Bb4:1 A4:.5 F4:.5 R:1
F5:1 D5:.5 C5:.5 Bb4:1
A4:1.5 G4:.5 Eb4:1
F4:1 G4:.5 A4:.5 C5:1~
C5:1 C5+F5:2
''',
 lh='''
Bb2:1.5 D3+A3:1.5
G3:1 F3:1 D3:1
F3:1 A3+C4:1.5 R:.5
Eb3:2 G3+Bb3:1
F3:1 Eb3+A3:1 R:1
G3:1.5 Bb3+D4:1 R:.5
Eb3:1 G3:.5 Bb3:.5 C4:1
D3:2 F3+C4:1
G3:1 F3+B3:1.5 D3:.5
C3:1.5 Eb3+Bb3:1.5
F3:1 A3+Eb4:1 C3:1
Bb2:1 D3+A3:1.5 R:.5
Eb3:1.5 Bb3+D4:1.5
Gb3:1 Bb3+Db4:1 Eb3:1
F3:1.5 A3+C4:1 R:.5
Bb2:1 D3+A3:1 G3:1~
G3:.5 F3:.5 Eb3+Bb3:1.5 R:.5
F3:1 Eb3+A3:1.5 F3:.5
Bb2:1 D3+A3:2
''',sections={1:'p',4:'pp',8:'mp',12:'p',16:'pp'},words={1:'poco rubato',18:'poco rit.'},
 slurs=[(1,3),(4,7),(8,12),(13,15),(16,19)],lower_phrases=[(2,4),(6,7),(9,11),(14,18)],
 hairpins=[('diminuendo',1,3),('crescendo',4,6),('diminuendo',6,7),('diminuendo',8,12),('crescendo',13,14),('diminuendo',14,15),('diminuendo',16,19)],tempo_changes={},group=4,
 performance=dict(rubato=[50,49,46,49,50,52,46,53,55,51,49,44,49,46,43,47,45,41,36],
  phrase_arcs=[[0,8,3],[9,20,3],[21,35,5],[36,44,2],[45,57,-1]],
  lower_entries=[[3,12],[15,21],[24,33],[39,54]],pedal_bars=list(range(1,20)),pedal_lift=.2,gate=.99,
  note='The five-bar middle crosses the phrase boundary with a sustained F. E-flat minor is held back slightly; the return settles into a slower, softer B-flat-major ninth.'))
]
