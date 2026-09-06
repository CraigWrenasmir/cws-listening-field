"""Individually composed studies for Volume 02, Op. 25–48."""
PIECES=[
dict(op=25,title='Iris Viaduct',key='e',fifths=1,meter='7/4',bpm=56,
 description='A long upper B opens above a low E, leaving room for the bass to remember Tern Palimpsest as E-G-B-D. Triplets appear inside the seven-beat spans rather than setting a continuous pattern. D and F major widen the landscape; B-flat-major colour shifts by a semitone into B dominant, whose inner notes lead back to E minor. A quiet C-Lydian reflection precedes the final added ninth.',
 difficulty='Advanced lyrical counterpoint',
 technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=9),
 technical_note='Unequal seven-beat phrases combine sustained upper notes, three-note voicings and triplet figures that migrate between the hands. The B-flat-to-B dominant shift depends on chromatic inner-voice control. Slow LH register changes are prepared by held notes or rests; chords remain within an octave and are sounded together.',
 tuplet_hands=['rh','lh'],
 parent_opus=23,motif=dict(hand='lh',start_beat=7,end_beat=11,pitches=['E','G','B','D']),
 ancestry=dict(source_opus=23,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['G','Bb','D','F'],transposition_semitones=-3),
 rh='''
B4:3 F#5:1 G5:1 F#5:1 E5:1~
E5:1 D5:.5 B4:.5 A4:1 G4:.5 F#4:.5 E4:2 R:1
F#4+A4+E5:2 B4:1 D5:1 F#5:1 E5:1 C#5:1
C#5:1 C5:.5 A4:.5 G4:1 E4+G4+D5:2 B4:1 A4:1
G4:2/3 Bb4:2/3 D5:2/3 F5:2 Eb5:.5 D5:.5 C5:1 A4:1
F#4+A4+D#5:2 E5:1 F#5:.5 A5:.5 G5:1 F#5:1 D#5:1~
D#5:1 E5:1 G5:.5 B5:.5 A5:1 G5:1 F#5:1 E5:1
D5:2 F#5:1 A5:1 G5:.5 F#5:.5 E5:1 C#5:1
B4:1 D5:.5 F#5:.5 A5:2 G5:1 E5:1 D5:1
C5:2 E5:1 G5:.5 B5:.5 A5:1 G5:1 F#5:1
E5:1 D#5:.5 C5:.5 B4:1 A4:.5 F#4:.5 E4:1 D#4:1 F#4:1~
F#4:1 G4:1 B4:1 D5:1 C#5:.5 B4:.5 F#4+B4+E5:2
''',
 lh='''
E2:1 B2:1 F#3:1 G3:1 D3:1 E3:2
E3:2/3 G3:2/3 B3:2/3 D4:2 G3:1 F#3:1 E3:1
D3:1 A3:1 C#4:1 F#3:.5 E3:.5 A3:1 C#4:1 D3:1
F3:1 C4:1 A3:1 E3:1 D4:.5 C4:.5 A3:1 G3:1
Bb2:1 F3:1 A3:1 D4:1 C4:.5 Bb3:.5 A3:1 F3:1
B2:1 F#3:1 A3:1 D#4:1 C4:1 A3:1 F#3:1
E3:2/3 G3:2/3 B3:2/3 D4:1 F#3:1 G3:1 B3:1 E3:1
D3:1 A3:1 F#3:1 C#4:1 E3:1 C4:1 A3:1
G3:1 D4:.5 B3:.5 F#3:1 A3:1 B3:1 D3:1 R:1
C3:1 E3:1 B3:1 D4:1 F#3:1 G3:1 E3:1
B2:1 F#3:1 A3:1 C4:1 D#4:.5 C4:.5 F#3:1 R:1
E2:1 B2:1 E3:1 G3:1 D4:.5 C#4:.5 E3+G3:2
''',sections={1:'p',3:'pp',5:'mp',7:'p',10:'pp'},words={1:'poco rubato',11:'poco rit.'},
 slurs=[(1,2),(3,4),(5,7),(8,10),(11,12)],lower_phrases=[(1,2),(3,5),(6,8),(9,10),(11,12)],
 hairpins=[('diminuendo',1,2),('crescendo',3,4),('diminuendo',5,7),('crescendo',8,9),('diminuendo',9,10),('diminuendo',11,12)],tempo_changes={},group=2,
 performance=dict(rubato=[56,52,55,51,58,55,50,55,53,48,45,38],
  phrase_arcs=[[0,13,3],[14,27,4],[28,48,5],[49,69,4],[70,84,-2]],
  lower_entries=[[0,14],[14,35],[35,56],[56,70],[70,82]],pedal_bars=list(range(1,13)),pedal_lift=.26,gate=.99,
  note='The long opening note lets the lower melody establish its own pace. The chromatic B-flat-to-B connection stays linked by its common A; the return to E minor releases that tension before a quiet last phrase.'))
