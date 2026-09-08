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
]
