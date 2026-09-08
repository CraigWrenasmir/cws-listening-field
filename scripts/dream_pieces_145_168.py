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
,
dict(op=156,title='Alder Snowmelt',key='F',fifths=-1,meter='3/4',bpm=52,
 description='A brighter elegy in F, with a raised fourth and a passing minor shadow. Camellia Solstice’s A–C–D–C becomes E–G–A–G, carried by a single singing line. The middle briefly folds into F minor and D-flat before the opening returns with a warmer lower third. The final major seventh remains gently unresolved.',
 difficulty='Intermediate modal colour and long lyrical arcs',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Shape phrases of four, seven and seven bars. The two full-hand rests at bars 4 and 11 separate them. Distinguish the B-natural colour from the later B-flat lower harmony, and allow the borrowed A-flat passage to darken briefly without slowing every note.',
 parent_opus=150,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['E','G','A','G']),ancestry=dict(source_opus=150,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['A','C','D','C'],transposition_semitones=-5),
 system_starts=[1,4,7,10,13,16],page_starts=[10],engraving=dict(spacing_system=14,pedal_offset_y=440),lower_sections={1:'pp',5:'p',8:'pp',12:'p',16:'pp'},
 pedal_spans=[[i*3,i*3+(1.8 if i in [3,10] else 2.8)] for i in range(18)],
 rh='''
E5:1 G5:.5 A5:1 G5:.5
E5:2 D5:1
C5:1 A4:1 G4:1
E4:2 R:1
G4:1 B4:1 D5:1
E5:2 D5:1
C5:1 B4:.5 A4:.5 G4:1
Ab4:2 C5:1
Eb5:1 Db5:.5 C5:.5 Ab4:1
G4:2 F4:1
E4:2 R:1
E5:1 G5:.5 A5:1 G5:.5
D5:2 C5:1
B4:1 D5:.5 E5:1 D5:.5
C5:2 A4:1
G4:1 A4:1 C5:1
B4:1 A4:1 G4:1
F4+A4+E5:3
''',lh='''
F3+C4:3
G3+B3:3
A3+E4:3
F3+C4:2 R:1
G3+B3:3
A3+E4:3
F3+C4:3
F3+C4:3
Db3+Ab3:3
C3+G3:3
C3+G3:2 R:1
F3+A3:3
Bb2+F3:3
G3+B3:3
F3+C4:3
A2+E3:3
C3+G3:3
F3+C4:3
''',sections={1:'p',5:'mp',8:'pp',12:'p',16:'pp'},words={1:'dolce',17:'poco rit.'},slurs=[(1,4),(5,11),(12,18)],lower_phrases=[],hairpins=[('crescendo',5,6),('diminuendo',14,17)],tempo_changes={},group=2,
 performance=dict(rubato=[52,50,48,41,52,54,49,46,48,44,38,51,47,50,45,43,36,25],phrase_arcs=[[0,12,2],[12,33,3],[33,54,2]],lower_entries=[],pedal_lift=.2,gate=.985,note='The brightness should feel fragile and warm. Keep the melody simple, letting the changing modal colours arrive through the harmony rather than a stronger attack.'))
,
dict(op=157,title='Heather Afterimage',key='a',fifths=0,meter='4/4',bpm=50,
 description='A remembered song returns with small gaps in it. Heather Soundings’s rising G–A–B becomes C–D–E above A minor. Its second appearance enters a distant flat-key region; the last return inserts silence between the familiar notes, leaving the listener to carry the phrase across the gaps.',
 difficulty='Intermediate melodic recall and measured phrase gaps',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The rising C–D–E begins bars 1, 6 and 10. In bar 10 a quarter rest separates C from D; bar 11 also interrupts the continuation. Keep these rests exact without making the returning tune sound fragmented in intention. The accompaniment remains soft and open.',
 parent_opus=151,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['C','D','E']),ancestry=dict(source_opus=151,source_hand='rh',source_start_beat=6,source_end_beat=9,source_pitches=['G','A','B'],transposition_semitones=5),
 system_starts=[1,4,6,9,11],page_starts=[],engraving=dict(spacing_system=12,pedal_offset_y=400),lower_sections={1:'pp',6:'p',10:'pp'},
 pedal_spans=[[i*4,i*4+(2.8 if i in [4,8] else 3.8)] for i in range(13)],
 rh='''
C5:1 D5:1 E5:2
G5:3 E5:1
D5:1 C5:1 A4:2
B4:1 D5:.5 E5:.5 G5:2
E5:3 R:1
C5:1 D5:1 E5:2
F5:2 Eb5:1 C5:1
Bb4:1 C5:1 Db5:2
C5:3 R:1
C5:1 R:1 D5:1 E5:1
G5:2 R:1 E5:1
D5:1 C5:1 A4:2
G4+B4+C5+E5:4
''',lh='''
A2:2 E3:2
C3+G3:4
F3+C4:2 E3+B3:2
G2+D3:4
A2+E3:3 R:1
F3+C4:4
Ab2+Eb3:4
Db3+Ab3:4
Ab2+Eb3:3 R:1
A2+E3:4
G2+D3:4
F3+C4:2 E3+B3:2
A2+E3:4
''',sections={1:'p',6:'mp',9:'pp',10:'p',12:'pp'},words={1:'cantabile',12:'poco rit.'},slurs=[(1,5),(6,9),(10,13)],lower_phrases=[],hairpins=[('crescendo',6,7),('diminuendo',10,12)],tempo_changes={},group=2,
 performance=dict(rubato=[50,48,49,52,42,51,49,46,39,47,44,37,26],phrase_arcs=[[0,20,3],[20,36,3],[36,52,-1]],lower_entries=[],pedal_lift=.2,gate=.98,note='Keep the shape of the remembered tune through its silences. The flat-key middle should feel more distant, and the final gaps should soften the phrase rather than break it.'))
