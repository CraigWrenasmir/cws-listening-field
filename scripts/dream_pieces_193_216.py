PIECES = [
dict(op=193,title='Hazel Undertone',key='f',fifths=-4,meter='3/4',bpm=52,
 description='A five-bar ground, F–E-flat–D-flat–C–F, returns three times beneath a developing lullaby. The second circuit introduces an E-natural against F minor and a softened dominant ninth; the last reshapes the melody into close chords and finally lets A-natural warm the F-major ninth.',
 difficulty='Intermediate to advanced changing voicings over a five-bar ground',technique_limits=dict(chord_span=12,melodic_leap=12,rapid_leap=7),technical_note='The first bass note of each bar repeats the same five-bar pattern throughout. The later upper harmonies change while the ground remains intact. Keep the new E-natural and final A-natural quiet and clearly voiced.',
 parent_opus=182,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['Ab','Bb','Ab']),ancestry=dict(source_opus=182,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=3,source_pitches=['E','F#','E'],transposition_semitones=4),
 system_starts=[1,4,6,9,11,14],page_starts=[9],engraving=dict(spacing_system=15,pedal_offset_y=520),
 rh='''
Ab4:1 Bb4:.5 Ab4:1.5
G4:1 Bb4:.5 C5:1.5
F4:1 Ab4:.5 C5:1 Bb4:.5
G4:1 E4:.5 Bb4:.5 Ab4:1
G4:1 Ab4:1 R:1
Ab4+C5+E5:2 G4+B4+Eb5:1
G4+Bb4+D5:1.5 F4+Ab4+C5:1.5
F4+Ab4+C5:2 E4+G4+Bb4:1
E4+Bb4+Db5:1 F4+Bb4+C5:1 E4+G4+Bb4:1
F4+Ab4+D5:2 R:1
Ab4:1 Bb4:.5 Ab4:1.5
G4:1 Bb4:.5 D5:1 C5:.5
Ab4+C5:1 F4+Bb4:1 Ab4:1
G4+Bb4:1 E4+A4:1 R:1
G4+A4+C5+E5:3
''',lh='''
F3:1 Ab3+C4:1.5 R:.5
Eb3:1 G3+Bb3:1.5 R:.5
Db3:1 F3+Ab3:1.5 R:.5
C3:1 E3+Bb3:2
F3:1 Ab3+C4:1 R:1
F3:1 Ab3+C4:2
Eb3:1 G3+Bb3:1.5 R:.5
Db3:1 F3+Ab3:2
C3:1 E3+Bb3:2
F3:1 Ab3+C4:1 R:1
F3:1 Ab3+C4:2
Eb3:1 G3+C4:2
Db3:1 F3+Ab3:2
C3:1 E3+Bb3:1 R:1
F3+C4:3
''',sections={1:'p',4:'pp',6:'mp',9:'p',10:'pp',11:'p',14:'pp'},lower_sections={1:'pp'},words={1:'cantabile',14:'poco rit.'},slurs=[(1,5),(6,10),(11,15)],lower_phrases=[],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*3+a,i*3+b-.2] for i,c in enumerate([[0,3],[0,3],[0,3],[0,3],[0,2],[0,2,3],[0,1.5,3],[0,2,3],[0,1,2,3],[0,2],[0,3],[0,3],[0,3],[0,2],[0,3]]) for a,b in zip(c,c[1:])],
 performance=dict(rubato=[52,53,52,49,43,54,53,51,48,42,51,50,47,39,28],phrase_arcs=[[0,14,4],[15,29,5],[30,45,2]],lower_entries=[],pedal_lift=.2,gate=.99,note='Three passes of the same ground acquire different upper light. The final major third is a gentle release rather than a bright accent.')),
dict(op=194,title='Willow Hearthline',key='Bb',fifths=-2,meter='5/4',bpm=54,
 description='A tenor lullaby sings G–B-flat–A–D beneath soft upper chords. The held bass descends F–E–E-flat–D–D-flat–C while the melody keeps its own five-beat breath. A quieter return passes through G minor and settles into B-flat with a sixth and ninth.',
 difficulty='Advanced LH tenor melody above held bass notes',technique_limits=dict(chord_span=12,melodic_leap=12,rapid_leap=7),technical_note='The LH sustains its bass while the tenor moves independently, within an octave. Keep the RH chords softer than the tenor. Release both LH voices together at the written breaths; the held bass should not turn the changing middle notes into a blur.',
 parent_opus=190,motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=5,pitches=['G','Bb','A','D']),ancestry=dict(source_opus=190,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=4,source_pitches=['G','Bb','A','D'],transposition_semitones=0),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=16,spacing_staff=20,pedal_offset_y=510),
 rh='''
F4+A4+C5:3 R:2
F4+A4+B4:3 R:2
F4+A4+Bb4:3 R:2
E4+G4+A4:3 R:2
Eb4+F4+Ab4:3 R:2
E4+G4+Bb4:4 R:1
D4+F4+A4:3 R:2
C4+Eb4+G4:3 R:2
D4+F4+Bb4:3 R:2
C4+Eb4+A4:3 R:2
D4+G4+C5:5
''',lh='''
F3:5
E3:5
Eb3:5
D3:5
Db3:5
C3:4 R:1
G2:5
C3:5
Bb2:5
F2:3 R:2
Bb2:5
''',lh_upper='''
G3:2 Bb3:1 A3:1 D4:1
C4:2 Bb3:1 A3:2
G3:2 Bb3:1 C4:2
F3:2 A3:1 C4:1 B3:1
Ab3:2 C4:1 Bb3:2
G3:1 Bb3:1 A3:2 R:1
Bb2:2 D3:1 F3:1 G3:1
Eb3:2 G3:1 Bb3:2
D3:2 F3:1 G3:1 A3:1
A2+C3:3 R:2
F3+Bb3:5
''',sections={1:'pp',5:'p',6:'pp'},lower_sections={1:'p',5:'mp',6:'pp',7:'p',10:'pp'},words={1:'cantabile',10:'poco rit.'},slurs=[],lower_phrases=[],voice_phrases=[dict(voice='tenor',start_beat=a,end_beat=b,swell=s) for a,b,s in [(0,29,4),(30,48,3)]],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*5,i*5+(2.8 if i==9 else 3.8 if i==5 else 4.8)] for i in range(11)],
 performance=dict(rubato=[54,53,52,51,49,42,53,51,47,38,28],phrase_arcs=[[0,29,0],[30,48,0],[50,55,-1]],lower_entries=[],tenor_entries=[[0,55]],pedal_lift=.2,gate=.99,note='The middle song belongs to the left hand. Let the upper chords recede while the chromatic bass descends without haste.')),
