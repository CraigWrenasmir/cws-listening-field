"""The seventh volume: individually authored piano studies, beginning at Op. 145."""

PIECES = [
dict(op=145,title='Linden Vestibule',key='C',fifths=0,meter='6/4',bpm=62,
 description='A modal hymn whose upper chords repeatedly arrive ahead of the bass. Elder Horizon’s F–G–F becomes C–D–C. The upper hand carries a late chord across each phrase boundary, letting the next lower harmony arrive beneath it before the upper notes move on. The close opens into G major.',
 difficulty='Advanced anticipations and sustained chord changes',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='All events are chords of at least three pitches. The late RH chords in bars 2, 6 and 10 continue into the following bar without another attack; each new LH chord begins underneath those held notes. Keep the anticipations soft enough to feel like part of the next breath.',
 parent_opus=144,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['C','D','C']),ancestry=dict(source_opus=144,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['F','G','F'],transposition_semitones=-5),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=14,pedal_offset_y=440),lower_sections={1:'p',5:'pp',9:'p',11:'pp'},
 pedal_spans=[[i*6+a,i*6+b-.2] for i,cuts in enumerate([[0,2,3,6],[0,3,6],[0,1,3.5,6],[0,3,6],[0,6],[0,3,6],[0,1,3.5,6],[0,3,6],[0,6],[0,3,6],[0,1,3,6],[0,6]]) for a,b in zip(cuts,cuts[1:])],
 rh='''
E4+G4+C5:2 F4+A4+D5:1 E4+G4+C5:3
R:.5 E4+G4+B4:2.5 F4+A4+C5:3~
F4+A4+C5:1 G4+B4+D5:2.5 A4+C5+E5:2.5
G4+B4+D5:3 F4+A4+C5:3
Eb4+G4+Bb4:6
R:.5 D4+F4+A4:2.5 Eb4+G4+Bb4:3~
Eb4+G4+Bb4:1 F4+Ab4+C5:2.5 G4+Bb4+D5:2.5
F4+Ab4+C5:3 E4+G4+B4:3
E4+G4+C5:6
R:.5 F#4+A4+C5:2.5 G4+B4+D5:3~
G4+B4+D5:1 F#4+A4+C5:2 E4+G4+B4:3
F#4+A4+B4+D5:6
''',lh='''
C3+E3+G3:2 Bb2+D3+F3:1 A2+C3+E3:3
E3+G3+B3:3 F3+A3+C4:3
G2+B2+D3:6
C3+E3+G3:3 F3+A3+C4:3
Eb3+G3+Bb3:6
D3+F3+A3:3 Eb3+G3+Bb3:3
Ab2+C3+Eb3:6
F3+Ab3+C4:3 E3+G3+B3:3
C3+E3+G3:6
D3+F#3+C4:3 G2+B2+D3:3
C3+E3+G3:3 D3+F#3+C4:3
G2+B2+D3:6
''',sections={1:'p',5:'pp',7:'mp',9:'p',11:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[(1,4),(5,8),(9,12)],lower_phrases=[],hairpins=[('crescendo',6,7),('diminuendo',9,11)],tempo_changes={},group=2,
 performance=dict(rubato=[62,59,62,54,57,56,61,52,57,53,43,29],phrase_arcs=[[0,24,2],[24,48,3],[48,72,-1]],lower_entries=[],pedal_lift=.2,gate=.995,note='The upper anticipations pass gently over the bar line. Keep their keys held as the pedal clears, so the bass can change the colour beneath them.'))
