"""Explicit Second Studies compositions, continuing the CWS opus sequence."""

PIECES = [
dict(op=217,title='Juniper Passage',key='d',fifths=-1,meter='9/8',bpm=61,
 description='A descending tune leans into a long-short lilt. Its companion figures gradually become unbroken eighths, then gather into gently displaced chords. The route passes through F minor and D-flat before the original melody returns; the final resting place is a B-flat sixth and ninth.',
 difficulty='Advanced compound-metre lilt and chord voicing',technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=7),technical_note='The written quarter and eighth form a two-to-one lilt within each dotted-quarter beat. Bars 9–16 use continuous LH eighths, while the last eight bars turn the tune into chordal phrases. Keep the top notes audible through the changed textures.',
 parent_opus=212,motif=dict(hand='rh',start_beat=0,end_beat=4.5,pitches=['D','C','A','G']),ancestry=dict(source_opus=212,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['Bb','Ab','F','Eb'],transposition_semitones=4),
 system_starts=list(range(1,33,2)),page_starts=[9,17,25],engraving=dict(spacing_system=18,spacing_staff=16,pedal_offset_y=560),
 rh='''
D5:1 C5:.5 A4:1.5 G4:1.5
Bb4:1 A4:.5 G4:1 F4:.5 D4:1.5
E4:1 G4:.5 B4:1 A4:.5 G4:1.5
A4:1 C5:.5 E5:1 D5:.5 C5:1.5
D5:1 F5:.5 E5:1 D5:.5 C5:1.5
Bb4:1 G4:.5 Eb4:1 G4:.5 D5:1.5
C5:1 B4:.5 A4:1 G4:.5 E4:1.5
G4:1 Bb4:.5 A4:1.5 R:1.5
D5:1 C5:.5 A4:1.5 G4:1.5
Ab4:1 C5:.5 Eb5:1 D5:.5 C5:1.5
Bb4:1 Ab4:.5 G4:1 F4:.5 C5:1.5
Db5:1 F5:.5 Ab5:1 G5:.5 F5:1.5
E5:1 Db5:.5 Bb4:1 G4:.5 F4:1.5
E4:1 G4:.5 Bb4:1 Db5:.5 C5:1.5
C5:1 A4:.5 G4:1 E4:.5 F4:1.5
E4:1 G4:.5 A4:1.5 R:1.5
D5:1 C5:.5 A4:1.5 G4:1.5
Bb4:1 A4:.5 G4:1 F4:.5 D4:1.5
E4:1 G4:.5 B4:1 A4:.5 G4:1.5
A4:1 C5:.5 E5:1 D5:.5 C5:1.5
D5:.5 F5:.5 A5:.5 G5:1 F5:.5 E5:1.5
Eb5:.5 G5:.5 Bb5:.5 Ab5:1 G5:.5 F5:1.5
E5:.5 G5:.5 A5:.5 C6:1 B5:.5 A5:1.5
G5:1 E5:.5 D5:1.5 R:1.5
F4+A4+D5:1 E4+G4+C5:.5 C4+F4+A4:1.5 Bb3+D4+G4:1.5
D4+F4+Bb4:1 C4+F4+A4:.5 Bb3+D4+G4:1 C4+F4:.5 A3+D4:1.5
C4+G4:1 E4+Bb4:.5 F4+A4:1.5 E4+G4:1.5
F4+A4+C5:1 G4+B4+D5:2 F4+A4+C5:1.5
F4+Bb4+D5:1 G4+C5+E5:.5 A4+D5+F5:1.5 G4+C5+E5:1.5
G4+Bb4+Eb5:1 F4+Ab4+Db5:2 Eb4+G4+C5:1.5
F4+A4+C5:1.5 Eb4+G4+Bb4:1.5 R:1.5
D4+F4+G4+C5:4.5
''',lh='''
D3:1 A3:.5 F3:1 A3:.5 G3:1.5
G2:1 D3:.5 Bb2:1 D3:.5 F3:1.5
C3:1 G3:.5 E3:1 G3:.5 B3:1.5
F3:1 C4:.5 A3:1 C4:.5 F3:1.5
Bb2:1 F3:.5 D3:1 F3:.5 A3:1.5
Eb3:1 Bb3:.5 G3:1 Bb3:.5 F3:1.5
A2:1 E3:.5 C3:1 E3:.5 G3:1.5
A2:1 E3:.5 G3:1.5 R:1.5
D3:.5 F3:.5 A3:.5 C4:.5 A3:.5 F3:.5 E3:.5 F3:.5 A3:.5
F3:.5 Ab3:.5 C4:.5 Eb4:.5 C4:.5 Ab3:.5 G3:.5 Ab3:.5 Eb3:.5
Ab2:.5 C3:.5 Eb3:.5 G3:.5 Eb3:.5 C3:.5 Bb2:.5 C3:.5 Eb3:.5
Db3:.5 F3:.5 Ab3:.5 C4:.5 Ab3:.5 F3:.5 Eb3:.5 F3:.5 Db3:.5
G2:.5 Bb2:.5 Db3:.5 F3:.5 Db3:.5 Bb2:.5 Ab2:.5 Bb2:.5 Db3:.5
C3:.5 E3:.5 G3:.5 Bb3:.5 G3:.5 E3:.5 D3:.5 E3:.5 G3:.5
F3:.5 A3:.5 C4:.5 E4:.5 C4:.5 A3:.5 G3:.5 A3:.5 E3:.5
A2:.5 C3:.5 E3:.5 G3:.5 E3:.5 C3:.5 R:1.5
Bb2:1 F3:.5 D3:1 F3:.5 A3:1.5
Eb3:1 Bb3:.5 G3:1 Bb3:.5 F3:1.5
A2:1 E3:.5 C3:1 E3:.5 G3:1.5
D3:1 A3:.5 F3:1 A3:.5 G3:1.5
Bb2+F3:1.5 D3+A3:1.5 C3+G3:1.5
Eb3+Bb3:1.5 Ab2+Eb3:1.5 Bb2+F3:1.5
A2+E3:1.5 C3+G3:1.5 E3+B3:1.5
A2+E3:1.5 D3+A3:1.5 R:1.5
D3+A3:1.5 C3+G3:1.5 Bb2+F3:1.5
G2+D3:1.5 Bb2+F3:1.5 D3+F3:1.5
C3+G3:1.5 F3+C4:1.5 C3+G3:1.5
F3+C4:1 A2+E3:2 F3+C4:1.5
Bb2+F3:1.5 D3+A3:1.5 C3+G3:1.5
Eb3+Bb3:1 Db3+Ab3:2 C3+G3:1.5
F3+C4:1.5 Eb3+Bb3:1.5 R:1.5
Bb2+F3:4.5
''',sections={1:'p',9:'p',13:'mp',17:'p',21:'mp',25:'p',29:'pp'},lower_sections={1:'pp',9:'pp',17:'pp',21:'p',25:'pp'},words={29:'poco rit.'},slurs=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],lower_phrases=[],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*4.5+a,i*4.5+b-.18] for i in range(32) for a,b in zip(([0] if i==31 else [0,1.5] if i in [7,15,23,30] else [0,1.5,3]),([4.5] if i==31 else [1.5,3] if i in [7,15,23,30] else [1.5,3,4.5]))],
 performance=dict(rubato=[61,62,63,60,63,62,60,52,63,62,61,63,60,61,59,51,61,62,63,60,66,67,65,53,59,58,59,57,55,52,46,34],phrase_arcs=[],lower_entries=[],pedal_lift=.18,gate=.97,note='Let the long-short melody breathe across the dotted beats. The running bass stays soft; the later chords inherit the same supple motion before settling into the B-flat colour.')),
dict(op=218,title='Reed Inversion',key='f',fifths=-4,meter='7/4',bpm=58,
 description='A long melody opens above an ascending bass, loosens into flowing figures, and returns as its own reflection: every upward interval becomes an equal downward one. New harmony makes that reflection sound like another song. The two outlines gradually find a common resting place in A-flat major.',
 difficulty='Advanced long-line phrasing and melodic inversion',technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=7),technical_note='Bars 10–12 are the exact interval inversion of the opening three-bar upper melody around F5, with its rhythm unchanged. Give the reflected phrase its own direction rather than emphasising the device. Later flowing notes should remain lighter than the long phrase notes.',
 parent_opus=213,motif=dict(hand='rh',start_beat=0,end_beat=7,pitches=['F','Ab','G','C']),ancestry=dict(source_opus=213,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=5,source_pitches=['C','Eb','D','G'],transposition_semitones=17),
 system_starts=list(range(1,22,2)),page_starts=[7,13,19],engraving=dict(spacing_system=19,spacing_staff=16,pedal_offset_y=560),
 rh='''
F5:2 Ab5:1 G5:2 C6:2
Bb5:1 Ab5:1 G5:1 F5:2 Eb5:2
D5:2 F5:1 Eb5:2 C5:1 R:1
F5:1 Eb5:.5 F5:.5 Ab5:1 G5:.5 Ab5:.5 G5:1 C6:2
Bb5:.5 Ab5:.5 G5:.5 F5:.5 Eb5:1 G5:1 Ab5:1 C6:2
Bb5:1 Ab5:.5 G5:.5 F5:1 Eb5:2 C5:1 R:1
Db5:2 F5:1 Ab5:2 G5:2
F5:1 Eb5:1 C5:1 Bb4:2 Ab4:2
G4:2 Bb4:1 C5:2 Eb5:1 R:1
F5:2 D5:1 Eb5:2 Bb4:2
C5:1 D5:1 Eb5:1 F5:2 G5:2
Ab5:2 F5:1 G5:2 Bb5:1 R:1
Ab4+C5+F5:3 G4+Bb4+Eb5:2 F4+Ab4+Db5:2
G4+Bb4+Eb5:2 Ab4+C5+F5:1 Bb4+Db5+G5:2 Ab4+C5+F5:2
G4+Bb4+Eb5:2 F4+Ab4+Db5:1 Eb4+G4+C5:3 R:1
F5:1 G5:.5 F5:.5 D5:1 Eb5:.5 F5:.5 Eb5:1 Bb4:2
C5:.5 D5:.5 Eb5:.5 F5:.5 G5:1 Bb5:1 Ab5:1 G5:2
F5:1 Ab5:.5 G5:.5 F5:1 Eb5:2 C5:1 R:1
F5:2 Ab5:1 G5:2 C6:2
Bb5:2 G5:1 F5:2 Eb5:1 R:1
Eb4+Ab4+C5:7
''',lh='''
F2:1 C3:1 F3:1 Ab3:1 C4:1 G3:1 F3:1
Eb3:1 Bb3:1 G3:1 Ab3:1 C4:1 G3:1 Eb3:1
Bb2:1 F3:1 D3:1 F3:1 Ab3:1 F3:1 R:1
F2:1 C3:.5 F3:.5 Ab3:1 C4:1 Ab3:1 G3:1 F3:1
Ab2:1 Eb3:.5 Ab3:.5 C4:1 Eb4:1 C4:1 Bb3:1 Ab3:1
Bb2:1 F3:.5 Bb3:.5 D4:1 Ab3:2 F3:1 R:1
Db3:1 Ab3:1 F3:1 Ab3:1 C4:1 Bb3:1 Ab3:1
Ab2:1 Eb3:1 Ab3:1 C4:1 G3:1 Eb3:1 C3:1
C3:1 G3:1 Bb3:1 E4:1 C4:1 G3:1 R:1
Bb2:1 F3:1 Ab3:1 D4:1 Bb3:1 F3:1 D3:1
C3:1 G3:1 Bb3:1 Eb4:1 C4:1 Bb3:1 G3:1
F3:1 C4:1 Ab3:1 Bb3:1 Db4:1 Bb3:1 R:1
Db3+Ab3:3 Eb3+Bb3:2 F3+C4:2
Eb3+Bb3:2 F3+C4:1 G3+Db4:2 Ab3+C4:2
Bb2+F3:2 Db3+Ab3:1 C3+G3:3 R:1
Bb2:1 F3:.5 Bb3:.5 D4:1 F4:1 D4:1 C4:1 Bb3:1
Eb3:1 Bb3:.5 Eb4:.5 G4:1 F4:1 Eb4:1 Bb3:1 G3:1
Db3:1 Ab3:.5 Db4:.5 F4:1 Eb4:2 C4:1 R:1
Db3+Ab3:3 Eb3+Bb3:2 F3+C4:2
Bb2+F3:2 Eb3+Bb3:1 Ab2+Eb3:3 R:1
C3+Ab3:7
''',sections={1:'p',4:'p',7:'pp',10:'mp',13:'p',16:'mp',19:'p',21:'pp'},lower_sections={1:'pp',4:'pp',10:'pp',13:'p',16:'pp',19:'pp'},words={19:'poco rit.'},slurs=[(1,3),(4,6),(7,9),(10,12),(16,18),(19,20)],lower_phrases=[],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*7+a,i*7+b-.2] for i in range(21) for a,b in zip(([0] if i==20 else [0,3,5]),([7] if i==20 else [3,5,6 if i in [2,5,8,11,14,17,19] else 7]))],
 performance=dict(rubato=[58,59,51,61,63,52,57,56,48,58,60,51,55,57,48,61,62,51,51,45,32],phrase_arcs=[],lower_entries=[],pedal_lift=.2,gate=.99,note='Let the long melody float above the bass. Its mirrored version is a fresh cantabile phrase; the closing return broadens gently into the first-inversion A-flat chord.')),
dict(op=219,title='Pearl Migration',key='b',fifths=2,meter='5/4',bpm=59,
 description='A six-bar melody begins low in the piano, rises two octaves, briefly runs at twice its original pace, and finally appears three octaves above its first home. Each migration changes the accompanying harmony. Soft chords draw the high voice back towards the centre, closing in E major with a lingering ninth.',
 difficulty='Advanced melodic projection across registers and rhythmic diminution',technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=7),technical_note='The entire first six-bar bass phrase returns in RH bars 7–12 two octaves higher, is compressed by half in bars 13–15, and returns three octaves above its original register at 19–24. Keep the running version connected to the same phrase shape, without forcing the high register.',
 parent_opus=214,motif=dict(hand='lh',start_beat=0,end_beat=5,pitches=['B','D','C#','A']),ancestry=dict(source_opus=214,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['E','G','F#','D'],transposition_semitones=-29),
 system_starts=list(range(1,31,2)),page_starts=[7,13,19,25],engraving=dict(spacing_system=18,spacing_staff=15,pedal_offset_y=560),
 rh='''
F#4+A4+C#5:3 E4+G4+B4:2
F#4+A4+B4:3 E4+G4+B4:2
G4+B4+D5:3 F#4+A4+C#5:2
E4+A4+C#5:3 F#4+A4+C#5:2
F#4+B4+D5:3 E4+A4+C#5:2
E4+G4+B4:2 E4+F#4+A4:2 R:1
B4:1 D5:1 C#5:1 A4:2
G4:1 B4:1 F#4:1 A4:2
E4:1 G4:1 B4:1 A4:2
F#4:1 A4:1 C#5:1 E5:2
D5:1 C#5:1 B4:1 A4:2
G4:2 F#4:2 R:1
B4:.5 D5:.5 C#5:.5 A4:1 G4:.5 B4:.5 F#4:.5 A4:1
E4:.5 G4:.5 B4:.5 A4:1 F#4:.5 A4:.5 C#5:.5 E5:1
D5:.5 C#5:.5 B4:.5 A4:1 G4:1 F#4:1 R:.5
G4:.5 B4:.5 D5:.5 F#5:.5 E5:1 D5:1 B4:1
A4:.5 C#5:.5 E5:.5 G5:.5 F#5:1 E5:1 C#5:1
D5:.5 F#5:.5 A5:.5 B5:.5 A5:1 F#5:1 E5:1
B5:1 D6:1 C#6:1 A5:2
G5:1 B5:1 F#5:1 A5:2
E5:1 G5:1 B5:1 A5:2
F#5:1 A5:1 C#6:1 E6:2
D6:1 C#6:1 B5:1 A5:2
G5:2 F#5:2 R:1
F#4+B4:1 A4+D5:1 G4+C#5:1 E4+A4:2
D4+G4:1 G4+B4:1 D4+F#4:1 E4+A4:2
B3+E4:1 D4+G4:1 F#4+B4:1 E4+A4:2
E4+G#4+B4:2 F#4+A4+C#5:1 G4+B4+D5:2
F#4+A4+C#5:2 E4+G#4+B4:2 R:1
D#4+F#4+G#4+B4:5
''',lh='''
B2:1 D3:1 C#3:1 A2:2
G2:1 B2:1 F#2:1 A2:2
E2:1 G2:1 B2:1 A2:2
F#2:1 A2:1 C#3:1 E3:2
D3:1 C#3:1 B2:1 A2:2
G2:2 F#2:2 R:1
G2:1 D3:.5 G3:.5 B3:1 A3:1 G3:1
E3:1 B3:.5 G3:.5 E3:1 F#3:1 G3:1
C3:1 G3:.5 E3:.5 C3:1 D3:1 E3:1
D3:1 A3:.5 F#3:.5 D3:1 E3:1 F#3:1
G2:1 D3:.5 G3:.5 B3:1 A3:1 F#3:1
E3:1 B3:.5 G3:.5 F#3:2 R:1
B2+F#3:2.5 G2+D3:2.5
E3+B3:2.5 F#3+C#4:2.5
G2+D3:2.5 E3+B3:2 R:.5
E3+B3:3 G2+D3:2
A2+E3:3 C#3+G3:2
D3+A3:3 F#3+C#4:2
B2:1 F#3:.5 B3:.5 D4:1 C#4:1 F#3:1
G2:1 D3:.5 G3:.5 B3:1 A3:1 G3:1
E3:1 B3:.5 E4:.5 G4:1 F#4:1 E4:1
F#3:1 C#4:.5 F#4:.5 A4:1 G4:1 F#4:1
G3:1 D4:.5 G4:.5 B4:1 A4:1 D4:1
E3:1 B3:.5 G3:.5 F#3:2 R:1
G2+D3:3 A2+E3:2
B2+F#3:3 A2+E3:2
E2+B2:3 F#2+C#3:2
E3+B3:2 F#3+C#4:1 G3+D4:2
A2+E3:2 B2+F#3:2 R:1
E3+B3:5
''',clef_changes=dict(lh={21:'treble',24:'bass'}),sections={1:'pp',7:'p',13:'p',16:'mp',19:'p',25:'pp'},lower_sections={1:'p',7:'pp',13:'pp',19:'pp',25:'pp'},words={25:'poco rit.'},slurs=[(7,12),(13,15),(16,18),(19,24)],lower_phrases=[(1,6)],hairpins=[],tempo_changes={},group=4,
 pedal_spans=[[i*5+a,i*5+b-.2] for i in range(30) for a,b in zip(([0] if i==29 else [0,2.5] if i in [12,13,14] else [0,3] if i<6 or 24<=i<27 else [0,2]),([5] if i==29 else [2.5,4.5 if i==14 else 5] if i in [12,13,14] else [3,4 if i==5 else 5] if i<6 or 24<=i<27 else [2,4 if i in [11,23,28] else 5]))],
 performance=dict(rubato=[59,60,60,61,58,49,61,62,61,63,60,50,62,63,53,65,66,63,59,60,60,62,59,49,51,50,48,46,41,31],phrase_arcs=[],lower_entries=[[0,29]],pedal_lift=.2,gate=.98,note='Bring the initial bass tune forward. Each higher version recalls its unhurried phrasing, including the half-duration version. Let the last chords ease the ear back into the middle register.')),