dict(op=195,title='Camellia Nightfold',key='F',fifths=-1,meter='7/4',bpm=58,
 description='An entirely chordal lullaby carries D–F–E–A in its top notes. Over an unchanged F-based lower chord, F–A–C becomes F–A-flat–C, then E–A-flat–C, then E–G–C: one pitch changes at each step. The seven-beat breaths open into a distant D-flat colour and return to a soft F-major ninth.',
 difficulty='Advanced chord voicing and long seven-beat breaths',technique_limits=dict(chord_span=12,melodic_leap=12,rapid_leap=7),technical_note='Every sounding event is a chord of at least three pitches. Bars 2–3 hold the LH shape constant while exactly one RH pitch changes per chord. Clear each new harmony with the written pedal lift; all chords are struck together, without unnotated rolls.',
 parent_opus=191,motif=dict(hand='rh',start_beat=0,end_beat=7,pitches=['D','F','E','A']),ancestry=dict(source_opus=191,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),
 system_starts=[1,2,3,4,5,6,7,8,9],page_starts=[5],engraving=dict(spacing_system=13,pedal_offset_y=510),
 rh='''
F4+A4+D5:2 A4+C5+F5:1 G4+B4+E5:1 D4+F4+A4:3
F4+A4+C5:3 F4+Ab4+C5:3 R:1
E4+Ab4+C5:3 E4+G4+C5:3 R:1
A4+C5+D5:3 Ab4+C5+Db5:3 R:1
F4+A4+Bb4:3 E4+A4+D5:3 R:1
Eb4+G4+Bb4:3 E4+G4+Bb4:3 R:1
F4+A4+D5:2 A4+C5+F5:1 G4+B4+E5:1 D4+F4+A4:2 R:1
E4+G4+C5:3 F4+A4+C5:3 R:1
G4+A4+C5+E5:7
''',lh='''
C3+G3+Bb3:2 F3+A3+C4:1 E3+G3+B3:1 D3+A3+C4:3
F3+G3+C4:3 F3+G3+C4:3 R:1
F3+G3+C4:3 F3+G3+C4:3 R:1
Bb2+F3+A3:3 Db3+Ab3+C4:3 R:1
G3+Bb3+D4:3 C3+G3+Bb3:3 R:1
F3+Ab3+C4:3 F3+Ab3+C4:3 R:1
Bb2+D3+F3:2 F3+A3+C4:1 E3+G3+B3:1 D3+A3+C4:2 R:1
C3+E3+Bb3:3 F3+A3+C4:3 R:1
F3+G3+C4:7
''',sections={1:'p',2:'pp',4:'mp',5:'p',6:'pp',7:'p',8:'pp'},lower_sections={1:'pp'},words={1:'dolce',8:'poco rit.'},slurs=[(1,3),(4,6),(7,9)],lower_phrases=[],hairpins=[],tempo_changes={},group=1,
 pedal_spans=[[i*7+a,i*7+b-.2] for i,c in enumerate([[0,2,3,4,7],[0,3,6],[0,3,6],[0,3,6],[0,3,6],[0,3,6],[0,2,3,4,6],[0,3,6],[0,7]]) for a,b in zip(c,c[1:])],
 performance=dict(rubato=[58,54,51,58,55,48,54,44,31],phrase_arcs=[[0,20,2],[21,41,4],[42,63,1]],lower_entries=[],pedal_lift=.2,gate=.99,note='The chord changes are small movements of light. Leave the final beat empty where written and let the last harmony settle without an accent.')),
dict(op=196,title='Sedge Lanternfall',key='Ab',fifths=-4,meter='12/8',bpm=66,
 description='A close inner melody floats inside twelve-eight arpeggios. Hazel Undertone’s A-flat–B-flat–A-flat opens the song; later, A-flat–G–G-flat–F and A–A-flat–G–F shade it by semitones. The upper voice holds long notes while the lower hand moves in broad compound pulses, ending with A-flat coloured by its sixth and ninth.',
 difficulty='Advanced inner melody and spacious compound arpeggios',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=7),technical_note='The RH upper note remains quieter than the independent inner melody. The LH arpeggios move on dotted-quarter pulses; clear the large bass moves with relaxed lateral motion. The six larger LH returns span 13–17 semitones with at least 1.5 quarter beats between attacks; these are deliberate slow register shifts, not held stretches. Inner chromatic descents in bars 3 and 6 retain their written lengths.',
 parent_opus=193,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=3,pitches=['Ab','Bb','Ab']),ancestry=dict(source_opus=193,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['Ab','Bb','Ab'],transposition_semitones=0),
 system_starts=[1,3,5,7,9],page_starts=[5],engraving=dict(spacing_system=17,spacing_staff=18,pedal_offset_y=520),
 rh='''
Eb5:6
Db5:6
C5:6
C5:5 R:1
Eb5:6
D5:6
Db5:6
C5:5 R:1
Db5:3 C5:2 R:1
Eb5:6
''',rh_inner='''
Ab4:1 Bb4:.5 Ab4:1.5 G4:1 F4:1 Eb4:1
F4:1.5 Ab4:.5 G4:1 Bb4:1.5 Ab4:1.5
Ab4:2 G4:1 Gb4:2 F4:1
E4:1 G4:1 Bb4:2 Ab4:1 R:1
Ab4:1 C5:.5 Bb4:.5 G4:2 F4:2
A4:2 Ab4:1 G4:2 F4:1
F4:1 Ab4:.5 G4:.5 Bb4:1 Ab4:1 F4:2
E4:1 G4:1 Bb4:2 G4:1 R:1
F4:2 Ab4:1 G4:1 F4:1 R:1
F4+Ab4+Bb4:6
''',lh='''
Ab2:1.5 Eb3:1.5 C4:1.5 Bb3:1.5
G2:1.5 Eb3:1.5 Bb3:1.5 Ab3:1.5
Gb2:1.5 Db3:1.5 Ab3:1.5 Bb3:1.5
F2:1.5 C3:1.5 A3:2 R:1
Db3:1.5 Ab3:1.5 F3:1.5 C4:1.5
Bb2:1.5 F3:1.5 Ab3:1.5 F3:1.5
Eb3:1.5 Bb3:1.5 G3:1.5 Db4:1.5
C3:1.5 G3:1.5 Bb3:1 E3:1 R:1
Db3:1.5 Ab3:1.5 G3:1 Bb3:1 R:1
Ab2:1.5 Eb3:1.5 Ab3+C4:3
''',sections={1:'p',3:'pp',5:'mp',7:'p',8:'pp'},lower_sections={1:'pp'},words={1:'cantabile',9:'poco rit.'},slurs=[],lower_phrases=[],voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=s) for a,b,s in [(0,23,4),(24,47,5),(48,60,1)]],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*6,i*6+(4.8 if i in [3,7,8] else 5.8)] for i in range(10)],
 performance=dict(rubato=[66,64,60,52,68,65,60,51,46,32],phrase_arcs=[[0,23,0],[24,47,1],[48,60,-1]],inner_entries=[[0,60]],lower_entries=[],pedal_lift=.2,gate=.99,note='The arpeggios cradle a more personal inner song. Its semitone changes are expressive arrivals within the phrase, never separate accents.')),