,
dict(op=146,title='Gorse Esplanade',key='F',fifths=-1,meter='9/8',bpm=84,
 description='A soft jazz waltz in three lilting compound beats. Juniper Glissade’s D–F-sharp–E becomes C–E–D. The lower chords leave little pockets of silence and change their placement in the middle, while the melody alternates long-short inflections with quieter chord replies.',
 difficulty='Advanced compound swing and syncopated chord placement',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The long-short swing is written explicitly as quarter plus eighth within the dotted-quarter pulse. Lower attacks fall at 0, 1.5 and 3 quarter beats in bars 1–4, then shift to .5, 2 and 3 in bars 5–8. Keep the released chords light; the middle should feel displaced without accelerating.',
 parent_opus=142,motif=dict(hand='rh',start_beat=0,end_beat=4.5,pitches=['C','E','D']),ancestry=dict(source_opus=142,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['D','F#','E'],transposition_semitones=-2),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=14,pedal_offset_y=440),lower_sections={1:'pp',5:'p',9:'pp'},
 pedal_spans=[[i*4.5+j,i*4.5+j+1.25] for i in range(12) for j in [0,1.5,3]],
 rh='''
C5:1 E5:.5 D5:3
C5:1 A4:.5 G4:1 Bb4:.5 A4:1.5
F4+A4+C5:1.5 G4+Bb4+D5:1 F4+A4+C5:.5 E4+G4+Bb4:1.5
D4+F4+A4:3 R:1.5
Bb4:1 D5:.5 F5:1 E5:.5 D5:1.5
C#5:1 E5:.5 G5:1 F5:.5 E5:1.5
D5:1 F5:.5 A5:1 G5:.5 F5:1.5
Eb5:1 Db5:.5 C5:1 Bb4:.5 G4:1.5
F4+A4+C5:1 A4+C5+E5:.5 G4+Bb4+D5:3
F4+A4+C5:1.5 E4+G4+Bb4:1.5 D4+F4+A4:1.5
D5:1 C5:.5 A4:1 G4:.5 E4+Bb4:1.5
G4+A4+C5+D5:4.5
''',lh='''
G2+Bb2+F3:1 R:.5 C3+E3+Bb3:.5 R:1 F3+A3+C4:1 R:.5
F3+A3+E4:1 R:.5 Bb2+D3+A3:.5 R:1 C3+E3+Bb3:1 R:.5
A2+C3+G3:1 R:.5 D3+F#3+C4:.5 R:1 G2+Bb2+F3:1 R:.5
D3+F3+A3:1 R:.5 G2+B2+F3:.5 R:1 C3+E3+Bb3:1 R:.5
R:.5 Bb2+D3+A3:1 R:.5 G2+Bb2+F3:.5 R:.5 C3+E3+Bb3:1 R:.5
R:.5 A2+C#3+G3:1 R:.5 E3+G3+B3:.5 R:.5 A2+C#3+G3:1 R:.5
R:.5 D3+F3+C4:1 R:.5 Bb2+D3+A3:.5 R:.5 G2+Bb2+F3:1 R:.5
R:.5 Eb3+G3+Bb3:1 R:.5 Db3+F3+Ab3:.5 R:.5 C3+E3+Bb3:1 R:.5
F3+A3+E4:1.5 G2+Bb2+F3:1.5 C3+E3+Bb3:1.5
A2+C3+G3:1.5 C3+E3+Bb3:1.5 D3+F3+A3:1.5
Bb2+D3+A3:1.5 G2+Bb2+F3:1.5 C3+E3+Bb3:1.5
F3+A3+C4:4.5
''',sections={1:'p',5:'mp',9:'p',11:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[(1,4),(5,8),(9,12)],lower_phrases=[],hairpins=[('crescendo',5,7),('diminuendo',9,11)],tempo_changes={},group=2,
 performance=dict(rubato=[84,83,84,76,85,86,88,77,82,77,63,43],phrase_arcs=[[0,18,2],[18,36,3],[36,54,-1]],lower_entries=[],pedal_lift=.2,gate=.91,note='A relaxed three-beat sway. The swing is already in the written durations; give the shorter notes a lighter touch and keep the lower offbeats quiet.'))
