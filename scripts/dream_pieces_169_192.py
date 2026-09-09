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
,
dict(op=171,title='Salt Aperture',key='d',fifths=-1,meter='4/4',bpm=50,
 description='The tidal preludes begin with a tune inside a held upper light. Velvet Estuary’s lower D–F–E–A rises into the RH inner voice. Twelve bars gather in unequal breaths: D minor opens towards B-flat and G minor, a brief E-flat colour interrupts the return, and the final ninth remains suspended above D.',
 difficulty='Advanced inner-voice cantabile and sustained outer notes',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The inner line carries the opening motif while the fifth finger sustains A. Release each held outer note before changing position; simultaneous RH reach never exceeds an octave. Inner phrases continue independently of the sparse upper line. The shared rest in bar 8 clears the earlier resonance.',
 parent_opus=2,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=4,pitches=['D','F','E','A']),ancestry=dict(source_opus=2,source_hand='lh',source_start_beat=0,source_end_beat=3,source_pitches=['D','F','E','A'],transposition_semitones=0),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=16,pedal_offset_y=520),
 rh='''
A5:4
G5:3 F5:1
E5:4~
E5:2 D5:2
F5:3 G5:1
A5:4
G5:2 F5:2
Eb5:3 R:1
A5:4
G5:2 F5:2
E5:3 D5:1
E5:4
''',rh_inner='''
D5:1 F5:.5 E5:.5 A4:2
D5:1 C5:1 A4:2
G4:1 Bb4:1 A4:2
G4:2 F4:2
A4:1 C5:1 D5:2
F5:1 E5:1 D5:2
Eb5:1 D5:1 Bb4:2
G4:1 Bb4:2 R:1
D5:1 F5:.5 E5:.5 A4:2
C5:1 D5:1 A4:2
G4:1 A4:1 Bb4:1 A4:1
F4+A4:4
''',lh='''
D3+A3:3 R:1
Bb2+F3:2 A3:1 F3:1
G3+D4:3 R:1
A2+E3:2 G3+C#4:2
F3+C4:3 R:1
Bb2+F3:2 G3:2
Eb3+Bb3:4
C3+G3:3 R:1
D3+A3:3 R:1
Bb2+F3:2 G3+D4:2
A2+E3:2 G3+C#4:2
D3+A3:4
''',sections={1:'p',5:'mp',8:'pp',9:'p',11:'pp'},lower_sections={1:'pp',5:'p',8:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[(1,4),(5,8),(9,12)],lower_phrases=[],voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=s) for a,b,s in [(0,16,4),(16,31,5),(32,48,3)]],
 hairpins=[('crescendo',5,6),('diminuendo',7,8)],tempo_changes={},group=2,
 pedal_spans=[[i*4,i*4+(2.8 if i==7 else 3.8)] for i in range(12)],
 performance=dict(rubato=[50,51,49,43,51,54,49,41,50,48,40,28],phrase_arcs=[[0,16,2],[16,31,3],[32,48,-1]],lower_entries=[],inner_entries=[[0,48]],pedal_lift=.2,gate=.995,note='Bring the moving middle voice gently forward beneath the sustained upper notes; the final ninth should fade without a new accent.'))
,
dict(op=172,title='Reed Undertow',key='g',fifths=-2,meter='4/4',bpm=56,
 description='Three slow upper notes cross two lower pulses, then drift into a long suspended landing. Salt Aperture’s inner D–F–E–A becomes G–B-flat–A–D. Triplet currents alternate with ordinary quarters and a completely still bar, opening through B-flat and E-flat before returning to G minor.',
 difficulty='Advanced gentle three-against-two and connected arpeggios',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The opening three quarter-note triplets occupy two ordinary quarter beats, against two LH quarter notes. Let the triplet land on the held D without accent. Bars 1, 3, 6, 9 and 11 use this crossing; the unhurried duple phrases between them keep it from becoming an exercise.',
 parent_opus=171,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['G','Bb','A','D']),ancestry=dict(source_opus=171,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=5),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=14,pedal_offset_y=470),
 rh='''
G4:2/3 Bb4:2/3 A4:2/3 D5:2
F5:1 E5:.5 D5:1.5 C5:1
Bb4:2/3 D5:2/3 F5:2/3 A5:2
G5:2 F5:1 D5:1
Eb5:3 D5:1
C5:2/3 Eb5:2/3 G5:2/3 F5:2
D5:2 C5:1 A4:1
Bb4+D5:3 R:1
G4:2/3 Bb4:2/3 A4:2/3 D5:2
F5:1 Eb5:1 D5:2~
D5:2/3 C5:2/3 A4:2/3 F#4:2
A4+Bb4+D5:4
''',lh='''
G3:1 D4:1 Bb3:2
F3:1 C4:1 A3:1 C4:1
Bb2:1 F3:1 D3:2
Eb3:1 Bb3:1 G3:2
C3+G3:2 Bb3:2
Ab2:1 Eb3:1 C4:2
D3+A3:2 F#3+C4:2
G3+D4:3 R:1
G3:1 D4:1 Bb3:2
Eb3:1 Bb3:1 G3:2
D3:1 A3:1 C4:2
G3+D4:4
''',sections={1:'p',5:'mp',8:'pp',9:'p',11:'pp'},lower_sections={1:'pp',5:'p',8:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[(1,3),(4,8),(9,12)],lower_phrases=[],hairpins=[('crescendo',5,6),('diminuendo',7,8)],tempo_changes={},group=2,
 pedal_spans=[[i*4,i*4+(2.8 if i==7 else 3.8)] for i in range(12)],
 performance=dict(rubato=[56,57,60,53,55,59,52,44,55,52,43,30],phrase_arcs=[[0,12,3],[12,31,4],[32,48,2]],lower_entries=[],pedal_lift=.2,gate=.99,note='The triplet currents stay rounded and quiet. Broaden the held arrivals and allow the eighth-bar silence to empty the pedal.'))
,
dict(op=173,title='Glass Inlet',key='C',fifths=0,meter='5/4',bpm=48,
 description='A narrow melody moves inside softly changing chords while their highest note stays still. Elder Horizon’s F–G–F becomes G–A–G in the inner voice. The five-beat spans turn from C major towards A minor, then an F-minor reflection; the final upper D preserves a little distance above the settled tonic.',
 difficulty='Advanced chord voicing under a sustained common tone',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The RH inner voice is written as changing dyads beneath the sustained outer note. Voice the top of each dyad; do not reattack tied outer notes. Combined RH shapes stay within an octave. The third and seventh bars shorten their texture with a shared final-beat rest.',
 parent_opus=144,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=5,pitches=['G','A','G']),ancestry=dict(source_opus=144,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['F','G','F'],transposition_semitones=2),
 system_starts=[1,3,5,7,9],page_starts=[7],engraving=dict(spacing_system=16,pedal_offset_y=490),
 rh='''
C5:5~
C5:3 B4:2
C5:4 R:1
E5:5
D5:3 C5:2
C5:5
Db5:4 R:1
C5:5
B4:3 D5:2
D5:5
''',rh_inner='''
E4+G4:2 F4+A4:1 E4+G4:2
D4+F4:3 D4+G4:2
E4+A4:2 E4+G4:2 R:1
G4+B4:2 A4+C5:3
F4+A4:3 E4+G4:2
Eb4+Ab4:2 F4+Ab4:3
F4+Bb4:2 Eb4+Ab4:2 R:1
E4+G4:2 F4+A4:1 E4+G4:2
D4+G4:3 F4+A4:2
E4+G4:5
''',lh='''
C3+G3:5
D3+A3:3 G2+D3:2
A2+E3:4 R:1
C3+G3:2 F3+C4:3
Bb2+F3:3 A2+E3:2
F3+C4:5
Bb2+F3:2 Eb3+Bb3:2 R:1
C3+G3:5
G2+D3:3 B2+F3:2
C3+G3:5
''',sections={1:'p',4:'mp',6:'p',9:'pp'},lower_sections={1:'pp',4:'p',6:'pp'},words={1:'sostenuto',9:'poco rit.'},slurs=[(1,3),(4,7),(8,10)],lower_phrases=[],voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=s) for a,b,s in [(0,14,3),(15,34,4),(35,50,2)]],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*5+a,i*5+b-.2] for i,cuts in enumerate([[0,2,3,5],[0,3,5],[0,2,4],[0,2,5],[0,3,5],[0,2,5],[0,2,4],[0,2,3,5],[0,3,5],[0,5]]) for a,b in zip(cuts,cuts[1:])],
 performance=dict(rubato=[48,47,40,50,48,44,38,46,38,26],phrase_arcs=[[0,14,2],[15,34,3],[35,50,-1]],lower_entries=[],inner_entries=[[0,50]],pedal_lift=.2,gate=.995,note='The moving dyads carry the expression; the held upper notes form a quiet ceiling. Clear the pedal at each written harmonic change while preserving ties with the fingers.'))