dict(op=197,title='Alder Vesper',key='c',fifths=-3,meter='4/4',bpm=50,
 description='Four quiet voices surround a C–E-flat–D–G lullaby. Across the first four bars the upper line falls B-flat–A–A-flat–G while the tenor rises G–A-flat–A–B-flat over an unchanged C bass. The middle passage frees the inner lines before a shorter return and an open C-minor ninth.',
 difficulty='Advanced four-voice cantabile and contrary chromatic motion',technique_limits=dict(chord_span=12,melodic_leap=12,rapid_leap=7),technical_note='Keep the two inner lines distinct beneath the upper voice and above the bass. The opening chromatic lines move in opposite directions, one step per bar. Both hands have written silence at each main phrase boundary; the final chord follows a two-beat shared rest.',
 parent_opus=191,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=4,pitches=['C','Eb','D','G']),ancestry=dict(source_opus=191,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=-2),
 system_starts=[1,3,5,7,9,11,13],page_starts=[7],engraving=dict(spacing_system=16,spacing_staff=22,pedal_offset_y=510),
 rh='''
Bb4:4
A4:4
Ab4:4
G4:3 R:1
Ab4:4
G4:4
F#4:4
G4:3 R:1
Bb4:4
A4:4
Ab4:4
G4:2 R:2
D5:4
''',rh_inner='''
C4:1 Eb4:.5 D4:.5 G4:2
Eb4+G4:4
D4+F4:4
D4+F4:3 R:1
Eb4:1 F4:1 G4:1 F4:1
C4:1 Eb4:.5 D4:.5 F4:2
A3:1 C4:1 D4:1 C4:1
B3:1 D4:1 F4:.5 E4:.5 R:1
C4:1 Eb4:.5 D4:.5 G4:2
Eb4+G4:4
D4+F4:4
D4+F4:2 R:2
Eb4+G4+C5:4
''',lh='''
C3:4
C3:4
C3:4
C3:3 R:1
F3:4
Eb3:4
D3:4
G2:3 R:1
C3:4
C3:4
F3:4
G2:2 R:2
C3:4
''',lh_upper='''
G3:4
Ab3:4
A3:4
Bb3:3 R:1
Ab3:1 C4:1 Ab3:1 G3:1
G3:1 Bb3:1 G3:1 F3:1
F3:1 A3:1 G3:1 F3:1
B2:1 D3:1 F3:1 R:1
G3:4
Ab3:4
A3:4
B2+F3:2 R:2
G3+Bb3:4
''',sections={1:'pp',5:'p',8:'pp',9:'pp'},lower_sections={1:'pp',5:'p',8:'pp'},words={1:'dolce',12:'poco rit.'},slurs=[],lower_phrases=[],voice_phrases=[dict(voice=v,start_beat=a,end_beat=b,swell=s) for v in ['inner','tenor'] for a,b,s in [(0,15,3),(16,31,4),(32,46,2)]],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*4,i*4+(2.8 if i in [3,7] else 1.8 if i==11 else 3.8)] for i in range(13)],
 performance=dict(rubato=[50,49,48,42,53,52,50,42,49,47,44,36,27],phrase_arcs=[[0,15,0],[16,31,1],[32,46,0],[48,52,-1]],lower_entries=[],inner_entries=[[0,52]],tenor_entries=[[0,52]],pedal_lift=.2,gate=.99,note='The opposing chromatic lines should remain gentle enough that the middle melody stays close. Give the final shared silence its full length.')),
dict(op=198,title='Clover Halfmoon',key='b',fifths=2,meter='5/8',meters=['5/8','5/8','7/8','5/8','5/8','7/8','5/8','5/8','7/8','5/8','5/8','7/8','5/8','5/8','7/8','7/8'],bpm=57,
 description='A light B-minor lullaby alternates short five-eighth bars with longer seven-eighth breaths. In the first four bars, the top of the LH rocking figure rises A–A-sharp–B–C while its B bass and F-sharp remain. The C turns briefly into a dominant flat ninth before the melody opens towards E minor and D major.',
 difficulty='Intermediate to advanced asymmetric sway and chromatic accompaniment',technique_limits=dict(chord_span=12,melodic_leap=12,rapid_leap=7),technical_note='Keep the short bars gentle, with a clear extra quarter beat in each 7/8 bar. The first four LH figures retain the same two opening notes while their third note rises by semitone. The longer bars leave space before the next phrase.',
 parent_opus=192,motif=dict(hand='rh',start_beat=0,end_beat=2.5,pitches=['B','D','C#','F#']),ancestry=dict(source_opus=192,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['E','G','F#','B'],transposition_semitones=7),
 system_starts=[1,4,7,10,13,15],page_starts=[10],engraving=dict(spacing_system=16,pedal_offset_y=520),
 rh='''
B4:.5 D5:.5 C#5:.5 F#5:1
E5:1 D5:.5 C#5:1
B4:1 D5:.5 F#5:1 E5:.5 D5:.5
F#4+A4+D#5:1.5 E5:1
G4:1 B4:.5 D5:1
C#5:1 B4:.5 A4:1 G4:.5 R:.5
F#4:1 A4:.5 C#5:1
B4:1 D5:.5 E5:1
C#5:1 A4:.5 F#4:1 E4:.5 R:.5
B4:.5 D5:.5 C#5:.5 F#5:1
E5:1 D5:.5 B4:1
C#5:1 E5:.5 D5:1 B4:.5 R:.5
A4:1 F#4:.5 E4:1
G4:1 B4:.5 A4:1
F#4:1 A4:.5 C#5:1 B4:.5 R:.5
E4+F#4+A4+C#5:3.5
''',lh='''
B2:1 F#3:.5 A3:1
B2:1 F#3:.5 A#3:1
B2:1 F#3:.5 B3:2
B2:1 F#3:.5 C4:1
E3:1 B3:.5 G3:1
F#3:1 A3:.5 C#4:1 B3:.5 R:.5
D3:1 A3:.5 F#3:1
G3:1 B3:.5 D4:1
A3:1 E3:.5 G3:1 C#3:.5 R:.5
B2:1 F#3:.5 A3:1
G3:1 B3:.5 D4:1
E3:1 B3:.5 G3:1 A3:.5 R:.5
F#3:1 A3:.5 C#4:1
E3:1 B3:.5 G3:1
A3:1 E3:.5 G3:1 C#3:.5 R:.5
D3+A3:3.5
''',sections={1:'p',4:'mp',6:'pp',7:'p',9:'pp',10:'p',12:'pp'},lower_sections={1:'pp'},words={1:'dolce',15:'poco rit.'},slurs=[(1,6),(7,9),(10,12),(13,16)],lower_phrases=[],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[sum([2.5,2.5,3.5,2.5,2.5,3.5,2.5,2.5,3.5,2.5,2.5,3.5,2.5,2.5,3.5,3.5][:i]),sum([2.5,2.5,3.5,2.5,2.5,3.5,2.5,2.5,3.5,2.5,2.5,3.5,2.5,2.5,3.5,3.5][:i])+n-(.7 if i in [5,8,11,14] else .2)] for i,n in enumerate([2.5,2.5,3.5,2.5,2.5,3.5,2.5,2.5,3.5,2.5,2.5,3.5,2.5,2.5,3.5,3.5])],
 performance=dict(rubato=[57,56,54,58,55,47,57,56,46,55,54,46,49,46,39,28],phrase_arcs=[[0,16.5,4],[17,25,3],[25.5,33.5,3],[34,46,1]],lower_entries=[],pedal_lift=.2,gate=.99,note='The rocking pulse is light enough to accommodate the unequal bars. The chromatic ascent in the accompaniment leans briefly into tension and then releases into the relative major.')),
dict(op=199,title='Pearl Nightmargin',key='Eb',fifths=-3,meter='4/4',bpm=51,
 description='A sparse lullaby leaves a high G suspended across three bars while the lower chord changes only its bass, E-flat–E–F. The held note becomes the third of E-flat, the minor third of E half-diminished and the ninth above F. Shorter descending phrases lead back to E-flat with a luminous major ninth.',
 difficulty='Intermediate to advanced long ties and harmonic listening',technique_limits=dict(chord_span=12,melodic_leap=12,rapid_leap=7),technical_note='The high G in bars 2–4 is one continuous twelve-beat note, not three attacks. Change the pedal at each lower harmony without restriking it. The LH retains B-flat and D while only its lowest note rises; shared rests later clear the resonance.',
 parent_opus=194,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['G','Bb','A','D']),ancestry=dict(source_opus=194,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=5,source_pitches=['G','Bb','A','D'],transposition_semitones=0),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=16,pedal_offset_y=520),
 rh='''
G4:1 Bb4:.5 A4:.5 D5:2
G5:4~
G5:4~
G5:4
F5:2 Eb5:1 R:1
D5:1 F5:.5 E5:.5 A4:2
C5:1 E5:.5 D5:.5 G4:2
Bb4:1 D5:.5 C5:.5 F4:1 R:1
G4:1 Bb4:.5 A4:.5 D5:2
C5:2 Bb4:1 R:1
A4:1 C5:1 Bb4:1 R:1
G4+Bb4+D5+F5:4
''',lh='''
Eb3+Bb3:4
Eb3+Bb3+D4:4
E3+Bb3+D4:4
F3+Bb3+D4:4
G3+Bb3+D4:3 R:1
F3+A3+C4:4
E3+G3+B3:4
Eb3+G3+Bb3:3 R:1
Ab3+C4+Eb4:4
F3+Ab3+C4:3 R:1
Bb2+F3+Ab3:3 R:1
Eb3+Bb3:4
''',sections={1:'p',2:'pp',6:'p',8:'pp',9:'p',10:'pp'},lower_sections={1:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[(1,5),(6,8),(9,12)],lower_phrases=[],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*4,i*4+(2.8 if i in [4,7,9,10] else 3.8)] for i in range(12)],
 performance=dict(rubato=[51,48,46,43,39,53,50,42,49,43,36,27],phrase_arcs=[[0,19,2],[20,31,3],[32,48,1]],lower_entries=[],pedal_lift=.2,gate=.995,note='The sustained high G is a point of stillness while the bass changes its meaning. Let the short final phrases leave real silence before the closing chord.')),