,
dict(op=158,title='Larch Footbridge',key='d',fifths=-1,meter='4/4',bpm=51,
 description='Two singing lines walk a bar apart. Bilberry Harbour’s A–G–A becomes D–C–D, beginning a quiet canon whose lower voice follows one octave below. A second subject rises a whole tone into E minor. The last chord lets the two lines rest together in A minor with a ninth.',
 difficulty='Intermediate to advanced two-voice canon and independent phrasing',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The LH follows the first seven RH bars exactly, one bar later and one octave lower. A new upper subject begins in bar 8; its five-bar answer starts in bar 9. Preserve the rests and phrase endings in each hand independently. The last bar leaves the canon for a shared chord.',
 parent_opus=153,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','C','D']),ancestry=dict(source_opus=153,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','G','A'],transposition_semitones=5),
 system_starts=[1,3,5,7,9,11,13],page_starts=[7],engraving=dict(spacing_system=13,pedal_offset_y=500),lower_sections={1:'pp',2:'p',6:'mp',9:'p',14:'pp'},
 pedal_spans=[[i*4+a,i*4+a+1.8] for i in range(14) for a in [0,2]],
 rh='''
D5:1 C5:1 D5:2
A4:2 F4:1 G4:1
A4:3 C5:1
D5:4
F5:2 E5:1 D5:1
C5:2 Bb4:1 A4:1
G4:3 R:1
E5:1 D5:1 E5:2
B4:2 G4:1 A4:1
B4:3 D5:1
E5:4
G5:2 F#5:1 E5:1
D5:2 C5:1 B4:1
G4+B4+C5+E5:4
''',lh='''
R:4
D4:1 C4:1 D4:2
A3:2 F3:1 G3:1
A3:3 C4:1
D4:4
F4:2 E4:1 D4:1
C4:2 Bb3:1 A3:1
G3:3 R:1
E4:1 D4:1 E4:2
B3:2 G3:1 A3:1
B3:3 D4:1
E4:4
G4:2 F#4:1 E4:1
A3+E4:4
''',sections={1:'p',5:'mp',8:'p',12:'mp',14:'pp'},words={1:'cantabile',13:'poco rit.'},slurs=[(1,4),(5,7),(8,11),(12,14)],lower_phrases=[(2,5),(6,8),(9,12),(13,14)],hairpins=[],tempo_changes={},group=2,
 performance=dict(rubato=[51,51,52,48,54,52,46,50,51,52,47,52,40,28],phrase_arcs=[[0,16,3],[16,28,3],[28,44,3],[44,56,-1]],lower_entries=[],pedal_lift=.2,gate=.985,note='Neither line becomes accompaniment when the other is singing. Keep each phrase connected through the other hand’s arrivals, letting the shared closing harmony emerge from the two paths.'))
,
dict(op=159,title='Bracken Lowlight',key='b',fifths=2,meter='4/4',bpm=50,
 description='A song in soft sixths moves above a descending bass. Heather Soundings’s E–D–E becomes B–A–B. The paired melody opens into an unexpected flat-key middle before finding B minor again, like familiar ground briefly seen in unfamiliar light.',
 difficulty='Intermediate legato sixths and changing harmonic colour',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The RH dyads remain sixths through bar 11; their upper notes carry the tune. Let the descending B–A–G–F-sharp bass in the first four bars remain audible. Both hands breathe at the end of bar 5. The final triad gathers the paired line into one chord.',
 parent_opus=151,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['B','A','B']),ancestry=dict(source_opus=151,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['E','D','E'],transposition_semitones=-5),
 system_starts=[1,4,7,10],page_starts=[],engraving=dict(spacing_system=14,pedal_offset_y=440),lower_sections={1:'pp',6:'p',9:'pp'},
 pedal_spans=[[i*4+a,i*4+b] for i in range(12) for a,b in ([(0,2.8)] if i==4 else [(0,1.8),(2,3.8)] if i in [6,8,9] else [(0,2.8),(3,3.8)] if i==10 else [(0,3.8)])],
 rh='''
D4+B4:1.5 C#4+A4:.5 D4+B4:2
E4+C#5:2 F#4+D5:2
G4+E5:3 F#4+D5:1
E4+C#5:2 D4+B4:2
C#4+A4:3 R:1
F#4+D5:1 G4+E5:1 A4+F#5:2
G4+E5:2 F4+Db5:2
Eb4+C5:3 Db4+Bb4:1
C4+A4:2 D4+B4:2
E4+C#5:1.5 F#4+D5:.5 E4+C#5:2
D4+B4:3 C#4+A4:1
D4+F#4+B4:4
''',lh='''
B2+F#3:4
A2+E3:4
G2+D3:4
F#2+C#3:4
E3+B3:3 R:1
D3+A3:4
C3+G3:4
Ab2+Eb3:4
F3+A3:2 E3+B3:2
A2+E3:2 F#2+C#3:2
G2+D3:3 F#2+C#3:1
B2+F#3:4
''',sections={1:'p',6:'mp',9:'p',11:'pp'},words={1:'cantabile',11:'poco rit.'},slurs=[(1,5),(6,8),(9,12)],lower_phrases=[],hairpins=[('crescendo',6,7),('diminuendo',9,11)],tempo_changes={},group=2,
 performance=dict(rubato=[50,51,49,48,40,51,48,45,49,47,39,27],phrase_arcs=[[0,20,3],[20,32,4],[32,48,-1]],lower_entries=[],pedal_lift=.2,gate=.98,note='The lower member of each sixth is a shadow of the tune. Shape the flat-key turn as a single long breath, with the bass quietly guiding the return.'))
