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
,
dict(op=74,title='Camellia Wake',key='c#',fifths=4,meter='12/8',bpm=57,
 description='Orchid Trestle’s opening becomes C-sharp–D-sharp–B–E inside a nine-note ribbon. Three such ribbons each pass across four slower lower notes, then settle on a two-beat note inside the compound bar. C-major and G-major windows briefly loosen the tonal centre before the line returns through a soft dominant to a C-sharp-minor ninth.',
 difficulty='Advanced nonuplets over a slower lower line',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 1, 5 and 9, nine RH eighth-note nonuplets share four quarter beats with four LH quarter notes. Treat each group as one unaccented contour, then let the final two beats settle. The sweep and settling note in bar 5 descend across more than an octave; plan its fingering before joining the hands. Keep the later chord tops gently voiced as the line returns to the middle register.',
 parent_opus=73,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['C#','D#','B','E']),
 ancestry=dict(source_opus=73,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=5,source_pitches=['D','E','C','F'],transposition_semitones=11),
 tuplet_groups=[dict(hand='rh',actual=9,normal=8,count=27)],
 tuplet_spans=[dict(hand='rh',start_beat=b*6,end_beat=b*6+4,actual=9,normal=8,stem='down') for b in [0,4,8]],
 polyrhythms=[dict(start_beat=b*6,end_beat=b*6+4,rh_notes=9,lh_notes=4) for b in [0,4,8]],
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[i*2,i*2+1.76] for i in range(48)],
 rh='''
C#5:4/9 D#5:4/9 B4:4/9 E5:4/9 F#5:4/9 G#5:4/9 F#5:4/9 E5:4/9 D#5:4/9 C#5:2
B4:3 D#5:1 C#5:2
G#4+B4+F#5:3 E5:1 D#5:2
E5:2 F#5:.5 G#5:.5 B5:2 A5:1
G#5:4/9 A5:4/9 G#5:4/9 F#5:4/9 E5:4/9 D#5:4/9 C#5:4/9 B4:4/9 A4:4/9 G#4:2
G4+B4+E5:4 D5:1 C5:1
A4+D5+G5:3 F5:1 E5:2
F#5:3 E5:1 D5:2
E5:4/9 F#5:4/9 G#5:4/9 B5:4/9 C#6:4/9 B5:4/9 A5:4/9 G#5:4/9 F#5:4/9 E5:2
D5+G5+C6:3 B5:1 A5:2
G#5:4 F#5:1 E5:1
D#5:3 C#5:1 B4:2
D#4+F#4+B#4:3 C#5:1 B4:2
A4:3 G#4:1 F#4:2
E4+G#4+D#5:3 C#5:1 B4:2
E4+G#4+D#5:6
''',
 lh='''
C#3:1 G#3:1 B3:1 D#4:1 E4:1 B3:1
A2:2 E3:1 G#3:1 B3:1 C#4:1
E3:1 B3:1 D#4:1 C#4:1 B3:2
F#3:1 C#4:1 E4:1 D#4:1 C#4:2
C#3:1 E3:1 G#3:1 B3:1 D#4:1 C#4:1
C3:1 G3:.5 B3:1.5 E4:1 D4:2
F3:1 C4:1 E4:1 D4:1 C4:2
B2:2 F#3:1 A3:1 C#4:1 B3:1
A3:1 B3:1 C#4:1 D#4:1 E4:1 D#4:1
G3:2 D3:1 F#3:1 A3:1 B3:1
E3:1 B3:.5 D#4:1.5 F#4:1 E4:2
D#3:1 A#3:1 C#4:1 F#4:1 E4:1 B3:1
G#2:1 D#3:1 F#3:1 B#3:1 C#4:1 B3:1
A2:2 E3:1 G#3:1 B3:1 A3:1
F#2:1 C#3:1 E3:1 A3:1 G#3:2
C#3+G#3:6
''',sections={1:'p',2:'pp',3:'p',4:'mp',5:'p',6:'pp',7:'mp',8:'pp',9:'p',10:'mp',11:'p',12:'pp',13:'p',14:'pp',15:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,16)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,16)],
 hairpins=[('diminuendo',1,2),('crescendo',3,4),('diminuendo',5,6),('diminuendo',7,8),('crescendo',9,10),('diminuendo',10,12),('diminuendo',13,16)],tempo_changes={},group=2,
 performance=dict(rubato=[57,49,55,61,56,45,58,47,57,62,53,46,51,43,36,27],
  phrase_arcs=[[0,23.5,4],[24,47.5,4],[48,71.5,4],[72,96,-2]],
  lower_entries=[[6,12],[30,36],[60,66],[84,90]],pedal_lift=.24,gate=.985,
  note='The nine-note figures rise or fall as complete arcs, staying light over the slower lower notes. Their settling tails let the compound metre breathe. The final four bars become progressively quieter and closer in register, leaving the minor ninth to ring in the warm room.'))
,
dict(op=75,title='Rowan Afterglow',key='e',fifths=1,meter='9/4',bpm=55,
 description='Camellia Wake’s opening becomes E–F-sharp–D–G inside a longer, nine-beat phrase. A quiet inner voice supports the melody, then withdraws for two whole-tone sweeps, one rising and one falling. Their brighter dominant colours dissolve into warmer minor and major harmony. At the close, an inner C falls to B before the bass adds the final ninth.',
 difficulty='Advanced whole-tone sweeps with an independent inner voice',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The six eighth-note triplets in bars 5 and 8 each fill two beats and move entirely by whole tones. The RH inner voice rests during those runs, returning beneath their held arrivals. Keep the nine-beat bars inside the longer phrases rather than accenting each subdivision. In the last bar, let the inner C resolve to B while the upper E-minor chord remains held.',
 parent_opus=74,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=9,pitches=['E','F#','D','G']),
 ancestry=dict(source_opus=74,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['C#','D#','B','E'],transposition_semitones=3),
 tuplet_groups=[dict(hand='rh',actual=3,normal=2,count=12)],
 system_starts=[1,3,5,7,9],page_starts=[7],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[i*3,i*3+2.76] for i in range(30)]+[[90,90.76],[91,93.76],[94,95.76],[96,98.76]],
 rh='''
E5:2 F#5:1 D5:3 G5:3
F#5:4 E5:2 D5:3
E5:3 G5:1 F#5:2 D5:3
C5:3 E5:2 D5:1 B4:3
E5:1/3 F#5:1/3 G#5:1/3 Bb5:1/3 C6:1/3 D6:1/3 E6:4 D6:1 B5:2
A5:4 G5:2 F#5:3
E5:3 G5:1 F#5:2 D5:3
D6:1/3 C6:1/3 Bb5:1/3 G#5:1/3 F#5:1/3 E5:1/3 D5:4 C5:1 B4:2
C5+E5+B5:4 A5:2 G5:3
F#5:3 E5:2 D#5:1 B4:3
E4+G4+B4:9
''',
 rh_inner='''
B4:3 A4:3 G4:3
A4:3 C5:2 B4:1 A4:3
G4:3 B4:3 A4:3
G4:3 B4:2 A4:1 F#4:3
R:6 G5:1 F#5:2
E5:3 D5:3 C5:3
G4:3 B4:3 A4:3
R:2 G4:4 A4:1 F#4:2
G5:4 F5:2 E5:3
A4:3 G4:2 F#4:1 D4:3
R:1 C4:3 B3:5
''',
 lh='''
E3:2 B3:1 D4:1 F#4:2 E4:1 B3:2
C3:3 G3:1 B3:2 D4:1 C4:2
A2:2 E3:1 G3:2 B3:1 C4:1 G3:2
B2:3 F#3:1 A3:2 C#4:1 B3:2
C3:3 G3:1 Bb3:2 E4:1 D4:2
A2:3 E3:1 G3:2 B3:1 C4:2
D3:2 A3:1 C4:2 E4:1 D4:1 A3:2
Ab2:3 E3:1 Gb3:2 C4:1 Bb3:2
C3:2 G3:1 B3:2 D4:1 C4:1 G3:2
B2:3 F#3:1 A3:2 C4:1 B3:2
E3:6 F#3:3
''',sections={1:'p',2:'p',3:'mp',4:'pp',5:'mp',6:'p',7:'pp',8:'mp',9:'p',10:'pp',11:'pp'},words={1:'poco rubato',10:'poco rit.'},
 slurs=[(1,4),(5,7),(8,11)],lower_phrases=[(1,3),(4,6),(7,9),(10,11)],
 hairpins=[('crescendo',1,2),('diminuendo',3,4),('diminuendo',5,7),('diminuendo',8,11)],tempo_changes={},group=2,
 performance=dict(rubato=[55,52,58,45,58,51,44,57,49,38,27],
  phrase_arcs=[[0,35.5,4],[36,62.5,4],[63,99,-2]],
  lower_entries=[[9,18],[27,36],[54,63],[81,90]],inner_entries=[[42,45],[65,72],[91,99]],pedal_lift=.24,gate=.99,
  note='The inner voice withdraws to leave each whole-tone sweep light and clear, then returns beneath the held melody. The longer nine-beat spans breathe across several lower-line changes. A pedal lift clears the inner C before its resolution to B, followed by the added ninth in the bass. The last harmony unfolds gradually while its upper notes remain held.'))
