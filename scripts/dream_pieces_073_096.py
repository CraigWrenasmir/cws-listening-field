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
]