,
dict(op=174,title='Sedge Soundings',key='c',fifths=-3,meter='3/4',meters=['3/4','4/4','3/4','2/4','4/4','3/4','4/4','2/4','3/4','4/4','3/4','2/4','4/4'],bpm=52,
 description='The tide is heard from the floor of the harmony. Heather Soundings’s E–D–E becomes G–F–G in a separate LH tenor above sustained bass notes. Changing two-, three- and four-beat bars follow the melody’s breath; a quiet E-flat-major middle slips back into C minor, ending on an open ninth.',
 difficulty='Advanced lower-hand polyphony and changing phrase lengths',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Hold the written bass beneath the tenor melody, keeping the full lower hand within an octave. There is no need to accent the changing metres. Both hands rest in bars 4 and 8; the tenor phrases are separately slurred and brought forward in the performance.',
 parent_opus=151,motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=3,pitches=['G','F','G']),ancestry=dict(source_opus=151,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['E','D','E'],transposition_semitones=3),
 system_starts=[1,3,5,7,9,11,13],page_starts=[7],engraving=dict(spacing_system=16,pedal_offset_y=570),
 rh='''
C5+Eb5:3
Bb4+Eb5:4
A4+D5:3
G4+C5:1 R:1
G4+Bb4:4
Ab4+C5:3
G4+B4:2 F4+Ab4:2
Eb4+G4:1 R:1
C5+Eb5:3
Bb4+D5:2 A4+C5:2
G4+B4:3
F4+Ab4:2
G4+D5:4
''',lh='''
C3:3
Ab2:4
F3:3
C3:1 R:1
Eb3:4
F3:3
G3:4
C3:1 R:1
C3:3
F3:4
G3:3
G3:2
C3:4
''',lh_upper='''
G3:1 F3:1 G3:1
Ab3:2 G3:1 Eb3:1
C4:1 Bb3:1 A3:1
G3:1 R:1
Bb3:1 C4:1 D4:2
C4:1 Ab3:2
D4:2 Db4:1 B3:1
G3:1 R:1
G3:1 F3:1 G3:1
A3:1 C4:1 Bb3:2
D4:1 Eb4:1 D4:1
C4:1 B3:1
Eb3:4
''',sections={1:'pp',5:'p',8:'pp'},lower_sections={1:'p',5:'mp',8:'pp',9:'p',11:'pp'},words={1:'cantabile',12:'poco rit.'},slurs=[],lower_phrases=[],voice_phrases=[dict(voice='tenor',start_beat=a,end_beat=b,swell=s) for a,b,s in [(0,11,3),(12,24,4),(25,41,2)]],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[a,b-.2] for a,b in [(0,3),(3,7),(7,10),(10,11),(12,16),(16,19),(19,21),(21,23),(23,24),(25,28),(28,30),(30,32),(32,35),(35,37),(37,41)]],
 performance=dict(rubato=[52,51,48,39,54,53,49,40,51,52,47,38,27],phrase_arcs=[[0,11,1],[12,24,2],[25,41,1]],lower_entries=[[0,41]],tenor_entries=[[0,41]],pedal_lift=.2,gate=.995,note='Sing from the lower staff. The upper dyads remain very soft; the short two-beat bars feel like the end of a breath rather than a new step.'))
,
dict(op=175,title='Pearl Backwater',key='c',fifths=-3,meter='6/4',bpm=54,
 description='An entirely chordal prelude, with a broad, chromatically descending middle. Bracken Lowlight’s B–A–B becomes E-flat–D-flat–E-flat. The opening C-minor field briefly slips onto D-flat; the centre descends through B, B-flat, A and A-flat bass colours before a G-dominant breath leads home.',
 difficulty='Advanced quiet chordal legato and chromatic harmonic balance',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Every attack contains at least three pitches in its hand. Keep the inner chord tones soft and connect common tones where possible. The bass roots of bars 4–8 descend B–B-flat–A–A-flat–G. The faster chord changes remain whole quarter beats or longer; both hands release together at the ends of bars 3 and 8.',
 parent_opus=159,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Eb','Db','Eb']),ancestry=dict(source_opus=159,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['B','A','B'],transposition_semitones=4),
 system_starts=[1,3,5,7,9],page_starts=[7],engraving=dict(spacing_system=16,pedal_offset_y=480),
 rh='''
F4+Bb4+Eb5:2 Eb4+Ab4+Db5:2 F4+Bb4+Eb5:2
Eb4+G4+D5:3 D4+F4+C5:3
Eb4+G4+Bb4:4 R:2
F#4+A4+D5:3 E4+G4+C5:3
F4+A4+C5:2 Eb4+G4+Bb4:1 D4+F4+A4:3
E4+G4+B4:3 D4+F#4+A4:3
Eb4+G4+Bb4:2 Db4+F4+Ab4:2 C4+Eb4+G4:2
D4+F4+A4:4 R:2
F4+Bb4+Eb5:2 Eb4+Ab4+Db5:2 Eb4+G4+C5:2
F4+Ab4+C5:3 D4+F4+B4:3
Eb4+G4+Bb4+D5:6
''',lh='''
C3+G3+Bb3:2 Db3+F3+Ab3:2 C3+G3+Bb3:2
Eb3+G3+Bb3:3 F3+A3+C4:3
Ab2+Eb3+G3:4 R:2
B2+F#3+A3:3 B2+E3+G3:3
Bb2+F3+A3:3 Bb2+D3+F3:3
A2+E3+G3:3 A2+D3+F#3:3
Ab2+Eb3+G3:2 Ab2+Db3+F3:2 Ab2+C3+Eb3:2
G2+D3+F3:4 R:2
C3+G3+Bb3:2 Db3+F3+Ab3:2 C3+G3+Bb3:2
F3+Ab3+C4:3 G2+D3+F3:3
C3+Eb3+G3:6
''',sections={1:'p',4:'mp',7:'p',9:'p',10:'pp'},lower_sections={1:'pp',4:'p',8:'pp'},words={1:'sostenuto',10:'poco rit.'},slurs=[(1,3),(4,8),(9,11)],lower_phrases=[],hairpins=[('crescendo',4,6),('diminuendo',7,8)],tempo_changes={},group=2,
 pedal_spans=[[i*6+a,i*6+b-.2] for i,cuts in enumerate([[0,2,4,6],[0,3,6],[0,4],[0,3,6],[0,2,3,6],[0,3,6],[0,2,4,6],[0,4],[0,2,4,6],[0,3,6],[0,6]]) for a,b in zip(cuts,cuts[1:])],
 performance=dict(rubato=[54,53,44,55,56,57,52,42,52,43,28],phrase_arcs=[[0,16,2],[18,46,4],[48,66,1]],lower_entries=[],pedal_lift=.2,gate=.995,note='Each chord should open gently from the same quiet touch. Let the chromatic bass descent carry the middle phrase, and release the rests completely before the return.'))
,
dict(op=176,title='Willow Littoral',key='e',fifths=1,meter='6/8',bpm=72,
 description='A running shoreline melody changes hands halfway through its journey. Camellia Threshold’s A–C–D–C becomes E–G–A–G. Five opening bars flow into a six-bar lower-hand reply; the seven-bar return grows warmer as G major and C major replace the opening E-minor shadow.',
 difficulty='Advanced melody transfer, compound flow and register changes',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The LH takes the tune in bars 6–11 while the RH supplies held dyads. The lower staff changes to treble clef for those six bars and returns to bass at bar 12. Keep the two hands in their written registers; no crossing is required. The phrase-end rests should remain audible.',
 parent_opus=170,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['E','G','A','G']),ancestry=dict(source_opus=170,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['A','C','D','C'],transposition_semitones=7),
 clef_changes={'lh':{1:'bass',6:'treble',12:'bass'}},system_starts=[1,4,6,9,12,15,17],page_starts=[9],engraving=dict(spacing_system=15,pedal_offset_y=480),
 rh='''
E5:.5 G5:.5 A5:1 G5:1
F#5:.5 E5:.5 D5:1 B4:1
E5:1 F#5:.5 G5:.5 B5:1
A5:1 G5:.5 E5:.5 D5:1
E5:2 R:1
B4+E5:3
A4+D5:3
C5+E5:3
B4+D5:3
A4+C5:3
G4+B4:2 R:1
E5:.5 G5:.5 A5:1 G5:1
B5:1 A5:.5 G5:.5 E5:1
F#5:1 E5:.5 D5:.5 B4:1
C5:1 E5:.5 G5:.5 A5:1
G5:1 E5:1 D5:1
F#5:1 E5:.5 D5:.5 B4:1
A4+B4+D5:3
''',lh='''
E3:.5 B3:.5 G3:1 B3:1
D3:1 A3:.5 F#3:.5 A3:1
C3:.5 G3:.5 B3:1 G3:1
A2:1 E3:.5 G3:.5 B3:1
E3+B3:2 R:1
E4:.5 G4:.5 A4:1 G4:1
G4:.5 F#4:.5 E4:1 B3:1
D4:.5 F#4:.5 A4:1 G4:1
F#4:1 A4:.5 G4:.5 D4:1
C4:.5 E4:.5 G4:1 F#4:1
B3:.5 D4:.5 F#4:1 R:1
E3:.5 B3:.5 G3:1 B3:1
C3:1 G3:.5 E3:.5 G3:1
D3:.5 A3:.5 F#3:1 A3:1
C3:1 G3:.5 A3:.5 C4:1
A2:1 E3:1 G3:1
D3:1 A3:.5 C4:.5 A3:1
G3+B3:3
''',sections={1:'p',6:'pp',12:'p',13:'mp',16:'p',17:'pp'},lower_sections={1:'pp',6:'p',9:'mp',11:'pp',12:'pp'},words={1:'dolce',17:'poco rit.'},slurs=[(1,5),(12,18)],lower_phrases=[(6,11)],hairpins=[('crescendo',12,14),('diminuendo',15,17)],tempo_changes={},group=3,
 pedal_spans=[[i*3,i*3+(1.8 if i in [4,10] else 2.8)] for i in range(18)],
 performance=dict(rubato=[72,74,77,72,60,71,72,75,73,69,59,73,78,75,72,66,53,35],phrase_arcs=[[0,14,3],[15,32,4],[33,54,4]],lower_entries=[[15,32]],pedal_lift=.2,gate=.985,note='The melody keeps the same light singing touch when it moves to the lower hand. The upper replies grow almost transparent; the return gradually gathers warmth before settling into G major with sixth and ninth colours.'))
