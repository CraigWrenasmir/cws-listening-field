"""The sixth volume: deliberately authored piano studies, Op. 121–144."""

PIECES = [
dict(op=121,title='Tamarisk Window',key='c',fifths=-3,meter='4/4',bpm=52,
 description='Juniper Anchorage’s G–B-flat–A–G returns over C-minor harmony. Three quiet shimmers alternate pairs of inner notes beneath a held upper tone, first in eighths, then sixteenths, then thirty-seconds. E-flat, D-flat and A-flat Lydian colours briefly brighten the register before a compact C-minor ninth closes the piece.',
 difficulty='Advanced measured dyad tremolo beneath a held upper voice',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 5, 11 and 15, keep the upper note held while alternating the two written inner dyads. There are eight, sixteen and thirty-two dyad attacks respectively, each passage filling four quarter beats. The widest complete RH shape is ten semitones at the final chord; the first two shimmering passages span eight and the third nine. Keep the alternating fingers close to the keys and the inner voice quieter than the sustained tone. Follow the poco rit. in the final thirty-second-note passage, then release the high shape cleanly before placing the lower closing chord.',
 parent_opus=120,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['G','Bb','A','G']),
 ancestry=dict(source_opus=120,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['G','Bb','A','G'],transposition_semitones=0),
 hidden_voice_rests={'inner':[1,2,3,4,6,7,8,9,10,12,13,14]},
 voice_phrases=[dict(voice='inner',start_beat=16,end_beat=20,swell=-3),dict(voice='inner',start_beat=40,end_beat=44,swell=-3),dict(voice='inner',start_beat=56,end_beat=60,swell=-3)],
 lower_sections={1:'pp',9:'p',11:'pp',13:'p',15:'pp'},
 system_starts=[1,3,5,6,8,10,11,12,14,15,16],page_starts=[8,14],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.2] for bar,cuts in enumerate([[0,1,1.5,2.5,4],[0,1.5,2,4],[0,1,1.5,2.5,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,1.5,2,3,4],[0,1,1.5,2,2.5,4],[0,1,2,3,4],[0,1.5,2,3,4],[0,1,1.5,2,2.5,4],[0,1,2,3,4],[0,1,1.5,2.5,3,4],[0,1,1.5,2,2.5,4],[0,1,1.5,2,2.5,4],[0,1,2,3,4],[0,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
G5:1 Bb5:.5 A5:1 G5:1.5
F5:1.5 Eb5:.5 D5:2
C5:1 Eb5:.5 G5:1 F5:1.5
D5:1 F5:1 Ab5:1 G5:1
Eb5:4
D5:1 C5:1 Bb4:1 G4:1
F4:1 Ab4:.5 C5:1 Bb4:1.5
G4:1 Bb4:1 D5:1 C5:1
Eb5:1.5 Db5:.5 C5:1 Bb4:1
Ab4:1 C5:.5 Eb5:1 Db5:1.5
Db5:4
C5:1 Bb4:.5 Ab4:1 Gb4:1.5
F4:1 A4:.5 C5:1 E5:1.5
D5:1 F5:.5 A5:1 G5:1.5
D5:4
C5:4
''',
 rh_inner='''
R:4
R:4
R:4
R:4
G4+C5:.5 A4+D5:.5 G4+C5:.5 A4+D5:.5 G4+C5:.5 A4+D5:.5 G4+C5:.5 A4+D5:.5
R:4
R:4
R:4
R:4
R:4
F4+Bb4:.25 G4+C5:.25 F4+Bb4:.25 G4+C5:.25 F4+Bb4:.25 G4+C5:.25 F4+Bb4:.25 G4+C5:.25 F4+Bb4:.25 G4+C5:.25 F4+Bb4:.25 G4+C5:.25 F4+Bb4:.25 G4+C5:.25 F4+Bb4:.25 G4+C5:.25
R:4
R:4
R:4
F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125 F4+Bb4:.125 G4+C5:.125
D4+Eb4+G4+Bb4:4
''',
 lh='''
C3:1.5 G3:.5 Bb3:2
Ab2+Eb3:2 G3+C4:2
F3+C4:1.5 Eb3+Bb3:2.5
Bb2+F3:2 Ab3+D4:2
Eb3+Bb3:4
Ab3:1 G3:.5 F3:1.5 Eb3:1
Db3+Ab3:2 C4+F4:2
G2+D3:2 F3+B3:2
Ab2:1.5 Eb3:.5 Gb3:2
Db3+Ab3:2 C4+F4:2
Db3+Ab3:4
Gb3:1 Db4:.5 F4:1.5 Eb4:1
F3+C4:2 E3+Bb3:2
D3+A3:2 C4+F4:2
Ab3+Eb4:4
C3+G3:4
''',sections={1:'p',2:'pp',3:'p',4:'mp',5:'pp',6:'p',7:'pp',8:'p',9:'mp',10:'p',11:'pp',12:'p',13:'p',14:'mp',15:'pp',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16)],lower_phrases=[(1,2),(3,4),(6,7),(8,9),(10,11),(12,13),(14,15)],
 hairpins=[('crescendo',3,4),('crescendo',13,14)],tempo_changes={},group=2,
 performance=dict(rubato=[52,46,50,54,45,44,42,47,51,45,42,40,46,49,40,25],
  phrase_arcs=[[0,8,3],[8,16,3],[16,24,2],[24,32,2],[32,40,3],[40,48,2],[48,56,3],[56,64,-2]],
  inner_entries=[],lower_entries=[],pedal_lift=.2,gate=.995,
  note='The inner dyads should sound like a quiet measured shimmer. Keep their increasing speed separate from their loudness, letting each held upper note decay naturally above them. Ease the pace for the last thirty-second-note passage and allow the low closing shape to settle.'))

,
dict(op=122,title='Heather Backwater',key='F',fifths=-1,meter='12/8',bpm=54,
 description='Velvet Estuary’s five-note opening returns an octave higher. The LH tenor answers three quarter beats later, two octaves below the new upper line and with every duration doubled. It keeps unfolding beneath the upper continuation. A whole-tone-lower reflection and a final return carry the canon through softer jazz harmony into F-major ninth.',
 difficulty='Advanced augmentation canon between the upper voice and LH tenor',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The five-note subject begins in the RH at bars 1, 6 and 12. Each LH tenor answer enters three quarter beats later and uses twice the RH durations, taking twelve beats to complete the same contour two octaves lower. The middle pair is a whole tone lower. Preserve the held bass notes beneath the tenor, especially the six-beat bass at each subject opening. Separate staff dynamics bring the slower answer forward after the upper subject has passed. Let the connecting phrases breathe without hurrying the answer.',
 parent_opus=2,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4.5,pitches=['A','C','D','C']),
 ancestry=dict(source_opus=2,source_hand='rh',source_start_beat=0,source_end_beat=4.5,source_pitches=['A','C','D','C'],transposition_semitones=0),
 hidden_voice_rests={'tenor':[4,5,9,10,11,15,16]},
 voice_phrases=[dict(voice='tenor',start_beat=3,end_beat=15,swell=3),dict(voice='tenor',start_beat=33,end_beat=45,swell=3),dict(voice='tenor',start_beat=69,end_beat=81,swell=2)],
 lower_sections={1:'pp',2:'p',3:'pp',4:'pp',6:'pp',7:'p',8:'pp',9:'p',11:'pp',12:'pp',13:'p',14:'pp',15:'pp'},
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=600),
 pedal_spans=[[(bar-1)*6+left,(bar-1)*6+right-.2] for bar,cuts in enumerate([[0,1.5,3,4,4.5,6],[0,2,3,4,5,6],[0,1.5,2,3,4,6],[0,1.5,2,3,6],[0,1,1.5,2,2.5,4,6],[0,1.5,3,4,4.5,6],[0,2,3,4,5,6],[0,1.5,2,3,4,6],[0,1.5,2,3,6],[0,1,1.5,2.5,3,4,6],[0,2,3,4,6],[0,1.5,3,4,4.5,6],[0,2,3,4,5,6],[0,1.5,2,3,6],[0,1,1.5,2,2.5,4,6],[0,6]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
A5:1.5 C6:1.5 D6:1 C6:.5 A5:1.5
G5:2 A5:1 C6:1 E6:2
D6:1.5 C6:.5 G5:2 F5:2
Ab5:1.5 G5:.5 F5:1 Eb5:3
D5:1 F5:.5 Ab5:1 G5:1.5 E5:2
G5:1.5 Bb5:1.5 C6:1 Bb5:.5 G5:1.5
F5:2 G5:1 Bb5:1 D6:2
C6:1.5 Bb5:.5 F5:2 Eb5:2
Db5:1.5 F5:.5 Ab5:1 C6:3
Bb5:1 Ab5:.5 Gb5:1 F5:1.5 Eb5:2
D5:2 F5:1 A5:1 G5:2
A5:1.5 C6:1.5 D6:1 C6:.5 A5:1.5
G5:2 E5:1 C5:1 D5:2
F5:1.5 E5:.5 D5:1 C5:3
Bb4:1 D5:.5 F5:1 E5:1.5 G5:2
F4+G4+A4+C5+E5:6
''',
 lh='''
D3:6
F3:3 G3:3
Bb2:3 A2:3
Db3+Ab3:3 C4+F4:3
G2:1.5 D3:.5 F3:1 B3:3
C3:6
Eb3:3 F3:3
Ab2:3 G2:3
Gb3+Db4:3 F3+C4:3
Eb3+Bb3:3 Db4+Gb4:3
E3+B3:2 D3+A3:2 C3+G3:2
D3:6
F3:3 G3:3
Bb2:3 A2:3
C3:1.5 G3:.5 Bb3:1 E4:3
F3+C4:6
''',
 lh_upper='''
R:3 A3:3
C4:3 D4:2 C4:1
A3:3 R:3
R:6
R:6
R:3 G3:3
Bb3:3 C4:2 Bb3:1
G3:3 R:3
R:6
R:6
R:6
R:3 A3:3
C4:3 D4:2 C4:1
A3:3 R:3
R:6
R:6
''',sections={1:'p',2:'pp',3:'p',4:'pp',5:'mp',6:'p',7:'pp',8:'p',9:'mp',10:'p',11:'pp',12:'p',13:'pp',14:'p',15:'pp',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,3),(4,5),(6,8),(9,11),(12,14),(15,16)],lower_phrases=[(1,3),(4,5),(6,8),(9,10),(11,12),(13,14),(15,16)],
 hairpins=[('crescendo',4,5),('diminuendo',9,11),('diminuendo',15,16)],tempo_changes={},group=2,
 performance=dict(rubato=[54,50,47,45,51,52,48,45,50,46,43,49,44,41,34,26],
  phrase_arcs=[[0,18,3],[18,30,2],[30,48,3],[48,66,3],[66,84,2],[84,96,-2]],
  tenor_entries=[[3,15],[33,45],[69,81]],lower_entries=[],pedal_lift=.2,gate=.995,
  note='Let the upper opening retain the gentle sway of Velvet Estuary. The slower tenor answer should be heard as a second voice with its own breathing, continuing calmly beneath the next upper phrase. Keep the long bass notes quiet and let the final return feel more distant before the warm major ninth.'))

,
dict(op=123,title='Thistle Isopleth',key='d',fifths=-1,meter='3/4',bpm=51,
 description='Heather Backwater’s A–C–D–C becomes G–B-flat–C–B-flat. A held upper F remains in place while nine quiet major triads rise chromatically beneath it, changing its harmonic meaning before resolving into D-minor ninth. A second passage, a whole tone lower, settles into C-minor ninth; a brief altered-dominant return restores D minor.',
 difficulty='Advanced chromatic chord planing beneath a held upper note',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Hold the upper F through bars 5–7 while the inner dyads and LH roots form nine major triads rising by semitone, from D-flat to A. The upper note changes from a chord tone to different tensions as the harmony moves. Bars 11–13 repeat the process one whole tone lower beneath a held E-flat, moving from C-flat to G. Keep each inner dyad quiet and connected while the RH maintains its upper hold; the first complete RH shape spans an octave. Clear the pedal at the written changes so the chromatic harmony does not accumulate.',
 parent_opus=122,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=3,pitches=['G','Bb','C','Bb']),
 ancestry=dict(source_opus=122,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4.5,source_pitches=['A','C','D','C'],transposition_semitones=-2),
 hidden_voice_rests={'inner':[1,2,3,4,9,10,15]},
 voice_phrases=[dict(voice='inner',start_beat=12,end_beat=21,swell=-2),dict(voice='inner',start_beat=30,end_beat=39,swell=-2)],
 lower_sections={1:'pp',5:'pp',9:'p',11:'pp',15:'pp'},
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=500),
 pedal_spans=[[(bar-1)*3+left,(bar-1)*3+right-.2] for bar,cuts in enumerate([[0,1,1.5,2.5,3],[0,1,1.5,2.5,3],[0,1,1.5,2.5,3],[0,1,1.5,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,3],[0,1,1.5,2.5,3],[0,1,1.5,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,3],[0,1,1.5,2,3],[0,3]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
G5:1 Bb5:.5 C6:1 Bb5:.5
A5:1 G5:.5 F5:1 E5:.5
D5:1 F5:.5 A5:1 G5:.5
F5:1 Eb5:1 D5:1
F5:3~
F5:3~
F5:3
D5:3
Eb5:1 G5:.5 Bb5:1 Ab5:.5
G5:1 F5:1 Eb5:1
Eb5:3~
Eb5:3~
Eb5:3
C5:3
Eb5:1 D5:.5 C#5:.5 Bb4:1
D5:3
''',
 rh_inner='''
R:3
R:3
R:3
R:3
F4+Ab4:1 F#4+A4:1 G4+Bb4:1
G#4+B4:1 A4+C5:1 A#4+C#5:1
B4+D5:1 C5+Eb5:1 C#5+E5:1
E4+F4+A4+C5:3
R:3
R:3
Eb4+Gb4:1 E4+G4:1 F4+Ab4:1
F#4+A4:1 G4+Bb4:1 G#4+B4:1
A4+C5:1 Bb4+Db5:1 B4+D5:1
D4+Eb4+G4+Bb4:3
R:3
E4+F4+A4+C5:3
''',
 lh='''
D3+A3:1.5 C4+F4:1.5
Bb2+F3:1.5 A3+D4:1.5
G3+D4:1.5 F3+C4:1.5
Eb3+Bb3:1.5 D3+A3:1.5
Db3:1 D3:1 Eb3:1
E3:1 F3:1 F#3:1
G3:1 Ab3:1 A3:1
D3+A3:3
C3+G3:1.5 Bb3+Eb4:1.5
Ab2+Eb3:1.5 G3+C4:1.5
Cb3:1 C3:1 Db3:1
D3:1 Eb3:1 E3:1
F3:1 Gb3:1 G3:1
C3+G3:3
A2+E3:1.5 G3+C#4:1.5
D3+A3:3
''',sections={1:'p',2:'pp',3:'mp',4:'p',5:'pp',8:'pp',9:'p',10:'pp',11:'pp',14:'pp',15:'p',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,2),(3,4),(5,8),(9,10),(11,14),(15,16)],lower_phrases=[(1,2),(3,4),(5,8),(9,10),(11,14),(15,16)],
 hairpins=[('crescendo',1,3),('diminuendo',15,16)],tempo_changes={},group=2,
 performance=dict(rubato=[51,46,52,45,47,49,44,35,48,43,45,47,41,33,32,24],
  phrase_arcs=[[0,6,3],[6,12,3],[12,24,-2],[24,30,2],[30,42,-2],[42,48,-2]],
  inner_entries=[],lower_entries=[],pedal_lift=.2,gate=.995,
  note='Let the upper hold stay as a quiet point of reference while the lower harmony changes around it. The chromatic chords should remain light enough for their tensions to pass without weight. Allow more time at both minor-ninth resolutions and let the last D minor feel settled.'))
,
dict(op=124,title='Clover Nightwalk',key='d',fifths=-1,meter='12/8',bpm=66,
 description='Velvet Estuary’s A–C–D–C returns above a circling left-hand minor-ninth arpeggio. Written quarter–eighth pairs give the accompaniment a quiet triplet swing. The melody leaves space around that pulse, then travels through B-flat, G minor and D-flat before the original figure returns more softly.',
 difficulty='Intermediate to advanced independent melody over a lilting ostinato',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=10),
 technical_note='The left hand alternates one-quarter and one-eighth durations throughout the moving bars: a written 2:1 lilt within each dotted-quarter pulse. Keep the eighth-note arrivals light. Bars 1–3 repeat the same eight-note D-minor figure exactly; the right hand changes its phrase length above it. Let the final two bars lengthen naturally rather than adding another loop.',
 parent_opus=2,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','C','D','C']),
 ancestry=dict(source_opus=2,source_hand='rh',source_start_beat=0,source_end_beat=4.5,source_pitches=['A','C','D','C'],transposition_semitones=0),
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 lower_sections={1:'pp',5:'p',8:'pp',11:'p',13:'pp'},
 pedal_spans=[[(bar-1)*6+start,(bar-1)*6+start+2.8] for bar in range(1,16) for start in [0,3]]+[[90,95.7]],
 rh='''
A4:1 C5:.5 D5:1 C5:.5 A4:3
R:1 G4:.5 A4:1 E5:.5 D5:3~
D5:1.5 C5:1 A4:.5 G4:1 E4:2
F4:1 A4:.5 C5:1 D5:.5 F5:3
E5:1.5 D5:1 C5:.5 A4:3
Bb4:1 D5:.5 F5:1 A5:.5 G5:3~
G5:1 F5:.5 D5:1 C5:.5 Bb4:3
Ab4:1 C5:.5 Eb5:1 F5:.5 Ab5:3
G5:1.5 F5:1 Eb5:.5 C5:3
E5:1 G5:.5 Bb5:1 A5:.5 G5:1 E5:2
F5:1.5 E5:1 D5:.5 C#5:3
A4:1 C5:.5 D5:1 C5:.5 A4:3
R:1 F5:.5 E5:1 D5:.5 C5:3~
C5:1 A4:.5 G4:1 E4:.5 F4:3
E4:1.5 G4:1 C#5:.5 D5:3
E4+F4+A4+C5:6
''',
 lh='''
D3:1 F3:.5 A3:1 C4:.5 A3:1 F3:.5 E3:1 A3:.5
D3:1 F3:.5 A3:1 C4:.5 A3:1 F3:.5 E3:1 A3:.5
D3:1 F3:.5 A3:1 C4:.5 A3:1 F3:.5 E3:1 A3:.5
Bb3:1 D3:.5 F3:1 A3:.5 F3:1 D3:.5 C3:1 F3:.5
F3:1 A3:.5 C4:1 E4:.5 C4:1 A3:.5 G3:1 C4:.5
G3:1 Bb3:.5 D4:1 F4:.5 D4:1 Bb3:.5 A3:1 D3:.5
C3:1 E3:.5 G3:1 Bb3:.5 G3:1 E3:.5 D3:1 G3:.5
Db3:1 F3:.5 Ab3:1 C4:.5 Ab3:1 F3:.5 Eb3:1 Ab3:.5
Eb3:1 G3:.5 Bb3:1 D4:.5 Bb3:1 G3:.5 F3:1 Bb3:.5
C3:1 E3:.5 G3:1 Bb3:.5 G3:1 E3:.5 D3:1 G3:.5
A2:1 C#3:.5 E3:1 G3:.5 E3:1 C#3:.5 B2:1 E3:.5
D3:1 F3:.5 A3:1 C4:.5 A3:1 F3:.5 E3:1 A3:.5
D3:1 F3:.5 A3:1 C4:.5 A3:1 F3:.5 E3:1 A3:.5
Bb3:1 D3:.5 F3:1 A3:.5 F3:1 D3:.5 C3:1 F3:.5
A2:1.5 E3:1.5 G3+C#4:3
D3+A3:6
''',sections={1:'p',4:'p',6:'mp',8:'p',11:'mp',12:'p',14:'pp'},words={1:'dolce',15:'poco rit.'},
 slurs=[(1,3),(4,5),(6,7),(8,9),(10,11),(12,14),(15,16)],lower_phrases=[(1,3),(4,5),(6,7),(8,9),(10,11),(12,14),(15,16)],
 hairpins=[('crescendo',4,6),('diminuendo',12,14)],tempo_changes={},group=2,
 performance=dict(rubato=[66,66,64,66,65,68,66,64,65,67,64,65,64,62,52,36],phrase_arcs=[[0,18,2],[18,30,2],[30,42,3],[42,54,2],[54,66,3],[66,84,1],[84,96,-2]],lower_entries=[],pedal_lift=.2,gate=.985,note='The score itself carries the long-short swing. Keep a mostly steady dotted-quarter pulse until the coda, with restrained phrase swells and a quiet rolling left hand.'))
,
dict(op=125,title='Fen Turnstile',key='F',fifths=-1,meter='15/8',bpm=72,
 description='A three-note left-hand cell takes five eighths to turn, crossing the five dotted-quarter pulses of each bar. Its long–short–long gait moves through F-major, B-flat Lydian and borrowed A-flat colours. Clover Nightwalk’s opening thought floats across those unevenly placed returns before the loop slowly opens into a major ninth.',
 difficulty='Advanced independence between a five-eighth ostinato and compound metre',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=10),
 technical_note='Each left-hand cell lasts five eighths: quarter, eighth, quarter. Three cells occupy a bar of 15/8, while the right hand often suggests dotted-quarter pulses. Do not accent every LH restart. Bars 1–2 retain exactly the same nine attacks; the coda lengthens the cell and finally releases it.',
 parent_opus=124,motif=dict(hand='rh',start_beat=0,end_beat=4.5,pitches=['A','C','D','C']),
 ancestry=dict(source_opus=124,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','C','D','C'],transposition_semitones=0),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=13,pedal_offset_y=440),lower_sections={1:'pp',5:'p',7:'pp',10:'pp'},
 pedal_spans=[[(bar-1)*7.5+start,(bar-1)*7.5+start+2.3] for bar in range(1,11) for start in [0,2.5,5]]+[[75,78.5],[78.75,82.2],[82.5,89.7]],
 rh='''
A4:1 C5:.5 D5:1 C5:2 G4:3
R:1.5 E5:3 D5:1.5 C5:1.5
A4:1.5 C5:1.5 E5:1.5 F5:3
D5:2 C5:.5 A4:1.5 G4:3.5
Bb4:1 Db5:.5 Eb5:1 Db5:2 Ab4:3
G4:1.5 Bb4:1.5 D5:1.5 F5:3
E5:3 D5:1 C5:.5 A4:3
G4:2 A4:.5 C5:1.5 E5:3.5
F5:1.5 E5:1.5 D5:1.5 B4:3
A4:1 C5:.5 D5:1 C5:2 G4:3
Bb4:1.5 A4:1 G4:.5 E4:1.5 G4:3
F4+G4+A4+C5+E5:7.5
''',
 lh='''
F3:1 A3:.5 E3:1 F3:1 A3:.5 E3:1 F3:1 A3:.5 E3:1
F3:1 A3:.5 E3:1 F3:1 A3:.5 E3:1 F3:1 A3:.5 E3:1
Bb3:1 D4:.5 A3:1 Bb3:1 D4:.5 A3:1 Bb3:1 D4:.5 A3:1
G3:1 Bb3:.5 F3:1 G3:1 Bb3:.5 F3:1 G3:1 Bb3:.5 F3:1
Ab3:1 C4:.5 G3:1 Ab3:1 C4:.5 G3:1 Ab3:1 C4:.5 G3:1
Eb3:1 G3:.5 D3:1 Eb3:1 G3:.5 D3:1 Eb3:1 G3:.5 D3:1
F3:1 A3:.5 E3:1 F3:1 A3:.5 E3:1 F3:1 A3:.5 E3:1
A3:1 C4:.5 G3:1 A3:1 C4:.5 G3:1 A3:1 C4:.5 G3:1
G3:1 B3:.5 F3:1 G3:1 B3:.5 F3:1 G3:1 B3:.5 F3:1
F3:1 A3:.5 E3:1 F3:1 A3:.5 E3:1 F3:1 A3:.5 E3:1
C3:1.5 E3:1 Bb3:.5 D4:1.5 G3:3
F3+C4:7.5
''',sections={1:'p',3:'p',5:'mp',7:'p',9:'mp',10:'p',11:'pp'},words={1:'dolce',11:'poco rit.'},
 slurs=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)],lower_phrases=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)],hairpins=[('crescendo',3,5),('diminuendo',9,11)],tempo_changes={},group=2,
 performance=dict(rubato=[72,72,73,71,72,71,72,71,73,70,58,42],phrase_arcs=[[0,15,2],[15,30,2],[30,45,3],[45,60,1],[60,75,2],[75,90,-2]],lower_entries=[],pedal_lift=.2,gate=.985,note='Keep the left-hand cell even in character but not equal in duration: the short middle note gives a small sideways lilt. The melody should float independently over the cell boundaries.'))
]