,
dict(op=147,title='Myrrh Archipelago',key='C',fifths=0,meter='7/4',bpm=60,
 description='Two ordinary triads combine into less ordinary islands of harmony. Marigold Station’s A–C-sharp–B becomes D–F-sharp–E. A D-major upper chord over C major opens a luminous raised-fourth colour; later E over D, G over F and E-flat over D-flat make related but distinct spaces. Written pauses separate the most distant changes before a simple C-major ending.',
 difficulty='Advanced paired-triad colour and unequal phrase lengths',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='All hand events are triads. Hear each six-note combination as two soft layers. The RH major triads a whole tone above the LH major triads supply ninth, raised fourth and sixth colours. Keep those upper extensions quieter than the tonal bass; release both hands in the written rests.',
 parent_opus=138,motif=dict(hand='rh',start_beat=0,end_beat=7,pitches=['D','F#','E']),ancestry=dict(source_opus=138,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['A','C#','B'],transposition_semitones=5),
 system_starts=[1,3,5,7,9],page_starts=[7],engraving=dict(spacing_system=14,pedal_offset_y=440),lower_sections={1:'p',5:'pp',9:'pp'},
 pedal_spans=[[0,2.8],[3,4.8],[5,6.8],[7,10.8],[11,13.8],[14,16.8],[17,19.7],[21,25.7],[27,27.8],[28,30.8],[31,33.7],[35,38.7],[40,41.8],[42,44.8],[45,47.7],[49,51.8],[52,55.8],[56,58.8],[59,62.8],[63,69.7]],
 rh='''
F#4+A4+D5:3 A4+C#5+F#5:2 G#4+B4+E5:2
B4+D5+G5:4 A4+C5+F5:3
G4+B4+E5:3 F4+A4+D5:3 R:1
G4+Bb4+Eb5:5 R:1 F4+Ab4+Db5:1
F#4+A4+D5:3 G#4+B4+E5:3 R:1
A4+C5+F5:4 R:1 G4+B4+E5:2
Ab4+C5+F5:3 G4+Bb4+Eb5:3 R:1
F4+A4+D5:3 E4+G4+C5:4
D4+F#4+A4:3 D4+F4+B4:4
E4+G4+C5:7
''',lh='''
C3+E3+G3:3 D3+F#3+A3:4
F3+A3+C4:4 Bb2+D3+F3:3
C3+E3+G3:3 Bb2+D3+F3:3 R:1
Db3+F3+Ab3:5 R:1 Gb2+Bb2+Db3:1
C3+E3+G3:3 D3+F#3+A3:3 R:1
Eb3+G3+Bb3:4 R:1 C3+E3+G3:2
Eb3+G3+Bb3:3 Db3+F3+Ab3:3 R:1
Bb2+D3+F3:3 A2+C3+E3:4
C3+E3+G3:3 G2+B2+F3:4
C3+E3+G3:7
''',sections={1:'p',3:'mp',4:'pp',5:'p',7:'mp',9:'pp'},words={1:'dolce',9:'poco rit.'},slurs=[],lower_phrases=[],hairpins=[('diminuendo',7,9)],tempo_changes={},group=2,
 performance=dict(rubato=[60,59,57,51,59,54,56,50,43,30],phrase_arcs=[[0,21,3],[21,42,2],[42,70,-1]],lower_entries=[],pedal_lift=.2,gate=.98,note='Each paired triad has a tonal centre beneath its unusual upper colour. Let the rests clear the distant harmonies, then give the final unextended C-major chord a simple, unforced sound.'))
,
dict(op=148,title='Hawthorn Interior',key='G',fifths=1,meter='3/2',bpm=58,
 description='Two slow chordal clocks share the same room. Linden Vestibule’s C–D–C becomes G–A–G. For eight bars the upper chords last three quarter beats and the lower chords last four, meeting only every second bar. Their gentle misalignment passes through F and A-flat before both hands find a common pace.',
 difficulty='Advanced sustained three-against-four chordal phrasing',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Every sounded event is a chord of at least three notes. Through bars 1–8 the RH attacks every three quarter beats and the LH every four. Follow the lower ties across alternate bar lines; do not reattack them. The final four bars release this pattern into unequal, shared cadential gestures.',
 parent_opus=145,motif=dict(hand='rh',start_beat=0,end_beat=9,pitches=['G','A','G']),ancestry=dict(source_opus=145,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['C','D','C'],transposition_semitones=7),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=14,pedal_offset_y=460),lower_sections={1:'p',5:'pp',9:'p',11:'pp'},
 pedal_spans=[[i*12+a,i*12+b-.2] for i in range(4) for a,b in zip([0,3,4,6,8,9,12],[3,4,6,8,9,12])]+[[48,50.8],[51,53.8],[54,56.8],[57,59.8],[60,63.8],[64,65.8],[66,71.7]],
 rh='''
B4+D5+G5:3 C5+E5+A5:3
B4+D5+G5:3 A4+C5+F#5:3
A4+C5+F5:3 G4+Bb4+Eb5:3
F4+A4+D5:3 E4+G4+C5:3
Ab4+C5+Eb5:3 F4+Ab4+Db5:3
G4+Bb4+Eb5:3 F4+Ab4+C5:3
G4+B4+D5:3 E4+G4+C5:3
F#4+A4+C5:3 G4+B4+D5:3
A4+C5+E5:3 G4+B4+D5:3
F4+A4+C5:4 E4+G4+B4:2
F#4+A4+C5:4 G4+B4+D5:2
B4+D5+E5+G5:6
''',lh='''
G3+B3+D4:4 E3+G3+B3:2~
E3+G3+B3:2 C3+E3+G3:4
F3+A3+C4:4 Eb3+G3+Bb3:2~
Eb3+G3+Bb3:2 D3+F3+A3:4
Ab2+C3+Eb3:4 Db3+F3+Ab3:2~
Db3+F3+Ab3:2 Eb3+G3+Bb3:4
G2+B2+D3:4 C3+E3+G3:2~
C3+E3+G3:2 D3+F#3+A3:4
A2+C3+E3:6
F3+A3+C4:3 E3+G3+B3:3
D3+F#3+C4:4 G2+B2+D3:2
G3+B3+D4:6
''',sections={1:'p',3:'mp',5:'pp',7:'p',9:'mp',11:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[(1,4),(5,8),(9,12)],lower_phrases=[],hairpins=[('crescendo',7,9),('diminuendo',10,11)],tempo_changes={},group=2,
 performance=dict(rubato=[58,56,59,52,55,52,57,50,54,48,40,28],phrase_arcs=[[0,24,3],[24,48,2],[48,72,-1]],lower_entries=[],pedal_lift=.2,gate=.995,note='Neither hand should force its pulse onto the other. Hold each chord for its full written value and allow the two cycles to meet naturally every twelve quarter beats.'))
