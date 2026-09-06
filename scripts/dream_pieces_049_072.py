"""Individually composed studies for Volume 03, Op. 49–72."""
PIECES=[
dict(op=49,title='Dew Pavilion',key='D',fifths=2,meter='4/4',bpm=56,
 description='Thistle Horizon’s inner line becomes A–D–E–C-sharp in a new left-hand tenor voice. Two independent lines now share each hand. The tenor opening moves beneath a sustained upper D; B-flat and D-flat reflections later lead through C and G before a quiet D-major sixth/ninth close. Half-bar pedal changes let the moving voices clear while held notes continue.',
 difficulty='Advanced four-voice counterpoint',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Each hand carries two independently notated voices. The opening tenor phrase needs to sing above the bass while the right hand sustains its melody. Bass changes keep the moving tenor within an octave of the held lower note. Printed half-bar pedal changes require finger sustain across the refreshes; the left-hand span reaches an octave.',
 parent_opus=48,motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=4,pitches=['A','D','E','C#']),
 ancestry=dict(source_opus=48,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=5,source_pitches=['B','E','F#','D#'],transposition_semitones=10),
 pedal_spans=[[i*2,i*2+1.78] for i in range(32)],
 rh='''
D5:4
C#5:2 B4:2
E5:3 D5:1
C#5:4
D5:2 F5:2
Eb5:3 Db5:1
E5:4
F#5:2 E5:2
G5:3 F#5:1
E5:2 D5:2
C5:3 Bb4:1
B4:4
D5:3 C#5:1
B4:2 A4:2
G4:3 E4:1
F#4:4
''',
 rh_inner='''
F#4:1 A4:1 B4:1 A4:1
E4:1 G4:.5 A4:.5 G4:2
G4:1 B4:1 C#5:2
F#4:1 A4:1 B4:1 G4:1
F4:2 A4:.5 C5:.5 Bb4:1
F4:1 Ab4:1 Bb4:.5 Ab4:1.5
G4:1 B4:1 D5:1 C5:1
A4:1 C5:1 D5:2
B4:1 D5:1 E5:.5 D5:1.5
G4:1 B4:.5 C5:.5 A4:2
E4:1 G4:1 A4:1 G4:1
D4:1 F#4:1 A4:.5 G4:1.5
F#4:1 A4:.5 B4:.5 E4:2
D4:1 G4:1.5 F#4:1.5
C#4:1 E4:1 F#4:.5 D4:1.5
D4:2 E4:2
''',
 lh='''
D3:2 F#3:2
A2:2 C#3:2
G2:2 B2:2
A2:2 C#3:2
Bb2:2 D3:2
Db3:2 F3:2
C3:1.5 E3:.5 G3:2
D3:2 F#3:2
G2:2 B2:2
E3:3 B2:1
F2:2 A2:2
G2:2 B2:2
B2:2 D3:2
E3:2 G3:2
A2:2 C#3:2
D3:4
''',
 lh_upper='''
A3:1 D4:1 E4:1 C#4:1
E3:1 G3:1 B3:1 A3:1
D3:1 F#3:1 A3:1 G3:1
E3:1 G3:.5 F#3:.5 G3:2
F3:1 A3:1 C4:.5 Bb3:1.5
Ab3:1 C4:1 Eb4:.5 Db4:1.5
G3:1 B3:.5 A3:.5 D4:2
A3:1 C4:.5 B3:.5 E4:2
D3:1.5 F#3:.5 A3:.5 G3:1.5
B3:1 D4:.5 C4:.5 F#3:2
C3:1 E3:.5 D3:.5 G3:1 F3:1
D3:1 F#3:1 A3:.5 G3:1.5
F#3:1 A3:1 C#4:.5 B3:1.5
B3:1 D4:1 F#4:.5 E4:1.5
E3:1 G3:1 Bb3:.5 A3:1.5
A3:2 B3:2
''',sections={1:'p',3:'mp',4:'pp',5:'p',6:'mp',7:'pp',8:'p',9:'mp',10:'p',12:'pp',13:'p',15:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,4),(5,7),(8,12),(13,16)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,16)],
 hairpins=[('crescendo',1,3),('diminuendo',3,4),('crescendo',5,6),('diminuendo',6,7),('crescendo',8,9),('diminuendo',9,12),('diminuendo',13,16)],tempo_changes={},group=4,
 performance=dict(rubato=[56,53,59,48,54,58,49,55,60,54,51,46,52,47,41,33],
  phrase_arcs=[[0,15,3],[16,27,4],[28,47,4],[48,64,-2]],
  lower_entries=[[16,20],[40,44],[56,64]],tenor_entries=[[0,4],[28,32],[52,56]],pedal_lift=.22,gate=.995,
  note='The tenor is slightly more present at its opening and later answers, while the bass stays lighter. Held keys preserve the longer lines through each pedal refresh. The final four-bar phrase withdraws into a close, quiet sixth/ninth sonority.'))
