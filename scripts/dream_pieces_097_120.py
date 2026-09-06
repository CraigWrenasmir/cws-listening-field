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
,
dict(op=99,title='Cyclamen Slipway',key='f',fifths=-4,meter='5/4',bpm=54,
 meters=['5/4','4/4','6/4','4/4','5/4','6/4','4/4','4/4','6/4','5/4','4/4','6/4','5/4','4/4','7/4'],
 description='A four-note inner fragment from Aconite Threshold becomes a melody whose major third softens into minor. Its bar lengths expand and contract around the phrases. Finger-held bass notes support a separate tenor, with three small streams of triplets passing underneath the upper melody. The opening returns in a shorter breath before an extended F-minor ninth.',
 difficulty='Advanced flexible-metre phrasing and sustained-bass independence',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Read each changing time signature as the length of a phrase rather than an accent pattern. In bars 3, 9 and 12, the LH tenor has six triplet eighths over the first two quarter beats while the bass remains finger-held. The hand reaches an octave in these passages. The LH uses treble clef only in bar 6. Upper ties connect bars 3–4 and 6–7; keep the line continuous over the new harmony.',
 parent_opus=98,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=5,pitches=['A','C','Bb','Ab']),
 ancestry=dict(source_opus=98,source_hand='rh',source_voice='inner',source_start_beat=70,source_end_beat=75,source_pitches=['B','D','C','Bb'],transposition_semitones=-2),
 clef_changes={'lh':{6:'treble',7:'bass'}},hidden_voice_rests={'tenor':[15]},
 tuplet_groups=[dict(hand='lh',actual=3,normal=2,count=18)],
 tuplet_spans=[dict(hand='lh',voice='tenor',start_beat=s,end_beat=s+1,actual=3,normal=2,stem='up') for s in [9,10,38,39,53,54]],
 system_starts=[1,3,5,6,8,9,11,12,14],page_starts=[6,11],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[base+left,base+right-.18] for base,cuts in [(0,[0,1.5,2,2.5,3.5,5]),(5,[0,1,2,3,4]),(9,[0,2,3,4,5,6]),(15,[0,1,1.5,2,3,4]),(19,[0,1,2,3,4,5]),(24,[0,2,3,4,5,6]),(30,[0,1,2,3,4]),(34,[0,1,2,4]),(38,[0,2,3,4,6]),(44,[0,1,2,3,5]),(49,[0,1,2,4]),(53,[0,2,3,4,6]),(59,[0,1,2,3,5]),(64,[0,.75,1.5,2.5,4]),(68,[0,7])] for left,right in zip(cuts,cuts[1:])],
 rh='''
A4:1.5 C5:1 Bb4:1 Ab4:1.5
G5:1 F5:1 Eb5:1 D5:1
F5:2 Ab5:1 G5:1 F5:1 Eb5:1~
Eb5:1 D5:.5 C5:.5 Bb4:2
Ab4:2 C5:1 Eb5:2
F5:3 Eb5:1 C5:1 Bb4:1~
Bb4:1 A4:1 G4:2
Ab4:1 B4:1 D5:2
C5:2 Eb5:1 G5:1 F5:2
F5:1 Ab5:1 G5:1 Eb5:2
D5:.5 Eb5:.5 F5:1 Ab5:2
G5:2 F5:1 E5:1 D5:2
C5:1 Eb5:.5 F5:.5 Eb5:1 D5:2
A4:.75 C5:.75 Bb4:1 Ab4:1.5
Ab4+C5+Eb5+G5:3~ Ab4+C5+Eb5+G5:4
''',
 lh='''
F3:3~ F3:2
Eb3:4
Db3:6
C3:4
F3:3~ F3:2
Ab3:6
D3:4
G3:4
C3:6
Db3:3~ Db3:2
Bb2:4
C3:6
F3:3~ F3:2
F3:4
F3+C4:3~ F3+C4:4
''',
 lh_upper='''
C4:2 D4:1 Eb4:2
Bb3:1 D4:1 C4:1 Bb3:1
Ab3:1/3 Bb3:1/3 C4:1/3 Db4:1/3 C4:1/3 Bb3:1/3 Ab3:2 F3:2
E3:1 G3:1 Bb3:1 A3:1
Ab3:1 C4:1 Eb4:1 D4:1 C4:1
Eb4:2 G4:1 F4:1 Eb4:1 C4:1
F3:1 A3:1 C4:1 B3:1
Bb3:1 Db4:1 E4:2
G3:1/3 Ab3:1/3 Bb3:1/3 C4:1/3 Bb3:1/3 Ab3:1/3 G3:2 Eb3:2
Ab3:2 C4:1 F3:2
F3:1 Ab3:1 G3:2
G3:1/3 A3:1/3 Bb3:1/3 C4:1/3 Bb3:1/3 A3:1/3 G3:2 E3:2
Ab3:1 C4:.5 D4:.5 C4:1 Bb3:2
C4:1 D4:1 Eb4:1 C4:1
R:7
''',sections={1:'p',2:'pp',3:'mp',4:'p',5:'p',6:'mp',7:'pp',8:'p',9:'p',10:'mp',11:'p',12:'p',13:'pp',14:'pp',15:'pp'},words={1:'poco rubato',14:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,15)],lower_phrases=[],
 hairpins=[('crescendo',1,2),('diminuendo',3,4),('crescendo',5,6),('diminuendo',7,8),('crescendo',9,10),('diminuendo',11,12),('diminuendo',13,15)],tempo_changes={},group=2,
 performance=dict(rubato=[54,49,57,48,53,56,45,50,55,52,48,51,44,39,27],
  phrase_arcs=[[0,18.7,3],[19,37.7,4],[38,58.7,3],[59,75,-2]],tenor_entries=[[9,15],[38,44],[53,59]],lower_entries=[[0,5],[68,75]],pedal_lift=.18,gate=.995,
  note='The changing bar lengths follow the upper breath. Keep the sustained lower notes soft, and allow the tenor triplets to move independently beneath the slower melody. The A-natural opening recolours into A-flat; its shorter return makes room for a long, quiet last chord.'))
,
dict(op=100,title='Lunaria Interstice',key='C',fifths=0,meter='6/4',bpm=56,
 description='Cyclamen Slipway’s ascending tenor fragment becomes G–A–B–C in the upper melody. A lower line reflects every interval in the opposite direction. The reflection returns in two new harmonic settings, while an additional RH voice opens the middle of the piece into four-part counterpoint. Near the end, both original lines return in reverse order, then give way to a quiet C-major ninth.',
 difficulty='Advanced contrary-motion counterpoint and four-voice balance',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The upper and tenor lines are exact interval reflections in bars 1, 7 and 11. In bar 15 both opening lines return in reverse order. Keep the bass lighter than the moving tenor, and distinguish the RH inner voice in bars 7–12 without hardening the melody. Sustained lower notes and moving tenor together reach an octave. The mirrored lines should sound like two phrases responding to one another, with no extra accent at each vertical meeting.',
 parent_opus=99,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=6,pitches=['G','A','B','C']),
 ancestry=dict(source_opus=99,source_hand='lh',source_voice='tenor',source_start_beat=9,source_end_beat=11,source_pitches=['Ab','Bb','C','Db'],transposition_semitones=-1),
 hidden_voice_rests={'inner':[1,2,3,4,5,6,13,14,15,16,17,18],'tenor':[18]},
 system_starts=[1,3,5,7,9,11,13,15,17],page_starts=[7,13],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*6+left,(bar-1)*6+right-.2] for bar,cuts in enumerate([[0,1.5,3,4.5,6],[0,2,3,4,6],[0,2,3,4,6],[0,1,2,3,4,5,6],[0,1,2,3,4,5,6],[0,1,2,3,4,6],[0,1.5,2,3,4,4.5,5,6],[0,2,3,4,6],[0,1,2,3,4,6],[0,1,2,3,4,6],[0,1.5,3,4.5,6],[0,1,2,3,4,6],[0,1,2,3,4,5,6],[0,1,2,3,4,5,6],[0,1.5,3,4.5,6],[0,2,3,4,5,6],[0,1,2,3,4,5,6],[0,6]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
G4:1.5 A4:1.5 B4:1.5 C5:1.5
B4:2 D5:1 F#5:1 E5:2
G5:3 F#5:1 E5:2
E5:2 D5:1 C5:2 B4:1
C5:1 Eb5:1 F5:1 Eb5:1 Db5:2
Bb4:2 Db5:1 F5:3
Db5:1.5 Eb5:1.5 F5:1.5 Gb5:1.5
F5:3 Eb5:1 Db5:2
E5:1 F#5:1 G#5:1 B5:3
A5:3 G5:1 E5:2
F5:1.5 Eb5:1.5 Db5:1.5 C5:1.5
Bb4:2 Db5:1 F5:1 Eb5:2
D5:1 F5:.5 G5:.5 A5:1 C6:1 B5:1 A5:1
G5:2 F5:1 E5:1 D5:2
C5:1.5 B4:1.5 A4:1.5 G4:1.5
F4:2 Ab4:1 C5:1 Bb4:2
A4:1 B4:1 D5:1 F5:1 E5:1 D5:1
E4+G4+B4+D5:3~ E4+G4+B4+D5:3
''',
 rh_inner='''
R:6
R:6
R:6
R:6
R:6
R:6
Ab4:2 Bb4:2 Cb5:1 Bb4:1
Ab4:3 G4:1 F4:2
B4:2 C#5:1 D#5:3
C5:1 D5:1 E5:1 D5:1 C5:2
Bb4:3 Ab4:3
F4:2 Ab4:1 C5:1 Bb4:2
R:6
R:6
R:6
R:6
R:6
R:6
''',
 lh='''
C3:6
B2:3 F#3:3
E3:4 C3:2
A2:3 E3:3
Db3:3 F3:3
Gb2:3 Db3:3
Gb3:6
Db3:6
E3:3 C#3:3
F3:4 D3:2
Db3:3 Eb3:3
Ab2:3 Eb3:3
G3:2 D3:2 F3:2
C3:6
C3:6
Db3:3 F3:3
G3:3 D3:3
C3+G3:3~ C3+G3:3
''',
 lh_upper='''
G3:1.5 F3:1.5 Eb3:1.5 D3:1.5
D3:2 F#3:1 A3:1 G3:2
G3:2 B3:1 D4:1 C4:2
E3:1 G3:1 A3:1 C4:1 B3:1 A3:1
F3:2 Ab3:1 C4:1 Bb3:1 Ab3:1
Db3:1 F3:1 Gb3:1 Ab3:1 F3:2
Db4:1.5 Cb4:1.5 A3:1.5 Ab3:1.5
F3:2 Ab3:1 C4:1 Bb3:2
G#3:1 B3:1 D#4:1 C#4:1 B3:2
A3:2 C4:1 E4:1 D4:2
F3:1.5 G3:1.5 A3:1.5 Bb3:1.5
Eb3:1 G3:1 Ab3:1 Bb3:1 G3:2
B3:2 A3:2 C4:2
G3:1 A3:1 Bb3:1 A3:1 G3:1 E3:1
D3:1.5 Eb3:1.5 F3:1.5 G3:1.5
Ab3:2 C4:1 Db4:1 C4:1 Ab3:1
B3:2 C4:1 A3:1 G3:1 F3:1
R:6
''',sections={1:'p',2:'pp',3:'mp',4:'p',5:'p',6:'pp',7:'mp',8:'p',9:'mp',10:'p',11:'pp',12:'p',13:'mp',14:'p',15:'pp',16:'p',17:'pp',18:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,14),(15,18)],lower_phrases=[],
 hairpins=[('crescendo',1,3),('diminuendo',4,6),('diminuendo',7,8),('diminuendo',9,12),('diminuendo',13,14),('diminuendo',15,18)],tempo_changes={},group=2,
 performance=dict(rubato=[56,51,58,49,54,48,57,50,60,52,46,51,59,50,44,47,37,28],
  phrase_arcs=[[0,23.7,4],[24,47.7,3],[48,71.7,4],[72,83.7,3],[84,108,-2]],
  tenor_entries=[[0,6],[36,42],[60,66],[84,90]],inner_entries=[[42,60],[66,72]],lower_entries=[[102,108]],pedal_lift=.2,gate=.995,
  note='Let the reflected voices have their own gentle direction. The four-voice middle becomes more luminous without growing much louder. The reversed opening recollects the earlier music in a quieter register; the final phrase takes progressively more time, ending in a soft major ninth.'))
,
dict(op=101,title='Mimosa Escapement',key='F',fifths=-1,meter='6/8',bpm=56,
 description='Lunaria Interstice’s descending tenor becomes A–G–F–E. This phrase gradually opens out: its durations grow to twice, four times and finally six times their original lengths. Shorter replies bring E-flat and D-flat colours into the F-major setting. The final E stays finger-held through three bars as the bass passes from C dominant through a G-flat altered dominant into F-major ninth.',
 difficulty='Advanced sustained phrasing and rhythmic augmentation',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The four-note phrase begins in bars 1, 3, 7 and 13, with written durations scaled by 1, 2, 4 and 6. Preserve the connected line through the ties in bars 7–8, 9–10 and 16–18. The final E is one nine-quarter-beat sound, held by the RH while the LH changes harmony and pedal beneath it. The last LH chord is compact but needs four softly balanced notes.',
 parent_opus=100,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','G','F','E']),
 ancestry=dict(source_opus=100,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=6,source_pitches=['G','F','Eb','D'],transposition_semitones=2),
 system_starts=[1,4,7,9,11,13,16],page_starts=[11],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*3+left,(bar-1)*3+right-.18] for bar,cuts in enumerate([[0,.75,1.5,2,3],[0,1,1.5,2,3],[0,1,2,3],[0,1.5,3],[0,1,2,3],[0,1,1.5,2,3],[0,1,1.5,2,3],[0,1,2,3],[0,1.5,3],[0,1,3],[0,1,2,3],[0,1,1.5,2,3],[0,1,2,3],[0,2,3],[0,1,1.5,2,3],[0,1,3],[0,1,3],[0,3]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
A4:.5 G4:.5 F4:.5 E4:1.5
D4:1 F4:.5 G4:.5 A4:1
A4:1 G4:1 F4:1
E4:3
G4:1 Bb4:.5 C5:.5 D5:1
C5:2 Bb4:1
A4:2 G4:1~
G4:1 F4:2
E4:3~
E4:3
G4:1 Bb4:1 Db5:1
C5:1 Ab4:1 Gb4:1
A4:3
G4:3
F4:3
E4:3~
E4:3~
E4:3
''',
 lh='''
F3:.75 C4:.75 D4:.5 C4:1
Bb2:1 F3:.5 A3:.5 C4:1
D3:1 A3:1 C4:1
A2+C3:1.5 G3+B3:1.5
Bb2:1 F3:1 A3:1
Eb3:1 Bb3:.5 D4:.5 C4:1
F3:1 C4:.5 Eb4:.5 D4:1
C3:1 G3:1 Bb3:1
D3+F3:1.5 A3+C4:1.5
C3+E3:1 G3+B3:2
Ab2:1 Eb3:1 G3:1
Db3:1 Ab3:.5 C4:.5 Bb3:1
F3:1 C4:1 D4:1
Eb3+G3:2 Bb3+D4:1
Bb2:1 F3:.5 Ab3:.5 C4:1
C3+E3:1 G3+Bb3:2
Gb2+Bb2:1 Fb3+A3:2
F3+G3+A3+C4:3
''',sections={1:'p',2:'pp',3:'p',4:'pp',5:'mp',6:'p',7:'p',8:'pp',9:'p',10:'pp',11:'mp',12:'p',13:'p',14:'pp',15:'p',16:'pp',17:'pp',18:'pp'},words={1:'poco rubato',16:'poco rit.'},
 slurs=[(1,2),(3,4),(5,6),(7,10),(11,12),(13,18)],lower_phrases=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18)],
 hairpins=[('diminuendo',1,2),('diminuendo',3,4),('diminuendo',5,6),('diminuendo',7,10),('diminuendo',11,12),('diminuendo',13,18)],tempo_changes={},group=3,
 performance=dict(rubato=[56,51,55,50,58,52,55,53,48,46,54,49,52,49,45,43,36,28],
  phrase_arcs=[[0,5.8,2],[6,11.8,2],[12,17.8,3],[18,29.8,2],[30,35.8,3],[36,54,-2]],lower_entries=[[45,54]],pedal_lift=.18,gate=.995,
  note='The slowing comes first from the written expansion of the melody. Leave its early form light and connected; the later versions have more space within the same contour. The final held E remains present through the changing lower harmony, with a little extra time before the soft F-major arrival.'))