,
dict(op=177,title='Lichen Floodplain',key='d',fifths=-1,meter='4/4',bpm=54,
 description='Four voices widen into the fullest tide of the set. Glass Inlet’s inner G–A–G becomes D–E–D. The two middle voices rise separately beneath long outer notes, reaching a high B-flat-major light before withdrawing through E-flat and A dominant to the opening D-minor shore.',
 difficulty='Advanced four-voice balance and independent inner phrasing',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Both hands contain separately notated voices. Keep the sustained upper and bass notes quieter than the moving inner lines. The LH moves to treble clef for bars 6–8 and returns to bass at bar 9. The full hand spans stay within an octave; the high climax asks for balance rather than force.',
 parent_opus=173,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=4,pitches=['D','E','D']),ancestry=dict(source_opus=173,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=5,source_pitches=['G','A','G'],transposition_semitones=-5),
 clef_changes={'lh':{1:'bass',6:'treble',9:'bass'}},system_starts=[1,3,5,7,9,11,13],page_starts=[7],engraving=dict(spacing_system=18,spacing_staff=22,pedal_offset_y=600),
 rh='''
A5:4
G5:3 F5:1
E5:4
G5:3 R:1
A5:4
C6:4
Bb5:4
D6:3 R:1
C6:4
Bb5:2 A5:2
A5:4
G5:3 F5:1
E5:2 D5:2
E5:4
''',rh_inner='''
D5:1 E5:1 D5:2
C5:1 Bb4:1 A4:2
G4:1 A4:1 Bb4:2
C5:1 Bb4:1 A4:1 R:1
C5:1 D5:1 F5:2
Eb5:1 G5:1 Ab5:2
D5:1 F5:1 Eb5:1 D5:1
G5:1 A5:1 F5:1 R:1
Eb5:1 G5:1 Bb5:2
D5:1 F5:1 E5:2
D5:1 E5:1 D5:2
C5:1 Bb4:1 A4:2
G4:1 A4:1 F4:2
F4+A4:4
''',lh='''
D3:4
Bb2:4
G3:4
A3:3 R:1
F3:4
Ab3:4
G3:4
Bb3:3 R:1
Eb3:4
A3:4
D3:4
Bb2:4
A2:4
D3:4
''',lh_upper='''
F3:2 A3:2
D3:1 F3:1 A3:2
Bb3:2 D4:2
C4:1 E4:2 R:1
A3:1 C4:1 E4:2
C4:2 Eb4:2
Bb3:1 D4:1 F4:2
D4:1 F4:2 R:1
G3:2 Bb3:2
C#4:1 E4:1 G4:2
F3:2 A3:2
D3:1 F3:1 G3:2
E3:2 G3:2
A3:4
''',sections={1:'p',5:'mp',8:'mf',9:'mp',11:'p',13:'pp'},lower_sections={1:'p',5:'mp',9:'p',13:'pp'},words={1:'cantabile',13:'poco rit.'},slurs=[(1,4),(5,8),(9,14)],lower_phrases=[],voice_phrases=[dict(voice=v,start_beat=a,end_beat=b,swell=s) for v,spans in [('inner',[(0,15,3),(16,31,5),(32,56,2)]),('tenor',[(0,8,3),(8,15,4),(16,24,4),(24,31,5),(32,40,3),(40,56,2)])] for a,b,s in spans],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*4,i*4+(2.8 if i in [3,7] else 3.8)] for i in range(14)],
 performance=dict(rubato=[54,55,53,44,57,59,61,49,55,52,53,49,40,27],phrase_arcs=[[0,15,2],[16,31,4],[32,56,1]],lower_entries=[],inner_entries=[[0,56]],tenor_entries=[[0,56]],pedal_lift=.2,gate=.995,note='Let the two middle voices gather independently. The single mezzo-forte arrival is spacious, not percussive; after it, allow the texture to retreat into the last unresolved ninth.'))
,
dict(op=178,title='Mallow Slackwater',key='Bb',fifths=-2,meter='7/4',bpm=46,
 description='A sparse pause after the floodplain: widely separated dyads arrive after a low three-note question. Sedge Soundings’s tenor G–F–G becomes F–E-flat–F. Seven-beat bars contain uneven islands of sound and silence, with a borrowed B-flat-minor shadow before a soft major sixth-and-ninth ending.',
 difficulty='Intermediate to advanced resonance, long rests and quiet timing',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The lower hand asks the opening question before the upper dyad enters. Preserve the written silence in bars 3 and 6, clearing the pedal at the indicated release. There are no rapid gestures; the difficulty is sustaining a phrase across its gaps without rushing the next entry.',
 parent_opus=174,motif=dict(hand='lh',start_beat=0,end_beat=7,pitches=['F','Eb','F']),ancestry=dict(source_opus=174,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=3,source_pitches=['G','F','G'],transposition_semitones=-2),
 system_starts=[1,3,5,7],page_starts=[5],engraving=dict(spacing_system=17,pedal_offset_y=460),
 rh='''
R:1 D5+G5:6
Eb5+G5:4 D5+F5:3
C5+Eb5:4 R:3
R:2 Db5+F5:3 C5+Eb5:2
Bb4+D5:3 A4+C5:4
G4+Bb4:5 R:2
R:1 A4+C5:3 G4+Bb4:3
C4+D4+F4:7
''',lh='''
F3:2 Eb3:2 F3:3
C3+G3:4 Bb2+F3:3
Eb3+Bb3:4 R:3
Bb2+F3:2 Db3+Ab3:3 Eb3+Bb3:2
G2+D3:3 F3+C4:4
C3+G3:3 Eb3:2 R:2
F3+C4:4 Eb3+A3:3
Bb2+F3+G3:7
''',sections={1:'pp',4:'p',6:'pp'},lower_sections={1:'p',2:'pp',4:'p',6:'pp'},words={1:'lento',7:'poco rit.'},slurs=[(1,3),(4,6),(7,8)],lower_phrases=[(1,3)],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[0,1.8],[2,3.8],[4,6.8],[7,10.8],[11,13.8],[14,17.8],[21,22.8],[23,25.8],[26,27.8],[28,30.8],[31,34.8],[35,39.8],[42,45.8],[46,48.8],[49,55.8]],
 performance=dict(rubato=[46,45,35,44,46,34,40,27],phrase_arcs=[[0,18,1],[21,40,2],[42,56,-1]],lower_entries=[[0,7]],pedal_lift=.2,gate=.995,note='Allow the room to empty in the long rests. The upper chords can arrive almost as an afterthought; the final major colour should feel discovered rather than announced.'))