dict(op=220,title='Velvet Arrival',key='c',fifths=-3,meter='6/4',bpm=51,
 description='A quiet chordal song opens into a slower, higher recollection, then loosens into a falling line and flowing figures. Its return has the same familiar upper shape with a different bass beneath it. The final E-flat sixth leaves a little air inside the arrival.',
 difficulty='Advanced chordal cantabile, augmentation and register changes',technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=7),technical_note='The opening three RH bars return an octave higher at 7–12 with every duration doubled. The falling single line at 13 connects the high chordal register to the central figuration. Project the top voice in the chordal sections and give the shared rests their full space.',
 parent_opus=215,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Eb','D','C','Bb']),ancestry=dict(source_opus=215,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['Ab','G','F','Eb'],transposition_semitones=7),
 system_starts=list(range(1,25,2)),page_starts=[7,13,19],engraving=dict(spacing_system=19,spacing_staff=16,pedal_offset_y=560),
 rh='''
G4+Bb4+Eb5:1.5 F4+Ab4+D5:1.5 Eb4+G4+C5:1.5 D4+F4+Bb4:1.5
C4+Eb4+Ab4:3 Eb4+G4+C5:3
G4+Bb4+D5:2 F4+Ab4+C5:2 Eb4+G4+Bb4:2
D4+F4+Ab4:3 Eb4+G4+C5:3
F4+Ab4+Db5:2 G4+Bb4+Eb5:1.5 Ab4+C5+F5:2.5
G4+Bb4+Eb5:2 F4+Ab4+D5:2 Eb4+G4+C5:1 R:1
G5+Bb5+Eb6:3 F5+Ab5+D6:3
Eb5+G5+C6:3 D5+F5+Bb5:3
C5+Eb5+Ab5:6
Eb5+G5+C6:6
G5+Bb5+D6:4 F5+Ab5+C6:2~
F5+Ab5+C6:2 Eb5+G5+Bb5:4
Bb5:1 G5:1 Eb5:1 Bb4:1 G4:1 Eb4:1
C4:.5 Eb4:.5 G4:.5 Bb4:.5 D5:.5 C5:.5 Bb4:.5 G4:.5 Eb4:.5 G4:.5 Bb4:.5 C5:.5
Db5:.5 Ab4:.5 F4:.5 Ab4:.5 C5:.5 Eb5:.5 Db5:.5 C5:.5 Ab4:.5 F4:.5 Eb4:.5 Db4:.5
Eb4:.5 G4:.5 Bb4:.5 D5:.5 F5:.5 Eb5:.5 D5:.5 Bb4:.5 G4:.5 Bb4:.5 D5:.5 Eb5:.5
F5:.5 Eb5:.5 C5:.5 Ab4:.5 F4:.5 Ab4:.5 C5:.5 Eb5:.5 F5:2
Eb5:1 D5:1 C5:1 Bb4:2 R:1
G4+Bb4+Eb5:1.5 F4+Ab4+D5:1.5 Eb4+G4+C5:1.5 D4+F4+Bb4:1.5
C4+Eb4+Ab4:3 Eb4+G4+C5:3
G4+Bb4+D5:2 F4+Ab4+C5:2 Eb4+G4+Bb4:2
F4+Ab4+Db5:3 G4+Bb4+Eb5:3
Ab4+C5+F5:2 G4+Bb4+Eb5:2 F4+Ab4+D5:1 R:1
Eb4+G4+C5:6
''',lh='''
C3+G3:1.5 Bb2+F3:1.5 Ab2+Eb3:1.5 G2+D3:1.5
F2+C3:3 Ab2+Eb3:3
Eb3+Bb3:2 Db3+Ab3:2 C3+G3:2
Bb2+F3:3 C3+G3:3
Db3+Ab3:2 Eb3+Bb3:1.5 F3+C4:2.5
Ab2+Eb3:2 Bb2+F3:2 C3+G3:1 R:1
Ab2+Eb3:3 Bb2+F3:3
F3+C4:3 G2+D3:3
Db3+Ab3:3 F3+C4:3
Ab2+Eb3:3 C3+G3:3
Bb2+F3:2 Eb3+Bb3:2 Ab2+Eb3:2
F3+C4:2 Eb3+Bb3:2 C3+G3:2
R:6
C3:3 Bb2:3
Db3:2 Ab3:1 F3:3
Eb3:2 Bb3:1 G3:3
F3:2 C4:1 Ab3:3
Bb2:2 F3:1 Ab3:2 R:1
Ab2+Eb3:1.5 Bb2+F3:1.5 F2+C3:1.5 G2+D3:1.5
Db3+Ab3:3 Ab2+Eb3:3
Bb2+F3:2 F3+C4:2 Eb3+Bb3:2
Db3+Ab3:3 Eb3+Bb3:3
F3+C4:2 Ab2+Eb3:2 Bb2+F3:1 R:1
Eb3+Bb3:6
''',sections={1:'p',7:'pp',13:'pp',14:'p',17:'mp',19:'p',22:'pp'},lower_sections={1:'pp',7:'pp',14:'pp',19:'pp'},words={22:'poco rit.'},slurs=[(13,13),(14,16),(17,18)],lower_phrases=[],hairpins=[],tempo_changes={},group=4,
 pedal_spans=[[i*6+a,i*6+b-.22] for i,cuts in enumerate([[0,1.5,3,4.5,6],[0,3,6],[0,2,4,6],[0,3,6],[0,2,3.5,6],[0,2,4,5],[0,3,6],[0,3,6],[0,3,6],[0,3,6],[0,2,4,6],[0,2,4,6],[0,3,6],[0,3,6],[0,3,6],[0,3,6],[0,3,6],[0,3,5],[0,1.5,3,4.5,6],[0,3,6],[0,2,4,6],[0,3,6],[0,2,4,5],[0,6]]) for a,b in zip(cuts,cuts[1:])],
 performance=dict(rubato=[51,53,52,51,54,46,50,51,49,50,52,48,48,55,56,57,58,47,51,50,49,45,40,29],phrase_arcs=[],lower_entries=[],pedal_lift=.22,gate=.99,note='Allow the opening song to breathe inside its chords. The higher augmentation is distant and soft; the falling line reconnects it with the flowing middle. The return is warmer, and the last chord remains gentle.')),
dict(op=221,title='Clover Filigree',key='d',fifths=-1,meter='4/4',bpm=72,
 description='A song of small rises and falling answers floats above a continuous triplet current. Duple notes gradually appear against it; later the hands exchange their rhythms. A quieter chordal passage opens the centre before the two currents return together and broaden into D major.',
 difficulty='Advanced sustained three-against-two coordination',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Keep triplet eighths even beneath the duple melody in bars 7–12 and 25–30. Bars 19–24 transfer the triplets to RH against LH duple eighths. Neither hand should accent every meeting point. The continuous figures require supple changes of position; the chordal close retains a singing top note.',
 parent_opus=216,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','F','E','A']),ancestry=dict(source_opus=216,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),
 system_starts=list(range(1,37,2)),page_starts=[7,13,19,25,31],engraving=dict(spacing_system=18,spacing_staff=16,pedal_offset_y=560),
 tuplet_spans=[dict(hand=hand,start_beat=i*4+j,end_beat=i*4+j+1,actual=3,normal=2,stem='up' if hand=='lh' else 'down') for hand,bars in [('lh',list(range(12))+list(range(24,30))),('rh',list(range(18,24)))] for i in bars for j in range(3 if i in [5,11,23,29] else 4)],
 rh='''
D5:1 F5:1 E5:1 A5:1
G5:1 E5:1 D5:1 C5:1
Bb4:1 D5:1 F5:1 E5:1
D5:1.5 C5:.5 A4:2
Bb4:1 C5:.5 D5:.5 E5:1 G5:1
F5:1 E5:1 D5:1 R:1
D5:.5 E5:.5 F5:.5 A5:.5 E5:.5 G5:.5 A5:.5 F5:.5
G5:.5 F5:.5 E5:.5 D5:.5 C5:.5 D5:.5 E5:.5 G5:.5
F5:.5 D5:.5 Bb4:.5 C5:.5 D5:.5 F5:.5 E5:.5 D5:.5
C5:.5 A4:.5 G4:.5 A4:.5 C5:.5 E5:.5 D5:.5 C5:.5
Bb4:.5 D5:.5 F5:.5 A5:.5 G5:.5 E5:.5 D5:.5 C5:.5
Bb4:.5 A4:.5 G4:.5 E4:.5 F4:1 R:1
F4+A4+C5:2 G4+Bb4+D5:2
Ab4+C5+Eb5:3 G4+Bb4+D5:1
F4+Ab4+Db5:2 Eb4+G4+C5:2
D4+F4+Bb4:1.5 Eb4+G4+C5:2.5
F4+Ab4+C5:2 E4+G4+B4:2
F4+A4+D5:2 E4+G4+C5:1 R:1
'''+ '\n'.join(' '.join(f'{n}:1/3' if ':' not in n else n for n in row.split()) for row in '''D5 F5 A5 G5 E5 C5 F5 E5 D5 C5 A4 C5
Bb4 D5 F5 A5 F5 D5 G5 F5 E5 D5 Bb4 D5
C5 E5 G5 Bb5 G5 E5 A5 G5 F5 E5 C5 E5
F5 A5 C6 Bb5 G5 E5 A5 F5 D5 F5 E5 C5
D5 F5 A5 G5 E5 C5 F5 D5 Bb4 C5 A4 C5
Bb4 D5 F5 E5 C5 A4 D5 C5 A4 R:1'''.splitlines())+'''
D5:.5 E5:.5 F5:.5 A5:.5 E5:.5 G5:.5 A5:.5 F5:.5
G5:.5 F5:.5 E5:.5 D5:.5 C5:.5 D5:.5 E5:.5 G5:.5
F5:.5 D5:.5 Bb4:.5 C5:.5 D5:.5 F5:.5 E5:.5 D5:.5
C5:.5 Eb5:.5 G5:.5 Bb5:.5 A5:.5 G5:.5 F5:.5 Eb5:.5
D5:.5 F5:.5 A5:.5 C6:.5 B5:.5 A5:.5 G5:.5 E5:.5
F5:.5 E5:.5 D5:.5 C5:.5 A4:1 R:1
F4+A4+D5:2 G4+Bb4+E5:2
A4+C5+F5:2 G4+B4+E5:2
F4+A4+D5:2 E4+G4+C5:2
D4+F#4+B4:2 E4+G4+C#5:2
E4+G4+C#5:2 F#4+A4+D5:1 R:1
F#4+A4+C#5+E5:4
''',lh='\n'.join(' '.join(f'{n}:1/3' if ':' not in n else n for n in row.split()) for row in '''D3 F3 A3 C4 A3 F3 E3 F3 A3 G3 E3 C3
C3 E3 G3 B3 G3 E3 D3 E3 G3 F3 D3 Bb2
Bb2 D3 F3 A3 F3 D3 C3 D3 F3 E3 C3 A2
A2 C3 E3 G3 E3 C3 B2 C3 E3 F3 D3 C3
G2 Bb2 D3 F3 D3 Bb2 C3 D3 F3 E3 G3 E3
A2 C3 E3 G3 E3 C3 D3 F3 A3 R:1
D3 F3 A3 C4 A3 F3 E3 F3 A3 G3 E3 C3
C3 E3 G3 B3 G3 E3 D3 E3 G3 F3 D3 Bb2
Bb2 D3 F3 A3 F3 D3 C3 D3 F3 E3 C3 A2
A2 C3 E3 G3 E3 C3 B2 C3 E3 F3 D3 C3
G2 Bb2 D3 F3 D3 Bb2 C3 D3 F3 E3 G3 E3
A2 C3 E3 G3 E3 C3 D3 F3 A3 R:1
F3+C4:2 Eb3+Bb3:2
Ab2+Eb3:3 Bb2+F3:1
Db3+Ab3:2 C3+G3:2
Bb2+F3:1.5 Eb3+Bb3:2.5
F3+C4:2 E3+B3:2
D3+A3:2 C3+G3:1 R:1
D3:.5 F3:.5 A3:.5 G3:.5 E3:.5 F3:.5 G3:.5 F3:.5
Bb2:.5 D3:.5 F3:.5 E3:.5 C3:.5 D3:.5 E3:.5 F3:.5
C3:.5 E3:.5 G3:.5 F3:.5 D3:.5 E3:.5 F3:.5 G3:.5
F3:.5 A3:.5 C4:.5 Bb3:.5 G3:.5 A3:.5 Bb3:.5 C4:.5
G3:.5 F3:.5 D3:.5 Bb2:.5 C3:.5 E3:.5 G3:.5 E3:.5
A2:.5 C3:.5 E3:.5 G3:.5 D3:.5 A2:.5 R:1
Bb2 D3 F3 A3 F3 D3 C3 D3 F3 E3 C3 A2
E3 G3 Bb3 D4 Bb3 G3 F3 G3 Bb3 A3 F3 D3
G2 Bb2 D3 F3 D3 Bb2 C3 D3 F3 E3 G3 E3
C3 Eb3 G3 Bb3 G3 Eb3 D3 Eb3 G3 F3 D3 Bb2
A2 C3 E3 G3 E3 C3 B2 C3 E3 G3 E3 C3
D3 F3 A3 C4 A3 F3 E3 C3 A2 R:1
D3+A3:2 C3+G3:2
Bb2+F3:2 E3+B3:2
D3+A3:2 C3+G3:2
B2+F#3:2 A2+E3:2
A2+E3:2 D3+A3:1 R:1
D3+A3:4'''.splitlines()),
 sections={1:'p',7:'mp',13:'pp',19:'p',25:'mp',31:'p',35:'pp'},lower_sections={1:'pp',7:'pp',13:'pp',19:'p',25:'pp',31:'pp'},words={31:'poco rit.'},slurs=[(1,6),(7,12),(19,24),(25,30)],lower_phrases=[(19,24)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*4+a,i*4+b-.18] for i in range(36) for a,b in zip(([0] if i==35 else [0,2]),([4] if i==35 else [2,3 if i in [5,11,17,23,29,34] else 4]))],
 performance=dict(rubato=[72,73,72,70,74,62,75,76,75,74,76,63,65,64,63,65,64,58,74,75,76,77,74,63,75,76,75,77,75,62,61,59,57,54,48,35],phrase_arcs=[[0,23,4],[24,47,5],[72,95,4],[96,119,5]],lower_entries=[[72,95]],pedal_lift=.18,gate=.98,note='The triplet current is light, the duple line supple and singing. The hands exchange those characters without a sudden change of pulse. The chordal centre and ending have room to breathe.')),
dict(op=222,title='Camellia Loom',key='e',fifths=1,meter='4/4',bpm=66,
 description='A middle voice sings beneath a held upper light, then becomes a fine stream of sixteenths. The left hand answers while that stream rests. A changed-harmony return brings the inner line forward again before all three voices settle into a quiet G-major sixth.',
 difficulty='Advanced finger independence with a held RH melody above sixteenths',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Hold the upper RH voice for its full written value while playing the inner sixteenths lightly beneath it. Keep an even touch when the thumb moves between positions. The central LH answer has its own dynamic and phrase; the final three-voice chords remain finger-held rather than being replaced by pedal.',
 parent_opus=218,motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=4,pitches=['E','G','F#','B']),ancestry=dict(source_opus=218,source_hand='rh',source_start_beat=0,source_end_beat=7,source_pitches=['F','Ab','G','C'],transposition_semitones=-13),
 system_starts=list(range(1,37,2)),page_starts=[7,13,19,25,31],engraving=dict(spacing_system=19,spacing_staff=22,pedal_offset_y=580),
 rh='''
D5:4
C5:4
B4:4
C5:4
D5:4
B4:3 R:1
E5:4~
E5:4
D5:4
C5:4
D5:4
B4:3 R:1
B4+D5:4
A4+C5:4
G4+B4:4
A4+C5:4
F#4+A4:4
G4+B4:3 R:1
E5:4
F5:4
Eb5:4
D5:4
C5:4
B4:3 R:1
E5:1 G5:1 F#5:1 B5:1
A5:1 G5:1 E5:1 D5:1
C5:1 E5:1 G5:1 F#5:1
E5:1 D5:1 B4:2
C5:1 D5:.5 E5:.5 F#5:1 A5:1
G5:1 E5:1 D5:1 R:1
E5:2 D5:2
C5:2 B4:2
A4:2 G4:2
B4:2 C5:2
A4:2 B4:1 R:1
E5:4
''',rh_inner='''
E4:1 G4:1 F#4:1 B4:1
A4:1 G4:.5 F#4:.5 E4:1 D4:1
E4:.5 F#4:.5 G4:1 A4:1 F#4:1
G4:1 B4:.5 A4:.5 G4:1 E4:1
F#4:1 A4:.5 C5:.5 B4:1 A4:1
G4:.5 F#4:.5 E4:1 F#4:1 R:1
'''+ '\n'.join(' '.join(f'{n}:.25' if ':' not in n else n for n in row.split()) for row in '''G4 B4 D5 C5 B4 A4 G4 A4 B4 D5 C5 B4 A4 G4 F#4 G4
A4 C5 D5 C5 B4 A4 G4 A4 C5 D5 C5 A4 B4 A4 G4 A4
F#4 A4 C5 B4 A4 G4 F#4 G4 A4 C5 B4 A4 G4 F#4 E4 F#4
E4 G4 B4 A4 G4 F#4 E4 F#4 G4 B4 A4 G4 F#4 E4 D4 E4
F#4 A4 C5 B4 A4 G4 F#4 G4 A4 C5 B4 A4 G4 F#4 E4 F#4
E4 G4 A4 G4 F#4 E4 D4 E4 F#4 A4 G4 F#4 R:1'''.splitlines())+'''
R:4
R:4
R:4
R:4
R:4
R:4
'''+ '\n'.join(' '.join(f'{n}:.25' if ':' not in n else n for n in row.split()) for row in '''G4 B4 D5 C5 B4 A4 G4 A4 B4 D5 C5 B4 A4 G4 F#4 G4
Ab4 C5 Eb5 D5 C5 Bb4 Ab4 Bb4 C5 Eb5 D5 C5 Bb4 Ab4 G4 Ab4
G4 Bb4 Db5 C5 Bb4 Ab4 G4 Ab4 Bb4 Db5 C5 Bb4 Ab4 G4 F4 G4
F#4 A4 C5 B4 A4 G4 F#4 G4 A4 C5 B4 A4 G4 F#4 E4 F#4
E4 G4 B4 A4 G4 F#4 E4 F#4 G4 B4 A4 G4 F#4 E4 D4 E4
E4 G4 A4 G4 F#4 E4 D4 E4 F#4 A4 G4 F#4 R:1'''.splitlines())+'''
B4:1 E5:1 D5:1 G5:1
F#5:1 E5:1 C5:1 B4:1
G4:1 B4:1 D5:1 C5:1
B4:1 A4:1 F#4:2
G4:1 A4:.5 B4:.5 D5:1 F#5:1
E5:1 C5:1 B4:1 R:1
G4+B4:2 F#4+A4:2
E4+G4:2 D4+F#4:2
C4+E4:2 B3+D4:2
D4+F#4:2 E4+G4:2
C4+E4:2 D4+F#4:1 R:1
G4+B4:4
''',lh='''
E3:2 B3:1 G3:1
C3:2 G3:1 E3:1
G2:2 D3:1 B2:1
A2:2 E3:1 C3:1
D3:2 A3:1 F#3:1
E3:1 B3:1 G3:1 R:1
E3+B3:2 D3+A3:2
C3+G3:2 A2+E3:2
D3+A3:2 B2+F#3:2
C3+G3:2 A2+E3:2
B2+F#3:2 D3+A3:2
E3+B3:2 B2+F#3:1 R:1
E3:1 G3:1 F#3:1 B3:1
A3:1 G3:.5 F#3:.5 E3:1 D3:1
E3:.5 F#3:.5 G3:1 A3:1 F#3:1
G3:1 B3:.5 A3:.5 G3:1 E3:1
F#3:1 A3:.5 C4:.5 B3:1 A3:1
G3:.5 F#3:.5 E3:1 F#3:1 R:1
C3+G3:2 E3+B3:2
F3+C4:2 Ab2+Eb3:2
Eb3+Bb3:2 C3+G3:2
D3+A3:2 B2+F#3:2
A2+E3:2 C3+G3:2
B2+F#3:2 E3+B3:1 R:1
E3:1 B3:1 G3:1 B3:1
D3:1 A3:1 F#3:1 A3:1
C3:1 G3:1 E3:1 G3:1
B2:1 F#3:1 D3:1 F#3:1
A2:1 E3:1 C3:1 E3:1
D3:1 A3:1 F#3:1 R:1
C3+G3:2 D3+A3:2
A2+E3:2 B2+F#3:2
A2+E3:2 G2+D3:2
B2+F#3:2 C3+G3:2
D3+A3:2 G2+D3:1 R:1
G2+D3:4
''',hidden_voice_rests=dict(inner=list(range(13,19))),sections={1:'p',7:'p',13:'pp',19:'mp',25:'p',31:'pp'},lower_sections={1:'pp',7:'pp',13:'p',19:'pp',25:'pp'},words={31:'poco rit.'},slurs=[(25,30)],lower_phrases=[(13,18)],voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=3) for a,b in [(0,23),(24,47),(72,95),(96,119)]],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*4+a,i*4+b-.18] for i in range(36) for a,b in zip(([0] if i==35 else [0,2]),([4] if i==35 else [2,3 if i in [5,11,17,23,29,34] else 4]))],
 performance=dict(rubato=[66,67,66,65,68,57,69,70,69,68,70,58,65,66,65,64,67,56,70,71,69,68,67,57,68,69,68,67,69,57,59,57,55,52,46,34],phrase_arcs=[],inner_entries=[[0,23]],lower_entries=[[48,71]],pedal_lift=.18,gate=.99,note='The inner opening phrase is voiced forward. In the sixteenth-note passages it becomes light beneath the upper voice, with a separate left-hand response in the centre. Preserve finger legato through pedal changes.')),
