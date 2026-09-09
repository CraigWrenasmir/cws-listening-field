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
 performance=dict(rubato=[51,53,52,51,54,46,50,51,49,50,52,48,48,55,56,57,58,47,51,50,49,45,40,29],phrase_arcs=[],lower_entries=[],pedal_lift=.22,gate=.99,note='Allow the opening song to breathe inside its chords. The higher augmentation is distant and soft; the falling line reconnects it with the flowing middle. The return is warmer, and the last chord remains gentle.'))
]