,
dict(op=179,title='Iris Countertide',key='a',fifths=0,meter='5/4',bpm=58,
 description='The earlier cross-current returns underneath the chords. Reed Undertow’s G–B-flat–A–D becomes A–C–B–E in the left hand. Lower quarter-note triplets move against two even upper attacks, then both hands float into a three-beat arrival. A brief B-flat and G-major middle widens the A-minor landscape.',
 difficulty='Advanced left-hand three-against-two and changing chord response',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The lower three-note triplets fill the first two quarter beats; upper attacks at beats 1 and 2 form the duple counter-rhythm. Keep the third triplet from becoming a pickup accent. The LH changes to treble clef in bars 5–7, returning to bass at bar 8. The upper line becomes a melody briefly in bars 6–7.',
 parent_opus=172,motif=dict(hand='lh',start_beat=0,end_beat=5,pitches=['A','C','B','E']),ancestry=dict(source_opus=172,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['G','Bb','A','D'],transposition_semitones=2),
 clef_changes={'lh':{1:'bass',5:'treble',8:'bass'}},system_starts=[1,3,5,7,9],page_starts=[7],engraving=dict(spacing_system=16,pedal_offset_y=480),
 rh='''
G4+B4:1 A4+C5:1 B4+E5:3
F4+A4:2 G4+B4:3
R:1 G4+C5:2 A4+D5:2
F4+Ab4+C5:4 R:1
G4+B4:1 A4+C5:1 B4+E5:3
G5:1 F5:1 D5:3
E5:1 D5:1 C5:3
B4+E5:2 A4+D5:3
A4+C5:1 B4+D5:1 C5+E5:3
D5:1 C5:1 G4+B4:3
G4+B4+C5+E5:5
''',lh='''
A3:2/3 C4:2/3 B3:2/3 E4:3
D3:1 A3:1 F3:1 C4:2
F3:1 C4:1 A3:3
Db3:1 Ab3:1 F3:2 R:1
A3:2/3 C4:2/3 B3:2/3 E4:3
Bb3:2/3 D4:2/3 C4:2/3 F4:3
G3:2/3 B3:2/3 D4:2/3 C4:3
E3:1 B3:1 G#3:1 D4:2
A3:2/3 C4:2/3 B3:2/3 E4:3
F3:2/3 A3:2/3 C4:2/3 B3:3
A2+E3:5
''',sections={1:'p',5:'mp',8:'p',10:'pp'},lower_sections={1:'p',4:'pp',5:'mp',8:'p',10:'pp'},words={1:'dolce',10:'poco rit.'},slurs=[(1,4),(5,8),(9,11)],lower_phrases=[(1,4),(5,7),(8,11)],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*5,i*5+(3.8 if i==3 else 4.8)] for i in range(11)],
 performance=dict(rubato=[58,57,59,48,59,62,60,54,57,46,29],phrase_arcs=[[0,19,3],[20,40,4],[40,55,1]],lower_entries=[[0,55]],pedal_lift=.2,gate=.99,note='The left hand is the current and the upper hand its reflection. Keep the two layers equally rounded; the long third-beat arrivals make room for the harmony to resonate.'))
,
dict(op=180,title='Fern Tideline',key='F',fifths=-1,meter='4/4',bpm=58,
 description='The set returns to its opening shore with the melody now in the light. Salt Aperture’s inner D–F–E–A moves into the upper voice, passes to the LH and finally becomes the top of a chordal reprise. A brief A-flat and D-flat reflection gives way to F major, where the last sixth-and-ninth chord remains open.',
 difficulty='Advanced arpeggio flow, melody transfer and chordal reprise',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The opening tune returns one octave lower in the LH at bar 6. At bar 11 the same pitch classes form the tops of four RH chords. Keep the faster chord changes close to the keys, with their lower tones soft. The LH treble clef in bars 6–7 avoids ledger lines; both phrase-end rests release the pedal.',
 parent_opus=171,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','F','E','A']),ancestry=dict(source_opus=171,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),
 clef_changes={'lh':{1:'bass',6:'treble',8:'bass'}},system_starts=[1,3,5,6,8,10,11,13,15],page_starts=[8],engraving=dict(spacing_system=14,pedal_offset_y=490),
 rh='''
D5:1 F5:.5 E5:.5 A4:2
C5:2 D5:.5 F5:.5 E5:1
G5:1 F5:1 D5:2
C5:1 A4:1 G4:1 E4:1
F4+A4+C5:3 R:1
G4+B4+E5:4
A4+C5+F5:2 G4+B4+E5:2
Eb5:.5 G5:.5 Bb5:1 Ab5:2
G5:1 F5:1 Eb5:1 Db5:1
C5:3 R:1
A4+C5+D5:1 C5+E5+F5:.5 Bb4+D5+E5:.5 E4+G4+A4:2
G4+B4+E5:2 F4+A4+D5:2
G4+Bb4+D5:2 F4+A4+C5:2
E4+G4+Bb4:2 D4+F4+A4:2
G4+A4+C5+D5:4
''',lh='''
D3:.5 A3:.5 F3:1 E3:.5 A3:.5 D4:1
C4:.5 B3:.5 A3:1 F3:.5 A3:.5 C4:1
G3:.5 D4:.5 Bb3:1 A3:1 F3:1
F3:.5 C4:.5 A3:1 G3:.5 Bb3:.5 D4:1
D3+A3:3 R:1
D4:1 F4:.5 E4:.5 A3:2
C4:1 D4:1 E4:1 C4:1
Ab2:.5 Eb3:.5 C4:1 Eb3:2
Db3:1 Ab3:.5 F3:.5 Ab3:1 C4:1
C3:1 G3+Bb3:2 R:1
F3:.5 C4:.5 A3:1 G3:.5 C4:.5 D4:1
E3+B3:2 D3+A3:2
G3+D4:2 F3+C4:2
C3+G3:2 D3+A3:2
F3+A3+C4:4
''',sections={1:'p',6:'pp',8:'mp',10:'pp',11:'mp',13:'p',14:'pp'},lower_sections={1:'pp',6:'p',8:'pp'},words={1:'dolce',14:'poco rit.'},slurs=[(1,5),(8,10),(11,15)],lower_phrases=[(6,7)],hairpins=[('crescendo',1,3),('diminuendo',4,5),('diminuendo',12,14)],tempo_changes={},group=2,
 pedal_spans=[[i*4+a,i*4+b-.2] for i,cuts in enumerate([[0,4],[0,4],[0,4],[0,4],[0,3],[0,4],[0,2,4],[0,4],[0,4],[0,3],[0,4],[0,2,4],[0,2,4],[0,2,4],[0,4]]) for a,b in zip(cuts,cuts[1:])],
 performance=dict(rubato=[58,60,62,56,46,55,53,61,55,44,58,55,51,42,28],phrase_arcs=[[0,19,3],[20,28,3],[28,39,4],[40,60,2]],lower_entries=[[20,28]],pedal_lift=.2,gate=.99,note='The melody passes from a single line into shared harmony. Keep the last reprise tender, easing through the final chord changes until the sixth and ninth feel like remaining light.'))
,
dict(op=181,title='Alder Afterlight',key='a',fifths=0,meter='4/4',bpm=54,
 description='An upper phrase leaves a lower afterimage before it has quite finished. Salt Aperture’s D–F–E–A becomes A–C–B–E. The first lower answer begins three beats after the upper entrance, one octave below it. Later answers remember only part of the phrase, while A minor opens towards F major and a borrowed D-minor colour.',
 difficulty='Advanced overlapping imitation and quiet melodic balance',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The exact opening answer starts in the LH on beat 4 and continues into bar 2. Keep its A–C–B–E connected under the held upper E. Similar entrances return in bars 6–7; the last lower answer omits the opening A. Clear the pedal through the shared rests without breaking held notes.',
 parent_opus=171,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['A','C','B','E']),ancestry=dict(source_opus=171,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=7),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=15,pedal_offset_y=470),
 rh='''
A4:1 C5:.5 B4:.5 E5:2
D5:2 C5:1 R:1
B4:1 D5:1 F5:2
E5:1 D5:.5 B4:.5 A4:2
G4+B4+D5:3 R:1
A4:1 C5:.5 B4:.5 E5:2
F5:2 E5:1 D5:1
C5:1 A4:1 G4:2
F4+A4+C5:3 R:1
C5:1 B4:.5 E5:2.5
D5:2 C5:2
B4:1 A4:1 G4:2
G4+B4+C5+E5:4
''',lh='''
A2+E3:2 R:1 A3:1
C4:.5 B3:.5 E4:2 R:1
G3+D4:3 F3:1
E3:1 B3:1 G#3:2
A3+E4:3 R:1
F3+C4:2 R:1 A3:1
C4:.5 B3:.5 E4:2 D4:1
A3:1 C4:1 E4:2
D3+A3:3 R:1
F3+C4:3 C4:1
B3:.5 E4:2.5 D4:1
E3+B3:2 G#3+D4:2
A2+E3:4
''',sections={1:'p',6:'p',9:'pp',10:'p',12:'pp'},lower_sections={1:'pp',6:'pp',10:'pp'},words={1:'dolce',12:'poco rit.'},slurs=[(1,2),(3,5),(6,9),(10,13)],lower_phrases=[(1,2),(6,8),(10,13)],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*4,i*4+(2.8 if i in [1,4,8] else 3.8)] for i in range(13)],
 performance=dict(rubato=[54,49,55,53,43,55,56,51,42,52,49,40,28],phrase_arcs=[[0,7,3],[8,19,3],[20,35,4],[36,52,2]],lower_entries=[[3,7],[23,28],[39,44]],pedal_lift=.2,gate=.99,note='Let each lower answer become audible while its upper source is still fading. The last answer remembers three notes only; keep its missing beginning as a real absence.'))
