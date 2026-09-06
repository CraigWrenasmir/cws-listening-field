"""Individually composed studies for Volume 05, Op. 97–120."""
PIECES=[
dict(op=97,title='Anemone Margin',key='b',fifths=2,meter='9/8',bpm=54,
 description='A new branch from Velvet Estuary carries its A–C–D–C contour into B–D–E–D. Anticipated notes tie across the compound bar lines, while three quintuplet turns move inside the RH beneath held upper notes. G-major, F-major and A-major colours widen the B-minor centre. A quieter descent brings the melody back to a compact minor ninth.',
 difficulty='Advanced compound-metre phrasing with inner-voice quintuplets',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The RH inner voice has five equal eighths across two quarter beats in bars 6, 10 and 14, followed by a held note. Keep the upper note finger-held for the whole bar and let the inner turn pass lightly beneath it. Upper ties anticipate bars 4, 9 and 16. The LH briefly uses treble clef in bar 14, returning to bass clef in bar 15.',
 parent_opus=2,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4.5,pitches=['B','D','E','D']),
 ancestry=dict(source_opus=2,source_hand='rh',source_start_beat=0,source_end_beat=4.5,source_pitches=['A','C','D','C'],transposition_semitones=2),
 hidden_voice_rests={'inner':[1,2,3]},clef_changes={'lh':{14:'treble',15:'bass'}},
 tuplet_groups=[dict(hand='rh',actual=5,normal=4,count=15)],
 tuplet_spans=[dict(hand='rh',voice='inner',start_beat=s,end_beat=s+2,actual=5,normal=4,stem='down') for s in [22.5,40.5,58.5]],
 system_starts=[1,3,5,6,8,10,12,14,16,18,20],page_starts=[8,16],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4.5+left,(bar-1)*4.5+right-.18] for bar,cuts in enumerate([[0,1,1.5,2,2.5,3.5,4.5],[0,1.5,2,2.5,3.5,4.5],[0,1,2,2.5,3.5,4,4.5],[0,1,2,3,4.5],[0,1.5,2,2.5,3.5,4.5],[0,1,2,3,3.5,4.5],[0,1.5,2,2.5,3,3.5,4.5],[0,1.5,2.5,3,3.5,4,4.5],[0,1,2,3,4.5],[0,1,2,3,3.5,4.5],[0,1.5,2,2.5,3.5,4.5],[0,1,1.5,2,2.5,3,3.5,4.5],[0,1.5,2,2.5,3.5,4.5],[0,1,2,3,3.5,4.5],[0,1,2,2.5,3.5,4,4.5],[0,1,1.5,2,2.5,3,3.5,4.5],[0,1,1.5,2,2.5,3.5,4.5],[0,1,1.5,2,2.5,3.5,4.5],[0,1,2,2.5,3,3.5,4.5],[0,4.5]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
B4:1 D5:.5 E5:1 D5:2
C#5:2 B4:.5 A4:1 G4:1
F#4:1 A4:1 B4:2 C#5:.5~
C#5:1 D5:1 F#5:1 E5:1.5
D5:2 F#5:1 A5:1.5
B5:3~ B5:1.5
A5:1.5 G5:1 F#5:1 E5:1
D5:3 C#5:1 B4:.5~
B4:1 D5:1 F5:1 G5:1.5
A5:3~ A5:1.5
G5:2 F5:.5 Eb5:1 D5:1
C5:1.5 Eb5:1 G5:1 F5:1
E5:2 G5:1 B5:1.5
A5:3~ A5:1.5
F#5:1 E5:1 D5:2 C#5:.5~
C#5:1 B4:1 A4:1 F#4:1.5
G4:1 B4:.5 D5:1 C#5:2
B4:1 D5:1 E5:1.5 C#5:1
A4:2 C#5:1 E5:1.5
B4+D5+F#5+A5:3~ B4+D5+F#5+A5:1.5
''',
 rh_inner='''
R:4.5
R:4.5
R:4.5
F#4:2 A4:1 B4:1.5
A4:2 C5:1 D5:1.5
D5:2/5 F#5:2/5 G5:2/5 F#5:2/5 E5:2/5 D5:2.5
C5:1.5 B4:1 A4:2
G4:3 A4:1 F#4:.5
G4:2 A4:1 Bb4:1.5
C5:2/5 E5:2/5 F5:2/5 E5:2/5 D5:2/5 C5:2.5
Bb4:2 A4:.5 G4:2
Ab4:1.5 Bb4:1 C5:2
B4:2 D5:1 E5:1.5
C#5:2/5 E5:2/5 F#5:2/5 E5:2/5 D5:2/5 C#5:2.5
B4:2 A4:2 G4:.5
G4:1 F#4:1 E4:1 D4:1.5
D4:1 F#4:.5 A4:1 G4:2
F#4:2 G4:1.5 A4:1
E4:2 G4:1 A4:1.5
C#5:3~ C#5:1.5
''',
 lh='''
B2:1 F#3:1 A3:.5 C#4:1 B3:1
G2:1.5 D3:1 F#3:1 A3:1
E3:2 B3:.5 D4:1 C#4:1
A2:1 E3:1 G3:1 C#4:1.5
D3:1.5 A3:1 C4:1 E4:1
G3:1 D4:1 F#4:1 E4:.5 D4:1
C3:2 G3:1 B3:.5 D4:1
F#3:1.5 C#3:1 E3:1 A3:1
G2:1 D3:1 F3:1 A3:1.5
F3:1 C4:1 E4:1 D4:.5 C4:1
Bb2:1.5 F3:1 Ab3:1 C4:1
Eb3:1 Bb3:1 Db4:1 C4:1.5
C3:1.5 G3:1 B3:1 D4:1
A3:1 E4:1 G4:1 F#4:.5 E4:1
D3:1 A3:1 C4:.5 B3:1 A3:1
G2:1.5 D3:1 F#3:1 B3:1
E3:1 B3:1 D4:.5 B3:1 A3:1
B2:1.5 F#3:1 A3:1 C#4:1
F#3:1 C#3:1 E3:.5 G#3:1 A#3:1
B2+F#3:3~ B2+F#3:1.5
''',sections={1:'p',2:'pp',3:'p',4:'p',5:'mp',6:'p',7:'pp',8:'p',9:'p',10:'mp',11:'pp',12:'p',13:'mp',14:'p',15:'pp',16:'p',17:'pp',18:'p',19:'pp',20:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,16),(17,20)],lower_phrases=[(1,4),(5,5),(6,6),(7,8),(9,12),(13,14),(15,16),(17,18),(19,20)],
 hairpins=[('crescendo',1,3),('diminuendo',4,7),('crescendo',8,10),('diminuendo',11,12),('diminuendo',13,16),('diminuendo',17,20)],tempo_changes={},group=2,
 performance=dict(rubato=[54,48,53,50,57,52,46,49,51,55,45,50,56,51,44,48,43,47,36,28],
  phrase_arcs=[[0,17.5,3],[18,35.5,4],[36,53.5,3],[54,71.5,3],[72,90,-2]],
  lower_entries=[[9,13.5],[67.5,76.5]],inner_entries=[[22.5,27],[40.5,45],[58.5,63]],pedal_lift=.18,gate=.995,
  note='The familiar contour returns with room around it, while the anticipated notes connect phrases across the bar lines. Each inner quintuplet turn is a small, unhurried breath under a held melody. The lower-register coda settles into a soft minor ninth.'))
,
dict(op=98,title='Aconite Threshold',key='G',fifths=1,meter='5/4',bpm=52,
 description='Anemone Margin’s five closing RH pitches remain, but a new G bass changes their meaning into a bright major thirteenth with a raised fourth. Its G–B–D–C-sharp phrase then appears an octave higher. Paired melodic fourths drift through contrasting bass harmonies before the two upper lines separate. The final G-major thirteenth releases the opening’s sharper colour.',
 difficulty='Advanced quartal voicing and harmonic reinterpretation',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The opening keeps the preceding piece’s B–C-sharp–D–F-sharp–A upper sonority over a new G. Give its close inner spacing a soft balance. Bars 2, 6 and 10 use matching rhythmic figures a perfect fourth apart; the later counter-lines are more independent. The LH briefly changes to treble clef in bar 15. The closing upper E replaces the earlier C-sharp colour.',
 parent_opus=97,motif=dict(hand='rh',voice='upper',start_beat=5,end_beat=10,pitches=['G','B','D','C#']),
 ancestry=dict(source_opus=97,source_hand='rh',source_voice='upper',source_start_beat=72,source_end_beat=76.5,source_pitches=['G','B','D','C#'],transposition_semitones=0),
 clef_changes={'lh':{15:'treble',16:'bass'}},
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*5+left,(bar-1)*5+right-.22] for bar,cuts in enumerate([[0,5],[0,1,2,3,4,5],[0,1,2,3,5],[0,1,2,3,4,5],[0,2,3,4,5],[0,1,2,3,5],[0,2,3,4,5],[0,2,3,4,5],[0,1,2,3,5],[0,1,2,3,4,5],[0,2,3,4,5],[0,1,2,3,5],[0,1,2,3,4,5],[0,1,2,3,5],[0,1,2,3,4,5],[0,5]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
B4+D5+F#5+A5:3~ B4+D5+F#5+A5:2
G5:1 B5:1 D6:1 C#6:2
B5:2 A5:1 G5:2
F#5:1 E5:1 D5:3
E5:3 G5:1 A5:1
F5:1 A5:1 C6:1 B5:2
A5:2 G5:1 F5:2
Eb5:3 D5:1 C5:1
D5:2 F5:1 G5:2
D5:1 F#5:1 A5:1 G#5:2
F#5:3 E5:1 D5:1
C#5:2 E5:1 G#5:2
F#5:1 E5:1 D#5:1 C#5:2
D5:2 F5:1 A5:2
G5:2 F5:1 E5:2
A4+B4+D5+F#5:3~ A4+B4+D5+F#5:2
''',
 rh_inner='''
C#5:3~ C#5:2
D5:1 F#5:1 A5:1 G#5:2
F#5:2 E5:1 D5:2
C5:1 B4:1 A4:3
B4:2 C5:1 D5:1 E5:1
C5:1 E5:1 G5:1 F#5:2
E5:2 D5:1 C5:2
Bb4:3 A4:1 G4:1
A4:2 C5:1 D5:2
A4:1 C#5:1 E5:1 D#5:2
B4:3 A4:1 G4:1
G#4:2 B4:1 D#5:2
A4:2 B4:1 A4:2
Bb4:2 C5:1 D5:2
B4:1 D5:1 C5:1 Bb4:2
E5:3~ E5:2
''',
 lh='''
G3:5
E3:2 B3:1 D4:1 C#4:1
A2:1 E3:1 G3:1 B3:2
D3:2 A3:1 C4:1 E4:1
C3:2 G3:1 B3:1 D4:1
D3:1 A3:1 C4:1 E4:2
G3:2 D3:1 F3:1 A3:1
C3:2 G3:1 Bb3:1 D4:1
Ab3:1 Eb3:1 G3:1 Bb3:2
B2:2 F#3:1 A3:1 C#4:1
E3:2 B3:1 D4:1 F#3:1
C#3:1 G#3:1 B3:1 D#4:2
F#3:2 C#4:1 E4:1 D#4:1
D3:1 A3:1 C4:1 E4:2
G3:2 D4:1 F4:1 E4:1
G3+D4:3~ G3+D4:2
''',sections={1:'pp',2:'p',3:'mp',4:'pp',5:'p',6:'mp',7:'p',8:'pp',9:'p',10:'mp',11:'pp',12:'p',13:'pp',14:'p',15:'p',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,16)],lower_phrases=[(2,3),(4,5),(6,7),(8,9),(10,11),(12,13),(14,15)],
 hairpins=[('crescendo',2,3),('diminuendo',4,5),('crescendo',6,7),('diminuendo',8,9),('crescendo',10,12),('diminuendo',13,16)],tempo_changes={},group=2,
 performance=dict(rubato=[52,56,50,46,51,55,48,44,52,56,46,50,45,49,39,29],
  phrase_arcs=[[0,4.8,0],[5,19.5,4],[20,39.5,3],[40,59.5,4],[60,80,-2]],
  lower_entries=[[0,5],[35,45]],inner_entries=[[5,10],[25,30],[45,50],[65,75]],pedal_lift=.22,gate=.995,
  note='The unchanged opening upper notes acquire a different warmth when the bass becomes G. Let the paired fourths move as soft harmonic planes, then bring out the counter-lines as they separate. The last chord settles without the opening’s raised-fourth edge.'))
]