dict(op=200,title='Velvet Confluence',key='F',fifths=-1,meter='6/8',meters=['6/8']*7+['4/4']*7+['6/8']*7,bpm=66,
 description='For the two-hundredth work, Velvet Estuary’s opening LH phrase D–F–E–A returns exactly one octave higher inside the RH. Seven bars of gentle compound motion open into seven broader chordal bars, where C–B–B-flat changes the upper light over an unchanged lower harmony. The original phrase returns with a different bass before a quiet F-major ninth gathers the voices.',
 difficulty='Advanced inner cantabile, changing metre and chordal transitions',technique_limits=dict(chord_span=12,melodic_leap=12,rapid_leap=7),technical_note='The inner voice at bars 1 and 15 preserves the exact rhythm and octave shape of Velvet Estuary’s opening LH phrase, transposed one octave up. Keep it in front of the upper line. Bars 8–10 alter only the upper note over fixed inner and lower chords. The three seven-bar sections move 6/8–4/4–6/8 without changing the quarter-note unit.',
 parent_opus=2,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=3,pitches=['D','F','E','A']),ancestry=dict(source_opus=2,source_hand='lh',source_start_beat=0,source_end_beat=3,source_pitches=['D','F','E','A'],transposition_semitones=0),
 system_starts=[1,4,7,10,13,16,19],page_starts=[10],engraving=dict(spacing_system=16,spacing_staff=20,pedal_offset_y=520),
 rh='''
A4:3
C5:3
B4:3
Bb4:3
A4:3
Ab4:3
G4:2 R:1
C5:4
B4:4
Bb4:4
A4:4
Ab4:4
G4:4
A4:3 R:1
A4:3
C5:3
B4:3
Bb4:3
A4:2 R:1
G4:3
E5:3
''',rh_inner='''
D4:.5 F4:.5 E4:.5 A3:1.5
F4:1 G4:.5 A4:1.5
E4:1 G4:.5 F#4:.5 E4:1
D4:1 F4:.5 E4:.5 D4:1
C4:1 E4:.5 G4:1.5
C4:1 Eb4:.5 F4:1.5
B3:1 D4:.5 F4:.5 R:1
E4+G4:4
E4+G4:4
E4+G4:4
F4:1 E4:1 D4:2
C4:1 Eb4:1 F4:1 Eb4:1
D4+F4:4
E4+G4:3 R:1
D4:.5 F4:.5 E4:.5 A3:1.5
F4:1 A4:.5 G4:.5 E4:1
F4:1 A4:.5 G4:.5 F4:1
E4:1 G4:.5 F4:.5 D4:1
F4:1 E4:.5 D4:.5 R:1
C4:1 E4:.5 F4:.5 E4:1
G4+A4+C5:3
''',lh='''
D3:1.5 F3:1.5
Bb2:1.5 F3+A3:1.5
C3:1.5 E3+G3:1.5
B2:1.5 D3+F3:1.5
Bb2:1.5 E3+G3:1.5
Ab2:1.5 C3+Eb3:1.5
G2:1 B2+F3:1 R:1
C3+G3:4
C3+G3:4
C3+G3:4
D3+A3:2 F3+A3:2
Db3+Ab3:2 F3+Ab3:2
C3+G3:2 E3+Bb3:2
A2+E3:1.5 G3+C#4:1.5 R:1
Bb2:1.5 D3+F3:1.5
D3:1.5 F3+A3:1.5
G3:1.5 B3+D4:1.5
C3:1.5 E3+Bb3:1.5
D3+A3:2 R:1
Bb2+F3:1.5 C3+G3:1.5
F3+C4:3
''',sections={1:'p',5:'pp',8:'p',11:'mp',14:'pp',15:'p',19:'pp'},lower_sections={1:'pp'},words={1:'cantabile',19:'poco rit.'},slurs=[],lower_phrases=[],voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=s) for a,b,s in [(0,20,4),(21,48,5),(49,63,4),(64,70,1)]],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[sum(([3]*7+[4]*7+[3]*7)[:i])+a,sum(([3]*7+[4]*7+[3]*7)[:i])+b-.2] for i,c in enumerate([[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,2],[0,4],[0,4],[0,4],[0,2,4],[0,2,4],[0,2,4],[0,1.5,3],[0,3],[0,3],[0,3],[0,3],[0,2],[0,1.5,3],[0,3]]) for a,b in zip(c,c[1:])],
 performance=dict(rubato=[66,65,63,61,60,57,49,55,53,51,57,54,50,42,63,61,59,55,46,40,28],phrase_arcs=[[0,20,0],[21,48,1],[49,63,0],[64,70,-1]],inner_entries=[[0,70]],lower_entries=[],pedal_lift=.2,gate=.99,note='The familiar phrase is an intimate recollection within a new piece. Let the broader central chords breathe, then recover the compound sway gently and leave the final ninth open.')),