,
dict(op=182,title='Hawthorn Dialtone',key='e',fifths=1,meter='3/4',bpm=52,
 description='A small bell keeps appearing above a melody that changes its meaning. Glass Inlet’s inner G–A–G becomes E–F-sharp–E. Repeated upper B notes first belong to E minor, then sound as a major seventh over C. The bell moves briefly to C and D before returning, leaving one final B above an open E-minor ninth.',
 difficulty='Advanced repeated-note touch above independent inner melody',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The upper voice consists of brief, separated bell notes; the lower RH voice sings independently beneath them. Allow the pedal to retain the resonance without turning the rests into held finger notes. Keep the repeated bell soft and give the inner line direction through its own slurs.',
 parent_opus=173,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=3,pitches=['E','F#','E']),ancestry=dict(source_opus=173,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=5,source_pitches=['G','A','G'],transposition_semitones=-3),
 system_starts=[1,4,6,9,12],page_starts=[9],engraving=dict(spacing_system=16,pedal_offset_y=480),
 rh='''
B4:.5 R:1 B4:.5 R:1
R:.5 B4:.5 R:1 B4:.5 R:.5
B4:.5 R:2 B4:.5
B4:1 R:2
C5:.5 R:1 C5:.5 R:1
R:1 C5:.5 R:.5 C5:.5 R:.5
D5:.5 R:1 D5:.5 R:1
C5:1 R:2
B4:.5 R:1 B4:.5 R:1
R:.5 B4:.5 R:2
B4:.5 R:2 B4:.5
A4:1 R:2
B4:.5 R:2.5
B4:3
''',rh_inner='''
E4:1 F#4:.5 E4:1.5
G4:1 F#4:1 E4:1
D4:1 E4:1 F#4:1
G4:2 R:1
E4:1 G4:1 A4:1
G4:1 F4:1 E4:1
F#4:1 A4:1 G4:1
E4:2 R:1
E4:1 F#4:.5 E4:1.5
D#4:1 F#4:1 A4:1
G4:1 F#4:1 E4:1
F#4:2 E4:1
D4:1 E4:2
E4+F#4+G4:3
''',lh='''
E3+B3:3
C3+G3:3
D3+A3:3
E3+B3:2 R:1
A2+E3:3
F3+C4:3
D3+A3:3
C3+G3:2 R:1
E3+B3:3
B2+F#3:3
C3+G3:3
A2+E3:3
B2+F#3:3
E3+B3:3
''',sections={1:'p',5:'p',9:'p',12:'pp'},lower_sections={1:'pp'},words={1:'dolce',13:'poco rit.'},slurs=[],lower_phrases=[],voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=s) for a,b,s in [(0,11,4),(12,23,5),(24,42,3)]],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*3,i*3+(1.8 if i in [3,7] else 2.8)] for i in range(14)],
 performance=dict(rubato=[52,53,51,43,54,52,55,44,51,50,52,47,39,27],phrase_arcs=[[0,11,0],[12,23,1],[24,42,-1]],lower_entries=[],inner_entries=[[0,42]],pedal_lift=.2,gate=.99,note='The middle voice breathes; the bell sounds almost incidental. The changing harmony should make each return of B feel slightly different.'))
,
dict(op=183,title='Briar Refrain',key='g',fifths=-2,meter='3/4',bpm=53,
 description='A high, clear melody returns intact while the ground underneath it changes. Reed Undertow’s G–B-flat–A–D opens a four-bar phrase in G minor. After a two-bar breath, the same phrase returns over E-flat, C minor, F and B-flat. The last recollection drops an octave and breaks the tune into two small pieces.',
 difficulty='Advanced high-register cantabile and harmonic recolouring',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Bars 7–10 repeat the RH pitches and rhythms of bars 1–4 exactly; the LH gives them a different harmonic context. Keep the upper register warm and unforced. The final octave-lower recollection is separated across bars 14–15 and ends in a quiet chord rather than another full phrase.',
 parent_opus=172,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['G','Bb','A','D']),ancestry=dict(source_opus=172,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['G','Bb','A','D'],transposition_semitones=0),
 system_starts=[1,4,7,10,13],page_starts=[10],engraving=dict(spacing_system=15,pedal_offset_y=480),
 rh='''
G5:1 Bb5:.5 A5:.5 D6:1
C6:1 Bb5:1 G5:1
A5:1 G5:.5 F5:.5 D5:1
F5:1 A5:1 G5:1
Eb5:1 D5:1 C5:1
D5:2 R:1
G5:1 Bb5:.5 A5:.5 D6:1
C6:1 Bb5:1 G5:1
A5:1 G5:.5 F5:.5 D5:1
F5:1 A5:1 G5:1
Eb5:1 F5:1 G5:1~
G5:1 F5:1 Eb5:1
D5:2 R:1
G4:1 Bb4:.5 A4:.5 R:1
D5:2 R:1
A4+Bb4+D5:3
''',lh='''
G3:1 D4:1 Bb3:1
Eb3:1 Bb3:1 G3:1
C3:1 G3:.5 Eb4:.5 G3:1
D3:1 A3:1 F#3:1
C3+G3:2 Eb3+Bb3:1
D3+A3:2 R:1
Eb3:1 Bb3:1 G3:1
C3:1 G3:1 Eb4:1
F3:1 C4:.5 A3:.5 Eb4:1
Bb2:1 F3:1 D4:1
Ab2+Eb3:2 G3:1
F3+C4:2 D3+A3:1
G3+D4:2 R:1
Eb3+Bb3:2 R:1
D3+A3:2 R:1
G3+D4:3
''',sections={1:'p',5:'pp',7:'p',11:'mp',13:'pp'},lower_sections={1:'pp',7:'p',11:'pp'},words={1:'cantabile',14:'poco rit.'},slurs=[(1,4),(5,6),(7,10),(11,13),(14,16)],lower_phrases=[],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*3,i*3+(1.8 if i in [5,12,13,14] else 2.8)] for i in range(16)],
 performance=dict(rubato=[53,54,52,48,46,39,54,55,54,49,54,49,40,43,35,25],phrase_arcs=[[0,12,3],[12,17,1],[18,30,4],[30,38,3],[39,48,0]],lower_entries=[],pedal_lift=.2,gate=.99,note='Play the repeated melody with recognition rather than emphasis. Its altered bass gives it a different memory; the last fragment arrives close and low, with room around each thought.'))
,
dict(op=184,title='Fern Longshadow',key='d',fifths=-1,meter='4/4',bpm=50,
 description='An echo moves at half the speed of the voice that made it. Alder Afterlight’s A–C–B–E becomes D–F–E–A. The lower reply doubles every duration, beginning two beats late and continuing across three bars. A C-minor reflection receives the same long shadow; the last answer stops before its final note and the close unexpectedly opens into D major.',
 difficulty='Advanced augmentation canon and sustained lower melody',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The LH answers the opening four RH notes an octave lower with exactly twice their durations. Hold the tied A through the bar line. The same procedure returns in bars 5–7. The final answer in bars 9–10 omits A; allow that silence to be heard before the closing major ninth.',
 parent_opus=181,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','F','E','A']),ancestry=dict(source_opus=181,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['A','C','B','E'],transposition_semitones=5),
 clef_changes={'lh':{1:'treble',4:'bass',5:'treble',8:'bass',9:'treble',11:'bass'}},system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=16,pedal_offset_y=500),
 rh='''
D5:.5 F5:.5 E5:1 A5:2
G5:2 F5:2
E5:2 G5:2
F5:1 E5:1 D5:1 R:1
C5:.5 Eb5:.5 D5:1 G5:2
F5:2 Eb5:2
D5:2 F5:2
Eb5:1 D5:1 C5:1 R:1
D5:.5 F5:.5 E5:1 A5:2
G5:2 F5:2
E5:1 D5:1 C#5:2
F#4+A4+E5:4
''',lh='''
D4:2 D4:1 F4:1
E4:2 A4:2~
A4:2 G4:1 E4:1
Bb3+D4:2 A3+C#4:1 R:1
C4:2 C4:1 Eb4:1
D4:2 G4:2~
G4:2 F4:1 D4:1
Ab3+C4:2 G3+B3:1 R:1
D4:2 D4:1 F4:1
E4:2 R:2
G3+B3:2 A3+C#4:2
D3+A3:4
''',sections={1:'p',4:'pp',5:'p',8:'pp',9:'p',11:'pp'},lower_sections={1:'p',4:'pp',5:'p',8:'pp',9:'p',11:'pp'},words={1:'cantabile',11:'poco rit.'},slurs=[(1,4),(5,8),(9,12)],lower_phrases=[(1,3),(5,7),(9,10)],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*4,i*4+(2.8 if i in [3,7] else 1.8 if i==9 else 3.8)] for i in range(12)],
 performance=dict(rubato=[50,51,47,40,51,50,46,39,49,45,38,26],phrase_arcs=[[0,15,3],[16,31,3],[32,48,1]],lower_entries=[[2,10],[18,26],[34,38]],pedal_lift=.2,gate=.995,note='The slower reply should remain a continuous song while the upper hand has already moved on. The final missing A leaves a space that the major-coloured ending gently answers.'))