,
dict(op=149,title='Willow Palimpsest',key='a',fifths=0,meter='4/4',bpm=57,
 description='One four-bar melody is heard three times through different chord interiors. Fern Lantern’s D–C–D becomes A–G–A. The first setting is close to A minor, the second admits brighter raised fourths and distant major chords, and the third changes the bass direction. A short descending coda returns to A minor with a ninth.',
 difficulty='Advanced chord-melody reharmonisation and inner-voice balance',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Every sounded event is a chord. The top notes and durations of bars 1–4 recur exactly in bars 5–8 and 9–12, but their inner notes and lower harmonies change. Preserve the identity of the melody while allowing its emotional colour to shift. The last two bars are a new coda.',
 parent_opus=135,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['A','G','A']),ancestry=dict(source_opus=135,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=12,source_pitches=['D','C','D'],transposition_semitones=7),
 system_starts=[1,3,5,7,9,11,13],page_starts=[7],engraving=dict(spacing_system=13,pedal_offset_y=440),lower_sections={1:'pp',5:'p',9:'p',13:'pp'},
 pedal_spans=[[i*4+a,i*4+b-.2] for i,cuts in enumerate([[0,1.5,2,4],[0,3,4],[0,1,2,4],[0,3,4],[0,1.5,2,4],[0,3,4],[0,1,2,4],[0,3,4],[0,1.5,2,4],[0,3,4],[0,1,2,4],[0,3,4],[0,1,2,3,4],[0,4]]) for a,b in zip(cuts,cuts[1:])],
 rh='''
C5+E5+A5:1.5 B4+D5+G5:.5 C5+E5+A5:2
G4+B4+E5:3 F4+A4+D5:1
E4+G4+C5:1 G4+C5+E5:1 B4+D5+G5:2
A4+C5+F5:3 G4+B4+E5:1
D5+F#5+A5:1.5 C5+E5+G5:.5 D5+F#5+A5:2
G#4+B4+E5:3 F#4+A4+D5:1
F4+Ab4+C5:1 A4+C5+E5:1 Bb4+Eb5+G5:2
Ab4+Db5+F5:3 Ab4+B4+E5:1
E5+F#5+A5:1.5 D5+E5+G5:.5 E5+F#5+A5:2
A4+C#5+E5:3 G4+B4+D5:1
G4+A4+C5:1 B4+D5+E5:1 C5+E5+G5:2
Bb4+D5+F5:3 A4+C5+E5:1
F4+A4+D5:1 E4+G4+C5:1 D4+G4+B4:1 C4+E4+A4:1
G4+B4+C5+E5:4
''',lh='''
A2+C3+G3:1.5 C3+E3+G3:.5 F3+A3+C4:2
C3+E3+G3:3 D3+F3+A3:1
C3+E3+G3:1 A2+C3+G3:1 G2+B2+D3:2
D3+F3+A3:3 E3+G#3+D4:1
F3+A3+E4:1.5 C3+E3+B3:.5 D3+F#3+A3:2
E3+G#3+B3:3 D3+F#3+A3:1
F3+Ab3+C4:1 A2+C3+E3:1 Eb3+G3+Bb3:2
Db3+F3+Ab3:3 E3+G#3+D4:1
D3+F#3+A3:1.5 E3+G3+B3:.5 B2+D3+F#3:2
A2+C#3+G3:3 E3+G3+B3:1
D3+F3+A3:1 G2+B2+D3:1 C3+E3+G3:2
Bb2+D3+F3:3 A2+C3+G3:1
D3+F3+A3:1 C3+E3+G3:1 G2+B2+D3:1 E3+G#3+B3:1
A2+C3+E3:4
''',sections={1:'p',5:'mp',9:'p',13:'pp'},words={1:'cantabile',13:'poco rit.'},slurs=[(1,4),(5,8),(9,12),(13,14)],lower_phrases=[],hairpins=[('crescendo',5,7),('diminuendo',11,13)],tempo_changes={},group=2,
 performance=dict(rubato=[57,53,58,49,59,55,61,50,56,52,57,47,39,27],phrase_arcs=[[0,16,3],[16,32,4],[32,48,2],[48,56,-2]],lower_entries=[],pedal_lift=.2,gate=.98,note='Keep the returning melody recognisable through the changed interiors. The three versions should feel like a remembered place seen in different light, not three equally weighted chorales.'))