dict(op=201,title='Fennel Daybreak',key='F',fifths=-1,meter='4/4',bpm=58,
 description='The Second Studies begin with an extended song. D–F–E–A from Velvet Confluence grows into a nine-bar melody, passes through a D-flat shadow and a fuller rising passage, then returns over a changed bass. A slowed recollection of the four notes leads to a plain F-major triad.',
 difficulty='Intermediate to advanced extended cantabile and changing harmonic fields',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=7),technical_note='Shape the nine-bar opening as one song. The opening three-bar melody returns in bars 24–26 over new bass notes. The central rise reaches C6 briefly; release the bass before its larger slow returns. The final D–F–E–A is stretched over two bars before the simple triad.',
 parent_opus=200,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','F','E','A']),ancestry=dict(source_opus=200,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=3,source_pitches=['D','F','E','A'],transposition_semitones=0),
 system_starts=list(range(1,37,3)),page_starts=[10,19,28],engraving=dict(spacing_system=16,pedal_offset_y=520),
 rh='''
D5:1 F5:.5 E5:.5 A4:2
C5:1 D5:.5 G5:1 F5:.5 E5:1
D5:2 C5:.5 A4:.5 G4:1
F4:1 A4:.5 C5:.5 D5:2~
D5:1 E5:1 F5:.5 A5:.5 G5:1
F5:1 E5:.5 D5:.5 C5:1 A4:1
Bb4:1 D5:.5 F5:1 E5:.5 C5:1
A4:1 C5:.5 B4:.5 D5:1 C5:1
A4:2 G4:1 R:1
Bb4:1 Db5:.5 F5:.5 Ab5:2
Gb5:1 F5:.5 Eb5:.5 Db5:2
C5:1 Eb5:.5 Gb5:.5 F5:1 D5:1
Eb5:2 D5:.5 C5:.5 G4:1
Ab4:1 C5:.5 Eb5:1 D5:.5 Bb4:1
A4:1 C5:.5 E5:.5 G5:2
F5:1 E5:.5 D5:.5 Bb4:1 A4:1
G4:2 A4:1 R:1
A4+C5+F5:1 G5:.5 A5:.5 C6:1 A5:1
G5:1 F5:.5 E5:.5 D5:1 C5:1
D5+F5+A5:2 G5:.5 F5:.5 E5:1
C5+E5+G5:1 A5:.5 G5:.5 F5:1 D5:1
Bb4+D5+F5:1 E5:.5 D5:.5 C5:1 A4:1
G4+Bb4+E5:2 A4+C5+F5:1 R:1
D5:1 F5:.5 E5:.5 A4:2
C5:1 D5:.5 G5:1 F5:.5 E5:1
D5:2 C5:.5 A4:.5 G4:1
F4:1 A4:.5 C5:.5 D5:2~
D5:1 Eb5:.5 D5:.5 C5:1 Ab4:1
G4:1 Bb4:.5 D5:1 C5:.5 A4:1
Bb4:1 A4:.5 F4:.5 E4:1 G4:1
A4:1 C5:.5 D5:.5 C5:1 G4:1
F4:2 A4:1 R:1
D4:2 F4:2
E4:2 A4:2
G4:1 E4:1 C4:1 R:1
F4+A4+C5:4
''',lh='''
D3:1 A3:1 F3+C4:2
F3:1 C4:1 A3:2
Bb2:1 F3:1 A3+C4:2
G3:1 D4:1 Bb3:2
C3:1 G3:1 E3+Bb3:2
F3:1 A3:1 C4:1 E3:1
Bb2:1 F3:1 D3+A3:2
G3:1 B3:1 D4:1 C3:1
F3:1 A3+C4:2 R:1
Bb2:1 F3:1 Ab3+Db4:2
Gb3:1 Bb3:1 Db4:1 Ab3:1
F3:1 C4:1 A3+Eb4:2
C3:1 G3:1 Bb3+Eb4:2
Ab2:1 Eb3:1 G3+C4:2
A2:1 E3:1 G3+C4:2
D3:1 A3:1 F3+C4:2
C3:1 E3+Bb3:2 R:1
F3:1 A3+C4:1 E3:1 G3+C4:1
E3:1 G3+B3:1 C3:1 E3+B3:1
D3:1 A3:1 F3+C4:2
C3:1 G3:1 E3+Bb3:2
Bb2:1 F3:1 D3+A3:2
C3:1 E3+Bb3:1 F3+A3:1 R:1
Bb2:1 F3:1 D3+A3:2
A2:1 E3:1 G3+C4:2
Ab2:1 Eb3:1 G3+C4:2
G3:1 D4:1 Bb3:2
F3:1 Ab3:1 C4:1 Eb3:1
Eb3:1 Bb3:1 G3:1 C3:1
D3:1 A3:1 C3:1 G3:1
Bb2:1 F3:1 C3:1 E3+Bb3:1
F3:1 A3+C4:2 R:1
Bb2+F3:2 D3+A3:2
C3+G3:2 E3+Bb3:2
Bb2+F3:2 C3:1 R:1
F2+C3:4
''',sections={1:'p',7:'pp',10:'mp',14:'p',18:'mf',21:'mp',23:'pp',24:'p',30:'pp'},lower_sections={1:'pp',10:'p',18:'mp',23:'pp'},words={1:'cantabile',33:'poco rit.'},slurs=[(1,9),(10,17),(18,23),(24,32),(33,36)],lower_phrases=[],hairpins=[('crescendo',18,20),('diminuendo',21,23)],tempo_changes={},group=3,
 pedal_spans=[[i*4+a,i*4+b-.2] for i,c in enumerate([[0,4]]*8+[[0,3]]+[[0,4]]*7+[[0,3]]+[[0,2,4]]*5+[[0,2,3]]+[[0,4]]*8+[[0,3]]+[[0,2,4],[0,2,4],[0,2,3],[0,4]]) for a,b in zip(c,c[1:])],
 performance=dict(rubato=[58,60,58,57,60,59,57,55,47,57,56,58,55,57,59,55,47,62,61,63,60,56,46,57,58,55,54,53,52,50,47,42,40,37,33,25],phrase_arcs=[[0,35,5],[36,67,5],[68,91,6],[92,127,4],[128,144,0]],lower_entries=[],pedal_lift=.2,gate=.99,note='The longer arc moves from a close song through darker colour into daylight, then comes home. Preserve the natural breathing points and the quiet plainness of the final triad.')),