,
dict(op=185,title='Juniper Vestige',key='Ab',fifths=-4,meter='6/4',bpm=56,
 description='Whole chords leave echoes rather than single notes. Pearl Backwater’s E-flat–D-flat–E-flat becomes A-flat–G-flat–A-flat at the tops of the opening chords. The lower hand repeats all three chords an octave below after three beats. On their return, the last lower chord remembers G instead of A-flat, gently changing the light inside the harmony.',
 difficulty='Advanced overlapping chord echoes and close voicing',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Every attack is a chord of at least three pitches. The first lower answer reproduces the RH chord shapes and durations an octave below, beginning on beat 4. Its return in bars 7–8 changes only the last chord’s top note from A-flat to G. Keep the answering chords softer and allow their common tones to connect.',
 parent_opus=175,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Ab','Gb','Ab']),ancestry=dict(source_opus=175,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['Eb','Db','Eb'],transposition_semitones=5),
 clef_changes={'lh':{1:'treble',3:'bass',7:'treble',9:'bass'}},system_starts=[1,3,5,7,9],page_starts=[7],engraving=dict(spacing_system=17,pedal_offset_y=520),
 rh='''
C5+Eb5+Ab5:2 Bb4+Db5+Gb5:1 C5+Eb5+Ab5:3
Bb4+Db5+F5:3 Ab4+C5+Eb5:3
G4+Bb4+D5:2 F4+A4+C5:2 E4+G4+Bb4:2
F4+Ab4+C5:3 E4+G4+B4:2 R:1
B4+D#5+F#5:3 A4+C#5+E5:3
Ab4+C5+Eb5:3 G4+Bb4+D5:3
C5+Eb5+Ab5:2 Bb4+Db5+Gb5:1 C5+Eb5+Ab5:3
Bb4+D5+F5:3 Ab4+C5+Eb5:2 R:1
G4+Bb4+D5:3 F4+Ab4+C5:3
G4+Bb4+C5+Eb5:6
''',lh='''
Ab3+C4+Eb4:3 C4+Eb4+Ab4:2 Bb3+Db4+Gb4:1
C4+Eb4+Ab4:3 G3+Bb3+Eb4:3
Eb3+G3+Bb3:2 F3+A3+C4:2 C3+E3+G3:2
Db3+F3+Ab3:3 C3+E3+G3:2 R:1
E3+G#3+B3:3 D3+F#3+A3:3
Db3+F3+Ab3:3 C3+E3+G3:3
Ab3+C4+Eb4:3 C4+Eb4+Ab4:2 Bb3+Db4+Gb4:1
C4+Eb4+G4:3 Ab3+C4+Eb4:2 R:1
Eb3+G3+Bb3:3 Db3+F3+Ab3:3
Ab2+Eb3+G3:6
''',sections={1:'p',4:'pp',5:'mp',7:'p',9:'pp'},lower_sections={1:'pp',5:'p',7:'pp'},words={1:'sostenuto',9:'poco rit.'},slurs=[(1,4),(5,6),(7,10)],lower_phrases=[(1,2),(7,8)],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*6+a,i*6+b-.2] for i,cuts in enumerate([[0,2,3,5,6],[0,3,6],[0,2,4,6],[0,3,5],[0,3,6],[0,3,6],[0,2,3,5,6],[0,3,5],[0,3,6],[0,6]]) for a,b in zip(cuts,cuts[1:])],
 performance=dict(rubato=[56,53,51,43,57,53,55,47,43,28],phrase_arcs=[[0,23,3],[24,36,4],[36,60,2]],lower_entries=[],pedal_lift=.2,gate=.995,note='The second set of echoes changes one upper note only. Keep that small alteration tender and let its harmony open into the last A-flat-major ninth.'))
,
dict(op=186,title='Willow Secondlight',key='e',fifths=1,meter='5/4',meters=['5/4','5/4','4/4','3/4','5/4','5/4','4/4','3/4','5/4','4/4','3/4','5/4'],bpm=56,
 description='An offbeat phrase casts an offbeat answer through changing bar lengths. Briar Refrain’s G–B-flat–A–D becomes E–G–F-sharp–B. The tune enters an eighth late; its lower echo follows two beats later and sustains across the bar. Shorter bars let the intervening thoughts fall away naturally before the next recollection.',
 difficulty='Advanced displaced imitation and changing metre',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Both source and echo begin between the main beats. In bars 1–2 and 5–6, the lower hand repeats the complete opening phrase one octave below with a two-beat delay. Keep the tied B connected across the bar line. The final echo omits that B and leads into a shorter closing phrase.',
 parent_opus=183,motif=dict(hand='rh',start_beat=.5,end_beat=5,pitches=['E','G','F#','B']),ancestry=dict(source_opus=183,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['G','Bb','A','D'],transposition_semitones=-3),
 clef_changes={'lh':{1:'treble',4:'bass',5:'treble',8:'bass',9:'treble',11:'bass'}},system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=16,pedal_offset_y=480),
 rh='''
R:.5 E5:1 G5:.5 F#5:.5 B5:2.5
A5:2 G5:1 F#5:1 E5:1
D5:1 F#5:.5 A5:.5 G5:2
F#5:1 E5:1 R:1
R:.5 E5:1 G5:.5 F#5:.5 B5:2.5
A5:2 G5:1 F#5:1 E5:1
Eb5:1 G5:.5 Bb5:.5 Ab5:2
G5:1 F5:1 R:1
R:.5 E5:1 G5:.5 F#5:.5 B5:2.5
A5:1 G5:1 E5:2
F#5:1 E5:1 R:1
R:1 G4+B4+E5:4
''',lh='''
E4:2 R:.5 E4:1 G4:.5 F#4:.5 B4:.5~
B4:2 A4:1 G4:1 E4:1
C4:1 G4:1 E4:2
B3+F#4:1 D#4+A4:1 R:1
C4:2 R:.5 E4:1 G4:.5 F#4:.5 B4:.5~
B4:2 A4:1 G4:1 E4:1
Ab3:1 Eb4:1 C4:2
Db4+Ab4:1 C4+G4:1 R:1
E4:2 R:.5 E4:1 G4:.5 F#4:1
C4+G4:2 B3+F#4:2
B3+F#4:1 D#4+A4:1 R:1
E3+B3:5
''',sections={1:'p',4:'pp',5:'p',7:'mp',8:'pp',9:'p',11:'pp'},lower_sections={1:'p',4:'pp',5:'p',8:'pp',9:'p',11:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[(1,4),(5,8),(9,12)],lower_phrases=[(1,3),(5,7),(9,10)],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[a,b-.2] for a,b in [(0,5),(5,10),(10,14),(14,16),(17,22),(22,27),(27,31),(31,33),(34,39),(39,43),(43,45),(46,51)]],
 performance=dict(rubato=[56,57,54,44,57,58,54,43,55,52,40,28],phrase_arcs=[[.5,16,3],[17.5,33,4],[34.5,51,2]],lower_entries=[[2.5,7],[19.5,24],[36.5,39]],pedal_lift=.2,gate=.995,note='The entries arrive gently from the side of the beat. Let the shorter bars release pressure; the final lower answer is only a trace of the complete earlier phrase.'))
,
dict(op=187,title='Elm Palinode',key='g',fifths=-2,meter='5/4',bpm=52,
 description='Two middle voices remember one another beneath a still outer frame. Hawthorn Dialtone’s E–F-sharp–E becomes G–A–G in the RH inner voice. The LH tenor answers two beats later, holding the last note through the next bar. A wider middle phrase reaches B-flat and F colours before the opening inner question returns over its original bass.',
 difficulty='Advanced four-voice imitation and independent finger sustain',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='There are two voices in each hand. The tenor echoes the opening inner phrase one octave below after two beats; the bass must stay held under that moving line. The combined hand reaches remain within an octave. The final answer stops when its quoted three notes finish, leaving the upper voices to continue alone briefly.',
 parent_opus=182,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=5,pitches=['G','A','G']),ancestry=dict(source_opus=182,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=3,source_pitches=['E','F#','E'],transposition_semitones=3),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=17,spacing_staff=22,pedal_offset_y=580),
 rh='''
D5:5
Eb5:5
D5:5
C5:3 R:2
F5:5
G5:5
A5:5
G5:3 R:2
D5:5
Eb5:5
D5:5
D5:5
''',rh_inner='''
G4:1 A4:1 G4:3
Bb4:1 A4:1 G4:3
F4:1 G4:1 A4:3
Eb4:3 R:2
Bb4:1 C5:1 Bb4:3
D5:1 Eb5:1 D5:3
D5:1 E5:1 F5:3
Eb5:1 D5:1 C5:1 R:2
G4:1 A4:1 G4:3
Bb4:1 A4:1 G4:3
F4:1 A4:1 G4:3
F4+G4+Bb4:5
''',lh='''
C3:5
Eb3:5
D3:5
G3:3 R:2
Eb3:5
F3:5
G3:5
Ab3:3 R:2
C3:5
Eb3:5
D3:5
G3:5
''',lh_upper='''
R:2 G3:1 A3:1 G3:1~
G3:2 Bb3:1 D4:2
F#3:1 A3:1 C4:3
Bb3:1 D4:2 R:2
R:2 Bb3:1 C4:1 Bb3:1~
Bb3:2 C4:1 Eb4:2
Bb3:1 D4:1 F4:3
C4:1 Eb4:1 F4:1 R:2
R:2 G3:1 A3:1 G3:1~
G3:2 R:3
A3:1 C4:1 F#3:3
Bb3:5
''',sections={1:'p',5:'mp',8:'pp',9:'p',11:'pp'},lower_sections={1:'p',5:'mp',8:'pp',9:'p',11:'pp'},words={1:'cantabile',11:'poco rit.'},slurs=[(1,4),(5,8),(9,12)],lower_phrases=[],voice_phrases=[dict(voice=v,start_beat=a,end_beat=b,swell=s) for v,spans in [('inner',[(0,18,4),(20,38,5),(40,60,3)]),('tenor',[(2,7,4),(7,18,3),(22,27,4),(27,38,4),(42,47,3),(50,60,2)])] for a,b,s in spans],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*5,i*5+(2.8 if i in [3,7] else 4.8)] for i in range(12)],
 performance=dict(rubato=[52,53,51,42,55,57,58,46,52,49,41,28],phrase_arcs=[[0,18,1],[20,38,2],[40,60,0]],lower_entries=[],inner_entries=[[0,60]],tenor_entries=[[0,60]],pedal_lift=.2,gate=.995,note='The inner phrases should feel like two people speaking softly beneath the same held light. Let the last lower quotation end naturally while the upper line continues its thought.'))
