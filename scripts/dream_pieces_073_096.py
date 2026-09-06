"""Individually composed studies for Volume 04, Op. 73–96."""
PIECES=[
dict(op=73,title='Orchid Trestle',key='Bb',fifths=-2,meter='5/4',bpm=56,
 description='Elder Anchorage’s four-note phrase becomes D–E–C–F over a B-flat bass held for fourteen beats. Four independent voices move around that sustained foundation. In bar 10 the melody returns six semitones higher over an equally long E bass, opening an altered dominant field that resolves towards A minor. The last descent brings the original phrase back into a B-flat major ninth with an added sixth.',
 difficulty='Advanced four-voice writing over sustained bass fields',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Hold the bass B-flat from bar 1 through the first four beats of bar 3, and the E from bar 10 through the first four beats of bar 12: each is one fourteen-beat note. Pedal refreshes clear the moving voices while the finger holds the bass. The RH opening phrase returns exactly six semitones higher in bar 10. Keep all four voices distinct, with the two inner lines softer and the tenor gently prominent over the two held bass notes.',
 parent_opus=72,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=5,pitches=['D','E','C','F']),
 ancestry=dict(source_opus=72,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=8,source_pitches=['A','B','G','C'],transposition_semitones=5),
 system_starts=[1,4,7,10,13,16,19,22],page_starts=[10,19],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[b*5+s,b*5+e] for b in range(23) for s,e in [(0,1.76),(2,2.76),(3,4.76)]],
 rh='''
D5:1.5 E5:.5 C5:1 F5:2
E5:3 D5:1 C5:1
D5:2 F5:1 Eb5:2
G5:3 F5:1 D5:1
C5:2 Eb5:1 D5:2
Db5:4 C5:1
Bb4:2 Db5:1 C5:2
D5:3 C5:1 B4:1
E5:3 D5:1 B4:1
G#5:1.5 A#5:.5 F#5:1 B5:2
A5:3 G#5:1 F#5:1
G5:2 B5:1 A5:2
C6:3 B5:1 A5:1
G5:3 F#5:1 E5:1
F5:2 A5:1 G5:2
Eb5:3 D5:1 C5:1
D5:2 F5:1 E5:2
Db5:3 C5:1 Bb4:1
D5:1.5 E5:.5 C5:1 F5:2
Eb5:3 D5:1 C5:1
Bb4:2 A4:1 G4:2
A4:3 G4:1 F4:1
D4+F4+A4:5
''',
 rh_inner='''
F4:2 G4:1 A4:2
Bb4:2 A4:1 G4:2
A4:3 C5:2
Bb4:2 D5:1 C5:2
G4:2 Bb4:1 A4:2
F4:3 Ab4:2
Eb4:2 F4:1 Ab4:2
F4:3 G4:2
G4:2 B4:1 A4:2
D5:2 E5:1 F#5:2
C#5:3 D5:2
D5:2 F5:1 E5:2
E5:3 G5:2
B4:3 D5:2
C5:3 Eb5:2
G4:2 Bb4:1 A4:2
A4:2 C5:1 Bb4:2
F4:3 Ab4:2
F4:2 G4:1 A4:2
G4:2 Bb4:1 A4:2
F4:2 E4:1 Eb4:2
Eb4:2 D4:1 C4:2
C4:5
''',
 lh='''
Bb2:5~
Bb2:5~
Bb2:4 F3:1
Eb3:3 G3:2
C3:3 E3:2
Db3:2 Ab2:3
Gb2:3 Bb2:2
D3:2 F3:3
E3:3 B2:2
E3:5~
E3:5~
E3:4 B2:1
A2:3 E3:2
D3:3 F#3:2
Bb2:3 F3:2
C3:3 E3:2
D3:3 F3:2
Db3:2 Ab2:3
Bb2:5
Eb3:3 G3:2
C3:2 Eb3:3
F3:2 C3:3
Bb2:5
''',
 lh_upper='''
D3:1 F3:1 A3:1 C3:2
D3:2 E3:1 F3:2
G3:1 F3:1 Eb3:2 A3:1
Bb3:2 Db4:1 C4:2
G3:2 Bb3:1 D4:1 C4:1
F3:2 Eb3:1 F3:2
Db3:2 F3:1 Ab3:2
A3:2 C4:1 B3:2
G3:2 B3:1 F#3:2
G#3:1 B3:1 D4:1 C#4:2
F#3:2 G#3:1 B3:2
C4:1 B3:1 A3:2 F#3:1
C3:1 E3:1 G3:1 B3:2
A3:2 C4:1 E4:1 D4:1
D3:1 F3:1 A3:1 C4:2
G3:2 Bb3:1 D4:1 C4:1
F3:1 A3:1 C4:1 E4:2
F3:2 Eb3:1 Gb3:2
D3:1 F3:1 A3:1 C3:2
Bb3:2 D4:1 C4:2
G3:2 Bb3:1 A3:2
A3:2 Bb3:1 Ab3:2
F3:3 G3:2
''',sections={1:'p',2:'p',3:'mp',4:'p',5:'mp',6:'pp',7:'p',8:'mp',9:'pp',10:'p',11:'p',12:'mp',13:'p',14:'pp',15:'mp',16:'p',17:'mp',18:'pp',19:'p',20:'p',21:'pp',22:'pp'},words={1:'poco rubato',22:'poco rit.'},
 slurs=[(1,4),(5,9),(10,14),(15,18),(19,23)],lower_phrases=[(1,4),(5,7),(8,9),(10,13),(14,16),(17,19),(20,23)],
 hairpins=[('crescendo',1,3),('diminuendo',3,4),('diminuendo',5,6),('crescendo',7,8),('diminuendo',8,9),('crescendo',10,12),('diminuendo',12,14),('diminuendo',15,16),('diminuendo',17,18),('diminuendo',19,23)],tempo_changes={},group=3,
 performance=dict(rubato=[56,55,60,50,58,45,53,59,46,57,55,61,52,45,58,51,59,44,53,49,43,36,27],
  phrase_arcs=[[0,19.5,4],[20,44.5,4],[45,69.5,4],[70,89.5,4],[90,115,-2]],
  lower_entries=[[0,14],[45,59],[105,115]],inner_entries=[[25,35],[60,70],[100,110]],tenor_entries=[[0,15],[45,60],[90,100]],pedal_lift=.24,gate=.995,
  note='The held bass remains physically sustained through the short pedal refreshes. Both inner voices breathe around it, with the tenor especially clear in the two long bass fields. The tritone-related middle passage expands the harmonic space before the returning theme and final added-sixth major ninth soften into the low register.'))
]