,
dict(op=76,title='Mallow Crescent',key='Eb',fifths=-3,meter='3/4',bpm=56,
 description='Rowan Afterglow’s inner descent becomes D–C–B-flat–C at the top of softly clustered chords. Neighbouring seconds remain inside the voicings while the upper line alternates with single-note space. C- and D-major reflections, a brief E-flat-minor shade and the returning opening shapes lead to an E-flat major ninth.',
 difficulty='Advanced quiet voicing of adjacent-note chords',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Most RH chord shapes contain four notes with a major or minor second inside. Give their top notes a clear, soft melody and keep the other chord notes lighter. The chord spans remain compact; the difficulty lies in even attacks and voicing. Pedal changes follow the denser chord changes in bars 1, 6, 13, 17, 19 and 23, clearing their adjacent pitches before the next shape.',
 parent_opus=75,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['D','C','Bb','C']),
 ancestry=dict(source_opus=75,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=12,source_pitches=['B','A','G','A'],transposition_semitones=3),
 system_starts=[1,5,9,13,17,21],page_starts=[13],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*3+left,(bar-1)*3+right-.2] for bar,cuts in enumerate([[0,1,2,3],[0,1.5,3],[0,2,3],[0,3],[0,1,2,3],[0,1.5,3],[0,1.5,3],[0,1.5,3],[0,2,3],[0,1.5,3],[0,2,3],[0,1.5,3],[0,1.5,3],[0,1.5,3],[0,1,3],[0,1.5,3],[0,1.5,3],[0,1.5,3],[0,1,2,3],[0,1.5,3],[0,2,3],[0,1.5,3],[0,1.5,3],[0,3]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
G4+Bb4+C5+D5:1 F4+Ab4+Bb4+C5:1 Eb4+G4+A4+Bb4:1
C5:3
F4+Ab4+Bb4+C5:2 Eb4+G4+A4+Bb4:1
G4+Bb4+D5+F5:3
Eb5:2 D5:1
G4+Bb4+C5+D5:1.5 F4+Ab4+Bb4+C5:1.5
E4+G4+A4+B4:3
C5:2 D5:1
F#4+A4+B4+C#5:2 E4+G4+A4+B4:1
D5:3
G4+Bb4+C5+D5:2 F4+Ab4+Bb4+C5:1
Bb4:3
Ab4+C5+Db5+Eb5:1.5 G4+Bb4+C5+D5:1.5
C5:2 Bb4:1
F4+Ab4+Bb4+C5:1 Eb4+Gb4+Ab4+Bb4:2
Ab4:3
E4+G4+A4+B4:1.5 F#4+A4+B4+C#5:1.5
D5:2 C#5:1
G4+Bb4+C5+D5:1 F4+Ab4+Bb4+C5:1 Eb4+G4+A4+Bb4:1
C5:3
Eb4+G4+A4+Bb4:2 D4+F4+G4+A4:1
G4:2 F4:1
D4+F4+G4+A4:1.5 Eb4+G4+A4+Bb4:1.5
D4+F4+G4+Bb4:3
''',
 lh='''
Eb3:1 Bb3:2
Ab2:1.5 Eb3:.5 G3:1
F3:1 C4:2
Bb2+F3:3
Eb3:1 G3:.5 Bb3:1.5
Ab2:1 Eb3:1 Gb3:1
C3:1 G3:.5 B3:1.5
G2:1 D3:1 F3:1
D3:1 A3:.5 C#4:.5 B3:1
B2:1 F#3:1 A3:1
Eb3:1 Bb3:.5 D4:.5 C4:1
Ab2:1.5 Eb3:.5 G3:1
Db3:1 Ab3:1 Bb3:1
Gb2:1 Db3:1 F3:1
Eb3:1 Bb3:.5 Db4:1.5
Ab2:1 Eb3:1 Gb3:1
C3:1 G3:.5 B3:1.5
D3:1 A3:1 C#4:1
Eb3:1 Bb3:2
Ab2:1.5 Eb3:.5 G3:1
C3:1 G3:.5 Bb3:1.5
F3:1 C4:1 Eb4:1
Bb2:1 F3:.5 G3:1.5
Eb3+Bb3:3
''',sections={1:'p',2:'pp',3:'p',4:'mp',5:'p',6:'mp',7:'pp',8:'p',9:'mp',10:'pp',11:'p',12:'pp',13:'mp',14:'p',15:'mp',16:'pp',17:'p',18:'mp',19:'p',20:'pp',21:'p',22:'pp',23:'pp'},words={1:'poco rubato',23:'poco rit.'},
 slurs=[(1,5),(6,10),(11,16),(17,20),(21,24)],lower_phrases=[(1,4),(5,7),(8,10),(11,13),(14,16),(17,20),(21,24)],
 hairpins=[('diminuendo',1,2),('diminuendo',4,5),('diminuendo',6,7),('diminuendo',9,10),('diminuendo',11,12),('diminuendo',13,14),('diminuendo',15,16),('crescendo',17,18),('diminuendo',19,20),('diminuendo',21,24)],tempo_changes={},group=4,
 performance=dict(rubato=[56,48,55,60,51,58,46,54,59,45,53,46,60,51,57,44,54,61,52,45,50,43,37,28],
  phrase_arcs=[[0,14.5,3],[15,29.5,4],[30,47.5,4],[48,59.5,4],[60,72,-2]],
  lower_entries=[[3,6],[18,24],[33,36],[45,48],[57,60],[66,69]],pedal_lift=.2,gate=.985,
  note='The uppermost chord notes carry the line while the adjacent inner pitches remain gentle. Single-note bars create space between the denser shapes. Pedal refreshes clear each close voicing before its successor, and the last major ninth settles without a forceful cadence.'))
,
dict(op=77,title='Ginkgo Crossing',key='D',fifths=2,meter='5/4',bpm=56,
 description='Mallow Crescent’s upper descent becomes F-sharp–E–D–E inside a seven-note phrase. Seven upper notes and five lower notes share two beats, then settle into a held three-beat harmony. Three crossings rise, turn and finally descend through D-major, C-major and quieter minor colours. A soft inner voice enters only after each crossing, leading towards a D-major ninth.',
 difficulty='Advanced seven-against-five with an entering inner voice',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 1, 5 and 9, seven RH eighth-note septuplets and five LH eighth-note quintuplets each fill two quarter beats. The RH inner voice rests for those two beats, entering with the three-beat settling note. Practise each line as a single smooth contour before joining the hands, and let their shared arrival stay unaccented.',
 parent_opus=76,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=2,pitches=['F#','E','D','E']),
 ancestry=dict(source_opus=76,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['D','C','Bb','C'],transposition_semitones=4),
 tuplet_groups=[dict(hand='rh',actual=7,normal=4,count=21),dict(hand='lh',actual=5,normal=4,count=15)],
 tuplet_spans=[dict(hand=hand,voice=voice,start_beat=b*5,end_beat=b*5+2,actual=count,normal=4,stem=stem) for b in [0,4,8] for hand,voice,count,stem in [('rh','upper',7,'up'),('lh','bass',5,'down')]],
 polyrhythms=[dict(start_beat=b*5,end_beat=b*5+2,rh_notes=7,lh_notes=5) for b in [0,4,8]],
 system_starts=[1,3,5,7,9,11,13],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[b*5+s,b*5+e] for b in range(14) for s,e in [(0,1.76),(2,3.76),(4,4.76)]],
 rh='''
F#5:2/7 E5:2/7 D5:2/7 E5:2/7 F#5:2/7 A5:2/7 G5:2/7 F#5:3
E5:3 D5:1 C#5:1
D5+G5:3 F#5:1 E5:1
F5:3 Eb5:1 Db5:1
C5:2/7 D5:2/7 E5:2/7 G5:2/7 A5:2/7 G5:2/7 F5:2/7 E5:3
D5:3 C5:1 B4:1
E5:2 G5:1 F#5:2
D5:3 C#5:1 B4:1
A5:2/7 G5:2/7 F#5:2/7 E5:2/7 D5:2/7 C#5:2/7 B4:2/7 A4:3
G4+B4+E5:3 D5:1 C5:1
C5+F5+Bb5:3 A5:1 G5:1
F#5:3 E5:1 D5:1
E5:2 D5:1 C#5:2
F#4+A4+C#5+E5:5
''',
 rh_inner='''
R:2 A4:3
G4:2 B4:1 A4:2
B4:3 A4:2
Ab4:3 C5:2
R:2 C5:3
A4:2 G4:1 F#4:2
B4:3 D5:2
G4:3 F#4:2
R:2 E4:3
F#4:3 E4:2
Bb4:3 C5:2
A4:2 C5:1 B4:2
G4:3 F#4:2
R:5
''',
 lh='''
D3:2/5 F#3:2/5 A3:2/5 C#4:2/5 B3:2/5 A3:3
G2:2 D3:1 F#3:1 A3:1
E3:1 B3:1 D4:1 C#4:2
Bb2:2 F3:1 Ab3:1 C4:1
C3:2/5 E3:2/5 G3:2/5 B3:2/5 A3:2/5 G3:3
D3:1 A3:1 C4:1 E4:2
E3:2 B3:1 D4:1 C#4:1
A2:1 E3:1 G3:1 B3:2
G3:2/5 F#3:2/5 E3:2/5 D3:2/5 C#3:2/5 B2:3
E3:1 B3:1 D4:1 C4:2
F3:1 C4:1 Eb4:1 B3:2
G2:2 D3:1 F#3:1 A3:1
A2:1 E3:1 G3:1 B3:1 C#4:1
D3+A3:5
''',sections={1:'p',2:'pp',3:'mp',4:'p',5:'p',6:'pp',7:'mp',8:'pp',9:'p',10:'pp',11:'mp',12:'p',13:'pp'},words={1:'poco rubato',13:'poco rit.'},
 slurs=[(1,4),(5,8),(9,14)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,14)],
 hairpins=[('diminuendo',1,2),('diminuendo',3,4),('diminuendo',5,6),('diminuendo',7,8),('diminuendo',9,10),('diminuendo',11,14)],tempo_changes={},group=2,
 performance=dict(rubato=[56,48,59,51,57,45,60,46,53,44,58,49,39,28],
  phrase_arcs=[[0,19.5,4],[20,39.5,4],[40,70,-2]],
  lower_entries=[[5,10],[25,30],[50,55],[60,65]],inner_entries=[[2,5],[22,25],[42,45]],pedal_lift=.24,gate=.985,
  note='The seven-note and five-note figures share a destination without accenting every unequal subdivision. The inner voice joins only when the two hands settle, giving each crossing a softer after-image. The final descent withdraws into a close major ninth.'))
,
dict(op=78,title='Saffron Interstice',key='Ab',fifths=-4,meter='7/4',bpm=56,
 meters=['7/4','5/4','4/4','6/4','5/4','3/4','4/4','4/4','6/4','5/4','7/4','3/4','4/4','5/4','6/4','7/4'],
 description='Ginkgo Crossing’s opening bass becomes an A-flat major-seventh ascent in the melody. Four voices pass through irregular, breathing spans. At the centre, an eight-beat upper G remains still while the inner C–B–B-flat–A falls against E-flat–E–F–F-sharp in the tenor. The resulting minor-to-major changes open a G-major clearing before the return through B-flat minor and borrowed D-flat minor towards A-flat sixth/ninth.',
 difficulty='Advanced four-voice colour changes and irregular phrase lengths',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Bars 7–8 hold the upper G continuously across the bar line. The two inner lines move in contrary chromatic steps, each note lasting two beats; voice them independently while the upper note remains quiet. Changing metres follow phrase lengths. The RH inner voice is absent for the first four beats, and the bass and tenor divide the wider opening and final harmonies between successive positions.',
 parent_opus=77,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=7,pitches=['Ab','C','Eb','G']),
 ancestry=dict(source_opus=77,source_hand='lh',source_voice='bass',source_start_beat=0,source_end_beat=2,source_pitches=['D','F#','A','C#'],transposition_semitones=6),
 system_starts=[1,3,5,7,9,11,13,15],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[start+left,start+right-.24] for start,cuts in zip([0,7,12,16,22,27,30,34,38,44,49,56,59,63,68,74],[[0,2,4,7],[0,2,3,5],[0,2,4],[0,2,3,4,6],[0,2,3,5],[0,1,2,3],[0,2,4],[0,2,4],[0,2,3,4,6],[0,2,3,5],[0,2,3,4,7],[0,1,2,3],[0,2,3,4],[0,2,3,5],[0,2,3,4,6],[0,4,7]]) for left,right in zip(cuts,cuts[1:])],
 rh='''
Ab4:1.5 C5:1 Eb5:1.5 G5:3
F5:3 Eb5:1 Db5:1
C5:2 Ab4:1 Bb4:1
D5:3 C5:1 Ab4:2
G5:2 F5:1 Eb5:2
F5:1 Ab5:1 G5:1
G5:4~
G5:4
B5:2 A5:1 G5:3
F#5:2 E5:1 D5:2
F5:3 Eb5:1 Db5:3
G5:1 F5:1 E5:1
Eb5:2 C5:1 Bb4:1
Fb5:3 Eb5:1 Db5:1
F5:3 Eb5:1 Db5:2
Bb4+C5:7
''',
 rh_inner='''
R:4 G4:3
Ab4:2 C5:1 Bb4:2
G4:2 F4:2
Ab4:3 G4:1 F4:2
Bb4:3 C5:2
D5:1 F5:1 E5:1
C5:2 B4:2
Bb4:2 A4:2
D5:2 C5:1 B4:3
B4:2 A4:1 G4:2
C5:2 Db5:1 C5:1 Ab4:3
Db5:1 C5:1 Bb4:1
Bb4:2 Ab4:1 G4:1
Ab4:2 Bb4:1 Ab4:2
Bb4:2 Ab4:1 G4:3
F4:7
''',
 lh='''
Ab2:4 Eb3:3
Db3:3 Ab2:2
F3:1 C3:3
Bb2:4 F3:2
Eb3:3 Bb2:2
B2:2 F3:1
C3:4
D3:4
G2:3 D3:3
E3:2 B2:3
Bb2:3 F3:4
Eb3:2 Bb2:1
Ab2:2 Eb3:2
Db3:3 Ab2:2
Eb3:2 Bb2:2 Db3:2
Ab2:4 Eb3:3
''',
 lh_upper='''
Eb3:2 F3:1 G3:1 Bb3:3
F3:2 Ab3:1 Gb3:2
Ab3:1 G3:1 Ab3:2
F3:2 Ab3:2 D4:2
G3:2 Ab3:1 G3:2
D3:1 F3:1 Ab3:1
Eb3:2 E3:2
F3:2 F#3:2
B2:2 D3:1 F#3:1 E3:2
G3:1 F#3:1 D3:1 F#3:2
Db3:2 Ab3:1 Bb3:2 Ab3:2
G3:1 F3:1 Db3:1
C3:1 Eb3:1 G3:1 F3:1
Fb3:2 Ab3:1 Gb3:2
Ab3:2 G3:2 Bb3:2
C3:4 Ab3:3
''',sections={1:'p',2:'pp',4:'mp',5:'p',6:'pp',7:'p',8:'mp',9:'pp',10:'p',11:'mp',12:'p',13:'pp',14:'p',15:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,5),(6,10),(11,16)],lower_phrases=[(1,4),(5,8),(9,12),(13,16)],
 hairpins=[('diminuendo',1,3),('crescendo',4,5),('diminuendo',6,9),('diminuendo',11,14),('diminuendo',15,16)],tempo_changes={},group=2,
 performance=dict(rubato=[56,49,52,57,48,53,46,44,50,46,54,44,49,42,38,29],
  phrase_arcs=[[0,26.5,3],[27,48.5,4],[49,81,-2]],
  lower_entries=[[12,16],[44,49],[59,63]],inner_entries=[[30,38],[63,68]],tenor_entries=[[30,38],[49,56]],pedal_lift=.24,gate=.99,
  note='An upper note stays finger-held through four inner harmonies, with pedal refreshes at each chromatic step. The inner parts briefly become the melody while the outer voices stay calm. Irregular spans follow the phrase, and the final sixth/ninth is allowed to settle with a lighter lower arrival.'))
,
dict(op=79,title='Clover Backwater',key='Eb',fifths=-3,meter='4/4',bpm=54,
 description='Saffron Interstice’s opening ascent returns as E-flat–G–B-flat–D, with offbeat entries and ties that carry the melody across bar lines. Left-hand bass notes alternate with spare jazz shell voicings. An E-major/A-dominant window leads through D minor and C major; a later D-major reflection and altered C/B-flat colours draw the line back towards E-flat.',
 difficulty='Advanced syncopated ballad phrasing and quiet shell voicings',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Keep the melody continuous through the offbeat entries and tied bar lines. The LH separates bass notes from upper shell chords; these are successive positions, not notes to stretch for simultaneously. Several chromatic colours sit inside dominant harmonies. The rests in the LH opening phrases and the long upper notes leave room for flexible, unhurried voicing.',
 parent_opus=78,motif=dict(hand='rh',start_beat=0,end_beat=8,pitches=['Eb','G','Bb','D']),
 ancestry=dict(source_opus=78,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=7,source_pitches=['Ab','C','Eb','G'],transposition_semitones=7),
 system_starts=[1,4,7,10,13,16,19],page_starts=[13],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.22] for bar,cuts in enumerate([[0,1.5,3,4],[0,1.5,3,4],[0,2,3.5,4],[0,1.5,3,4],[0,2,3,4],[0,1,3,4],[0,1.5,3,4],[0,2,3.5,4],[0,1,2.5,4],[0,2,3,4],[0,1,2.5,4],[0,1,3,4],[0,1.5,3,4],[0,2,3,4],[0,1.5,3,4],[0,1,2,4],[0,1,2,4],[0,2,3,4],[0,1,2,3,4],[0,2,3,4],[0,1,2,4],[0,1,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
Eb5:1.5 G5:2 Bb5:.5~
Bb5:1 D6:2 C6:1
Ab5:1.5 G5:.5 F5:1 Eb5:1
D5+G5:2 C5+F5:1.5 Bb4+Eb5:.5~
Bb4+Eb5:1 G4+D5:1 Eb5:2
F#5:1.5 G#5:1 B5:1.5~
B5:.5 A5:1.5 G5:2
F5:1.5 E5:.5 D5:2~
D5:1 B4:1.5 A4:1.5
G4+B4+E5:3 D5:1
F5:1 Ab5:1.5 G5:1.5
Eb5:1.5 D5:1.5 C5:1
G5:2 Ab5:1 G5:1~
G5:.5 F5:1.5 Eb5:2
F#5:1.5 E5:1.5 A5:1
Bb5:1 A5:1.5 G5:1.5~
G5:1 F5:1 Eb5:2
C5:1.5 Eb5:.5 G5:2
Gb5:1 F5:1 D5:2
F5:1.5 G5:1.5 Bb5:1~
Bb5:1 G5:1 F5:2~
F5:1 G4+Bb4+Eb5:3
''',
 lh='''
Eb3:1.5 Bb3+D4:1.5 G3+C4:1
Ab2:1 R:.5 Eb3+G3:1.5 C4:1
F3:2 Ab3+Eb4:1.5 G3:.5
Bb2:1 R:.5 Ab3+D4:1.5 G3+C4:1
Eb3:2 G3+Bb3:1 F3+A3:1
E3:1 B3+D#4:2 G#3+C#4:1
A2:1.5 G3+C#4:1.5 F#3+B3:1
D3:2 F3+C4:1.5 E3+A3:.5
G2:1 F3+B3:1.5 E3+A3:1.5
C3:2 G3+B3:1 D3:1
Db3:1 Ab3+Cb4:1.5 F3+Bb3:1.5
C3:1 G3+Bb3:2 Eb3:1
F3:1.5 Ab3+Eb4:1.5 C4:1
Bb2:2 Ab3+D4:1 G3+C4:1
D3:1.5 A3+C#4:1.5 F#3+B3:1
G3:1 D3:1 Bb3+E4:2
C3:1 Bb3+E4:1 A3+D4:2
F3:2 Ab3+Eb4:1 G3+C4:1
Bb2:1 Ab3+D4:1 Cb4:1 F3:1
Eb3:2 Bb3+D4:1 G3+C4:1
Ab2:1 Eb3+G3:1 C4:2
Eb3+Bb3:4
''',sections={1:'p',3:'pp',4:'mp',5:'p',6:'pp',7:'p',8:'pp',10:'p',11:'mp',12:'pp',13:'p',14:'pp',15:'p',16:'mp',17:'p',18:'pp',19:'p',20:'pp',21:'pp'},words={1:'poco rubato',21:'poco rit.'},
 slurs=[(1,5),(6,10),(11,14),(15,18),(19,22)],lower_phrases=[(1,5),(6,9),(10,12),(13,15),(16,19),(20,22)],
 hairpins=[('diminuendo',1,3),('diminuendo',4,5),('crescendo',6,7),('diminuendo',8,10),('diminuendo',11,14),('crescendo',15,16),('diminuendo',17,18),('diminuendo',19,22)],tempo_changes={},group=3,
 performance=dict(rubato=[54,58,48,56,45,52,58,49,45,40,57,46,54,44,51,59,50,43,48,43,35,26],
  phrase_arcs=[[0,19.5,4],[20,39.5,4],[40,55.5,3],[56,71.5,4],[72,88,-2]],
  lower_entries=[[8,12],[32,36],[44,48],[68,72]],pedal_lift=.22,gate=.99,
  note='The melody leans gently into its delayed entries and remains held across bar lines. The lower chord shapes answer the tune without a fixed repeated accompaniment. Quieter bass attacks leave the upper chord tones audible; the return slows across its last three bars into a plain major harmony.'))
,
dict(op=80,title='Tamarisk Confluence',key='G',fifths=1,meter='4/4',bpm=53,
 description='Clover Backwater’s rising figure becomes G–B–D–F-sharp. At the centre, a held upper G and bass G surround a continuous ripple passed between the inner voices. One bar uses major colours and the next minor colours, while the outer notes remain unchanged. E-flat and A-flat reflections lead back through E minor and a borrowed C-minor shade to G sixth/ninth.',
 difficulty='Advanced interlocking inner voices beneath sustained outer notes',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 6–7, the LH tenor and RH inner voice alternate sixteenth notes, beginning with the tenor. Each inner voice rests during the other’s note. Hold the upper G from the end of bar 5 through bar 7, and the bass G throughout bars 5–7. The LH changes to treble clef at bar 5 and returns to bass at bar 8. Pedal supports the ripple but the outer notes remain finger-held through its refreshes.',
 parent_opus=79,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['G','B','D','F#']),
 ancestry=dict(source_opus=79,source_hand='rh',source_start_beat=0,source_end_beat=8,source_pitches=['Eb','G','Bb','D'],transposition_semitones=4),
 clef_changes={'lh':{5:'treble',8:'bass'}},
 system_starts=[1,4,6,7,8,11,14],page_starts=[8],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.2] for bar,cuts in enumerate([[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,1,2,3,4],[0,2,3,4],[0,2,4],[0,2,4],[0,2,3,4],[0,2,4],[0,1,2,4],[0,2,3,4],[0,1,2,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,4],[0,1,2,4],[0,2,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
G4:1 B4:1 D5:1 F#5:1
E5:2 D5:1 B4:1
C5:3 B4:1
F#5:1 E5:1 D5:2
B5:2 A5:1 G5:1~
G5:4~
G5:4
F5:2 Eb5:2
D5:1 Eb5:1 G5:2
F#5:3 E5:1
D5:1.5 C5:.5 A4:2
B4:1 D5:1 F#5:2
G5:2 F#5:1 E5:1
F#5:1 E5:1 C5:2
D5:3 B4:1
Eb5:2 D5:1 C5:1
A4+B4+D5:4
''',
 rh_inner='''
R:3 A4:1
G4:2 F4:1 E4:1
G4:2 E4:2
A4:2 C5:2
D5:2 C5:1 B4:1
R:.25 B4:.25 R:.25 D5:.25 R:.25 E5:.25 R:.25 D5:.25 R:.25 B4:.25 R:.25 A4:.25 R:.25 B4:.25 R:.25 D5:.25
R:.25 Bb4:.25 R:.25 D5:.25 R:.25 Eb5:.25 R:.25 D5:.25 R:.25 Bb4:.25 R:.25 A4:.25 R:.25 Bb4:.25 R:.25 D5:.25
Bb4:2 G4:2
Bb4:2 C5:2
C#5:2 B4:2
F#4:2 E4:2
G4:2 B4:2
C5:2 B4:1 A4:1
A4:2 G4:2
G4:2 E4:2
A4:2 G4:2
E4:4
''',
 lh='''
G2:2 D3:2
C3:2 G2:2
A2:3 E3:1
D3:2 A2:2
G3:4~
G3:4~
G3:4
Eb3:3 Bb2:1
Ab2:2 Eb3:2
D3:2 A2:2
B2:3 F#3:1
E3:2 B2:2
A2:2 E3:2
D3:2 A2:2
G2:2 D3:2
C3:2 G2:2
G2:2 D3:2
''',
 lh_upper='''
B2:2 F#3:2
E3:2 D3:2
C3:2 G3:1 A3:1
F#3:1 G3:1 F#3:1 E3:1
D4:2 E4:1 F#4:1
B3:.25 R:.25 D4:.25 R:.25 E4:.25 R:.25 F#4:.25 R:.25 E4:.25 R:.25 D4:.25 R:.25 B3:.25 R:.25 A3:.25 R:.25
Bb3:.25 R:.25 D4:.25 R:.25 Eb4:.25 R:.25 F4:.25 R:.25 Eb4:.25 R:.25 D4:.25 R:.25 Bb3:.25 R:.25 A3:.25 R:.25
G3:2 F3:1 Eb3:1
C3:2 F3:2
F#3:1 A3:1 G3:2
D#3:2 A3:1 C4:1
G3:1 F#3:1 D3:2
C3:1 D3:1 G3:1 F#3:1
F#3:1 G3:1 F#3:1 E3:1
B2:1 D3:1 F#3:2
Eb3:1 F3:1 Eb3:2
B2:2 G3:2
''',sections={1:'p',2:'pp',4:'p',5:'mp',6:'p',7:'pp',8:'pp',9:'p',10:'mp',11:'p',12:'pp',13:'p',14:'p',15:'pp',16:'p',17:'pp'},words={1:'poco rubato',16:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,17)],lower_phrases=[(1,4),(5,8),(9,12),(13,17)],
 hairpins=[('diminuendo',1,3),('diminuendo',5,8),('crescendo',9,10),('diminuendo',11,12),('diminuendo',13,15),('diminuendo',16,17)],tempo_changes={},group=3,
 performance=dict(rubato=[53,48,44,54,58,51,46,41,49,55,46,42,52,45,39,35,27],
  phrase_arcs=[[0,15.5,3],[16,31.5,4],[32,47.5,4],[48,68,-2]],
  lower_entries=[[8,12],[40,44],[60,64]],inner_entries=[[20,28]],tenor_entries=[[20,28]],pedal_lift=.2,gate=.99,
  note='The outer Gs stay still as the middle texture lights up in alternate hands. Major thirds and sixths darken by a semitone in the second ripple bar. Each short note stays light and the pedal supplies continuity between hands; the slow outer line returns to the foreground afterwards.'))
,
dict(op=81,title='Magnolia Interval',key='bb',fifths=-5,meter='6/4',bpm=52,
 description='Tamarisk Confluence’s inner ripple supplies B-flat–D-flat–E-flat–D-flat, now stretched into a quiet B-flat-minor melody. A D-flat pentatonic sweep appears alone in the treble, then returns two octaves lower at four-thirds of its original note lengths while the RH rests. The reunited voices move through E major, A dominant and D minor before a B-flat minor sixth/ninth close.',
 difficulty='Advanced solo-hand exchanges, triplets and flexible minor-ballad voicing',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Bar 7 has twelve unaccompanied RH sixteenth notes over three beats, followed by a held D-flat. Bar 8 echoes those twelve pitches two octaves lower as LH eighth-note triplets over four beats; both RH voices remain silent. Let the returning lower contour expand naturally. The final close contains a soft C/D-flat second inside the RH chord, with an independently held G below it.',
 parent_opus=80,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=6,pitches=['Bb','Db','Eb','Db']),
 ancestry=dict(source_opus=80,source_hand='rh',source_voice='inner',source_start_beat=20,source_end_beat=22,source_pitches=['B','D','E','D'],transposition_semitones=-1),
 tuplet_groups=[dict(hand='lh',actual=3,normal=2,count=12)],
 system_starts=[1,3,5,7,8,9,11,13],page_starts=[8],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*6+left,(bar-1)*6+right-.24] for bar,cuts in enumerate([[0,2,3,4,6],[0,2,3,4,6],[0,3,4,6],[0,2,3,4,6],[0,2,3,4,6],[0,2,3,4,5,6],[0,1.5,3,6],[0,2,4,6],[0,2,3,5,6],[0,2,3,4,6],[0,2,3,4,6],[0,2,3,4,6],[0,2,3,4,6],[0,2,3,4,6],[0,3,6]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
Bb4:2 Db5:1 Eb5:2 Db5:1
F5:3 Eb5:1 Db5:2
Gb5:2 F5:1 Eb5:3
C5+F5:3 Bb4+Eb5:1 Ab4+Db5:2
F5:2 Ab5:1 G5:1 F5:2
Eb5:6
Db5:.25 Eb5:.25 F5:.25 Ab5:.25 Bb5:.25 Db6:.25 Eb6:.25 Db6:.25 Bb5:.25 Ab5:.25 F5:.25 Eb5:.25 Db5:3
R:6
F5:3 Eb5:1 Db5:2
G#5:2 F#5:1 E5:3
G5:2 F#5:1 E5:3
F5:3 E5:1 D5:2
F5:2 Eb5:1 Db5:3
Eb5:2 Db5:1 C5:3
C5+Db5+F5:6
''',
 rh_inner='''
F4:3 Ab4:3
Bb4:2 Ab4:2 Bb4:2
Bb4:3 Db5:3
R:6
C5:3 Db5:1 C5:2
A4:2 G4:2 Bb4:2
R:6
R:6
C5:2 Bb4:1 Ab4:3
B4:3 D#5:3
C#5:3 B4:3
A4:2 C5:1 B4:1 A4:2
Bb4:3 Ab4:3
A4:3 Gb4:1 F4:2
G4:6
''',
 lh='''
Bb2:2 F3:1 Ab3:1 C4:1 Bb3:1
Gb2:3 Db3:1 F3:2
Eb3:1 Bb3:2 Db4:1 Gb3:2
Ab2:2 Eb3:1 Gb3:1 Bb3:1 C4:1
Db3:2 Ab3:1 C4:1 Eb4:1 Db4:1
C3:2 G3:1 Bb3:1 E4:1 Eb4:1
R:6
Db3:1/3 Eb3:1/3 F3:1/3 Ab3:1/3 Bb3:1/3 Db4:1/3 Eb4:1/3 Db4:1/3 Bb3:1/3 Ab3:1/3 F3:1/3 Eb3:1/3 Db3:2
Bb2:2 F3:1 Ab3:2 C4:1
E3:2 B3:1 D#4:1 F#4:1 C#4:1
A2:2 E3:1 G3:1 B3:1 C#4:1
D3:2 A3:1 C4:1 E4:1 D4:1
Gb3:2 Db3:1 F3:1 Bb3:2
F3:2 C4:1 Eb4:1 Gb3:1 A3:1
Bb2:3 F3:3
''',sections={1:'p',2:'pp',3:'p',4:'mp',5:'p',6:'pp',7:'p',9:'pp',10:'p',11:'mp',12:'p',13:'pp',14:'p',15:'pp'},words={1:'poco rubato',14:'poco rit.'},
 slurs=[(1,6),(7,7),(9,9),(10,12),(13,15)],lower_phrases=[(1,4),(5,6),(8,9),(10,12),(13,15)],
 hairpins=[('crescendo',1,3),('diminuendo',4,6),('diminuendo',7,9),('crescendo',10,11),('diminuendo',12,13),('diminuendo',14,15)],tempo_changes={},group=2,
 performance=dict(rubato=[52,46,54,50,55,43,48,46,45,52,56,47,42,36,27],
  phrase_arcs=[[0,35.5,4],[36,53.5,2],[54,71.5,4],[72,90,-2]],
  lower_entries=[[6,12],[42,48],[72,78]],inner_entries=[[30,36],[66,72]],pedal_lift=.24,gate=.99,
  note='The upper sweep is briefly unaccompanied, and the lower answer takes more time to trace the same pitches. Silence in the other hand makes each register feel distinct. The returning harmony stays gentle, with a restrained inner voice and a final minor sixth/ninth that lingers rather than closes firmly.'))
,
dict(op=82,title='Teasel Parabola',key='f',fifths=-4,meter='7/8',bpm=55,
 description='Magnolia Interval’s opening bass becomes F–C–E-flat–G in an uneven, flowing melody. At the centre, one diminished-seventh chord remains held through four bars while the bass roots descend by minor thirds in pitch class: C, A, G-flat and E-flat. The same upper notes acquire four dominant flat-ninth meanings before resolving into A-flat minor. Brighter B-, E- and D-major reflections lead back to F minor sixth/ninth.',
 difficulty='Advanced sustained-chord reinterpretation and asymmetric phrasing',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Hold all four RH pitches in bars 9–12 for fourteen quarter beats without reattacking them. The bass changes the harmonic meaning of that diminished seventh, including enharmonic reinterpretations. Keep the chord finger-held through the pedal refreshes. The seven-eighth bars have varied internal groupings; follow the melodic phrase rather than stressing every bar line.',
 parent_opus=81,motif=dict(hand='rh',start_beat=0,end_beat=3.5,pitches=['F','C','Eb','G']),
 ancestry=dict(source_opus=81,source_hand='lh',source_voice='bass',source_start_beat=0,source_end_beat=5,source_pitches=['Bb','F','Ab','C'],transposition_semitones=7),
 system_starts=[1,5,9,13,17,21],page_starts=[13],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*3.5+left,(bar-1)*3.5+right-.2] for bar,cuts in enumerate([[0,1,1.5,2.5,3.5],[0,1.5,2.5,3.5],[0,2,2.5,3.5],[0,1,2.5,3.5],[0,1,2,2.5,3.5],[0,2,3,3.5],[0,.5,1.5,2.5,3.5],[0,1,1.5,2.5,3.5],[0,1.5,2.5,3.5],[0,2,2.5,3.5],[0,1.5,2.5,3.5],[0,1,2,2.5,3.5],[0,2,2.5,3.5],[0,1,1.5,2.5,3.5],[0,1,2,3.5],[0,1,1.5,2,3.5],[0,1,2,3.5],[0,1.5,2.5,3.5],[0,1,2,2.5,3.5],[0,1,1.5,2.5,3.5],[0,2,2.5,3.5],[0,1.5,2.5,3.5],[0,1,2,2.5,3.5],[0,3.5]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
F5:1 C5:1 Eb5:.5 G5:1
Ab5:1.5 G5:1 F5:1
G5:2 Eb5:.5 D5:1
F5:1.5 E5:.5 D5:1.5
G5:1 F5:1 Eb5:1.5
C5:2 Bb4:1 Ab4:.5
B4:1 Db5:1 D5:.5 F5:1
E5:1.5 Db5:1 C5:1
E4+G4+Bb4+Db5:3.5~
E4+G4+Bb4+Db5:3.5~
E4+G4+Bb4+Db5:3.5~
E4+G4+Bb4+Db5:3.5
Eb4+Ab4+Cb5:1.5 Eb5:1 Gb5:1
F#5:1.5 E5:1 D#5:1
G#5:2 F#5:.5 E5:1
F#5:1 E5:1.5 D5:1
F5:1.5 D5:1 Bb4:1
E5:1 F5:.5 G5:1.5 E5:.5
Ab5:2 G5:.5 F5:1
G5:1 F5:1 D5:1.5
F5:1 C5:1 Eb5:.5 G5:1
F5:1.5 Eb5:1 Db5:1
E4+G4+Bb4+Db5:2 C5:1 Bb4:.5
G4+Ab4+C5:3.5
''',
 lh='''
F3:1 C4:.5 Eb4:1 C4:1
Db3:1.5 Ab3:1 C4:1
C3:2 G3:.5 Bb3:1
Bb2:1 F3:1.5 Ab3:1
Eb3:1 Bb3:1 D4:.5 C4:1
Ab2:2 Eb3:1 G3:.5
G3:.5 D3:1 F3:1 B3:1
C3:1 G3:.5 Bb3:1 D4:1
C3:1.5 G3:1 Bb3:1
A2:2 E3:.5 G3:1
Gb2:1.5 Db3:1 Fb3:1
Eb3:1 Bb3:1 Db4:.5 Bb3:1
Ab2:2 Eb3:.5 Gb3:1
B2:1 F#3:.5 A#3:1 C#4:1
E3:1 B3:1 D#4:1.5
D3:1 A3:.5 C#4:.5 B3:1.5
G2:1 D3:1 Bb3:1.5
C3:1.5 G3:1 Bb3:1
F3:1 C4:1 Eb4:.5 C4:1
Bb2:1 F3:.5 Ab3:1 C4:1
F3:2 Ab3:.5 C4:1
Db3:1.5 Ab3:1 C4:1
C3:1 G3:1 Bb3:.5 E3:1
F3+D4:3.5
''',sections={1:'p',2:'pp',3:'p',4:'pp',5:'p',6:'pp',7:'mp',8:'p',9:'p',13:'pp',14:'p',15:'mp',16:'p',17:'pp',18:'p',19:'pp',20:'p',21:'pp',22:'p',23:'pp'},words={1:'poco rubato',23:'poco rit.'},
 slurs=[(1,4),(5,8),(9,13),(14,18),(19,24)],lower_phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],
 hairpins=[('diminuendo',1,4),('crescendo',5,7),('diminuendo',8,13),('crescendo',14,15),('diminuendo',16,17),('diminuendo',18,19),('diminuendo',20,24)],tempo_changes={},group=4,
 performance=dict(rubato=[55,49,54,46,53,44,56,47,48,44,42,40,49,51,55,48,50,54,46,51,45,41,34,25],
  phrase_arcs=[[0,13.5,3],[14,27.5,4],[28,45.5,-1],[45.5,62.5,4],[63,84,-2]],
  lower_entries=[[28,42],[56,59.5],[73.5,77]],pedal_lift=.2,gate=.99,
  note='The diminished chord is one sustained event, growing quieter while the bass gives it successive meanings. The pedal clears around each lower change without releasing those upper keys. Brighter reflections regain movement, and the final return settles into a compact minor sixth/ninth.'))
,
dict(op=83,title='Dahlia Overpass',key='c',fifths=-3,meter='6/4',bpm=55,
 description='A new branch from Velvet Estuary turns its opening intervals into G–B-flat–C–B-flat. Six upper quarter notes are answered one beat later, a perfect fifth below, by the RH inner voice. In the middle, the inner voice leads the same contour an octave lower and the upper voice answers a fifth above. Jazz-coloured C-minor, G-minor and brighter E-minor reflections lead towards a late-arriving ninth in the close.',
 difficulty='Advanced two-voice canons within one hand and independent bass',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 1–2 the RH inner voice echoes six upper notes one beat late and seven semitones lower. In bars 8–9 the inner voice leads, and the upper voice answers one beat late and seven semitones higher. Keep the two stem directions distinct, including their separate rests and releases. The widest combined RH span is an octave, reached briefly during the second canon.',
 parent_opus=2,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['G','Bb','C','Bb']),
 ancestry=dict(source_opus=2,source_hand='rh',source_start_beat=0,source_end_beat=4.5,source_pitches=['A','C','D','C'],transposition_semitones=-2),
 system_starts=[1,3,5,7,8,10,12],page_starts=[8],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*6+left,(bar-1)*6+right-.22] for bar,cuts in enumerate([[0,2,4,6],[0,2,4,6],[0,2,3,4,6],[0,1,3,4,6],[0,2,3,4,6],[0,2,3,4,6],[0,2,3,4,5,6],[0,2,3,4,5,6],[0,2,3,4,6],[0,1,3,4,6],[0,2,3,4,5,6],[0,2,3,4,5,6],[0,2,3,4,5,6],[0,3,6]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
G5:1 Bb5:1 C6:1 Bb5:1 F5:1 D5:1
E5:2 D5:2 Bb4:2
G5:3 F5:1 Eb5:2
F5:2 Eb5:1 D5:3
Bb5:2 A5:1 G5:3
G5:1 Ab5:2 F5:1 Eb5:2
F5:3 D5:1 C5:2
R:1 D5:1 F5:1 G5:1 F5:1 C5:1
A4:1 C5:2 D5:1 F5:2
E5:3 D5:1 B4:2
F#5:2 E5:1 D5:3
Eb5:3 D5:1 C5:2
F5:2 Eb5:1 Db5:3
C5+Eb5:6
''',
 rh_inner='''
R:1 C5:1 Eb5:1 F5:1 Eb5:1 Bb4:1
G4:1 R:1 G4:2 F4:2
Bb4:2 C5:1 Bb4:1 G4:2
A4:3 C5:1 Bb4:2
D5:2 C5:1 Bb4:3
C5:3 D5:1 C5:2
Bb4:2 A4:1 G4:3
G4:1 Bb4:1 C5:1 Bb4:1 F4:1 D4:1
F4:2 E4:2 A4:2
A4:2 G4:2 F#4:2
B4:2 A4:1 G4:3
Bb4:2 Ab4:2 G4:2
B4:2 Bb4:1 G4:3
A4:6
''',
 lh='''
C3:2 G3:1 Bb3:1 D4:1 C4:1
F3:2 C4:1 Eb4:1 Bb3:2
Ab2:2 Eb3:1 G3:1 Bb3:2
D3:1 A3:2 C4:1 F#3:2
G2:3 D3:1 F3:2
Eb3:2 Bb3:1 Db4:1 C4:2
C3:2 G3:1 Bb3:1 D4:1 C4:1
G2:2 D3:1 F3:1 A3:1 Bb3:1
F3:2 C4:1 D4:1 C4:2
E3:1 B3:2 D4:1 C4:2
B2:2 F#3:1 A3:1 B3:2
Ab2:2 Eb3:1 Gb3:1 Bb3:1 C4:1
G2:2 D3:1 F3:1 Ab3:1 B3:1
C3:3 G3+D4:3
''',sections={1:'p',2:'pp',3:'p',4:'mp',5:'pp',6:'p',7:'pp',8:'p',9:'pp',10:'p',11:'mp',12:'pp',13:'p',14:'pp'},words={1:'poco rubato',13:'poco rit.'},
 slurs=[(1,3),(4,7),(8,10),(11,14)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,14)],
 hairpins=[('diminuendo',1,2),('crescendo',3,4),('diminuendo',5,7),('diminuendo',8,9),('crescendo',10,11),('diminuendo',12,14)],tempo_changes={},group=2,
 performance=dict(rubato=[55,48,51,56,46,54,43,50,47,51,55,45,37,27],
  phrase_arcs=[[0,17.5,3],[18,41.5,4],[42,59.5,3],[60,84,-2]],
  lower_entries=[[12,18],[36,42],[66,72]],inner_entries=[[1,7],[42,48]],pedal_lift=.22,gate=.99,
  note='The answering voice emerges gently without obscuring its leader. At the second canon the roles exchange: the lower RH line leads and the upper line enters after a breath. The independent bass shapes the harmony beneath both, and the last ninth arrives only after the upper sixth has settled.'))
,
dict(op=84,title='Celandine Spire',key='d',fifths=-1,meter='3/4',bpm=54,
 meters=['3/4','4/4','5/4','3/4','4/4','6/4','3/4','5/4','4/4','3/4','5/4','4/4','3/4','6/4','4/4','5/4','3/4','4/4'],
 description='Dahlia Overpass’s opening intervals become A–C–D–C within a seven-note sweep. Three seven-against-two crossings each fill a three-beat bar, followed by longer, quieter harmonies. The changing bar lengths let the phrases settle at different distances. B-flat Lydian and A-minor colours, an altered D-flat dominant and a soft A-dominant approach return to D minor with an added ninth.',
 difficulty='Advanced 7:6 eighth-note groups and changing phrase lengths',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 1, 7 and 13, seven RH eighth notes fill the time of six ordinary eighths. The LH plays two dotted quarters over the same three beats. The 7:6 brackets state that relationship explicitly. Let each group arrive as a single contour, then give the following longer bar time to settle. The four-note closing RH shape spans a major seventh.',
 parent_opus=83,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','C','D','C']),
 ancestry=dict(source_opus=83,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4,source_pitches=['G','Bb','C','Bb'],transposition_semitones=2),
 tuplet_groups=[dict(hand='rh',actual=7,normal=6,count=21)],
 tuplet_spans=[dict(hand='rh',start_beat=start,end_beat=start+3,actual=7,normal=6,stem='down',show_number='both') for start in [0,25,49]],
 polyrhythms=[dict(start_beat=start,end_beat=start+3,rh_notes=7,lh_notes=2) for start in [0,25,49]],
 system_starts=[1,3,5,7,9,11,13,15,17],page_starts=[11],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[start+left,start+right-.22] for start,cuts in zip([0,3,7,12,15,19,25,28,33,37,40,45,49,52,58,62,67,70],[[0,1.5,3],[0,2,3,4],[0,1,2,3,5],[0,1,2,3],[0,1,2,3,4],[0,2,3,4,6],[0,1.5,3],[0,1,2,3,5],[0,2,3,4],[0,1,2,3],[0,2,3,4,5],[0,1,2,3,4],[0,1.5,3],[0,2,3,4,5,6],[0,1,2,3,4],[0,2,3,4,5],[0,1,2,3],[0,4]]) for left,right in zip(cuts,cuts[1:])],
 rh='''
A5:3/7 C6:3/7 D6:3/7 C6:3/7 A5:3/7 F5:3/7 E5:3/7
F5:4
E5:2 D5:1 C5:2
D5+G5:2 C5+F5:1
E5:1.5 G5:1 F5:1.5
D5+F5+A5:3 G5:1 E5:2
C6:3/7 Bb5:3/7 A5:3/7 G5:3/7 F5:3/7 E5:3/7 D5:3/7
C5+F5+A5:3 G5:1 F5:1
E5:2 D5:1 B4:1
C5+E5+G5:3
D5:1 F5:2 E5:1 Cb5:1
C5:2 B4:1 A4:1
E5:3/7 G5:3/7 A5:3/7 G5:3/7 E5:3/7 C5:3/7 B4:3/7
C5+E5+G5:4 F5:1 E5:1
F5:1.5 E5:.5 D5:2
G5:2 F5:1 E5:2
G4+Bb4+C#5+E5:3
F4+A4+D5+E5:4
''',
 lh='''
D3:1.5 A3:1.5
Bb2:2 F3:1 A3:1
G3:1 D3:1 F3:1 A3:2
C3:1 G3:1 Bb3:1
A2:1 E3:1 G3:1 C#4:1
D3:2 A3:1 C4:1 E4:1 D4:1
Bb2:1.5 F3:1.5
F3:1 C4:1 E4:1 D4:2
E3:2 B3:1 D4:1
C3:1 G3:1 B3:1
Db3:2 Ab3:1 Cb4:1 Bb3:1
C3:1 G3:1 B3:1 D4:1
A2:1.5 E3:1.5
A2:2 E3:1 G3:1 B3:1 C4:1
D3:1 A3:1 C4:1 B3:1
G2:2 D3:1 F3:1 B3:1
A2:1 E3:1 G3:1
D3+A3:4
''',sections={1:'p',2:'pp',3:'p',4:'mp',5:'p',6:'pp',7:'p',8:'pp',9:'p',10:'pp',11:'mp',12:'pp',13:'p',14:'pp',15:'p',16:'p',17:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,4),(5,8),(9,12),(13,18)],lower_phrases=[(1,4),(5,8),(9,12),(13,15),(16,18)],
 hairpins=[('diminuendo',1,2),('crescendo',3,4),('diminuendo',5,6),('diminuendo',7,8),('diminuendo',9,10),('diminuendo',11,12),('diminuendo',13,14),('diminuendo',15,18)],tempo_changes={},group=2,
 performance=dict(rubato=[54,44,50,56,49,42,53,43,50,42,55,44,50,41,47,42,34,26],
  phrase_arcs=[[0,14.5,3],[15,32.5,4],[33,48.5,3],[49,74,-2]],
  lower_entries=[[7,12],[33,37],[45,49],[58,62]],pedal_lift=.22,gate=.99,
  note='Each seven-note gesture floats across two lower pulses. Longer following bars relax the motion. The final dominant loses weight before the added-ninth minor close.'))