,
dict(op=188,title='Moss Palimpsest',key='F',fifths=-1,meter='7/4',bpm=44,
 description='A phrase gradually loses its last note. Mallow Slackwater’s F–E-flat–F becomes C–B-flat–C. The lower reply remembers only C and B-flat; a higher F–E-flat–F receives the same incomplete answer. By the final return the upper voice also leaves its third note unsaid, and the remaining harmony settles into F major.',
 difficulty='Intermediate to advanced sparse phrasing and resonant silence',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The missing final notes are written rests, not pauses to fill. Keep the long shared silences in bars 2, 4, 6, 7 and 8 free of pedal. The upper register briefly reaches C6, but the dynamics stay intimate. The final chord is a new harmonic answer rather than a completion of the earlier tune.',
 parent_opus=178,motif=dict(hand='rh',start_beat=0,end_beat=7,pitches=['C','Bb','C']),ancestry=dict(source_opus=178,source_hand='lh',source_start_beat=0,source_end_beat=7,source_pitches=['F','Eb','F'],transposition_semitones=7),
 clef_changes={'lh':{1:'bass',6:'treble',7:'bass'}},system_starts=[1,3,5,7],page_starts=[5],engraving=dict(spacing_system=17,pedal_offset_y=470),
 rh='''
C5:2 Bb4:2 C5:3
E5+G5:4 R:3
F5:3 E5:2 D5:2
Eb5:4 R:3
F5:2 Eb5:2 F5:3
A5+C6:4 R:3
C5:2 Bb4:2 R:3
A4:3 G4:2 R:2
A4+C5+G5:7
''',lh='''
F3+C4:4 R:3
C4:2 Bb3:2 R:3
A3+C4:3 G3+B3:2 F3+A3:2
Ab3+C4:4 R:3
Bb2+F3:4 R:3
F4:2 Eb4:2 R:3
G3+D4:4 R:3
E3+B3:3 F3+C4:2 R:2
F3+C4:7
''',sections={1:'p',2:'pp',3:'p',4:'pp',5:'p',6:'pp'},lower_sections={1:'pp',2:'p',3:'pp',6:'p',7:'pp'},words={1:'lento',8:'poco rit.'},slurs=[(1,2),(3,4),(5,6),(7,9)],lower_phrases=[(2,2),(6,6)],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[0,1.8],[2,3.8],[4,6.8],[7,8.8],[9,10.8],[14,16.8],[17,18.8],[19,20.8],[21,24.8],[28,29.8],[30,31.8],[32,34.8],[35,36.8],[37,38.8],[42,43.8],[44,45.8],[49,51.8],[52,53.8],[56,62.8]],
 performance=dict(rubato=[44,38,46,37,45,37,40,34,25],phrase_arcs=[[0,11,2],[14,25,2],[28,39,2],[42,63,-1]],lower_entries=[[7,11],[35,39]],pedal_lift=.2,gate=.995,note='Give the rests the same attention as the notes. Each shortened answer leaves more of the phrase to memory; the final major ninth arrives without trying to restore what has disappeared.'))
,
dict(op=189,title='Rowan Refraction',key='a',fifths=0,meter='4/4',bpm=56,
 description='A curved triplet gesture is passed between the hands while its last note is still ringing. Willow Secondlight’s E–G–F-sharp–B becomes A–C–B–E. Five upper phrases receive exact lower echoes two beats later; their changing harmonies pass through E minor and an A-flat reflection before the motion settles into an A-minor ninth.',
 difficulty='Advanced triplet imitation, register shifts and sustained arrivals',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The three quarter-note triplets occupy two ordinary beats. As the RH holds its fourth note, the LH starts the same four-note phrase one octave below. Keep the long arrivals legato and the triplets rounded. Written rests in bars 4 and 8 provide time for the larger LH register returns.',
 parent_opus=186,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['A','C','B','E']),ancestry=dict(source_opus=186,source_hand='rh',source_start_beat=.5,source_end_beat=5,source_pitches=['E','G','F#','B'],transposition_semitones=5),
 clef_changes={'lh':{1:'bass',4:'treble',5:'bass',7:'treble',9:'bass'}},system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=16,pedal_offset_y=490),
 rh='''
A4:2/3 C5:2/3 B4:2/3 E5:2
F5:1 E5:1 D5:2
E5:2/3 G5:2/3 F#5:2/3 B5:2
A5:1 G5:1 F#5:1 R:1
A4:2/3 C5:2/3 B4:2/3 E5:2
F5:2 E5:1 D5:1
Eb5:2/3 G5:2/3 F5:2/3 Bb5:2
Bb5:1 Ab5:1 Gb5:1 R:1
A4:2/3 C5:2/3 B4:2/3 E5:2
D5:2 C5:2
B4:1 A4:1 G4:2
G4+B4+C5+E5:4
''',lh='''
A2+E3:2 A3:2/3 C4:2/3 B3:2/3
E4:2 G3+B3:2
C3+G3:2 E4:2/3 G4:2/3 F#4:2/3
B4:2 A4:1 R:1
F3+C4:2 A3:2/3 C4:2/3 B3:2/3
E4:2 D4:1 C4:1
Ab3+Eb4:2 Eb4:2/3 G4:2/3 F4:2/3
Bb4:2 Ab4:1 R:1
D3+A3:2 A3:2/3 C4:2/3 B3:2/3
E4:2 R:2
E3+B3:2 G#3+D4:2
A2+E3:4
''',sections={1:'p',3:'mp',4:'pp',5:'p',7:'mp',8:'pp',9:'p',11:'pp'},lower_sections={1:'pp',3:'p',4:'pp',5:'pp',7:'p',8:'pp',9:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[(1,2),(3,4),(5,6),(7,8),(9,12)],lower_phrases=[(1,2),(3,4),(5,6),(7,8),(9,10)],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*4,i*4+(2.8 if i in [3,7] else 1.8 if i==9 else 3.8)] for i in range(12)],
 performance=dict(rubato=[56,53,59,47,56,54,58,45,55,50,41,28],phrase_arcs=[[0,8,3],[8,15,4],[16,24,3],[24,31,4],[32,48,1]],lower_entries=[[2,6],[10,14],[18,22],[26,30],[34,38]],pedal_lift=.2,gate=.99,note='The triplet echo begins while the upper arrival still rings. Let the changing harmonies carry the colour, with no extra accent when the hands exchange roles.'))