,
dict(op=150,title='Camellia Solstice',key='F',fifths=-1,meter='4/4',bpm=54,
 description='Velvet Estuary’s A–C–D–C returns in luminous upper chords, then descends through quieter harmonic rooms. A whole-tone-lower recollection opens the second half, giving the familiar outline a different weight. The closing voices gather into an F-major ninth held across the last two bars: a resting place for the first one hundred and fifty works.',
 difficulty='Advanced chordal cantabile and sustained closing voicing',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Every sounded event is a chord of at least three pitches. The opening melody is carried by the highest chord notes; its whole-tone-lower reflection begins at bar 9. Let the middle voices stay soft, particularly in the five-note final RH chord. Both hands hold the closing harmony across bars 15–16 without rearticulation.',
 parent_opus=2,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['A','C','D','C']),ancestry=dict(source_opus=2,source_hand='rh',source_start_beat=0,source_end_beat=4.5,source_pitches=['A','C','D','C'],transposition_semitones=0),
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=440),lower_sections={1:'pp',5:'p',9:'pp',13:'pp'},
 pedal_spans=[[i*4+a,i*4+b-.2] for i,cuts in enumerate([[0,1,2,3,4],[0,3,4],[0,4],[0,2,4],[0,3,4],[0,4],[0,1,2,4],[0,3,4],[0,1,2,3,4],[0,3,4],[0,2,4],[0,4],[0,2,4],[0,1,2,4]]) for a,b in zip(cuts,cuts[1:])]+[[56,63.7]],
 rh='''
C5+E5+A5:1 E5+G5+C6:1 F5+A5+D6:1 E5+G5+C6:1
D5+F5+A5:3 C5+E5+G5:1
A4+C5+F5:4
G4+B4+E5:2 A4+C5+F5:2
G4+Bb4+Eb5:3 F4+Ab4+Db5:1
F4+A4+D5:4
E4+G4+C5:1 G4+Bb4+Eb5:1 A4+C5+F5:2
G4+B4+E5:3 F#4+A4+D5:1
Bb4+D5+G5:1 D5+F5+Bb5:1 Eb5+G5+C6:1 D5+F5+Bb5:1
C5+Eb5+G5:3 Bb4+D5+F5:1
A4+C5+F5:2 G4+Bb4+E5:2
F4+A4+D5:4
E4+G4+C5:2 F4+A4+D5:2
Eb4+G4+Bb4:1 D4+F4+A4:1 E4+G4+Bb4:2
F4+G4+A4+C5+E5:4~
F4+G4+A4+C5+E5:4
''',lh='''
D3+F3+C4:1 C3+E3+B3:1 Bb2+D3+A3:1 C3+E3+B3:1
F3+A3+C4:3 C3+E3+G3:1
Db3+F3+Ab3:4
C3+E3+G3:2 D3+F3+A3:2
Ab2+C3+Eb3:3 Gb2+Bb2+Db3:1
Bb2+D3+F3:4
Ab2+C3+Eb3:1 Eb3+G3+Bb3:1 F3+A3+C4:2
C3+E3+G3:3 D3+F#3+A3:1
G2+Bb2+F3:1 F3+A3+E4:1 Eb3+G3+D4:1 F3+A3+E4:1
Eb3+G3+Bb3:3 Bb2+D3+F3:1
Db3+F3+Ab3:2 C3+E3+G3:2
Bb2+D3+F3:4
A2+C3+E3:2 D3+F3+A3:2
Ab2+C3+Eb3:1 Bb2+D3+F3:1 C3+E3+G3:2
F3+A3+C4:4~
F3+A3+C4:4
''',sections={1:'p',3:'pp',5:'p',7:'mp',9:'p',11:'pp',13:'p',15:'pp'},words={1:'cantabile',15:'poco rit.'},slurs=[(1,4),(5,8),(9,12),(13,16)],lower_phrases=[],hairpins=[('crescendo',5,7),('diminuendo',13,15)],tempo_changes={},group=2,
 performance=dict(rubato=[54,51,47,52,50,46,54,47,52,49,46,42,46,41,34,24],phrase_arcs=[[0,16,3],[16,32,3],[32,48,2],[48,64,-2]],lower_entries=[],pedal_lift=.2,gate=.995,note='The high chord melody should sing gently, without brilliance. Let its lower recollection feel familiar but altered, and allow the final eight-note harmony to decay naturally without another attack.'))