dict(op=223,title='Willow Tessellation',key='d',fifths=-1,meter='3/4',bpm=52,
 description='A falling four-note song gathers a second edge in thirds. The paired line turns through F major and a softer B-flat minor colour; a spare central answer opens into sixths before the first falling gesture returns in warmer harmony.',
 difficulty='Advanced legato thirds and sixths with independent bass phrasing',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Voice the upper note of each moving third without tightening the lower fingers. The middle section opens the same gesture into sixths; change position between paired attacks rather than stretching. Let the bass phrase across the waltz barline.',
 parent_opus=217,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['D','C','A','G']),ancestry=dict(source_opus=217,source_hand='rh',source_start_beat=0,source_end_beat=4.5,source_pitches=['D','C','A','G'],transposition_semitones=0),
 system_starts=list(range(1,37,2)),page_starts=[7,13,19,25,31],engraving=dict(spacing_system=18,spacing_staff=16,pedal_offset_y=550),
 rh='''D5:.5 C5:.5 A4:.5 G4:1.5
Bb4:1 A4:.5 F4:.5 E4:1
'''+ '\n'.join(' '.join(f'{n}:.5' if ':' not in n else n for n in row.split()) for row in '''Bb4+D5 A4+C5 F4+A4 E4+G4 F4+A4 G4+Bb4
A4+C5 Bb4+D5 C5+E5 Bb4+D5 A4+C5 F4+A4
G4+Bb4 A4+C5 Bb4+D5 C5+E5 A4+C5 G4+Bb4
F4+A4 E4+G4 D4+F4:1 R:1
F4+A4 G4+Bb4 A4+C5 Bb4+D5 C5+E5 D5+F5
C5+E5 Bb4+D5 A4+C5 G4+Bb4 F4+A4 E4+G4
F4+A4 Ab4+C5 Bb4+Db5 C5+Eb5 Bb4+Db5 Ab4+C5
Gb4+Bb4 F4+Ab4 Eb4+Gb4 F4+Ab4 Gb4+Bb4 Ab4+C5
G4+Bb4 A4+C5 Bb4+D5 A4+C5 G4+Bb4 E4+G4
F4+A4 G4+Bb4 E4+G4:1 R:1'''.splitlines())+'''
F4+A4:2 E4+G4:1
D4+F4:1 E4+G4:2
Eb4+G4:1 F4+Ab4:1 G4+Bb4:1
Ab4+C5:2 G4+Bb4:1
F4+A4:1.5 G4+Bb4:1.5
E4+G4:2 R:1
'''+ '\n'.join(' '.join(f'{n}:.5' if ':' not in n else n for n in row.split()) for row in '''F4+D5 E4+C5 C4+A4 Bb3+G4 C4+A4 D4+Bb4
E4+C5 F4+D5 G4+E5 F4+D5 E4+C5 C4+A4
D4+Bb4 E4+C5 F4+D5 G4+E5 E4+C5 D4+Bb4
Db4+Bb4 Eb4+C5 F4+Db5 Ab4+F5 G4+Eb5 F4+Db5
Eb4+C5 D4+B4 C4+A4 D4+B4 E4+C5 D4+B4
C4+A4 Bb3+G4 A3+F4:1 R:1
Bb4+D5 A4+C5 F4+A4 E4+G4 F4+A4 G4+Bb4
A4+C5 Bb4+D5 C5+E5 Bb4+D5 A4+C5 F4+A4
G4+Bb4 A4+C5 Bb4+D5 C5+E5 A4+C5 G4+Bb4
Ab4+C5 Bb4+Db5 C5+Eb5 Db5+F5 C5+Eb5 Bb4+Db5
A4+C5 B4+D5 C5+E5 D5+F5 C5+E5 B4+D5
A4+C5 G4+Bb4 F4+A4:1 R:1'''.splitlines())+'''
F4+A4+C5:2 E4+G4+Bb4:1
D4+F4+A4:2 C4+E4+G4:1
D4+F4+A4:1.5 E4+G4+Bb4:1.5
F4+A4+C5:2 G4+Bb4+D5:1
G4+Bb4+E5:2 R:1
F4+A4+D5:3
''',lh='''D3:1 A3:.5 G3:.5 F3:1
C3:1 G3:.5 F3:.5 E3:1
Bb2:1 F3:.5 E3:.5 D3:1
A2:1 E3:.5 G3:.5 C3:1
G2:1 D3:.5 F3:.5 Bb2:1
A2:1 E3:1 R:1
F3:1 C4:.5 Bb3:.5 A3:1
E3:1 Bb3:.5 A3:.5 G3:1
Db3:1 Ab3:.5 Gb3:.5 F3:1
Bb2:1 F3:.5 Ab3:.5 Db3:1
C3:1 G3:.5 Bb3:.5 E3:1
A2:1 E3:1 R:1
D3:.5 F3:.5 A3:.5 G3:.5 F3:.5 E3:.5
C3:.5 E3:.5 G3:.5 A3:.5 G3:.5 E3:.5
C3:.5 Eb3:.5 G3:.5 Bb3:.5 G3:.5 Eb3:.5
F3:.5 Ab3:.5 C4:.5 Bb3:.5 Ab3:.5 F3:.5
Bb2:.5 D3:.5 F3:.5 A3:.5 G3:.5 F3:.5
A2:.5 C3:.5 E3:1 R:1
D3:1 A3:1 F3:1
C3:1 G3:1 E3:1
Bb2:1 F3:1 D3:1
Gb2:1 Db3:1 Bb2:1
A2:1 E3:1 C3:1
D2:1 A2:1 R:1
Bb2:1 F3:.5 A3:.5 D3:1
F3:1 C4:.5 Bb3:.5 A3:1
Eb3:1 Bb3:.5 A3:.5 G3:1
Db3:1 Ab3:.5 C4:.5 F3:1
G2:1 D3:.5 F3:.5 B2:1
C3:1 G3:1 R:1
D3+A3:2 C3+G3:1
Bb2+F3:2 A2+E3:1
Bb2+F3:1.5 C3+G3:1.5
D3+A3:2 Eb3+Bb3:1
C3+G3:2 R:1
Bb2+F3:3''',sections={1:'p',7:'mp',13:'pp',19:'p',25:'mp',31:'pp'},lower_sections={1:'pp',13:'p',19:'pp'},words={31:'poco rit.'},slurs=[(1,6),(7,12),(19,24),(25,30)],lower_phrases=[(13,18)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*3,i*3+(2 if i in [5,11,17,23,29,34] else 3)-.2] for i in range(36)],
 performance=dict(rubato=[52,53,54,54,53,46,55,54,53,52,53,45,49,50,50,51,49,44,53,54,53,52,51,45,55,55,54,53,52,45,46,45,44,42,38,29],phrase_arcs=[[0,17,4],[18,35,5],[54,71,4],[72,89,5]],lower_entries=[[36,53]],pedal_lift=.2,gate=.98,note='The paired upper line remains singing; the brief bass solo in the centre is closer and more present. The sixths open the space gently before the return gathers more motion.')),
dict(op=224,title='Pearl Orbit',key='b',fifths=2,meter='4/4',bpm=64,
 description='A B-minor phrase becomes two unequal circles: five-note arpeggios underneath a four-note singing pulse. A quiet chordal window interrupts the orbit, which returns in a brighter register and finally unwinds into an open A-major ninth.',
 difficulty='Advanced sustained five-against-four independence',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Practise each two-beat quintuplet against four even eighths, retaining the melody across their different points of contact. The central chords release that coordination before the current returns. The final bars broaden without accelerating the arpeggios.',
 parent_opus=219,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['B','D','C#','A']),ancestry=dict(source_opus=219,source_hand='lh',source_start_beat=0,source_end_beat=5,source_pitches=['B','D','C#','A'],transposition_semitones=24),
 system_starts=list(range(1,33,2)),page_starts=[7,13,19,25,29],engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=560),
 tuplet_spans=[dict(hand='lh',start_beat=i*4+j,end_beat=i*4+j+2,actual=5,normal=4,show_number='both',stem='up') for i in list(range(2,12))+list(range(16,27)) for j in ([0] if i in [6,11,23,26] else [0,2])],
 rh='''B4:1 D5:1 C#5:1 A4:1
F#4:1.5 A4:.5 C#5:1 E5:1
'''+ '\n'.join(' '.join(f'{n}:.5' if ':' not in n else n for n in row.split()) for row in '''D5 F#5 E5 C#5 B4 D5 C#5 A4
B4 C#5 D5 F#5 E5 D5 C#5 B4
A4 C#5 E5 G#5 F#5 E5 D5 C#5
D5 E5 F#5 A5 G5 F#5 E5 D5
C#5 A4 B4 F#4 R:2
E5 G5 F#5 D5 C#5 E5 D5 B4
D5 F#5 A5 C#6 B5 A5 F#5 E5
D5 F5 Ab5 C6 Bb5 Ab5 F5 Eb5
E5 G5 Bb5 D6 C6 Bb5 G5 F5
F#5 E5 D5 B4 R:2'''.splitlines())+'''
D4+F#4+A4:3 E4+G#4+B4:1
F4+Ab4+C5:2 G4+Bb4+D5:2
F#4+A4+C#5:1.5 E4+G#4+B4:2.5
D4+F#4+B4:2 R:2
'''+ '\n'.join(' '.join(f'{n}:.5' if ':' not in n else n for n in row.split()) for row in '''B5 A5 F#5 E5 D5 F#5 A5 C#6
B5 G#5 E5 D5 C#5 E5 G#5 B5
A5 F#5 D5 C#5 B4 D5 F#5 A5
G5 E5 C5 B4 A4 C5 E5 G5
F#5 D5 B4 A4 G4 B4 D5 F#5
F5 Db5 Bb4 Ab4 Gb4 Bb4 Db5 F5
E5 C#5 A4 G#4 F#4 A4 C#5 E5
D5 B4 C#5 A4 R:2
D5 F#5 E5 C#5 B4 D5 C#5 A4
B4 C#5 D5 F#5 E5 D5 C#5 B4
A4 C#5 E5 G#5 R:2'''.splitlines())+'''
F#4+A4+C#5:2 E4+G#4+B4:2
D4+F#4+B4:2 C#4+E4+A4:2
C4+E4+A4:2 D4+F#4+B4:2
D4+F#4+B4:2 R:2
C#4+E4+G#4+B4:4
''',lh='''B2:2 F#3:1 D3:1
A2:2 E3:1 C#3:1
'''+ '\n'.join(' '.join(f'{n}:2/5' if ':' not in n else n for n in row.split()) for row in '''B2 D3 F#3 A3 F#3 E3 F#3 A3 F#3 D3
G2 B2 D3 F#3 D3 C#3 D3 F#3 D3 B2
A2 C#3 E3 G#3 E3 D3 E3 G#3 E3 C#3
D3 F#3 A3 C#4 A3 G3 A3 C#4 A3 F#3
F#3 A3 C#4 E4 C#4 R:2
C#3 E3 G3 B3 G3 F#3 G3 B3 G3 E3
B2 D3 F#3 A3 F#3 E3 F#3 A3 F#3 D3
Bb2 Db3 F3 Ab3 F3 Eb3 F3 Ab3 F3 Db3
C3 E3 G3 Bb3 G3 F3 G3 Bb3 G3 E3
B2 D3 F#3 A3 F#3 R:2'''.splitlines())+'''
B2+F#3:3 A2+E3:1
Db3+Ab3:2 Eb3+Bb3:2
D3+A3:1.5 E3+B3:2.5
B2+F#3:2 R:2
'''+ '\n'.join(' '.join(f'{n}:2/5' if ':' not in n else n for n in row.split()) for row in '''G3 B3 D4 F#4 D4 C#4 D4 F#4 D4 B3
E3 G#3 B3 D4 B3 A3 B3 D4 B3 G#3
D3 F#3 A3 C#4 A3 G3 A3 C#4 A3 F#3
C3 E3 G3 B3 G3 F#3 G3 B3 G3 E3
G2 B2 D3 F#3 D3 C3 D3 F#3 D3 B2
Gb2 Bb2 Db3 F3 Db3 Cb3 Db3 F3 Db3 Bb2
A2 C#3 E3 G#3 E3 D3 E3 G#3 E3 C#3
B2 D3 F#3 A3 F#3 R:2
G2 B2 D3 F#3 D3 C#3 D3 F#3 D3 B2
E3 G3 B3 D4 B3 A3 B3 D4 B3 E3
A2 C#3 E3 G#3 E3 R:2'''.splitlines())+'''
D3+A3:2 E3+B3:2
G2+D3:2 A2+E3:2
F2+C3:2 G2+D3:2
E2+B2:2 R:2
A2+E3:4''',sections={1:'p',3:'p',8:'mp',13:'pp',17:'mp',25:'p',28:'pp'},lower_sections={1:'pp'},words={28:'poco rit.'},slurs=[(1,7),(8,12),(17,24),(25,27)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*4+a,i*4+b-.18] for i in range(32) for a,b in ([(0,2)] if i in [6,11,15,23,26,30] else [(0,2),(2,4)])],
 performance=dict(rubato=[64,65,66,67,66,65,54,66,68,67,66,54,57,56,58,51,68,69,68,67,66,64,65,53,64,65,54,55,52,48,43,32],phrase_arcs=[[0,26,4],[28,46,5],[64,94,5],[96,106,3]],lower_entries=[],pedal_lift=.18,gate=.97,note='The quintuplets stay light and even, against the broader upper phrase. Allow the harmonic detour to darken the colour before the higher return.')),
dict(op=225,title='Fennel Polyphony',key='e',fifths=1,meter='5/4',bpm=58,
 description='Four voices enter a long, uneven room. The outer song is answered by a more insistent tenor; suspensions shift the weight between the hands, and a brief F-minor dusk passes through the middle before an E-minor sixth remains.',
 difficulty='Advanced four-voice legato and independent suspensions in five',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Sustain each voice for its own written duration. The tenor enters after the bass and must retain its phrase when the RH moves; the inner RH suspensions resolve without disturbing the soprano. Practise each pair of voices separately before balancing all four.',
 parent_opus=222,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=5,pitches=['E','G','F#','B']),ancestry=dict(source_opus=222,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=4,source_pitches=['E','G','F#','B'],transposition_semitones=12),
 system_starts=list(range(1,25,2)),page_starts=[5,9,13,17,21],engraving=dict(spacing_system=20,spacing_staff=24,pedal_offset_y=590),
 rh='''E5:1.5 G5:.5 F#5:1 B5:2
A5:2 G5:1 E5:1 D5:1
C5:1 D5:.5 E5:.5 G5:1 F#5:2
E5:2 D5:1 B4:1 R:1
D5:1 F#5:1 A5:1 G5:2
F#5:1 E5:.5 D5:.5 B4:1 D5:2
E5:1 G5:1 B5:.5 A5:.5 G5:2
F#5:2 E5:1 D5:1 R:1
C5:2 D5:1 E5:2
Db5:2 Eb5:1 F5:2
Eb5:1 G5:1 F5:1 Bb5:2
Ab5:2 G5:1 Eb5:1 R:1
G5:1.5 F#5:.5 E5:1 D5:2
F#5:1.5 E5:.5 D5:1 C5:2
E5:1.5 D5:.5 B4:1 A4:2
B4:2 D5:1 E5:1 R:1
E5:1.5 G5:.5 F#5:1 B5:2
A5:2 G5:1 E5:1 D5:1
C5:1 D5:.5 E5:.5 G5:1 F#5:2
E5:2 D5:1 B4:1 R:1
E5:2 D5:1 C5:2
D5:2 C5:1 B4:2
B4:2 A4:1 G4:1 R:1
C#5:5
''',rh_inner='''B4:5
C5:2 B4:1 A4:2
G4:1 A4:2 B4:2
B4:1 A4:2 G4:1 R:1
A4:2 C5:1 B4:2
A4:1 G4:2 F#4:2
B4:1 D5:2 C5:2
C5:1 B4:2 A4:1 R:1
G4:1 B4:2 A4:2
Ab4:1 C5:2 Bb4:2
Bb4:1 Db5:2 C5:2
Eb5:1 Db5:2 Bb4:1 R:1
B4:1 D5:2 C5:2
A4:1 C5:2 B4:2
G4:1 A4:2 F#4:2
F#4:1 A4:2 B4:1 R:1
B4:2 D5:1 C5:2
C5:1 B4:2 A4:2
G4:1 B4:2 A4:2
B4:1 A4:2 G4:1 R:1
B4:1 A4:2 G4:2
A4:1 G4:2 F#4:2
F#4:1 E4:2 D4:1 R:1
G4:5
''',lh='''E3:3 F#3:2
D3:3 E3:2
C3:3 D3:2
E3:2 D3:2 R:1
D3:3 E3:2
B2:3 C3:2
E3:3 F#3:2
D3:2 C3:2 R:1
A2:3 B2:2
Bb2:3 C3:2
C3:3 D3:2
Eb3:2 F3:2 R:1
E3:3 F#3:2
D3:3 E3:2
C3:3 D3:2
B2:2 C3:2 R:1
C3:3 D3:2
D3:3 E3:2
A2:3 B2:2
E3:2 D3:2 R:1
C3:3 D3:2
B2:3 C3:2
A2:2 B2:2 R:1
E3:5
''',lh_upper='''R:1 G3:1 B3:1 A3:2
F#3:1 A3:1 C4:1 B3:2
E3:1 G3:1 B3:1 A3:2
G3:1 B3:1 A3:1 F#3:1 R:1
R:.5 F#3:.5 A3:1 C4:1 B3:2
D3:1 F#3:.5 A3:.5 G3:1 E3:2
G3:1 B3:.5 D4:.5 C4:1 A3:2
A3:1 G3:1 F#3:1 E3:1 R:1
C3:1 E3:.5 G3:.5 F#3:1 D3:2
Db3:1 F3:.5 Ab3:.5 G3:1 Eb3:2
Eb3:1 G3:.5 Bb3:.5 A3:1 F3:2
G3:1 Bb3:1 Ab3:1 C4:1 R:1
G3:1 B3:.5 D4:.5 C4:1 A3:2
F#3:1 A3:.5 C4:.5 B3:1 G3:2
E3:1 G3:.5 B3:.5 A3:1 F#3:2
D3:1 F#3:1 A3:1 G3:1 R:1
E3:1 G3:1 B3:1 A3:2
F#3:1 A3:1 C4:1 B3:2
C3:1 E3:1 G3:1 F#3:2
G3:1 B3:1 A3:1 F#3:1 R:1
E3:1 G3:1 B3:1 A3:2
D3:1 F#3:1 A3:1 G3:2
C3:1 E3:1 F#3:1 D3:1 R:1
B3:5
''',sections={1:'p',5:'p',9:'pp',13:'mp',17:'p',21:'pp'},lower_sections={1:'pp',5:'p',9:'p',17:'pp'},words={21:'poco rit.'},slurs=[(1,4),(5,8),(9,12),(13,16),(17,20)],hairpins=[],tempo_changes={},group=3,
 voice_phrases=[dict(voice=v,start_beat=a,end_beat=b,swell=3) for v,spans in [('inner',[(0,19),(20,39),(40,59),(60,79),(80,99)]),('tenor',[(1,19),(20.5,39),(40,59),(60,79),(80,99)])] for a,b in spans],
 pedal_spans=[[i*5+a,i*5+b-.22] for i in range(24) for a,b in ([(0,5)] if i==23 else [(0,3),(3,4 if i in [3,7,11,15,19,22] else 5)])],
 performance=dict(rubato=[58,60,59,51,61,62,61,52,57,56,58,50,62,63,62,52,60,61,59,51,51,48,42,30],phrase_arcs=[[0,19,4],[20,39,3],[40,59,3],[60,79,4],[80,99,3]],lower_entries=[],tenor_entries=[[20,39],[60,79]],inner_entries=[[40,59]],pedal_lift=.22,gate=.99,note='Bring the tenor forward at its longer answering entries, keeping the other three lines alive at a lower dynamic. Pedal changes do not replace the written finger-held durations.')),