,
dict(op=26,title='Haze Contour',key='f#',fifths=3,meter='6/4',bpm=56,
 description='Long F-sharp-minor, D-major, C-major and B-minor colours each linger across two bars. Iris Viaduct\'s bass memory rises to F-sharp-A-C-sharp-E in the treble. A sustained upper chord and occasional triplets interrupt the sense of a regular accompaniment; written pedal spans preserve each harmonic field until the altered C-sharp dominant finds its way home.',
 difficulty='Advanced resonance and voicing',
 technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),
 technical_note='Long chord ties, wide upper voicings and spacious bass travel require soft voicing and controlled pedal. The written pedal spans continue across bar lines only while a harmonic field remains stable. A brief triplet figure loosens the upper phrase; chord spans remain within an octave.',
 tuplet_hands=['rh'],
 pedal_spans=[[0,11.75],[12,23.75],[24,35.75],[36,47.75],[48,53.75],[54,59.75],[60,71.75]],
 parent_opus=25,motif=dict(hand='rh',start_beat=12,end_beat=15,pitches=['F#','A','C#','E']),
 ancestry=dict(source_opus=25,source_hand='lh',source_start_beat=7,source_end_beat=11,source_pitches=['E','G','B','D'],transposition_semitones=2),
 rh='''
C#5:4 A4+C#5+G#5:2~
A4+C#5+G#5:2 G#5:1 F#5:.5 E5:.5 C#5:1 B4:1
F#4:2/3 A4:2/3 C#5:2/3 E5:3 D5:1~
D5:1 C#5:.5 A4:.5 G#4:1 E4+G#4+C#5:2 R:1
E4+G4+D5:3 C5:1 B4:1 A4:1
G4:1 B4:.5 D5:.5 F#5:2 E5:1 D5:1~
D5:1 C#5:.5 A4:.5 G#4:1 F#4:.5 E4:.5 D4:1 C#4:1
D4+F#4+C#5:3 B4:1 A4:.5 F#4:.5 E4:1
E4:2/3 G#4:2/3 B4:2/3 D5:2 C#5:1 G#4:1~
G#4:1 F#4:.5 E4:.5 C#4:1 E4+F#4+A4:3
A4:1 C#5:.5 E5:.5 G#5:2 F#5:1 E5:1~
E5:1 C#5:1 B4:1 A4+C#5+G#5:3
''',
 lh='''
F#2:1 C#3:1 E3:1 G#3:1 A3:1 C#4:1
F#3:1.5 C#4:.5 A3:2 G#3:1 F#3:1
D3:2 A3:1 C#4:1 E4:1 F#3:1
D3:1 A3:1.5 C#4:.5 E3:1 F#3:2
C3:1 E3:1 G3:2 B3:1 D4:1
C3:1.5 G3:.5 B3:1 D4:1 E3:2
B2:1 D3:1 F#3:1.5 A3:.5 F#3:1 D3:1
B2:2 F#3:1 A3:1 C#4:.5 F#3:.5 R:1
C#3:1 E#3:1 G#3:1 B3:1 D4:1 E#3:1
F#2:1 C#3:1 E3:2 A3:1 F#3:1
F#2:1.5 C#3:.5 E3:1 G#3:1 A3:1 C#3:1
F#2:1 C#3:1 E3:1 F#3+A3:3
''',sections={1:'pp',3:'p',5:'mp',7:'p',10:'pp'},words={1:'poco rubato',11:'poco rit.'},
 slurs=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)],lower_phrases=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)],
 hairpins=[('crescendo',3,4),('diminuendo',5,6),('diminuendo',7,8),('diminuendo',9,10),('diminuendo',11,12)],tempo_changes={},group=3,
 performance=dict(rubato=[56,52,55,51,56,52,53,48,53,47,45,38],
  phrase_arcs=[[0,11,2],[12,23,3],[24,35,4],[36,47,3],[48,59,3],[60,72,-2]],
  lower_entries=[[0,12],[12,24],[24,36],[36,48],[48,60]],pedal_bars=[],gate=.99,
  note='The score and MIDI use the same explicit pedal spans. Harmonic changes, rather than every bar line, determine the release; each long field is softly voiced to keep its upper extensions clear.'))
