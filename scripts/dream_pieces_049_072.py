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
]
