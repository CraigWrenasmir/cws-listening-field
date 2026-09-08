"""Individually specified studies in Craig's revised, freer musical direction.

Each row is a bar; durations use quarter-note units. A trailing ~ sustains a
pitch/chord into the next matching event without another sounded onset.
"""
DREAM_PIECES=[
dict(op=7,title='Silt Reverie',key='d',fifths=-1,meter='9/8',bpm=63,
 description='A slow nine-beat estuary: the D-F-E-A ancestor opens into asymmetrical three-, four- and five-bar breaths. Suspensions cross the bar line while spacious left-hand shells move through D minor, B-flat major, G minor and a brief D-flat-major reflection. An unhurried D-minor added-ninth close keeps the light warm.',
 parent_opus=2,motif=dict(hand='rh',start_beat=0,end_beat=4.5,pitches=['D','F','E','A']),
 rh='''
D5:1.5 F5:.5 E5:1 A4:1.5
C5:1.5 A4:1 G4:.5 E4:1.5
D5:2 F5:1 E5:1.5~
E5:1 D5:.5 A4:1.5 G4:1 R:.5
A4:1.5 C5:1 E5:1.5 D5:.5
G5:1 F5:.5 E5:1 D5:.5 Bb4:1 R:.5
A4:2 E5:.5 D5:2~
D5:1.5 C5:1 A4:1 R:1
Bb4:1.5 D5:.5 F5:1 A5:1.5
Ab5:1.5 F5:1 Eb5:.5 C5:1.5
E5:1 D5:.5 Bb4:1 A4:.5 G4:1 R:.5
A4+C5:3 E5:.5 D5:1
D5:1.5 F5:.5 E5:1 A4:1.5
C5:2 A4:1 E4:1 R:.5
D5:1.5 E5:.5 D5:1 Bb4:1.5
A4:1.5 G4:1 E4:.5 C#4:1 R:.5
F4:2 E4:.5 D4:1 A4:1~
A4:1.5 E4+A4:3
''',
 lh='''
D3:1.5 F3+A3:2 R:1
Bb2:1 F3+A3:2 D3:1 R:.5
G3:1.5 Bb3+D4:1.5 A3:1.5
C3:2 E3+Bb3:1.5 R:1
F3:1 A3+C4:2 G3:1.5
E3+Bb3:1.5 A2:1 G3+C#4:2
D3:2 F3+A3:1 C3:1.5
Bb2:1.5 F3+A3:2 R:1
G3:1 Bb3+D4:2 F3:1.5
Db3:1.5 F3+Ab3:2 R:1
C3:1.5 E3+Bb3:1.5 D4:1.5
F3:2 A3+C4:1.5 R:1
D3:1.5 F3+A3:2 R:1
Bb2:2 D3+A3:1.5 R:1
G3:1.5 Bb3+D4:1.5 E3:1.5
A2:1.5 G3+C#4:2 R:1
D3:2 A3:1 F3:1.5
D3+F3:3~ D3+F3:1.5
''',
 sections={1:'p',5:'p',9:'mp',12:'p',15:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,3),(4,7),(8,12),(13,16),(17,18)],lower_phrases=[(3,4),(9,11),(15,18)],
 hairpins=[('crescendo',5,6),('diminuendo',6,8),('crescendo',9,10),('diminuendo',10,12),('diminuendo',15,18)],
 tempo_changes={},group=3,
 performance=dict(rubato=[63,62,58,60,64,65,61,56,63,59,60,55,60,58,56,53,49,42],
  phrase_arcs=[[0,12.5,3],[13.5,33,4],[36,52,5],[54,70,3],[72,81,-2]],
  lower_entries=[[9,18],[36,49.5],[63,76.5]],pedal_bars=list(range(1,19)),pedal_lift=.18,gate=.99,
  note='Continuous half-quarter tempo changes interpolate the authored bar starts; a small anticipatory pedal lift clears each harmony. No random onset jitter.')),
