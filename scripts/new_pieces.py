"""Individually composed continuations of the CWS First Studies catalogue."""
NEW_PIECES=[
 dict(op=4,title='Tidal Orchard',key='d',fifths=-1,meter='6/8',bpm=72,
 description='A slower, minor-coloured descendant of Velvet Estuary. The four-note thought begins above the water, passes into the lower voice at bar 9, and returns with a changed continuation. F-major and B-flat-major light soften the D-minor close.',
 parent_opus=2,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['D','F','E','A']),
 rh='''
D5:.5 F5:.5 E5:.5 A4:1.5
C5:1 D5:.5 F5:1 E5:.5
D5:1.5 C5:1 A4:.5
G4:1 A4:.5 E4:1.5
F4:.5 A4:.5 C5:.5 D5:1 C5:.5
Bb4:1 A4:.5 F4:1.5
G4:1.5 A4:.5 G4:.5 E4:.5
A4:2.5 R:.5
A4:1.5 C5:1.5
D5:1 C5:.5 A4:1.5
Bb4:.5 D5:.5 F5:.5 E5:1 D5:.5
C5:1.5 A4:1 G4:.5
A4:.5 C5:.5 E5:.5 D5:1 C5:.5
Bb4:1 A4:.5 G4:1.5
G4:.5 A4:.5 Bb4:.5 A4:1 G4:.5
E4:1.5 A4:1 R:.5
D5:.5 F5:.5 E5:.5 A4:1.5
C5:1.5 D5:.5 C5:.5 A4:.5
Bb4:1 D5:.5 F5:1 E5:.5
D5:1.5 C5:1 A4:.5
G4:1 Bb4:.5 A4:1 G4:.5
F4:1.5 E4:.5 F4:.5 G4:.5
E4:1.5 C#4:1 E4:.5
D4:3
''',
 lh='''
D3:1.5 A3:.5 F3:.5 E3:.5
Bb2:.5 F3:.5 A3:.5 G3:1.5
F3:1 A3:.5 G3:1 E3:.5
C3:1.5 G3:1 E3:.5
D3:.5 F3:.5 E3:.5 A2:1.5
Bb2:1.5 D3:.5 F3:.5 G3:.5
C3:1.5 E3:1 E3:.5
A2:1.5 E3:1 C#3:.5
D3:.5 F3:.5 E3:.5 A2:1.5
F3:1.5 A3:1 F3:.5
G3:1.5 Bb3:.5 A3:.5 F3:.5
A3:1 G3:.5 F3:1 E3:.5
F3:1.5 A3:1 C4:.5
G3:1.5 D3:1 F3:.5
Bb2:.5 D3:.5 F3:.5 G3:1.5
A2:1.5 E3:.5 G3:.5 C#3:.5
D3:1.5 A3:1 F3:.5
Bb2:1.5 F3:1 A3:.5
G3:.5 A3:.5 Bb3:.5 A3:1.5
F3:1.5 C3:1 C3:.5
G2:1.5 D3:1 F3:.5
Bb2:1.5 D3:.5 F3:.5 E3:.5
A2:1.5 E3:1 G3:.5
D3+F3:3
''',sections={1:'p',9:'mp',17:'p',21:'pp'},words={23:'poco rit.'},
 slurs=[(i,i+1) for i in range(1,25,2)],lower_phrases=[(5,6),(9,10),(13,14)],
 hairpins=[('crescendo',5,7),('diminuendo',7,8),('crescendo',9,11),('diminuendo',13,16),('diminuendo',21,24)],tempo_changes={23:67,24:60},group=4),
 dict(op=5,title='Glass Footpath',key='g',fifths=-2,meter='3/4',bpm=69,
 description='The ancestor moves to G-B-flat-A-D and a three-beat walking rhythm. Small rests open the phrases; an answering bass line changes the direction of the melody. The middle passage briefly looks towards B-flat major before the two voices settle into G minor.',
 parent_opus=2,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['G','Bb','A','D']),
 rh='''
G4:1 Bb4:.5 A4:.5 D5:1
C5:1 Bb4:1 A4:.5 G4:.5
F4:1 A4:.5 C5:.5 D5:1
Bb4:2 R:1
G4:1 A4:.5 Bb4:.5 D5:1
Eb5:1 D5:1 Bb4:1
A4:1 G4:.5 F#4:.5 A4:1
G4:2 R:1
D5:1 F5:.5 Eb5:.5 D5:1
C5:1 Bb4:1 G4:1
A4:.5 C5:.5 D5:1 F5:1
Eb5:1 D5:1 C5:1
D5:1 Bb4:.5 A4:.5 G4:1
Bb4:1 C5:1 D5:1
C5:1 A4:.5 G4:.5 F#4:1
G4:2 R:1
G4:1 Bb4:.5 A4:.5 D5:1
C5:1 A4:1 G4:1
Bb4:1 D5:1 C5:.5 Bb4:.5
A4:2 R:1
G4:1 F4:.5 Eb4:.5 G4:1
A4:1 G4:.5 F#4:.5 D4:1
Eb4:1 F#4:1 A4:1
G4:3
''',
 lh='''
G2:1 D3:1 Bb3:1
Eb3:1 G3:.5 F3:.5 Eb3:1
F3:1 C3:1 A3:1
Bb2:1 F3:1 D3:1
Eb3:1 G3:1 Bb3:1
C3:1 G3:.5 A3:.5 Bb3:1
D3:1 A3:1 C4:1
G3:1 D3:1 R:1
Bb2:1 F3:1 A3:1
Eb3:1 G3:1 Bb3:1
F3:1 A3:1 C4:1
C3:1 G3:.5 A3:.5 Eb3:1
G3:1 Bb3:.5 A3:.5 D3:1
Eb3:1 G3:.5 F3:.5 Eb3:1
D3:1 A3:1 C4:1
G3:1 D3:1 Bb2:1
G2:1 D3:1 Bb3:1
Eb3:1 G3:.5 F3:.5 Eb3:1
C3:1 G3:1 Eb3:1
D3:1 A3:1 C4:1
Eb3:1 Bb2:1 Eb3:1
D3:1 A2:1 C3:1
C3:1 D3:1 F#3:1
G2+Bb2:3
''',sections={1:'p',9:'mp',17:'p',21:'pp'},words={23:'poco rit.'},
 slurs=[(i,i+1) for i in range(1,25,2)],lower_phrases=[(5,6),(13,14),(21,22)],
 hairpins=[('crescendo',5,6),('diminuendo',7,8),('crescendo',9,11),('diminuendo',13,16),('diminuendo',21,24)],tempo_changes={23:64,24:57},group=4),
 dict(op=6,title='Willow Transit',key='C',fifths=0,meter='6/8',bpm=81,
 description='A-C-B-E, the shared figure moved into a new register and tonal setting, begins in the left hand. A floating upper voice gradually takes it over. The middle leans towards A minor, then opens into C major with a softened plagal return.',
 parent_opus=2,motif=dict(hand='lh',start_beat=0,end_beat=3,pitches=['A','C','B','E']),
 rh='''
E5:1.5 G5:1 E5:.5
D5:1 F5:.5 E5:1 C5:.5
B4:1 D5:.5 G5:1 F5:.5
E5:2.5 R:.5
A4:.5 C5:.5 B4:.5 E5:1.5
F5:1 E5:.5 C5:1 A4:.5
B4:.5 D5:.5 E5:.5 D5:1 B4:.5
C5:2.5 R:.5
C5:1.5 E5:1.5
F5:1 E5:.5 D5:1 B4:.5
C5:.5 E5:.5 G5:.5 F5:1 E5:.5
D5:1.5 B4:1 G#4:.5
A4:1 C5:.5 E5:1 D5:.5
C5:1.5 A4:1 G4:.5
B4:.5 C5:.5 D5:.5 B4:1 G4:.5
A4:2.5 R:.5
E5:1.5 G5:1 E5:.5
D5:1 F5:.5 E5:1 C5:.5
D5:.5 E5:.5 F5:.5 D5:1 B4:.5
C5:1.5 E5:1.5
F5:1 E5:.5 C5:1 A4:.5
G4:1.5 B4:1 D5:.5
C5:1.5 D5:1 B4:.5
C5:3
''',
 lh='''
A2:.5 C3:.5 B2:.5 E3:1.5
F3:1.5 A3:1 D3:.5
G2:1.5 D3:.5 E3:.5 F3:.5
C3:1.5 G3:1 E3:.5
A2:1.5 E3:1 G3:.5
F3:1.5 C3:.5 E3:.5 F3:.5
G3:1.5 F3:1 D3:.5
C3:1.5 E3:1 E3:.5
A2:.5 C3:.5 B2:.5 E3:1.5
D3:1.5 A3:1 F3:.5
A2:1.5 E3:.5 G3:.5 C4:.5
E3:1.5 B2:1 D3:.5
A2:1.5 E3:1 G3:.5
F3:.5 A3:.5 G3:.5 E3:1.5
G3:1.5 D3:1 F3:.5
A2:1.5 E3:1 C3:.5
C3:.5 E3:.5 D3:.5 G3:1.5
F3:1.5 A3:1 D3:.5
G2:1.5 D3:1 F3:.5
C3:1.5 G3:.5 A3:.5 B3:.5
F3:1.5 A3:1 D3:.5
G2:1.5 D3:.5 F3:.5 G3:.5
F3:1.5 G3:1 F3:.5
C3+E3:3
''',sections={1:'p',9:'mp',17:'p',21:'pp'},words={23:'poco rit.'},
 slurs=[(i,i+1) for i in range(1,25,2)],lower_phrases=[(1,2),(9,10),(17,18)],
 hairpins=[('crescendo',5,7),('diminuendo',7,8),('crescendo',9,11),('diminuendo',13,16),('diminuendo',21,24)],tempo_changes={23:75,24:66},group=4)
]
