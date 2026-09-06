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
]