,
dict(op=85,title='Yarrow Elevation',key='f#',fifths=3,meter='5/4',bpm=52,
 meters=['5/4','4/4','6/4','3/4','5/4','4/4','7/4','3/4','6/4','3/4','7/4','4/4','5/4','3/4','6/4','4/4','5/4','6/4'],
 description='Celandine Spire’s opening contour becomes F-sharp–A–B–A. Eight sustained chord fields lead outwards from F-sharp minor to a central D-flat-major reflection, then return in exact reverse order and at the same lengths. The melody takes a different route on the return. A separate coda adds sixth and ninth colours to F-sharp minor.',
 difficulty='Experimental harmonic form and voicing; moderate physical demands',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Bars 1–17 form a palindrome in the LH chord pitches and their durations, with bar 9 at its centre. The melody is newly shaped on the return rather than reversed. Keep each three-note LH chord finger-held through the pedal changes, and let the changing metres follow the phrase. The final RH chord spans a major seventh; all earlier LH shapes fit within a fifth.',
 parent_opus=84,motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['F#','A','B','A']),
 ancestry=dict(source_opus=84,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','C','D','C'],transposition_semitones=-3),
 system_starts=[1,3,5,7,9,11,13,15,17],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[start+left,start+right-.25] for start,cuts in zip([0,5,9,15,18,23,27,34,37,43,46,53,57,62,65,71,75,80],[[0,2,3,5],[0,2,3,4],[0,1.5,3,6],[0,.5,2,3],[0,2,3,5],[0,2,4],[0,2,4,7],[0,1,2,3],[0,2,6],[0,1.5,2,3],[0,3,4,7],[0,2,4],[0,2,3,5],[0,1,1.5,3],[0,2,3,6],[0,1.5,2,4],[0,5],[0,6]]) for left,right in zip(cuts,cuts[1:])],
 rh='''
F#5:1.5 A5:.5 B5:1 A5:2
C#5:2 E5:1 F#5:1
A4:1.5 C#5:1.5 D5:3
E5:.5 F#5:1.5 A5:1
D5:2 F5:.5 G5:.5 C5:2
D5:1 F5:1 A5:2
G5:1.5 B5:.5 E5:2 D5:3
E5:1 G5:1 Bb5:1
C6:1 Bb5:1 Ab5:4
G5:1.5 E5:.5 D5:1
C5:3 B4:1 G4:3
A4:1 C5:1 D5:2
Bb4:2 G4:1 F4:2
A4:1 G4:.5 F#4:1.5
E4:2 F#4:1 A4:3
C#5:1.5 B4:.5 A4:2
G#4+B4+E5:5
A4+C#5+D#5+G#5:6
''',
 lh='''
F#3+A3+C#4:5
D3+F#3+A3:4
B2+D3+F#3:6
G3+B3+D4:3
Eb3+G3+Bb3:5
C3+Eb3+G3:4
A2+C3+E3:7
F3+A3+C4:3
Db3+F3+Ab3:6
F3+A3+C4:3
A2+C3+E3:7
C3+Eb3+G3:4
Eb3+G3+Bb3:5
G3+B3+D4:3
B2+D3+F#3:6
D3+F#3+A3:4
F#3+A3+C#4:5
F#3+C#4:6
''',sections={1:'p',2:'pp',3:'p',4:'mp',5:'p',6:'pp',7:'p',8:'mp',9:'pp',10:'p',11:'pp',12:'p',13:'mp',14:'p',15:'pp',16:'p',17:'pp',18:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,4),(5,9),(10,13),(14,18)],lower_phrases=[],
 hairpins=[('crescendo',1,3),('diminuendo',4,6),('crescendo',7,8),('diminuendo',9,11),('crescendo',12,14),('diminuendo',15,18)],tempo_changes={},group=2,
 performance=dict(rubato=[52,47,54,49,51,45,56,48,40,46,52,43,49,44,46,38,32,24],
  phrase_arcs=[[0,17.5,3],[18,42.5,4],[43,61.5,3],[62,86,-2]],
  lower_entries=[[37,43],[75,80]],pedal_lift=.25,gate=.995,
  note='The chord fields remain quiet and sustained while the melody changes its sense of direction. Returning harmonies have different upper colours and gentler phrase endings. Pedal refreshes clear the melody while the lower keys stay held, and the separate coda lets the minor sixth/ninth settle slowly.'))