,
dict(op=160,title='Willow Homeward',key='F',fifths=-1,meter='3/4',bpm=53,
 description='A homecoming song that begins over D minor and closes in F major. Alder Snowmelt’s E–G–A–G becomes A–C–D–C. After a brief minor-coloured detour the upper voice falls silent, leaving the lower hand to remember the opening alone before both hands find a gentle major ending.',
 difficulty='Intermediate singing line and exposed lower-hand answer',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The first two bars return exactly one octave lower in bars 11–12, with the RH silent. Give that answer its own vocal shape. The rests in bars 5 and 10 divide the first two phrases; the final seven bars continue through the lower-hand recollection into F major.',
 parent_opus=156,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','C','D','C']),ancestry=dict(source_opus=156,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['E','G','A','G'],transposition_semitones=5),
 system_starts=[1,4,7,10,13,16],page_starts=[10],engraving=dict(spacing_system=14,pedal_offset_y=460),lower_sections={1:'pp',6:'p',11:'mp',13:'pp'},
 pedal_spans=[[i*3,i*3+(1.8 if i in [4,9] else 2.8)] for i in range(17)],
 rh='''
A4:.5 C5:.5 D5:1 C5:1
A4:2 G4:1
F4:1 G4:.5 A4:.5 C5:1
D5:2 E5:1
F5:2 R:1
E5:1 D5:1 C5:1
A4:2 C5:1
Eb5:1 Db5:1 C5:1
Bb4:2 Ab4:1
G4:2 R:1
R:3
R:3
F4:1 A4:1 C5:1
D5:1 C5:2
A4:1 G4:1 F4:1
E4+G4:2 C4+E4:1
F4+A4+C5:3
''',lh='''
D3+A3:3
Bb2+F3:3
F3+C4:3
G3+D4:3
D3+A3:2 R:1
C3+G3:3
F3+C4:3
Ab2+Eb3:3
Db3+Ab3:3
C3+G3:2 R:1
A3:.5 C4:.5 D4:1 C4:1
A3:2 G3:1
F3+C4:3
Bb2+F3:3
C3+G3:3
Bb2+F3:3
F3+C4:3
''',sections={1:'p',4:'mp',6:'p',11:'pp',13:'p',16:'pp'},words={1:'cantabile',16:'poco rit.'},slurs=[(1,5),(6,10),(13,17)],lower_phrases=[(11,12)],hairpins=[('crescendo',13,14),('diminuendo',15,16)],tempo_changes={},group=2,
 performance=dict(rubato=[53,51,54,52,44,53,52,48,46,40,50,47,52,50,46,38,26],phrase_arcs=[[0,15,4],[15,30,2],[30,51,3]],lower_entries=[[30,36]],pedal_lift=.2,gate=.985,note='Let the solo lower answer feel remembered rather than newly announced. The change to major should arrive gradually, carrying some of the opening minor colour into the last phrase.'))