dict(op=202,title='Clover Sunshower',key='g',fifths=-2,meter='3/4',meters=['3/4','3/4','5/4','3/4','4/4']*8,bpm=64,
 description='A gently restless dance keeps changing the length of its breath. The G–B-flat–A–D thought inherited from Clover Halfmoon opens into ten-bar spans, moves towards E-flat daylight, grows into offbeat chords, and returns over a new bass. Its final colour falls away to bare G octaves.',
 difficulty='Advanced asymmetric dance phrases and offbeat chord attacks',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=7),technical_note='The five-bar pattern is 3/4, 3/4, 5/4, 3/4, 4/4. Keep a continuous quarter-note pulse through these changes. The middle section separates short chord attacks from the moving melody; the first five-bar tune returns in bars 31–35 with altered bass harmony. Allow the last shared rest before the open octaves.',
 parent_opus=198,motif=dict(hand='rh',start_beat=.5,end_beat=3,pitches=['G','Bb','A','D']),ancestry=dict(source_opus=198,source_hand='rh',source_start_beat=0,source_end_beat=2.5,source_pitches=['B','D','C#','F#'],transposition_semitones=-4),
 system_starts=[1,4,6,9,11,14,16,19,21,24,26,29,31,34,36,39],page_starts=[11,21,31],engraving=dict(spacing_system=14,pedal_offset_y=520),
 rh='''
R:.5 G4:.5 Bb4:.5 A4:.5 D5:1
C5:1 Bb4:.5 A4:.5 G4:1
F4:1 A4:.5 C5:.5 D5:1 F5:1 Eb5:1
D5:1 C5:.5 Bb4:.5 A4:1
G4:1 Bb4:.5 D5:.5 C5:1 R:1
R:.5 Bb4:.5 D5:.5 C5:.5 F5:1
Eb5:1 D5:.5 C5:.5 Bb4:1
A4:1 C5:.5 Eb5:.5 D5:1 Bb4:1 G4:1
F#4:1 A4:.5 C5:.5 D5:1
Bb4:1 A4:.5 G4:.5 G4+D5:1 R:1
R:.5 G4:.5 Bb4:.5 C5:.5 Eb5:1
D5:1 C5:.5 Bb4:.5 G4:1
Ab4:1 C5:.5 Eb5:.5 G5:1 F5:1 D5:1
C5:1 Bb4:.5 Ab4:.5 G4:1
F4:1 Ab4:.5 C5:.5 Bb4:1 R:1
R:.5 A4:.5 C5:.5 D5:.5 F5:1
Eb5:1 D5:.5 C5:.5 A4:1
Bb4:1 D5:.5 F5:.5 A5:1 G5:1 E5:1
F5:1 Eb5:.5 D5:.5 C5:1
Bb4:1 A4:.5 F4:.5 Eb4+G4:1 R:1
G4+Bb4+D5:.5 R:.5 F5:.5 D5:.5 G5:1
F5:1 D5:.5 Bb4:.5 A4:1
G4+Bb4+Eb5:1 F5:.5 G5:.5 Bb5:1 A5:1 F5:1
E5:1 D5:.5 C5:.5 Bb4:1
A4+C5+F5:1 G5:.5 F5:.5 D5:1 R:1
F4+A4+C5:.5 R:.5 Eb5:.5 C5:.5 F5:1
D5:1 C5:.5 A4:.5 G4:1
Eb4+G4+Bb4:1 C5:.5 D5:.5 F5:1 Eb5:1 C5:1
D5:1 C5:.5 Bb4:.5 A4:1
F#4+A4+C5:1 G4+Bb4+D5:2 R:1
R:.5 G4:.5 Bb4:.5 A4:.5 D5:1
C5:1 Bb4:.5 A4:.5 G4:1
F4:1 A4:.5 C5:.5 D5:1 F5:1 Eb5:1
D5:1 C5:.5 Bb4:.5 A4:1
G4:1 Bb4:.5 D5:.5 C5:1 R:1
Bb4:1 A4:.5 G4:.5 F4:1
Eb4:1 G4:.5 Bb4:.5 A4:1
G4:2 F4:1 Eb4:1 D4:1
F#4:1 A4:1 R:1
G4+G5:4
''',lh='''
G2:1.5 D3+Bb3:1 R:.5
Eb3:1 G3+Bb3:2
F3:1 C4:1 A3:1 Bb3:1 R:1
D3:1 F#3+C4:2
G3:1 Bb3+D4:2 R:1
Bb2:1.5 F3+A3:1 R:.5
C3:1 Eb3+Bb3:2
F3:1 A3:1 C4:1 Eb3:1 R:1
D3:1 F#3+C4:2
G3:1 Bb3+D4:2 R:1
Eb3:1.5 G3+Bb3:1 R:.5
C3:1 G3+Bb3:2
Ab2:1 Eb3:1 G3+C4:1 Bb3:1 R:1
Eb3:1 G3+Bb3:2
F3:1 Ab3+C4:2 R:1
F3:1.5 A3+C4:1 R:.5
A2:1 E3+G3:2
Bb2:1 F3:1 A3+D4:1 C4:1 R:1
C3:1 E3+Bb3:2
F3:1 Ab3+C4:2 R:1
G3:.5 R:.5 Bb3+D4:1 F3:1
Eb3:1 G3+Bb3:2
C3:1 G3:1 Bb3+Eb4:1 D4:1 R:1
A2:1 E3+G3:2
D3:1 F3+A3:2 R:1
F3:.5 R:.5 A3+C4:1 Eb3:1
D3:1 F3+A3:2
Eb3:1 Bb3:1 G3+C4:1 Ab3:1 R:1
D3:1 F#3+C4:2
D3:1 G3+Bb3:2 R:1
Eb3:1.5 G3+Bb3:1 R:.5
F3:1 A3+C4:2
Bb2:1 F3:1 A3+D4:1 C4:1 R:1
B2:1 D3+F3:2
C3:1 Eb3+Bb3:2 R:1
Eb3:1 G3+Bb3:2
C3:1 Eb3+G3:2
Bb2:2 F3:1 Eb3:1 C3:1
D3+F#3:2 R:1
G2+G3:4
''',sections={1:'p',6:'mp',10:'pp',11:'p',16:'mp',20:'pp',21:'mf',26:'mp',30:'pp',31:'p',36:'pp'},lower_sections={1:'pp',16:'p',21:'mp',30:'pp'},words={1:'dolce',36:'poco rit.'},slurs=[(1,5),(6,10),(11,15),(16,20),(21,25),(26,30),(31,35),(36,40)],lower_phrases=[],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[sum(([3,3,5,3,4]*8)[:i]),sum(([3,3,5,3,4]*8)[:i])+n-(1.2 if i%5==4 and i!=39 else 1.2 if i==38 else .7 if i%5==0 else .2)] for i,n in enumerate([3,3,5,3,4]*8)],
 performance=dict(rubato=[64,65,63,62,54,66,65,64,61,53,65,66,64,62,54,67,66,65,62,53,70,68,71,67,57,68,66,65,61,52,63,64,61,59,51,52,49,44,36,27],phrase_arcs=[[.5,17,4],[18.5,35,5],[36.5,53,4],[54.5,71,5],[72,89,6],[90,107,5],[108.5,125,3],[126,144,0]],lower_entries=[],pedal_lift=.2,gate=.98,note='The pulse remains light through changes in bar length. Let the fuller middle passage have more definition, then relax into the familiar tune and the final open octaves.')),