,
dict(op=190,title='Willow Remanence',key='Bb',fifths=-2,meter='4/4',bpm=52,
 description='The last study remembers the beginning from inside its harmony. Alder Afterlight’s A–C–B–E becomes G–B-flat–A–D in the RH inner voice. The lower hand answers one bar later while the upper F breaks into small bell notes. A C-minor recollection follows; the opening then returns over E-flat, and its last lower answer leaves D unsounded before a B-flat sixth-and-ninth close.',
 difficulty='Advanced inner melody, delayed answers and bell-note release',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The inner RH melody is the source of the LH echoes in bars 2 and 6, each one octave lower and one bar later. The upper voice alternates held notes with short bell-like releases. In bar 10 the LH remembers G–B-flat–A only. Keep the three independent lines clear and let the final chord follow the last bell without emphasis.',
 parent_opus=181,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=4,pitches=['G','Bb','A','D']),ancestry=dict(source_opus=181,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['A','C','B','E'],transposition_semitones=-2),
 system_starts=[1,3,5,7,9,11,13],page_starts=[7],engraving=dict(spacing_system=16,spacing_staff=16,pedal_offset_y=510),
 rh='''
F5:4
F5:.5 R:1 F5:.5 R:2
E5:4
D5:3 R:1
G5:4
G5:.5 R:1 G5:.5 R:2
F5:4
Eb5:3 R:1
F5:4
F5:.5 R:2.5 F5:.5 R:.5
Eb5:4
D5:2 R:2
F5:.5 R:3.5
F5:4
''',rh_inner='''
G4:1 Bb4:.5 A4:.5 D5:2
F4:2 A4:2
G4:1 A4:1 Bb4:2
F4+A4:3 R:1
C5:1 Eb5:.5 D5:.5 G4:2
Bb4:2 C5:2
Ab4:1 C5:1 Eb5:2
G4+Bb4:3 R:1
G4:1 Bb4:.5 A4:.5 D5:2
C5:2 A4:2
G4:2 F4:2
F4:2 R:2
A4:1 G4:1 F4:2
G4+C5+D5:4
''',lh='''
G3+D4:2 R:2
G3:1 Bb3:.5 A3:.5 D4:2
C3+G3:2 E3+Bb3:2
Bb2+F3:3 R:1
C3+G3:2 R:2
C4:1 Eb4:.5 D4:.5 G3:2
Ab2+Eb3:2 C4:2
Eb3+Bb3:3 R:1
Eb3+Bb3:2 R:2
G3:1 Bb3:.5 A3:.5 R:2
C3+G3:2 F3+C4:2
Bb2+F3:2 R:2
F3+C4:2 Eb3+A3:2
Bb2+F3:4
''',sections={1:'p',5:'mp',8:'pp',9:'p',11:'pp'},lower_sections={1:'pp',2:'p',3:'pp',6:'p',7:'pp',10:'p',11:'pp'},words={1:'dolce',13:'poco rit.'},slurs=[],lower_phrases=[(2,2),(6,6),(10,10)],voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=s) for a,b,s in [(0,15,4),(16,31,5),(32,46,3),(48,56,1)]],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*4+a,i*4+b-.2] for i,cuts in enumerate([[0,4],[0,4],[0,2,4],[0,3],[0,4],[0,4],[0,4],[0,3],[0,4],[0,2],[0,2,4],[0,2],[0,2,4],[0,4]]) for a,b in zip(cuts,cuts[1:])],
 performance=dict(rubato=[52,50,51,42,54,52,55,43,51,47,45,37,35,25],phrase_arcs=[[0,15,0],[16,31,1],[32,46,0],[48,56,-1]],lower_entries=[[4,8],[20,24],[36,38]],inner_entries=[[0,56]],pedal_lift=.2,gate=.995,note='The final echo is allowed to remain incomplete. The last upper bell and the inner descent leave space for a chord that feels warm, open and unhurried.'))
,
dict(op=191,title='Linden Nightglass',key='d',fifths=-1,meter='4/4',bpm=54,
 description='A middle-voice D–F–E–A melody settles into a held D-minor harmony. Its upper note descends C–B–B-flat while every other chord tone remains still; the same small change returns later with the bass moving beneath it. A brief G-minor song opens the texture before a D-minor sixth-and-ninth close.',
 difficulty='Advanced inner cantabile and quiet chromatic voicing',technique_limits=dict(chord_span=12,melodic_leap=12,rapid_leap=7),technical_note='Voice the RH inner melody above its soft upper line. Bars 2–4 keep the inner dyad and LH fifth identical while only the upper note falls by semitone. Shared rests clear the pedal before the next phrase.',
 parent_opus=181,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=4,pitches=['D','F','E','A']),ancestry=dict(source_opus=181,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['A','C','B','E'],transposition_semitones=5),
 system_starts=[1,3,5,7,9,11,13],page_starts=[7],engraving=dict(spacing_system=16,spacing_staff=18,pedal_offset_y=510),
 rh='''
C5:4
C5:4
B4:4
Bb4:4
B4:3 R:1
D5:4
Db5:4
C5:3 R:1
C5:4
B4:4
Bb4:4
A4:3 R:1
D5:4
E5:4
''',rh_inner='''
D4:1 F4:.5 E4:.5 A4:2
F4+A4:4
F4+A4:4
F4+A4:4
E4:1 G4:1 F4:1 R:1
G4:1 Bb4:1 A4:2
G4:1 F4:.5 E4:.5 G4:2
E4+G4:3 R:1
D4:1 F4:.5 E4:.5 A4:2
G4:2 F4:2
F4:1 G4:1 A4:2
E4+G4:3 R:1
F4:1 E4:1 D4:2
F4+A4+B4:4
''',lh='''
D3+A3:4
D3+A3:4
D3+A3:4
D3+A3:4
G3+B3:3 R:1
G3+D4:4
Bb2+F3:4
C3+G3:3 R:1
D3+A3:4
C3+G3:4
Bb2+F3:4
A2+E3:3 R:1
G2+D3:2 A2+E3:2
D3+A3:4
''',sections={1:'p',2:'pp',6:'p',8:'pp',9:'p',12:'pp'},lower_sections={1:'pp'},words={1:'cantabile',13:'poco rit.'},slurs=[],lower_phrases=[],voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=s) for a,b,s in [(0,19,3),(20,31,4),(32,47,3),(48,56,1)]],hairpins=[],tempo_changes={},group=2,
 pedal_spans=sorted([[i*4,i*4+(2.8 if i in [4,7,11] else 3.8)] for i in range(14) if i!=12]+[[48,49.8],[50,51.8]]),
 performance=dict(rubato=[54,53,51,49,43,56,53,43,53,51,49,42,39,28],phrase_arcs=[[0,19,0],[20,31,1],[32,47,0],[48,56,-1]],inner_entries=[[0,56]],lower_entries=[],pedal_lift=.2,gate=.995,note='The inner song is close and unhurried; the upper chromatic notes shade it rather than interrupting it.'))
,
dict(op=192,title='Bracken Cradlesong',key='e',fifths=1,meter='6/8',meters=['6/8','6/8','8/8','6/8','6/8','8/8','6/8','6/8','8/8','6/8','6/8','8/8','6/8','8/8'],bpm=65,
 description='A rocking E-minor song lengthens selected bars by a quarter note. Beneath E–G–F-sharp–B, the bass falls E–D-sharp–D–C-sharp–C–B while the left hand keeps returning to neighbouring tones. A G-major opening in the middle loosens the descent; the returning song finishes with E minor warmed by its sixth and ninth.',
 difficulty='Intermediate to advanced unequal compound bars and legato cantabile',technique_limits=dict(chord_span=12,melodic_leap=12,rapid_leap=7),technical_note='The 8/8 bars add one quarter-note breath to the 6/8 sway. The LH rocking figure changes its final duration and sometimes leaves the last beat silent. Let the chromatic bass descent support one melodic phrase rather than six separate gestures.',
 parent_opus=191,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['E','G','F#','B']),ancestry=dict(source_opus=191,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=2),
 system_starts=[1,3,5,7,9,11,13],page_starts=[7],engraving=dict(spacing_system=15,pedal_offset_y=520),
 rh='''
E4:1 G4:.5 F#4:.5 B4:1
A4:1.5 G4:.5 F#4:1
E4:1 G4:.5 B4:.5 A4:1 G4:1
F#4:1.5 A4:.5 G4:1
E4:1 G4:.5 B4:1 C5:.5
A4:1 F#4:1 E4:1 R:1
B4:1 D5:.5 E5:1 D5:.5
C5:1.5 B4:.5 G4:1
A4:1 C5:.5 B4:.5 F#4:1 R:1
E4:1 G4:.5 F#4:.5 B4:1
C5:1 B4:.5 A4:.5 G4:1
F#4:1 A4:.5 G4:.5 E4:1 R:1
G4:1 F#4:.5 E4:1.5
G4+B4+C#5+F#5:4
''',lh='''
E3:1 B3:.5 G3:1 R:.5
D#3:1 B3:.5 G3:1 R:.5
D3:1 B3:.5 G3:1 R:.5 A3:1
C#3:1 A3:.5 E3:1 R:.5
C3:1 G3:.5 E3:1 R:.5
B2:1 F#3:.5 A3:.5 B3:1 R:1
G3:1 D4:.5 B3:1 R:.5
E3:1 B3:.5 G3:1 R:.5
C3:1 G3:.5 A3:.5 B3:1 R:1
E3:1 B3:.5 G3:1 R:.5
C3:1 G3:.5 E3:1 R:.5
B2:1 F#3:.5 A3:.5 D#4:1 R:1
A3:1 C4:.5 B3:1.5
E3+B3:4
''',sections={1:'p',4:'pp',7:'mp',9:'pp',10:'p',12:'pp'},lower_sections={1:'pp'},words={1:'dolce',13:'poco rit.'},slurs=[(1,6),(7,9),(10,12),(13,14)],lower_phrases=[],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[sum([3,3,4,3,3,4,3,3,4,3,3,4,3,4][:i]),sum([3,3,4,3,3,4,3,3,4,3,3,4,3,4][:i])+n-(1.2 if i in [5,8,11] else .2)] for i,n in enumerate([3,3,4,3,3,4,3,3,4,3,3,4,3,4])],
 performance=dict(rubato=[65,64,61,63,62,51,67,64,52,63,61,50,46,32],phrase_arcs=[[0,19,4],[20,29,4],[30,39,3],[40,47,0]],lower_entries=[],pedal_lift=.2,gate=.99,note='The extra quarter beat is a breath inside the rocking motion. The return is softer and the ending opens into the sixth and ninth.'))
]