,
dict(op=86,title='Eglantine Terrace',key='Bb',fifths=-2,meter='4/4',bpm=52,
 description='Yarrow Elevation’s opening contour enters the tenor as F–A-flat–B-flat–A-flat. Across eight bars, the upper melody rises from D5 to D6 while the bass falls chromatically from B-flat2 to E-flat2. Two inner voices give those opposite motions changing jazz colours. F-sharp-minor and B-major reflections interrupt the return before a late major seventh completes the B-flat-major thirteenth close.',
 difficulty='Advanced four-voice control over opposing sustained lines',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The first eight upper notes each last a whole bar while the bass descends by semitone at every bar line. Keep both outer lines sustained and voice the shorter inner notes softly. The opening LH tenor briefly reaches an octave above the finger-held bass; later LH spans remain within a major seventh. The final upper chord and inner G stay held while the tenor moves from F to A.',
 parent_opus=85,motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=4,pitches=['F','Ab','Bb','Ab']),
 ancestry=dict(source_opus=85,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['F#','A','B','A'],transposition_semitones=-1),
 system_starts=[1,4,7,10,13,16],page_starts=[10],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[(bar-1)*4+left,(bar-1)*4+right-.24] for bar,cuts in enumerate([[0,1,2,3,4],[0,2,3,4],[0,1,2,3,4],[0,2,3,4],[0,1,2,4],[0,2,3,4],[0,2,3,4],[0,1,2,3,4],[0,2,4],[0,2,3,4],[0,2,3,4],[0,1,2,4],[0,2,3,4],[0,1,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,1,2,4],[0,2,4]],1) for left,right in zip(cuts,cuts[1:])],
 rh='''
D5:4
Eb5:4
F5:4
G5:4
A5:4
Bb5:4
C6:4
D6:4
C6:2 Bb5:2
Ab5:3 F5:1
E5:2 F#5:1 A5:1
G#5:2 F#5:2
Gb5:2 F5:1 Eb5:1
G5:2 F5:1 Eb5:1
F5:2 Eb5:1 D5:1
E5:2 D5:1 C5:1
Eb5:2 Db5:1 Bb4:1
D5:2 C5:2
C5+D5+F5:4
''',
 rh_inner='''
F4:2 G4:2
G4:2 F4:1 E4:1
Bb4:3 C5:1
B4:2 D5:2
C#5:2 D#5:2
D5:2 F5:2
E5:2 G5:2
F5:1 G5:1 Bb5:2
Eb5:2 F5:2
C5:2 Db5:2
C#5:2 D5:1 E5:1
D#5:2 C#5:2
Bb4:2 C5:1 Db5:1
C5:2 Bb4:2
A4:2 G4:1 F4:1
Bb4:2 A4:1 G4:1
Gb4:2 F4:1 Eb4:1
A4:2 Eb4:2
G4:4
''',
 lh='''
Bb2:4
A2:4
Ab2:4
G2:4
F#2:4
F2:4
E2:4
Eb2:4
Ab2:4
Db3:4
F#2:4
B2:4
Eb3:4
Ab2:4
Bb2:4
G2:4
Eb3:4
F2:4
Bb2:4
''',
 lh_upper='''
F3:1 Ab3:1 Bb3:1 Ab3:1
E3:2 F#3:2
Eb3:1 F3:1 G3:2
D3:2 E3:1 F3:1
C#3:1 D#3:1 E3:2
C3:2 D3:1 Eb3:1
B2:2 C3:1 D3:1
Bb2:2 C3:1 D3:1
Eb3:2 G3:2
Ab3:2 Bb3:1 C4:1
C#3:2 D#3:1 E3:1
F#3:1 G#3:1 A#3:2
Gb3:2 Ab3:1 Bb3:1
Eb3:1 Gb3:1 F3:2
F3:2 G3:1 A3:1
D3:2 E3:1 F3:1
Gb3:2 Ab3:1 Bb3:1
C3:1 D3:1 Eb3:2
F3:2 A3:2
''',sections={1:'p',2:'p',3:'p',4:'mp',5:'pp',6:'p',7:'p',8:'mp',9:'pp',10:'p',11:'pp',12:'mp',13:'p',14:'p',15:'pp',16:'p',17:'pp',18:'p',19:'pp'},words={1:'poco rubato',18:'poco rit.'},
 slurs=[(1,8),(9,13),(14,19)],lower_phrases=[],
 hairpins=[('crescendo',1,4),('crescendo',5,8),('diminuendo',9,11),('diminuendo',12,15),('diminuendo',16,19)],tempo_changes={},group=3,
 performance=dict(rubato=[52,48,55,50,46,53,44,57,43,51,48,54,46,50,45,49,40,35,26],
  phrase_arcs=[[0,15.5,3],[16,31.5,4],[32,51.5,3],[52,76,-2]],
  lower_entries=[[0,32],[64,72]],inner_entries=[[8,16],[40,48]],tenor_entries=[[0,4],[32,40],[72,76]],pedal_lift=.24,gate=.995,
  note='The outer lines take opposite directions over eight long notes, while the middle voices move quietly inside them. The ascending melody grows gradually brighter as the low bass recedes. Later harmonic reflections relax the register, and the last tenor A arrives gently under an already held upper harmony.'))