,
dict(op=102,title='Calluna Observatory',key='b',fifths=2,meter='4/4',bpm=56,
 description='Mimosa Escapement’s descending phrase becomes B–A–G–F-sharp. Two long inner-voice flourishes place eleven equal notes across a complete four-beat bar, below a finger-held upper note and above two slower lower chords. Their related shapes illuminate G and E-flat harmonies. The surrounding counter-lines move through B minor, C, F and D-flat colours before a quiet B-minor sixth and ninth.',
 difficulty='Advanced eleven-note tuplets beneath a sustained melody',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 6 and 14 the RH inner voice plays eleven equal eighths in the time of eight, with one continuous 11:8 bracket. The upper note lasts all four beats; the LH changes dyads at the halfway point, between the sixth and seventh inner attacks. Keep the eleven-note line light and even inside the broader phrase. The combined RH stretch stays within ten semitones. The final G-sharp gives the minor close its sixth.',
 parent_opus=101,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['B','A','G','F#']),
 ancestry=dict(source_opus=101,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','G','F','E'],transposition_semitones=2),
 hidden_voice_rests={'inner':[1,2]},
 tuplet_groups=[dict(hand='rh',actual=11,normal=8,count=22)],
 tuplet_spans=[dict(hand='rh',voice='inner',start_beat=s,end_beat=s+4,actual=11,normal=8,stem='down',show_number='both') for s in [20,52]],
 system_starts=[1,3,5,6,7,9,11,13,14,15,17,19],page_starts=[7,14],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.2] for bar,cuts in enumerate([[0,1,2,3,4],[0,1,2,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,2,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,2,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
B4:1 A4:1 G4:1 F#4:1
E4:1 G4:.5 A4:.5 B4:2
C#5:2 E5:1 D5:1
C#5:1 B4:1 A4:2
D5:1 F#5:1 A5:2
B5:4
A5:2 G5:1 F#5:1
E5:1 D5:1 C#5:2
D5:2 F5:1 G5:1
A5:2 G5:1 E5:1
F5:1 Ab5:1 G5:2
Eb5:2 D5:1 C5:1
D5:1 F5:1 Bb5:2
G5:4
F5:2 Eb5:1 D5:1
C5:1 Eb5:1 G5:2
F#5:1 E5:1 D5:1 C#5:1
B4:1 D5:.5 E5:.5 F#5:2
A5:2 G#5:1 F#5:1
B4+D5+F#5+G#5:4
''',
 rh_inner='''
R:4
R:4
E4:2 G4:1 F#4:1
E4:1 D4:1 C#4:2
A4:1 C5:1 D5:2
D5:4/11 E5:4/11 F#5:4/11 G5:4/11 A5:4/11 G5:4/11 F#5:4/11 E5:4/11 D5:4/11 C#5:4/11 D5:4/11
C5:2 B4:1 A4:1
G4:1 F#4:1 E4:2
A4:2 C5:1 D5:1
C5:2 B4:1 G4:1
Ab4:1 C5:1 Bb4:2
G4:2 F4:1 Eb4:1
Bb4:1 C5:1 D5:2
Bb4:4/11 C5:4/11 D5:4/11 Eb5:4/11 F5:4/11 Eb5:4/11 D5:4/11 C5:4/11 Bb4:4/11 A4:4/11 Bb4:4/11
Ab4:2 G4:1 F4:1
E4:1 G4:1 B4:2
A4:1 G4:1 F#4:1 E4:1
F#4:1 A4:.5 B4:.5 C#5:2
C#5:2 B4:1 A4:1
C#5:4
''',
 lh='''
B2:1 F#3:1 A3:1 C#4:1
E3:1 B3:.5 D4:.5 C#4:2
A2:1 E3:1 G3:1 B3:1
F#3:1 C#3:1 E3:1 A3:1
D3:1 A3:1 C4:1 E4:1
G3+D4:2 F#3+A3:2
C3:1 G3:1 B3:1 D4:1
F#3:2 C#3:1 E3:1
G2:1 D3:1 F3:1 A3:1
F3:1 C4:1 E4:1 D4:1
Db3:1 Ab3:1 C4:1 Eb4:1
Ab3:1 Eb3:1 G3:1 Bb3:1
Bb2:1 F3:1 Ab3:1 C4:1
Eb3+Bb3:2 D3+F3:2
Ab2:1 Eb3:1 G3:1 Bb3:1
C3:1 G3:1 Bb3:1 D4:1
E3:1 B3:1 D4:1 C#4:1
B2:1 F#3:1 A3:1 C#4:1
F#3:1 C#4:1 E4:1 D#4:1
B2+F#3:4
''',sections={1:'p',2:'pp',3:'p',4:'pp',5:'mp',6:'p',7:'pp',8:'p',9:'p',10:'mp',11:'p',12:'pp',13:'mp',14:'p',15:'pp',16:'p',17:'pp',18:'p',19:'pp',20:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,16),(17,20)],lower_phrases=[(1,2),(3,4),(5,5),(6,6),(7,8),(9,10),(11,12),(13,13),(14,14),(15,16),(17,18),(19,20)],
 hairpins=[('crescendo',1,3),('diminuendo',4,7),('crescendo',8,10),('diminuendo',11,12),('diminuendo',13,16),('diminuendo',17,20)],tempo_changes={},group=2,
 performance=dict(rubato=[56,50,54,48,58,53,46,51,54,57,49,45,56,52,44,50,46,49,36,28],
  phrase_arcs=[[0,15.8,3],[16,31.8,4],[32,47.8,3],[48,63.8,4],[64,80,-2]],
  inner_entries=[[20,24],[52,56]],lower_entries=[[44,48],[60,68]],pedal_lift=.2,gate=.995,
  note='Each eleven-note flourish occupies one slow breath below a held melody. Its midpoint passes across the LH chord change without an accent. Leave space around those two phrases, and let the later descent settle into the warmer Dorian colour of the final minor sixth and ninth.'))
,
dict(op=103,title='Rain Prospect',key='Eb',fifths=-3,meter='4/4',bpm=54,
 description='Calluna Observatory’s E-flat–D–C–D becomes a melody above late-arriving jazz voicings. The left hand often enters after the upper phrase and leaves space between its chords. Three written pauses shared by both hands widen from one to one-and-a-half to two quarter beats. D-flat and C-major reflections lead back to a soft E-flat-major ninth.',
 difficulty='Advanced jazz voicing, delayed accompaniment and shared phrasing',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Keep the LH chord entries supple and quieter than the melody, especially when they arrive after an upper note. The shared rests across bars 4–5, 10–11 and 16–17 grow progressively longer; release the pedal before each gap and let the room carry the sound. The upper thirds in bars 9–10 and 15–16 should retain a single melodic direction. Balance the four-note RH closing chord lightly.',
 parent_opus=102,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['Eb','D','C','D']),
 ancestry=dict(source_opus=102,source_hand='rh',source_voice='upper',source_start_beat=44,source_end_beat=49,source_pitches=['Eb','D','C','D'],transposition_semitones=0),
 system_starts=[1,3,5,7,9,11,13,15,17,19],page_starts=[11],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right] for bar,spans in enumerate([[(1.5,2.8),(3,3.8)],[(0,1.3),(2,3.8)],[(.5,1.8),(2,2.8)],[(0,1.3),(1.5,3.3)],[(1.5,3.8)],[(0,.8),(1,2.8)],[(.5,1.8),(2,3.8)],[(0,1.8),(2,3.3)],[(1,1.8),(2,3.8)],[(0,.8),(1,2.8)],[(1.5,2.8),(3,3.8)],[(0,1.3),(2,3.8)],[(.5,1.8),(2,2.8)],[(0,1.8),(2,3.3)],[(1,1.8),(2,3.8)],[(0,.8),(1,2.3)],[(1.5,2.8),(3,3.8)],[(0,1.3),(2,3.8)],[(0,1.3),(1.5,2.8)],[(0,3.8)]],1) for left,right in spans],
 rh='''
Eb5:1 D5:.5 C5:1 D5:1.5
G5:2 F5:.5 Eb5:.5 D5:1
C5:1 Eb5:1 G5:1 F5:1
Eb5:1.5 D5:1 C5:1 R:.5
R:.5 Db5:1 F5:.5 Ab5:2
G5:1 F5:1 Eb5:2
Db5:1 F5:1 Eb5:1 C5:1
Bb4:2 Db5:.5 Eb5:.5 F5:1
Eb5+G5:1 Db5+F5:1 C5+Eb5:2
Bb4+Db5:1 C5+Eb5:1 Db5+F5:1 R:1
R:.5 E5:1 G5:.5 B5:2
A5:2 G5:.5 F5:.5 E5:1
D5:1 F5:1 A5:1 G5:1
F5:2 Eb5:1 D5:1
C5+Eb5:1 D5+F5:1 Eb5+G5:2
D5+F5:1 C5+Eb5:1 Bb4+Db5:.5 R:1.5
R:.5 Eb5:1 D5:.5 C5:1 D5:1
F5:1 Eb5:.5 D5:.5 C5:2
D5+F5:1 C5+Eb5:1 Bb4+D5:2
G4+Bb4+D5+F5:4
''',
 lh='''
R:1.5 Ab3+C4:1.5 Bb3+D4:1
G3+Bb3+D4:1.5 R:.5 Eb3+Bb3:2
R:.5 Ab3+C4+Eb4:1.5 G3+Bb3+D4:1 R:1
C3+G3:1.5 Bb3+Eb4:2 R:.5
R:1.5 F3+Ab3+C4:2.5
Bb2+F3:1 Ab3+C4+D4:2 R:1
R:.5 Eb3+Bb3:1.5 G3+Bb3+Db4:2
Ab2+Eb3:2 G3+Bb3+C4:1.5 R:.5
R:1 Db3+Ab3:1 F3+Ab3+C4:2
Bb2+F3:1 Ab3+C4:2 R:1
R:1.5 C3+G3:1.5 E3+B3:1
F3+C4:1.5 R:.5 A3+C4+E4:2
R:.5 Bb2+F3:1.5 A3+C4+E4:1 R:1
Eb3+Bb3:2 G3+C4:1.5 R:.5
R:1 Ab2+Eb3:1 G3+Bb3+Db4:2
Bb2+F3:1 Ab3+C4:1.5 R:1.5
R:1.5 Ab3+C4:1.5 Bb3+D4:1
G3+Bb3+Eb4:1.5 R:.5 F3+C4:2
Bb2+F3:1.5 Ab3+C4:1.5 R:1
Eb3+Bb3:4
''',sections={1:'p',2:'pp',3:'mp',4:'pp',5:'p',6:'pp',7:'p',8:'pp',9:'mp',10:'pp',11:'p',12:'mp',13:'p',14:'pp',15:'mp',16:'pp',17:'p',18:'pp',19:'pp',20:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,4),(5,10),(11,16),(17,20)],lower_phrases=[],
 hairpins=[('crescendo',1,3),('diminuendo',5,8),('diminuendo',9,10),('crescendo',11,13),('diminuendo',14,16),('diminuendo',17,20)],tempo_changes={},group=2,
 performance=dict(rubato=[54,49,55,45,52,48,53,46,51,42,56,50,54,45,49,39,47,44,36,28],
  phrase_arcs=[[0,15.5,3],[16.5,39,4],[40.5,62.5,4],[64.5,80,-2]],lower_entries=[[18,20],[42,44]],pedal_lift=.2,gate=.995,
  note='Let the melody begin before the lower harmony settles beneath it. The growing written pauses are breaths inside the larger arc, with the pedal released and the room left to resonate. The final return stays quieter, and the last major ninth has time to fade.'))
,
dict(op=104,title='Copper Headland',key='a',fifths=0,meter='9/8',bpm=55,
 description='Rain Prospect’s B-flat–D-flat–E-flat–F rises into A–C–D–E. Three arpeggios begin in the LH and continue seamlessly in the RH inner voice beneath a held melody. A fourth turns back down, passing from the RH to the LH. Their quieter endings leave the upper note alone. The surrounding phrases trace A-minor, G-major and A-flat colours before a minor-ninth close.',
 difficulty='Advanced arpeggio handovers beneath a sustained upper voice',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 4, 8 and 14, the LH plays three eighths and the RH inner voice continues with three more, without a break. The upper melody is held for the complete 9/8 bar. In bar 18 the direction reverses: three RH inner eighths pass to three LH eighths. Keep the handover even, then allow the moving voices to rest while the upper note remains. The LH uses treble clef for bar 18 and returns to bass clef in bar 19.',
 parent_opus=103,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4.5,pitches=['A','C','D','E']),
 ancestry=dict(source_opus=103,source_hand='rh',source_start_beat=28,source_end_beat=32,source_pitches=['Bb','Db','Eb','F'],transposition_semitones=-1),
 hidden_voice_rests={'inner':[1,2,3,5,6,7,9,10,11,12,13,15,16,17,19,20]},clef_changes={'lh':{18:'treble',19:'bass'}},
 system_starts=[1,3,4,5,7,8,9,11,13,14,15,17,18,19],page_starts=[8,15],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4.5+left,(bar-1)*4.5+right-.2] for bar,cuts in enumerate([[0,1,1.5,2,2.5,4.5],[0,1.5,2.5,3.5,4.5],[0,1,2,3,4.5],[0,3],[0,1,2,2.5,3,4.5],[0,1,1.5,2,2.5,3,4.5],[0,1,1.5,2.5,3.5,4.5],[0,3],[0,1.5,2,2.5,3,4.5],[0,1,1.5,2.5,3.5,4.5],[0,1,1.5,2,2.5,3.5,4.5],[0,1.5,2,2.5,3.5,4.5],[0,1,2,2.5,3,4.5],[0,3],[0,1,1.5,2,2.5,4.5],[0,1.5,2.5,3.5,4.5],[0,1,1.5,2,2.5,4.5],[0,3],[0,1.5,2.5,3.5,4.5],[0,4.5]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
A4:1 C5:.5 D5:1 E5:2
F5:1.5 E5:1 D5:1 C5:1
B4:1 D5:1 E5:1 F5:1.5
B4:3~ B4:1.5
C5:2 E5:1 G5:1.5
F5:1 A5:.5 G5:1 E5:2
D5:1 F#5:.5 A5:1 G5:2
D5:3~ D5:1.5
E5:2 G5:1 B5:1.5
A5:1.5 G5:1 E5:1 D5:1
C5:1.5 Eb5:1 F5:1 G5:1
F5:2 Eb5:.5 Db5:1 C5:1
Bb4:1 Db5:1 Eb5:1 F5:1.5
Bb4:3~ Bb4:1.5
C5:1 Eb5:.5 G5:1 F5:2
E5:1.5 D5:1 C5:1 B4:1
A4:1 C5:.5 D5:1 E5:2
E5:3~ E5:1.5
F5:1.5 E5:1 D5:1 B4:1
G4+B4+C5+E5:3~ G4+B4+C5+E5:1.5
''',
 rh_inner='''
R:4.5
R:4.5
R:4.5
R:1.5 E4:.5 G4:.5 A4:.5 R:1.5
R:4.5
R:4.5
R:4.5
R:1.5 F#4:.5 A4:.5 B4:.5 R:1.5
R:4.5
R:4.5
R:4.5
R:4.5
R:4.5
R:1.5 Eb4:.5 F4:.5 Ab4:.5 R:1.5
R:4.5
R:4.5
R:4.5
D5:.5 C5:.5 A4:.5 R:3
R:4.5
R:4.5
''',
 lh='''
A2:1 E3:1 G3:.5 B3:2
D3:1.5 A3:1 C4:2
G3:1 D3:1 F3:1 A3:1.5
D3:.5 A3:.5 C4:.5 R:3
C3:1 G3:1 B3:.5 D4:2
F3:1 C4:1 E4:1 D4:1.5
B2:1.5 F#3:1 A3:1 C#4:1
G3:.5 B3:.5 D4:.5 R:3
C3:1.5 G3:1 B3:2
F3:1 C4:.5 E4:1 D4:2
Ab3:1 Eb3:1 G3:1 Bb3:1.5
Db3:1.5 Ab3:1 C4:2
Bb2:1 F3:1 Ab3:.5 C4:2
Ab2:.5 Eb3:.5 G3:.5 R:3
Eb3:1 Bb3:1 Db4:.5 C4:2
E3:1.5 B3:1 D4:2
A2:1 E3:1 G3:.5 B3:2
R:1.5 G4:.5 E4:.5 C4:.5 R:1.5
D3:1.5 A3:1 C4:1 E4:1
A2+E3:3~ A2+E3:1.5
''',sections={1:'p',2:'pp',3:'p',4:'pp',5:'p',6:'mp',7:'p',8:'pp',9:'mp',10:'p',11:'p',12:'pp',13:'p',14:'pp',15:'mp',16:'p',17:'pp',18:'p',19:'pp',20:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,16),(17,20)],lower_phrases=[(1,2),(3,3),(5,6),(7,7),(9,10),(11,12),(13,13),(15,16),(17,17),(19,20)],
 hairpins=[('crescendo',1,3),('crescendo',5,6),('diminuendo',7,8),('diminuendo',9,12),('crescendo',13,15),('diminuendo',16,20)],tempo_changes={},group=2,
 performance=dict(rubato=[55,49,53,47,54,58,51,46,59,51,53,45,52,44,56,48,45,48,35,27],
  phrase_arcs=[[0,17.8,3],[18,35.8,4],[36,53.8,3],[54,71.8,4],[72,90,-2]],
  inner_entries=[[15,16.5],[33,34.5],[60,61.5],[76.5,78]],lower_entries=[[13.5,15],[31.5,33],[58.5,60],[78,79.5]],pedal_lift=.2,gate=.995,
  note='The moving arpeggio should retain its shape and weight as it changes hands. Hold the upper melody through each complete bar, including the space after the arpeggio ends. The descending handover later in the piece releases the movement back towards the lower register before the quiet minor ninth.'))
,
dict(op=105,title='Ochre Vestibule',key='d',fifths=-1,meter='6/8',bpm=54,
 meters=['6/8','6/8','6/8','6/8','3/4','3/4','3/4','3/4','6/8','6/8','6/8','6/8','3/4','3/4','3/4','3/4','6/8','6/8','6/8','6/8','3/4','3/4','3/4','6/8'],
 description='Copper Headland’s C–E-flat–F–G becomes D–F–G–A. Equal-length bars alternate between compound and simple readings, while three paired passages set three upper quarter notes against two dotted-quarter lower chords. Tied notes connect the changing groups. D-minor, C-major and D-flat reflections return to a close-spaced minor ninth.',
 difficulty='Advanced hemiola, changing metre and jazz chord balance',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Every bar contains three quarter beats, whether written as 6/8 or 3/4. In bars 6–7, 14–15 and 22–23, the RH has three equal quarter notes while the LH has two equal dotted-quarter dyads. Keep the two layers independent without forcing an accent at their meetings. Upper ties connect bars 4–5, 11–12 and 19–20. The final RH chord uses all five fingers within a nine-semitone span.',
 parent_opus=104,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['D','F','G','A']),
 ancestry=dict(source_opus=104,source_hand='rh',source_voice='upper',source_start_beat=45,source_end_beat=49.5,source_pitches=['C','Eb','F','G'],transposition_semitones=2),
 polyrhythms=[dict(start_beat=s,end_beat=s+3,rh_notes=3,lh_notes=2) for s in [15,18,39,42,63,66]],
 system_starts=[1,4,7,10,13,16,19,22],page_starts=[13],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*3+left,(bar-1)*3+right-.18] for bar,cuts in enumerate([[0,1,1.5,2,2.5,3],[0,1,1.5,2,3],[0,1,1.5,2,3],[0,1,1.5,2,2.5,3],[0,1,1.5,2,3],[0,1,1.5,2,3],[0,1,1.5,2,3],[0,1,2,3],[0,1,1.5,2,3],[0,1,1.5,2,3],[0,1,1.5,2,2.5,3],[0,1,2,3],[0,1,2,3],[0,1,1.5,2,3],[0,1,1.5,2,3],[0,1,2,3],[0,1,1.5,2,3],[0,1,1.5,2,3],[0,1,1.5,2,2.5,3],[0,1,1.5,2,3],[0,1,2,3],[0,1,1.5,2,3],[0,1,1.5,2,3],[0,3]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
D5:1 F5:.5 G5:.5 A5:1
Bb5:1 A5:.5 G5:.5 F5:1
E5:1 G5:.5 A5:.5 Bb5:1
A5:1.5 G5:1 F5:.5~
F5:.5 E5:.5 D5:1 C5:1
F5:1 E5:1 D5:1
C5:1 Eb5:1 G5:1
F5:1 Eb5:1 D5:1
E5:1 G5:.5 A5:.5 G5:1
F#5:1 A5:.5 B5:.5 A5:1
G5:1.5 F#5:1 E5:.5~
E5:1 D5:1 C5:1
F5:1 Ab5:1 C6:1
Ab5:1 Gb5:1 F5:1
Eb5:1 Db5:1 C5:1
Db5:1 F5:1 Ab5:1
G5:1 Bb5:.5 Ab5:.5 F5:1
Eb5:1 G5:.5 F5:.5 D5:1
C5:1.5 Eb5:1 G5:.5~
G5:1 F5:1 E5:1
D5:1 F5:1 A5:1
E5:1 D5:1 C#5:1
D5:1 F5:1 E5:1
C5+D5+E5+F5+A5:3
''',
 lh='''
D3:1 A3:1 C4:.5 E4:.5
Bb3:1.5 F3:.5 A3:1
G3:1 D3:.5 F3:.5 A3:1
A2:1 E3:.5 G3:.5 C#4:1
D3:1 F3:.5 A3:.5 C4:1
Bb2+F3:1.5 A3+C4:1.5
Eb3+Bb3:1.5 G3+Db4:1.5
C3:1 G3:1 Bb3:1
C3:1.5 G3:.5 B3:1
D3:1 A3:.5 C4:.5 E4:1
E3:1 B3:1 D4:.5 C#4:.5
A3:1 E3:1 G3:1
Db3:1 Ab3:1 C4:1
Db3+Ab3:1.5 C4+Eb4:1.5
Ab2+Eb3:1.5 Gb3+Bb3:1.5
Bb2:1 F3:1 Ab3:1
Eb3:1 Bb3:.5 Db4:.5 C4:1
C3:1.5 G3:.5 Bb3:1
Ab2:1 Eb3:1 G3:.5 Bb3:.5
C4:1 G3:.5 Bb3:.5 E4:1
D3:1 A3:1 C4:1
A2+E3:1.5 G3+B3:1.5
Bb2+F3:1.5 A3+C4:1.5
D3+A3:3
''',sections={1:'p',2:'mp',3:'p',4:'pp',5:'p',6:'p',7:'mp',8:'pp',9:'p',10:'mp',11:'p',12:'pp',13:'mp',14:'p',15:'pp',16:'p',17:'mp',18:'p',19:'pp',20:'p',21:'p',22:'pp',23:'pp',24:'pp'},words={1:'poco rubato',23:'poco rit.'},
 slurs=[(1,5),(6,8),(9,12),(13,16),(17,20),(21,24)],lower_phrases=[(1,2),(3,4),(5,5),(6,7),(8,8),(9,10),(11,12),(13,13),(14,15),(16,16),(17,18),(19,20),(21,21),(22,24)],
 hairpins=[('crescendo',1,3),('diminuendo',4,5),('diminuendo',6,8),('crescendo',9,10),('diminuendo',11,12),('diminuendo',13,16),('diminuendo',17,20),('diminuendo',21,24)],tempo_changes={},group=3,
 performance=dict(rubato=[54,49,55,48,53,51,50,46,54,57,49,45,56,52,48,46,55,50,47,44,51,45,38,27],
  phrase_arcs=[[0,14.8,3],[15,23.8,2],[24,35.8,4],[36,47.8,3],[48,59.8,3],[60,72,-2]],
  lower_entries=[[15,21],[39,45],[63,69]],pedal_lift=.18,gate=.995,
  note='The pulse can be heard in two or in three without changing the length of the bar. Let the hemiola passages float between those readings, keeping the upper notes connected and the lower chords soft. The tied phrases ease the transitions, and the last close-spaced minor ninth settles slowly.'))
,
dict(op=106,title='Silver Tidelock',key='c#',fifths=4,meter='9/8',bpm=54,
 description='Ochre Vestibule’s F-sharp–A–B–A becomes G-sharp–B–C-sharp–B. A six-note upper phrase is echoed an octave lower by the tenor, first a dotted quarter late, then an eighth late in a new key, and finally with both lines together. A sustained bass gives these converging echoes a quiet foundation. F-major, E-minor and A-flat shadows lead back to C-sharp-minor ninth.',
 difficulty='Advanced converging canons and sustained-bass counterpoint',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The complete six-note phrases in bars 1–2, 7–8 and 15–16 are echoed by the tenor an octave lower. Their entry delays are 1.5, 0.5 and zero quarter beats respectively; preserve the exact written ties as the earlier echoes cross bar lines. Keep the LH bass finger-held beneath the tenor, including its nine-beat E across bars 7–8. The two opening lines meet in octave motion in bars 15–16, without an extra accent.',
 parent_opus=105,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4.5,pitches=['G#','B','C#','B']),
 ancestry=dict(source_opus=105,source_hand='rh',source_start_beat=27,source_end_beat=30,source_pitches=['F#','A','B','A'],transposition_semitones=2),
 hidden_voice_rests={'tenor':[20]},
 system_starts=[1,3,5,7,9,11,13,15,17,19],page_starts=[11],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4.5+left,(bar-1)*4.5+right-.18] for bar,cuts in enumerate([[0,1,1.5,2,2.5,3,3.5,4.5],[0,1.5,2.5,4,4.5],[0,1,1.5,2.5,3.5,4.5],[0,2,2.5,3.5,4.5],[0,1,2,3,4.5],[0,2,2.5,3.5,4.5],[0,.5,1,1.5,2,2.5,4.5],[0,.5,2.5,3,4.5],[0,.5,1,1.5,2,2.5,3,4.5],[0,1.5,2.5,3.5,4.5],[0,2,2.5,3.5,4.5],[0,1.5,2.5,3.5,4.5],[0,1,1.5,2.5,4.5],[0,2,2.5,3.5,4.5],[0,1,1.5,2,4.5],[0,2.5,4.5],[0,1,1.5,2,2.5,4.5],[0,1.5,2.5,3.5,4.5],[0,1,2,3,4.5],[0,4.5]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
G#4:1 B4:.5 C#5:.5 B4:2.5
A4:2.5 G#4:2
B4:1 D#5:.5 E5:1 F#5:2
E5:2 D#5:.5 C#5:1 B4:1
A4:1 C5:1 D5:1 E5:1.5
F#5:2 E5:.5 D5:1 C5:1
B4:1 D5:.5 E5:.5 D5:2.5
C5:2.5 B4:2
A4:1 C5:1 D5:1 E5:1.5
G5:1.5 F#5:1 E5:1 D5:1
Eb5:2 Gb5:.5 Ab5:1 Bb5:1
Ab5:1.5 Gb5:1 F5:1 Eb5:1
D5:1 F5:.5 G5:1 A5:2
G5:2 F5:.5 E5:1 D5:1
F#4:1 A4:.5 B4:.5 A4:2.5
G4:2.5 F#4:2
G#4:1 B4:.5 C#5:1 D#5:2
E5:1.5 D#5:1 C#5:1 B4:1
A4:1 C#5:1 E5:1 D#5:1.5
G#4+B4+D#5+E5:3~ G#4+B4+D#5+E5:1.5
''',
 lh='''
C#3:3~ C#3:1.5
F#3:3~ F#3:1.5
E3:3~ E3:1.5
C#3:3~ C#3:1.5
F3:3~ F3:1.5
G3:3~ G3:1.5
E3:3~ E3:1.5~
E3:3~ E3:1.5
C3:3~ C3:1.5
C3:3~ C3:1.5
Ab3:3~ Ab3:1.5
Db3:3~ Db3:1.5
F3:3~ F3:1.5
C3:3~ C3:1.5
B2:3~ B2:1.5
E3:3~ E3:1.5
E3:2 G#3:2.5
B2:3~ B2:1.5
C#3:3~ C#3:1.5
C#3+G#3:3~ C#3+G#3:1.5
''',
 lh_upper='''
R:1.5 G#3:1 B3:.5 C#4:.5 B3:1~
B3:1.5 A3:2.5 G#3:.5~
G#3:1.5 A3:1 B3:1 C#4:1
A3:2 G#3:.5 F#3:1 E3:1
A3:1 C4:1 D4:1 B3:1.5
B3:2 D4:.5 F4:1 E4:1
R:.5 B3:1 D4:.5 E4:.5 D4:2~
D4:.5 C4:2.5 B3:1.5~
B3:.5 A3:1 G3:1 F#3:2
C4:1.5 B3:1 A3:1 G3:1
Cb4:2 Db4:.5 Eb4:1 F4:1
Bb3:1.5 Ab3:1 Gb3:1 F3:1
A3:1 C4:.5 D4:1 E4:2
C4:2 Bb3:.5 A3:1 G3:1
F#3:1 A3:.5 B3:.5 A3:2.5
G3:2.5 F#3:2
G#3:1 B3:.5 D#4:1 C#4:2
B3:1.5 A3:1 G#3:1 F#3:1
A3:1 G#3:1 F#3:1 E3:1.5
R:4.5
''',sections={1:'p',2:'pp',3:'p',4:'pp',5:'p',6:'mp',7:'p',8:'pp',9:'p',10:'mp',11:'p',12:'pp',13:'mp',14:'p',15:'pp',16:'pp',17:'p',18:'pp',19:'pp',20:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,4),(5,6),(7,10),(11,14),(15,20)],lower_phrases=[],
 hairpins=[('crescendo',1,3),('diminuendo',4,5),('diminuendo',6,8),('crescendo',9,10),('diminuendo',11,12),('diminuendo',13,16),('diminuendo',17,20)],tempo_changes={},group=2,
 performance=dict(rubato=[54,48,53,46,52,57,51,45,52,56,49,44,55,48,43,41,48,43,35,27],
  phrase_arcs=[[0,17.8,3],[18,26.8,3],[27,44.8,4],[45,62.8,3],[63,90,-2]],
  tenor_entries=[[1.5,10.5],[27.5,36.5],[63,72]],lower_entries=[[85.5,90]],pedal_lift=.18,gate=.995,
  note='Let the tenor echo retain the upper phrase’s shape, even as the distance between their entries contracts. The long bass holds stay quieter than either line. When the voices arrive together, let that convergence feel settled; the final phrase then opens out into a soft minor ninth.'))
