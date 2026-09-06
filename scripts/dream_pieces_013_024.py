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
  note='The opening stays suspended while the lower voice answers. The middle phrase moves forward briefly; the lower return and six-bar close gradually give up that momentum.'))
]