dict(op=226,title='Alder Cascade',key='d',fifths=-1,meter='7/8',bpm=62,
 description='A small D-minor song loosens into a continuous ribbon of sixteenths. The seven-eighth bar alternates three-plus-two-plus-two and two-plus-two-plus-three; the ribbon passes to the bass, rises through a chromatic corridor and returns as a slower fragment above a departing left hand.',
 difficulty='Advanced flowing semiquavers across changing positions in seven',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Carry the long sixteenth-note line through each change of hand position without accenting the thumb. The LH takes the complete moving texture in the centre. Hear the changing groupings inside seven, keeping the slower voice independent of the beamed figures.',
 parent_opus=221,motif=dict(hand='rh',start_beat=0,end_beat=3.5,pitches=['D','F','E','A']),ancestry=dict(source_opus=221,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),
 system_starts=list(range(1,37,2)),page_starts=[7,13,19,25,31],engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=550),
 beam_spans=[dict(hand=h,start_beat=i*3.5+a,end_beat=i*3.5+b,note_type='16th',stem='down' if h=='rh' else 'up') for h,bars in [('rh',list(range(2,12))+list(range(18,24))+list(range(26,30))),('lh',list(range(12,18)))] for i in bars for a,b in ([(0,1.5),(1.5,2.5)] if i in [5,11,17,23,29] else [(0,1),(1,2),(2,3.5)] if i%2 else [(0,1.5),(1.5,2.5),(2.5,3.5)])],
 rh='''D5:1 F5:.5 E5:.5 A5:1.5
G5:1 E5:.5 D5:.5 C5:1.5
'''+ '\n'.join(' '.join(f'{n}:.25' if ':' not in n else n for n in row.split()) for row in '''D4 F4 A4 C5 E5 F5 A5 G5 E5 C5 A4 F4 E4 C4
C4 E4 G4 B4 D5 E5 G5 F5 D5 B4 G4 E4 D4 C4
D4 F4 A4 Bb4 D5 F5 A5 G5 F5 D5 Bb4 A4 F4 D4
E4 G4 A4 C5 E5 G5 E5 C5 A4 G4 R:1
F4 A4 C5 E5 G5 A5 C6 Bb5 G5 E5 C5 A4 G4 E4
E4 G4 B4 D5 F5 G5 B5 A5 F5 D5 B4 G4 F4 D4
Eb4 G4 Bb4 Db5 F5 G5 Bb5 Ab5 F5 Db5 Bb4 G4 F4 Db4
Db4 F4 Ab4 C5 Eb5 F5 Ab5 Gb5 Eb5 C5 Ab4 F4 Eb4 C4
D4 F4 A4 C5 E5 F5 A5 G5 E5 C5 A4 F4 E4 C4
D4 F4 A4 C5 E5 F5 E5 C5 A4 F4 R:1'''.splitlines())+'''
F4+A4+D5:1.5 E4+G4+C5:2
G4+Bb4+E5:1 F4+A4+D5:2.5
A4+C5+F5:1.5 G4+B4+E5:2
Ab4+C5+F5:1 G4+Bb4+Eb5:2.5
F4+A4+D5:1.5 E4+G4+C5:2
F4+A4+D5:2.5 R:1
'''+ '\n'.join(' '.join(f'{n}:.25' if ':' not in n else n for n in row.split()) for row in '''D5 F5 A5 C6 A5 F5 E5 C5 A4 C5 E5 G5 F5 D5
C5 E5 G5 B5 G5 E5 D5 B4 G4 B4 D5 F5 E5 C5
Bb4 D5 F5 A5 F5 D5 C5 A4 F4 A4 C5 E5 D5 Bb4
Bb4 Db5 F5 Ab5 F5 Db5 C5 Ab4 F4 Ab4 C5 Eb5 Db5 Bb4
A4 C5 E5 G5 E5 C5 B4 G4 E4 G4 B4 D5 C5 A4
A4 C5 D5 F5 E5 C5 A4 G4 F4 E4 R:1'''.splitlines())+'''
D5:1 F5:.5 E5:.5 A5:1.5
G5:1 E5:.5 D5:.5 C5:1.5
'''+ '\n'.join(' '.join(f'{n}:.25' if ':' not in n else n for n in row.split()) for row in '''D4 F4 A4 C5 E5 F5 A5 G5 E5 C5 A4 F4 E4 C4
C4 Eb4 G4 Bb4 D5 Eb5 G5 F5 D5 Bb4 G4 Eb4 D4 C4
D4 F4 A4 C5 E5 F5 A5 G5 E5 C5 A4 F4 E4 C4
D4 F4 A4 C5 D5 F5 E5 C5 A4 F4 R:1'''.splitlines())+'''
F4+A4:1.5 E4+G4:2
D4+F4:1 C4+E4:2.5
D4+F4:1.5 E4+G4:2
F4+A4:1.5 G4+Bb4:2
E4+G4:2.5 R:1
F4+A4+B4:3.5
''',lh='''D3:1.5 A3:1 F3:1
C3:1 G3:1 E3:1.5
D3:1.5 A3:1 F3:1
C3:1 G3:1 E3:1.5
Bb2:1.5 F3:1 D3:1
A2:1.5 E3:1 R:1
F3:1.5 C4:1 A3:1
E3:1 B3:1 G3:1.5
Eb3:1.5 Bb3:1 G3:1
Db3:1 Ab3:1 F3:1.5
Bb2:1.5 F3:1 D3:1
D3:1.5 A3:1 R:1
'''+ '\n'.join(' '.join(f'{n}:.25' if ':' not in n else n for n in row.split()) for row in '''D3 F3 A3 C4 A3 F3 E3 C3 A2 C3 E3 G3 F3 D3
C3 E3 G3 Bb3 G3 E3 D3 Bb2 G2 Bb2 D3 F3 E3 C3
F3 A3 C4 E4 C4 A3 G3 E3 C3 E3 G3 Bb3 A3 F3
F3 Ab3 C4 Eb4 C4 Ab3 G3 Eb3 C3 Eb3 G3 Bb3 Ab3 F3
Bb2 D3 F3 A3 F3 D3 C3 A2 F2 A2 C3 E3 D3 Bb2
A2 C3 E3 G3 E3 C3 D3 F3 A3 F3 R:1'''.splitlines())+'''
D3:1.5 A3:1 F3:1
C3:1 G3:1 E3:1.5
Bb2:1.5 F3:1 D3:1
Gb2:1 Db3:1 Bb2:1.5
A2:1.5 E3:1 C3:1
D3:1.5 A3:1 R:1
Bb2:1.5 F3:1 D3:1
E3:1 B3:1 G3:1.5
Bb2:1.5 F3:1 D3:1
C3:1 G3:1 Eb3:1.5
A2:1.5 E3:1 C3:1
D3:1.5 A3:1 R:1
D3:.5 F3:.5 A3:.5 C4:.5 A3:.5 G3:.5 E3:.5
C3:.5 E3:.5 G3:.5 Bb3:.5 G3:.5 F3:.5 D3:.5
Bb2:.5 D3:.5 F3:.5 A3:.5 F3:.5 E3:.5 C3:.5
A2:.5 C3:.5 E3:.5 G3:.5 E3:.5 F3:.5 G3:.5
C3:.5 E3:.5 G3:.5 Bb3:.5 G3:.5 R:1
D3+A3:3.5''',sections={1:'p',3:'p',7:'mp',13:'pp',19:'mp',25:'p',31:'pp'},lower_sections={1:'pp',13:'p',19:'pp',31:'p'},words={31:'poco rit.'},slurs=[(1,6),(7,12),(19,24),(25,30)],lower_phrases=[(13,18),(31,35)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*3.5,i*3.5+(2.5 if i in [5,11,17,23,29,34] else 3.5)-.18] for i in range(36)],
 performance=dict(rubato=[62,63,66,67,66,55,68,69,68,67,66,55,65,66,67,66,65,54,68,69,68,67,66,55,62,63,66,65,64,54,56,54,52,48,42,30],phrase_arcs=[[0,20,4],[21,41,5],[63,83,5],[84,104,4]],lower_entries=[[42,62],[105,121.5]],pedal_lift=.18,gate=.97,note='Maintain one flowing line as the changing groups move through each hand. The final bass figure becomes slower and warmer, with the B-natural sixth held above the D-minor chord.')),
dict(op=227,title='Reed Cantilever',key='d',fifths=-1,meter='4/4',bpm=60,
 description='A quiet song discovers a buoyant, displaced chord dance. The left hand moves between low bass and close upper chords, while the right hand arrives just beyond the beat. A chordal pause lets the space widen before the dance returns and ends on a gentle F-major ninth.',
 difficulty='Advanced quiet stride leaps and syncopated chord voicing',technique_limits=dict(chord_span=12,melodic_leap=24,rapid_leap=9),technical_note='Move the released LH between its low bass and higher chord during each written rest. The largest shifts are prepared quarter-beat positions, never held stretches. Shape the RH top line through the syncopated chords without punching their entrances; sustain the written rests as part of the dance.',
 parent_opus=223,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','C','A','G']),ancestry=dict(source_opus=223,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['D','C','A','G'],transposition_semitones=0),
 system_starts=list(range(1,29,2)),page_starts=[5,9,15,21,25],engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=570),
 rh='''D5:1 C5:.5 A4:.5 G4:2
Bb4:1 A4:.5 G4:.5 F4:2
'''+ '\n'.join(f'R:.5 {a}:.75 R:.25 {b}:1 {c}:.5 R:.5 {d}:.5' for a,b,c,d in [row.split() for row in '''F4+A4+D5 G4+Bb4+E5 A4+C5+F5 G4+Bb4+E5
E4+G4+C5 F4+A4+D5 G4+B4+E5 F4+A4+D5
D4+F4+Bb4 E4+G4+C5 F4+A4+D5 E4+G4+C5
C4+E4+A4 D4+F4+B4 E4+G4+C5 F4+A4+D5
F4+A4+C5 G4+Bb4+D5 A4+C5+E5 Bb4+D5+F5
G4+B4+D5 A4+C5+E5 B4+D5+F#5 A4+C5+E5
Ab4+C5+Eb5 Bb4+Db5+F5 C5+Eb5+G5 Bb4+Db5+F5
A4+C5+E5 G4+Bb4+D5 F4+A4+C5 E4+G4+C5'''.splitlines()])+'''
F4+A4+D5:2 G4+Bb4+E5:2
Ab4+C5+F5:3 G4+Bb4+Eb5:1
F4+Ab4+Db5:2 Eb4+G4+C5:2
D4+F4+Bb4:3 R:1
'''+ '\n'.join(f'{a}:.75 R:.25 {b}:.5 R:.5 {c}:1.5 {d}:.5' for a,b,c,d in [row.split() for row in '''F4+A4+D5 G4+Bb4+E5 A4+C5+F5 G4+Bb4+E5
G4+B4+E5 A4+C5+F#5 B4+D5+G5 A4+C5+F#5
A4+C5+F5 Bb4+D5+G5 C5+E5+A5 Bb4+D5+G5
Ab4+C5+F5 Bb4+Db5+G5 C5+Eb5+Ab5 Bb4+Db5+G5
G4+Bb4+Eb5 A4+C5+F5 Bb4+D5+G5 A4+C5+F5
F4+A4+D5 E4+G4+C5 D4+F4+Bb4 E4+G4+C5'''.splitlines()])+ '\n'+'\n'.join(f'R:.5 {a}:.75 R:.25 {b}:1 {c}:.5 R:.5 {d}:.5' for a,b,c,d in [row.split() for row in '''F4+A4+D5 G4+Bb4+E5 A4+C5+F5 G4+Bb4+E5
E4+G4+C5 F4+A4+D5 G4+B4+E5 F4+A4+D5
Eb4+G4+C5 F4+Ab4+D5 G4+Bb4+Eb5 Ab4+C5+F5
F4+A4+D5 E4+G4+C5 D4+F4+Bb4 E4+G4+C5'''.splitlines()])+'''
F4+A4+C5:1.5 G4+Bb4+D5:2.5
A4+C5+E5:2 G4+Bb4+D5:2
G4+Bb4+C5:3 R:1
G4+A4+C5+E5:4
''',lh='''D3:2 A3:1 F3:1
Bb2:2 F3:1 D3:1
'''+ '\n'.join(f'{a}:.5 R:.5 {b}:.5 R:.5 {c}:.5 R:.5 {d}:.5 R:.5' for a,b,c,d in [row.split() for row in '''D2 F3+A3+C4 A2 E3+G3+C4
C2 E3+G3+B3 G2 D3+F3+B3
Bb1 D3+F3+A3 F2 C3+E3+A3
A1 C3+E3+G3 E2 B2+D3+G3
F2 A3+C4+E4 C3 G3+Bb3+D4
E2 G3+B3+D4 B2 F#3+A3+C4
Ab2 C4+Eb4+G4 Eb3 Bb3+Db4+F4
A2 C4+E4+G4 E3 B3+D4+F4'''.splitlines()])+'''
D3+A3:2 C3+G3:2
F3+C4:3 Eb3+Bb3:1
Db3+Ab3:2 C3+G3:2
Bb2+F3:3 R:1
'''+ '\n'.join(f'{a}:.5 R:.5 {b}:.5 R:.5 {c}:.5 R:.5 {d}:.5 R:.5' for a,b,c,d in [row.split() for row in '''Bb1 D3+F3+A3 F2 C3+E3+A3
E2 G3+B3+D4 B2 F#3+A3+C4
F2 A3+C4+E4 C3 G3+Bb3+D4
Db2 F3+Ab3+C4 Ab2 Eb3+G3+Bb3
Eb2 G3+Bb3+D4 Bb2 F3+A3+C4
A1 C3+E3+G3 E2 B2+D3+G3
Bb1 D3+F3+A3 F2 C3+E3+A3
E2 G3+B3+D4 B2 F#3+A3+C4
C2 Eb3+G3+Bb3 G2 D3+F3+Bb3
D2 F3+A3+C4 A2 E3+G3+C4'''.splitlines()])+'''
D3+A3:1.5 C3+G3:2.5
F3+C4:2 Eb3+Bb3:2
C3+G3:3 R:1
F2+C3:4''',sections={1:'p',3:'mp',11:'pp',15:'mp',21:'p',25:'pp'},lower_sections={1:'pp'},words={25:'poco rit.'},slurs=[(1,2),(11,14),(25,28)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*4+a,i*4+b-.16] for i in range(28) for a,b in ([(0,3)] if i in [13,26] else [(0,4)] if i==27 else [(0,1.5),(2,4)] if 14<=i<20 else [(0,2),(2,4)])],
 performance=dict(rubato=[60,58,63,64,63,62,65,66,64,57,54,53,52,47,65,66,67,66,65,57,63,64,62,55,52,48,42,31],phrase_arcs=[[0,8,3],[8,40,4],[56,80,5],[80,96,3]],lower_entries=[],pedal_lift=.16,gate=.95,note='The RH offbeats are buoyant and closely voiced. LH chords are quiet arrivals after relaxed, released leaps, while the bass remains warm. The final F-major ninth releases the dance.')),