dict(op=8,title='Bracken Meridian',key='F',fifths=-1,meter='4/4',bpm=56,
 description='An unhurried F-major ballad whose melody enters after the downbeat and repeatedly outlasts the harmony underneath. The D-F-E-A ancestor arrives quietly in the left hand at bar 9. A borrowed E-flat-major colour and an E-half-diminished to A-dominant turn shade the centre before a soft added-ninth return to F.',
 parent_opus=7,motif=dict(hand='lh',start_beat=32,end_beat=36,pitches=['D','F','E','A']),
 rh='''
R:.5 E5:1.5 G5:.5 A5:.5 G5:1
F5:1.5 E5:.5 C5:2~
C5:1 D5:.5 F5:1.5 E5:1
D5:1.5 Bb4:.5 A4:1 R:1
R:.5 G4:.5 A4:1 C5:1 E5:1~
E5:1 F5:.5 D5:1.5 Bb4:1
F5:2 D5:.5 C5:.5 Bb4:1
A4:2 G4:.5 E4:.5 R:1
A4+C5:2 E5:1 D5:1~
D5:1 C5:.5 A4:1.5 R:1
G4:1 Bb4:.5 D5:.5 G5:2
F5:1 E5:.5 C#5:.5 Bb4:1 A4:1~
A4:1 C5:.5 D5:.5 F5:1 E5:1
D5:2 C5:.5 A4:.5 G4:1~
G4:1 A4:.5 C5:1.5 E5:1
F5:2 E5:.5 C5:.5 A4:1~
A4:1 G4:1 E4:1 D4:1
E4+G4:1.5 F4+A4:2.5
''',
 lh='''
F3:1 A3+C4:2 R:1
D3:1.5 F3+A3:1.5 E3:1
Bb2:1.5 D3+A3:1.5 F3:1
C3:1 E3+Bb3:2 R:1
F3:2 A3+C4:1 R:1
G3:1 Bb3+D4:2 F3:1
Eb3:1.5 G3+Bb3:1.5 R:1
C3:1 E3+Bb3:1.5 G3:1.5
D3:.5 F3:.5 E3:1 A3:2
Bb2:2 D3+A3:1 F3:1
E3+Bb3:2 G3:1 D3:1
A2:1 G3+C#4:2 R:1
D3:1.5 F3+A3:1.5 R:1
Bb2:2 D3+A3:1.5 R:.5
C3:1 E3+Bb3:2 G3:1
F3:1 A3+C4:2 R:1
G3:1 Bb3+D4:1 C3:2
F3+A3:4
''',sections={1:'p',5:'pp',9:'p',11:'mp',14:'p',17:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,3),(4,8),(9,11),(12,16),(17,18)],lower_phrases=[(2,4),(9,10),(14,18)],
 hairpins=[('diminuendo',2,4),('crescendo',5,7),('diminuendo',7,8),('crescendo',9,11),('diminuendo',12,14),('diminuendo',16,18)],
 tempo_changes={},group=3,
 performance=dict(rubato=[56,55,52,50,55,57,54,49,54,53,57,55,54,51,53,50,47,42],
  phrase_arcs=[[.5,11,3],[12,31,4],[32,43,4],[44,63,3],[64,72,-2]],
  lower_entries=[[32,40],[64,70]],pedal_bars=list(range(1,19)),pedal_lift=.22,gate=.99,
  note='The melody begins after the first bass attack; explicitly tied suspensions carry through changing harmony. A broad tempo arch is authored for each phrase.')),
dict(op=9,title='Lichen Aperture',key='a',fifths=0,meter='3/4',bpm=54,
 description='The shared thought becomes A-C-B-E, slipping over the first bar line into a small A-minor nocturne. Unequal phrases and suspended upper notes soften the triple metre. F-major sevenths surround a brief Dorian opening towards D and G major; the final added ninth remains luminous above A minor.',
 parent_opus=8,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','C','B','E']),
 rh='''
A4:1.5 C5:.5 B4:.5 E5:.5~
E5:1 D5:.5 C5:.5 A4:1
G4:2 B4:.5 D5:.5~
D5:1 E5:.5 G5:.5 F5:1
E5:1.5 C5:.5 B4:1~
B4:.5 A4:1.5 R:1
A4+C5:1.5 E5:.5 D5:1
F5:1 E5:.5 D5:.5 C5:1~
C5:.5 B4:.5 G4:1 R:1
A4:1 C5:.5 E5:1 D5:.5
F#5:1.5 E5:.5 C5:1
B4:1.5 A4:.5 G4:.5 R:.5
C5:1 E5:1 D5:1
B4:1 D5:.5 C5:.5 A4:1~
A4:1.5 C5:.5 B4:.5 E5:.5
D5:1 C5:.5 A4:1 R:.5
G4:1.5 B4:.5 D5:1~
D5:.5 C5:.5 A4:1 G4:1
F4:1 E4:.5 D4:.5 G#4:1
A4:1 B4+E5:2
''',
 lh='''
A2+E3:3
F3:1 A3+C4:1.5 R:.5
C3:1 E3+B3:2
D3:1 F3+A3:2
E3:1 G#3+D4:1.5 R:.5
A2:1 E3+G3:2
F3:1 A3+C4:1 E3:1
D3:1 F3+A3:2
G2:1 F3+B3:1.5 R:.5
C3:1 E3+B3:2
D3:1 F#3+C4:2
G3:1 B3+D4:1.5 R:.5
F3:1 A3+C4:2
E3:1 G#3+D4:1.5 R:.5
A2:1 E3+G3:2
F3:1 A3+C4:1.5 R:.5
G3:1 F3+B3:1 R:1
C3:1 E3+B3:1.5 R:.5
D3:1 F3+A3:1 E3:1
A3+C4:3
''',sections={1:'p',7:'p',10:'mp',13:'p',17:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,4),(5,6),(7,9),(10,14),(15,18),(19,20)],lower_phrases=[(1,3),(7,10),(15,17)],
 hairpins=[('crescendo',3,4),('diminuendo',5,6),('crescendo',7,8),('diminuendo',8,9),('crescendo',10,11),('diminuendo',12,14),('diminuendo',17,20)],
 tempo_changes={},group=4,
 performance=dict(rubato=[54,53,55,51,50,47,53,54,49,55,57,53,52,48,52,50,48,47,44,39],
  phrase_arcs=[[0,11,3],[12,18,-2],[18,26,3],[27,41,4],[42,53,3],[54,60,-2]],
  lower_entries=[[0,9],[18,24]],pedal_bars=list(range(1,21)),pedal_lift=.2,gate=.99,
  note='The triple pulse is softened by ties and phrase lengths of four, two, three, five, four and two bars. The Dorian colour receives a small forward motion, then recedes.')),