,
dict(op=107,title='Fluorite Quayside',key='c',fifths=-3,meter='4/4',bpm=54,
 description='Silver Tidelock’s A–C-sharp–E–D-sharp becomes A-flat–C–E-flat–D. Two eight-beat passages leave the minor-key melody for a whole-tone field: E-flat is held above the first, F above the second, while inner dyads and lower notes shift underneath. The returning melody gathers those colours into a quiet C-minor sixth and ninth.',
 difficulty='Advanced whole-tone harmony and sustained upper-note voicing',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Hold the upper E-flat through bars 5–6 and F through bars 9–10. Each of those two-bar passages uses only D-flat, E-flat, F, G, A and B. The moving RH dyads stay beneath the held note; the widest combination reaches an octave. Keep the upper note present without pressing the lower pair. The final A-natural retains a little of the whole-tone colour inside the C-minor close.',
 parent_opus=106,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['Ab','C','Eb','D']),
 ancestry=dict(source_opus=106,source_hand='rh',source_voice='upper',source_start_beat=81,source_end_beat=85.5,source_pitches=['A','C#','E','D#'],transposition_semitones=-1),
 hidden_voice_rests={'inner':[1,2,3,4,7,8,11,12,13,14,15,16]},
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.2] for bar,cuts in enumerate([[0,1,1.5,2,2.5,4],[0,1.5,2,3,4],[0,1,1.5,2,3,4],[0,2,3,4],[0,2,4],[0,2,4],[0,1,1.5,2,3,4],[0,1,2,4],[0,2,4],[0,2,4],[0,1,2,3,4],[0,1,1.5,2,4],[0,1,2,3,4],[0,1,1.5,2,4],[0,1,2,3,4],[0,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
Ab4:1 C5:.5 Eb5:1 D5:1.5
G5:2 F5:1 Eb5:1
D5:1 F5:.5 G5:.5 Bb5:2
Ab5:2 G5:1 F5:1
Eb5:4~
Eb5:4
C5:1 Eb5:.5 F5:.5 G5:2
Ab5:1 G5:1 Eb5:2
F5:4~
F5:4
Eb5:2 D5:1 C5:1
Bb4:1 D5:.5 F5:.5 Ab5:2
G5:1 F5:1 Eb5:1 D5:1
C5:1 Eb5:.5 F5:.5 Eb5:2
D5:1 C5:1 Bb4:1 G4:1
A4+D5+Eb5+G5:4
''',
 rh_inner='''
R:4
R:4
R:4
R:4
G4+B4:2 A4+Db5:2
F4+A4:2 Eb4+G4:2
R:4
R:4
A4+Db5:2 B4+Eb5:2
G4+B4:2 F4+A4:2
R:4
R:4
R:4
R:4
R:4
R:4
''',
 lh='''
C3:1 G3:.5 Bb3:.5 D4:2
Ab2+Eb3:1.5 G3+Bb3:2.5
Bb2:1 F3:1 Ab3:1 C4:1
F3+Ab3:2 Eb3+G3:2
Eb3:2 A3:2
B2:2 F3:2
Ab2:1 Eb3:1 G3:1 Bb3:1
Db3+Ab3:2 C4+Eb4:2
Db3:2 G3:2
A2:2 Eb3:2
G2:1 D3:1 F3:1 Bb3:1
C3+G3:2 Bb3+Eb4:2
Ab3:1 Eb3:1 G3:1 Bb3:1
F3+A3:2 Eb3+G3:2
G2:1 D3:1 F3:1 B3:1
C3+G3:4
''',sections={1:'p',2:'pp',3:'mp',4:'p',5:'pp',6:'pp',7:'p',8:'mp',9:'pp',10:'pp',11:'p',12:'mp',13:'p',14:'pp',15:'pp',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,16)],lower_phrases=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16)],
 hairpins=[('crescendo',1,3),('diminuendo',4,6),('crescendo',7,8),('crescendo',9,12),('diminuendo',13,16)],tempo_changes={},group=2,
 performance=dict(rubato=[53,47,55,49,48,43,52,47,49,44,46,51,48,43,36,27],
  phrase_arcs=[[0,15.8,3],[16,23.8,1],[24,31.8,3],[32,39.8,1],[40,47.8,3],[48,64,-2]],
  inner_entries=[[16,24],[32,40]],lower_entries=[[56,64]],pedal_lift=.2,gate=.995,
  note='The held upper notes give the whole-tone fields a point of stillness while the lower colours move. Let those passages feel suspended, then recover a more melodic direction on returning to the minor-key phrases. The final natural sixth keeps the closing harmony open and warm.'))
,
dict(op=108,title='Slate Semaphore',key='eb',fifths=-6,meter='4/4',bpm=52,
 description='Fluorite Quayside’s A-flat–C–E-flat–D becomes G-flat–B-flat–D-flat–C in a lower singing line. The RH begins with quiet, sustained jazz voicings while the LH tenor carries the melody above its own held bass. The complete four-bar phrase then moves up an octave into the RH, with the lower accompaniment receding. A varied lower-voice return settles into E-flat-minor ninth.',
 difficulty='Advanced melody transfer and independent staff dynamics',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The LH tenor leads in bars 1–8 and 13–15, with RH chords marked pp above its p. In bars 9–12 the complete opening four-bar melody moves to the RH an octave higher; its p is accompanied by a lower pp. Keep the bass quieter than the tenor within the LH. The separate staff dynamics are reflected in the recording. The final two lower voices join into an E-flat-minor triad beneath the upper ninth colour.',
 parent_opus=107,motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=4,pitches=['Gb','Bb','Db','C']),
 ancestry=dict(source_opus=107,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4,source_pitches=['Ab','C','Eb','D'],transposition_semitones=-2),
 lower_sections={1:'p',9:'pp',13:'p',16:'pp'},hidden_voice_rests={'tenor':[9,10,11,12]},
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.2] for bar,cuts in enumerate([[0,1,1.5,2.5,4],[0,2,3,4],[0,1,1.5,2,4],[0,1,2,4],[0,1,1.5,2,4],[0,2,3,4],[0,1,2,3,4],[0,2,3,4],[0,1,1.5,2,2.5,4],[0,1,2,3,4],[0,1,1.5,2,4],[0,1,2,3,4],[0,1.5,2,3,4],[0,1,2,4],[0,1,1.5,2,4],[0,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
Bb4+Db5+F5+Ab5:4
Ab4+C5+Eb5+G5:4
Bb4+Db5+Eb5+Gb5:4
Ab4+C5+Eb5+G5:4
C5+E5+G5:2 B4+D5+F#5:2
A4+C5+E5:2 G4+B4+D5:2
Ab4+C5+Eb5:2 G4+Bb4+Db5:2
Gb4+Bb4+Db5:2 F4+Ab4+C5:2
Gb4:1 Bb4:.5 Db5:1 C5:1.5
Bb4:2 Ab4:1 Gb4:1
F4:1 Ab4:.5 Bb4:.5 Db5:2
C5:1 Bb4:1 Ab4:2
Gb4+Bb4+Eb5+F5:4
F4+Ab4+C5+Eb5:4
Ab4+C5+D5+F5:4
F4+Bb4+Db5:4
''',
 lh='''
Eb3:4
Db3:4
Eb3:4
F3:4
D3:4
C3:4
Db3:4
Cb3:4
Eb2:1 Bb2:1 Db3:.5 F3:1.5
Db3:1 Ab3:1 C4:1 Bb3:1
Eb3:1 Bb3:.5 Db4:.5 F3:2
F3:1 C4:1 Eb4:1 D4:1
Eb3:4
Db3:4
D3:4
Eb3:4
''',
 lh_upper='''
Gb3:1 Bb3:.5 Db4:1 C4:1.5
Bb3:2 Ab3:1 Gb3:1
F3:1 Ab3:.5 Bb3:.5 Db4:2
C4:1 Bb3:1 Ab3:2
F3:1 A3:.5 C4:.5 B3:2
E3:2 G3:1 A3:1
F3:1 Ab3:1 C4:1 Bb3:1
Eb3:2 Gb3:1 Ab3:1
R:4
R:4
R:4
R:4
Gb3:1.5 Bb3:.5 Db4:1 C4:1
Bb3:1 Ab3:1 Gb3:2
F3:1 Ab3:.5 Bb3:.5 C4:2
Gb3+Bb3:4
''',sections={1:'pp',2:'pp',3:'pp',4:'pp',5:'pp',6:'pp',7:'pp',8:'pp',9:'p',10:'p',11:'p',12:'p',13:'pp',14:'pp',15:'pp',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,16)],lower_phrases=[(9,10),(11,12)],
 hairpins=[('crescendo',1,3),('diminuendo',4,6),('crescendo',7,8),('crescendo',9,10),('diminuendo',11,12),('diminuendo',13,16)],tempo_changes={},group=2,
 performance=dict(rubato=[52,47,53,45,54,48,52,44,54,49,53,45,46,42,35,27],
  phrase_arcs=[[0,15.8,3],[16,31.8,3],[32,47.8,4],[48,64,-2]],
  tenor_entries=[[0,32],[48,64]],lower_entries=[],pedal_lift=.2,gate=.995,
  note='The lower melody begins in the foreground while the upper chords remain soft. Its transfer to the RH changes the balance without changing the four-bar phrase. On the lower-voice return, let the accompaniment soften again; the final chord brings both hands to the same quiet dynamic.'))
,
dict(op=109,title='Calcite Interchange',key='g',fifths=-2,meter='5/4',bpm=53,
 description='Slate Semaphore’s lower F–A-flat–B-flat–C becomes upper G–B-flat–C–D. A minor-key opening gives way to a brighter passage over one held G: seven five-beat upper phrases move past five seven-beat tenor phrases, meeting again after thirty-five beats. Their different breathing points create a gentle drift. Borrowed minor colours return before the G-minor ninth close.',
 difficulty='Advanced unequal phrase lengths over a sustained bass',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 5–11, hold bass G3 for thirty-five quarter beats while the LH tenor sings five seven-beat phrases above it. The RH has seven five-beat phrases. These are differing phrase lengths, not tuplets: their common pulse remains a quarter note. The tenor crosses four bar lines with ties; do not rearticulate those notes. B-natural gives the central passage its warmer colour before B-flat returns. Keep each hand’s phrase direction independent of the printed bar lines.',
 parent_opus=108,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=5,pitches=['G','Bb','C','D']),
 ancestry=dict(source_opus=108,source_hand='lh',source_voice='tenor',source_start_beat=56,source_end_beat=60,source_pitches=['F','Ab','Bb','C'],transposition_semitones=2),
 voice_phrases=[dict(voice='tenor',start_beat=start,end_beat=start+7,swell=4) for start in [20,27,34,41,48]],
 lower_sections={1:'pp',5:'p',12:'pp'},hidden_voice_rests={'tenor':[1,2,3,4,12,13,14,15,16,17]},
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*5+left,(bar-1)*5+right-.18] for bar,cuts in enumerate([[0,1,1.5,2,3,5],[0,1,1.5,2,2.5,3,5],[0,2,3,5],[0,1,1.5,2,3,5],[0,1,1.5,3,5],[0,1,1.5,2,3,3.5,5],[0,1,1.5,2,3,4,5],[0,.5,1,1.5,2,3,4,5],[0,1,1.5,2.5,3,4,5],[0,1,1.5,3,4.5,5],[0,1,1.5,3,5],[0,1,2,2.5,3,5],[0,1,1.5,2,3,5],[0,1,2,3,5],[0,1,1.5,2,3,5],[0,1,2,3,5],[0,5]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
G4:1 Bb4:.5 C5:1.5 D5:2
F5:1.5 Eb5:1 D5:.5 C5:2
Bb4:2 A4:1 G4:2
F4:1 A4:.5 C5:1.5 Eb5:2
G4:1 B4:.5 D5:1.5 E5:2
D5:1 C5:.5 A4:1.5 G4:2
B4:1 D5:.5 F5:1.5 E5:2
A4:1 C5:.5 D5:1.5 G5:2
F5:1 E5:.5 C5:1.5 B4:2
D5:1 B4:.5 A4:1.5 G4:2
A4:1 D5:.5 C5:1.5 B4:2
Eb5:2 D5:.5 C5:.5 Bb4:2
Db5:1 F5:.5 Ab5:1.5 G5:2
F5:1 Eb5:1 D5:1 C5:2
Bb4:1 D5:.5 F5:1.5 E5:2
D5:1 C5:1 A4:1 G4:2
A4+Bb4+D5+F5:3~ A4+Bb4+D5+F5:2
''',
 lh='''
G2:1 D3:1 F3:1 A3:2
Eb3:1 Bb3:1 D4:1 G3:2
C3:2 G3:1 Bb3:2
D3:1 A3:1 C4:1 F#3:2
G3:3~ G3:2~
G3:3~ G3:2~
G3:3~ G3:2~
G3:3~ G3:2~
G3:3~ G3:2~
G3:3~ G3:2~
G3:3~ G3:2
Eb3:1 Bb3:1 D4:1 G3:2
Bb2:1 F3:1 Ab3:1 C4:2
Eb3+G3:2 D3+F#3:1 C4:2
C3:1 G3:1 Bb3:1 E4:2
D3:1 A3:1 C4:1 F#3:2
G3+D4:3~ G3+D4:2
''',
 lh_upper='''
R:5
R:5
R:5
R:5
B3:1.5 D4:1.5 E4:2
D4:2 A3:1.5 C4:1.5
D4:2 F4:2 E4:1~
E4:.5 D4:1.5 B3:2 A3:1~
A3:1 C4:1.5 B3:1.5 A3:1~
A3:1 D4:2 F4:1.5 E4:.5~
E4:1 D4:2 B3:2
R:5
R:5
R:5
R:5
R:5
R:5
''',sections={1:'p',2:'mp',3:'p',4:'pp',5:'p',6:'p',7:'p',8:'mp',9:'p',10:'p',11:'pp',12:'p',13:'mp',14:'p',15:'p',16:'pp',17:'pp'},words={1:'poco rubato',16:'poco rit.'},
 slurs=[(1,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,14),(15,17)],lower_phrases=[(1,2),(3,4),(12,13),(14,15),(16,17)],
 hairpins=[('crescendo',1,2),('diminuendo',3,4),('crescendo',5,8),('diminuendo',9,11),('crescendo',12,13),('diminuendo',14,17)],tempo_changes={},group=2,
 performance=dict(rubato=[53,47,49,43,54,52,53,51,54,50,46,48,53,49,46,38,28],
  phrase_arcs=[[0,19.8,3],[20,24.8,2],[25,29.8,2],[30,34.8,2],[35,39.8,2],[40,44.8,2],[45,49.8,2],[50,54.8,1],[55,69.8,3],[70,85,-2]],
  tenor_entries=[[20,55]],lower_entries=[],pedal_lift=.18,gate=.995,
  note='Keep the G bass very soft beneath the two circulating melodies. The upper line breathes every five beats; the tenor makes a longer seven-beat journey. Let the return to minor colour feel like a change of light rather than an abrupt interruption. The final ninth opens out as the pulse slows.'))
,
dict(op=110,title='Nacre Turnstile',key='f',fifths=-4,meter='4/4',bpm=54,
 description='Calcite Interchange’s G–B-flat–C–D becomes F–A-flat–B-flat–C. One A-flat–C–E-flat–G chord stays held through six bars while the bass descends F–E–E-flat–D–D-flat–C and a tenor line continues beneath it. The unchanged upper harmony takes on increasingly chromatic meanings. A more mobile passage carries those colours back to an octave-raised return and a minor sixth/ninth close.',
 difficulty='Advanced chromatic bass harmony and sustained chord voicing',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Hold all four RH notes throughout bars 5–10 without rearticulation. The bass descends one semitone per bar; the LH tenor must remain distinct above each four-beat bass note. Pedal refreshes clear the changing lower notes while the upper chord stays finger-held. The LH reaches eleven semitones under the tenor at two points. Three longer tenor slurs shape the six-bar passage. The opening melody returns an octave higher in bar 17 before folding into the final F-minor sixth/ninth.',
 parent_opus=109,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['F','Ab','Bb','C']),
 ancestry=dict(source_opus=109,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=5,source_pitches=['G','Bb','C','D'],transposition_semitones=-2),
 lower_sections={1:'pp',5:'p',11:'pp'},hidden_voice_rests={'tenor':[1,2,3,4,11,12,13,14,15,16,17,18,19,20]},
 voice_phrases=[dict(voice='tenor',start_beat=start,end_beat=start+8,swell=3) for start in [16,24,32]],
 system_starts=[1,3,5,7,9,11,13,15,17,19],page_starts=[11],engraving=dict(spacing_system=11,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.18] for bar,cuts in enumerate([[0,1,1.5,2,2.5,4],[0,1.5,2,4],[0,1,1.5,2,3,4],[0,1,2,3,4],[0,1,1.5,3,4],[0,1.5,2,3,4],[0,1,2,4],[0,1,1.5,3,4],[0,2,3,4],[0,1,2,2.5,4],[0,1,1.5,2,3,4],[0,1.5,2,4],[0,1,1.5,2,4],[0,1,1.5,2,3,4],[0,2,3,4],[0,1,1.5,2,3,4],[0,1,1.5,2.5,4],[0,1,1.5,2,4],[0,1,2,3,4],[0,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
F4:1 Ab4:.5 Bb4:1 C5:1.5
Eb5:1.5 Db5:.5 C5:2
Bb4:1 C5:.5 Eb5:.5 G5:2
F5:2 Eb5:1 Db5:1
Ab4+C5+Eb5+G5:4~
Ab4+C5+Eb5+G5:4~
Ab4+C5+Eb5+G5:4~
Ab4+C5+Eb5+G5:4~
Ab4+C5+Eb5+G5:4~
Ab4+C5+Eb5+G5:4
G5:1 F5:.5 Eb5:1.5 C5:1
Eb5:1.5 F5:.5 Ab5:2
G5:1 Gb5:.5 F5:.5 Eb5:2
D5:1 F5:.5 Ab5:1.5 G5:1
Eb5:2 D5:1 C5:1
Bb4:1 Db5:.5 E5:1.5 G5:1
F5:1 Ab5:.5 Bb5:1 C6:1.5
Ab5:1.5 G5:.5 F5:2
Eb5:1 D5:1 C5:1 Ab4:1
G4+Ab4+C5+D5:4
''',
 lh='''
F3:1 C4:.5 Eb4:.5 G3:2
Db3+Ab3:2 C4+F4:2
Eb3:1 Bb3:1 Db4:1 G3:1
C3:1 G3:1 Bb3:1 E4:1
F3:4
E3:4
Eb3:4
D3:4
Db3:4
C3:4
Ab2:1 Eb3:1 G3:1 C4:1
Db3:1.5 Ab3:.5 C4:2
E3+Bb3:2 Eb3+A3:2
D3:1 A3:1 C4:1 F3:1
G3+Bb3:2 F3+A3:2
C3:1 G3:1 Bb3:1 E4:1
F3:1 C4:.5 Eb4:1 Db4:1.5
Bb2:1 F3:1 Ab3:2
Db3:1 Ab3:1 C4:1 E3:1
F3+C4:4
''',
 lh_upper='''
R:4
R:4
R:4
R:4
Ab3:1 C4:.5 Eb4:1.5 C4:1
G#3:1.5 B3:.5 D#4:1 C4:1
G3:1 Bb3:1 C4:2
F3:1 Ab3:.5 C4:1.5 B3:1
F3:2 Ab3:1 C4:1
Eb3:1 G3:1 Bb3:.5 Ab3:1.5
R:4
R:4
R:4
R:4
R:4
R:4
R:4
R:4
R:4
R:4
''',sections={1:'p',2:'pp',3:'mp',4:'p',5:'pp',11:'p',12:'mp',13:'p',14:'mp',15:'p',16:'pp',17:'p',18:'pp',19:'pp',20:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,4),(11,14),(15,16),(17,20)],lower_phrases=[(1,2),(3,4),(11,12),(13,14),(15,16),(17,18),(19,20)],
 hairpins=[('crescendo',1,3),('diminuendo',4,5),('crescendo',11,12),('crescendo',13,14),('diminuendo',15,16),('diminuendo',17,20)],tempo_changes={},group=2,
 performance=dict(rubato=[54,48,56,46,49,47,50,46,48,42,53,57,51,55,47,43,49,43,35,27],
  phrase_arcs=[[0,15.8,3],[16,39.8,1],[40,55.8,3],[56,63.8,2],[64,80,-2]],
  tenor_entries=[[16,40]],lower_entries=[],pedal_lift=.18,gate=.995,
  note='Let the upper chord decay naturally through the chromatic bass descent; holding the keys preserves its resonance without creating new attacks. Shape the tenor in three long breaths above the changing bass. The return becomes more mobile and rises into a higher register, then settles softly into the added sixth and ninth.'))