dict(op=228,title='Juniper Parallax',key='c',fifths=-3,meter='6/8',bpm=51,
 description='Seven gently circling notes move against the six of a slow compound pulse. The hands exchange that slight difference in pace; two whole-bar silences open the form, and the final harmony turns the C-minor light towards an A-flat-major ninth.',
 difficulty='Advanced seven-against-six coordination and exchanged rhythmic roles',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Keep each seven-note group evenly spaced across the full bar while the other hand retains its six eighths. Avoid aligning the inner notes by approximation; only the barlines meet. The central exchange preserves the long phrase in the opposite hand.',
 parent_opus=224,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['C','Eb','D','Bb']),ancestry=dict(source_opus=224,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['B','D','C#','A'],transposition_semitones=1),
 system_starts=list(range(1,37,2)),page_starts=[7,13,19,25,31],engraving=dict(spacing_system=18,spacing_staff=18,pedal_offset_y=560),
 tuplet_spans=[dict(hand=h,start_beat=i*3,end_beat=i*3+3,actual=7,normal=6,show_number='both',stem='up' if h=='lh' else 'down') for h,bars in [('lh',list(range(2,11))+list(range(24,30))),('rh',list(range(16,23)))] for i in bars],
 rh='''C5:.5 Eb5:.5 D5:.5 Bb4:1.5
G4:1 Bb4:.5 D5:.5 F5:1
'''+ '\n'.join(' '.join(f'{n}:.5' for n in row.split()) for row in '''Eb5 G5 F5 D5 C5 Bb4
Ab4 C5 Eb5 G5 F5 Eb5
D5 F5 Ab5 C6 Bb5 Ab5
G5 Eb5 D5 C5 Bb4 G4
Ab4 C5 Eb5 D5 C5 Ab4
A4 C5 E5 G5 F5 E5
Bb4 Db5 F5 Ab5 G5 F5
Eb5 G5 Bb5 Ab5 F5 D5
Eb5 D5 C5 Bb4 G4 C5'''.splitlines())+'''
R:3
Eb4+G4+C5:1.5 F4+Ab4+D5:1.5
G4+Bb4+Eb5:2 Ab4+C5+F5:1
F4+Ab4+Db5:1.5 Eb4+G4+C5:1.5
D4+F4+Bb4:2 G4+B4+D5:1
'''+ '\n'.join(' '.join(f'{n}:3/7' for n in row.split()) for row in '''C5 Eb5 G5 Bb5 G5 F5 D5
Bb4 D5 F5 Ab5 F5 Eb5 C5
Ab4 C5 Eb5 G5 Eb5 D5 Bb4
A4 C5 E5 G5 E5 D5 B4
Bb4 Db5 F5 Ab5 F5 Eb5 C5
G4 B4 D5 F5 D5 C5 A4
G4 Bb4 C5 Eb5 D5 Bb4 C5'''.splitlines())+'''
R:3
'''+ '\n'.join(' '.join(f'{n}:.5' for n in row.split()) for row in '''Eb5 G5 F5 D5 C5 Bb4
Ab4 C5 Eb5 G5 F5 Eb5
D5 F5 Ab5 C6 Bb5 Ab5
G5 E5 D5 C5 B4 G4
Ab4 C5 Eb5 G5 F5 D5
Eb5 D5 C5 Bb4 G4 C5'''.splitlines())+'''
Eb4+G4+C5:1.5 D4+F4+Bb4:1.5
C4+Eb4+Ab4:2 D4+F4+Bb4:1
Eb4+G4+C5:1.5 F4+Ab4+D5:1.5
G4+Bb4+Eb5:2 F4+Ab4+D5:1
Eb4+G4+C5:2 R:1
G4+Bb4+C5+Eb5:3
''',lh='''C3:1.5 G3:1.5
Bb2:1.5 F3:1.5
'''+ '\n'.join(' '.join(f'{n}:3/7' for n in row.split()) for row in '''C3 Eb3 G3 Bb3 Ab3 F3 D3
Ab2 C3 Eb3 G3 F3 D3 Bb2
Bb2 D3 F3 Ab3 G3 Eb3 C3
C3 Eb3 G3 Bb3 Ab3 F3 D3
F3 Ab3 C4 Eb4 Db4 Bb3 G3
F3 A3 C4 E4 D4 B3 G3
Bb2 Db3 F3 Ab3 Gb3 Eb3 C3
Eb3 G3 Bb3 D4 C4 A3 F3
C3 Eb3 G3 Bb3 Ab3 F3 D3'''.splitlines())+'''
R:3
C3+G3:1.5 Bb2+F3:1.5
Eb3+Bb3:2 F3+C4:1
Db3+Ab3:1.5 C3+G3:1.5
Bb2+F3:2 G2+D3:1
'''+ '\n'.join(' '.join(f'{n}:.5' for n in row.split()) for row in '''C3 Eb3 G3 Bb3 G3 Eb3
Bb2 D3 F3 Ab3 F3 D3
Ab2 C3 Eb3 G3 Eb3 C3
F2 A2 C3 E3 C3 A2
Bb2 Db3 F3 Ab3 F3 Db3
G2 B2 D3 F3 D3 B2
C3 Eb3 G3 Bb3 G3 Eb3'''.splitlines())+'''
R:3
'''+ '\n'.join(' '.join(f'{n}:3/7' for n in row.split()) for row in '''Ab2 C3 Eb3 G3 F3 D3 Bb2
F3 Ab3 C4 Eb4 Db4 Bb3 G3
Bb2 D3 F3 Ab3 G3 Eb3 C3
E3 G3 B3 D4 C4 A3 F3
F3 Ab3 C4 Eb4 Db4 Bb3 G3
C3 Eb3 G3 Bb3 Ab3 F3 D3'''.splitlines())+'''
C3+G3:1.5 Bb2+F3:1.5
Ab2+Eb3:2 Bb2+F3:1
C3+G3:1.5 Bb2+F3:1.5
Eb3+Bb3:2 D3+Ab3:1
C3+G3:2 R:1
Ab2+Eb3:3''',sections={1:'p',3:'p',7:'mp',13:'pp',17:'p',25:'mp',31:'pp'},lower_sections={1:'pp',17:'p',25:'pp'},words={31:'poco rit.'},slurs=[(1,6),(7,11),(17,23),(25,30)],lower_phrases=[(17,23)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*3,i*3+(2 if i==34 else 3)-.2] for i in range(36) if i not in [11,23]],
 performance=dict(rubato=[51,52,54,55,54,51,55,56,55,53,47,48,49,50,49,47,54,55,54,55,54,52,46,48,54,55,54,55,52,46,47,45,43,40,36,28],phrase_arcs=[[0,18,3],[18,33,4],[48,69,4],[72,90,4]],lower_entries=[[48,69]],pedal_lift=.2,gate=.98,note='Treat the seven-note circles as one breath rather than separate accents. Two complete silent bars remain clear of pedal. The final A-flat sonority stays open and luminous.')),
dict(op=229,title='Camellia Altitude',key='f#',fifths=3,meter='4/4',meters=['4/4']*6+['5/4']*6+['3/4']*6+['4/4']*6,bpm=50,
 description='A singing octave line moves above fine left-hand arpeggios. Its phrases lengthen into five, then contract into a three-beat exchange of bass octaves and upper thirds. The opening returns with altered bass colours before settling on a clear A-major sixth.',
 difficulty='Advanced cantabile octaves, supple position changes and mixed metre',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Voice the upper edge of the RH octaves, releasing and relocating the hand between attacks without losing the sung line. The LH sixteenths require an even thumb passage under that broad phrase. In the three-beat section the octaves pass to LH beneath moving RH thirds.',
 parent_opus=225,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['F#','A','G#','C#']),ancestry=dict(source_opus=225,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=5,source_pitches=['E','G','F#','B'],transposition_semitones=2),
 system_starts=list(range(1,25,2)),page_starts=[5,9,13,17,21],engraving=dict(spacing_system=19,spacing_staff=18,pedal_offset_y=570),
 rh='''F#4+F#5:1.5 A4+A5:.5 G#4+G#5:1 C#5+C#6:1
B4+B5:1 A4+A5:.5 F#4+F#5:.5 E4+E5:2
D4+D5:1 E4+E5:.5 F#4+F#5:.5 A4+A5:1 G#4+G#5:1
F#4+F#5:1 E4+E5:.5 C#4+C#5:.5 D4+D5:2
E4+E5:1 G#4+G#5:.5 B4+B5:.5 A4+A5:1 G#4+G#5:1
F#4+F#5:1 E4+E5:1 C#4+C#5:1 R:1
F#4+F#5:.5 G#4+G#5:.5 A4+A5:.5 C#5+C#6:.5 B4+B5:.5 A4+A5:.5 G#4+G#5:.5 E4+E5:.5 F#4+F#5:1
E4+E5:.5 F#4+F#5:.5 G#4+G#5:.5 B4+B5:.5 A4+A5:.5 G#4+G#5:.5 F#4+F#5:.5 D4+D5:.5 E4+E5:1
D4+D5:.5 E4+E5:.5 F#4+F#5:.5 A4+A5:.5 G#4+G#5:.5 F#4+F#5:.5 E4+E5:.5 C#4+C#5:.5 D4+D5:1
Eb4+Eb5:.5 F4+F5:.5 G4+G5:.5 Bb4+Bb5:.5 Ab4+Ab5:.5 G4+G5:.5 F4+F5:.5 D4+D5:.5 Eb4+Eb5:1
E4+E5:.5 F#4+F#5:.5 G#4+G#5:.5 B4+B5:.5 A4+A5:.5 G#4+G#5:.5 F#4+F#5:.5 D4+D5:.5 E4+E5:1
F#4+F#5:.5 A4+A5:.5 G#4+G#5:.5 E4+E5:.5 D4+D5:.5 C#4+C#5:.5 E4+E5:1 R:1
'''+ '\n'.join(' '.join(f'{n}:.5' if ':' not in n else n for n in row.split()) for row in '''A4+C#5 B4+D5 C#5+E5 B4+D5 A4+C#5 G#4+B4
G#4+B4 A4+C#5 B4+D5 A4+C#5 G#4+B4 F#4+A4
F#4+A4 G#4+B4 A4+C#5 G#4+B4 F#4+A4 E4+G#4
G4+Bb4 A4+C5 Bb4+D5 A4+C5 G4+Bb4 F4+A4
G#4+B4 A4+C#5 B4+D5 A4+C#5 G#4+B4 F#4+A4
A4+C#5 G#4+B4 F#4+A4 E4+G#4 R:1'''.splitlines())+'''
F#4+F#5:1.5 A4+A5:.5 G#4+G#5:1 C#5+C#6:1
B4+B5:1 A4+A5:.5 F#4+F#5:.5 E4+E5:2
D4+D5:1 E4+E5:.5 F#4+F#5:.5 A4+A5:1 G#4+G#5:1
F#4+F#5:1 E4+E5:.5 C#4+C#5:.5 D4+D5:2
E4+E5:2 G#4+G#5:1 R:1
F#4+A4+C#5:4
''',lh='\n'.join(' '.join(f'{n}:.25' if ':' not in n else n for n in row.split()) for row in '''F#2 A2 C#3 E3 F#3 A3 C#4 B3 A3 F#3 E3 C#3 B2 C#3 E3 C#3
E2 G#2 B2 D3 E3 G#3 B3 A3 G#3 E3 D3 B2 A2 B2 D3 B2
D2 F#2 A2 C#3 D3 F#3 A3 G#3 F#3 D3 C#3 A2 G#2 A2 C#3 A2
C#2 E2 G#2 B2 C#3 E3 G#3 F#3 E3 C#3 B2 G#2 A2 B2 C#3 E3
B2 D3 F#3 A3 B3 D4 F#4 E4 D4 B3 A3 F#3 E3 F#3 A3 F#3
C#3 E3 G#3 B3 G#3 E3 F#3 A3 G#3 B3 A3 F#3 R:1
F#2 A2 C#3 E3 F#3 A3 C#4 B3 A3 F#3 E3 C#3 B2 C#3 E3 F#3 A3 G#3 E3 C#3
E2 G#2 B2 D3 E3 G#3 B3 A3 G#3 E3 D3 B2 A2 B2 D3 E3 G#3 F#3 D3 B2
D2 F#2 A2 C#3 D3 F#3 A3 G#3 F#3 D3 C#3 A2 G#2 A2 C#3 D3 F#3 E3 C#3 A2
C2 Eb2 G2 Bb2 C3 Eb3 G3 F3 Eb3 C3 Bb2 G2 F2 G2 Bb2 C3 Eb3 D3 Bb2 G2
B1 D2 F#2 A2 B2 D3 F#3 E3 D3 B2 A2 F#2 E2 F#2 A2 B2 D3 C#3 A2 F#2
C#2 E2 G#2 B2 C#3 E3 G#3 F#3 E3 C#3 B2 G#2 F#2 A2 C#3 E3 R:1'''.splitlines())+'''
F#2+F#3:1 A2+A3:.5 G#2+G#3:.5 C#3+C#4:1
E2+E3:1 G#2+G#3:.5 F#2+F#3:.5 B2+B3:1
D2+D3:1 F#2+F#3:.5 E2+E3:.5 A2+A3:1
Eb2+Eb3:1 G2+G3:.5 F2+F3:.5 Bb2+Bb3:1
E2+E3:1 G#2+G#3:.5 F#2+F#3:.5 B2+B3:1
C#2+C#3:1 F#2+F#3:1 R:1
'''+ '\n'.join(' '.join(f'{n}:.25' for n in row.split()) for row in '''D2 F#2 A2 C#3 D3 F#3 A3 G#3 F#3 D3 C#3 A2 G#2 A2 C#3 A2
E2 G#2 B2 D3 E3 G#3 B3 A3 G#3 E3 D3 B2 A2 B2 D3 F#2
B1 D2 F#2 A2 B2 D3 F#3 E3 D3 B2 A2 F#2 G#2 A2 B2 G#2
C#2 E2 G#2 B2 C#3 E3 G#3 F#3 E3 C#3 B2 G#2 A2 B2 C#3 E3'''.splitlines())+'''
E3+B3:2 D3+A3:1 R:1
A2+E3:4''',sections={1:'p',7:'mp',13:'p',19:'p',23:'pp'},lower_sections={1:'pp',13:'p',19:'pp'},words={21:'poco rit.'},slurs=[(1,6),(7,12),(19,23)],lower_phrases=[(13,18)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[start,start+length-(1 if i in [5,11,17,22] else 0)-.2] for i,(start,length) in enumerate(zip([0,4,8,12,16,20,24,29,34,39,44,49,54,57,60,63,66,69,72,76,80,84,88,92],[4]*6+[5]*6+[3]*6+[4]*6))],
 performance=dict(rubato=[50,52,51,50,52,44,53,54,53,52,51,43,52,53,52,51,52,43,51,52,48,45,39,29],phrase_arcs=[[0,23,4],[24,53,5],[72,91,3]],lower_entries=[[54,71]],pedal_lift=.2,gate=.97,note='The upper octaves sing over light sixteenths. Give the LH octave answer the same warmth, then release the growing phrase into A major.')),
dict(op=230,title='Velvet Lattice',key='Eb',fifths=-3,meter='4/4',bpm=68,
 description='The descending phrase from Velvet Arrival is threaded through held tones, unequal pulses, paired notes and fine inner movement. The song returns closer to the middle register before a final flowing ascent releases it into an E-flat-major ninth.',
 difficulty='Advanced synthesis of layered voicing, cross-rhythm and double notes',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='The opening triplets lie beneath a duple inner line and a held soprano. The paired-note passage requires a clear upper edge; later inner sixteenths stay lighter than the held top note. Preserve the change of character as the triplets move to RH near the end.',
 parent_opus=220,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['Eb','D','C','Bb']),ancestry=dict(source_opus=220,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),
 system_starts=list(range(1,37,2)),page_starts=[7,13,19,25,31],engraving=dict(spacing_system=18,spacing_staff=24,pedal_offset_y=590),
 tuplet_spans=[dict(hand=h,start_beat=i*4+j,end_beat=i*4+j+1,actual=3,normal=2,stem='up' if h=='lh' else 'down') for h,bars in [('lh',list(range(2,8))),('rh',list(range(26,32)))] for i in bars for j in range(3 if i in [7,31] else 4)],
 rh='''Eb5:1 D5:1 C5:1 Bb4:1
Ab4:1 C5:1 Eb5:1 D5:1
G5:4
F5:4
Eb5:4
F5:4
G5:4
Eb5:3 R:1
'''+ '\n'.join(' '.join(f'{n}:.5' if ':' not in n else n for n in row.split()) for row in '''G4+Bb4 Ab4+C5 Bb4+D5 C5+Eb5 D5+F5 C5+Eb5 Bb4+D5 Ab4+C5
F4+Ab4 G4+Bb4 Ab4+C5 Bb4+D5 C5+Eb5 Bb4+D5 Ab4+C5 G4+Bb4
Eb4+G4 F4+Ab4 G4+Bb4 Ab4+C5 Bb4+D5 Ab4+C5 G4+Bb4 F4+Ab4
F4+Ab4 G4+Bb4 Ab4+C5 Bb4+Db5 C5+Eb5 Bb4+Db5 Ab4+C5 G4+Bb4
G4+B4 A4+C5 B4+D5 C5+E5 D5+F5 C5+E5 B4+D5 A4+C5
G4+Bb4 F4+Ab4 Eb4+G4 F4+Ab4 G4+Bb4 Eb4+G4 R:1'''.splitlines())+'''
Eb5:4
F5:4
G5:4
Ab5:4
G5:4
Eb5:3 R:1
Eb5:1 D5:1 C5:1 Bb4:1
Ab4:1 C5:1 Eb5:1 D5:1
C5:1 Eb5:.5 G5:.5 F5:1 Eb5:1
D5:1 F5:.5 Ab5:.5 G5:1 F5:1
Eb5:1 D5:.5 C5:.5 Bb4:1 Ab4:1
G4:1 Bb4:1 C5:1 R:1
'''+ '\n'.join(' '.join(f'{n}:1/3' if ':' not in n else n for n in row.split()) for row in '''Eb5 G5 Bb5 D6 Bb5 G5 F5 D5 Bb4 D5 F5 Ab5
F5 Ab5 C6 Eb6 C6 Ab5 G5 Eb5 C5 Eb5 G5 Bb5
G5 Bb5 D6 F6 D6 Bb5 Ab5 F5 D5 F5 Ab5 C6
Ab5 C6 Eb6 G6 Eb6 C6 Bb5 G5 Eb5 G5 Bb5 D6
Bb5 Ab5 G5 F5 Eb5 D5 C5 Bb4 G4 Bb4 D5 F5
Eb5 G5 Bb5 Ab5 F5 D5 Eb5 D5 Bb4 R:1'''.splitlines())+'''
Eb5:2 D5:2
C5:2 Bb4:2
Ab4:2 Bb4:1 R:1
Eb5:4
''',rh_inner='''R:4
R:4
'''+ '\n'.join(' '.join(f'{n}:.5' if ':' not in n else n for n in row.split()) for row in '''G4 Bb4 D5 F5 Eb5 D5 Bb4 G4
F4 A4 C5 Eb5 Db5 C5 A4 F4
Eb4 G4 Bb4 D5 C5 Bb4 G4 Eb4
F4 Ab4 C5 Eb5 Db5 C5 Ab4 F4
G4 B4 D5 F5 Eb5 D5 B4 G4
Eb4 G4 Bb4 D5 C5 Bb4 R:1'''.splitlines())+'''
R:4
R:4
R:4
R:4
R:4
R:4
'''+ '\n'.join(' '.join(f'{n}:.25' if ':' not in n else n for n in row.split()) for row in '''G4 Bb4 D5 C5 Bb4 Ab4 G4 Ab4 Bb4 D5 C5 Bb4 Ab4 G4 F4 G4
Ab4 C5 Eb5 D5 C5 Bb4 Ab4 Bb4 C5 Eb5 D5 C5 Bb4 Ab4 G4 Ab4
Bb4 D5 F5 Eb5 D5 C5 Bb4 C5 D5 F5 Eb5 D5 C5 Bb4 Ab4 Bb4
C5 Eb5 G5 F5 Eb5 Db5 C5 Db5 Eb5 G5 F5 Eb5 Db5 C5 Bb4 C5
B4 D5 F5 E5 D5 C5 B4 C5 D5 F5 E5 D5 C5 B4 A4 B4
G4 Bb4 D5 C5 Bb4 Ab4 G4 Ab4 Bb4 D5 C5 Bb4 R:1'''.splitlines())+'''
G4:1 F4:1 Eb4:1 D4:1
F4:1 Ab4:1 C5:1 Bb4:1
G4:1 Bb4:.5 D5:.5 C5:1 Bb4:1
Bb4:1 D5:.5 F5:.5 Eb5:1 D5:1
G4:1 F4:.5 Eb4:.5 D4:1 C4:1
Eb4:1 G4:1 Ab4:1 R:1
R:4
R:4
R:4
R:4
R:4
R:4
G4+Bb4:2 F4+Ab4:2
Eb4+G4:2 D4+F4:2
C4+Eb4:2 D4+F4:1 R:1
G4+Bb4+D5:4
''',lh='''Eb3:2 Bb3:1 G3:1
Ab2:2 Eb3:1 C3:1
'''+ '\n'.join(' '.join(f'{n}:1/3' if ':' not in n else n for n in row.split()) for row in '''Eb3 G3 Bb3 D4 Bb3 G3 F3 G3 Bb3 Ab3 F3 D3
Bb2 D3 F3 A3 F3 D3 C3 D3 F3 Eb3 C3 A2
C3 Eb3 G3 Bb3 G3 Eb3 D3 Eb3 G3 F3 D3 Bb2
Db3 F3 Ab3 C4 Ab3 F3 Eb3 F3 Ab3 Gb3 Eb3 C3
G3 B3 D4 F4 D4 B3 A3 B3 D4 C4 A3 F3
C3 Eb3 G3 Bb3 G3 Eb3 F3 D3 Bb2 R:1'''.splitlines())+ '\n'+'\n'.join(' '.join(f'{n}:.5' if ':' not in n else n for n in row.split()) for row in '''Eb3 G3 Bb3 Ab3 F3 G3 Ab3 F3
D3 F3 Ab3 G3 Eb3 F3 G3 Eb3
C3 Eb3 G3 F3 D3 Eb3 F3 D3
Db3 F3 Ab3 Gb3 Eb3 F3 Gb3 Eb3
G2 B2 D3 F3 E3 D3 C3 B2
C3 Eb3 G3 Bb3 G3 Eb3 R:1'''.splitlines())+'''
C3:1 G3:1 Eb3:1 G3:1
F3:1 C4:1 Ab3:1 C4:1
Eb3:1 Bb3:1 G3:1 Bb3:1
Ab3:1 Eb4:1 C4:1 Eb4:1
G3:1 D4:1 B3:1 D4:1
C3:1 G3:1 Eb3:1 R:1
Ab2:1 Eb3:1 C3:1 Eb3:1
F3:1 C4:1 Ab3:1 C4:1
Eb3:1 Bb3:1 G3:1 Bb3:1
Bb2:1 F3:1 D3:1 F3:1
C3:1 G3:1 Eb3:1 G3:1
C3:1 G3:1 Eb3:1 R:1
'''+ '\n'.join(' '.join(f'{n}:.5' if ':' not in n else n for n in row.split()) for row in '''Eb3 G3 Bb3 Ab3 F3 G3 Ab3 F3
F3 Ab3 C4 Bb3 G3 Ab3 Bb3 G3
G3 Bb3 D4 C4 A3 Bb3 C4 A3
Ab3 C4 Eb4 Db4 Bb3 C4 Db4 Bb3
G3 F3 Eb3 D3 C3 Eb3 G3 F3
C3 Eb3 G3 Bb3 G3 Eb3 R:1'''.splitlines())+'''
C3+G3:2 Bb2+F3:2
Ab2+Eb3:2 G2+D3:2
F2+C3:2 Bb2+F3:1 R:1
Eb3+Bb3:4''',hidden_voice_rests=dict(inner=[1,2]+list(range(9,15))+list(range(27,33))),
 sections={1:'p',3:'p',9:'mp',15:'p',21:'p',27:'mp',33:'pp'},lower_sections={1:'pp',27:'p',33:'pp'},words={33:'poco rit.'},slurs=[(1,2),(9,14),(21,26),(27,32)],hairpins=[],tempo_changes={},group=3,
 voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=3) for a,b in [(8,31),(56,79),(80,103)]],
 pedal_spans=[[i*4+a,i*4+b-.2] for i in range(36) for a,b in ([(0,4)] if i==35 else [(0,2),(2,3 if i in [7,13,19,25,31,34] else 4)])],
 performance=dict(rubato=[68,67,70,71,70,69,71,58,72,73,72,71,72,59,70,71,72,73,71,58,68,69,70,71,68,57,73,74,75,76,70,57,54,49,42,30],phrase_arcs=[[0,8,3],[32,55,4],[80,103,4],[104,127,5]],lower_entries=[[104,127]],inner_entries=[[8,31],[56,79]],pedal_lift=.2,gate=.98,note='The held soprano, singing inner line and triplet bass keep distinct weights. Their reunion near the end grows warmer rather than louder; the final major ninth receives a long unhurried release.')),