,
dict(op=27,title='Moss Interchange',key='Db',fifths=-5,meter='4/4',bpm=61,
 description='Rain Arcade\'s rising C-E-G-A returns as D-flat-F-A-flat-B-flat, with its last note held over a bass reply. Unequal phrases move through F minor and B-flat minor before an E-minor-to-A-major window. A D dominant chord approaches the home key from a semitone above. The later return is quieter, ending with the plain tonic after an added-ninth recollection.',
 difficulty='Advanced jazz ballad',system_starts=[1,4,8,11,15,19],
 technique_limits=dict(chord_span=12,melodic_leap=14,rapid_leap=9),
 technical_note='Held upper notes, triplets in both hands, displaced bass replies and chromatic three-note voicings require independent phrasing. The D-dominant approach to D-flat needs careful inner-voice balance. Bass chords are held as written; the slow line allows planned register changes.',
 tuplet_hands=['rh','lh'],
 parent_opus=21,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['Db','F','Ab','Bb']),
 ancestry=dict(source_opus=21,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['C','E','G','A'],transposition_semitones=1),
 rh='''
Db5:1 F5:.5 Ab5:.5 Bb5:2~
Bb5:1 Ab5:.5 F5:.5 Eb5:1 C5:1~
C5:.5 Db5:.5 F4+Ab4+Eb5:2 R:1
Ab4:2/3 C5:2/3 Eb5:2/3 G5:1 F5:1
Eb5:1 Db5:.5 C5:.5 Ab4:1 F4:1~
F4:1 Ab4:.5 Bb4:.5 Db5:1 C5:1
Bb4:1 A4:.5 G4:.5 F4+Ab4+C5:2
E4+G4+B4:2 D5:1 C#5:1~
C#5:1 B4:.5 A4:.5 G#4+B4+F#5:2
F5:1 Eb5:.5 Db5:.5 C5:1 Bb4:1
A4+C5+F#5:2 E5:1 Eb5:1
Db5:3 F5:.5 Ab5:.5
Bb5:1 Ab5:.5 Gb5:.5 F5:1 Eb5:1~
Eb5:1 D5:.5 C5:.5 Bb4:1 A4:1
Ab4:2/3 C5:2/3 Eb5:2/3 G5:2
F5:1 Eb5:.5 C5:.5 Bb4:1 Ab4:1
Gb4+Bb4+F5:2 Eb5:1 Db5:1
C5:1 Bb4:.5 Ab4:.5 Gb4+Bb4+Eb5:2
F4+Ab4+Eb5:2 Db5:1 C5:1~
C5:1 Bb4:.5 Ab4:.5 F4:1 Eb4:1
F4+Ab4+Db5:4
''',
 lh='''
Db3:2 Ab3:1 F3:1
Bb2:1 F3:.5 Ab3:.5 Db4:1 F3:1
Db3+F3:2 Ab3:.5 C4:.5 Eb3:1
F3:1 C4:2/3 Eb4:2/3 Ab3:2/3 G3:1
Bb2:1.5 F3:.5 Ab3+Db4:2
Gb3:1 Db4:.5 F3:.5 Bb3:1 Ab3:1
F3:1 Eb3:1 A3:1 C4:1
E3:2 B3:1 D4:.5 F#3:.5
A2:1 E3:1 G#3+B3:2
Ab2:1.5 Eb3:.5 Gb3:1 C4:1
D3:1 A3:.5 C4:.5 F#3:2
Db3:2 Ab3:1 F3:1
Gb3:1 Bb3:2/3 Db4:2/3 F3:2/3 Ab3:1
C3:1 G3:1 Bb3+E4:2
F3:1 C4:.5 Eb4:.5 Ab3:1 G3:1
Bb2:2 F3:1 Ab3:1
Gb3:1.5 Db4:.5 Bb3:1 Ab3:1
Ab2:1 Eb3:.5 Gb3:.5 C4:1 Ab3:1
Db3+Ab3:2 F3:1 C4:1
Gb3:1 Db4:.5 Bb3:.5 Ab3:1 Eb3:1
Db3+Ab3:4
''',sections={1:'p',4:'mp',8:'pp',10:'mp',12:'p',17:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,3),(4,7),(8,9),(10,12),(13,16),(17,18),(19,21)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,16),(17,18),(19,21)],
 hairpins=[('diminuendo',1,3),('crescendo',4,6),('diminuendo',6,7),('crescendo',8,9),('diminuendo',10,12),('crescendo',13,15),('diminuendo',15,16),('diminuendo',19,21)],tempo_changes={},group=4,
 performance=dict(rubato=[61,58,53,63,59,61,55,54,51,60,55,51,60,58,61,54,52,49,47,42,35],
  phrase_arcs=[[0,11,3],[12,27,4],[28,35,2],[36,47,4],[48,63,4],[64,71,1],[72,84,-2]],
  lower_entries=[[0,12],[12,24],[28,36],[40,48],[48,64],[72,84]],pedal_bars=list(range(1,22)),pedal_lift=.24,gate=.99,
  note='Long bass values alternate with replies and triplets, rather than supplying a continuous walking pulse. The distant A-major window is softened before the two chromatic approach chords; the last tonic is allowed to settle.'))