,
dict(op=161,title='Cypress Afterhours',key='d',fifths=-1,meter='2/4',bpm=54,
 description='A slow dance with a dotted, habanera-like bass and a melody that sometimes floats across the bar line. Larch Footbridge’s D–C–D returns in a new rhythmic setting. The central flat-key passage darkens the room briefly; the returning tune gradually releases the dance into a held D-minor chord.',
 difficulty='Intermediate to advanced dotted bass rhythm under sustained melody',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Most bass bars divide into three sixteenths, one sixteenth and two eighths. Keep that written pulse supple under the upper ties in bars 3–4 and 15–16. Both hands breathe in bars 6 and 12. The final two bars sustain one chord without repeating it.',
 parent_opus=158,motif=dict(hand='rh',start_beat=0,end_beat=2,pitches=['D','C','D']),ancestry=dict(source_opus=158,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','C','D'],transposition_semitones=0),
 system_starts=[1,5,9,13,17,20],page_starts=[13],engraving=dict(spacing_system=14,pedal_offset_y=480),lower_sections={1:'pp',7:'p',13:'pp'},
 pedal_spans=[[i*2,i*2+(1.3 if i in [5,11] else 1.8)] for i in range(20)]+[[40,43.8]],
 rh='''
D5:.75 C5:.25 D5:1
A4:1.5 C5:.5
F5:2~
F5:.5 E5:.5 D5:1
C5:1 A4:.5 G4:.5
A4:1.5 R:.5
Bb4:.5 D5:1 C5:.5
A4:1 G4:1
Ab4:.75 C5:.25 Eb5:1
Db5:1 C5:1
Bb4:.5 Ab4:.5 G4:1
A4:1.5 R:.5
D5:.75 C5:.25 D5:1
F5:1 E5:.5 D5:.5
C5:2~
C5:.5 Bb4:.5 A4:1
G4:1 E4:.5 F4:.5
A4:1.5 C5:.5
Bb4:1 A4:.5 G4:.5
E4+G4:1 C#4+E4:1
D4+F4+A4:2~
D4+F4+A4:2
''',lh='''
D3:.75 A3:.25 F3:.5 A3:.5
C3:.75 G3:.25 E3:.5 G3:.5
Bb2:.75 F3:.25 D3:.5 D3:.5
G2:.75 D3:.25 Bb2:.5 D3:.5
A2:.75 E3:.25 C3:.5 E3:.5
D3+A3:1.5 R:.5
Bb2:.75 F3:.25 D3:.5 F3:.5
C3:.75 G3:.25 E3:.5 E3:.5
Ab2:.75 Eb3:.25 C3:.5 Eb3:.5
Db3:.75 Ab3:.25 F3:.5 Ab3:.5
C3:.75 G3:.25 Eb3:.5 G3:.5
A2+E3:1.5 R:.5
D3:.75 A3:.25 F3:.5 A3:.5
C3:.75 G3:.25 E3:.5 G3:.5
Bb2:.75 F3:.25 D3:.5 F3:.5
F3:.75 C4:.25 A3:.5 C4:.5
E3:.75 B3:.25 G3:.5 B3:.5
F3:.75 C4:.25 A3:.5 C4:.5
G3+Bb3:1 F3+A3:1
A2+E3:2
D3+A3:2~
D3+A3:2
''',sections={1:'p',7:'mp',12:'pp',13:'p',19:'pp'},words={1:'dolce',20:'poco rit.'},slurs=[(1,6),(7,12),(13,18),(19,22)],lower_phrases=[],hairpins=[('crescendo',7,9),('diminuendo',17,20)],tempo_changes={},group=2,
 performance=dict(rubato=[54,54,55,53,51,46,54,54,52,50,49,43,54,55,53,51,50,49,45,39,31,26],phrase_arcs=[[0,12,3],[12,24,4],[24,36,3],[36,44,-2]],lower_entries=[],pedal_lift=.2,gate=.975,note='The bass has a small spring in its dotted rhythm. Keep its weight low enough for the long upper notes to seem suspended, and let the last four bars gradually lose their urge to dance.'))
,
dict(op=162,title='Juniper Arcade',key='a',fifths=0,meter='3/4',bpm=56,
 description='A hesitant night waltz: a bass note, a small chord, a gap, and a late response. Cypress Afterhours’s D–C–D becomes A–G–A, now surrounded by warm sevenths and a little Dorian light. Phrases of four, five and six bars let the melody stretch beyond the accompaniment’s regular steps.',
 difficulty='Intermediate to advanced delayed waltz responses and sustained melody',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The eighth rest in the recurring LH figure delays its second chord response. Keep that gap distinct within the quiet pedal resonance. The first E in bar 3 continues into bar 4; do not repeat it. F-sharp in bar 7 briefly brightens the A-minor setting.',
 parent_opus=161,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','G','A']),ancestry=dict(source_opus=161,source_hand='rh',source_start_beat=0,source_end_beat=2,source_pitches=['D','C','D'],transposition_semitones=7),
 system_starts=[1,4,7,10,13],page_starts=[],engraving=dict(spacing_system=12,pedal_offset_y=450),lower_sections={1:'pp',5:'p',10:'pp'},
 pedal_spans=[[i*3,i*3+(1.8 if i in [3,8] else 2.8)] for i in range(15)],
 rh='''
A4:.5 G4:.5 A4:2
C5:1 B4:.5 A4:1.5
E5:3~
E5:1 D5:1 R:1
C5:.5 B4:.5 D5:2
E5:2 G5:1
F#5:1 E5:1 D5:1
C5:1 A4:1 G4:1
B4:2 R:1
A4:.5 G4:.5 A4:2
C5:1 D5:.5 E5:1.5
G5:2 E5:1
D5:1 C5:1 B4:1
A4:1 G4:1 E4:1
G4+B4+C5+E5:3
''',lh='''
A2:1 E3+G3:.5 R:.5 C4+E4:1
G2:1 D3+F3:.5 R:.5 B3+D4:1
F3:1 A3+C4:.5 R:.5 A3+C4:1
E3+B3:2 R:1
F3:1 A3+C4:.5 R:.5 A3+C4:1
C3:1 G3+B3:.5 R:.5 G3+B3:1
D3:1 A3+C4:.5 R:.5 A3+C4:1
F3:1 A3+C4:2
E3+B3:2 R:1
A2:1 E3+G3:.5 R:.5 C4+E4:1
F3:1 A3+C4:.5 R:.5 A3+C4:1
C3:1 G3+B3:.5 R:.5 G3+B3:1
G2:1 D3+F3:.5 R:.5 G3+B3:1
F3:1 A3+C4:2
A2+E3:3
''',sections={1:'p',5:'mp',9:'pp',10:'p',14:'pp'},words={1:'dolce',14:'poco rit.'},slurs=[(1,4),(5,9),(10,15)],lower_phrases=[],hairpins=[('crescendo',5,7),('diminuendo',12,14)],tempo_changes={},group=2,
 performance=dict(rubato=[56,56,57,48,56,58,57,54,46,56,57,55,51,43,28],phrase_arcs=[[0,12,3],[12,27,4],[27,45,2]],lower_entries=[],pedal_lift=.2,gate=.98,note='Give the little late chords a feeling of leaning towards the next step. The tune stays unhurried above them, gathering warmth through the middle phrase and relaxing into the final ninth.'))
,
dict(op=163,title='Laurel Underpass',key='e',fifths=1,meter='4/4',bpm=55,
 description='A nocturnal walk in uneven steps: three eighths, three eighths, then two. Heather Afterimage’s C–D–E becomes G–A–B over E minor. The melody crosses the bass accents, rises into a Dorian phrase and turns briefly towards G minor before recovering its opening warmth.',
 difficulty='Intermediate to advanced 3+3+2 accompaniment against lyrical phrasing',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The recurring LH attacks fall on quarter-beat offsets 0, 1.5 and 3. Avoid shifting the RH to match them. Its long E begins midway through bar 5 and continues into bar 6. Bars 4 and 12 release the recurring pattern into longer harmonies.',
 parent_opus=157,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['G','A','B']),ancestry=dict(source_opus=157,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['C','D','E'],transposition_semitones=7),
 system_starts=[1,4,7,10],page_starts=[],engraving=dict(spacing_system=14,pedal_offset_y=470),lower_sections={1:'pp',5:'p',10:'pp'},
 pedal_spans=[[i*4,i*4+(2.8 if i==3 else 3.8)] for i in range(12)],
 rh='''
G4:1 A4:1 B4:2
D5:3 B4:1
A4:.5 R:.5 G4:1 E4:2
F#4:3 R:1
B4:1 D5:.5 E5:2.5~
E5:1 D5:1 C#5:1 B4:1
A4:1 F#4:1 E4:2
G4:1 Bb4:1 D5:2
C5:1 Bb4:1 A4:1 F4:1
G4:1 A4:1 B4:2
D5:1 B4:1 A4:1 G4:1
F#4:1 E4+G4+B4:3
''',lh='''
E3:1.5 G3+B3:1.5 F#3+B3:1
D3:1.5 F#3+A3:1.5 E3+A3:1
C3:1.5 E3+G3:1.5 E3+B3:1
B2+F#3:3 R:1
G3:1.5 B3+D4:1.5 A3+D4:1
A3:1.5 C#4+E4:1.5 B3+E4:1
D3:1.5 F#3+A3:1.5 E3+A3:1
G3:1.5 Bb3+D4:1.5 A3+D4:1
F3:1.5 A3+C4:1.5 G3+C4:1
E3:1.5 G3+B3:1.5 F#3+B3:1
C3:1.5 E3+G3:1.5 D3+G3:1
E3+B3:4
''',sections={1:'p',5:'mp',8:'p',11:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[(1,4),(5,9),(10,12)],lower_phrases=[],hairpins=[('crescendo',5,6),('diminuendo',10,11)],tempo_changes={},group=2,
 performance=dict(rubato=[55,55,53,45,56,57,54,52,48,54,45,30],phrase_arcs=[[0,16,3],[16,36,4],[36,48,-1]],lower_entries=[],pedal_lift=.2,gate=.98,note='The unequal bass steps should feel like a quiet current under the song. Let the RH phrase breathe across them, with a little more space at the flat-key turn and the final return.'))
,
dict(op=164,title='Saffron Promenade',key='f',fifths=-4,meter='6/8',bpm=63,
 description='A slow rocking dance in F minor, with long-short steps inside each compound beat. Willow Homeward’s F–A–C becomes A-flat–C–E-flat. The middle opens unexpectedly into major colour; the returning minor melody keeps a little of that light in its final added sixth.',
 difficulty='Intermediate compound lilt and changing minor-major colour',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The LH often divides each dotted-quarter beat into a quarter and an eighth. Let that gentle lilt support the longer upper line. Both hands rest for the second half of bars 4 and 9. Distinguish D-flat in the returning phrase from D-natural in the middle and final chord.',
 parent_opus=160,motif=dict(hand='rh',start_beat=0,end_beat=2,pitches=['Ab','C','Eb']),ancestry=dict(source_opus=160,source_hand='rh',source_start_beat=36,source_end_beat=39,source_pitches=['F','A','C'],transposition_semitones=3),
 system_starts=[1,4,7,10,13],page_starts=[],engraving=dict(spacing_system=12,pedal_offset_y=470),lower_sections={1:'pp',5:'p',10:'pp'},
 pedal_spans=[[i*3,i*3+(1.3 if i in [3,8] else 2.8)] for i in range(15)],
 rh='''
Ab4:.5 C5:.5 Eb5:1 C5:1
Eb5:1.5 C5:1 Bb4:.5
Ab4:1 G4:.5 F4:1 G4:.5
Ab4:1.5 R:1.5
A4:1 C5:.5 E5:1 D5:.5
C5:1.5 A4:1 G4:.5
B4:1 D5:.5 F5:1 E5:.5
D5:1.5 C5:1 A4:.5
G4:1.5 R:1.5
Ab4:.5 C5:.5 Eb5:1 C5:1
Eb5:1.5 F5:1 Eb5:.5
Db5:1 C5:.5 Bb4:1 Ab4:.5
G4:1 Bb4:.5 C5:1 Bb4:.5
Ab4:1.5 G4:1 F4:.5
Ab4+C5+D5:3
''',lh='''
F3:1 C4:.5 Ab3:1 Ab3:.5
Db3:1 Ab3:.5 F3:1 F3:.5
Bb2:1 F3:.5 Db3:1 F3:.5
C3+G3:1.5 R:1.5
F3:1 C4:.5 A3:1 A3:.5
D3:1 A3:.5 F3:1 A3:.5
G3:1 D4:.5 B3:1 D4:.5
A3:1 E4:.5 C4:1 G3:.5
C3+G3:1.5 R:1.5
F3:1 C4:.5 Ab3:1 C4:.5
Ab3:1 Eb4:.5 C4:1 Ab3:.5
Db3:1 Ab3:.5 F3:1 Ab3:.5
Eb3:1 Bb3:.5 G3:1 Bb3:.5
Db3:1 Ab3:.5 F3:1 Ab3:.5
F3+C4:3
''',sections={1:'p',5:'mp',9:'pp',10:'p',14:'pp'},words={1:'dolce',14:'poco rit.'},slurs=[(1,4),(5,9),(10,15)],lower_phrases=[],hairpins=[('crescendo',5,7),('diminuendo',12,14)],tempo_changes={},group=2,
 performance=dict(rubato=[63,64,62,53,65,65,66,62,51,63,65,62,59,49,32],phrase_arcs=[[0,12,3],[12,27,4],[27,45,2]],lower_entries=[],pedal_lift=.2,gate=.98,note='Keep the two rocking beats broad enough for the short notes to settle gently into them. The major passage is a passing clearing; retain its warmth when the minor tune returns.'))
,
dict(op=165,title='Elm Interchange',key='c',fifths=-3,meter='5/4',bpm=55,
 description='A spacious five-beat dance whose weight shifts from three-plus-two to two-plus-three. Willow Homeward’s A–C–D becomes G–B-flat–C over C minor. A full two-beat breath opens the central phrase, where a brief F-major light leads back through G into a quiet minor ninth.',
 difficulty='Intermediate to advanced shifting five-beat balance and chord voicing',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The opening bass moves for three beats, then settles into a two-beat chord. Bars 5–6 reverse that balance: chord first, moving notes afterwards. Leave the two beats of shared silence in bar 4 intact. Voice the highest note of the final four-note RH chord without forcing its ninth.',
 parent_opus=160,motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['G','Bb','C']),ancestry=dict(source_opus=160,source_hand='rh',source_start_beat=0,source_end_beat=2,source_pitches=['A','C','D'],transposition_semitones=-2),
 system_starts=[1,4,6,9],page_starts=[],engraving=dict(spacing_system=14,pedal_offset_y=490),lower_sections={1:'pp',5:'p',9:'pp'},
 pedal_spans=[[i*5+a,i*5+b] for i in range(11) for a,b in ([(0,2.8)] if i==3 else [(0,2.8),(3,4.8)] if i==9 else [(0,4.8)])],
 rh='''
G4:1 Bb4:1 C5:3
Eb5:2 D5:1 C5:2
Bb4:1.5 G4:.5 F4:3
D4+G4:3 R:2
Ab4:1 C5:1 Eb5:3
D5:2 C5:1 Bb4:2
A4:1.5 C5:.5 E5:3
D5:2 B4:1 G4:2
G4:1 Bb4:1 C5:3
Eb5:2 D5:1 Bb4:2
Eb4+G4+Bb4+D5:5
''',lh='''
C3:1.5 G3:.5 Bb3:1 Eb3+G3:2
Ab2:1.5 Eb3:.5 G3:1 C3+Eb3:2
F3:1.5 C4:.5 Ab3:1 C3+G3:2
G2+D3:3 R:2
Ab2+Eb3:2 C3:1.5 G3:.5 C4:1
Bb2+F3:2 D3:1.5 A3:.5 D4:1
F3:1.5 C4:.5 A3:1 E3+A3:2
G3+B3:3 D3+G3:2
C3:1.5 G3:.5 Bb3:1 Eb3+G3:2
Ab2:1.5 Eb3:.5 G3:1 Bb2+F3:2
C3+G3:5
''',sections={1:'p',5:'mp',8:'p',10:'pp'},words={1:'dolce',10:'poco rit.'},slurs=[(1,4),(5,8),(9,11)],lower_phrases=[],hairpins=[('crescendo',5,7),('diminuendo',9,10)],tempo_changes={},group=2,
 performance=dict(rubato=[55,56,53,45,56,56,57,50,54,45,30],phrase_arcs=[[0,20,3],[20,40,4],[40,55,-1]],lower_entries=[],pedal_lift=.2,gate=.98,note='Keep a sense of dancing through the extra beat. The reversal in the middle should feel like changing direction while still holding the same partner, and the final chord should settle without closing every colour.'))