dict(op=231,title='Sedge Pendulum',key='d',fifths=-1,meter='4/4',bpm=58,final_fermata=False,
 description='A five-note ground moves across four-beat bars beneath a melody that takes its own longer breaths. The ground changes colour through G minor, E-flat and a warmer F-major opening. Its last return loses notes until only a small descending phrase remains, still in tempo.',
 difficulty='Advanced independence over displaced five-note grounds',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='The opening LH repeats D–A–C–F–E in even eighths across five bars; its starts migrate through the metre. Project the slower RH phrase without accenting each restart of the ground. Later bass patterns change with the harmony; the last five bars progressively thin the texture.',
 parent_opus=221,motif=dict(hand='rh',start_beat=0,end_beat=8,pitches=['D','F','E','A']),ancestry=dict(source_opus=221,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),
 system_starts=list(range(1,31,2)),page_starts=[9,17,25],engraving=dict(spacing_system=18,spacing_staff=15,pedal_offset_y=560),
 rh='''D5:2 F5:1 E5:1~
E5:1 A5:3
G5:1 E5:.5 F5:.5 D5:2~
D5:1 C5:1 A4:1 G4:1
A4:2 C5:1 R:1
D5:1.5 F5:.5 A5:2
Bb5:1 A5:1 G5:2~
G5:1 F5:.5 Eb5:.5 D5:1 C5:1
Bb4:1 D5:1 F5:2
G5:2 F5:1 Eb5:1~
Eb5:1 D5:1 C5:1 Bb4:1
A4:1 C5:1 D5:1 R:1
E5:2 G5:1 A5:1~
A5:2 G5:1 F5:1
E5:1 D5:1 C5:1 A4:1
G4:2 A4:1 R:1
F5:1 A5:.5 G5:.5 E5:2
D5:1 F5:.5 E5:.5 C5:2
Bb4:1 D5:.5 C5:.5 A4:2
G4:1 Bb4:.5 A4:.5 F4:2
E4:1 G4:1 A4:2
C5:1 E5:1 F5:2
A5:1 G5:.5 F5:.5 E5:2
D5:1 C5:1 A4:2
G4:1 A4:1 C5:1 R:1
D5:2 F5:1 E5:1
A5:2 G5:1 E5:1
D5:2 C5:2
A4:2 G4:1 R:1
D5:1 C5:1 A4:2''',
 lh='''D3:.5 A3:.5 C4:.5 F3:.5 E3:.5 D3:.5 A3:.5 C4:.5
F3:.5 E3:.5 D3:.5 A3:.5 C4:.5 F3:.5 E3:.5 D3:.5
A3:.5 C4:.5 F3:.5 E3:.5 D3:.5 A3:.5 C4:.5 F3:.5
E3:.5 D3:.5 A3:.5 C4:.5 F3:.5 E3:.5 D3:.5 A3:.5
C4:.5 F3:.5 E3:.5 D3:.5 A3:.5 C4:.5 F3:.5 E3:.5
G3:.5 D4:.5 F4:.5 Bb3:.5 A3:.5 G3:.5 D4:.5 F4:.5
Bb3:.5 A3:.5 G3:.5 D4:.5 F4:.5 Bb3:.5 A3:.5 G3:.5
Eb3:.5 Bb3:.5 D4:.5 G3:.5 F3:.5 Eb3:.5 Bb3:.5 D4:.5
G3:.5 F3:.5 Eb3:.5 Bb3:.5 D4:.5 G3:.5 F3:.5 Eb3:.5
C3:.5 G3:.5 Bb3:.5 Eb3:.5 D3:.5 C3:.5 G3:.5 Bb3:.5
Eb3:.5 D3:.5 C3:.5 G3:.5 Bb3:.5 Eb3:.5 D3:.5 C3:.5
A2:.5 E3:.5 G3:.5 C3:.5 E3:.5 G3:.5 R:1
F3:1 C4:.5 A3:.5 G3:1 A3:1
C3:1 G3:.5 E3:.5 D3:1 E3:1
Bb2:1 F3:.5 D3:.5 C3:1 D3:1
C3:1 G3:.5 E3:.5 F3:1 R:1
F3:.5 C4:.5 E4:.5 A3:.5 G3:.5 F3:.5 C4:.5 E4:.5
A3:.5 G3:.5 F3:.5 C4:.5 E4:.5 A3:.5 G3:.5 F3:.5
D3:.5 A3:.5 C4:.5 F3:.5 E3:.5 D3:.5 A3:.5 C4:.5
F3:.5 E3:.5 D3:.5 A3:.5 C4:.5 F3:.5 E3:.5 D3:.5
C3:.5 G3:.5 Bb3:.5 E3:.5 D3:.5 C3:.5 G3:.5 Bb3:.5
F3:.5 C4:.5 E4:.5 A3:.5 G3:.5 F3:.5 C4:.5 E4:.5
Bb3:.5 F4:.5 A4:.5 D4:.5 C4:.5 Bb3:.5 F3:.5 A3:.5
G3:.5 D4:.5 F4:.5 Bb3:.5 A3:.5 G3:.5 D3:.5 F3:.5
C3:.5 G3:.5 Bb3:.5 E3:.5 G3:.5 Bb3:.5 R:1
D3:.5 A3:.5 C4:.5 F3:.5 E3:.5 D3:.5 A3:.5 C4:.5
F3:.5 E3:.5 D3:.5 A3:.5 C4:1 A3:1
F3:1 E3:1 D3:2
A2:1 D3:1 R:2
R:4''',
 sections={1:'p',6:'mp',13:'p',17:'p',22:'mp',26:'pp'},lower_sections={1:'pp',22:'p',26:'pp'},words={},slurs=[(1,5),(6,12),(13,16),(17,21),(22,25),(26,28),(30,30)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*4+a,i*4+b-.18] for i in range(29) for a,b in ([(0,2)] if i==28 else [(0,2),(2,3 if i in [11,15,24] else 4)])],
 performance=dict(rubato=[58,59,59,58,55,59,60,60,59,58,58,54,60,61,60,56,60,61,61,60,59,61,62,61,56,58,58,58,58,58],phrase_arcs=[[0,19,3],[20,47,5],[48,63,3],[64,83,4],[84,99,5],[100,112,2]],lower_entries=[],pedal_lift=.18,gate=.98,note='Let the ground pass through the bar lines without added accents. The melody breathes across it; the last solitary phrase keeps the original pulse.')),
dict(op=232,title='Myrtle Escalier',key='e',fifths=1,meter='7/8',bpm=54,
 description='Three-note stairways drift through seven-eighth bars. A long E-minor song gathers paired notes, is briefly answered by the bass, and climbs towards a warmer C-major vista. The final suspension holds the door open on the dominant.',
 difficulty='Advanced irregular-metre ostinato and paired-note cantabile',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=12),technical_note='The first nine bars use three-note LH cells across seven-eighth measures, changing their starting position each bar. The released LH move from B3 to C3 at bar 4 is eleven semitones with about half a second between attacks; prepare the hand at each change of ground. Later paired RH voices need an even upper melody. Bars 15–21 exchange the melodic weight between hands; do not turn every seven-eighth bar into an accented dance step.',
 parent_opus=225,motif=dict(hand='rh',start_beat=0,end_beat=3.5,pitches=['E','G','F#','B']),ancestry=dict(source_opus=225,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=5,source_pitches=['E','G','F#','B'],transposition_semitones=0),
 system_starts=list(range(1,35,2)),page_starts=[9,17,25,31],engraving=dict(spacing_system=18,spacing_staff=16,pedal_offset_y=560),
 rh='''E5:1 G5:.5 F#5:1 B5:1
A5:1 G5:.5 E5:2~
E5:1 D5:1 B4:1.5
C5:1 E5:.5 G5:2
F#5:1 E5:.5 D5:1 B4:1
A4:1 C5:.5 E5:1 F#5:1
G5:1 B5:.5 A5:2
F#5:1 A5:.5 G5:1 E5:1
D5:1 F#5:.5 E5:1 R:1
G4+B4:1 A4+C5:.5 B4+D5:2
C5+E5:1 B4+D5:.5 A4+C5:2
G4+B4:1 F#4+A4:.5 E4+G4:1 D4+F#4:1
E4+G4:1 F#4+A4:.5 G4+B4:2
A4+C5:1 B4+D5:.5 G4+B4:1 R:1
B4:3.5
C5:3.5
D5:3.5
C5:3.5
B4:2 A4:1.5
G4:1 B4:.5 A4:1 F#4:1
E4:2 R:1.5
E5:1 G5:.5 F#5:1 B5:1
C6:1 B5:.5 G5:2
A5:1 G5:.5 E5:1 D5:1
F#5:.5 G5:.5 A5:.5 B5:1 D6:1
C6:1 B5:.5 A5:1 G5:1
F#5:.5 A5:.5 G5:.5 E5:1 D5:1
C5:1 E5:.5 G5:2
F#5:1 D5:.5 B4:1 R:1
E5:1 G5:.5 F#5:2
D5:1 C5:.5 B4:2
A4:1 C5:.5 E5:1 F#5:1
G5:1 E5:.5 D#5:1 C#5:1
A4+D#5+F#5:3.5''',
 lh='''E3:.5 G3:.5 B3:.5 E3:.5 G3:.5 B3:.5 E3:.5
G3:.5 B3:.5 E3:.5 G3:.5 B3:.5 E3:.5 G3:.5
B3:.5 E3:.5 G3:.5 B3:.5 E3:.5 G3:.5 B3:.5
C3:.5 E3:.5 G3:.5 C3:.5 E3:.5 G3:.5 C3:.5
E3:.5 G3:.5 C3:.5 E3:.5 G3:.5 C3:.5 E3:.5
G3:.5 C3:.5 E3:.5 G3:.5 C3:.5 E3:.5 G3:.5
A2:.5 C3:.5 E3:.5 A2:.5 C3:.5 E3:.5 A2:.5
C3:.5 E3:.5 A2:.5 C3:.5 E3:.5 A2:.5 C3:.5
B2:.5 D#3:.5 F#3:.5 B2:.5 D#3:.5 F#3:.5 R:.5
G2:1 D3:.5 G3:1 F#3:1
A2:1 E3:.5 A3:1 G3:1
B2:1 F#3:.5 D3:1 B2:1
C3:1 G3:.5 E3:1 C3:1
D3:1 A3:.5 F#3:1 R:1
E3:1 G3:.5 F#3:1 B3:1
A3:1 G3:.5 E3:2
D3:1 F#3:.5 A3:1 B3:1
C4:1 B3:.5 A3:1 G3:1
F#3:1 A3:.5 G3:1 E3:1
D3:1 F#3:.5 B3:1 A3:1
G3:1 E3:1 R:1.5
C3:.5 E3:.5 G3:.5 C3:.5 E3:.5 G3:.5 C3:.5
E3:.5 G3:.5 C3:.5 E3:.5 G3:.5 C3:.5 E3:.5
A2:.5 C3:.5 E3:.5 A2:.5 C3:.5 E3:.5 A2:.5
D3:.5 F#3:.5 A3:.5 D3:.5 F#3:.5 A3:.5 D3:.5
G3:.5 B3:.5 D4:.5 G3:.5 B3:.5 D4:.5 G3:.5
F#3:.5 A3:.5 C4:.5 F#3:.5 A3:.5 C4:.5 F#3:.5
E3:.5 G3:.5 B3:.5 E3:.5 G3:.5 B3:.5 E3:.5
B2:.5 D#3:.5 F#3:.5 B2:.5 D#3:.5 R:1
C3+G3:1.5 E3+B3:2
B2+F#3:1.5 D3+A3:2
A2+E3:1.5 C3+G3:2
B2+F#3:1.5 A3:1 F#3:1
B2+F#3:3.5''',
 sections={1:'p',10:'mp',15:'pp',22:'mp',30:'p',34:'pp'},lower_sections={1:'pp',15:'p',22:'pp'},words={},slurs=[(1,3),(4,6),(7,9),(10,14),(20,21),(22,24),(25,29),(30,34)],lower_phrases=[(15,18),(19,21)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*3.5+a,i*3.5+b-.16] for i in range(34) for a,b in ([(0,2)] if i==20 else [(0,3.5)] if i==33 else [(0,1.5),(1.5,2.5 if i in [13,28] else 3 if i==8 else 3.5)])],
 performance=dict(rubato=[54,55,53,54,55,54,56,55,50,55,56,55,54,50,54,55,56,55,54,53,48,56,57,56,58,58,56,55,49,53,53,52,50,43],phrase_arcs=[[0,10.5,3],[10.5,21,3],[21,31,4],[31.5,48,4],[73.5,84,4],[84,100.5,5],[101.5,115.5,2]],lower_entries=[[49,72]],pedal_lift=.16,gate=.98,note='The three-note ground turns quietly through the changing accents. Bring the bass song forward when it appears; let the final dominant suspension remain expectant.')),
dict(op=233,title='Pearl Switchyard',key='b',fifths=2,meter='5/4',bpm=58,final_fermata=False,
 description='A sustained song is lit from within by small oscillating figures, while the bass crosses the five-beat bar with longer pulses. A quiet chordal reflection interrupts the machinery. The upper voices eventually disappear, leaving the ancestral phrase alone in the bass.',
 difficulty='Advanced three-voice balance and displaced dotted-quarter bass',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Hold the upper melody while the inner RH voice moves independently. The dotted-quarter LH pulses cross the first three five-beat bars with written ties. The later bass-only ending retains the pulse and its original unadorned contour.',
 parent_opus=224,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=5,pitches=['B','D','C#','A']),ancestry=dict(source_opus=224,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['B','D','C#','A'],transposition_semitones=0),
 system_starts=list(range(1,26,2)),page_starts=[7,13,19],engraving=dict(spacing_system=18,spacing_staff=23,pedal_offset_y=600),
 rh='''B4:1 D5:1 C#5:1 A4:2
G4:1 B4:1 D5:2 C#5:1
B4:2 A4:1 F#4:1 R:1
D5:5
E5:3 D5:2
F#5:5
E5:3 C#5:2
D5:3 E5:2
F#5:3 E5:2
D5:2 C#5:2 R:1
F#4+B4+D5:3 E4+A4+C#5:2
E4+G4+B4:2 F#4+A4+C#5:3
G4+B4+D5:3 F#4+A4+C5:2
E4+G4+B4:2 D4+F#4+A4:2 R:1
F#5:5
G5:3 F#5:2
A5:5
G5:3 E5:2
F#5:2 E5:1 D5:2
C#5:2 B4:2 R:1
B4:2 D5:1 C#5:2
A4:3 G4:2
F#4:3 R:2
R:5
R:5''',rh_inner='''R:5
R:5
R:5
F#4:.5 A4:.5 C#5:1 A4:.5 F#4:.5 A4:1 C#5:1
G4:.5 B4:.5 D5:1 B4:.5 G4:.5 A4:1 B4:1
A4:.5 C#5:.5 E5:1 C#5:.5 A4:.5 B4:1 C#5:1
G4:.5 B4:.5 D5:1 B4:.5 G4:.5 E4:1 G4:1
F#4:.5 A4:.5 C#5:1 A4:.5 F#4:.5 G4:1 B4:1
A4:.5 C#5:.5 E5:1 C#5:.5 A4:.5 G4:1 B4:1
F#4:.5 A4:.5 B4:1 G4:1 E4:1 R:1
R:5
R:5
R:5
R:5
A4:.5 C#5:.5 E5:1 C#5:.5 A4:.5 B4:1 C#5:1
B4:.5 D5:.5 F#5:1 D5:.5 B4:.5 A4:1 C#5:1
C#5:.5 E5:.5 G5:1 E5:.5 C#5:.5 D5:1 E5:1
B4:.5 D5:.5 F#5:1 D5:.5 B4:.5 G4:1 B4:1
A4:.5 C#5:.5 E5:1 G4:1 F#4:2
E4:1 G4:1 F#4:2 R:1
F#4:2 A4:1 G4:2
E4:3 D4:2
R:5
R:5
R:5''',lh='''B2:1.5 F#3:1.5 A3:1.5 F#3:.5~
F#3:1 B2:1.5 F#3:1.5 A3:1~
A3:.5 F#3:1.5 B2:1.5 F#3:1.5
B2:1.5 F#3:1.5 A3:2
C3:1.5 G3:1.5 B3:2
D3:1.5 A3:1.5 C#4:2
E3:1.5 B3:1.5 G3:2
G2:1.5 D3:1.5 F#3:2
A2:1.5 E3:1.5 G3:2
B2:1.5 F#3:1.5 A3:1 R:1
G2+D3:3 A2+E3:2
C3+G3:2 D3+A3:3
Eb3+Bb3:3 D3+A3:2
C3+G3:2 B2+F#3:2 R:1
D3:.5 A3:.5 C#4:.5 F#3:.5 E3:1 F#3:1 A3:1
E3:.5 B3:.5 D4:.5 G3:.5 F#3:1 G3:1 B3:1
F#3:.5 C#4:.5 E4:.5 A3:.5 G3:1 A3:1 C#4:1
G3:.5 D4:.5 F#4:.5 B3:.5 A3:1 B3:1 D4:1
D3:.5 A3:.5 C#4:.5 F#3:.5 G3:1 B3:1 D3:1
E3:1 B3:1 F#3:2 R:1
G2:1.5 D3:1.5 F#3:2
C3:1.5 G3:1.5 B3:2
B2:1.5 F#3:1.5 A3:2
B3:1 D4:1 C#4:1 A3:2
B2:1 D3:1 C#3:1 A2:2''',
 hidden_voice_rests=dict(inner=[1,2,3,11,12,13,14,23]),sections={1:'p',4:'p',11:'pp',15:'mp',21:'pp'},lower_sections={1:'pp',15:'p',21:'pp',24:'p'},words={},slurs=[(1,3),(11,14),(19,22)],lower_phrases=[(24,24),(25,25)],hairpins=[],tempo_changes={},group=3,
 voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=3) for a,b in [(15,30),(30,49),(70,90),(90,99)]],
 pedal_spans=[[i*5+a,i*5+b-.2] for i in range(23) for a,b in ([(0,2),(2,4)] if i in [9,13,19] else [(0,3),(3,5)])],
 performance=dict(rubato=[58,59,55,58,60,61,59,60,61,53,53,54,52,49,61,62,64,62,60,54,56,56,56,56,56],phrase_arcs=[[0,14,3],[15,35,3],[35,49,4],[50,69,2],[70,95,5],[100,115,2]],lower_entries=[[115,125]],inner_entries=[[15,49],[70,99]],pedal_lift=.2,gate=.98,note='Keep the moving inner voice feather-light beneath the held song. The final two bass phrases are plain and evenly paced, the second an octave lower.')),