dict(op=10,title='Reed Parallax',key='g',fifths=-2,meter='6/8',bpm=60,
 description='A G-minor reverie descended from Bracken Meridian\'s opening E-G-A-G, moved down a tone to D-F-G-F. The lower voice sometimes waits, sometimes continues through the next harmony, so the two hands do not repeatedly begin together. E-flat Lydian light and soft dominant colours return to a plain G-minor close.',
 parent_opus=8,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['D','F','G','F']),
 ancestry=dict(source_opus=8,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['E','G','A','G'],transposition_semitones=-2),
 rh='''
R:.5 D5:1 F5:.5 G5:.5 F5:.5
Eb5:1.5 D5:.5 Bb4:1~
Bb4:1 C5:.5 D5:1 R:.5
Eb5:1 F5:.5 G5:1 F5:.5~
F5:.5 Eb5:.5 C5:1 A4:.5 R:.5
Bb4:1 A4:.5 F#4:.5 A4:1~
A4:1 D5:.5 G5:.5 F5:1
D5:2 R:1
C5:.5 D5:1 F5:.5 A5:1
G5:1 F5:.5 Eb5:.5 C5:1~
C5:1 D5:.5 F5:1 E5:.5
Eb5:1.5 C5:.5 A4:1
F#4:.5 A4:.5 C5:1 Bb4:.5 R:.5
G4:1.5 Bb4:.5 A4:1~
A4:1 G4:.5 E4:.5 Bb4:1~
Bb4:1 A4:.5 F4:1 R:.5
G4:1 Bb4:.5 D5:.5 C5:1~
C5:.5 Bb4:.5 A4:.5 G4:1.5
''',
 lh='''
G3:1.5 Bb3+D4:1 R:.5
R:.5 Eb3:2 Bb3:.5~
Bb3:1 D4:1 A3:1
C3:2 Eb3+Bb3:1~
Eb3+Bb3:.5 A3:.5 C4:1 Eb3:1
D3:1.5 F#3+C4:1.5
R:1 G3:1 D4:1~
D4:1 Bb3:.5 A3:.5 F3:1
Eb3+G3:2 Bb3:1
R:.5 F3:1 A3+Eb4:1.5
Bb3:2 D4:.5 R:.5
A3:1 C4+Eb4:1 G3:1
R:.5 D3:.5 F#3+C4:1.5 R:.5
G3+Bb3:2 D4:1~
D4:.5 C4:.5 Bb3:1 E3:1
F3:1.5 A3+C4:1 R:.5
D3:1 F#3+C4:1.5 R:.5
G3+Bb3:3
''',sections={1:'pp',5:'p',9:'mp',13:'p',16:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,3),(4,8),(9,12),(13,16),(17,18)],lower_phrases=[(2,5),(7,9),(10,12),(14,18)],
 hairpins=[('crescendo',4,6),('diminuendo',6,8),('crescendo',9,10),('diminuendo',11,12),('diminuendo',14,18)],tempo_changes={},group=3,
 performance=dict(rubato=[60,57,54,58,59,56,54,50,60,59,56,51,55,53,54,50,46,40],
  phrase_arcs=[[.5,8.5,3],[9,23,4],[24,35,5],[36,47,2],[48,54,-2]],
  lower_entries=[[3,15],[18,27],[39,45]],pedal_bars=list(range(1,19)),pedal_lift=.18,gate=.99,
  note='Four left-hand ties and several delayed bass entries let the accompaniment breathe independently. Phrase tempo changes follow the authored harmonic motion.')),