,
dict(op=87,title='Verbena Switchyard',key='g#',fifths=5,meter='7/4',bpm=53,
 meters=['7/4','4/4','5/4','3/4','6/4','4/4','7/8','5/4','4/4','6/4','3/4','5/4','7/4','7/4','4/4','5/4','3/4','6/4'],
 description='Eglantine Terrace’s tenor contour becomes G-sharp–B–C-sharp–B at the start of a seven-note phrase. Its quarter notes return two octaves lower as eighths in the bass, then one octave lower as two-beat notes in the RH inner voice. Each version has different surrounding harmonies. D-major, D-flat-major and D-minor reflections open the G-sharp-minor centre before a sixth/ninth close.',
 difficulty='Advanced thematic compression and augmentation across three voices',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The seven-note opening occupies seven quarter beats. Bar 7 gives the same pitches two octaves lower in seven eighth notes. Bars 13–14 place them one octave below the opening in seven two-beat inner-voice notes; the B is tied across their bar line. Keep that slower inner phrase distinct from the upper line. The D-sharp dominant in bar 17 uses F-double-sharp as its major third.',
 parent_opus=86,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['G#','B','C#','B']),
 ancestry=dict(source_opus=86,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=4,source_pitches=['F','Ab','Bb','Ab'],transposition_semitones=3),
 system_starts=[1,3,5,7,9,11,13,15,17],page_starts=[9],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[start+left,start+right-.23] for start,cuts in zip([0,7,11,16,19,25,29,32.5,37.5,41.5,47.5,50.5,55.5,62.5,69.5,73.5,78.5,81.5],[[0,2,3,4,5,7],[0,2,3,4],[0,2,3,4,5],[0,1,2,3],[0,2,3,4,6],[0,1,2,3,4],[0,1.5,2.5,3.5],[0,2,3,4,5],[0,1,2,3,4],[0,2,3,4,6],[0,1,2,3],[0,2,3,4,5],[0,2,3,4,5,6,7],[0,1,2,3,4,5,7],[0,1,2,3,4],[0,2,3,4,5],[0,1,2,3],[0,3,6]]) for left,right in zip(cuts,cuts[1:])],
 rh='''
G#5:1 B5:1 C#6:1 B5:1 F#5:1 D#5:1 C#5:1
D#5:2 C#5:1 B4:1
E5:3 D#5:1 C#5:1
F#5:1 E5:1 D5:1
F5:2 Eb5:1 Db5:3
E5:2 D#5:1 B4:1
B4:3.5
D#5:2 F#5:1 E5:2
C#5:2 B4:1 A#4:1
D5:2 F5:1 A5:3
G5:1 F5:1 Eb5:1
F#5:2 E5:1 D#5:2
F#5:4 E5:3
D#5:3 B4:2 G#4:2
B4:2 C#5:1 D#5:1
E5:2 D#5:1 C#5:2
F##4+A#4+C#5+E5:3
B4+D#5+E#5+A#5:6
''',
 rh_inner='''
R:7
G#4:2 F#4:1 E4:1
A4:3 B4:2
A4:2 G4:1
Ab4:3 C5:3
G#4:2 F#4:2
F#4:3.5
B4:3 G#4:2
G#4:2 F#4:2
A4:2 C5:1 D5:3
Bb4:2 Ab4:1
A#4:3 C#5:2
G#4:2 B4:2 C#5:2 B4:1~
B4:1 F#4:2 D#4:2 C#4:2
G#4:2 A#4:1 B4:1
A4:2 G#4:1 F#4:2
R:3
R:6
''',
 lh='''
G#2:2 D#3:1 F#3:1 B3:1 C#4:1 B3:1
E3:2 B3:1 C#4:1
A2:2 E3:1 G#3:1 B3:1
D3:1 A3:1 C#4:1
Db3:2 Ab3:1 C4:1 Eb4:1 Db4:1
E3:1 B3:1 D#4:1 C#4:1
G#3:.5 B3:.5 C#4:.5 B3:.5 F#3:.5 D#3:.5 C#3:.5
G#2:2 D#3:1 F#3:1 A#3:1
C#3:1 G#3:1 B3:1 D#4:1
D3:2 A3:1 C4:1 E4:1 D4:1
Eb3:1 Bb3:1 Db4:1
B2:2 F#3:1 A#3:1 C#4:1
G#2:3 D#3:2 F#3:2
C#3:2 G#3:1 B3:1 A#3:1 G#3:2
E3:1 B3:1 D#4:1 F#3:1
A2:2 E3:1 G#3:1 B3:1
D#3:1 A#3:1 C#4:1
G#2:3 D#3:3
''',sections={1:'p',2:'pp',3:'mp',4:'p',5:'p',6:'pp',7:'p',8:'pp',9:'p',10:'p',11:'mp',12:'pp',13:'p',14:'pp',15:'p',16:'pp',17:'p',18:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,6),(7,12),(13,18)],lower_phrases=[(1,4),(5,8),(9,12),(13,16),(17,18)],
 hairpins=[('crescendo',1,3),('diminuendo',4,6),('diminuendo',7,9),('crescendo',10,11),('diminuendo',12,14),('diminuendo',15,18)],tempo_changes={},group=2,
 performance=dict(rubato=[53,47,54,50,52,43,56,46,48,55,51,45,49,43,46,40,33,25],
  phrase_arcs=[[0,28.5,4],[29,50,3],[50.5,69,2],[69.5,87.5,-2]],
  lower_entries=[[29,32.5],[41.5,47.5]],inner_entries=[[55.5,69.5]],pedal_lift=.23,gate=.99,
  note='The bass compresses the opening phrase into a light passing memory. Later, the same contour unfolds slowly in the inner voice while the upper notes take another route. The three note-value scales remain connected through voicing and phrase rubato, and the final minor sixth/ninth is kept quiet.'))
]