,
dict(op=28,title='Birch Hypotenuse',key='G',fifths=1,meter='3/4',bpm=57,
 description='A high G-B-D-E memory from Moss Interchange opens above a widely spaced bass. Five-note figures first glimmer in E minor, then carry a whole-tone ascent over D dominant before the return to G. Near the end, the bass takes up the quintuplet motion while the treble holds still. The final added ninth keeps a little distance in the otherwise warm close.',
 difficulty='Advanced quintuplet study',system_starts=[1,4,8,12,16,20],
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Five eighth notes occupy two quarter-note beats, crossing the slower notes in the other hand. The upper line reaches E6. Two descending LH elevenths, E-flat4 to B-flat2 and C4 to G2, connect the upper bass reply to a resonant new root; each follows a full quarter note at the slow tempo. These planned register changes require hand travel. Three-note voicings stay within an octave, and the melodic quintuplets use small intervals.',
 tuplet_groups=[dict(hand='rh',actual=5,normal=4,count=10),dict(hand='lh',actual=5,normal=4,count=5)],
 parent_opus=27,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['G','B','D','E']),
 ancestry=dict(source_opus=27,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['Db','F','Ab','Bb'],transposition_semitones=6),
 rh='''
G5:.5 B5:.5 D6:1 E6:1~
E6:1 D6:.5 B5:.5 A5:1
G5:2 F#5:1
E5:2/5 F#5:2/5 G5:2/5 B5:2/5 D6:2/5 C6:1
B5:1 A5:.5 G5:.5 F#5:1~
F#5:1 E5:.5 D5:.5 B4:1
G4+B4+F#5:2 E5:1
E5:1 G5:.5 B5:.5 D6:1
C6:1 B5:.5 G5:.5 F#5:1~
F#5:.5 G5:.5 E5:1 D5:1
Eb5+G5+C6:2 Bb5:1
A5:1 G5:.5 F5:.5 D5:1
C5+E5+B5:2 A5:1
D5:2/5 E5:2/5 F#5:2/5 G#5:2/5 A#5:2/5 C6:1
B5:1 A5:.5 G5:.5 E5:1~
E5:1 D5:.5 B4:.5 A4:1
C5+E5+B5:2 A5:1
G5:2 F#5:1
F5:1 E5:.5 D5:.5 C5:1
B4+D5+A5:2 G5:1~
G5:1 F#5:.5 E5:.5 D5:1
B4+D5+A5:3
''',
 lh='''
G2:1 D3:1 B3:1
E3:1.5 B3:.5 D4:1
G3:1 F#3:.5 E3:.5 D3:1
E3:1 B3:1 G3:1
C3:1 G3:.5 B3:.5 E4:1
A3:1 E3:1 G3:1
B2:1 F#3:.5 A3:.5 D#4:1
C3:1 G3:1 B3:1
E3:1.5 B3:.5 D4:1
C3:1 G3:.5 A3:.5 B3:1
F3:1 C4:1 Eb4:1
Bb2:1 F3:1 A3:1
A2:1 E3:.5 G3:.5 B3:1
D3:1 A3:1 C4:1
G3:1 D4:.5 B3:.5 E3:1
E3+G3:1.5 B3:.5 D4:1
C3:1 G3:1 E4:1
C3:2/5 D3:2/5 E3:2/5 G3:2/5 B3:2/5 A3:1
D3:1 F#3:.5 A3:.5 C4:1
G2:1 D3:1 F#3:1
G3:1 D4:.5 B3:.5 A3:1
G3+B3:3
''',sections={1:'p',4:'mp',8:'p',11:'mp',13:'p',16:'pp'},words={1:'poco rubato',20:'poco rit.'},
 slurs=[(1,3),(4,7),(8,11),(12,15),(16,19),(20,22)],lower_phrases=[(1,3),(4,7),(8,10),(11,12),(13,15),(16,19),(20,22)],
 hairpins=[('diminuendo',1,3),('crescendo',4,5),('diminuendo',5,7),('crescendo',8,10),('diminuendo',11,12),('crescendo',13,14),('diminuendo',14,15),('diminuendo',20,22)],tempo_changes={},group=4,
 performance=dict(rubato=[57,54,50,59,57,53,48,57,54,52,56,49,54,57,49,48,51,49,46,43,39,34],
  phrase_arcs=[[0,8,3],[9,20,4],[21,32,4],[33,44,4],[45,56,2],[57,66,-2]],
  lower_entries=[[0,9],[9,21],[21,30],[33,45],[45,57]],pedal_bars=list(range(1,23)),pedal_lift=.2,gate=.99,
  note='The quintuplets flow as single gestures across two beats. The whole-tone ascent briefly suspends the tonal centre; the following B restores G-major warmth. The bass quintuplet answers beneath a still upper note, then the ending broadens.'))
]