,
dict(op=111,title='Chalcedony Landing',key='a',fifths=0,meter='12/8',bpm=54,
 description='Nacre Turnstile’s F–A-flat–B-flat–C becomes A–C–D–E. Three held upper notes leave room for increasingly long inner flourishes: five notes in two beats, seven in two, then nine in four. Each begins after a one-beat breath and crosses two slower LH notes. The surrounding melody rises into brighter registers before returning to a quiet A-minor ninth.',
 difficulty='Advanced inner-voice tuplets under held melody notes',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 4, 8 and 12, hold the upper E, G and F for the whole six-beat bar. After one quarter beat the RH inner voice enters: five equal eighths in the time of four, seven in four, then nine in eight. Each flourish crosses two equal LH notes; the final crossing lasts four beats rather than two. Keep the held melody present while allowing the ornament to move lightly beneath it. Two of the combined RH shapes reach an octave. The high middle phrases should retain the same soft touch as the opening.',
 parent_opus=110,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=6,pitches=['A','C','D','E']),
 ancestry=dict(source_opus=110,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4,source_pitches=['F','Ab','Bb','C'],transposition_semitones=4),
 hidden_voice_rests={'inner':[1,2,3,5,6,7,9,10,11,13,14,15,16]},
 tuplet_spans=[dict(hand='rh',voice='inner',start_beat=19,end_beat=21,actual=5,normal=4,stem='down',show_number='both',placement='below'),dict(hand='rh',voice='inner',start_beat=43,end_beat=45,actual=7,normal=4,stem='down',show_number='both',placement='below'),dict(hand='rh',voice='inner',start_beat=67,end_beat=71,actual=9,normal=8,stem='down',show_number='both',placement='below')],
 polyrhythms=[dict(start_beat=19,end_beat=21,rh_notes=5,lh_notes=2),dict(start_beat=43,end_beat=45,rh_notes=7,lh_notes=2),dict(start_beat=67,end_beat=71,rh_notes=9,lh_notes=2)],
 system_starts=[1,3,4,5,7,8,9,11,12,13,15],page_starts=[7,12],engraving=dict(spacing_system=12,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*6+left,(bar-1)*6+right-.18] for bar,cuts in enumerate([[0,1,1.5,2,2.5,3,4,6],[0,2,3,4,6],[0,1,1.5,2,3,4,6],[0,1,2,3,6],[0,1,1.5,2,3,6],[0,1,2,3,4,6],[0,1,1.5,2,4,6],[0,1,2,3,6],[0,1,1.5,2,3,4,6],[0,1,1.5,2,3,4,6],[0,1,1.5,2,3,4,6],[0,1,3,5,6],[0,1,1.5,2,3,4,6],[0,2,3,4,6],[0,1,1.5,2,3,4,6],[0,6]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
A4:1.5 C5:.5 D5:1 E5:3
G5:2 F5:1 E5:1 D5:2
C5:1.5 B4:.5 A4:2 G4:2
E5:3~ E5:3
F5:1.5 A5:.5 C6:1 B5:3
G5:2 E5:1 D5:1 C5:2
B4:1 D5:.5 F5:.5 A5:2 G5:2
G5:3~ G5:3
G#5:1 B5:.5 D6:.5 C6:2 B5:2
A5:1.5 G5:.5 F5:2 E5:2
D5:1.5 F5:.5 A5:1 G5:3
F5:3~ F5:3
E5:1.5 G5:.5 B5:1 A5:3
G5:2 F5:1 E5:1 D5:2
C5:1.5 B4:.5 A4:2 G4:2
G4+B4+C5+E5:3~ G4+B4+C5+E5:3
''',
 rh_inner='''
R:6
R:6
R:6
R:1 F4:2/5 G4:2/5 A4:2/5 C5:2/5 B4:2/5 R:3
R:6
R:6
R:6
R:1 D5:2/7 C5:2/7 A4:2/7 G4:2/7 A4:2/7 C5:2/7 E5:2/7 R:3
R:6
R:6
R:6
R:1 Bb4:4/9 A4:4/9 G4:4/9 F4:4/9 G4:4/9 A4:4/9 C5:4/9 D5:4/9 E5:4/9 R:1
R:6
R:6
R:6
R:6
''',
 lh='''
A2:1 E3:.5 G3:1 C4:1.5 B3:2
F3+A3:2 E3+G3:1 D3+F3:1 C4:2
D3:1 A3:.5 C4:1.5 F3:1 E3:2
F3:1 C4:1 E4:1 A3:3
D3:1 A3:1 C4:1 F3:3
G2:1 D3:1 F3:1 B3:1 E3:2
C3:1 G3:.5 Bb3:.5 E4:2 D4:2
C3:1 G3:1 B3:1 E3:3
E3:1 B3:1 D4:1 G#3:1 F3:2
A2:1 E3:1 G3:1 C4:1 B3:2
G3:1 D4:1 F4:1 Bb3:1 A3:2
Bb2:1 F3:2 A3:2 D4:1
A2:1 E3:.5 G3:.5 C4:1 B3:1 E3:2
F3+A3:2 E3+G3:1 D3+F3:1 C4:2
D3:1 A3:1 C4:1 G#3:1 B3:2
A3+E4:3~ A3+E4:3
''',sections={1:'p',2:'mp',3:'pp',4:'p',5:'mp',6:'p',7:'pp',8:'p',9:'mp',10:'p',11:'pp',12:'p',13:'p',14:'pp',15:'pp',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,3),(4,6),(7,10),(11,14),(15,16)],lower_phrases=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16)],
 hairpins=[('crescendo',1,2),('crescendo',3,5),('diminuendo',6,7),('crescendo',8,9),('diminuendo',10,11),('diminuendo',13,16)],tempo_changes={},group=2,
 performance=dict(rubato=[56,51,46,49,57,51,46,48,57,51,45,47,49,43,36,28],
  phrase_arcs=[[0,17.8,3],[18,35.8,3],[36,59.8,3],[60,83.8,3],[84,96,-2]],
  inner_entries=[[19,21],[43,45],[67,71]],lower_entries=[[90,96]],pedal_lift=.18,gate=.995,
  note='Treat the inner flourishes as measured freedom around the held melody. The last one has more time to unfold, rather than simply becoming faster. Let the high middle phrases carry some lightness, then draw back into the lower register and the open minor-ninth ending.'))
,
dict(op=112,title='Marl Sundial',key='d',fifths=-1,meter='6/4',bpm=54,
 description='Chalcedony Landing’s E–G–B–A becomes D–F–A–G. A lyrical opening leads to eight moving RH chords built from stacked fourths and a top octave, while a chromatic tenor line travels over a held D. Both moving parts later retrace their pitches in exact reverse order. The surrounding phrases rise into brighter jazz colours before the final D-minor ninth.',
 difficulty='Advanced quartal chord movement and paired retrograde',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The eight RH chords in bars 5–6 each contain two stacked perfect fourths and a top note one octave above the root. Their complete shapes span an octave and move in dotted-quarter steps. The LH holds D3 through both bars while its tenor moves independently above it. Bars 13–14 reverse the order of all eight chords and all eight tenor notes, retaining their original durations. Keep the top of each chord present and the middle pitches softer. The close contains an adjacent E–F inside the RH voicing.',
 parent_opus=111,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=6,pitches=['D','F','A','G']),
 ancestry=dict(source_opus=111,source_hand='rh',source_voice='upper',source_start_beat=72,source_end_beat=78,source_pitches=['E','G','B','A'],transposition_semitones=-2),
 lower_sections={1:'pp',5:'p',7:'pp',13:'p',15:'pp'},hidden_voice_rests={'tenor':[1,2,3,4,7,8,9,10,11,12,15,16]},
 voice_phrases=[dict(voice='tenor',start_beat=24,end_beat=36,swell=4),dict(voice='tenor',start_beat=72,end_beat=84,swell=3)],
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*6+left,(bar-1)*6+right-.18] for bar,cuts in enumerate([[0,1,1.5,2,3,6],[0,2,3,4,6],[0,1,1.5,2,3,6],[0,1,1.5,2,3,4,6],[0,1.5,3,4.5,6],[0,1.5,3,4.5,6],[0,2,3,4,6],[0,1,1.5,2,3,4,6],[0,1,1.5,2,3,6],[0,1,2,3,4,6],[0,1,1.5,2,3,6],[0,1,1.5,2,3,4,6],[0,1.5,3,4.5,6],[0,1.5,3,4.5,6],[0,2,3,4,6],[0,6]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
D5:1.5 F5:.5 A5:1 G5:3
E5:2 D5:1 C5:1 A4:2
Bb4:1.5 D5:.5 F5:1 E5:3
C5:1.5 A4:.5 G4:2 F4:2
D4+G4+C5+D5:1.5 E4+A4+D5+E5:1.5 F#4+B4+E5+F#5:1.5 G#4+C#5+F#5+G#5:1.5
G4+C5+F5+G5:1.5 F4+Bb4+Eb5+F5:1.5 E4+A4+D5+E5:1.5 D4+G4+C5+D5:1.5
F5:2 Eb5:1 D5:1 C5:2
Bb4:1.5 Db5:.5 E5:1 G5:3
F5:1.5 A5:.5 C6:1 B5:3
A5:2 G5:1 E5:1 D5:2
C5:1.5 E5:.5 G5:1 F#5:3
D5:1.5 F5:.5 A5:1 G5:3
D4+G4+C5+D5:1.5 E4+A4+D5+E5:1.5 F4+Bb4+Eb5+F5:1.5 G4+C5+F5+G5:1.5
G#4+C#5+F#5+G#5:1.5 F#4+B4+E5+F#5:1.5 E4+A4+D5+E5:1.5 D4+G4+C5+D5:1.5
F5:2 E5:1 D5:1 C5:2
E4+F4+A4+C5+D5:3~ E4+F4+A4+C5+D5:3
''',
 lh='''
D3:1 A3:1 C4:1 E3:3
Bb2+F3:2 A3+C4:2 G3:2
G3:1 D4:1 F4:1 A3:3
C3:1 G3:1 Bb3:1 E4:1 A3:2
D3:3~ D3:3~
D3:3~ D3:3
Eb3+Bb3:2 D3+A3:2 C4:2
C3:1 G3:1 Bb3:1 Db4:1 E3:2
F3:1 C4:1 E4:1 A3:3
D3:1 A3:1 C4:1 F3:1 E3:2
G3:1 D4:1 F4:1 B3:3
A2:1 E3:1 G3:1 C4:1 B3:2
D3:3~ D3:3~
D3:3~ D3:3
G3+Bb3:2 F3+A3:2 E3+G3:2
D3+A3:3~ D3+A3:3
''',
 lh_upper='''
R:6
R:6
R:6
R:6
F3:1.5 F#3:1.5 G3:1.5 Ab3:1.5
B3:1.5 Bb3:1.5 A3:1.5 G3:1.5
R:6
R:6
R:6
R:6
R:6
R:6
G3:1.5 A3:1.5 Bb3:1.5 B3:1.5
Ab3:1.5 G3:1.5 F#3:1.5 F3:1.5
R:6
R:6
''',sections={1:'p',2:'pp',3:'mp',4:'pp',5:'p',6:'p',7:'pp',8:'p',9:'mp',10:'p',11:'mp',12:'p',13:'p',14:'pp',15:'pp',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,4),(5,6),(7,8),(9,12),(13,14),(15,16)],lower_phrases=[(1,2),(3,4),(7,8),(9,10),(11,12),(15,16)],
 hairpins=[('crescendo',1,3),('crescendo',4,5),('crescendo',8,9),('crescendo',10,11),('diminuendo',12,14),('diminuendo',15,16)],tempo_changes={},group=2,
 performance=dict(rubato=[54,48,56,46,51,45,48,51,56,49,54,46,47,41,35,27],
  phrase_arcs=[[0,23.8,3],[24,35.8,3],[36,47.8,2],[48,71.8,3],[72,83.8,2],[84,96,-2]],
  tenor_entries=[[24,36],[72,84]],lower_entries=[],pedal_lift=.18,gate=.995,
  note='The moving fourths should feel broad and buoyant rather than percussive. Let the tenor retain its own line above the held D. When the passage returns in reverse, soften its arrival and let the motion gradually unwind into the close.'))