,
dict(op=50,title='Mica Understory',key='F',fifths=-1,meter='6/4',bpm=57,
 engraving=dict(spacing_system=13,pedal_offset_y=420),
 description='Dew Pavilion’s tenor phrase moves into the treble as C–F–G–E. A sustained bass and a separately moving tenor share the left hand beneath it. Two quintuplet gestures open and fold back, first in bright F-major colour and later over D-flat. E-flat and E-major reflections lead through a borrowed F-minor passage to a quiet, richly added F-major close.',
 difficulty='Advanced lower-voice independence',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The left hand sustains the bass while shaping a distinct tenor line with upward stems. Half-bar pedal changes must preserve the held keys. The right hand alternates sustained voicings with two groups of five quarter-note quintuplets across four beats. Balance the moving tenor beneath the melody without losing the bass.',
 tuplet_groups=[dict(hand='rh',actual=5,normal=4,count=10)],
 parent_opus=49,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=6,pitches=['C','F','G','E']),
 ancestry=dict(source_opus=49,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=4,source_pitches=['A','D','E','C#'],transposition_semitones=3),
 pedal_spans=[[i*3,i*3+2.77] for i in range(32)],
 rh='''
C5:1 F5:1 G5:1 E5:3
D5:2 C5:.5 A4:.5 G4:1 A4:2
Bb4+D5+A5:3 G5:1 F5:1 E5:1
C5+E5+Bb5:2 A5:1 G5:.5 F5:.5 E5:2
F5:4/5 A5:4/5 C6:4/5 B5:4/5 G5:4/5 A5:2
G5:2 F5:.5 E5:.5 D5:1 C5:2
Eb5+G5+D6:3 C6:1 Bb5:1 G5:1
F#5:2 E5:1 D#5:1 B4:2
E5+G#5+D#6:3 C#6:1 B5:.5 G#5:.5 F#5:1
F5:4/5 Eb5:4/5 Db5:4/5 C5:4/5 Ab4:4/5 Bb4:2
A4+C5+G5:3 F5:1 E5:1 D5:1
G4+B4+F5:2 E5:1 D5:.5 C5:.5 B4:2
E4+G4+D5:3 E5:1 G5:2
F5:1 Eb5:.5 C5:.5 Bb4:1 Ab4:3
G4+Bb4+E5:3 D5:1 C5:1 Bb4:1
A4:2 G4:1 E4+G4+A4:3
''',
 lh='''
F3:6
D3:3 F3:3
Bb2:2 D3:4
C3:2 E3:4
F3:6
A2:2 C3:4
Eb3:2 G3:4
B2:2 D#3:4
E3:6
Db3:2 F3:4
D3:6
G2:2 B2:4
C3:2 E3:4
F3:2 Ab3:4
C3:2 E3:4
F3:6
''',
 lh_upper='''
A3:1 C4:1 D4:1 C4:3
A3:1 C4:2 B3:.5 A3:2.5
F3:1.5 A3:.5 C4:1 Bb3:3
G3:1 Bb3:1 D4:1 C4:3
A3:2 C4:.5 D4:.5 E4:1 D4:2
E3:1 G3:.5 F3:.5 A3:2 G3:2
Bb3:1 D4:.5 C4:.5 F4:1 Eb4:3
F#3:1 A#3:1 C#4:1 B3:3
G#3:1 B3:1 C#4:2 D#4:2
Ab3:1 C4:1 Eb4:1 Db4:3
F3:1 A3:.5 C4:.5 B3:1 A3:3
D3:1 F3:1 A3:1 G3:3
G3:1 B3:.5 A3:.5 D4:1 C4:3
C4:1 Eb4:.5 D4:.5 G4:1 F4:3
G3:1 Bb3:1 D4:1 C4:3
A3:2 C4:1 D4:3
''',sections={1:'p',3:'mp',5:'p',6:'pp',7:'mp',8:'p',9:'mp',10:'pp',11:'p',13:'mp',14:'p',15:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,4),(5,8),(9,13),(14,16)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,16)],
 hairpins=[('crescendo',1,3),('diminuendo',3,4),('diminuendo',5,6),('crescendo',6,7),('diminuendo',7,8),('diminuendo',9,10),('crescendo',11,13),('diminuendo',14,16)],tempo_changes={},group=4,
 performance=dict(rubato=[57,54,59,51,60,48,58,51,59,49,54,57,60,49,43,33],
  phrase_arcs=[[0,23,3],[24,47,4],[48,77,4],[78,96,-2]],
  lower_entries=[[0,6],[30,36],[60,66],[90,96]],tenor_entries=[[6,12],[36,42],[60,66],[78,84]],pedal_lift=.23,gate=.995,
  note='The bass remains quietly held while the tenor takes small breaths. The two quintuplet figures form broad gestures above that slower movement. Each pedal refresh clears the passing harmony without cutting the sustained voice, and the closing minor colour softens into the last major sonority.'))