,
dict(op=166,title='Violet Nightferry',key='g',fifths=-2,meter='4/4',bpm=52,
 description='A chordal night dance above a chromatically descending bass. Larch Footbridge’s D–C–D becomes the top line of close, softly changing chords. G–F-sharp–F–E–E-flat–D in the bass draws the opening inward; a warmer second phrase briefly visits D-flat before recovering G minor.',
 difficulty='Advanced chord melody, chromatic bass and controlled pedal gaps',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Every RH attack is a chord; bring out its highest note. In the recurring LH figure the bass note and middle dyad are separated by rests, and the final eighth-note pickup is unpedalled. The first six bass entries descend by semitone. Release both hands for the last two beats of bar 6.',
 parent_opus=158,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','C','D']),ancestry=dict(source_opus=158,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','C','D'],transposition_semitones=0),
 system_starts=[1,3,5,7,9,11,13],page_starts=[7],engraving=dict(spacing_system=14,pedal_offset_y=480),lower_sections={1:'pp',7:'p',10:'pp'},
 pedal_spans=[[i*4+a,i*4+b] for i in range(14) for a,b in ([(0,1.8)] if i==5 else [(0,3.8)] if i==13 else [(0,1.3),(2,2.8)])],
 rh='''
F4+Bb4+D5:1.5 Eb4+G4+C5:.5 F4+Bb4+D5:2
F4+A4+D5:3 E4+G4+C5:1
Eb4+G4+C5:2 D4+F4+Bb4:2
D4+G4+B4:3 E4+G4+C5:1
Eb4+G4+C5:3 D4+F4+Bb4:1
C4+F#4+A4:2 R:2
F4+Bb4+D5:1.5 G4+C5+Eb5:.5 F4+Bb4+D5:2
Eb4+G4+C5:3 D4+F4+Bb4:1
Db4+F4+Ab4:2 C4+Eb4+G4:2
D4+G4+Bb4:1.5 E4+A4+C5:.5 F4+Bb4+D5:2
Eb4+G4+C5:2 D4+F4+Bb4:2
C4+E4+A4:3 D4+F#4+A4:1
D4+G4+Bb4:2 D4+F4+A4:2
D4+F4+G4+Bb4:4
''',lh='''
G2:1.5 R:.5 D3+Bb3:1 R:.5 G2:.5
F#2:1.5 R:.5 D3+A3:1 R:.5 F#2:.5
F2:1.5 R:.5 C3+A3:1 R:.5 F2:.5
E2:1.5 R:.5 B2+G3:1 R:.5 E2:.5
Eb2:1.5 R:.5 Bb2+G3:1 R:.5 Eb2:.5
D2+A2:2 R:2
Bb2:1.5 R:.5 F3+D4:1 R:.5 Bb2:.5
Ab2:1.5 R:.5 Eb3+C4:1 R:.5 Ab2:.5
Db3:1.5 R:.5 Ab3:1 R:.5 Db3:.5
G2:1.5 R:.5 D3+Bb3:1 R:.5 G2:.5
Eb3:1.5 R:.5 Bb3:1 R:.5 Eb3:.5
A2:1.5 R:.5 E3+G3:1 R:.5 D3:.5
G2:1.5 R:.5 D3+A3:1 R:.5 G2:.5
G2+D3:4
''',sections={1:'p',7:'mp',10:'p',13:'pp'},words={1:'dolce',13:'poco rit.'},slurs=[(1,6),(7,9),(10,14)],lower_phrases=[],hairpins=[('crescendo',7,8),('diminuendo',11,13)],tempo_changes={},group=2,
 performance=dict(rubato=[52,52,51,50,49,43,53,52,48,52,50,47,39,27],phrase_arcs=[[0,24,4],[24,36,3],[36,56,2]],lower_entries=[],pedal_lift=.2,gate=.965,note='Keep the chord melody connected in intention while the bass steps through its silences. The chromatic descent should suggest a slow change of light, with the short unpedalled pickups drawing the dance onward.'))
