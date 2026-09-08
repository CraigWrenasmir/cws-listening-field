PIECES = [
dict(op=169,title='Willow Belvedere',key='a',fifths=0,meter='3/4',bpm=54,
 description='A waltz heard from below: the lower hand sings while quiet upper chords arrive after the beat. Laurel Underpass’s G–A–B becomes C–D–E in the lower voice. Three five-bar phrases lift that melody into the middle register, pass through a brief minor shadow and settle into A minor with a ninth.',
 difficulty='Intermediate to advanced lower-hand melody and delayed upper chords',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Keep the LH melody in front of the RH chords. Most upper responses enter on beat 2; bars 6–7 enter an eighth earlier. The lower staff changes to treble clef for bars 6–12, then returns to bass in bar 13. Both hands breathe at bars 5 and 10.',
 parent_opus=163,motif=dict(hand='lh',start_beat=0,end_beat=3,pitches=['C','D','E']),ancestry=dict(source_opus=163,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['G','A','B'],transposition_semitones=5),
 clef_changes={'lh':{1:'bass',6:'treble',13:'bass'}},
 system_starts=[1,4,6,9,11,14],page_starts=[9],engraving=dict(spacing_system=14,pedal_offset_y=550),lower_sections={1:'p',6:'mp',9:'p',11:'p',14:'pp'},
 pedal_spans=[[i*3,i*3+(1.8 if i in [4,9] else 2.8)] for i in range(15)],
 rh='''
R:1 G4+B4+E5:2
R:1 F4+A4+D5:2
R:1 E4+G4+C5:2
R:1 F4+A4+D5:2
G4+B4+E5:2 R:1
R:.5 G4+C5+E5:1.5 A4+C5+F5:1
R:.5 A4+C5+F5:1.5 G4+B4+E5:1
R:1 G4+B4+E5:2
R:1 F4+Ab4+C5:2
E4+G4+C5:2 R:1
R:1 G4+B4+E5:2
R:1 A4+C5+E5:2
R:1 F4+A4+D5:2
R:1 E4+G4+B4:2
G4+B4+C5+E5:3
''',lh='''
A3+C4:1 D4:1 E4:1
G3+B3:1.5 D4:.5 C4:1
F3:1 A3:.5 C4:1 B3:.5
E3:1 G3:1 B3:1
A3:2 R:1
C4:1 D4:.5 E4:1.5
F4:2 E4:1
D4:1 F4:.5 E4:1.5
C4:1 Bb3:1 Ab3:1
G3:2 R:1
A3+C4:1 D4:1 E4:1
G4:1 F4:.5 E4:1.5
D4:1 C4:1 A3:1
G3:1 E3:1 G3:1
A2+E3:3
''',sections={1:'pp',6:'p',9:'pp'},words={1:'cantabile',14:'poco rit.'},slurs=[],lower_phrases=[(1,5),(6,10),(11,15)],hairpins=[],tempo_changes={},group=2,
 performance=dict(rubato=[54,55,54,52,45,56,57,54,50,43,54,55,50,41,28],phrase_arcs=[[0,15,4],[15,30,5],[30,45,3]],lower_entries=[[0,45]],pedal_lift=.2,gate=.985,note='Imagine the upper chords as a quiet room around the lower song. Let their delayed entries support its breath, and carry the melody naturally through the clef changes without changing its role.'))
,
dict(op=170,title='Camellia Threshold',key='F',fifths=-1,meter='12/8',bpm=66,
 description='A broad final dance in four rocking beats, returning to the folk set’s homecoming melody. Willow Homeward’s A–C–D–C is stretched across the opening bar above D minor. The middle rises into brighter jazz colours, then passes through a brief flat-key shadow. The tune returns over F major, and the closing steps finally come to rest.',
 difficulty='Advanced compound phrasing, changing registers and voiced jazz harmony',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Feel four dotted-quarter pulses in each 12/8 bar. Keep the long melody connected above the changing lower dyads. The LH uses treble clef in bars 5–6, returning to bass in bar 7. Shared dotted-quarter rests close bars 5 and 10; the final bar settles from a ninth-coloured C harmony into F major.',
 parent_opus=160,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['A','C','D','C']),ancestry=dict(source_opus=160,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','C','D','C'],transposition_semitones=0),
 clef_changes={'lh':{1:'bass',5:'treble',7:'bass'}},
 system_starts=[1,3,5,7,9,11,13],page_starts=[7],engraving=dict(spacing_system=14,pedal_offset_y=480),lower_sections={1:'pp',6:'p',11:'pp'},
 pedal_spans=[[i*6+a,i*6+b] for i in range(14) for a,b in [(0,2.8),(3,4.3 if i in [4,9] else 5.8)]],
 rh='''
A4:1 C5:.5 D5:1.5 C5:3
F5:3 E5:1.5 D5:1.5
C5:1 A4:.5 G4:1.5 A4:3
D5:3 E5:1.5 F5:1.5
E5:4.5 R:1.5
G5:1 E5:.5 D5:1.5 C5:3
B4:1 D5:.5 E5:1.5 D5:3
C5:1 A4:.5 G4:1.5 F4:3
Ab4:1 C5:.5 Eb5:1.5 Db5:3
C5:4.5 R:1.5
A4:1 C5:.5 D5:1.5 C5:3
F5:3 E5:1.5 D5:1.5
C5:1 A4:.5 G4:1.5 A4+C5:3
G4+B4+D5:3 F4+A4+C5:3
''',lh='''
D3:1.5 A3:1.5 F3+C4:1.5 A3+E4:1.5
Bb2:1.5 F3:1.5 D3+A3:1.5 F3+C4:1.5
F3:1.5 C4:1.5 A3+E4:1.5 G3+C4:1.5
G3:1.5 D4:1.5 Bb3+F4:1.5 A3+D4:1.5
A3:1.5 E4:1.5 C4+G4:1.5 R:1.5
C4:1.5 G4:1.5 E4+B4:1.5 D4+G4:1.5
G3:1.5 D4:1.5 B3+F4:1.5 A3+D4:1.5
F3:1.5 C4:1.5 A3+E4:1.5 G3+C4:1.5
Ab2:1.5 Eb3:1.5 Db3+Ab3:1.5 F3+C4:1.5
Ab2:1.5 Eb3:1.5 C3+G3:1.5 R:1.5
F3:1.5 C4:1.5 A3+E4:1.5 G3+C4:1.5
Bb2:1.5 F3:1.5 D3+A3:1.5 F3+C4:1.5
G3:1.5 D4:1.5 B3+F4:1.5 A3+E4:1.5
C3+G3:3 F3+C4:3
''',sections={1:'p',4:'mp',5:'pp',6:'mp',10:'pp',11:'p',13:'pp'},words={1:'cantabile',13:'poco rit.'},slurs=[(1,5),(6,10),(11,14)],lower_phrases=[],hairpins=[('crescendo',1,4),('diminuendo',6,9),('diminuendo',12,13)],tempo_changes={},group=2,
 performance=dict(rubato=[66,67,65,67,56,69,68,65,61,52,65,64,52,34],phrase_arcs=[[0,30,4],[30,60,5],[60,84,2]],lower_entries=[],pedal_lift=.2,gate=.985,note='Give the four rocking beats a long, breathing shape. The tune’s final return carries the memory of the opening minor harmony into a warmer setting; let the last two chords settle with tenderness.'))
]