,
dict(op=51,title='Pewter Lagoon',key='c',fifths=-3,meter='5/4',bpm=56,
 description='A tenor fragment from Mica Understory becomes C–E-flat–F–G in the upper melody. Four independent voices gather around it. Twice the left-hand tenor moves in five-note groups while the bass remains held, opening first into C-major light and later into A-flat. The return passes through a soft altered dominant and settles into C minor with an added sixth.',
 difficulty='Advanced four-voice quintuplet study',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 4 and 10, the LH tenor plays five quarter-note quintuplets across four beats while the bass stays held. The bass changes on the fifth beat to support the tenor’s arrival. Both RH voices continue independently. Keep the tenor even without accenting each note; finger sustain preserves the bass through pedal changes.',
 tuplet_groups=[dict(hand='lh',actual=5,normal=4,count=10)],
 parent_opus=50,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=5,pitches=['C','Eb','F','G']),
 ancestry=dict(source_opus=50,source_hand='lh',source_voice='tenor',source_start_beat=24,source_end_beat=28,source_pitches=['A','C','D','E'],transposition_semitones=3),
 page_starts=[10],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[span for i in range(15) for span in [[i*5,i*5+1.78],[i*5+2,i*5+4.78]]],
 rh='''
C5:1 Eb5:.5 F5:.5 G5:3
F5:3 Eb5:2
D5:2 C5:3
E5:5
D5:3 C5:2
F5:3 E5:2
G5:2 F5:3
E5:3 D5:2
Db5:5
C5:5
Bb4:2 C5:3
D5:3 C5:2
B4:3 A4:2
Ab4:3 G4:2
G4:5
''',
 rh_inner='''
G4:1 Bb4:.5 C5:.5 Eb5:3
Ab4:1 C5:1 Db5:1 C5:2
F4:1 Ab4:.5 Bb4:.5 A4:1 G4:2
G4:1 A4:1 B4:1 D5:2
F4:1 A4:.5 C5:.5 B4:1 A4:2
A4:1 C5:1 D5:1 C5:2
Bb4:1 D5:.5 Eb5:.5 C5:1 Bb4:2
G4:1 B4:1 C5:.5 B4:.5 A4:2
F4:1 Ab4:.5 Bb4:.5 C5:1 Bb4:2
Eb4:1 F4:1 G4:1 Bb4:2
Eb4:1 G4:.5 Ab4:.5 F4:1 G4:2
F#4:1 A4:1 B4:1 A4:2
D4:1 G4:.5 A4:.5 G4:1 F4:2
D4:1 F4:1 Eb4:1 D4:2
Eb4:2 D4:1 Eb4:2
''',
 lh='''
C3:2 Eb3:3
F3:5
Bb2:2 D3:3
C3:4 E3:1
D3:3 F3:2
F3:5
Eb3:2 G3:3
C3:2 E3:3
Db3:2 F3:3
Ab2:4 C3:1
F3:5
D3:2 F#3:3
G2:2 B2:3
G2:2 B2:3
C3:5
''',
 lh_upper='''
G3:1 Bb3:1 D4:1 C4:2
Ab3:1 C4:.5 Eb4:.5 D4:1 C4:2
F3:1 Ab3:1 C4:.5 Bb3:2.5
E3:4/5 G3:4/5 A3:4/5 B3:4/5 C4:4/5 D4:1
F3:1 A3:1 C4:1 E4:1 D4:1
A3:1 C4:1 E4:.5 D4:2.5
Bb3:1 D4:1 F4:1 Eb4:2
G3:1 B3:.5 A3:.5 D4:1 C4:2
Ab3:1 C4:1 Eb4:1 Db4:2
C3:4/5 Eb3:4/5 F3:4/5 G3:4/5 Ab3:4/5 Bb3:1
Ab3:1 C4:1 Eb4:.5 D4:2.5
A3:1 C4:1 E4:.5 D4:2.5
D3:1 F3:1 A3:.5 G3:2.5
D3:1 F3:1 Ab3:.5 G3:2.5
G3:2 Bb3:1 A3:2
''',sections={1:'p',2:'mp',3:'pp',4:'p',6:'mp',8:'p',9:'pp',10:'p',12:'mp',13:'p',14:'pp'},words={1:'poco rubato',14:'poco rit.'},
 slurs=[(1,3),(4,8),(9,12),(13,15)],lower_phrases=[(1,2),(3,5),(6,8),(9,11),(12,13),(14,15)],
 hairpins=[('crescendo',1,2),('diminuendo',2,3),('crescendo',4,6),('diminuendo',6,8),('crescendo',9,12),('diminuendo',13,15)],tempo_changes={},group=3,
 performance=dict(rubato=[56,53,49,60,52,57,59,51,48,56,49,53,47,41,32],
  phrase_arcs=[[0,14,3],[15,39,4],[40,59,4],[60,75,-2]],
  lower_entries=[[0,5],[40,45],[65,75]],tenor_entries=[[15,20],[45,50]],pedal_lift=.22,gate=.995,
  note='The quintuplet tenor comes forward slightly while the held bass remains quiet. Its five-note gesture leads into a shared arrival on the last beat, with the upper voices retaining their own timing. The final minor sixth is allowed to settle without a hard accent.'))
]