,
dict(op=167,title='Clover Lamplight',key='Bb',fifths=-2,meter='2/4',bpm=54,
 description='A small major-key dance with a late-entering melody and borrowed minor shadows. Heather Afterimage’s C–D–E becomes F–G–A, rising towards B-flat above a dotted bass. E-flat minor and D-flat pass through the middle, but the final steps recover a plain, quiet B-flat major.',
 difficulty='Intermediate late melody entries and dotted bass transitions',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The melody waits an eighth before its first three notes, and again in bar 13. Keep the bass moving gently through those entrances. The shorter shared rests in bars 4, 8 and 12 separate the phrases. The last two bars leave the dotted figure for held harmony.',
 parent_opus=157,motif=dict(hand='rh',start_beat=.5,end_beat=2,pitches=['F','G','A']),ancestry=dict(source_opus=157,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['C','D','E'],transposition_semitones=5),
 system_starts=[1,5,9,13,16],page_starts=[],engraving=dict(spacing_system=12,pedal_offset_y=460),lower_sections={1:'pp',5:'p',13:'pp'},
 pedal_spans=[[i*2,i*2+(1.3 if i in [3,7,11] else 1.8)] for i in range(18)],
 rh='''
R:.5 F4:.5 G4:.5 A4:.5
Bb4:1.5 A4:.5
F4:.5 D4:.5 C4:1
D4:1.5 R:.5
F4:.5 A4:.5 C5:1
D5:1 C5:.5 Bb4:.5
Ab4:1 Gb4:1
F4:1.5 R:.5
G4:.5 Bb4:.5 D5:1
C5:1 A4:1
Ab4:1 F4:1
E4:1.5 R:.5
R:.5 F4:.5 G4:.5 A4:.5
Bb4:1 D5:1
C5:1 Bb4:.5 A4:.5
F4:1 D4:1
C4+F4+A4:2
D4+F4+Bb4:2
''',lh='''
Bb2:.75 F3:.25 D3:.5 F3:.5
A2:.75 E3:.25 C3:.5 E3:.5
G2:.75 D3:.25 Bb2:.5 D3:.5
Bb2+F3:1.5 R:.5
Eb3:.75 Bb3:.25 G3:.5 Bb3:.5
D3:.75 A3:.25 F3:.5 A3:.5
Eb3:.75 Bb3:.25 Gb3:.5 Bb3:.5
F3+C4:1.5 R:.5
G3:.75 D4:.25 Bb3:.5 D4:.5
F3:.75 C4:.25 A3:.5 A3:.5
Db3:.75 Ab3:.25 F3:.5 Ab3:.5
C3+G3:1.5 R:.5
Bb2:.75 F3:.25 D3:.5 D3:.5
G2:.75 D3:.25 Bb2:.5 D3:.5
Eb3:.75 Bb3:.25 G3:.5 Bb3:.5
F3:.75 C4:.25 A3:.5 F3:.5
Bb2+F3:2
Bb2+F3:2
''',sections={1:'p',5:'mp',8:'pp',9:'p',13:'p',17:'pp'},words={1:'dolce',16:'poco rit.'},slurs=[(1,4),(5,8),(9,12),(13,18)],lower_phrases=[],hairpins=[('crescendo',5,6),('diminuendo',15,17)],tempo_changes={},group=2,
 performance=dict(rubato=[54,55,52,46,55,56,51,44,54,53,50,43,54,55,52,46,38,28],phrase_arcs=[[0,8,3],[8,16,4],[16,24,3],[24,36,2]],lower_entries=[],pedal_lift=.2,gate=.975,note='Let the tune enter as if it has quietly joined a dance already underway. The borrowed minor colours should pass with tenderness, leaving a little shadow in the simple major ending.'))