,
dict(op=151,title='Heather Soundings',key='e',fifths=1,meter='3/4',bpm=49,
 description='A small E-Dorian song above open fifths. Fern Lantern’s D–C–D becomes E–D–E, sung simply before a five-bar phrase opens toward the raised sixth. A quieter C-natural shadow crosses the return, but the last phrase restores C-sharp and leaves the song resting on an open E fifth.',
 difficulty='Intermediate lyrical phrasing and sustained open fifths',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Keep the single upper melody present over the soft open fifths. The first lower E–B lasts across two bars without reattack. The three phrases have five, five and seven bars; let the written rest in bar 10 mark the deepest breath. Distinguish C-natural in the return from the later C-sharp.',
 parent_opus=135,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['E','D','E']),ancestry=dict(source_opus=135,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=12,source_pitches=['D','C','D'],transposition_semitones=2),
 system_starts=[1,4,6,9,11,14,16],page_starts=[11],engraving=dict(spacing_system=13,pedal_offset_y=440),lower_sections={1:'pp',6:'p',11:'pp'},
 pedal_spans=[[i*3,i*3+(1.8 if i==9 else 2.8)] for i in range(17)],
 rh='''
E5:1.5 D5:.5 E5:1
B4:2 A4:1
G4:1.5 A4:.5 B4:1
C#5:2 B4:1
A4:1 G4:.5 F#4:.5 E4:1
R:1 E5:.5 G5:.5 A5:1
G5:1.5 F#5:.5 E5:1
D5:2 B4:1
A4:1 C#5:1 B4:1
G4:2 R:1
E5:2 D5:1
B4:1.5 A4:.5 G4:1
F#4:1 A4:.5 C5:.5 B4:1
A4:1 B4:1 C#5:1
B4:2 G4:1
F#4:1.5 G4:.5 E4:1
E4+B4:3
''',lh='''
E3+B3:3~
E3+B3:3
D3+A3:3
A2+E3:3
E3+B3:3
A2+E3:3
D3+A3:3
G2+D3:3
A2+E3:3
E3+B3:2 R:1
C3+G3:3
G2+D3:3
D3+A3:3
A2+E3:3
E3+B3:3
B2+F#3:3
E3+B3:3
''',sections={1:'p',6:'mp',11:'p',16:'pp'},words={1:'cantabile',16:'poco rit.'},slurs=[(1,5),(6,10),(11,15),(16,17)],lower_phrases=[],hairpins=[('crescendo',6,7),('diminuendo',14,16)],tempo_changes={},group=2,
 performance=dict(rubato=[49,48,50,47,42,49,51,46,47,39,47,45,48,49,44,36,26],phrase_arcs=[[0,15,3],[15,30,3],[30,51,2]],lower_entries=[],pedal_lift=.2,gate=.985,note='Sing the melody with the unforced pace of a remembered song. The open fifths remain quieter, and the raised sixth offers a little warmth without turning the piece into a major-key resolution.'))
,
dict(op=152,title='Rowan Hinterland',key='g',fifths=-2,meter='5/4',bpm=56,
 description='A song passed between the hands across a broad five-beat span. Heather Soundings’s E–D–E becomes G–F–G; the lower hand repeats the opening two-bar phrase two octaves beneath its first appearance. A second, more searching phrase receives the same answer before the two voices share a quiet close.',
 difficulty='Intermediate to advanced melodic hand exchange',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The LH sings exact two-octave-lower answers in bars 3–4 and 7–8 while the RH holds quiet dyads. Bring the lower staff forward for those answers. The melody should keep its character as it moves between registers; the final phrase belongs to both hands.',
 parent_opus=151,motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['G','F','G']),ancestry=dict(source_opus=151,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['E','D','E'],transposition_semitones=3),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=14,pedal_offset_y=460),lower_sections={1:'pp',3:'mp',5:'pp',7:'mp',9:'p',11:'pp'},
 pedal_spans=[[i*5,i*5+4.8] for i in range(12)],
 rh='''
G5:2 F5:1 G5:2
D5:3 Bb4:2
Bb4+D5:5
A4+C5:5
A5:1 Bb5:.5 D6:.5 F6:2 Eb6:1
D6:2 C6:1 Bb5:2
D5+G5:5
F4+A4:5
G5:1 F5:.5 Eb5:.5 D5:3
C5:2 Bb4:1 A4:2
Bb4:1 D5:1 C5:1 A4:2
G4+Bb4+D5:5
''',lh='''
G2+D3:5
Bb2+F3:3 D3+A3:2
G3:2 F3:1 G3:2
D3:3 Bb2:2
Eb3+Bb3:5
C3+G3:5
A3:1 Bb3:.5 D4:.5 F4:2 Eb4:1
D4:2 C4:1 Bb3:2
Eb3+Bb3:5
F3+C4:2 Eb3+Bb3:1 D3+A3:2
G3:1 F3:1 Eb3:1 D3:2
G2+D3:5
''',sections={1:'p',3:'pp',5:'mp',7:'pp',9:'p',11:'pp'},words={1:'cantabile',11:'poco rit.'},slurs=[(1,2),(5,6),(9,12)],lower_phrases=[(3,4),(7,8),(11,12)],hairpins=[('crescendo',5,6),('diminuendo',9,11)],tempo_changes={},group=2,
 performance=dict(rubato=[56,50,54,48,58,53,55,49,52,48,40,28],phrase_arcs=[[0,10,3],[10,20,2],[20,30,4],[30,40,3],[40,60,-1]],lower_entries=[],pedal_lift=.2,gate=.98,note='Let the lower answers sound like another person carrying the same song. The accompaniment recedes as the melody changes hands.'))
