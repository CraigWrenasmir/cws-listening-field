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
]