dict(op=234,title='Juniper Viaduct',key='c',fifths=-3,meter='11/8',bpm=57,
 description='An uneven long-short ground carries a broad minor melody over eleven-eighth bars. A more fluid passage sends five notes across two beats, then leaves the tune suspended above the bass. The final return takes a different road into a quiet F-minor sixth.',
 difficulty='Advanced asymmetric lilt, quintuplet release and harmonic voicing',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='The bass outlines three long-short pairs and a final quarter. In bars 10–15, five RH eighth-note quintuplets occupy two quarter beats before a held arrival. Keep the long upper arrivals singing while the LH maintains its uneven cycle.',
 parent_opus=228,motif=dict(hand='rh',start_beat=0,end_beat=5.5,pitches=['C','Eb','D','Bb']),ancestry=dict(source_opus=228,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['C','Eb','D','Bb'],transposition_semitones=0),
 system_starts=list(range(1,23,2)),page_starts=[7,13,19],engraving=dict(spacing_system=18,spacing_staff=16,pedal_offset_y=560),
 tuplet_spans=[dict(hand='rh',start_beat=i*5.5,end_beat=i*5.5+2,actual=5,normal=4,stem='down',show_number='both') for i in range(9,15)],
 rh='''C5:1.5 Eb5:1 D5:1 Bb4:2
Ab4:2 C5:1 Eb5:1.5 F5:1
G5:2 F5:1 Eb5:1 D5:1.5
C5:1.5 D5:.5 Eb5:1 G5:1 F5:1.5
Eb5:2 D5:1 C5:1.5 R:1
F4+Ab4+C5:1.5 G4+Bb4+D5:1.5 Ab4+C5+Eb5:2.5
G4+Bb4+D5:2 F4+Ab4+C5:1.5 Eb4+G4+Bb4:2
F4+Ab4+Db5:1.5 G4+Bb4+Eb5:1.5 Ab4+C5+F5:2.5
G4+Bb4+Eb5:2 F4+Ab4+Db5:1.5 R:2
C5:2/5 Eb5:2/5 G5:2/5 Bb5:2/5 Ab5:2/5 G5:3.5
D5:2/5 F5:2/5 Ab5:2/5 C6:2/5 Bb5:2/5 A5:3.5
Eb5:2/5 G5:2/5 Bb5:2/5 D6:2/5 C6:2/5 Bb5:3.5
F5:2/5 Ab5:2/5 C6:2/5 Eb6:2/5 Db6:2/5 C6:3.5
G5:2/5 B5:2/5 D6:2/5 F6:2/5 Eb6:2/5 D6:3.5
C6:2/5 Bb5:2/5 Ab5:2/5 G5:2/5 F5:2/5 Eb5:2.5 R:1
C5:1.5 Eb5:1 D5:1 Bb4:2
Ab4:2 C5:1 Eb5:1.5 D5:1
Db5:2 F5:1 Ab5:1.5 G5:1
F5:1.5 Eb5:.5 Db5:1 C5:1 Bb4:1.5
Ab4:2 C5:1 D5:1.5 F5:1
Eb5:2 D5:1 C5:1.5 R:1
Ab4+C5+D5:5.5''',
 lh='''C3:1 G3:.5 Bb3:1 G3:.5 Eb3:1 G3:.5 C3:1
Ab2:1 Eb3:.5 G3:1 Eb3:.5 C3:1 Eb3:.5 Ab2:1
Eb3:1 Bb3:.5 D4:1 Bb3:.5 G3:1 Bb3:.5 Eb3:1
Bb2:1 F3:.5 Ab3:1 F3:.5 D3:1 F3:.5 Bb2:1
C3:1 G3:.5 Bb3:1 G3:.5 Eb3:1 G3:.5 R:1
F3:1 C4:.5 Eb4:1 C4:.5 Ab3:1 C4:.5 F3:1
Eb3:1 Bb3:.5 D4:1 Bb3:.5 G3:1 Bb3:.5 Eb3:1
Db3:1 Ab3:.5 C4:1 Ab3:.5 F3:1 Ab3:.5 Db3:1
Bb2:1 F3:.5 Ab3:1 F3:.5 D3:.5 R:2
C3:.5 G3:.5 Bb3:.5 Eb3:.5 D3:.5 C3:.5 G3:.5 Bb3:.5 Ab3:.5 G3:.5 Eb3:.5
D3:.5 A3:.5 C4:.5 F3:.5 E3:.5 D3:.5 A3:.5 C4:.5 Bb3:.5 A3:.5 F3:.5
Eb3:.5 Bb3:.5 D4:.5 G3:.5 F3:.5 Eb3:.5 Bb3:.5 D4:.5 C4:.5 Bb3:.5 G3:.5
F3:.5 C4:.5 Eb4:.5 Ab3:.5 G3:.5 F3:.5 C4:.5 Eb4:.5 Db4:.5 C4:.5 Ab3:.5
G3:.5 D4:.5 F4:.5 B3:.5 A3:.5 G3:.5 D4:.5 F4:.5 E4:.5 D4:.5 B3:.5
C4:.5 Bb3:.5 Ab3:.5 G3:.5 F3:.5 Eb3:.5 D3:.5 C3:.5 G3:.5 R:1
Ab2:1 Eb3:.5 G3:1 Eb3:.5 C3:1 Eb3:.5 Ab2:1
F3:1 C4:.5 Eb4:1 C4:.5 Ab3:1 C4:.5 F3:1
Db3:1 Ab3:.5 C4:1 Ab3:.5 F3:1 Ab3:.5 Db3:1
Bb2:1 F3:.5 Ab3:1 F3:.5 Db3:1 F3:.5 Bb2:1
F3:1 C4:.5 D4:1 C4:.5 Ab3:1 C4:.5 F3:1
G3:1 C4:.5 Bb3:1 G3:.5 F3:1 Ab3:.5 R:1
F3+C4:5.5''',
 sections={1:'p',6:'pp',10:'mp',13:'mf',16:'p',20:'pp'},lower_sections={1:'pp',10:'p',16:'pp'},words={},slurs=[(1,5),(6,9),(10,12),(13,15),(16,19),(20,22)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*5.5+a,i*5.5+b-.18] for i in range(22) for a,b in ([(0,5.5)] if i==21 else [(0,1.5),(1.5,3),(3,3.5)] if i==8 else [(0,1.5),(1.5,3),(3,4.5 if i in [4,14,20] else 5.5)])],
 performance=dict(rubato=[57,58,59,57,51,55,56,56,49,59,60,61,62,63,52,57,58,58,55,54,49,42],phrase_arcs=[[0,26.5,4],[27.5,47.5,2],[49.5,66,4],[66,81.5,6],[82.5,104.5,3],[104.5,120,2]],lower_entries=[],pedal_lift=.18,gate=.98,note='The lilt stays light through the asymmetric metre. Let the quintuplet gestures open into long resonant notes; the altered return rests in F minor with an added sixth.')),
dict(op=235,title='Alder Flywheel',key='d',fifths=-1,meter='4/4',meters=['4/4']*8+['3/4']*6+['5/4']*6+['4/4']*8,bpm=54,final_fermata=False,
 description='A seven-note wheel of quiet sixteenths carries a broad song through ordinary bars. The music then contracts into three beats, opens into five, and recovers its first space with a changed melody. The wheel comes to rest on a short, clear major chord while the pulse is still moving.',
 difficulty='Advanced seven-note sixteenth ground and changing phrase metre',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='The first seven LH bars repeat the same seven-note cell continuously, so its beginnings travel across the four-beat bar. Keep the RH line slower and independent. Subsequent three-, five- and four-beat sections change the phrase space, with each signature change written explicitly.',
 parent_opus=231,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','F','E','A']),ancestry=dict(source_opus=231,source_hand='rh',source_start_beat=0,source_end_beat=8,source_pitches=['D','F','E','A'],transposition_semitones=0),
 system_starts=list(range(1,29,2)),page_starts=[7,13,19,25],engraving=dict(spacing_system=18,spacing_staff=16,pedal_offset_y=560),
 rh='''D5:.5 F5:.5 E5:1 A5:2
G5:1 F5:.5 E5:.5 D5:2~
D5:1 C5:1 A4:2
Bb4:1 D5:1 F5:2
E5:1 D5:.5 C5:.5 A4:2
G4:1 Bb4:1 D5:2
C5:1 E5:1 G5:2
F5:1 E5:1 D5:1 R:1
A4:1 C5:.5 E5:.5 D5:1
G4:1 Bb4:.5 D5:.5 C5:1
F4:1 A4:.5 C5:.5 Bb4:1
E4:1 G4:.5 Bb4:.5 A4:1
F4+A4+D5:1 E4+G4+C5:1 D4+F4+Bb4:1
E4+G4+C5:2 R:1
D5:2 F5:1 E5:2
A5:3 G5:2
F5:1 A5:.5 G5:.5 E5:1 D5:2
C5:1 E5:.5 D5:.5 Bb4:1 A4:2
G4:1 Bb4:.5 A4:.5 F4:1 E4:2
D4:2 F4:1 G4:1 R:1
A4:1 D5:.5 F5:.5 E5:2
G5:1 F5:.5 E5:.5 D5:2
C5:1 E5:.5 G5:.5 A5:2
Bb5:1 A5:.5 G5:.5 F5:2
E5:1 D5:.5 C5:.5 Bb4:2
A4:1 C5:.5 E5:.5 D5:2
C5:1 A4:1 F4:1 E4:1
F#4+A4+D5:2 R:2''',
 lh='\n'.join(' '.join(n+':.25' for n in ('D3 F3 A3 C4 A3 F3 E3'.split()*16)[i*16:(i+1)*16]) for i in range(7))+'''
D3:.5 F3:.5 A3:.5 C4:.5 A3:.5 F3:.5 R:1
F3:1 C4:.5 A3:.5 G3:1
Eb3:1 Bb3:.5 G3:.5 F3:1
D3:1 A3:.5 F3:.5 E3:1
C3:1 G3:.5 E3:.5 D3:1
Bb2+F3:1 C3+G3:1 D3+A3:1
C3+G3:2 R:1
Bb2:1 F3:.5 A3:.5 D3:1 C3:1 D3:1
G2:1 D3:.5 F3:.5 Bb2:1 A2:1 Bb2:1
F3:1 C4:.5 E4:.5 A3:1 G3:1 F3:1
Eb3:1 Bb3:.5 D4:.5 G3:1 F3:1 Eb3:1
Bb2:1 F3:.5 A3:.5 D3:1 C3:1 Bb2:1
A2:1 E3:.5 G3:.5 C3:1 E3:1 R:1
D3:.25 F3:.25 A3:.25 C4:.25 A3:.25 F3:.25 E3:.25 D3:.25 F3:.25 A3:.25 C4:.25 A3:.25 F3:.25 E3:.25 D3:.25 F3:.25
G3:.25 Bb3:.25 D4:.25 F4:.25 D4:.25 Bb3:.25 A3:.25 G3:.25 Bb3:.25 D4:.25 F4:.25 D4:.25 Bb3:.25 A3:.25 G3:.25 Bb3:.25
A3:.25 C4:.25 E4:.25 G4:.25 E4:.25 C4:.25 B3:.25 A3:.25 C4:.25 E4:.25 G4:.25 E4:.25 C4:.25 B3:.25 A3:.25 C4:.25
Bb3:.25 D4:.25 F4:.25 A4:.25 F4:.25 D4:.25 C4:.25 Bb3:.25 D4:.25 F4:.25 A4:.25 F4:.25 D4:.25 C4:.25 Bb3:.25 D4:.25
G3:.5 Bb3:.5 D4:.5 F4:.5 D4:.5 Bb3:.5 A3:.5 G3:.5
F3:.5 A3:.5 C4:.5 E4:.5 C4:.5 A3:.5 G3:.5 F3:.5
D3:1 A3:1 F3:1 E3:1
D3+A3:2 R:2''',
 sections={1:'p',9:'p',13:'pp',15:'p',21:'mp',25:'p',28:'pp'},lower_sections={1:'pp',21:'p',25:'pp'},words={},slurs=[(1,3),(4,8),(9,12),(13,14),(15,20),(21,24),(25,28)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[start+a,start+b-.16] for i,(start,length) in enumerate(zip([i*4 for i in range(8)]+[32+i*3 for i in range(6)]+[50+i*5 for i in range(6)]+[80+i*4 for i in range(8)],[4]*8+[3]*6+[5]*6+[4]*8)) for a,b in ([(0,2)] if i in [13,27] else [(0,2),(2,length-1 if i in [7,19] else length)])],
 performance=dict(rubato=[54,55,55,56,55,54,55,50,54,55,54,53,52,49,53,54,55,54,53,49,56,57,58,59,56,55,54,54],phrase_arcs=[[0,12,3],[12,31,4],[32,44,3],[50,79,4],[80,96,5],[96,110,2]],lower_entries=[],pedal_lift=.16,gate=.97,note='Let the seven-note wheel turn beneath the song. The final major chord is a brief arrival followed by written silence, with no extra slowing.')),
dict(op=236,title='Velvet Clerestory',key='Eb',fifths=-3,meter='4/4',bpm=46,
 description='Slow chords reveal a descending song and small inner movements. Warm suspensions give way to a distant D-major light before the original line returns over new bass notes. The final chord belongs to A-flat, leaving the opening room gently altered.',
 difficulty='Advanced quiet chord voicing and independent inner suspensions',technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=7),technical_note='The RH upper line must remain audible above the separately written inner dyads. Keep held upper notes down while the lower chord tones change; the LH supplies a soft harmonic floor. The most active voice is often inside the chord rather than at its top.',
 parent_opus=230,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=8,pitches=['Eb','D','C','Bb']),ancestry=dict(source_opus=230,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),
 system_starts=list(range(1,25,2)),page_starts=[9,17],engraving=dict(spacing_system=18,spacing_staff=25,pedal_offset_y=610),
 rh='''Eb5:2 D5:2
C5:2 Bb4:2
Eb5:4
F5:4
G5:3 F5:1
Eb5:2 D5:2
C5:3 R:1
D5:4
E5:4
F#5:3 E5:1
D5:2 C#5:2
B4:2 A4:1 R:1
Eb5:2 D5:2
C5:2 Bb4:2
G5:4
Ab5:3 G5:1
F5:2 Eb5:2
D5:2 C5:2
Bb4:3 R:1
Eb5:2 D5:2
C5:2 Bb4:2
Ab4:2 G4:2
F4:2 G4:1 R:1
Bb4:4''',rh_inner='''G4+Bb4:2 F4+Ab4:2
Eb4+G4:2 D4+F4:2
G4+Bb4:2 F4+A4:1 G4+Bb4:1
Ab4+C5:2 A4+C5:1 Ab4+C5:1
Bb4+D5:2 B4+D5:1 A4+C5:1
G4+Bb4:2 F4+Ab4:2
Eb4+G4:2 E4+G4:1 R:1
F#4+A4:2 E4+G4:1 F#4+A4:1
G4+B4:2 G#4+B4:1 G4+B4:1
A4+C#5:2 A4+C5:1 G4+B4:1
F#4+A4:2 E4+G#4:2
D4+F#4:2 C#4+E4:1 R:1
G4+Bb4:2 F4+Ab4:2
Eb4+G4:2 D4+F4:2
Bb4+D5:2 A4+C5:1 Bb4+D5:1
C5+Eb5:2 B4+D5:1 Bb4+D5:1
Ab4+C5:2 G4+Bb4:2
F4+Ab4:2 Eb4+G4:2
D4+F4:2 Eb4+G4:1 R:1
G4+Bb4:2 F4+Ab4:2
Eb4+G4:2 D4+F4:2
C4+Eb4:2 Bb3+D4:2
Ab3+C4:2 Bb3+D4:1 R:1
Eb4+G4:4''',lh='''Eb3+Bb3:2 Bb2+F3:2
Ab2+Eb3:2 G2+D3:2
C3+G3:4
F3+C4:4
Eb3+Bb3:3 Bb2+F3:1
Ab2+Eb3:2 Bb2+F3:2
C3+G3:3 R:1
D3+A3:4
C3+G3:4
D3+A3:3 C3+G3:1
B2+F#3:2 A2+E3:2
G2+D3:2 A2+E3:1 R:1
Ab2+Eb3:2 Bb2+F3:2
F3+C4:2 G2+D3:2
Eb3+Bb3:4
F3+C4:3 G3+D4:1
Ab3+Eb4:2 G3+D4:2
F3+C4:2 Eb3+Bb3:2
Bb2+F3:3 R:1
C3+G3:2 Bb2+F3:2
Ab2+Eb3:2 G2+D3:2
F2+C3:2 Eb2+Bb2:2
Db2+Ab2:2 Eb2+Bb2:1 R:1
Ab2+Eb3:4''',
 sections={1:'p',3:'pp',8:'p',13:'p',15:'mp',20:'pp'},lower_sections={1:'pp',15:'p',20:'pp'},words={},slurs=[(1,2),(5,7),(10,12),(13,14),(16,19),(20,23)],hairpins=[],tempo_changes={},group=3,
 voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=2) for a,b in [(8,27),(28,47),(56,75)]],
 pedal_spans=[[i*4+a,i*4+b-.2] for i in range(24) for a,b in ([(0,4)] if i==23 else [(0,2),(2,3),(3,4)] if i in [2,3,4,7,8,9,14,15] else [(0,2),(2,3 if i in [6,11,18,22] else 4)])],
 performance=dict(rubato=[46,45,46,47,48,46,42,46,47,48,46,42,46,47,49,50,48,46,42,45,44,43,40,38],phrase_arcs=[[0,8,2],[8,27,3],[28,47,3],[48,75,4],[76,91,2]],lower_entries=[],inner_entries=[[8,27],[28,47],[56,75]],pedal_lift=.2,gate=1.0,note='Allow the small inner movements to colour held chords without drawing hard accents. The A-flat ending is a quiet change of perspective.')),