dict(op=11,title='Fen Lantern',key='Eb',fifths=-3,meter='12/8',bpm=66,
 description='Wide twelve-eight breaths open an E-flat-major landscape. Reed Parallax\'s D-F-G-F becomes G-B-flat-C-B-flat, then stretches into a different melody. The middle darkens briefly through G dominant and C minor before F ninths and B-flat thirteenths return it to E-flat. The bass leaves whole pulses empty and answers in shorter arcs.',
 parent_opus=10,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['G','Bb','C','Bb']),
 ancestry=dict(source_opus=10,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['D','F','G','F'],transposition_semitones=-7),
 rh='''
G4:1.5 Bb4:.5 C5:.5 Bb4:1.5 D5:1 Eb5:1~
Eb5:1.5 D5:.5 C5:1 G4:2 R:1
C5:2 Eb5:1 G5:1 F5:1 D5:1~
D5:1 C5:1 Ab4:1.5 G4:.5 F4:1 R:1
G4:1 Bb4:.5 C5:.5 D5:1 F5:1.5 Eb5:.5 C5:1
Bb4:1.5 G4:.5 F4:1 Eb4:2 R:1
D5:1 F5:.5 Ab5:.5 G5:1 F5:1 B4:1 D5:1
Eb5:2 D5:.5 C5:.5 G4:1 Bb4:1 R:1
A4:1.5 C5:.5 Eb5:1 D5:1 C5:1 G4:1~
G4:1 Bb4:1 D5:.5 F5:1.5 Eb5:1 C5:1
Bb4:1.5 G4:.5 F4:1 G4:1 Bb4:1 D5:1~
D5:1 Eb5:1 C5:1.5 Bb4:.5 G4:1 R:1
Ab4:1 G4:.5 F4:.5 D4:1 F4:1 C5:1 Bb4:1~
Bb4:1 G4:1 F4:1 Eb4+G4:3
''',
 lh='''
Eb3:3 G3+Bb3:1.5 R:1.5
R:1 C3:1.5 Eb3+Bb3:2.5 G3:1
Ab2:1.5 Eb3+G3:2 C4:1.5 R:1
F3:2 Ab3+C4:1.5 Eb3:1 R:1.5
Bb2:1 D3+Ab3:2 F3:1 C4:1 R:1
Eb3:3 Bb3:1 G3:1 R:1
G3+B3:1 F3:1 Ab3:1 D4:1 F3:1 R:1
C3:1.5 G3+Bb3:2.5 Eb3:1 R:1
F3:1 A3+Eb4:2 C4:1 A3:1 R:1
Bb2:2 D3+Ab3:1.5 F3:1.5 R:1
Eb3:2 G3+Bb3:1.5 F3:.5 D3:1 Bb2:1
Ab2:2 Eb3+G3:1.5 C3:1 R:1.5
Bb2:2 D3+Ab3:2 C3:1 R:1
Eb3:1.5 Bb3:1.5 Eb3+G3:3
''',sections={1:'p',4:'pp',7:'mp',9:'p',12:'pp'},words={1:'poco rubato',13:'poco rit.'},
 slurs=[(1,2),(3,5),(6,8),(9,12),(13,14)],lower_phrases=[(2,4),(6,8),(10,12)],
 hairpins=[('diminuendo',1,2),('crescendo',3,5),('crescendo',6,7),('diminuendo',7,8),('crescendo',9,10),('diminuendo',11,14)],tempo_changes={},group=3,
 performance=dict(rubato=[66,61,65,63,60,64,68,61,65,63,60,57,53,46],
  phrase_arcs=[[0,11,3],[12,29,4],[30,47,5],[48,71,4],[72,84,-2]],
  lower_entries=[[6,24],[30,48],[60,72]],pedal_bars=list(range(1,15)),pedal_lift=.3,gate=.99,
  note='Long compound-metre phrases gain and lose momentum within the line. Sparse bass answers leave the upper melody room to sustain through the pulse.')),