,
dict(op=113,title='Selenite Walkway',key='eb',fifths=-6,meter='5/4',bpm=52,
 description='Marl Sundial’s D–F–A–G becomes E-flat–G-flat–B-flat–A-flat in an unaccompanied lower phrase. The RH answers it two octaves higher. Three shared pauses then separate the later phrases: four quarter beats, two and a half, and one. The gaps draw closer together as the wandering jazz harmonies return to E-flat-minor ninth.',
 difficulty='Advanced harmonic listening with spacious, flexible phrasing',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The LH begins alone; bar 2 repeats its complete phrase two octaves higher in the RH. Keep the written silences between bars 6–7, 10–11 and 13–14 clear of the pedal. These gaps last four, two-and-a-half and one quarter beats respectively. The room resonance may linger, but the hands should make no new sound in those rests. Let the increasingly shorter breaths guide the return. This is a quieter contrast to the surrounding denser studies.',
 parent_opus=112,motif=dict(hand='lh',start_beat=0,end_beat=5,pitches=['Eb','Gb','Bb','Ab']),
 ancestry=dict(source_opus=112,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=6,source_pitches=['D','F','A','G'],transposition_semitones=1),
 system_starts=[1,3,5,7,9,11,13],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*5+left,(bar-1)*5+right-.18] for bar,cuts in enumerate([[0,1.5,2,3,5],[0,1,1.5,2,3,5],[0,2,3,4,5],[0,1,2.5,3,5],[0,1,1.5,2,3,5],[0,1,2,3],[2,3.5,4,5],[0,1,1.5,2,3,5],[0,1,1.5,2,3,5],[0,1,2,3,4],[1.5,2.5,3,5],[0,1,2,3,5],[0,1,1.5,2,2.5,4.5],[.5,5]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
R:5
Eb5:1.5 Gb5:.5 Bb5:1 Ab5:2
F5:2 Eb5:1 Db5:1 Bb4:1
R:1 Ab4:1.5 C5:.5 Eb5:2
D5:1 F5:.5 A5:1.5 G5:2
F5:1 Eb5:1 C5:1 R:2
R:2 D5:1.5 F5:.5 Ab5:1
G5:1.5 E5:.5 C5:1 B4:2
Bb4:1 Db5:.5 E5:1.5 G5:2
F5:2 Eb5:1 C5:1 R:1
R:1.5 Gb5:1 Bb5:.5 Ab5:2
F5:1 Eb5:1 Db5:1 Bb4:2
Gb4:1 Bb4:.5 Db5:1 C5:2 R:.5
R:.5 F4+Gb4+Bb4+Db5:1.5~ F4+Gb4+Bb4+Db5:3
''',
 lh='''
Eb3:1.5 Gb3:.5 Bb3:1 Ab3:2
R:1 Eb3+Bb3:2 Db4+F4:2
Gb3:2 Db4:1 F4:1 Eb4:1
Db3+Ab3:3 C4+F4:2
Bb2:1 F3:1 Ab3:1 C4:2
A3+C4:2 G3+Bb3:1 R:2
R:2 E3+Bb3:3
A2:1 E3:1 G3:1 C4:2
C3:1 G3:1 Bb3:1 Db4:2
F3:1 C4:1 Eb4:2 R:1
R:1.5 Eb3+Bb3:3.5
Gb3:1 Db4:1 F4:1 Ab3:2
F3+Ab3:2 Eb3+Gb3:2.5 R:.5
R:.5 Eb3+Bb3:1.5~ Eb3+Bb3:3
''',sections={1:'p',2:'p',3:'pp',4:'p',5:'mp',6:'pp',7:'pp',8:'p',9:'mp',10:'pp',11:'p',12:'pp',13:'pp',14:'pp'},words={1:'poco rubato',13:'poco rit.'},
 slurs=[(2,3),(4,6),(7,10),(11,12),(13,14)],lower_phrases=[(1,1),(2,3),(4,5),(8,9),(11,12)],
 hairpins=[('crescendo',2,3),('crescendo',4,5),('crescendo',7,9),('diminuendo',11,12)],tempo_changes={},group=2,
 performance=dict(rubato=[51,53,47,49,55,43,45,50,54,42,47,43,36,27],
  phrase_arcs=[[0,4.8,3],[5,14.8,3],[15,27.8,3],[32,48.8,3],[51.5,64.4,2],[65.5,70,-2]],
  lower_entries=[[0,5]],pedal_lift=.18,gate=.995,
  note='Give the solitary lower opening the same singing quality as its higher answer. The three written gaps are part of the form: let them hang without filling them, then make the next phrase feel like a continuation of the same thought. The final pause is short enough for the last chord to feel close and warm.'))
,
dict(op=114,title='Flint Atrium',key='c',fifths=-3,meter='4/4',bpm=54,
 description='Selenite Walkway’s F–E-flat–D-flat–B-flat becomes G–F–E-flat–C. A six-note descending subject receives an answer one beat later and a fifth lower, first in the RH inner voice, then in the LH bass beneath its tenor. A later D-minor reflection repeats both exchanges one whole tone higher. Chordal windows connect the canons before the C-minor ninth close.',
 difficulty='Advanced alternating canons within each hand',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 1–2 and 9–10 the RH inner voice answers the upper voice one quarter beat later and seven semitones lower. In bars 3–4 and 11–12 the LH bass answers its tenor by the same delay and interval. Keep each six-note phrase distinct through the overlap. Separate staff dynamics bring the LH exchanges forward while the RH holds quiet chords. The later pair of canons is two semitones above the first. Allow time for the lower hand to travel out of its deep register after each answer.',
 parent_opus=113,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['G','F','Eb','C']),
 ancestry=dict(source_opus=113,source_hand='rh',source_start_beat=55,source_end_beat=60,source_pitches=['F','Eb','Db','Bb'],transposition_semitones=2),
 lower_sections={1:'pp',3:'p',5:'pp',11:'p',13:'pp'},
 hidden_voice_rests={'inner':[3,4,5,6,7,8,11,12,13,14,15,16],'tenor':[1,2,5,6,7,8,9,10,13,14,15,16]},
 voice_phrases=[dict(voice='inner',start_beat=1,end_beat=7,swell=3),dict(voice='tenor',start_beat=8,end_beat=14,swell=3),dict(voice='inner',start_beat=33,end_beat=39,swell=3),dict(voice='tenor',start_beat=40,end_beat=46,swell=3)],
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=14,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.18] for bar,cuts in enumerate([[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,1.5,2,3,4],[0,1,1.5,2,2.5,3,4],[0,1,2,3,4],[0,1,1.5,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,1.5,2,3,4],[0,1,2,3,4],[0,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
G5:1 F5:1 Eb5:1 C5:1
Bb4:1 G4:1 R:2
Bb4+Eb5+G5:4
Ab4+C5+F5:4
Ab5:1 G5:.5 F5:.5 Eb5:2
D5:1 F5:.5 Ab5:1 G5:1.5
F5:1 Eb5:1 D5:1 C5:1
Bb4:1 D5:.5 F5:.5 Ab5:2
A5:1 G5:1 F5:1 D5:1
C5:1 A4:1 R:2
C5+F5+A5:4
Bb4+D5+G5:4
G5:1 F5:1 Eb5:1 D5:1
C5:1 Eb5:.5 F5:.5 G5:2
Bb4:1 Ab4:1 G4:1 F4:1
D4+Eb4+G4+Bb4:4
''',
 rh_inner='''
R:1 C5:1 Bb4:1 Ab4:1
F4:1 Eb4:1 C4:1 R:1
R:4
R:4
R:4
R:4
R:4
R:4
R:1 D5:1 C5:1 Bb4:1
G4:1 F4:1 D4:1 R:1
R:4
R:4
R:4
R:4
R:4
R:4
''',
 lh='''
C3:4
Ab2:4
R:1 C3:1 Bb2:1 Ab2:1
F2:1 Eb2:1 C2:1 R:1
Eb3:1 Bb3:1 D4:1 G3:1
G2:1 D3:1 F3:1 B3:1
Ab2:1 Eb3:1 G3:1 Bb3:1
A2:1 E3:1 G3:1 C#4:1
D3:4
Bb2:4
R:1 D3:1 C3:1 Bb2:1
G2:1 F2:1 D2:1 R:1
C3:1 G3:1 Bb3:1 Eb4:1
Ab3:1 Eb3:1 G3:1 Bb3:1
G2:1 D3:1 F3:1 B3:1
C3+G3:4
''',
 lh_upper='''
R:4
R:4
G3:1 F3:1 Eb3:1 C3:1
Bb2:1 G2:1 R:2
R:4
R:4
R:4
R:4
R:4
R:4
A3:1 G3:1 F3:1 D3:1
C3:1 A2:1 R:2
R:4
R:4
R:4
R:4
''',sections={1:'p',3:'pp',4:'pp',5:'p',6:'mp',7:'p',8:'pp',9:'p',11:'pp',12:'pp',13:'p',14:'pp',15:'pp',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,2),(3,4),(5,8),(9,10),(11,12),(13,16)],lower_phrases=[(3,4),(5,6),(7,8),(11,12),(13,14),(15,16)],
 hairpins=[('crescendo',5,6),('diminuendo',7,8),('diminuendo',13,16)],tempo_changes={},group=2,
 performance=dict(rubato=[54,48,52,45,55,58,51,46,54,47,50,44,47,42,35,27],
  phrase_arcs=[[0,7.8,3],[8,15.8,2],[16,31.8,3],[32,39.8,3],[40,47.8,2],[48,64,-2]],
  inner_entries=[[1,7],[33,39]],tenor_entries=[[8,14],[40,46]],lower_entries=[[9,15],[41,47]],pedal_lift=.18,gate=.995,
  note='Let each answer emerge as a second singing line, with the leading voice still audible. The left-hand exchanges should feel like the same music heard from a lower register, rather than a change of character. Keep the connecting chordal passages warm, and let the final return lose weight as it settles into the ninth.'))
