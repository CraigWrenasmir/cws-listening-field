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
]