dict(op=203,title='Camellia Refractions',key='F',fifths=-1,meter='5/4',bpm=60,
 description='An eight-bar chord song passes through three variations. Its D–F–E–A top line comes from Camellia Nightfold. The first variation changes bass and spacing, the second lifts the song into a brighter octave, and the last stretches its outline into long quiet chords that finish as interlocking open fifths.',
 difficulty='Advanced chord voicing, registral variation and long releases',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),technical_note='Every attack is a chord. Preserve the top-note song in the first three eight-bar sections while the lower voicings and rhythms change. The high second variation reaches F6 briefly; the final section returns to close lower voicings. Strike each chord together and clear every written harmonic change with the pedal.',
 parent_opus=195,motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['D','F','E','A']),ancestry=dict(source_opus=195,source_hand='rh',source_start_beat=0,source_end_beat=7,source_pitches=['D','F','E','A'],transposition_semitones=0),
 system_starts=list(range(1,33,2)),page_starts=[9,17,25],engraving=dict(spacing_system=14,pedal_offset_y=520),
 rh='''
F4+A4+D5:1 A4+C5+F5:1 G4+B4+E5:1 D4+F4+A4:2
E4+G4+C5:2 D4+F4+Bb4:1 C4+E4+G4:2
F4+A4+Bb4:2 E4+G4+A4:1 C4+E4+F4:2
D4+F4+A4:3 C4+E4+G4:1 R:1
Bb3+D4+G4:2 C4+Eb4+Ab4:1 D4+F4+Bb4:2
C4+E4+F4:2 B3+D4+E4:1 C4+E4+F4:2
C4+E4+G4:2 C4+E4+Bb4:1 C4+E4+G4:2
C4+F4+A4:4 R:1
F4+Bb4+D5:1.5 A4+D5+F5:.5 G4+C5+E5:1 E4+G4+A4:2
E4+A4+C5:1.5 D4+G4+Bb4:.5 C4+F4+G4:3
F4+Ab4+Bb4:1.5 E4+G4+A4:.5 C4+Eb4+F4:3
D4+G4+A4:3 C4+F4+G4:1 R:1
Bb3+Eb4+G4:1.5 C4+F4+Ab4:.5 D4+G4+Bb4:3
C4+Eb4+F4:1.5 B3+D4+E4:.5 C4+D4+F4:3
C4+F4+G4:1.5 D4+G4+Bb4:.5 C4+E4+G4:3
C4+F4+A4:3 R:2
F5+A5+D6:1 A5+C6+F6:1 G5+B5+E6:1 D5+F5+A5:2
E5+G5+C6:2 D5+F5+Bb5:1 C5+E5+G5:2
F5+A5+Bb5:2 E5+G5+A5:1 C5+E5+F5:2
D5+F5+A5:3 C5+E5+G5:1 R:1
Bb4+D5+G5:2 C5+Eb5+Ab5:1 D5+F5+Bb5:2
C5+E5+F5:2 B4+D5+E5:1 C5+E5+F5:2
C5+E5+G5:2 C5+E5+Bb5:1 C5+E5+G5:2
C5+F5+A5:3 R:2
F4+A4+D5:5
E4+G4+C5:5
D4+F4+Bb4:5
C4+E4+A4:4 R:1
Bb3+D4+G4:5
A3+C4+F4:5
G3+C4+E4:3 R:2
G3+D4:5
''',lh='''
D3+F3+A3:1 F3+A3+C4:1 E3+G3+B3:1 D3+F3+A3:2
C3+E3+G3:2 Bb2+D3+F3:1 C3+E3+G3:2
Bb2+D3+F3:2 A2+C3+E3:1 F2+A2+C3:2
D3+F3+A3:3 C3+E3+Bb3:1 R:1
G2+Bb2+D3:2 Ab2+C3+Eb3:1 Bb2+D3+F3:2
F2+A2+C3:2 Eb2+G2+Bb2:1 F2+A2+C3:2
C3+E3+G3:2 C3+E3+Bb3:1 C3+E3+G3:2
F2+A2+C3:4 R:1
Bb2+F3+A3:1.5 D3+A3+C4:.5 C3+G3+Bb3:1 F3+A3+C4:2
A2+E3+G3:1.5 G2+D3+F3:.5 F2+C3+E3:3
Ab2+Eb3+G3:1.5 A2+E3+G3:.5 Db3+Ab3:3
G2+D3+F3:3 C3+G3+Bb3:1 R:1
Eb2+Bb2+D3:1.5 F2+C3+Eb3:.5 G2+D3+F3:3
Db3+F3+Ab3:1.5 C3+E3+G3:.5 Bb2+D3+F3:3
F2+C3+Eb3:1.5 G2+D3+F3:.5 C3+E3+Bb3:3
F2+A2+C3:3 R:2
D3+F3+A3:1 F3+A3+C4:1 E3+G3+B3:1 D3+F3+A3:2
C3+E3+G3:2 Bb2+D3+F3:1 C3+E3+G3:2
Bb2+D3+F3:2 A2+C3+E3:1 F2+A2+C3:2
D3+F3+A3:3 C3+E3+Bb3:1 R:1
G2+Bb2+D3:2 Ab2+C3+Eb3:1 Bb2+D3+F3:2
F2+A2+C3:2 Eb2+G2+Bb2:1 F2+A2+C3:2
C3+E3+G3:2 C3+E3+Bb3:1 C3+E3+G3:2
F2+A2+C3:3 R:2
Bb2+D3+F3:5
A2+C3+E3:5
Ab2+C3+Eb3:5
G2+B2+D3:4 R:1
Eb2+G2+Bb2:5
D2+F2+A2:5
C2+G2+B2:3 R:2
F2+C3:5
''',sections={1:'p',5:'pp',9:'mp',13:'p',17:'mf',21:'mp',24:'pp',25:'p',29:'pp'},lower_sections={1:'pp',9:'p',17:'mp',24:'pp'},words={1:'dolce',29:'poco rit.'},slurs=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32)],lower_phrases=[],hairpins=[],tempo_changes={},group=2,
 pedal_spans=[[i*5+a,i*5+b-.2] for i,c in enumerate([[0,1,2,3,5],[0,2,3,5],[0,2,3,5],[0,3,4],[0,2,3,5],[0,2,3,5],[0,2,3,5],[0,4],[0,1.5,2,3,5],[0,1.5,2,5],[0,1.5,2,5],[0,3,4],[0,1.5,2,5],[0,1.5,2,5],[0,1.5,2,5],[0,3],[0,1,2,3,5],[0,2,3,5],[0,2,3,5],[0,3,4],[0,2,3,5],[0,2,3,5],[0,2,3,5],[0,3],[0,5],[0,5],[0,5],[0,4],[0,5],[0,5],[0,3],[0,5]]) for a,b in zip(c,c[1:])],
 performance=dict(rubato=[60,59,58,51,58,57,55,48,61,60,59,52,59,58,55,47,64,63,62,54,61,59,56,46,53,51,49,43,44,40,35,27],phrase_arcs=[[0,19,4],[20,39,3],[40,59,5],[60,78,4],[80,99,5],[100,118,3],[120,139,2],[140,160,0]],lower_entries=[],pedal_lift=.2,gate=.99,note='The same top-line song changes its setting and register, then becomes an outline. The final fifths retain space for the listener rather than completing a familiar jazz cadence.')),
dict(op=204,title='Fennel Parallax',key='e',fifths=1,meter='3/2',bpm=62,
 description='Two independent songs meet across a wide, quiet space. The E–G–F-sharp–B thought from Fennel Daybreak is answered two octaves below, with the hands breathing at different points. The lines wander through brighter C and A harmonies before a compressed exchange; the left hand eventually falls silent and the upper song finishes alone.',
 difficulty='Intermediate to advanced spacious two-part counterpoint',technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=7),technical_note='Hear the half-note pulse beneath the independent phrases. The lower voice enters in bar 3 with the opening four notes two octaves below. Phrase ends are deliberately staggered; bars 7, 14, 21 and 27 finally let both hands breathe. Let the final upper voice continue without filling its space with bass notes.',
 parent_opus=201,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['E','G','F#','B']),ancestry=dict(source_opus=201,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=2),
 system_starts=[1,4,7,10,13,16,19,22,25,28],page_starts=[10,19,25],engraving=dict(spacing_system=17,pedal_offset_y=520),
 rh='''
E5:2 G5:1 F#5:1 B4:2
A4:3 C5:1 B4:2
G4:2 B4:2 D5:2
E5:3 D5:1 C5:2
B4:2 A4:1 G4:1 F#4:2
G4:3 E4:2 R:1
R:6
G4:2 B4:1 A4:1 D5:2
E5:3 D5:1 B4:2
C5:2 E5:2 G5:2
F#5:3 E5:1 D5:2
C5:2 B4:1 A4:1 G4:2
A4:3 F#4:2 R:1
R:6
B4:1 D5:1 C#5:1 F#5:3
E5:2 C#5:1 B4:1 A4:2
G#4:3 B4:1 E5:2
D5:2 F#5:1 E5:1 B4:2
C5:3 A4:1 G4:2
F#4:2 A4:1 G4:1 E4:1 R:1
R:6
E5:1 G5:.5 F#5:.5 B4:2 A4:2
G4:2 B4:1 D5:1 E5:2
C5:3 B4:1 A4:2
G4:2 F#4:1 E4:1 D4:2
E4:2 G4:2 F#4:1 R:1
R:6
B4:2 A4:2 G4:2
F#4:3 E4:2 R:1
E4:6
''',lh='''
R:6
R:6
E3:2 G3:1 F#3:1 B2:2
C3:3 E3:1 A3:2
G3:2 F#3:2 D3:2
E3:2 B2:2 C3:2
B2:3 E3:2 R:1
R:6
C3:2 E3:1 D3:1 G3:2
A3:3 G3:1 E3:2
D3:2 F#3:2 B3:2
A3:3 G3:1 E3:2
F#3:2 D3:2 B2:2
E3:3 C3:2 R:1
R:6
A2:2 C#3:1 B2:1 E3:2
E3:3 D3:1 C3:2
B2:2 D3:2 G3:2
A3:2 C4:1 B3:1 E3:2
D3:3 C3:1 B2:2
E3:3 G3:2 R:1
R:6
E3:1 G3:.5 F#3:.5 B2:2 C3:2
A2:3 C3:1 E3:2
E3:2 D3:2 B2:2
C3:3 A2:2 R:1
B2:2 E3:2 R:2
E3:3 B2:2 R:1
R:6
R:6
''',sections={1:'p',8:'p',15:'mp',18:'p',22:'mp',25:'pp'},lower_sections={1:'pp',3:'p',9:'p',16:'mp',20:'p',26:'pp'},words={1:'cantabile',28:'poco rit.'},slurs=[(1,6),(8,13),(15,20),(22,26),(28,30)],lower_phrases=[(3,7),(9,14),(16,21),(23,27)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*6+a,i*6+b-.25] for i,cut in enumerate([6,6,6,6,6,5,5,6,6,6,6,6,5,5,6,6,6,6,6,6,5,6,6,6,6,5,4,6,5,6]) for a,b in zip([0,2,4],[2,4,min(6,cut)]) if b>a],
 performance=dict(rubato=[60,61,62,63,61,56,50,62,64,65,63,60,55,49,65,66,64,63,60,55,48,62,61,59,56,53,47,45,39,29],phrase_arcs=[[0,35,3],[42,77,4],[84,119,4],[126,155,3],[162,180,0]],lower_entries=[[12,41],[48,83],[90,125],[132,160]],pedal_lift=.25,gate=.99,note='The lower entries should be heard as replies, never as an accompaniment pattern. Preserve the separate phrase endings and the moments when both voices finally release. The last two bars belong to a solitary upper voice.')),