,
dict(op=115,title='Basalt Driftway',key='f',fifths=-4,meter='4/4',bpm=54,
 description='Flint Atrium’s G–F–E-flat–C becomes C–B-flat–A-flat–F. Four appearances of the six-note descending phrase begin at successively later points in the bar: zero, half a beat, one beat and one-and-a-half beats. Its harmony moves through F minor, G minor and E-flat minor before returning. Ties let the melody float over the bar lines and the changing lower voicings.',
 difficulty='Advanced displaced phrase entries and cross-bar sustains',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The six-note phrase begins in bars 1, 5, 9 and 13, displaced by another half quarter beat on each appearance. Its durations remain 1.5, 0.5, 1, 2, 1 and 2 quarter beats. Observe the cross-bar ties, especially where an arrival continues into the next bar rather than beginning again. The second phrase is two semitones higher, the third two lower, and the fourth returns to the original pitches. Keep the quieter LH dyads separate from the melody’s changing points of arrival.',
 parent_opus=114,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['C','Bb','Ab','F']),
 ancestry=dict(source_opus=114,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4,source_pitches=['G','F','Eb','C'],transposition_semitones=5),
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.18] for bar,cuts in enumerate([[0,1.5,2,3,4],[0,1,2,4],[0,1,1.5,2,3,4],[0,1,1.5,2,4],[0,.5,1.5,2,2.5,3.5,4],[0,1.5,2,2.5,4],[0,.5,1,1.5,2,3,4],[0,1,2,2.5,3,4],[0,1,1.5,2.5,3,4],[0,2,3,4],[0,1,1.5,2,3,4],[0,1,1.5,2,3,4],[0,1.5,2,3,3.5,4],[0,.5,2,2.5,3.5,4],[0,1,1.5,2,2.5,3,4],[0,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
C6:1.5 Bb5:.5 Ab5:1 F5:1~
F5:1 Eb5:1 C5:2
Ab5:1 G5:.5 F5:.5 Eb5:2
D5:1 F5:.5 Ab5:.5 C6:2
R:.5 D6:1.5 C6:.5 Bb5:1 G5:.5~
G5:1.5 F5:1 D5:1.5~
D5:.5 R:.5 F5:1 A5:1 Ab5:1
G5:1 F5:1 Eb5:.5 Db5:.5 C5:1
R:1 Bb5:1.5 Ab5:.5 Gb5:1
Eb5:2 Db5:1 Bb4:1~
Bb4:1 R:.5 Db5:.5 F5:1 Ab5:1
G5:1 F5:.5 Eb5:.5 C5:1 Bb4:1
R:1.5 C6:1.5 Bb5:.5 Ab5:.5~
Ab5:.5 F5:2 Eb5:1 C5:.5~
C5:1.5 B4:.5 Ab4:1 G4:1
F4+G4+Ab4+C5+Eb5:4
''',
 lh='''
F3:1.5 C4:.5 Eb4:2
Db3+Ab3:2 G3+C4:2
Bb2:1 F3:.5 Ab3:1.5 C4:1
D3+Ab3:1.5 C4+F4:2.5
G3:1.5 D4:1 Bb3:1.5
Eb3+Bb3:2 A3+D4:2
C3:1 G3:.5 Bb3:1.5 E4:1
F3+A3:2 Eb3+G3:2
Eb3:1.5 Bb3:1 Db4:1.5
Cb3+Gb3:2 F3+Bb3:2
Ab2:1 Eb3:.5 Gb3:1.5 C4:1
Db3+Ab3:1.5 C4+E4:2.5
F3:1.5 C4:.5 Eb4:2
Db3+Ab3:2 G3+C4:2
Bb2:1 F3:.5 Ab3:1.5 B3:1
F3+C4:4
''',sections={1:'p',2:'pp',3:'mp',4:'p',5:'p',6:'pp',7:'mp',8:'p',9:'p',10:'pp',11:'mp',12:'p',13:'p',14:'pp',15:'pp',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,2),(3,4),(5,7),(8,8),(9,11),(12,12),(13,16)],lower_phrases=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16)],
 hairpins=[('crescendo',1,3),('diminuendo',4,6),('crescendo',7,8),('crescendo',9,11),('diminuendo',12,16)],tempo_changes={},group=2,
 performance=dict(rubato=[54,47,55,49,53,46,54,48,51,44,52,45,48,41,34,26],
  phrase_arcs=[[0,7.8,3],[8,15.8,3],[16.5,24.4,3],[25,32.8,2],[33,40.8,3],[41.5,49.3,2],[49.5,57.4,2],[57.5,64,-2]],
  lower_entries=[],pedal_lift=.18,gate=.995,
  note='Let the melody’s later entries feel like a phrase leaning gently across the pulse. Keep the long notes connected through their ties while the lower voicings change underneath. The last appearance should be the least insistent, opening into a soft ninth at the close.'))
,
dict(op=116,title='Chert Pavilion',key='g',fifths=-2,meter='4/4',bpm=53,
 description='Basalt Driftway’s C–B-flat–A-flat–F becomes D–C–B-flat–G. Twice the hands exchange registers: the RH sings a low version of the melody while the LH holds quiet chords high above it. The second crossing moves the material up a minor third. Written pauses prepare both exchanges, and rising RH lines bring the hands back together before the G-minor ninth close.',
 difficulty='Advanced crossed-hands melody with prepared register exchanges',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Both hands rest for one quarter beat before and after bars 7–8 and 15–16. In those passages, the RH is the upper written staff in bass clef (m.d.) and plays the low melody; the LH is the lower written staff in treble clef (m.s.) and holds the high chords at pp. The second crossed passage transposes both hands up three semitones. Normal clefs and labels return at bars 9 and 17. Use the full written pauses for the arm movements; the closest-note transition intervals reach seventeen semitones.',
 parent_opus=115,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','C','Bb','G']),
 ancestry=dict(source_opus=115,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['C','Bb','Ab','F'],transposition_semitones=2),
 hand_crossings=[dict(start_beat=24,end_beat=31,rest_before=1,rest_after=1),dict(start_beat=56,end_beat=63,rest_before=1,rest_after=1)],
 hand_labels={'rh':{7:'m.d.',9:'m.d.',15:'m.d.',17:'m.d.'},'lh':{7:'m.s.',9:'m.s.',15:'m.s.',17:'m.s.'}},
 clef_changes={'rh':{7:'bass',9:'treble',15:'bass',17:'treble'},'lh':{7:'treble',9:'bass',15:'treble',17:'bass'}},
 lower_sections={1:'pp',7:'pp',9:'pp',15:'pp',17:'pp'},
 system_starts=[1,3,5,7,9,11,13,15,17],page_starts=[11],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.2] for bar,cuts in enumerate([[0,1,1.5,3,4],[0,1,2,4],[0,1,1.5,2,3,4],[0,2,3,4],[0,1,1.5,2,3,4],[0,3],[0,1,1.5,3,4],[0,1,2,3],[0,1,2,3,4],[0,1,1.5,3,4],[0,2,3,4],[0,1,1.5,2,3,4],[0,1,2,3,4],[0,3],[0,1,1.5,3,4],[0,1,2,3],[0,1,2,3,4],[0,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
D5:1 C5:.5 Bb4:1.5 G4:1
F4:1 G4:1 Ab4:2
Bb4:1 D5:.5 F5:1.5 E5:1
D5:2 C5:1 Bb4:1
A4:1 C5:.5 Eb5:1.5 D5:1
G4+Bb4+D5:3 R:1
D3:1 C3:.5 Bb2:1.5 G2:1
F2:1 G2:1 Ab2:1 R:1
Bb3:1 D4:1 F4:1 A4:1
G4:1 Bb4:.5 D5:1.5 C5:1
Eb5:2 D5:1 C5:1
Bb4:1 Db5:.5 F5:1.5 Eb5:1
D5:1 C5:1 Bb4:1 Ab4:1
Bb4+Db5+F5:3 R:1
F3:1 Eb3:.5 Db3:1.5 Bb2:1
Ab2:1 Bb2:1 Cb3:1 R:1
C4:1 Eb4:1 G4:1 Bb4:1
A4+Bb4+D5+F5:4
''',
 lh='''
G2:1 D3:.5 F3:1.5 Bb3:1
Eb3+Bb3:2 D3+A3:2
C3:1 G3:1 Bb3:1 E4:1
F3+A3:2 Eb3+G3:2
D3:1 A3:1 C4:1 F#3:1
Eb3+Bb3:3 R:1
Bb4+D5+F5+A5:4
Ab4+C5+Eb5+G5:3 R:1
Eb3:1 Bb3:1 D4:1 G3:1
C3:1 G3:.5 Bb3:1.5 E4:1
Eb3+G3:2 D3+F#3:2
Bb2:1 F3:1 Ab3:1 C4:1
Db3:1 Ab3:1 C4:1 F3:1
Eb3+Bb3:3 R:1
Db5+F5+Ab5+C6:4
Cb5+Eb5+Gb5+Bb5:3 R:1
Gb3:1 Db4:1 F4:1 Bb3:1
G3+D4:4
''',sections={1:'p',2:'pp',3:'mp',4:'p',5:'p',6:'pp',7:'p',8:'p',9:'p',10:'mp',11:'p',12:'mp',13:'p',14:'pp',15:'p',16:'pp',17:'p',18:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,5),(7,8),(9,13),(15,16),(17,18)],lower_phrases=[(1,2),(3,4),(7,8),(9,10),(11,12),(15,16),(17,18)],
 hairpins=[('crescendo',1,3),('diminuendo',4,5),('crescendo',9,10),('diminuendo',11,13),('diminuendo',17,18)],tempo_changes={},group=2,
 performance=dict(rubato=[53,47,55,49,51,40,48,42,49,54,48,52,45,39,46,40,35,26],
  phrase_arcs=[[0,19.8,3],[24,31,2],[32,51.8,3],[56,63,2],[64,72,-2]],
  lower_entries=[],pedal_lift=.2,gate=.995,
  note='The crossed passages keep the melodic thread in the RH while changing its register completely. Let the high LH chords remain distant and soft. Take the whole written rest to reposition each hand, and let the rising returns recover the ordinary register without haste.'))

,
dict(op=117,title='Rutile Colonnade',key='f',fifths=-4,meter='6/4',bpm=54,
 description='Chert Pavilion’s D–C–B-flat–G becomes C–B-flat–A-flat–F. Nine-note, nine-beat phrases run across six-beat bars above slower changing harmony. A chordal passage and shared silence divide the piece; the later phrases reverse their pitch order while retaining the uneven rhythm. Their shifting accents gather into a quiet F-minor ninth.',
 difficulty='Advanced nine-beat melodic phrases over six-beat bars',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The first four phrases begin at beats 0, 9, 18 and 27; each lasts nine quarter beats with durations 1.5, 0.5, 1, 0.5, 1.5, 1, 0.5, 1 and 1.5. In bars 11–16 their pitches return in reverse order, keeping those durations; the first reversed phrase is an octave higher. Keep the lower harmony spacious as the melody crosses the bar. Both hands rest for three beats in bar 10. Let that silence separate the two directions of the melodic line.',
 parent_opus=116,motif=dict(hand='rh',start_beat=0,end_beat=3.5,pitches=['C','Bb','Ab','F']),
 ancestry=dict(source_opus=116,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','C','Bb','G'],transposition_semitones=-2),
 lower_sections={1:'pp',7:'p',10:'pp',11:'pp',17:'pp'},
 system_starts=[1,3,5,7,9,11,13,15,17],page_starts=[11],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*6+left,(bar-1)*6+right-.18] for bar,cuts in enumerate([[0,1.5,2,3,3.5,5,6],[0,.5,1.5,3,4,4.5,5,6],[0,.5,2,3,3.5,4.5,6],[0,1.5,2,3,3.5,5,6],[0,.5,1.5,3,4.5,5,6],[0,.5,2,3,3.5,4.5,6],[0,2,3,6],[0,1,1.5,2,3,4,6],[0,3,5,6],[0,3],[0,1.5,2,3,3.5,5,6],[0,.5,1.5,3,4,4.5,5,6],[0,.5,2,3,3.5,4.5,6],[0,1.5,2,3,3.5,5,6],[0,.5,1.5,3,4.5,5,6],[0,.5,2,3,3.5,4.5,6],[0,1,1.5,2,2.5,3,4,5,6],[0,6]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
C5:1.5 Bb4:.5 Ab4:1 F4:.5 G4:1.5 Ab4:1
C5:.5 Db5:1 Bb4:1.5 G5:1.5 F5:.5 Eb5:1
C5:.5 D5:1.5 Eb5:1 G5:.5 Ab5:1 F5:1.5
Eb5:1.5 Db5:.5 Cb5:1 Ab4:.5 Bb4:1.5 Cb5:1
Eb5:.5 Fb5:1 Db5:1.5 C5:1.5 Bb4:.5 Ab4:1
F4:.5 G4:1.5 Ab4:1 C5:.5 Db5:1 Bb4:1.5
Ab4+Db5:2 G4+C5:1 F4+Bb4:3
Eb4+Ab4:1 F4+Bb4:.5 G4+C5:1.5 Ab4+Db5:3
G4+B4+D5:3 F4+A4+C5:2 Eb4+G4+Bb4:1
E4+G4+Bb4+Db5:3 R:3
Bb5:1.5 Db6:.5 C6:1 Ab5:.5 G5:1.5 F5:1
Ab5:.5 Bb5:1 C6:1.5 F5:1.5 Ab5:.5 G5:1
Eb5:.5 D5:1.5 C5:1 Eb5:.5 F5:1 G5:1.5
Db5:1.5 Fb5:.5 Eb5:1 Cb5:.5 Bb4:1.5 Ab4:1
Cb5:.5 Db5:1 Eb5:1.5 Bb4:1.5 Db5:.5 C5:1
Ab4:.5 G4:1.5 F4:1 Ab4:.5 Bb4:1 C5:1.5
D5:1 F5:.5 Ab5:1 G5:.5 F5:1 Eb5:1 Db5:1
F4+G4+Ab4+C5+Eb5:6
''',
 lh='''
F2+C3:3 Eb3+Ab3:3
Db3+Ab3:4 C3+G3:2
C3+G3:3 Bb3+Eb4:3
Ab2+Eb3:2 Gb3+Cb4:4
Cb3+Gb3:3 Bb2+F3:3
F3+C4:3 Eb3+Ab3:3
Db3+Ab3:3 C3+G3:3
Bb2+F3:2 Ab3+Db4:2 G3+C4:2
E3+B3:3 D3+A3:3
C3+G3:3 R:3
Db3+Ab3:3 C3+G3:3
F3+C4:4 Eb3+Bb3:2
Ab2+Eb3:3 G3+C4:3
Cb3+Gb3:2 Bb2+F3:4
Ab2+Eb3:3 Db3+Ab3:3
Bb2+F3:3 Ab3+Db4:3
Bb2:1 F3:1 Ab3:1 D3:1 F3:1 B3:1
F3+C4:6
''',sections={1:'p',3:'mp',4:'p',6:'pp',7:'p',8:'mp',9:'p',10:'pp',11:'p',13:'mp',14:'p',16:'pp',17:'p',18:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,3),(4,6),(7,8),(9,10),(11,13),(14,16),(17,18)],lower_phrases=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16)],
 hairpins=[('crescendo',1,3),('diminuendo',4,6),('crescendo',7,8),('crescendo',11,13),('diminuendo',14,16),('diminuendo',17,18)],tempo_changes={},group=2,
 performance=dict(rubato=[54,51,55,50,48,45,49,52,47,39,51,49,53,47,44,41,35,27],
  phrase_arcs=[[0,9,3],[9,18,3],[18,27,3],[27,36,2],[36,48,3],[48,57,-2],[60,69,3],[69,78,3],[78,87,3],[87,96,2],[96,108,-2]],
  lower_entries=[],pedal_lift=.18,gate=.995,
  note='Shape each nine-beat melody as a single breath across the six-beat bars. Let the chordal middle grow warmer before its shared silence. The reversed phrases should have the same patient movement even as their contours turn upwards and the first rises into a higher register.'))
]