,
dict(op=168,title='Hawthorn Crosswalk',key='c',fifths=-3,meter='2/4',bpm=55,
 meters=['2/4','2/4','3/4','2/4','2/4','3/4','2/4','3/4','2/4','2/4','3/4','2/4','2/4','3/4','2/4','3/4'],
 description='A small dance that occasionally takes an extra step. Willow Homeward’s A–C–D–C becomes G–B-flat–C–B-flat in C minor. Two-beat movement opens into three-beat hesitations: sometimes a breath, sometimes a longer continuation. The final added beat lets the music settle without hurrying its goodbye.',
 difficulty='Intermediate to advanced changing metre and flexible phrase length',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Keep the quarter-note pulse steady as 2/4 changes to 3/4. The extra beat is silent in bars 3, 6 and 11, but carries the phrase onward in bars 8 and 14. The shorter LH bars end with an eighth rest; keep those releases distinct from the longer shared breaths.',
 parent_opus=160,motif=dict(hand='rh',start_beat=0,end_beat=2,pitches=['G','Bb','C','Bb']),ancestry=dict(source_opus=160,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','C','D','C'],transposition_semitones=-2),
 system_starts=[1,4,7,10,13,15],page_starts=[10],engraving=dict(spacing_system=14,pedal_offset_y=470),lower_sections={1:'pp',7:'p',12:'pp'},
 pedal_spans=[[s,s+(1.8 if i in [2,5,10] else 2.8 if i in [7,13,15] else 1.3)] for i,s in enumerate([0,2,4,7,9,11,14,16,19,21,23,26,28,30,33,35])],
 rh='''
G4:.5 Bb4:.5 C5:.5 Bb4:.5
Eb5:1 D5:.5 C5:.5
Bb4:2 R:1
G4:.5 F4:.5 Eb4:1
F4:1 G4:1
C5:2 R:1
D5:.5 F5:.5 Eb5:1
D5:1 C5:2
Bb4:1 G4:1
Ab4:.5 C5:.5 Db5:1
C5:2 R:1
G4:.5 Bb4:.5 C5:.5 Bb4:.5
Eb5:1 D5:.5 C5:.5
Bb4:1 Ab4:1 G4:1
F4:.5 Eb4:.5 D4:1
Eb4+G4+C5:3
''',lh='''
C3:1 G3+Bb3:.5 R:.5
Ab2:1 Eb3+G3:.5 R:.5
Bb2+F3:2 R:1
Eb3:1 G3+Bb3:.5 R:.5
F3:1 Ab3+C4:.5 R:.5
C3+G3:2 R:1
Bb2:1 F3+A3:.5 R:.5
Ab2:1 Eb3+G3:2
G2:1 D3+Bb3:.5 R:.5
Db3:1 Ab3+C4:.5 R:.5
Ab2+Eb3:2 R:1
C3:1 G3+Bb3:.5 R:.5
Ab2:1 Eb3+G3:.5 R:.5
F3:1 Ab3+C4:2
G2:1 D3+B3:.5 R:.5
C3+G3:3
''',sections={1:'p',7:'mp',11:'pp',12:'p',15:'pp'},words={1:'dolce',15:'poco rit.'},slurs=[(1,3),(4,6),(7,11),(12,16)],lower_phrases=[],hairpins=[('crescendo',7,8),('diminuendo',13,15)],tempo_changes={},group=2,
 performance=dict(rubato=[55,56,48,55,55,47,57,56,54,51,45,55,54,50,42,28],phrase_arcs=[[0,7,3],[7,14,3],[14,26,4],[26,38,2]],lower_entries=[],pedal_lift=.2,gate=.975,note='Feel the changing bar lengths as extensions of a phrase. The quiet extra beats need room without becoming stops, and the last three-beat bar should finally let the step come to rest.'))
]