,
dict(op=153,title='Bilberry Harbour',key='d',fifths=-1,meter='6/8',bpm=61,
 description='A gently rocking song built largely from five notes. Heather Soundings’s E–D–E becomes A–G–A over broken lower fifths. The melody rises once into a brighter register, then returns alone for a breath before a B-natural lends the closing phrase a small Dorian warmth.',
 difficulty='Intermediate compound-time song and exposed melodic entry',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Keep the lower broken fifths light and unequal in weight. The LH is silent throughout bar 10, leaving the new upper entry alone. The B-natural in bar 11 briefly colours the otherwise pentatonic melody. The first phrase lasts five bars; do not force an earlier cadence.',
 parent_opus=151,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','G','A']),ancestry=dict(source_opus=151,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['E','D','E'],transposition_semitones=5),
 system_starts=[1,4,7,10,13],page_starts=[],engraving=dict(spacing_system=12,pedal_offset_y=400),lower_sections={1:'pp',6:'p',11:'pp'},
 pedal_spans=[[i*3,i*3+2.8] for i in range(15) if i!=9],
 rh='''
A4:1 G4:.5 A4:1.5
F4:2 D4:1
G4:1 A4:.5 C5:1.5
A4:2 G4:1
F4:1 E4:.5 D4:1.5
A4:1.5 C5:.5 D5:1
F5:1 E5:.5 D5:1.5
C5:1 A4:1 G4:1
F4:3
R:.5 D5:.5 C5:1 A4:1
G4:1 A4:.5 B4:1.5
A4:2 F4:1
E4:1 G4:.5 A4:1.5
F4:1 E4:.5 D4:1.5
D4+F4+A4:3
''',lh='''
D3:1 A3:.5 C4:1.5
Bb2+F3:3
C3:1 G3:.5 Bb3:1.5
F3:1.5 C4:1.5
D3+A3:3
F3:1 C4:.5 E4:1.5
Bb2+F3:3
C3:1 G3:1 E3:1
D3+A3:3
R:3
G2:1 D3:.5 F3:1.5
D3+A3:3
C3:1 G3:.5 Bb3:1.5
A2+E3:3
D3+A3:3
''',sections={1:'p',6:'mp',9:'pp',11:'p',14:'pp'},words={1:'dolce',14:'poco rit.'},slurs=[(1,5),(6,9),(10,15)],lower_phrases=[],hairpins=[('crescendo',6,7),('diminuendo',12,14)],tempo_changes={},group=2,
 performance=dict(rubato=[61,58,62,57,51,61,64,58,49,56,59,54,56,45,30],phrase_arcs=[[0,15,3],[15,27,3],[27,45,2]],lower_entries=[],pedal_lift=.2,gate=.98,note='A soft rocking motion supports the song without making it hurry. The unaccompanied entry should feel like a new breath, and the borrowed sixth should pass naturally.'))