dict(op=237,title='Camellia Pane',key='f#',fifths=3,meter='6/4',bpm=52,final_fermata=False,
 description='Every attack is a chord. A wide opening is folded into close voicings, where one changing note can turn the light from major to minor. The music reaches a brief radiant crest, then returns to a smaller, warmer F-sharp-minor sonority without slowing to a final tableau.',
 difficulty='Advanced all-chord cantabile with chromatic inner voice leading',technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=7),technical_note='Keep the highest note of each RH chord connected across changing inversions. Several repeated top notes conceal semitone changes within the chord. Use the written releases to relocate each hand; no chord is silently rolled or redistributed.',
 parent_opus=229,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['F#','A','G#','C#']),ancestry=dict(source_opus=229,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['F#','A','G#','C#'],transposition_semitones=0),
 system_starts=list(range(1,21,2)),page_starts=[7,13,17],engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=560),
 rh='''A4+C#5+F#5:2 C#5+E5+A5:1.5 B4+D#5+G#5:1.5 E5+G#5+C#6:1
D5+F#5+B5:2 C#5+E5+A5:2 B4+D5+G#5:2
A4+C#5+F#5:3 G#4+B4+E5:2 R:1
F#4+A4+C#5:2 F#4+A4+C5:1 F#4+A4+B4:3
E4+G#4+B4:2 E4+G4+B4:1 E4+G#4+B4:3
F#4+A4+D5:2 F#4+G#4+D5:1 F#4+A4+D5:3
E4+G#4+C#5:2 E4+G4+C5:2 D4+F#4+B4:1 R:1
F4+Ab4+C5:3 F4+A4+C5:3
Gb4+Bb4+Db5:2 G4+Bb4+Db5:1 Ab4+C5+Eb5:3
G4+B4+D5:2 F4+A4+C5:2 E4+G#4+B4:1 R:1
A4+C#5+F#5:2 B4+D5+G#5:1 C#5+E5+A5:3
D5+F#5+B5:2 E5+G#5+C#6:1 F#5+A5+D6:3
E5+G#5+C#6:2 D5+F#5+B5:2 C#5+E5+A5:2
B4+D5+G#5:3 A4+C#5+F#5:2 R:1
F#4+A4+C#5:2 F#4+A4+D5:1 G#4+B4+E5:3
A4+C#5+F#5:2 A4+C#5+E#5:1 A4+C#5+F#5:3
G#4+B4+E5:2 G4+Bb4+Eb5:2 F#4+A4+D5:2
E4+G#4+C#5:3 D4+F#4+B4:2 R:1
C#4+F#4+A4:2 C#4+E#4+G#4:1 C#4+F#4+A4:3
F#4+A4+C#5+D#5:6''',
 lh='''F#3+C#4:2 D3+A3:1.5 E3+B3:1.5 A3+E4:1
B3+F#4:2 A3+E4:2 E3+B3:2
D3+A3:3 E3+B3:2 R:1
F#2+C#3:2 F#2+C3:1 B2+F#3:3
E3+B3:2 E3+Bb3:1 E3+B3:3
D3+A3:2 D3+Ab3:1 D3+A3:3
A2+E3:2 C3+G3:2 B2+F#3:1 R:1
Db3+Ab3:3 F3+C4:3
Gb3+Db4:2 Eb3+Bb3:1 Ab3+Eb4:3
G3+D4:2 F3+C4:2 E3+B3:1 R:1
F#3+C#4:2 E3+B3:1 A3+E4:3
B3+F#4:2 A3+E4:1 D4+A4:3
A3+E4:2 G3+D4:2 F#3+C#4:2
E3+B3:3 D3+A3:2 R:1
D3+A3:2 B2+F#3:1 E3+B3:3
F#3+C#4:2 C#3+G#3:1 F#3+C#4:3
E3+B3:2 Eb3+Bb3:2 D3+A3:2
A2+E3:3 B2+F#3:2 R:1
F#2+C#3:2 C#3+G#3:1 F#2+C#3:3
F#2+C#3:6''',
 sections={1:'p',4:'pp',8:'p',11:'mp',12:'mf',15:'p',19:'pp'},lower_sections={1:'pp',11:'p',15:'pp'},words={},slurs=[(1,3),(4,7),(8,10),(11,14),(15,18),(19,20)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*6+a,i*6+b-.2] for i in range(20) for a,b in ([(0,6)] if i==19 else [(0,2),(2,3.5),(3.5,5),(5,6)] if i==0 else [(0,2),(2,3),(3,6)] if i in [3,4,5,8,10,11,14,15,18] else [(0,3),(3,5)] if i in [2,13,17] else [(0,2),(2,4),(4,5)] if i in [6,9] else [(0,3),(3,6)] if i==7 else [(0,2),(2,4),(4,6)])],
 performance=dict(rubato=[52,53,48,49,50,51,47,49,50,46,54,56,55,48,51,52,51,47,50,50],phrase_arcs=[[0,17,3],[18,41,2],[42,59,3],[60,83,5],[84,107,3],[108,120,1]],lower_entries=[],pedal_lift=.2,gate=.99,note='Sing through the chord tops, giving the chromatic inner changes a soft touch. The brief crest subsides into an evenly paced minor-sixth ending.')),
dict(op=238,title='Reed Glazing',key='d',fifths=-1,meter='5/4',bpm=57,
 description='A melody begins inside the left hand, under a still two-note canopy. Four voices gradually move at different moments, opening the chords from within. An E-flat reflection and a brief D-major clearing change the song before it returns, softer and closer to the ground.',
 difficulty='Advanced four-voice chorale with an independent LH tenor melody',technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=7),technical_note='The opening tune lies in the LH tenor over held bass notes, sometimes spanning an octave within that hand. Sustain each voice for its full written value while the other fingers move. The upper two lines remain lighter than the tenor at its melodic entries.',
 parent_opus=227,motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=5,pitches=['D','C','A','G']),ancestry=dict(source_opus=227,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','C','A','G'],transposition_semitones=-12),
 system_starts=list(range(1,27,2)),page_starts=[7,13,19,23],engraving=dict(spacing_system=18,spacing_staff=26,pedal_offset_y=630),
 rh='''F5:5
E5:5
D5:3 C5:2
E5:5
F5:3 E5:2
D5:5
C5:3 Bb4:2
A4:3 C5:2
D5:4 R:1
Eb5:5
F5:3 Eb5:2
G5:5
F5:3 Eb5:2
D5:4 R:1
F#5:5
E5:3 D5:2
G5:3 F#5:2
A5:5
G5:3 F#5:2
E5:3 D5:2
C#5:4 R:1
F5:3 E5:2
D5:3 C5:2
Bb4:3 A4:2
G4:3 A4:1 R:1
D5:5''',rh_inner='''A4:3 C5:2
G4:3 B4:2
F4:3 E4:2
G4:2 Bb4:1 A4:2
A4:2 C5:1 G4:2
F4:2 A4:1 Bb4:2
E4:2 G4:1 D4:2
D4:2 F4:1 E4:2
F4:2 A4:2 R:1
G4:3 Bb4:2
Ab4:2 C5:1 G4:2
Bb4:2 D5:1 C5:2
Ab4:2 C5:1 G4:2
F4:2 Ab4:2 R:1
A4:3 C#5:2
G4:2 B4:1 F#4:2
B4:2 D5:1 A4:2
C#5:2 E5:1 D5:2
B4:2 D5:1 A4:2
G4:2 B4:1 F#4:2
E4:2 G4:2 R:1
A4:3 G4:2
F4:3 E4:2
D4:3 C4:2
Bb3:3 C4:1 R:1
F4+A4+C5:5''',lh='''D3:5
C3:5
Bb2:5
C3:5
D3:5
Bb2:5
A2:5
Bb2:3 C3:2
D3:4 R:1
Eb3:5
Db3:5
Eb3:5
C3:3 Bb2:2
C3:4 R:1
D3:5
C3:3 B2:2
E3:3 D3:2
F#3:5
E3:3 D3:2
C3:3 B2:2
A2:4 R:1
D3:3 C3:2
Bb2:3 A2:2
G2:3 F2:2
Eb2:3 F2:1 R:1
D3:5''',lh_upper='''D4:1.5 C4:1.5 A3:1 G3:1
C4:2 B3:1 A3:1 G3:1
Bb3:2 A3:1 F3:2
G3:2 E3:1 G3:2
A3:2 F3:1 A3:2
Bb3:2 A3:1 G3:2
G3:2 E3:1 F3:2
F3:2 D3:1 G3:2
A3:2 F3:2 R:1
Eb4:1.5 D4:1.5 Bb3:1 Ab3:1
Db4:2 C4:1 Ab3:2
Bb3:2 G3:1 Bb3:2
C4:2 Ab3:1 F3:2
G3:2 E3:2 R:1
D4:1.5 C#4:1.5 A3:1 G3:1
C4:2 G3:1 F#3:2
B3:2 G3:1 A3:2
C#4:2 A3:1 B3:2
B3:2 G3:1 A3:2
G3:2 E3:1 F#3:2
E3:2 G3:2 R:1
A3:1.5 G3:1.5 E3:2
F3:1.5 E3:1.5 C3:2
D3:1.5 C3:1.5 A2:2
Bb2:2 G2:1 A2:1 R:1
A3:5''',
 sections={1:'pp',10:'p',15:'p',18:'mp',22:'pp'},lower_sections={1:'p',10:'p',15:'mp',22:'p',26:'pp'},words={},slurs=[(3,9),(10,14),(15,21),(22,25)],hairpins=[],tempo_changes={},group=3,
 voice_phrases=[dict(voice='tenor',start_beat=a,end_beat=b,swell=4) for a,b in [(0,15),(15,44),(45,69),(70,104),(105,124)]],
 pedal_spans=[[i*5+a,i*5+b-.18] for i in range(26) for a,b in ([(0,5)] if i==25 else [(0,1.5),(1.5,3),(3,4),(4,5)] if i in [0,9,14] else [(0,2),(2,3),(3,4)] if i in [8,13,20,24] else [(0,2),(2,3),(3,5)])],
 performance=dict(rubato=[57,58,56,57,58,58,56,55,50,57,58,59,56,50,58,59,60,62,60,57,50,54,53,52,47,38],phrase_arcs=[[0,15,2],[15,44,2],[45,69,2],[70,104,3],[105,124,1]],lower_entries=[],tenor_entries=[[0,44],[45,69],[70,104],[105,124]],pedal_lift=.18,gate=1.0,note='Let the tenor carry the song inside the left hand. The upper canopy changes without drawing attention away from it; the final minor seventh is a quiet homecoming.')),
dict(op=239,title='Moss Atrium',key='g',fifths=-2,meter='7/4',bpm=51,final_fermata=False,
 description='Chords enter just before and after one another, making a slow seven-beat space feel gently unsettled. An opening ascent becomes a series of common-tone reflections; a brighter middle passage is followed by a shorter, darker recollection. The final minor colour releases into a long written silence.',
 difficulty='Advanced staggered chord attacks and sustained harmonic pacing',technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=7),technical_note='The hands often change harmony at different moments. Hear the temporary suspensions between their chord attacks, and keep the delayed RH entries unforced. All attacks are chords, with no hidden arpeggiation; observe the final four beats of silence.',
 parent_opus=232,motif=dict(hand='rh',start_beat=0,end_beat=7,pitches=['G','Bb','A','D']),ancestry=dict(source_opus=232,source_hand='rh',source_start_beat=0,source_end_beat=3.5,source_pitches=['E','G','F#','B'],transposition_semitones=3),
 system_starts=list(range(1,18,2)),page_starts=[7,13],engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=570),
 rh='''Bb4+D5+G5:2 D5+F5+Bb5:1 C5+E5+A5:2 F5+A5+D6:2
Eb5+G5+C6:3 D5+F5+Bb5:2 C5+Eb5+A5:2
Bb4+D5+G5:2 A4+C5+F5:3 G4+Bb4+Eb5:2
F#4+A4+D5:3 G4+Bb4+Eb5:3 R:1
R:.5 G4+Bb4+D5:1.5 G4+B4+D5:2 G4+C5+D5:3
R:.5 F4+A4+C5:1.5 F4+Ab4+C5:2 E4+G4+C5:3
R:.5 Eb4+G4+Bb4:1.5 E4+G4+Bb4:2 F4+A4+C5:3
R:.5 F#4+A4+D5:1.5 G4+Bb4+D5:2 A4+C5+D5:2 R:1
G4+B4+E5:3 A4+C#5+F#5:2 B4+D5+G5:2
C5+E5+A5:2 D5+F#5+B5:3 E5+G5+C6:2
D5+F#5+B5:2 C5+E5+A5:2 B4+D5+G5:3
A4+C5+F#5:3 G4+B4+E5:3 R:1
Bb4+D5+G5:2 D5+F5+Bb5:1 C5+Eb5+A5:2 F4+A4+D5:2
R:.5 Eb4+G4+C5:1.5 F4+A4+D5:2 G4+Bb4+Eb5:3
R:.5 F4+Ab4+Db5:1.5 Eb4+G4+C5:2 D4+F4+Bb4:3
C4+Eb4+A4:3 D4+F#4+A4:3 R:1
Eb4+G4+A4+D5:3 R:4''',
 lh='''G3+D4:3 Eb3+Bb3:4
C4+G4:3 Bb3+F4:2 A3+E4:2
G3+D4:2 F3+C4:3 Eb3+Bb3:2
D3+A3:3 C3+G3:3 R:1
G2+D3:3 C3+G3:4
F2+C3:3 A2+E3:4
Eb3+Bb3:3 D3+A3:4
D3+A3:3 C3+G3:3 R:1
E3+B3:2 D3+A3:3 G3+D4:2
A3+E4:3 B3+F#4:2 C4+G4:2
B3+F#4:3 A3+E4:2 G3+D4:2
D3+A3:3 E3+B3:3 R:1
Eb3+Bb3:3 C3+G3:2 Bb2+F3:2
C3+G3:3 Bb2+F3:4
Db3+Ab3:3 C3+G3:4
A2+E3:3 D3+A3:3 R:1
C3+G3:3 R:4''',
 sections={1:'p',5:'pp',9:'mp',10:'mf',13:'p',17:'pp'},lower_sections={1:'pp',9:'p',13:'pp'},words={},slurs=[(1,4),(5,7),(9,12),(13,16)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*7+a,i*7+b-.2] for i in range(17) for a,b in ([(0,3)] if i==16 else [(0,2),(2,3),(3,5),(5,7)] if i in [0,1,8,9,10,12] else [(0,2),(2,5),(5,7)] if i==2 else [(0,3),(3,6)] if i in [3,11,15] else [(0,2),(2,3),(3,4),(4,6)] if i==7 else [(0,2),(2,3),(3,4),(4,7)])],
 performance=dict(rubato=[51,52,50,46,49,50,50,46,52,54,53,47,50,51,50,47,49],phrase_arcs=[[0,27,4],[28,55,2],[56,83,5],[84,111,3]],lower_entries=[],pedal_lift=.2,gate=1.0,note='The delayed chord changes are soft arrivals, not accents. Let the bright middle passage open naturally, then keep the final silence fully measured.')),
dict(op=240,title='Fennel Lantern',key='F',fifths=-1,meter='12/8',bpm=50,final_fermata=False,
 description='Four soft chord changes float over three slower bass changes. Their shared tones pass through bright and shadowed rooms before the rhythm finally aligns. At the end the chords fall away, leaving one plain F in the middle of the piano.',
 difficulty='Advanced four-against-three chordal pulse and voicing',technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=7),technical_note='In the opening five bars, four dotted-quarter RH chords sound against three half-note LH dyads in each bar. Keep both streams even and quiet. The later shared rhythm should feel like a release of tension; the final single note is unaccompanied.',
 parent_opus=236,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['F','E','D','C']),ancestry=dict(source_opus=236,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=8,source_pitches=['Eb','D','C','Bb'],transposition_semitones=2),
 system_starts=list(range(1,19,2)),page_starts=[7,13],engraving=dict(spacing_system=18,spacing_staff=18,pedal_offset_y=590),
 rh='''A4+C5+F5:1.5 G4+Bb4+E5:1.5 F4+A4+D5:1.5 E4+G4+C5:1.5
F4+A4+D5:1.5 G4+Bb4+E5:1.5 A4+C5+F5:1.5 Bb4+D5+G5:1.5
A4+C5+F5:1.5 G4+Bb4+Eb5:1.5 F4+Ab4+Db5:1.5 Eb4+G4+C5:1.5
F4+Ab4+Db5:1.5 G4+Bb4+Eb5:1.5 Ab4+C5+F5:1.5 G4+Bb4+Eb5:1.5
F4+A4+D5:1.5 E4+G4+C5:1.5 D4+F4+Bb4:1.5 E4+G4+C5:1.5
F4+A4+C5:3 G4+Bb4+D5:2 R:1
A4+C5+F5:2 A4+B4+E5:1 G4+Bb4+D5:3
G4+B4+E5:2 G4+Bb4+Eb5:1 F4+A4+D5:3
F4+A4+D5:2 F4+Ab4+Db5:1 Eb4+G4+C5:3
E4+G4+C5:2 D4+F4+Bb4:2 C4+E4+A4:1 R:1
A4+C5+F5:1.5 G4+Bb4+E5:1.5 F4+A4+D5:1.5 E4+G4+C5:1.5
Bb4+D5+G5:1.5 A4+C5+F5:1.5 G4+Bb4+E5:1.5 F4+A4+D5:1.5
C5+E5+A5:1.5 Bb4+D5+G5:1.5 A4+C5+F5:1.5 G4+Bb4+E5:1.5
F4+A4+D5:2 E4+G4+C5:2 D4+F4+Bb4:2
C4+E4+A4:3 D4+F4+Bb4:3
E4+G4+C5:3 F4+A4+C5:2 R:1
C5:1 D5:2 R:3
F4:6''',
 lh='''F3+C4:2 C3+G3:2 Bb2+F3:2
Bb2+F3:2 C3+G3:2 F3+C4:2
F3+C4:2 Eb3+Bb3:2 Db3+Ab3:2
Db3+Ab3:2 Eb3+Bb3:2 Ab3+Eb4:2
Bb2+F3:2 C3+G3:2 G2+D3:2
F3+C4:3 C3+G3:2 R:1
D3+A3:2 E3+B3:1 F3+C4:3
E3+B3:2 Eb3+Bb3:1 D3+A3:3
D3+A3:2 Db3+Ab3:1 C3+G3:3
C3+G3:2 Bb2+F3:2 A2+E3:1 R:1
D3+A3:2 C3+G3:2 Bb2+F3:2
Eb3+Bb3:2 D3+A3:2 C3+G3:2
F3+C4:2 Eb3+Bb3:2 D3+A3:2
Bb2+F3:2 C3+G3:2 G2+D3:2
A2+E3:3 Bb2+F3:3
C3+G3:3 F3+C4:2 R:1
R:6
R:6''',
 sections={1:'p',6:'pp',7:'p',11:'mp',14:'p',17:'pp'},lower_sections={1:'pp',11:'p',14:'pp'},words={},slurs=[(1,2),(3,6),(7,10),(11,13),(14,16),(17,17)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*6+a,i*6+b-.18] for i in range(16) for a,b in ([(0,1.5),(1.5,2),(2,3),(3,4),(4,4.5),(4.5,6)] if i in list(range(5))+[10,11,12] else [(0,3),(3,5)] if i in [5,15] else [(0,2),(2,4),(4,5)] if i==9 else [(0,2),(2,3),(3,6)] if i in [6,7,8] else [(0,2),(2,4),(4,6)] if i==13 else [(0,3),(3,6)])],
 performance=dict(rubato=[50,51,50,49,50,46,49,50,49,45,52,53,54,50,48,46,47,47],phrase_arcs=[[0,12,3],[12,35,3],[36,59,3],[60,78,5],[78,95,2]],lower_entries=[],pedal_lift=.18,gate=1.0,note='Let the two chordal streams float across one another. Their later alignment feels calm; the solitary final F receives its full written length without an added fermata.'))
]
