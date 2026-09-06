"""Individually specified studies in Craig's revised, freer musical direction.

Each row is a bar; durations use quarter-note units. A trailing ~ sustains a
pitch/chord into the next matching event without another sounded onset.
"""
DREAM_PIECES=[
dict(op=7,title='Silt Reverie',key='d',fifths=-1,meter='9/8',bpm=63,
 description='A slow nine-beat estuary: the D-F-E-A ancestor opens into asymmetrical three-, four- and five-bar breaths. Suspensions cross the bar line while spacious left-hand shells move through D minor, B-flat major, G minor and a brief D-flat-major reflection. An unhurried D-minor added-ninth close keeps the light warm.',
 parent_opus=2,motif=dict(hand='rh',start_beat=0,end_beat=4.5,pitches=['D','F','E','A']),
 rh='''
D5:1.5 F5:.5 E5:1 A4:1.5
C5:1.5 A4:1 G4:.5 E4:1.5
D5:2 F5:1 E5:1.5~
E5:1 D5:.5 A4:1.5 G4:1 R:.5
A4:1.5 C5:1 E5:1.5 D5:.5
G5:1 F5:.5 E5:1 D5:.5 Bb4:1 R:.5
A4:2 E5:.5 D5:2~
D5:1.5 C5:1 A4:1 R:1
Bb4:1.5 D5:.5 F5:1 A5:1.5
Ab5:1.5 F5:1 Eb5:.5 C5:1.5
E5:1 D5:.5 Bb4:1 A4:.5 G4:1 R:.5
A4+C5:3 E5:.5 D5:1
D5:1.5 F5:.5 E5:1 A4:1.5
C5:2 A4:1 E4:1 R:.5
D5:1.5 E5:.5 D5:1 Bb4:1.5
A4:1.5 G4:1 E4:.5 C#4:1 R:.5
F4:2 E4:.5 D4:1 A4:1~
A4:1.5 E4+A4:3
''',
 lh='''
D3:1.5 F3+A3:2 R:1
Bb2:1 F3+A3:2 D3:1 R:.5
G3:1.5 Bb3+D4:1.5 A3:1.5
C3:2 E3+Bb3:1.5 R:1
F3:1 A3+C4:2 G3:1.5
E3+Bb3:1.5 A2:1 G3+C#4:2
D3:2 F3+A3:1 C3:1.5
Bb2:1.5 F3+A3:2 R:1
G3:1 Bb3+D4:2 F3:1.5
Db3:1.5 F3+Ab3:2 R:1
C3:1.5 E3+Bb3:1.5 D4:1.5
F3:2 A3+C4:1.5 R:1
D3:1.5 F3+A3:2 R:1
Bb2:2 D3+A3:1.5 R:1
G3:1.5 Bb3+D4:1.5 E3:1.5
A2:1.5 G3+C#4:2 R:1
D3:2 A3:1 F3:1.5
D3+F3:3~ D3+F3:1.5
''',
 sections={1:'p',5:'p',9:'mp',12:'p',15:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,3),(4,7),(8,12),(13,16),(17,18)],lower_phrases=[(3,4),(9,11),(15,18)],
 hairpins=[('crescendo',5,6),('diminuendo',6,8),('crescendo',9,10),('diminuendo',10,12),('diminuendo',15,18)],
 tempo_changes={},group=3,
 performance=dict(rubato=[63,62,58,60,64,65,61,56,63,59,60,55,60,58,56,53,49,42],
  phrase_arcs=[[0,12.5,3],[13.5,33,4],[36,52,5],[54,70,3],[72,81,-2]],
  lower_entries=[[9,18],[36,49.5],[63,76.5]],pedal_bars=list(range(1,19)),pedal_lift=.18,gate=.99,
  note='Continuous half-quarter tempo changes interpolate the authored bar centres; a small anticipatory pedal lift clears each harmony. No random onset jitter.'))
]