,
dict(op=154,title='Sorrel Barrow',key='c',fifths=-3,meter='4/4',bpm=48,
 description='A low song beneath distant bell notes. Rowan Hinterland’s G–F–G becomes C–B-flat–C in the left hand. The upper hand uses only the three notes of C minor, leaving the lower melody to change their meaning. A shared silence divides the opening phrase from the higher, more searching continuation.',
 difficulty='Intermediate lower melody and quiet bell-note balance',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The LH is the singing voice. Keep the RH very soft; all its pitches belong to C, E-flat and G. Both hands release for the last beat of bar 4. Do not let the bell notes obscure the stepwise lower phrase or its longer held notes.',
 parent_opus=152,motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['C','Bb','C']),ancestry=dict(source_opus=152,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['G','F','G'],transposition_semitones=5),
 system_starts=[1,4,7,10],page_starts=[],engraving=dict(spacing_system=14,pedal_offset_y=460),lower_sections={1:'p',5:'mp',9:'p',11:'pp'},
 pedal_spans=[[i*4,i*4+(2.8 if i==3 else 3.8)] for i in range(12)],
 rh='''
G5:2 Eb5:2
C5:4
Eb5:2 G5:2
C5:3 R:1
G5:2 Eb5:2
C5:4
G5:1 R:1 Eb5:2
C5:4
Eb5:2 G5:2
G5:2 Eb5:2
C5:4
G4+C5+Eb5:4
''',lh='''
C4:1.5 Bb3:.5 C4:2
Ab3:2 G3:1 Eb3:1
F3:1 G3:1 Bb3:2
C4:3 R:1
D4:1 Eb4:1 F4:2
Eb4:1 D4:.5 C4:.5 Bb3:2
Ab3:2 G3:2
F3:1 G3:.5 Ab3:.5 Bb3:2
C4:3 Bb3:1
Ab3:2 G3:1 F3:1
Eb3:1 G3:.5 Bb3:.5 C4:2
C3+G3:4
''',sections={1:'pp',5:'pp',9:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[],lower_phrases=[(1,4),(5,8),(9,12)],hairpins=[],tempo_changes={},group=2,
 performance=dict(rubato=[48,46,49,40,49,48,44,47,44,42,35,25],phrase_arcs=[[0,16,3],[16,32,3],[32,48,-1]],lower_entries=[],pedal_lift=.2,gate=.985,note='The lower melody carries the human voice; the upper triad tones remain distant. Let the shared rest clear the first phrase before the melody climbs.'))
,
dict(op=155,title='Yarrow Peninsula',key='f#',fifths=3,meter='5/4',bpm=55,
 description='The two hands begin by singing one tune two octaves apart. Heather Soundings’s E–D–E becomes F-sharp–E–F-sharp, carried through three unison bars before the lower hand opens into fifths. A raised sixth brightens the long second phrase, and the closing melody rests over a quiet minor-sixth chord.',
 difficulty='Intermediate octave-separated unison and modal phrasing',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The first three bars have identical melodic rhythm in both hands, separated by two octaves. Match their phrasing without giving the low notes extra weight. After bar 3 the hands become independent. The D-sharp in bar 7 and at the close is the warm Dorian sixth.',
 parent_opus=151,motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['F#','E','F#']),ancestry=dict(source_opus=151,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['E','D','E'],transposition_semitones=2),
 system_starts=[1,4,7,10],page_starts=[],engraving=dict(spacing_system=14,pedal_offset_y=440),lower_sections={1:'p',4:'pp',6:'p',11:'pp'},
 pedal_spans=[[i*5,i*5+(3.8 if i==4 else 4.8)] for i in range(12)],
 rh='''
F#4:2 E4:1 F#4:2
A4:3 G#4:2
C#5:2 B4:1 A4:2
G#4:1 B4:1 A4:3
F#4:4 R:1
F#4:1 A4:1 B4:1 C#5:2
D#5:3 C#5:2
B4:2 A4:1 G#4:2
F#4:2 E4:1 F#4:2
G#4:1 A4:1 B4:3
C#5:2 B4:1 G#4:2
F#4+A4+C#5+D#5:5
''',lh='''
F#2:2 E2:1 F#2:2
A2:3 G#2:2
C#3:2 B2:1 A2:2
B2+F#3:5
F#2+C#3:4 R:1
F#2+C#3:5
B2+F#3:5
E3+B3:5
B2:2 F#3:1 A3:2
E3:1 G#3:1 B3:3
C#3+G#3:2 B2+F#3:1 A2+E3:2
F#2+C#3:5
''',sections={1:'p',6:'mp',9:'p',11:'pp'},words={1:'cantabile',11:'poco rit.'},slurs=[(1,5),(6,8),(9,12)],lower_phrases=[(1,3)],hairpins=[('crescendo',6,7),('diminuendo',9,11)],tempo_changes={},group=2,
 performance=dict(rubato=[55,52,56,51,43,54,57,48,52,49,40,28],phrase_arcs=[[0,25,3],[25,40,4],[40,60,-1]],lower_entries=[],pedal_lift=.2,gate=.985,note='The opening is one song in two registers. Keep its low doubling gentle, and allow the later independence to arrive gradually rather than as a change of character.'))
]