dict(op=12,title='Cloud Causeway',key='D',fifths=2,meter='4/4',bpm=52,
 description='Fen Lantern\'s G-B-flat-C-B-flat falls by a semitone into F-sharp-A-B-A. In this quieter D-major ballad it hovers over major sevenths and B-minor shadows. A C-Lydian reflection briefly widens the view before an E-to-A dominant turn and a soft plagal approach bring the music home.',
 parent_opus=11,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['F#','A','B','A']),
 ancestry=dict(source_opus=11,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['G','Bb','C','Bb'],transposition_semitones=-1),
 rh='''
F#4:1.5 A4:.5 B4:1 A4:1~
A4:1 E5:1 D5:.5 C#5:.5 F#4:1
G4:1 B4:.5 D5:1.5 E5:1~
E5:1 D5:.5 B4:.5 A4:1 R:1
C#5:2 B4:.5 A4:.5 F#4:1~
F#4:1 E4:1 D4:.5 F#4:.5 A4:1
G4:1.5 B4:.5 D5:.5 F#5:.5 E5:1
D5:1 C5:.5 B4:.5 G4:1 R:1
F#4:1 A4:.5 B4:1.5 D5:1~
D5:1 C#5:1 A4:.5 G#4:.5 F#4:1
E4:1.5 G4:.5 A4:1 C#5:1~
C#5:1 B4:.5 A4:.5 F#4:1 R:1
G4:1 B4:.5 D5:.5 E5:1 D5:1~
D5:.5 C#5:.5 B4:1 A4:1 E4:1
F#4:1 A4:1 G4:.5 E4:.5 D4:1~
D4:1 F#4+A4:3
''',
 lh='''
D3:1.5 A3+C#4:1.5 R:1
R:.5 B2:1.5 D3+A3:1 F#3:1
G3:2 B3+D4:1.5 R:.5
A3:1 G3+C#4:2 R:1
F#3:1 A3+E4:1.5 C#4:.5 R:1
B2+D3:2 F#3:1 A3:1~
A3:.5 G3:.5 E3+B3:2 C3:1
G3:1 D3:1 F#3:1 B3:1
B2:2 D3+F#3:1 A3:1
E3:1 G#3+D4:1.5 B2:.5 R:1
A2:1 G3+B3:2 R:1
D3:1.5 A3+C#4:1.5 R:1
G3:1.5 D3+F#3:1.5 B2:1
A2:1 C#3+G3:1.5 E3:.5 R:1
G3:1 B3+D4:1 E3:1 A2:1
D3+F#3:4
''',sections={1:'p',5:'pp',7:'mp',9:'p',13:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,3),(4,6),(7,8),(9,12),(13,16)],lower_phrases=[(2,4),(6,8),(10,12),(14,16)],
 hairpins=[('diminuendo',2,4),('crescendo',5,7),('diminuendo',7,8),('crescendo',9,11),('diminuendo',11,12),('diminuendo',13,16)],tempo_changes={},group=4,
 performance=dict(rubato=[52,51,49,47,51,50,54,48,52,54,51,46,49,46,43,38],
  phrase_arcs=[[0,11,3],[12,23,2],[24,31,4],[32,47,3],[48,64,-1]],
  lower_entries=[[4,12],[20,32],[36,44]],pedal_bars=list(range(1,17)),pedal_lift=.23,gate=.99,
  note='The two hands breathe at different places; the bass phrase continues into the brief C-Lydian colour. The closing descent stays soft and unhurried.'))
]

from dream_pieces_013_024 import PIECES as CONTINUATION_013_024
DREAM_PIECES.extend(CONTINUATION_013_024)
from dream_pieces_025_048 import PIECES as CONTINUATION_025_048
DREAM_PIECES.extend(CONTINUATION_025_048)
from dream_pieces_049_072 import PIECES as CONTINUATION_049_072
DREAM_PIECES.extend(CONTINUATION_049_072)

from dream_pieces_073_096 import PIECES as CONTINUATION_073_096
DREAM_PIECES.extend(CONTINUATION_073_096)

from dream_pieces_097_120 import PIECES as CONTINUATION_097_120
DREAM_PIECES.extend(CONTINUATION_097_120)

from dream_pieces_121_144 import PIECES as CONTINUATION_121_144
DREAM_PIECES.extend(CONTINUATION_121_144)

from dream_pieces_145_168 import PIECES as CONTINUATION_145_168
DREAM_PIECES.extend(CONTINUATION_145_168)

from dream_pieces_169_192 import PIECES as CONTINUATION_169_192
DREAM_PIECES.extend(CONTINUATION_169_192)