dict(op=205,title='Willow Iridescence',key='a',fifths=0,meter='6/4',bpm=62,
 description='A small A–C–B–E thought from Fennel Parallax gradually changes its surroundings. Spacious melody gains a flowing left hand, then the movement passes upward while the bass becomes still. Broad chords emerge from the moving line and gather into an A-major arrival, retaining their light rather than fading away.',
 difficulty='Advanced evolving textures, flowing eighths and resonant chord arrivals',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),technical_note='The texture develops continuously through four six-bar spans and a four-bar arrival. Give the eighth-note patterns a half-note destination rather than an equal accent on every note. The line migrates from the LH into the RH in bar 13. Keep the final major-key chords full and warm; the ending broadens without diminishing to silence.',
 parent_opus=204,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['A','C','B','E']),ancestry=dict(source_opus=204,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['E','G','F#','B'],transposition_semitones=5),
 system_starts=[1,3,5,7,9,11,13,15,17,19,21,23,25,27],page_starts=[7,13,19,25],engraving=dict(spacing_system=16,pedal_offset_y=520),
 rh='''
A4:2 C5:1 B4:1 E5:2
D5:3 C5:1 A4:2
G4:2 B4:1 D5:1 F5:2
E5:3 D5:1 B4:2
C5:2 E5:1 D5:1 G5:2
F5:2 E5:1 C5:1 B4:1 R:1
A4:1 C5:.5 B4:.5 E5:2 D5:2
C5:2 E5:1 G5:1 F5:2
E5:1 D5:1 B4:2 G4:2
A4:2 C5:1 E5:1 D5:2
F5:2 A5:1 G5:1 E5:2
D5:2 C5:1 B4:1 A4:1 R:1
A4:.5 C5:.5 E5:.5 B4:.5 D5:.5 E5:.5 G5:1 F5:1 E5:1
D5:.5 F5:.5 A5:.5 E5:.5 G5:.5 A5:.5 C6:1 B5:1 G5:1
E5:.5 G5:.5 B5:.5 F#5:.5 A5:.5 B5:.5 D6:1 C6:1 A5:1
F5:.5 A5:.5 C6:.5 G5:.5 B5:.5 C6:.5 E6:1 D6:1 B5:1
G5:.5 B5:.5 D6:.5 A5:.5 C6:.5 D6:.5 F6:1 E6:1 C6:1
D6:1 B5:1 G5:1 E5:1 D5:1 R:1
E5+G5+C6:2 B5:1 A5:1 D5+F5+A5:2
C5+E5+G5:3 A5:1 C5+F5+A5:2
D5+F5+Bb5:2 A5:1 G5:1 C5+E5+G5:2
B4+D5+F#5:2 G5:1 A5:1 C#5+E5+A5:2
C5+E5+G5:2 F5:1 E5:1 B4+D5+F#5:2
C5+E5+A5:3 B4+D5+G5:2 R:1
A4+C#5+E5:2 B4+D5+F#5:2 C#5+E5+A5:2
D5+F#5+B5:2 C#5+E5+A5:2 B4+D5+G#5:2
C#5+E5+A5:2 D5+F#5+B5:2 E5+G#5+B5:1 R:1
C#5+E5+A5:6
''',lh='''
A2+E3:4 G3:2
F3+C4:3 E3+B3:3
E3+B3:4 D3+A3:2
C3+G3:3 B2+F#3:3
A2+E3:2 G3:2 C3+G3:2
D3+A3:2 E3+B3:3 R:1
A2:.5 E3:.5 A3:.5 B3:.5 C4:1 B3:1 G3:1 E3:1
F3:.5 A3:.5 C4:.5 D4:.5 E4:1 D4:1 C4:1 A3:1
E3:.5 G3:.5 B3:.5 D4:.5 E4:1 D4:1 B3:1 G3:1
D3:.5 A3:.5 C4:.5 E4:.5 F4:1 E4:1 C4:1 A3:1
F3:.5 A3:.5 C4:.5 E4:.5 F4:1 E4:1 C4:1 A3:1
E3:.5 B3:.5 D4:.5 E4:.5 G4:1 E4:1 B3:1 R:1
A2+E3:3 G3+C4:3
D3+A3:3 F3+C4:3
E3+B3:3 G3+D4:3
F3+C4:3 A3+E4:3
G3+D4:3 B3+F4:3
E3+B3:3 G3+D4:2 R:1
C3+G3:2 E3+B3:2 D3+A3:2
A2+E3:3 F3+C4:3
Bb2+F3:2 D3+A3:2 C3+G3:2
G2+D3:2 B2+F#3:2 A2+E3:2
C3+G3:2 A2+E3:2 B2+F#3:2
F3+C4:3 E3+B3:2 R:1
A2+E3:2 B2+F#3:2 C#3+G#3:2
D3+A3:2 C#3+G#3:2 E3+B3:2
A2+E3:2 D3+A3:2 E3+B3:1 R:1
A2+E3+A3:6
''',sections={1:'pp',5:'p',7:'p',11:'mp',13:'mp',16:'mf',19:'mf',23:'mp',25:'mf'},lower_sections={1:'pp',7:'p',11:'mp',13:'p',19:'mp',25:'mf'},words={1:'dolce',25:'poco rit.'},slurs=[(1,6),(7,12),(13,18),(19,24),(25,28)],lower_phrases=[(7,12)],hairpins=[('crescendo',13,17)],tempo_changes={},group=3,
 pedal_spans=[[i*6+a,i*6+b-.2] for i,c in enumerate([[0,4,6],[0,3,6],[0,4,6],[0,3,6],[0,2,4,6],[0,2,5]]+[[0,2,4,6]]*5+[[0,2,4,5]]+[[0,3,6]]*5+[[0,3,5]]+[[0,2,4,6],[0,3,6],[0,2,4,6],[0,2,4,6],[0,2,4,6],[0,3,5]]+[[0,2,4,6]]*2+[[0,2,4,5],[0,6]]) for a,b in zip(c,c[1:])],
 performance=dict(rubato=[60,59,61,60,62,54,64,66,65,67,68,57,70,72,74,75,76,61,66,64,65,63,61,54,56,53,48,38],phrase_arcs=[[0,35,4],[36,71,5],[72,107,6],[108,143,5],[144,168,2]],lower_entries=[[36,71]],pedal_lift=.2,gate=.99,note='Allow the half-note pulse to gather momentum as the figuration moves between the hands. A broader sound replaces the moving notes; the final four bars keep their brightness and forward intention even as the pulse expands.'))
]
