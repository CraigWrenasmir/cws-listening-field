"""Individually composed studies for Volume 03, Op. 49–72."""
PIECES=[
dict(op=49,title='Dew Pavilion',key='D',fifths=2,meter='4/4',bpm=56,
 description='Thistle Horizon’s inner line becomes A–D–E–C-sharp in a new left-hand tenor voice. Two independent lines now share each hand. The tenor opening moves beneath a sustained upper D; B-flat and D-flat reflections later lead through C and G before a quiet D-major sixth/ninth close. Half-bar pedal changes let the moving voices clear while held notes continue.',
 difficulty='Advanced four-voice counterpoint',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Each hand carries two independently notated voices. The opening tenor phrase needs to sing above the bass while the right hand sustains its melody. Bass changes keep the moving tenor within an octave of the held lower note. Printed half-bar pedal changes require finger sustain across the refreshes; the left-hand span reaches an octave.',
 parent_opus=48,motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=4,pitches=['A','D','E','C#']),
 ancestry=dict(source_opus=48,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=5,source_pitches=['B','E','F#','D#'],transposition_semitones=10),
 pedal_spans=[[i*2,i*2+1.78] for i in range(32)],
 rh='''
D5:4
C#5:2 B4:2
E5:3 D5:1
C#5:4
D5:2 F5:2
Eb5:3 Db5:1
E5:4
F#5:2 E5:2
G5:3 F#5:1
E5:2 D5:2
C5:3 Bb4:1
B4:4
D5:3 C#5:1
B4:2 A4:2
G4:3 E4:1
F#4:4
''',
 rh_inner='''
F#4:1 A4:1 B4:1 A4:1
E4:1 G4:.5 A4:.5 G4:2
G4:1 B4:1 C#5:2
F#4:1 A4:1 B4:1 G4:1
F4:2 A4:.5 C5:.5 Bb4:1
F4:1 Ab4:1 Bb4:.5 Ab4:1.5
G4:1 B4:1 D5:1 C5:1
A4:1 C5:1 D5:2
B4:1 D5:1 E5:.5 D5:1.5
G4:1 B4:.5 C5:.5 A4:2
E4:1 G4:1 A4:1 G4:1
D4:1 F#4:1 A4:.5 G4:1.5
F#4:1 A4:.5 B4:.5 E4:2
D4:1 G4:1.5 F#4:1.5
C#4:1 E4:1 F#4:.5 D4:1.5
D4:2 E4:2
''',
 lh='''
D3:2 F#3:2
A2:2 C#3:2
G2:2 B2:2
A2:2 C#3:2
Bb2:2 D3:2
Db3:2 F3:2
C3:1.5 E3:.5 G3:2
D3:2 F#3:2
G2:2 B2:2
E3:3 B2:1
F2:2 A2:2
G2:2 B2:2
B2:2 D3:2
E3:2 G3:2
A2:2 C#3:2
D3:4
''',
 lh_upper='''
A3:1 D4:1 E4:1 C#4:1
E3:1 G3:1 B3:1 A3:1
D3:1 F#3:1 A3:1 G3:1
E3:1 G3:.5 F#3:.5 G3:2
F3:1 A3:1 C4:.5 Bb3:1.5
Ab3:1 C4:1 Eb4:.5 Db4:1.5
G3:1 B3:.5 A3:.5 D4:2
A3:1 C4:.5 B3:.5 E4:2
D3:1.5 F#3:.5 A3:.5 G3:1.5
B3:1 D4:.5 C4:.5 F#3:2
C3:1 E3:.5 D3:.5 G3:1 F3:1
D3:1 F#3:1 A3:.5 G3:1.5
F#3:1 A3:1 C#4:.5 B3:1.5
B3:1 D4:1 F#4:.5 E4:1.5
E3:1 G3:1 Bb3:.5 A3:1.5
A3:2 B3:2
''',sections={1:'p',3:'mp',4:'pp',5:'p',6:'mp',7:'pp',8:'p',9:'mp',10:'p',12:'pp',13:'p',15:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,4),(5,7),(8,12),(13,16)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,16)],
 hairpins=[('crescendo',1,3),('diminuendo',3,4),('crescendo',5,6),('diminuendo',6,7),('crescendo',8,9),('diminuendo',9,12),('diminuendo',13,16)],tempo_changes={},group=4,
 performance=dict(rubato=[56,53,59,48,54,58,49,55,60,54,51,46,52,47,41,33],
  phrase_arcs=[[0,15,3],[16,27,4],[28,47,4],[48,64,-2]],
  lower_entries=[[16,20],[40,44],[56,64]],tenor_entries=[[0,4],[28,32],[52,56]],pedal_lift=.22,gate=.995,
  note='The tenor is slightly more present at its opening and later answers, while the bass stays lighter. Held keys preserve the longer lines through each pedal refresh. The final four-bar phrase withdraws into a close, quiet sixth/ninth sonority.'))
,
dict(op=50,title='Mica Understory',key='F',fifths=-1,meter='6/4',bpm=57,
 engraving=dict(spacing_system=13,pedal_offset_y=420),
 description='Dew Pavilion’s tenor phrase moves into the treble as C–F–G–E. A sustained bass and a separately moving tenor share the left hand beneath it. Two quintuplet gestures open and fold back, first in bright F-major colour and later over D-flat. E-flat and E-major reflections lead through a borrowed F-minor passage to a quiet, richly added F-major close.',
 difficulty='Advanced lower-voice independence',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The left hand sustains the bass while shaping a distinct tenor line with upward stems. Half-bar pedal changes must preserve the held keys. The right hand alternates sustained voicings with two groups of five quarter-note quintuplets across four beats. Balance the moving tenor beneath the melody without losing the bass.',
 tuplet_groups=[dict(hand='rh',actual=5,normal=4,count=10)],
 parent_opus=49,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=6,pitches=['C','F','G','E']),
 ancestry=dict(source_opus=49,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=4,source_pitches=['A','D','E','C#'],transposition_semitones=3),
 pedal_spans=[[i*3,i*3+2.77] for i in range(32)],
 rh='''
C5:1 F5:1 G5:1 E5:3
D5:2 C5:.5 A4:.5 G4:1 A4:2
Bb4+D5+A5:3 G5:1 F5:1 E5:1
C5+E5+Bb5:2 A5:1 G5:.5 F5:.5 E5:2
F5:4/5 A5:4/5 C6:4/5 B5:4/5 G5:4/5 A5:2
G5:2 F5:.5 E5:.5 D5:1 C5:2
Eb5+G5+D6:3 C6:1 Bb5:1 G5:1
F#5:2 E5:1 D#5:1 B4:2
E5+G#5+D#6:3 C#6:1 B5:.5 G#5:.5 F#5:1
F5:4/5 Eb5:4/5 Db5:4/5 C5:4/5 Ab4:4/5 Bb4:2
A4+C5+G5:3 F5:1 E5:1 D5:1
G4+B4+F5:2 E5:1 D5:.5 C5:.5 B4:2
E4+G4+D5:3 E5:1 G5:2
F5:1 Eb5:.5 C5:.5 Bb4:1 Ab4:3
G4+Bb4+E5:3 D5:1 C5:1 Bb4:1
A4:2 G4:1 E4+G4+A4:3
''',
 lh='''
F3:6
D3:3 F3:3
Bb2:2 D3:4
C3:2 E3:4
F3:6
A2:2 C3:4
Eb3:2 G3:4
B2:2 D#3:4
E3:6
Db3:2 F3:4
D3:6
G2:2 B2:4
C3:2 E3:4
F3:2 Ab3:4
C3:2 E3:4
F3:6
''',
 lh_upper='''
A3:1 C4:1 D4:1 C4:3
A3:1 C4:2 B3:.5 A3:2.5
F3:1.5 A3:.5 C4:1 Bb3:3
G3:1 Bb3:1 D4:1 C4:3
A3:2 C4:.5 D4:.5 E4:1 D4:2
E3:1 G3:.5 F3:.5 A3:2 G3:2
Bb3:1 D4:.5 C4:.5 F4:1 Eb4:3
F#3:1 A#3:1 C#4:1 B3:3
G#3:1 B3:1 C#4:2 D#4:2
Ab3:1 C4:1 Eb4:1 Db4:3
F3:1 A3:.5 C4:.5 B3:1 A3:3
D3:1 F3:1 A3:1 G3:3
G3:1 B3:.5 A3:.5 D4:1 C4:3
C4:1 Eb4:.5 D4:.5 G4:1 F4:3
G3:1 Bb3:1 D4:1 C4:3
A3:2 C4:1 D4:3
''',sections={1:'p',3:'mp',5:'p',6:'pp',7:'mp',8:'p',9:'mp',10:'pp',11:'p',13:'mp',14:'p',15:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,4),(5,8),(9,13),(14,16)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,16)],
 hairpins=[('crescendo',1,3),('diminuendo',3,4),('diminuendo',5,6),('crescendo',6,7),('diminuendo',7,8),('diminuendo',9,10),('crescendo',11,13),('diminuendo',14,16)],tempo_changes={},group=4,
 performance=dict(rubato=[57,54,59,51,60,48,58,51,59,49,54,57,60,49,43,33],
  phrase_arcs=[[0,23,3],[24,47,4],[48,77,4],[78,96,-2]],
  lower_entries=[[0,6],[30,36],[60,66],[90,96]],tenor_entries=[[6,12],[36,42],[60,66],[78,84]],pedal_lift=.23,gate=.995,
  note='The bass remains quietly held while the tenor takes small breaths. The two quintuplet figures form broad gestures above that slower movement. Each pedal refresh clears the passing harmony without cutting the sustained voice, and the closing minor colour softens into the last major sonority.'))
,
dict(op=51,title='Pewter Lagoon',key='c',fifths=-3,meter='5/4',bpm=56,
 description='A tenor fragment from Mica Understory becomes C–E-flat–F–G in the upper melody. Four independent voices gather around it. Twice the left-hand tenor moves in five-note groups while the bass remains held, opening first into C-major light and later into A-flat. The return passes through a soft altered dominant and settles into C minor with an added sixth.',
 difficulty='Advanced four-voice quintuplet study',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 4 and 10, the LH tenor plays five quarter-note quintuplets across four beats while the bass stays held. The bass changes on the fifth beat to support the tenor’s arrival. Both RH voices continue independently. Keep the tenor even without accenting each note; finger sustain preserves the bass through pedal changes.',
 tuplet_groups=[dict(hand='lh',actual=5,normal=4,count=10)],
 parent_opus=50,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=5,pitches=['C','Eb','F','G']),
 ancestry=dict(source_opus=50,source_hand='lh',source_voice='tenor',source_start_beat=24,source_end_beat=28,source_pitches=['A','C','D','E'],transposition_semitones=3),
 page_starts=[10],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[span for i in range(15) for span in [[i*5,i*5+1.78],[i*5+2,i*5+4.78]]],
 rh='''
C5:1 Eb5:.5 F5:.5 G5:3
F5:3 Eb5:2
D5:2 C5:3
E5:5
D5:3 C5:2
F5:3 E5:2
G5:2 F5:3
E5:3 D5:2
Db5:5
C5:5
Bb4:2 C5:3
D5:3 C5:2
B4:3 A4:2
Ab4:3 G4:2
G4:5
''',
 rh_inner='''
G4:1 Bb4:.5 C5:.5 Eb5:3
Ab4:1 C5:1 Db5:1 C5:2
F4:1 Ab4:.5 Bb4:.5 A4:1 G4:2
G4:1 A4:1 B4:1 D5:2
F4:1 A4:.5 C5:.5 B4:1 A4:2
A4:1 C5:1 D5:1 C5:2
Bb4:1 D5:.5 Eb5:.5 C5:1 Bb4:2
G4:1 B4:1 C5:.5 B4:.5 A4:2
F4:1 Ab4:.5 Bb4:.5 C5:1 Bb4:2
Eb4:1 F4:1 G4:1 Bb4:2
Eb4:1 G4:.5 Ab4:.5 F4:1 G4:2
F#4:1 A4:1 B4:1 A4:2
D4:1 G4:.5 A4:.5 G4:1 F4:2
D4:1 F4:1 Eb4:1 D4:2
Eb4:2 D4:1 Eb4:2
''',
 lh='''
C3:2 Eb3:3
F3:5
Bb2:2 D3:3
C3:4 E3:1
D3:3 F3:2
F3:5
Eb3:2 G3:3
C3:2 E3:3
Db3:2 F3:3
Ab2:4 C3:1
F3:5
D3:2 F#3:3
G2:2 B2:3
G2:2 B2:3
C3:5
''',
 lh_upper='''
G3:1 Bb3:1 D4:1 C4:2
Ab3:1 C4:.5 Eb4:.5 D4:1 C4:2
F3:1 Ab3:1 C4:.5 Bb3:2.5
E3:4/5 G3:4/5 A3:4/5 B3:4/5 C4:4/5 D4:1
F3:1 A3:1 C4:1 E4:1 D4:1
A3:1 C4:1 E4:.5 D4:2.5
Bb3:1 D4:1 F4:1 Eb4:2
G3:1 B3:.5 A3:.5 D4:1 C4:2
Ab3:1 C4:1 Eb4:1 Db4:2
C3:4/5 Eb3:4/5 F3:4/5 G3:4/5 Ab3:4/5 Bb3:1
Ab3:1 C4:1 Eb4:.5 D4:2.5
A3:1 C4:1 E4:.5 D4:2.5
D3:1 F3:1 A3:.5 G3:2.5
D3:1 F3:1 Ab3:.5 G3:2.5
G3:2 Bb3:1 A3:2
''',sections={1:'p',2:'mp',3:'pp',4:'p',6:'mp',8:'p',9:'pp',10:'p',12:'mp',13:'p',14:'pp'},words={1:'poco rubato',14:'poco rit.'},
 slurs=[(1,3),(4,8),(9,12),(13,15)],lower_phrases=[(1,2),(3,5),(6,8),(9,11),(12,13),(14,15)],
 hairpins=[('crescendo',1,2),('diminuendo',2,3),('crescendo',4,6),('diminuendo',6,8),('crescendo',9,12),('diminuendo',13,15)],tempo_changes={},group=3,
 performance=dict(rubato=[56,53,49,60,52,57,59,51,48,56,49,53,47,41,32],
  phrase_arcs=[[0,14,3],[15,39,4],[40,59,4],[60,75,-2]],
  lower_entries=[[0,5],[40,45],[65,75]],tenor_entries=[[15,20],[45,50]],pedal_lift=.22,gate=.995,
  note='The quintuplet tenor comes forward slightly while the held bass remains quiet. Its five-note gesture leads into a shared arrival on the last beat, with the upper voices retaining their own timing. The final minor sixth is allowed to settle without a hard accent.'))
,
dict(op=52,title='Cobalt Avenue',key='Bb',fifths=-2,meter='6/4',bpm=54,
 description='Pewter Lagoon’s inner phrase becomes B-flat–C–D–F. Long tied notes hang above two-note lower harmonies that descend and change at their own pace. A G-major reflection briefly brightens the route before A-flat and D-flat colours lead into E-flat minor. A softly altered F dominant returns to a B-flat-major ninth.',
 difficulty='Advanced spacious duet',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The melody sustains through several changes of lower harmony. Open fifths, fourths and an occasional wider sixth move in the left hand, with pedal changes aligned to those shifts. Preserve the tied notes with the fingers while allowing each lower sonority to clear; the exposed texture needs gentle control of balance.',
 parent_opus=51,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Bb','C','D','F']),
 ancestry=dict(source_opus=51,source_hand='rh',source_voice='inner',source_start_beat=45,source_end_beat=50,source_pitches=['Eb','F','G','Bb'],transposition_semitones=7),
 engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[0,1.78],[2,3.78],[4,5.78],[6,8.78],[9,10.78],[11,11.78],[12,13.78],[14,15.78],[16,17.78],[18,20.78],[21,22.78],[23,23.78],[24,25.78],[26,27.78],[28,29.78],[30,31.78],[32,33.78],[34,35.78],[36,38.78],[39,39.78],[40,41.78],[42,43.78],[44,45.78],[46,47.78],[48,50.78],[51,51.78],[52,53.78],[54,55.78],[56,57.78],[58,59.78],[60,61.78],[62,63.78],[64,65.78],[66,71.78]],
 rh='''
Bb4:1 C5:.5 D5:.5 F5:4~
F5:1.5 Eb5:.5 D5:1 C5:1 A4:2
Bb4+D5+A5:3 G5:1 F5:1 Eb5:1
E5:2 D5:1 C5:3~
C5:1 D5:.5 E5:.5 F#5:2 G5:2
F#5:3 E5:1 D5:2
E5+G5+D6:3 C#6:1 B5:1 A5:1
G5:2 F5:.5 Eb5:.5 Db5:1 C5:2
F4+Ab4+Eb5:4 Db5:1 C5:1
Bb4+Db5+Ab5:3 Gb5:1 F5:1 Eb5:1
A4+C5+Gb5:2 F5:1 Eb5:1 D5:1 C5:1
D4+F4+C5:6
''',
 lh='''
Bb2:2 F3+A3:2 D3+G3:2
G2+D3:3 F3+Bb3:2 A3:1
Eb3+Bb3:2 D3+A3:2 C3+G3:2
F3+A3:3 C3+G3:2 Bb2+F3:1
G2+D3:2 F#3+A3:2 E3+B3:2
D3+A3:2 C3+G3:2 B2+F#3:2
C3+G3:3 B2+F#3:1 A2+E3:2
Ab2+Eb3:2 G3+Bb3:2 F3+C4:2
Db3+Ab3:3 C3+G3:1 Bb2+F3:2
Eb3+Bb3:2 Db3+Ab3:2 C3+Gb3:2
F3+C4:2 Eb3+Bb3:2 C3+A3:2
Bb2+F3:6
''',sections={1:'p',3:'mp',4:'pp',5:'p',6:'mp',8:'p',9:'pp',10:'p',11:'pp'},words={1:'poco rubato',11:'poco rit.'},
 slurs=[(1,3),(4,7),(8,10),(11,12)],lower_phrases=[(1,2),(3,5),(6,8),(9,10),(11,12)],
 hairpins=[('crescendo',1,3),('crescendo',4,6),('diminuendo',6,7),('diminuendo',8,9),('diminuendo',10,12)],tempo_changes={},group=3,
 performance=dict(rubato=[54,51,55,50,56,59,52,49,46,51,44,32],
  phrase_arcs=[[0,17,3],[18,41,4],[42,59,3],[60,72,-2]],
  lower_entries=[[0,12],[24,42],[48,60]],pedal_lift=.22,gate=.995,
  note='The long upper suspensions stay connected while the lower pairs change colour. The bass movement is kept gentle and unaccented. The G-major reflection opens slightly, then the phrase withdraws through the borrowed minor colours into the final added ninth.'))
,
dict(op=53,title='Viridian Terrace',key='Eb',fifths=-3,meter='7/4',bpm=57,
 description='Cobalt Avenue’s descending G–F–E-flat–D-flat becomes the opening thought. Its falling line passes through E-flat, B-flat minor and G-flat before two floating seven-against-three gestures open into C-major and A-flat light. The gestures are separated by a quieter chromatic route; the last descent returns to E-flat with a luminous major seventh and ninth.',
 difficulty='Advanced seven-against-three duet',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 5 and 10, seven quarter-note septuplets in the right hand share four beats with three half-note triplets in the left. Both hands arrive together on beat five. Shape each whole gesture, then release into the longer following note. The surrounding seven-beat bars contain ties and unequal phrases, with sustained voicings spanning up to a major seventh.',
 parent_opus=52,motif=dict(hand='rh',start_beat=0,end_beat=7,pitches=['G','F','Eb','Db']),
 ancestry=dict(source_opus=52,source_hand='rh',source_start_beat=42,source_end_beat=48,source_pitches=['G','F','Eb','Db'],transposition_semitones=0),
 tuplet_groups=[dict(hand='rh',actual=7,normal=4,count=14),dict(hand='lh',actual=3,normal=2,count=6)],
 polyrhythms=[dict(start_beat=28,end_beat=32,rh_notes=7,lh_notes=3),dict(start_beat=63,end_beat=67,rh_notes=7,lh_notes=3)],
 rh='''
G5:2 F5:.5 Eb5:.5 Db5:1 C5:3~
C5:2 Db5:1 F5:1 Eb5:3
Bb4+Db5+Ab5:3 Gb5:1 F5:1 Eb5:2
Bb4+Db5+F5:4 Eb5:1 Db5:2
E5:4/7 G5:4/7 B5:4/7 D6:4/7 C6:4/7 A5:4/7 G5:4/7 F#5:3
E5:2 D5:.5 C5:.5 B4:1 A4:3
G4+B4+F#5:3 E5:2 D5:2~
D5:2 C#5:1 B4:.5 A4:.5 G4:3
F4+A4+E5:4 D5:1 C5:2
C5:4/7 Eb5:4/7 G5:4/7 Bb5:4/7 Ab5:4/7 F5:4/7 Eb5:4/7 D5:3
C5:2 Bb4:1 Ab4:.5 G4:.5 F4:3
Ab4+C5+G5:3 F5:1 Eb5:1 Db5:2
D5:2 C5:1 Bb4:.5 Ab4:.5 G4:1 F4:2
G4+Bb4+D5:3 F4+G4+Bb4:4
''',
 lh='''
Eb3:2 Bb3:1 Db4:1 C4:3
Bb2:3 F3:.5 Ab3:.5 C4:2 Bb3:1
Ab2:2 Eb3:1 G3:2 Bb3:1 Ab3:1
Gb2:3 Db3:1 F3:1 Ab3:2
C3:4/3 E3:4/3 G3:4/3 A3:2 G3:1
A2:2 E3:2 G3:.5 B3:.5 C4:2
G2:3 D3:1 F#3:2 A3:1
E3:1.5 G3:.5 B3:2 F#3:1 E3:2
D3:2 A3:1 C4:1 E3:3
Ab2:4/3 C3:4/3 Eb3:4/3 F3:2 G3:1
Db3:3 Ab3:1 C4:1 Eb4:2
F3:2 C4:1 Eb4:1 D4:2 C4:1
Bb2:3 F3:1 Ab3:2 C4:1
Eb3+Bb3:7
''',sections={1:'p',3:'mp',4:'pp',5:'mp',6:'p',7:'pp',8:'p',9:'pp',10:'mp',11:'p',13:'pp'},words={1:'poco rubato',13:'poco rit.'},
 slurs=[(1,4),(5,7),(8,11),(12,14)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,14)],
 hairpins=[('crescendo',1,3),('diminuendo',3,4),('diminuendo',5,7),('crescendo',8,10),('diminuendo',10,11),('diminuendo',12,14)],tempo_changes={},group=3,
 performance=dict(rubato=[57,54,58,49,61,53,47,54,50,60,51,55,45,32],
  phrase_arcs=[[0,27,3],[28,48,4],[49,76,4],[77,98,-2]],
  lower_entries=[[7,14],[49,56],[70,77]],pedal_bars=list(range(1,15)),pedal_lift=.25,gate=.99,
  note='The two cross-rhythmic gestures expand and settle as single waves, with no extra accents on their individual notes. The lower voice answers between them. Longer tied notes keep the surrounding phrases connected, and the closing major colour recedes into the room.'))
,
dict(op=54,title='Fennel Tangent',key='b',fifths=2,meter='3/4',bpm=56,
 description='Viridian Terrace’s D–C-sharp–B–A descent enters a B-minor three-voice study. In the first long departure, the inner voice falls chromatically from F-sharp to C-sharp over six bars while the melody and bass take different routes. Later C-minor, A-flat and E-major windows widen the landscape before the opening returns and settles into a bare, quiet B minor.',
 difficulty='Advanced chromatic inner-voice study',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The right hand carries a singing upper line and a distinct inner voice. In bars 5–10, hold each inner note for the complete bar while changing the upper notes without losing balance. The chromatic descent must remain connected through changing harmonies. Later inner lines become more mobile; the bass needs an unhurried, independent shape.',
 parent_opus=53,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=3,pitches=['D','C#','B','A']),
 ancestry=dict(source_opus=53,source_hand='rh',source_start_beat=47,source_end_beat=56,source_pitches=['D','C#','B','A'],transposition_semitones=0),
 page_starts=[17],
 rh='''
D5:1 C#5:.5 B4:.5 A4:1
B4:3
A4:2 G4:1
F#4:2 R:1
E5:1 D5:1 B4:1
Eb5:2 Db5:1
D5:1 C#5:.5 B4:.5 A4:1
Db5:2 Bb4:1
C5:1 Bb4:1 A4:1
B4:1 A4:.5 G4:.5 F#4:1
B4:3
D5:2 C#5:1
E5:1 D5:2
D5:3
Eb5:2 D5:1
C5:3
F5:1 Eb5:1 Db5:1
C5:3
B4:1 C#5:.5 D#5:.5 E5:1
C#5:3
F#5:1 E5:1 D5:1
B4:2 A4:1
G4:3
A#4:1 G#4:.5 F#4:.5 E4:1
D5:1 C#5:.5 B4:.5 A4:1
B4:2 A4:1
A4:1 F#4:2
''',
 rh_inner='''
F#4:1 F4:.5 E4:.5 D4:1
D4:1 F#4:2
C#4:1 E4:1 D4:1
A3:1 C#4:1 E4:1
F#4:3
F4:3
E4:3
Eb4:3
D4:3
C#4:3
D4:1 F#4:.5 A4:.5 G4:1
F#4:1 A4:1 B4:1
B4:1 A4:1 G4:1
G4:1 F#4:.5 E4:1.5
G4:1 Bb4:.5 A4:.5 G4:1
Eb4:1 G4:2
Ab4:1 C5:1 Bb4:1
Db4:1 F4:1 Ab4:1
G#4:3
E4:1 G#4:.5 B4:.5 A4:1
A4:1 C#5:.5 B4:.5 A4:1
D4:1 F#4:.5 G4:.5 F#4:1
B3:1 D4:1 E4:1
C#4:3
F#4:1 F4:.5 E4:.5 D4:1
G4:1 F#4:2
D4:3
''',
 lh='''
B2:2 F#3:1
G3:3
A2:1 E3:2
F#2:1 C#3:1 E3:1
G2:2 D3:1
Bb2:1 F3:2
A2+E3:3
Ab2:2 Eb3:1
G2:1 D3:2
F#2:2 C#3:1
B2:1 F#3:1 A3:1
D3:2 A3:1
G2:1 D3:1 F#3:1
E3:2 B3:1
C3:1 G3:2
Ab2:2 Eb3:1
Db3:1 Ab3:2
Bb2:1 F3:1 Ab3:1
E3:3
A2:2 E3:1
D3:1 A3:1 F#3:1
G2:2 D3:1
C3:1 G3:2
F#2:1 C#3:2
B2:2 F#3:1
E3:1 B3:2
B2+F#3:3
''',sections={1:'p',3:'pp',5:'p',6:'mp',7:'p',10:'pp',11:'p',13:'mp',14:'pp',15:'p',17:'mp',18:'pp',19:'p',21:'mp',22:'p',24:'pp',25:'p',26:'pp'},words={1:'poco rubato',26:'poco rit.'},
 slurs=[(1,4),(5,10),(11,14),(15,18),(19,24),(25,27)],lower_phrases=[(1,3),(4,7),(8,10),(11,13),(14,16),(17,20),(21,24),(25,27)],
 hairpins=[('diminuendo',1,4),('crescendo',5,6),('diminuendo',7,10),('crescendo',11,13),('diminuendo',13,14),('crescendo',15,17),('diminuendo',17,18),('crescendo',19,21),('diminuendo',21,24),('diminuendo',25,27)],tempo_changes={},group=4,
 performance=dict(rubato=[56,53,51,45,55,59,56,54,51,46,55,58,60,48,55,52,58,47,56,59,61,54,50,45,51,42,31],
  phrase_arcs=[[0,11,2],[12,29,3],[30,41,4],[42,53,3],[54,71,4],[72,81,-2]],
  lower_entries=[[9,12],[18,24],[42,48],[66,72]],pedal_bars=list(range(1,28)),pedal_lift=.2,gate=.995,
  note='The six-bar chromatic inner descent stays softer than the upper melody, with a small breath in tempo at its end. The later brighter harmonies open gradually. The final return is closer and quieter than the beginning, with the last bare minor chord fading naturally.'))
,
dict(op=55,title='Aster Verge',key='d',fifths=-1,meter='9/8',bpm=59,
 description='Fennel Tangent’s chromatic inner descent contracts into A–A-flat–G–F-sharp in the left-hand tenor. A long upper E floats above it. The lower line opens through G minor, F, E-flat and D-flat, then a brighter E-major/A-dominant passage turns back towards D. The chromatic opening returns beneath a descending treble, and a quiet added ninth remains at the close.',
 difficulty='Advanced compound-metre tenor study',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Hold the bass with the left-hand fifth finger while its tenor moves independently. The opening tenor’s semitone descent is a passing line, not a set of accented chords. Printed pedal refreshes follow the three compound pulses while the bass remains physically held. Upper ties and unequal phrase lengths soften the metre; keep the melody above the tenor in balance.',
 parent_opus=54,motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=4.5,pitches=['A','Ab','G','F#']),
 ancestry=dict(source_opus=54,source_hand='rh',source_voice='inner',source_start_beat=12,source_end_beat=24,source_pitches=['F#','F','E','Eb'],transposition_semitones=3),
 page_starts=[10],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[i*1.5,i*1.5+1.28] for i in range(54)],
 rh='''
E5:4.5~
E5:1.5 D5:.5 C5:.5 Bb4:2
G4+B4+F5:3 E5:.5 D5:1
A4+C5+G5:3 F5:1 E5:.5
D5:1.5 F5:.5 A5:.5 G5:2
Gb5:2 F5:.5 Eb5:2
C5:1.5 Bb4:.5 Ab4:.5 G4:2
F4+Ab4+Eb5:3 Db5:.5 C5:1
B4+D#5+A5:3 G#5:1 F#5:.5
G4+B4+F#5:1.5 E5:.5 D5:.5 C#5:2
F5:1.5 E5:.5 D5:.5 C5:2
A4+C5+F5:3 E5:.5 D5:1
E5:1.5 D5:.5 B4:.5 A4:2
Eb5:1.5 Db5:.5 C5:.5 Bb4:2
D5+F5+A5:3 G5:1 F5:.5
C#5:1.5 E5:.5 G5:.5 Bb5:2
A5:1.5 G5:.5 F5:.5 E5:2
A4:1.5 E4+A4:3
''',
 lh='''
D3:4.5
G2:1.5 Bb2:3
C3:1.5 E3:3
F3:4.5
Bb2:1.5 D3:3
Eb3:1.5 G3:3
Ab2:1.5 C3:3
Db3:1.5 F3:3
E3:4.5
A2:1.5 C#3:3
D3:4.5
G2:1.5 B2:3
C3:1.5 E3:3
F3:4.5
Bb2:1.5 D3:3
A2:1.5 C#3:3
D3:4.5
D3:4.5
''',
 lh_upper='''
A3:1.5 Ab3:.5 G3:1 F#3:1.5
D3:1.5 F3:.5 A3:1 G3:1.5
G3:1 B3:.5 D4:1 C4:2
A3:1.5 C4:.5 D4:1 C4:1.5
F3:1 A3:.5 C4:1 Bb3:2
Bb3:1 Db4:.5 F4:1 Eb4:2
Eb3:1.5 G3:.5 Bb3:.5 Ab3:2
Ab3:1 C4:.5 Eb4:1 Db4:2
G#3:1.5 B3:.5 D4:.5 C#4:2
E3:1 G3:.5 B3:1 A3:2
F3:1.5 A3:.5 C4:1 B3:1.5
D3:1 F3:.5 A3:1 G3:2
G3:1.5 B3:.5 D4:.5 C4:2
Ab3:1.5 C4:.5 Eb4:.5 D4:2
F3:1 Ab3:.5 C4:1 Bb3:2
E3:1 G3:.5 Bb3:1 A3:2
A3:1.5 Ab3:.5 G3:1 F#3:1.5
F3:1.5 E3:1.5 F3:1.5
''',sections={1:'p',3:'mp',4:'pp',5:'p',6:'mp',7:'p',8:'pp',9:'mp',10:'p',11:'pp',12:'p',13:'mp',14:'pp',15:'p',16:'mp',17:'p',18:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,4),(5,8),(9,13),(14,18)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,15),(16,18)],
 hairpins=[('crescendo',1,3),('diminuendo',3,4),('crescendo',5,6),('diminuendo',6,8),('diminuendo',9,11),('crescendo',11,13),('crescendo',14,16),('diminuendo',16,18)],tempo_changes={},group=3,
 performance=dict(rubato=[59,55,62,49,57,61,54,48,63,56,50,59,62,49,57,60,46,32],
  phrase_arcs=[[0,17,3],[18,35,4],[36,58,4],[58.5,81,3]],
  lower_entries=[[9,13.5],[36,40.5],[63,67.5]],tenor_entries=[[0,4.5],[27,36],[72,76.5]],pedal_lift=.22,gate=.995,
  note='The opening chromatic tenor is slightly more present beneath a softly held upper E. Three gentle pedal refreshes per bar keep the changing line clear. The large harmonic journey gradually opens, then the returning tenor and descending melody come closer together before the final added ninth.'))
,
dict(op=56,title='Juniper Ferry',key='e',fifths=1,meter='12/8',bpm=61,
 description='A new branch returns to Orchard Static’s E–C–D–A, transposed into B–G–A–E. The opening passes this thought through all four voices in successive bars: upper melody, tenor, inner voice and bass. Broader F-major, E-major and A-flat reflections follow. The original gesture returns close to the middle of the keyboard, and the final E-minor chord is left quietly open.',
 difficulty='Advanced four-voice imitative nocturne',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The same four-note phrase enters successively in the upper voice, left-hand tenor, right-hand inner voice and bass during bars 1–4, with the same dotted-quarter rhythm and changing octave. Bring each entry forward without hard accents. Sustain the other lines independently, observing rests where voices withdraw. The return moves into a closer register and needs careful balance between the hands.',
 parent_opus=3,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=6,pitches=['B','G','A','E']),
 ancestry=dict(source_opus=3,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['E','C','D','A'],transposition_semitones=7),
 page_starts=[13],
 rh='''
B4:1.5 G4:1.5 A4:1.5 E4:1.5
G4:3 F#4:3
D5:3 C5:1.5 B4:1.5
F#5:3 E5:3
C5:3 A4:3
Bb4:2 C5:.5 D5:.5 E5:3
F5:4.5 E5:1.5
D#5:3 C#5:1.5 B4:1.5
E5:6
G5:1.5 E5:1.5 F5:1.5 C5:1.5
Db5:4.5 C5:1.5
Bb4:3 Ab4:3
C5:3 D5:1.5 Eb5:1.5
D5:4.5 B4:1.5
B4:1.5 G4:1.5 A4:1.5 E4:1.5
G4:3 F#4:1.5 E4:1.5
A4:4.5 G4:1.5
F#4:1.5 E4:1.5 D#4:3
E4:6
''',
 rh_inner='''
E4:1.5 D4:1.5 C4:1.5 B3:1.5
D4:1 E4:.5 D4:1.5 C4:3
B4:1.5 G4:1.5 A4:1.5 E4:1.5
A4:1.5 G4:1.5 F#4:1.5 E4:1.5
F4:2 E4:1 D4:3
F4:1 A4:.5 G4:1.5 Bb4:3
A4:3 C5:1.5 B4:1.5
F#4:1 A4:.5 G#4:1.5 F#4:3
G#4:2 B4:1 C#5:1.5 B4:1.5
B4:1 C5:.5 B4:1.5 A4:1.5 G4:1.5
Eb4:1 G4:.5 Ab4:1.5 G4:3
Db4:3 F4:1.5 Eb4:1.5
F4:2 Ab4:1 G4:3
F4:1 A4:.5 G4:1.5 F4:3
E4:1.5 D4:1.5 C4:1.5 B3:1.5
D4:1 C4:.5 B3:1.5 A3:3
C4:1.5 E4:1.5 F#4:1.5 E4:1.5
B3:1.5 A3:1.5 F#3:3
B3:3 C#4:1.5 B3:1.5
''',
 lh='''
E3:3 G3:3
E3:4.5 C3:1.5
C3:3 E3:3
B2:1.5 G2:1.5 A2:1.5 E2:1.5
F3:3 D3:3
Bb2:1.5 D3:4.5
D3:1.5 F3:4.5
B2:1.5 D#3:4.5
E3:6
C3:1.5 E3:4.5
Ab2:1.5 C3:4.5
Db3:3 F3:3
Bb2:1.5 D3:4.5
G2:1.5 B2:4.5
E3:3 G3:3
C3:3 D3:3
A2:1.5 C3:4.5
B2:3 D#3:3
E3:6
''',
 lh_upper='''
R:6
B3:1.5 G3:1.5 A3:1.5 E3:1.5
R:3 B3:3
D3:3 C3:1.5 B2:1.5
A3:3 F3:3
F3:1 A3:.5 C4:1.5 Bb3:3
A3:1 C4:.5 E4:1.5 D4:3
F#3:1 A3:.5 C#4:1.5 B3:3
B3:3 D#4:1.5 C#4:1.5
G3:1 B3:.5 D4:1.5 C4:3
Eb3:1 G3:.5 Bb3:1.5 Ab3:3
Ab3:2 C4:1 Bb3:3
F3:1 Ab3:.5 C4:1.5 Bb3:3
D3:1 F3:.5 A3:1.5 G3:3
R:6
G3:3 F#3:3
E3:1 G3:.5 B3:1.5 A3:3
R:6
G3:3 F#3:3
''',sections={1:'p',3:'mp',4:'p',5:'pp',6:'p',7:'mp',8:'p',9:'pp',10:'mp',11:'p',12:'pp',13:'p',14:'mp',15:'p',16:'pp',17:'p',18:'pp'},words={1:'poco rubato',18:'poco rit.'},
 slurs=[(1,4),(5,9),(10,14),(15,19)],lower_phrases=[(1,2),(3,4),(5,7),(8,10),(11,13),(14,16),(17,19)],
 hairpins=[('crescendo',1,3),('diminuendo',3,5),('crescendo',5,7),('diminuendo',7,9),('diminuendo',10,12),('crescendo',12,14),('diminuendo',15,19)],tempo_changes={},group=4,
 performance=dict(rubato=[61,58,63,55,51,59,64,55,48,63,56,49,59,62,53,47,52,42,31],
  phrase_arcs=[[0,23,4],[24,53,4],[54,83,4],[84,114,-2]],
  lower_entries=[[18,24],[72,78],[102,114]],inner_entries=[[12,18]],tenor_entries=[[6,12],[42,48],[96,102]],pedal_bars=list(range(1,20)),pedal_lift=.24,gate=.995,
  note='The opening phrase is passed between voices with a little prominence for the tenor, inner-voice and bass entries. The later upper melody unfolds in longer spans over softer inner movement. As the opening returns, the register contracts and the final minor chord is allowed to fade without a new surge.'))
,
dict(op=57,title='Tamarisk Angle',key='Gb',fifths=-6,meter='7/8',bpm=58,
 description='Juniper Ferry’s tenor fragment becomes G-flat–B-flat–D-flat–C-flat. Open stacks of fourths surround a melody that drifts across the seven-eighth bars. A whole-tone ascent reaches towards a nearby G-major reflection; later a falling triplet gesture returns to the flat-side colours. The ending leaves a softly spaced sixth, ninth and raised fourth around G-flat.',
 difficulty='Advanced quartal and whole-tone study',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Keep the three-note fourth-based voicings balanced, with the upper note singing. Two groups of six eighth-note triplets cross two quarter beats, followed by a longer arrival. Ties carry the melody across the seven-eighth bar lines. The six-flat notation and neighbouring G-major passage need careful reading; the ending’s three upper whole tones should be soft and evenly voiced.',
 parent_opus=56,motif=dict(hand='rh',start_beat=0,end_beat=3.5,pitches=['Gb','Bb','Db','Cb']),
 ancestry=dict(source_opus=56,source_hand='lh',source_voice='tenor',source_start_beat=54,source_end_beat=60,source_pitches=['G','B','D','C'],transposition_semitones=11),
 tuplet_groups=[dict(hand='rh',actual=3,normal=2,count=12)],page_starts=[13],
 rh='''
Gb4:1 Bb4:.5 Db5:1 Cb5:1
Bb4:2 Ab4:.5 Gb4:1
Ab4+Db5+Gb5:2 F5:.5 Eb5:1
Db5:3.5~
Db5:1 Eb5:.5 Gb5:2
C5+F5+Bb5:2 Ab5:.5 Gb5:1
Bb4+Eb5+Ab5:2 Gb5:1 F5:.5
Ab4+Db5+Gb5:3.5
Gb5:1/3 Ab5:1/3 Bb5:1/3 C6:1/3 D6:1/3 E6:1/3 D6:1.5
B5:1.5 A5:.5 G5:1.5
A4+D5+G5:2 F#5:.5 E5:1
F#5:3.5~
F#5:1.5 E5:.5 D5:1.5
G4+C5+F5:2 E5:.5 D5:1
E5:1 D5:.5 C5:2
Eb5:2 Db5:.5 Cb5:1
Bb5:1/3 Ab5:1/3 Gb5:1/3 F5:1/3 Eb5:1/3 Db5:1/3 Cb5:1.5
Bb4+Eb5+Ab5:2 Gb5:.5 F5:1
F4+Bb4+Eb5:2 Db5:1 Cb5:.5
Ab4+Db5+Gb5:3.5
Bb4:1 Ab4:.5 Gb4:2
Ab4:.5 Bb4:.5 Db5:1 Cb5:1.5
Bb4:1 Ab4:.5 F4:1 Eb4:1
Ab4+Bb4+C5:3.5
''',
 lh='''
Eb3:2 Bb3:.5 Db4:1
Cb3:1.5 Gb3:.5 Bb3:1.5
Ab2:1 Db3:.5 Gb3:2
Db3:2 Ab3:1 F3:.5
Gb3:1 Bb3:.5 Ab3:2
F3:1 C4:.5 Eb4:2
Eb3:2 Bb3:.5 Db4:1
Db3:1 Ab3:1 Cb4:1.5
Gb3:2 C4:1 D4:.5
G3:1 B3:.5 D4:2
C3:1.5 G3:.5 B3:1.5
B2:2 F#3:1 A3:.5
E3:1 B3:.5 G3:2
F3:2 C4:.5 A3:1
A2:1.5 E3:1 G3:1
Ab2:2 Eb3:.5 Gb3:1
Db3:2 Ab3:1 Gb3:.5
Cb3:1.5 Gb3:.5 Bb3:1.5
Bb2:1.5 F3:.5 Ab3:1.5
Ab2:1.5 Db3:.5 Gb3:1.5
Gb3:2 Db4:.5 Bb3:1
Eb3:1.5 Bb3:1 Db4:1
Db3:1 Ab3:.5 Cb4:1 Ab3:1
Gb2+Db3+Eb3:3.5
''',sections={1:'p',3:'mp',4:'pp',5:'p',6:'mp',8:'pp',9:'mp',10:'p',12:'pp',13:'p',14:'mp',15:'p',16:'pp',17:'mp',18:'p',20:'pp',21:'p',23:'pp'},words={1:'poco rubato',23:'poco rit.'},
 slurs=[(1,4),(5,8),(9,13),(14,16),(17,20),(21,24)],lower_phrases=[(1,3),(4,6),(7,10),(11,13),(14,17),(18,20),(21,24)],
 hairpins=[('crescendo',1,3),('diminuendo',3,4),('crescendo',5,6),('diminuendo',6,8),('diminuendo',9,12),('crescendo',13,14),('diminuendo',14,16),('diminuendo',17,20),('diminuendo',21,24)],tempo_changes={},group=4,
 performance=dict(rubato=[58,54,61,48,56,62,55,47,64,59,54,49,57,61,53,48,62,56,52,46,53,49,42,31],
  phrase_arcs=[[0,13,3],[14,27,4],[28,45,4],[45.5,55,3],[56,69,4],[70,84,-2]],
  lower_entries=[[10.5,17.5],[35,42],[66.5,73.5]],pedal_bars=list(range(1,25)),pedal_lift=.2,gate=.995,
  note='The fourth-based voicings remain quiet and open. The whole-tone ascent is one brief arc into the brighter neighbouring key; its later descending answer folds back into the darker flats. The final upper whole tones are balanced gently over the widely spaced bass.'))
,
dict(op=58,title='Gossamer Junction',key='E',fifths=4,meter='6/4',bpm=53,
 description='A descent from Tamarisk Angle becomes G-sharp–F-sharp–E–G. The last note briefly darkens E major before rising into G-sharp, while a quieter inner line changes beneath the held melody. G, A-flat, C and D-flat colours appear as slow reflections. The opening returns an octave lower, and the major third eventually withdraws from the final open added-ninth sonority.',
 difficulty='Advanced chromatic suspension study',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The RH upper melody and inner voice need independent finger sustain through the printed half-bar pedal changes. The opening G natural is a brief chromatic neighbour resolving into G-sharp. Hold the long upper G-sharp across the bar line while the inner voice and bass change. The final return sits an octave lower and should remain clear without becoming heavy.',
 parent_opus=57,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=6,pitches=['G#','F#','E','G']),
 ancestry=dict(source_opus=57,source_hand='rh',source_start_beat=38.5,source_end_beat=49,source_pitches=['F#','E','D','F'],transposition_semitones=2),
 page_starts=[10],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[i*3,i*3+2.78] for i in range(28)],
 rh='''
G#5:2 F#5:1 E5:2 G5:1
G#5:6~
G#5:2 F#5:1 E5:3
D5:4 C5:2
Eb5:3 F5:3
E5:6
G5:4 F#5:2
F5:3 Eb5:3
D5:2 C#5:1 B4:3
Db5:6
C#5:2 D#5:1 E5:3
D5:3 C#5:1 B4:2
G#4:2 F#4:1 E4:2 G4:1
G#4:2 F#4:4
''',
 rh_inner='''
E5:2 D#5:1 C#5:2 D5:1
D#5:3 B4:3
C#5:1.5 B4:.5 A4:1 G#4:3
G4:2 A4:2 B4:2
Ab4:4 G4:2
G#4:3 B4:3
B4:3 A4:3
A4:2 C5:1 Bb4:3
F#4:3 A4:3
F4:2 Ab4:1 B4:3
G#4:1.5 B4:.5 A4:1 G#4:3
F#4:2 A4:1 G#4:3
E4:2 D#4:1 C#4:2 D4:1
E4:3 D#4:1 E4:2
''',
 lh='''
E3:4 B3:2
C#3:3 G#3:3
A2:2 E3:1 G#3:3
G3:3 D3:3
Ab2:2 Eb3:1 F3:3
E3:6
C3:3 E3:3
F3:3 Ab3:3
B2:3 D3:3
Db3:3 F3:3
A2:3 C#3:3
B2:2 F#3:1 A3:3
E3:3 B2:3
E3+B3:6
''',sections={1:'p',2:'mp',3:'p',4:'pp',5:'p',6:'pp',7:'mp',8:'p',9:'pp',10:'p',11:'mp',12:'p',13:'pp'},words={1:'poco rubato',13:'poco rit.'},
 slurs=[(1,3),(4,6),(7,10),(11,14)],lower_phrases=[(1,2),(3,5),(6,8),(9,11),(12,14)],
 hairpins=[('crescendo',1,2),('diminuendo',2,3),('crescendo',4,5),('diminuendo',5,6),('diminuendo',7,9),('crescendo',10,11),('diminuendo',11,14)],tempo_changes={},group=3,
 performance=dict(rubato=[53,56,48,47,52,44,55,49,45,50,54,46,40,30],
  phrase_arcs=[[0,17,3],[18,35,3],[36,59,4],[60,84,-2]],
  lower_entries=[[18,24],[42,48],[66,72]],inner_entries=[[24,30],[54,60]],pedal_lift=.22,gate=.995,
  note='The chromatic neighbour is a brief change of light before the upper line settles. The inner voice comes a little closer in two of the distant reflections. The whole final phrase withdraws, leaving the added ninth above an open fifth rather than repeating the major third.'))
,
dict(op=59,title='Marigold Detour',key='bb',fifths=-5,meter='6/8',bpm=61,
 description='Gossamer Junction’s chromatic turn becomes B-flat–A-flat–G-flat–A. Four gently spaced notes pass over three in the other hand; twice the roles reverse. The treble opens into a high B-flat-minor register before a C-major/D-minor reflection draws it closer. Fourth-based chords and a later A-flat-minor colour return to a quiet B-flat-minor seventh.',
 difficulty='Advanced four-against-three nocturne',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In the declared crossing bars, four dotted eighths share the full 6/8 bar with three quarter notes. The RH carries the four-note gesture first; the LH takes it in bars 11 and 20. Both parts must stay even without forcing accents on their intermediate alignments. Keep the high treble soft, and let the longer notes between these gestures breathe.',
 parent_opus=58,motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['Bb','Ab','Gb','A']),
 ancestry=dict(source_opus=58,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=6,source_pitches=['G#','F#','E','G'],transposition_semitones=2),
 polyrhythms=[dict(start_beat=0,end_beat=3,rh_notes=4,lh_notes=3),dict(start_beat=12,end_beat=15,rh_notes=4,lh_notes=3),dict(start_beat=27,end_beat=30,rh_notes=4,lh_notes=3),dict(start_beat=30,end_beat=33,rh_notes=3,lh_notes=4),dict(start_beat=48,end_beat=51,rh_notes=4,lh_notes=3),dict(start_beat=57,end_beat=60,rh_notes=3,lh_notes=4),dict(start_beat=60,end_beat=63,rh_notes=4,lh_notes=3)],
 page_starts=[13],system_starts=[1,5,9,13,17,21],
 rh='''
Bb5:.75 Ab5:.75 Gb5:.75 A5:.75
Bb5:2 Ab5:1
F5+Ab5+Eb6:1.5 Db6:.5 C6:1
Bb5:1.5 Ab5:.5 F5:1
Gb5:.75 Bb5:.75 Db6:.75 C6:.75
Bb5:2 Ab5:1
Eb5+Ab5+Db6:1.5 C6:.5 Bb5:1
Ab5:2.5 R:.5
G5:1.5 F5:.5 E5:1
E5:.75 G5:.75 B5:.75 D6:.75
C6:1 B5:1 A5:1
G5:2 E5:1
F5:1.5 D5:.5 C5:1
Eb5:2 Db5:1
Bb4+Db5+Ab5:1.5 Gb5:.5 F5:1
E5:1 F5:.5 Gb5:1.5
F5:.75 Ab5:.75 Cb6:.75 Bb5:.75
Db5+Gb5+Cb6:1.5 Bb5:.5 Ab5:1
Gb5:2 F5:1
F5:1 Eb5:1 Db5:1
C5:.75 Eb5:.75 G5:.75 Bb5:.75
A5:1.5 G5:.5 F5:1
Gb5:2 F5:1
Db5:1 C5:.5 Bb4:1.5
Db4+F4+Ab4:3
''',
 lh='''
Bb2:1 Db3:1 F3:1
Eb3:1.5 Bb3:.5 Db4:1
Ab2:1.5 Eb3:.5 Gb3:1
Db3:2 Ab3:.5 F3:.5
Gb3:1 Ab3:1 Bb3:1
Eb3:1 Bb3:.5 Db4:1.5
Ab2:1.5 Eb3:1 Gb3:.5
Db3:1 Ab3:.5 Cb4:1.5
C3:1.5 G3:.5 B3:1
C3:1 E3:1 G3:1
D3:.75 F3:.75 A3:.75 C4:.75
G2:1.5 D3:.5 F3:1
A2:1 E3:.5 G3:1.5
Ab2:2 Eb3:1
Gb2:1 Db3:1 F3:1
F3:1 C4:.5 Eb3:1.5
Ab2:1 Cb3:1 Eb3:1
Cb3:1.5 Gb3:.5 Bb3:1
Db3:2 Ab3:1
Bb2:.75 Db3:.75 F3:.75 Ab3:.75
C3:1 E3:1 G3:1
F3:1.5 C4:.5 Eb4:1
Gb3:2 Db4:.5 Bb3:.5
F3:1.5 Ab3:.5 C4:1
Bb2+F3:3
''',sections={1:'p',3:'mp',4:'pp',5:'p',7:'mp',8:'pp',9:'p',10:'mp',12:'pp',13:'p',14:'pp',15:'p',16:'mp',17:'p',18:'mp',19:'pp',20:'p',21:'mp',22:'p',23:'pp'},words={1:'poco rubato',24:'poco rit.'},
 slurs=[(1,4),(5,8),(9,13),(14,19),(20,25)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,16),(17,20),(21,23),(24,25)],
 hairpins=[('crescendo',1,3),('diminuendo',3,4),('crescendo',5,7),('diminuendo',7,8),('crescendo',9,10),('diminuendo',10,13),('crescendo',14,16),('diminuendo',18,19),('crescendo',20,21),('diminuendo',21,25)],tempo_changes={},group=4,
 performance=dict(rubato=[61,57,63,50,60,56,62,47,58,64,59,51,48,50,56,61,58,63,49,57,62,54,47,41,31],
  phrase_arcs=[[0,11,3],[12,23,4],[24,38,4],[39,56,4],[57,75,-2]],
  lower_entries=[[30,33],[57,60],[69,72]],pedal_bars=list(range(1,26)),pedal_lift=.2,gate=.99,
  note='Each crossing is shaped as one small floating gesture. The lower voice comes forward when it carries the four-note figure, then recedes beneath the high melody. The closing five-bar phrase descends into a quieter register and a plain minor seventh.'))
,
dict(op=60,title='Cypress Orbit',key='c#',fifths=4,meter='5/4',bpm=56,
 description='Marigold Detour’s bass figure becomes C-sharp–E–G-sharp–B, enlarged eightfold into four six-beat upper notes. These notes drift across five-beat bars while three other voices continue beneath them. D-major, G-major and A-flat reflections widen the route before it passes through E and B-flat colour. The lines gradually contract into a quiet C-sharp-minor sixth.',
 difficulty='Advanced four-voice augmentation study',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The opening upper notes each last six quarter beats, crossing the five-beat bars at different points. Preserve these long notes with the fingers through the printed pedal changes, while both inner parts and the bass continue independently. The three quicker lines should support the large upper arc without giving every bar the same accent. The final register is close and needs a very light balance.',
 parent_opus=59,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=25,pitches=['C#','E','G#','B']),
 ancestry=dict(source_opus=59,source_hand='lh',source_start_beat=57,source_end_beat=60,source_pitches=['Bb','Db','F','Ab'],transposition_semitones=3),
 engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[span for i in range(16) for span in [[i*5,i*5+1.78],[i*5+2,i*5+4.78]]],
 rh='''
C#5:5~
C#5:1 E5:4~
E5:2 G#5:3~
G#5:3 B5:2~
B5:4 R:1
A5:2 G#5:3
F#5:4 E5:1
D5:5
Eb5:2 F5:3
E5:5
C#5:3 B4:2
D5:2 C5:1 Bb4:2
B4:5
C#5:2 B4:1 A4:2
G#4:2 F#4:1 E4:2
G#4:5
''',
 rh_inner='''
E4:2 G#4:1 A4:2
G#4:1 B4:2 D#5:2
C#5:2 D#5:1 F#5:2
E5:1 F#5:2 G#5:2
F#5:2 E5:2 D#5:1
E5:2 D#5:3
A4:2 C#5:1 D#5:2
G4:2 B4:1 C5:2
Ab4:3 C5:2
G#4:2 B4:1 D5:2
E4:2 G#4:1 A4:2
F4:3 A4:2
D#4:2 F#4:1 G#4:2
F#4:3 G#4:2
B#3:2 D#4:1 C#4:2
E4:2 D#4:1 E4:2
''',
 lh='''
C#3:2 E3:3
B2:2 D#3:3
A2:2 C#3:3
F#3:5
G#2:2 B#2:3
C#3:2 E3:3
D3:2 F#3:3
G2:2 B2:3
Ab2:2 C3:3
E3:5
A2:2 C#3:3
Bb2:2 D3:3
B2:5
F#3:5
G#2:2 B#2:3
C#3:5
''',
 lh_upper='''
G#3:1.5 B3:.5 D#4:1 C#4:2
F#3:2 A3:.5 C#4:.5 B3:2
E3:1 G#3:1 B3:1 A3:2
A3:2 C#4:1 E4:.5 D#4:1.5
D#3:1.5 F#3:.5 A3:1 G#3:2
G#3:2 B3:.5 D#4:.5 C#4:2
A3:1 C#4:1 E4:1 D4:2
D3:2 F#3:1 A3:.5 G3:1.5
Eb3:1.5 G3:.5 Bb3:1 Ab3:2
B3:2 C#4:1 D4:2
E3:2 G3:.5 B3:.5 A3:2
F3:1 Ab3:1 C4:1 Bb3:2
F#3:2 A3:1 G#3:2
A3:1.5 C#4:.5 E4:3
D#3:2 F#3:1 A3:2
G#3:2 B3:1 A#3:2
''',sections={1:'p',3:'mp',5:'p',6:'pp',7:'p',8:'mp',9:'p',10:'pp',11:'p',12:'mp',13:'p',14:'pp',15:'p',16:'pp'},words={1:'poco rubato',15:'poco rit.'},
 slurs=[(1,5),(6,10),(11,14),(15,16)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,16)],
 hairpins=[('crescendo',1,3),('diminuendo',3,6),('crescendo',6,8),('diminuendo',8,10),('crescendo',11,12),('diminuendo',12,14),('diminuendo',15,16)],tempo_changes={},group=4,
 performance=dict(rubato=[56,54,58,61,49,47,55,60,54,46,55,59,51,45,41,31],
  phrase_arcs=[[0,24,4],[25,49,4],[50,69,3],[70,80,-2]],
  lower_entries=[[15,20],[35,40],[65,70]],tenor_entries=[[5,10],[30,35],[55,60]],inner_entries=[[20,25],[45,50]],pedal_lift=.22,gate=.995,
  note='The large four-note upper arc is kept continuous while the inner lines change pace. Tenor and inner answers briefly come closer, then return behind the melody. Pedal refreshes clear each harmonic field while held keys preserve the independent lines, and the final minor sixth fades in a closer register.'))
,
dict(op=61,title='Saffron Traverse',key='f',fifths=-4,meter='4/4',bpm=56,
 meters=['4/4','5/4','3/4','4/4','4/4','5/4','5/4','3/4','4/4','5/4','3/4','4/4','5/4','4/4','3/4','5/4','4/4','3/4','4/4','5/4'],
 description='Cypress Orbit’s tenor becomes F–A-flat–C–B-flat. Four voices move through bars of four, five and three quarter beats, allowing the phrases to expand and contract. The upper C remains held across the first change of metre; later an E-major reflection sustains through another boundary. D-flat, G and A-flat colours return to a close F-minor added ninth.',
 difficulty='Advanced four-voice changing-metre study',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Keep the quarter-note pulse continuous as the printed metre changes between 4/4, 5/4 and 3/4. The upper line sometimes remains held across a change, while the inner voices and bass continue independently. Follow the phrase shape rather than accenting every new bar. Pedal refreshes follow the actual changing bar lengths, with finger sustain retaining the longer notes.',
 parent_opus=60,motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=4,pitches=['F','Ab','C','Bb']),
 ancestry=dict(source_opus=60,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=5,source_pitches=['G#','B','D#','C#'],transposition_semitones=9),
 page_starts=[11],engraving=dict(spacing_system=13,pedal_offset_y=420),system_starts=[1,4,7,9,11,14,17,19],
 pedal_spans=[[0,1.78],[2,3.78],[4,5.78],[6,8.78],[9,9.78],[10,11.78],[12,13.78],[14,15.78],[16,17.78],[18,19.78],[20,21.78],[22,24.78],[25,26.78],[27,29.78],[30,31.28],[31.5,32.78],[33,34.28],[34.5,36.78],[37,38.78],[39,41.78],[42,43.28],[43.5,44.78],[45,46.78],[47,48.78],[49,50.78],[51,53.78],[54,55.78],[56,57.78],[58,58.78],[59,60.78],[61,62.78],[63,65.78],[66,67.78],[68,69.78],[70,71.28],[71.5,72.78],[73,74.78],[75,76.78],[77,78.78],[79,81.78]],
 rh='''
C5:4~
C5:1 Eb5:4
Db5:2 C5:1
Bb4:4
C5:2 Eb5:2
F5:3 Eb5:2
D5:5
C5:3
Eb5:2 F5:2
Gb5:3 F5:2
E5:3~
E5:1 D5:1 C5:2
Db5:5
C5:2 Bb4:2
Ab4:3
Bb4:2 C5:1 Db5:2
C5:4~
C5:1 Bb4:1 Ab4:1
G4:2 F4:2
Ab4:3 G4:2
''',
 rh_inner='''
Ab4:1 Bb4:1 Ab4:2
G4:2 Bb4:1 Db5:2
F4:1 Ab4:1 Bb4:1
Eb4:1 G4:.5 Ab4:.5 G4:2
Ab4:2 G4:1 Bb4:1
A4:2 C5:1 D5:2
G4:2 B4:1 C5:2
E4:1 G4:1 Bb4:1
Ab4:1 C5:1 Db5:2
Bb4:1 Db5:1 Eb5:1 Db5:2
G#4:1 B4:1 C#5:1
G4:1 B4:1 A4:2
F4:2 Ab4:1 C5:2
Eb4:1 G4:1 Ab4:2
Db4:1 F4:1 Gb4:1
Eb4:2 G4:1 Bb4:2
Ab4:1 Bb4:1 Ab4:2
G4:1 F4:1 Eb4:1
C4:1 Eb4:1 Db4:2
F4:2 Eb4:1 F4:2
''',
 lh='''
Db3:4
F3:5
Bb2:1 D3:2
Eb3:2 G3:2
Ab2:2 C3:2
D3:2 F3:3
G2:2 B2:3
C3:3
Ab2:1.5 C3:2.5
Db3:2 F3:3
E3:3
C3:2 E3:2
Db3:2 F3:3
F3:4
Gb2:1 Bb2:2
Eb3:2 G3:3
Db3:4
C3:3
C3:2 E3:2
F3:5
''',
 lh_upper='''
F3:1 Ab3:1 C4:1 Bb3:1
Ab3:1 C4:1 Eb4:1 D4:2
F3:1 Ab3:1 C4:1
Bb3:1 D4:1 F4:.5 Eb4:1.5
Eb3:1 G3:1 Bb3:1 Ab3:1
A3:1 C4:1 E4:1 D4:2
D3:1 F#3:1 A3:1 G3:2
G3:1 Bb3:1 A3:1
Eb3:1 G3:.5 Bb3:.5 Ab3:2
Ab3:1 C4:1 Eb4:1 Db4:2
G#3:1 B3:1 D#4:1
G3:1 B3:1 D4:.5 C4:1.5
Ab3:1 C4:1 Eb4:1 Db4:2
Ab3:1 C4:.5 Eb4:.5 D4:2
Db3:1 F3:1 Ab3:1
Bb3:1 D4:1 F4:1 Eb4:2
F3:1 Ab3:1 C4:1 Bb3:1
G3:1 Bb3:1 Ab3:1
G3:1 Bb3:1 Ab3:1 Bb3:1
Ab3:2 C4:1 Ab3:2
''',sections={1:'p',2:'mp',3:'pp',4:'p',6:'mp',7:'p',8:'pp',9:'p',10:'mp',11:'pp',12:'p',13:'mp',14:'p',15:'pp',16:'mp',17:'p',18:'pp',19:'p',20:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,3),(4,8),(9,12),(13,16),(17,20)],lower_phrases=[(1,2),(3,5),(6,8),(9,11),(12,14),(15,17),(18,20)],
 hairpins=[('crescendo',1,2),('diminuendo',2,3),('crescendo',4,6),('diminuendo',6,8),('crescendo',9,10),('diminuendo',10,11),('crescendo',12,13),('diminuendo',13,15),('diminuendo',16,20)],tempo_changes={},group=3,
 performance=dict(rubato=[56,59,48,53,57,62,54,46,55,61,48,54,59,52,45,60,51,44,40,30],
  phrase_arcs=[[0,11,3],[12,32,4],[33,48,4],[49,65,4],[66,82,-2]],
  lower_entries=[[9,12],[25,30],[58,61],[73,77]],tenor_entries=[[0,4],[16,20],[66,70]],inner_entries=[[20,25],[45,49]],pedal_lift=.22,gate=.995,
  note='The quarter pulse stays continuous while each phrase is given a different amount of room. The tenor opening and its late return come gently forward. Upper ties bridge metre changes without a fresh accent, and the last phrase closes around a soft minor added ninth.'))
,
dict(op=62,title='Daphne Slipway',key='Db',fifths=-5,meter='7/8',bpm=59,
 meters=['7/8','9/8','6/8','4/4','7/8','7/8','9/8','3/4','5/8','9/8','4/4','7/8','6/8','9/8','5/8','4/4','7/8','9/8','3/4','4/4'],
 description='Saffron Traverse’s inner turn becomes D-flat–E-flat–D-flat–C. Seven- and nine-eighth bars open and close around shorter and even-length measures, following the melody’s uneven breath. Fourth-based voicings and a held F connect the phrases. A B-minor/C-major window slips back towards G-flat and D-flat, ending in a softly voiced major ninth.',
 difficulty='Advanced mixed-metre duet',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Keep the eighth-note subdivision continuous through the changing time signatures; their groupings change without a sudden change of speed. The upper F crosses a 7/8-to-9/8 boundary and remains held while the lower line moves. Shape the fourth-based chords gently and prepare the wider lower-register descents during their longer preceding notes. The final four-note RH chord should remain soft and balanced.',
 parent_opus=61,motif=dict(hand='rh',start_beat=0,end_beat=3.5,pitches=['Db','Eb','Db','C']),
 ancestry=dict(source_opus=61,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=6,source_pitches=['Ab','Bb','Ab','G'],transposition_semitones=5),
 page_starts=[13],system_starts=[1,4,7,10,13,16,18],
 rh='''
Db5:1 Eb5:.5 Db5:1 C5:1
Db5:2 F5:1 Ab5:1.5
Gb5:2 F5:1
Eb5:3 Db5:1
C5+F5+Bb5:2 Ab5:.5 Gb5:1
F5:3.5~
F5:1.5 Eb5:.5 Db5:.5 C5:2
Bb4+Eb5+Ab5:3
Gb5:1 F5:.5 Eb5:1
Gb4+Bb4+F5:3 Eb5:1 Db5:.5
D5:2 E5:.5 F#5:.5 A5:1
G5:2 F#5:.5 E5:1
C5+E5+B5:2 A5:1
Bb5:1.5 Ab5:.5 Gb5:.5 F5:2
Eb5:1 Db5:.5 C5:1
C5+F5+Bb5:2 Ab5:1 Gb5:1
F5:1 Eb5:.5 Db5:1 C5:1
Db5:2 C5:.5 Ab4:.5 Gb4:1.5
F4+Ab4+Eb5:2 Db5:1
F4+Ab4+C5+Eb5:4
''',
 lh='''
Bb2:1 F3:.5 Ab3:1 C4:1
Gb3:1.5 Db4:.5 F4:1 Eb4:1.5
F3:1 C4:.5 Eb4:1.5
Eb3:1.5 Bb3:.5 Db4:2
Bb2:1 F3:1 Ab3:1.5
Ab2:2 Eb3:.5 Gb3:1
Db3:1.5 Ab3:.5 C4:1 Bb3:1.5
Eb3:1 Bb3:.5 Db4:1.5
Ab2:1 Eb3:.5 Gb3:1
Gb3:1.5 Db4:.5 F4:1 Eb4:1.5
B2:1.5 F#3:.5 A3:1 C#4:1
E3:1 B3:.5 D4:2
C3:1 G3:.5 B3:1.5
Gb2:1.5 Db3:.5 F3:1 Ab3:1.5
Ab2:1 Eb3:.5 Gb3:1
Bb2:1.5 F3:.5 Ab3:1 C4:1
Gb3:1.5 Db4:.5 F4:1 Bb3:.5
Db3:2 Ab3:.5 C4:.5 Bb3:1.5
Gb2:1 Db3:.5 F3:1.5
Db3+Ab3:4
''',sections={1:'p',2:'mp',3:'p',4:'pp',5:'mp',6:'p',8:'pp',9:'p',10:'mp',11:'p',13:'pp',14:'mp',15:'pp',16:'p',17:'mp',18:'p',19:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,4),(5,9),(10,13),(14,17),(18,20)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,15),(16,18),(19,20)],
 hairpins=[('crescendo',1,2),('diminuendo',2,4),('diminuendo',5,8),('crescendo',9,10),('diminuendo',10,13),('diminuendo',14,15),('crescendo',16,17),('diminuendo',18,20)],tempo_changes={},group=3,
 performance=dict(rubato=[59,62,55,49,60,52,57,50,45,58,63,56,49,61,48,57,53,46,41,30],
  phrase_arcs=[[0,14.5,3],[15,31.5,4],[32,46.5,4],[47,61,4],[61.5,73,-2]],
  lower_entries=[[8,11],[36.5,40.5],[58,61.5]],pedal_bars=list(range(1,21)),pedal_lift=.2,gate=.995,
  note='The uneven measures share a continuous underlying subdivision, while the larger phrases gather and release. The lower line answers beneath the held upper F and through the neighbouring tonal window. A final major ninth settles softly after the last descending phrase.'))
,
dict(op=63,title='Myrtle Folly',key='F',fifths=-1,meter='3/4',bpm=57,
 description='Daphne Slipway’s opening turn becomes F–G–F–E in the left-hand tenor before the upper melody enters. A steadier three-beat frame gives space to the two lower voices and two small tenor triplet gestures. The treble rises into a new register, passes through E-minor and A-flat reflections, then descends towards a close, gently added F-major sixth.',
 difficulty='Advanced tenor-led nocturne',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The left-hand tenor opens above a held bass; the right-hand melody enters in bar 2. In bars 9 and 19, the tenor’s three quarter-note triplets share two beats while the bass stays held. Keep those lines distinct through the half-bar pedal refreshes. Prepare the RH register change before bar 9 during its preceding quarter note, then let the high melody recede gradually.',
 parent_opus=62,motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=3,pitches=['F','G','F','E']),
 ancestry=dict(source_opus=62,source_hand='rh',source_start_beat=0,source_end_beat=3.5,source_pitches=['Db','Eb','Db','C'],transposition_semitones=4),
 tuplet_groups=[dict(hand='lh',actual=3,normal=2,count=6)],
 page_starts=[17],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[i*1.5,i*1.5+1.28] for i in range(56)],
 rh='''
R:3
A4:3
G4:2 F4:1
E4:3
F4:1.5 G4:.5 A4:1
C5:2 Bb4:1
A4:3
G4:2 E4:1
F5:3
E5:1 D5:.5 C5:1.5
D5:3
C5:2 B4:1
B4:1.5 D5:.5 E5:1
F#5:3
G5:2 F#5:1
E5:2 D5:1
Eb5:3
Db5:2 C5:1
F5:3
Eb5:2 Db5:1
C5:3
Bb4:1.5 C5:.5 D5:1
Db5:2 C5:1
Bb4:3
A4:1.5 G4:.5 F4:1
E4:2 F4:1
G4:1 E4:1 C4:1
F4+A4:3
''',
 lh='''
C3:3
F3:2 D3:1
Bb2:1 D3:2
C3:1 E3:2
F3:3
Eb3:1 G3:2
D3:3
C3:1 E3:2
D3:3
A2:1 C3:2
G2:1 B2:2
C3:3
E3:3
B2:1 D#3:2
E3:3
A2:1 C3:2
Ab2:1 C3:2
Bb2:1 Db3:2
Db3:3
Gb2:1 Bb2:2
F3:3
Bb2:1 D3:2
Gb2:1 Bb2:2
C3:1 E3:2
F3:3
D3:3
C3:3
F3:3
''',
 lh_upper='''
F3:1.5 G3:.5 F3:.5 E3:.5
C4:1 A3:.5 G3:.5 F3:1
F3:1 A3:.5 C4:.5 Bb3:1
G3:1 Bb3:.5 D4:.5 C4:1
A3:1 C4:.5 D4:.5 C4:1
Bb3:1 D4:.5 F4:.5 Eb4:1
F3:1 A3:1 C4:1
G3:1 Bb3:.5 A3:.5 G3:1
F3:2/3 A3:2/3 C4:2/3 B3:1
E3:1 G3:.5 B3:.5 A3:1
D3:1 F#3:1 A3:1
E3:1 G3:.5 A3:.5 G3:1
G3:1 B3:.5 D4:.5 C4:1
F#3:1 A3:1 C#4:1
G3:1 B3:1 D4:1
E3:1 G3:.5 B3:.5 A3:1
Eb3:1 G3:1 Bb3:1
F3:1 Ab3:.5 C4:.5 Bb3:1
F3:2/3 Ab3:2/3 C4:2/3 Bb3:1
Db3:1 F3:.5 Ab3:.5 Gb3:1
Ab3:1 C4:.5 Eb4:.5 D4:1
F3:1 Ab3:1 C4:1
Db3:1 F3:.5 Ab3:.5 Gb3:1
G3:1 Bb3:.5 Db4:.5 C4:1
A3:1 C4:.5 D4:.5 C4:1
F3:1 A3:1 C4:1
E3:1 G3:1 Bb3:1
C4:1 D4:2
''',sections={1:'p',2:'p',3:'mp',4:'pp',5:'p',6:'mp',8:'pp',9:'p',11:'mp',12:'pp',13:'p',15:'mp',16:'p',17:'pp',18:'p',19:'mp',20:'pp',21:'p',22:'mp',24:'pp',25:'p',27:'pp'},words={1:'poco rubato',27:'poco rit.'},
 slurs=[(2,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28)],lower_phrases=[(1,4),(5,7),(8,10),(11,13),(14,17),(18,20),(21,24),(25,28)],
 hairpins=[('crescendo',2,3),('diminuendo',3,4),('crescendo',5,6),('diminuendo',6,8),('crescendo',9,11),('diminuendo',11,12),('crescendo',13,15),('diminuendo',15,16),('crescendo',17,19),('diminuendo',19,20),('crescendo',21,22),('diminuendo',22,24),('diminuendo',25,28)],tempo_changes={},group=4,
 performance=dict(rubato=[57,54,59,46,55,60,54,47,58,55,62,48,56,60,64,53,47,55,61,48,56,60,52,46,53,47,40,30],
  phrase_arcs=[[0,11,3],[12,23,4],[24,35,4],[36,47,4],[48,59,3],[60,71,4],[72,84,-2]],
  lower_entries=[[9,12],[33,36],[69,72]],tenor_entries=[[0,3],[24,27],[54,57]],pedal_lift=.22,gate=.995,
  note='The tenor begins clearly above the quieter bass. Its two triplet gestures return gently to the foreground while the upper melody holds. The rise in register opens the middle of the piece, and the final four-bar descent returns to the warmth of a close major sixth.'))
,
dict(op=64,title='Hyacinth Bend',key='A',fifths=3,meter='4/4',bpm=56,
 description='Myrtle Folly’s tenor turn becomes A–B–A–G-sharp. Three times, a four-note thought passes from the right hand to the left an octave lower while the right hand falls silent. The left-hand staff changes clef for two high answers. F-sharp minor, B-flat and D-flat reflections connect the exchanges before the final return settles into an A-major sixth.',
 difficulty='Advanced hand-to-hand dialogue',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The left hand uses treble clef in bars 1–2 and 10, returning to bass clef in bars 3 and 11. Keep each note in its written hand. The RH phrases in bars 1, 9 and 17 are answered an octave lower by the LH tenor in the following bars, with exactly the same rhythm. Prepare the left-hand register shifts during the preceding held notes and keep the answers gently prominent.',
 clef_changes={'lh':{1:'treble',3:'bass',10:'treble',11:'bass'}},
 parent_opus=63,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['A','B','A','G#']),
 ancestry=dict(source_opus=63,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=3,source_pitches=['F','G','F','E'],transposition_semitones=4),
 page_starts=[13],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[i*2,i*2+1.78] for i in range(40)],
 rh='''
A5:1 B5:1 A5:1 G#5:1
R:4
C#5:3 B4:1
A4:2 G#4:1 F#4:1
G4:3 F4:1
E4+G4+D5:2 C5:1 B4:1
D5:3 C5:1
B4:2 C#5:1 D#5:1
E5:1 F#5:1 E5:1 D#5:1
R:4
G#4:3 F#4:1
F5:2 Eb5:1 Db5:1
C5:2 Bb4:1 Ab4:1
B4:2 C#5:1 D5:1
E5:3 D5:1
C#5:2 B4:1 A4:1
A4:1 B4:1 A4:1 G#4:1
R:4
C#4:2 B3:2
C#4+E4+A4:4
''',
 lh='''
A3:4
E4:2 C#4:2
F#3:4
D3:2 F#3:2
Bb2:2 D3:2
C3:2 E3:2
Bb2:2 D3:2
B2:2 D#3:2
E3:4
B3:2 G#3:2
E3:4
Db3:2 F3:2
Ab2:2 C3:2
B2:2 D3:2
A2:2 C#3:2
D3:2 F#3:2
A3:4
E3:2 C#3:2
A2:4
A2:4
''',
 lh_upper='''
E4:4
A4:1 B4:1 A4:1 G#4:1
A3:1 C#4:1 E4:1 D#4:1
A3:1 C#4:1 E4:.5 D4:1.5
F3:1 A3:1 C4:1 Bb3:1
G3:1 B3:1 D4:.5 C4:1.5
F3:1 Ab3:1 C4:1 Bb3:1
F#3:1 A3:1 C#4:1 B3:1
B3:4
E4:1 F#4:1 E4:1 D#4:1
G#3:1 B3:.5 C#4:.5 D#4:2
Ab3:1 C4:1 Eb4:1 Db4:1
Eb3:1 G3:1 Bb3:1 Ab3:1
F#3:1 A3:1 C#4:1 B3:1
E3:1 G3:1 B3:1 A3:1
A3:1 C#4:1 E4:.5 D4:1.5
E4:4
A3:1 B3:1 A3:1 G#3:1
E3:2 F#3:2
E3:2 F#3:2
''',sections={1:'p',2:'p',3:'mp',4:'p',5:'pp',6:'p',7:'mp',8:'p',9:'mp',10:'p',11:'pp',12:'p',13:'pp',14:'p',15:'mp',16:'p',17:'p',18:'pp',19:'pp'},words={1:'poco rubato',19:'poco rit.'},
 slurs=[(1,1),(3,5),(6,8),(9,9),(11,13),(14,17),(19,20)],lower_phrases=[(1,2),(3,5),(6,8),(9,10),(11,13),(14,16),(17,18),(19,20)],
 hairpins=[('diminuendo',3,5),('crescendo',6,7),('diminuendo',7,8),('diminuendo',11,13),('crescendo',14,15),('diminuendo',15,17),('diminuendo',19,20)],tempo_changes={},group=4,
 performance=dict(rubato=[56,51,58,53,49,56,51,57,60,50,54,48,52,57,60,53,49,43,37,29],
  phrase_arcs=[[0,7,2],[8,19,3],[20,31,4],[32,39,2],[40,51,3],[52,67,4],[68,80,-2]],
  lower_entries=[[8,12],[40,44],[72,80]],tenor_entries=[[4,8],[36,40],[68,72]],pedal_lift=.22,gate=.995,
  note='The high phrases and their lower answers have matching, unaccented quarter-note shapes. The tenor comes closer during each response while the right hand rests. Left-hand clef changes make those positions readable; the final exchange moves down another octave before the quiet major sixth.'))
,
dict(op=65,title='Sorrel Switchback',key='g',fifths=-2,meter='6/4',bpm=57,
 description='A middle phrase from Hyacinth Bend becomes G–F–E-flat–D, followed by an E-natural that briefly opens the minor phrase into Dorian light. Five broad melody notes cross three slower lower notes, then settle into a shared two-beat breath. These crossings recur with different harmonies and directions; E-flat, F-sharp minor and whole-tone colour open the centre before the last descent returns to G minor with a sixth and ninth.',
 difficulty='Advanced five-against-three reverie',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='In bars 1, 4, 7, 11 and 13, five RH quarter-note quintuplets share four beats with three LH half-note triplets. Both hands then settle into the final two beats. Practise each complete crossing as one gesture, keeping the RH melody above the quieter bass. The intervening bars release the cross-rhythm through longer notes and small eighth-note turns.',
 parent_opus=64,motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['G','F','Eb','D']),
 ancestry=dict(source_opus=64,source_hand='rh',source_voice='upper',source_start_beat=8,source_end_beat=15,source_pitches=['C#','B','A','G#'],transposition_semitones=6),
 tuplet_groups=[dict(hand='rh',actual=5,normal=4,count=25),dict(hand='lh',actual=3,normal=2,count=15)],
 polyrhythms=[dict(start_beat=b*6,end_beat=b*6+4,rh_notes=5,lh_notes=3) for b in [0,3,6,10,12]],
 system_starts=[1,4,7,10,13],page_starts=[10],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[i*2,i*2+1.78] for i in range(45)],
 rh='''
G5:4/5 F5:4/5 Eb5:4/5 D5:4/5 E5:4/5 C5:2
D5:3~ D5:1 C5:1 Bb4:1
A4:2 C5:.5 D5:.5 F5:2 E5:1
F5:4/5 G5:4/5 Bb5:4/5 A5:4/5 G5:4/5 F5:2
Eb5:3 D5:1 C5:1 Bb4:1
D5+G5:2 F5:1 Eb5:1 D5:2
Eb5:4/5 F5:4/5 G5:4/5 Bb5:4/5 A5:4/5 G5:2
F#5:3 E5:1 D5:1 C#5:1
B4:2 D5:.5 E5:.5 G#5:2 F#5:1
E5:3 D5:1 C5:1 Bb4:1
C5:4/5 D5:4/5 E5:4/5 F#5:4/5 G#5:4/5 F#5:2
F5:2 Eb5:1 D5:.5 C5:.5 Bb4:2
G5:4/5 F5:4/5 E5:4/5 Eb5:4/5 D5:4/5 Bb4:2
A4:3 G4:1 F4:1 D4:1
Bb3+D4+A4:6
''',
 lh='''
G3:4/3 Bb3:4/3 D4:4/3 C4:2
Eb3:2 Bb3:1 D4:1 C4:2
F3:1 C4:1 Eb4:2 D4:1 C4:1
D3:4/3 F3:4/3 A3:4/3 C4:2
C3:2 G3:.5 Bb3:.5 D4:1 C4:2
Bb2:1 F3:1 A3:2 C4:1 Bb3:1
Eb3:4/3 G3:4/3 Bb3:4/3 D4:2
F#3:2 C#4:1 E4:1 D4:2
B2:1 F#3:1 A3:2 C#4:1 B3:1
C3:2 G3:1 Bb3:1 E4:1 Bb3:1
Ab2:4/3 C3:4/3 E3:4/3 Bb3:2
D3:1 A3:1 C4:2 Eb4:1 D4:1
G3:4/3 Bb3:4/3 D4:4/3 C4:2
C3:2 G3:1 Bb3:1 A3:1 F#3:1
G2+D3:3 E3:3
''',sections={1:'p',2:'pp',3:'p',4:'mp',5:'p',6:'pp',7:'mp',8:'p',9:'mp',10:'pp',11:'p',12:'pp',13:'p',14:'pp'},words={1:'poco rubato',14:'poco rit.'},
 slurs=[(1,3),(4,6),(7,10),(11,12),(13,15)],lower_phrases=[(1,2),(3,5),(6,8),(9,10),(11,12),(13,15)],
 hairpins=[('diminuendo',1,2),('crescendo',3,4),('diminuendo',4,6),('diminuendo',7,8),('diminuendo',9,10),('diminuendo',11,12),('diminuendo',13,15)],tempo_changes={},group=3,
 performance=dict(rubato=[57,51,59,63,55,48,61,54,60,49,58,50,54,43,29],
  phrase_arcs=[[0,17,4],[18,35,4],[36,59,4],[60,71,3],[72,90,-2]],
  lower_entries=[[6,12],[30,36],[54,60],[84,90]],pedal_lift=.22,gate=.99,
  note='Each five-against-three span moves as a single unaccented arc towards its shared two-beat ending. The bass remains soft through the crossings, emerging in the held melodic spaces. The remote harmonic window gathers slightly more motion before the final minor-sixth-and-ninth chord recedes.'))
,
dict(op=66,title='Lupin Gradient',key='a',fifths=0,meter='5/8',bpm=48,
 description='Sorrel Switchback’s descending line is stretched into A–G–F–E in the bass, while the upper melody climbs. Two softer inner voices enter around those opposing lines. The short five-eighth bars join into longer arcs, including an upper E held across a bar line. A-flat, D-flat and B-minor reflections lead through a suspended dominant into a softly open A-minor sixth.',
 difficulty='Advanced four-voice contrary motion',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Follow the four independent voices through their staggered entries. The opening bass falls through A–G–F–E–D while the upper melody rises A–B–C–D–E. Several RH inner entries begin after an eighth or quarter rest. Keep the five-eighth bars inside the longer phrases, and sustain the upper E across bars 5–6 without repeating its attack.',
 parent_opus=65,motif=dict(hand='lh',voice='bass',start_beat=0,end_beat=10,pitches=['A','G','F','E']),
 ancestry=dict(source_opus=65,source_hand='rh',source_start_beat=42,source_end_beat=48,source_pitches=['F#','E','D','C#'],transposition_semitones=3),
 system_starts=[1,6,11,16,21],page_starts=[16],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[b*2.5,b*2.5+2.25] for b in range(25)],
 rh='''
A4:2.5
B4:1.5 A4:1
C5:2.5
D5:1.5 C5:1
E5:2.5~
E5:2.5
D5:1.5 C5:.5 B4:.5
C5:2.5
Db5:1.5 Eb5:1
F5:2.5
G5:1.5 F5:1
F#5:2.5
E5:1.5 D5:.5 C#5:.5
D5:2.5
C#5:1.5 B4:1
A4:2.5
Bb4:1.5 Db5:1
C5:2.5
B4:1.5 A4:1
G#4:2.5
A4:1.5 B4:.5 C5:.5
B4:2.5
A4:1.5 G4:1
G#4:1.5 E4:1
A4:2.5
''',
 rh_inner='''
R:.5 E4:1 G4:1
D4:1 R:.5 G4:1
R:1 E4:1.5
G#4:1 A4:.5 G#4:1
A4:1.5 C5:1
B4:1 A4:.5 G4:1
E4:1 R:.5 G4:1
R:.5 G4:1 Bb4:1
Ab4:1 F4:.5 Ab4:1
R:1 A4:1.5
Bb4:1 D5:.5 Eb5:1
A4:1 F#4:.5 A4:1
B4:1 G#4:.5 A4:1
R:.5 G4:1 B4:1
E4:1 G4:.5 A#4:1
F#4:1.5 E4:1
G4:1 F4:.5 E4:1
Eb4:1 G4:.5 Bb4:1
F4:1 Ab4:.5 G4:1
D4:1 E4:.5 D4:1
E4:1.5 G4:1
D4:1 R:.5 F4:1
C4:1 E4:.5 F4:1
D4:1.5 B3:1
C4+E4:2.5
''',
 lh='''
A2:2.5
G2:2.5
F2:2.5
E2:2.5
D2:2.5
G2:2.5
C3:2.5
Ab2:1.5 Eb3:1
Db3:2.5
Bb2:2.5
Eb3:1 Bb2:1.5
B2:2.5
E3:1.5 B2:1
C3:2 R:.5
F#2:2.5
B2:2.5
E3:2.5
Ab2:1.5 Eb3:1
D3:1 A2:1.5
E3:1 B2:1.5
A2:2.5
G2:2 R:.5
F2:2.5
E2:2.5
A2:2.5
''',
 lh_upper='''
E3:1.5 C3:1
D3:1 B2:.5 F3:1
C3:1.5 A2:1
B2:1 D3:.5 C3:1
F2:1.5 A2:1
B2:1 D3:.5 F3:1
G3:1 E3:1.5
C3:1 Eb3:.5 G3:1
F3:1.5 Ab3:1
F3:1 D3:.5 A3:1
G3:1 Bb3:.5 A3:1
D3:1.5 F#3:1
G#3:1 B3:.5 A3:1
E3:1.5 G3:1
A#2:1 C#3:.5 E3:1
D3:1.5 F#3:1
G3:1 Bb3:.5 A3:1
C3:1.5 G3:1
F3:1 Ab3:.5 G3:1
G#3:1.5 B3:1
C3:1.5 E3:1
B2:1 D3:.5 F3:1
A2:1.5 C3:1
B2:1 D3:.5 C3:1
E3:1.5 F#3:1
''',sections={1:'p',2:'p',3:'mp',4:'p',5:'mp',6:'p',7:'pp',8:'p',9:'mp',10:'p',11:'mp',12:'p',13:'pp',14:'p',15:'mp',16:'p',17:'pp',18:'p',19:'mp',20:'pp',21:'p',22:'p',23:'pp'},words={1:'poco rubato',23:'poco rit.'},
 slurs=[(1,7),(8,13),(14,20),(21,25)],lower_phrases=[(1,5),(6,9),(10,13),(14,17),(18,20),(21,25)],
 hairpins=[('crescendo',1,5),('diminuendo',5,7),('crescendo',8,11),('diminuendo',11,13),('crescendo',14,15),('diminuendo',15,17),('crescendo',18,19),('diminuendo',19,20),('diminuendo',21,25)],tempo_changes={},group=5,
 performance=dict(rubato=[48,49,52,50,54,48,41,47,52,49,55,48,42,47,53,49,42,46,51,40,45,42,38,34,26],
  phrase_arcs=[[0,17,4],[17.5,32,4],[32.5,49.5,4],[50,62.5,-2]],
  lower_entries=[[0,12.5],[50,62.5]],inner_entries=[[12.5,17.5],[30,35],[45,50]],tenor_entries=[[20,27.5],[35,42.5]],pedal_lift=.25,gate=.995,
  note='The opening bass descent and upper ascent stay gently present while the two inner voices speak more softly. The five-eighth bars share one long breath through each larger phrase. Delayed inner entries and the held upper E keep the surface from becoming a repeated accompaniment pattern; the final descent narrows towards the minor sixth.'))
,
dict(op=67,title='Nacre Driftway',key='Gb',fifths=-6,meter='9/8',bpm=56,
 description='A new branch returns to Velvet Estuary’s A–C–D–C, now E-flat–G-flat–A-flat–G-flat. A quieter inner voice later turns the melody’s intervals upside down beneath a held B-flat. Compound pulses and long ties carry the three voices through G-flat, C-flat minor colour and a distant D-major reflection, before the close opens into a G-flat major ninth.',
 difficulty='Advanced three-voice inverted reflection',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='Shape the opening four-note melody over a quieter inner line. In bar 9 the RH inner voice gives its exact interval inversion, G-flat–E-flat–D-flat–E-flat, beneath the held upper B-flat. Retain both voice lengths through the pedal changes and let the inner answer emerge. The upper F in bars 4–5 is one sustained note across the bar line.',
 parent_opus=2,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4.5,pitches=['Eb','Gb','Ab','Gb']),
 ancestry=dict(source_opus=2,source_hand='rh',source_start_beat=0,source_end_beat=4.5,source_pitches=['A','C','D','C'],transposition_semitones=6),
 system_starts=[1,4,7,10,13,16],page_starts=[10],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[i*1.5,i*1.5+1.27] for i in range(51)],
 rh='''
Eb5:1.5 Gb5:1.5 Ab5:1 Gb5:.5
F5:3 Eb5:1 Db5:.5
Eb5:1.5 Db5:1 Cb5:.5 Bb4:1.5
F5:4.5~
F5:1.5 Eb5:1.5 Db5:1 Cb5:.5
Bb4:3 Ab4:1 Gb4:.5
Ab4:1.5 Bb4:1 Db5:.5 Eb5:1.5
Fb5:3 Eb5:1 Db5:.5
Bb4:4.5
A4:3 B4:1 C#5:.5
D5:1.5 F#5:1 E5:.5 C#5:1.5
C5:3 Bb4:1 Db5:.5
Gb5:1.5 Ab5:1.5 Bb5:1 Ab5:.5
Gb5:3 F5:1 Eb5:.5
Db5:1.5 Cb5:1 Bb4:.5 Ab4:1.5
Bb4:3 Ab4:1 Gb4:.5
F4+Ab4:4.5
''',
 rh_inner='''
Bb4:3 Db5:1.5
Ab4:1.5 Cb5:1 Bb4:.5 Ab4:1.5
Gb4:2 R:.5 Ab4:2
Db5:1.5 Eb5:1.5 Db5:1.5
Cb5:1.5 Ab4:1.5 Gb4:1.5
F4:1.5 Eb4:1.5 Db4:1.5
Eb4:1.5 Gb4:1 F4:.5 Ab4:1.5
Ab4:2 R:.5 Cb5:2
Gb4:1.5 Eb4:1.5 Db4:1 Eb4:.5
F#4:1.5 E4:1.5 D4:1.5
A4:1.5 D5:1 B4:.5 A4:1.5
E4:1.5 G4:1.5 F4:1.5
Eb5:1.5 F5:1 Eb5:.5 Db5:1.5
Bb4:1.5 Db5:1 Cb5:.5 Ab4:1.5
Gb4:1.5 F4:1.5 Eb4:1.5
Db4:1.5 F4:1.5 Eb4:1.5
Bb3:4.5
''',
 lh='''
Eb3:1.5 Bb3:1 Db4:.5 Cb4:1.5
Db3:1 Ab3:.5 Cb4:1.5 Bb3:1.5
Cb3:2 Gb3:.5 Bb3:1 Ab3:1
Bb2:1.5 F3:1.5 Ab3:1.5
Eb3:1 Bb3:.5 Db4:1.5 Cb4:1.5
Db3:1.5 Ab3:1.5 Gb3:1.5
Cb3:1 Gb3:.5 Bb3:1.5 Ab3:1.5
Fb3:2 Cb4:.5 Eb4:1 Db4:1
Cb3:1.5 Gb3:1 Bb3:.5 Ab3:1.5
D3:1 A3:.5 C#4:1.5 B3:1.5
B2:1.5 F#3:1.5 A3:1.5
C3:1 G3:.5 Bb3:1.5 A3:1.5
Eb3:1.5 Bb3:1 Db4:.5 Cb4:1.5
Cb3:2 Gb3:.5 Bb3:1 Ab3:1
Db3:1 Ab3:.5 Cb4:1.5 Bb3:1.5
Cb3:1.5 Gb3:1.5 F3:1.5
Gb2+Db3:3 Eb3:1.5
''',sections={1:'p',2:'p',3:'pp',4:'mp',5:'p',6:'pp',7:'p',8:'mp',9:'pp',10:'p',11:'mp',12:'pp',13:'mp',14:'p',15:'pp',16:'pp'},words={1:'poco rubato',16:'poco rit.'},
 slurs=[(1,3),(4,6),(7,9),(10,12),(13,17)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,15),(16,17)],
 hairpins=[('diminuendo',1,3),('diminuendo',4,6),('crescendo',7,8),('diminuendo',8,9),('crescendo',10,11),('diminuendo',11,12),('diminuendo',13,17)],tempo_changes={},group=3,
 performance=dict(rubato=[56,54,47,58,53,43,54,60,46,53,59,47,57,51,45,38,28],
  phrase_arcs=[[0,13,3],[13.5,26.5,4],[27,40,4],[40.5,53.5,4],[54,76.5,-2]],
  lower_entries=[[13.5,22.5],[31.5,36],[58.5,63]],inner_entries=[[36,40.5]],pedal_lift=.23,gate=.995,
  note='The compound pulses flow underneath longer melodic spans. The inner inversion in bar 9 comes forward while the upper B-flat stays quiet. A distant major reflection provides a brief lift, then the returning melody gradually loses height and settles into a spacious major ninth.'))
,
dict(op=68,title='Seagrass Relay',key='D',fifths=2,meter='5/4',bpm=55,
 meters=['5/4','4/4','6/4','5/4','3/4','6/4','4/4','5/4','4/4','6/4','5/4','3/4','5/4','4/4','6/4','5/4','4/4','6/4'],
 description='Nacre Driftway’s inner inversion becomes G–E–D–E at the top of three-note chords stacked in fourths. The shapes move through changing bars, sometimes shifting by a semitone over a more distant bass. A whole chord is held across the six-beat and five-beat bars near the centre. The last descent releases the fourths into a D-major ninth.',
 difficulty='Advanced quartal chord planing in changing metre',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The RH opening and most later chords contain two stacked perfect fourths, spanning ten semitones. Voice their top notes as one melody. Maintain all three tied notes across bars 2–3 and 10–11, even while the bass and metre change. The final chord changes the interval shape; prepare its closer spacing during the preceding held chord.',
 parent_opus=67,motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['G','E','D','E']),
 ancestry=dict(source_opus=67,source_hand='rh',source_voice='inner',source_start_beat=36,source_end_beat=40.5,source_pitches=['Gb','Eb','Db','Eb'],transposition_semitones=1),
 system_starts=[1,4,7,10,13,16],page_starts=[10],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[0,1.8],[2,3.8],[4,4.8],[5,6.8],[7,8.8],[9,11.8],[12,14.8],[15,17.8],[18,19.8],[20,21.8],[22,22.8],[23,25.8],[26,28.8],[29,30.8],[31,32.8],[33,35.8],[36,37.8],[38,39.8],[40,41.8],[42,44.8],[45,47.8],[48,49.8],[50,52.8],[53,54.3],[54.5,55.8],[56,57.8],[58,60.8],[61,63.8],[64,64.8],[65,67.8],[68,70.8],[71,72.8],[73,75.8],[76,77.8],[78,79.8],[80,82.8],[83,85.8]],
 rh='''
A4+D5+G5:2 F#4+B4+E5:1 E4+A4+D5:1 F#4+B4+E5:1
G4+C5+F5:4~
G4+C5+F5:1 F#4+B4+E5:2 F4+Bb4+Eb5:3
E4+A4+D5:3 F4+Bb4+Eb5:2
E4+A4+D5:2 D#4+G#4+C#5:1
D4+G4+C5:3 E4+A4+D5:1 F#4+B4+E5:2
G4+C5+F5:2 A4+D5+G5:2
Ab4+Db5+Gb5:3 G4+C5+F5:1 Gb4+Cb5+Fb5:1
F4+Bb4+Eb5:2 E4+A4+D5:2
F#4+B4+E5:6~
F#4+B4+E5:2 G4+C5+F5:1 F4+Bb4+Eb5:2
E4+A4+D5:1.5 D4+G4+C5:1.5
D4+G4+C5:2 E4+A4+D5:1 F#4+B4+E5:1 G4+C5+F5:1
F#4+B4+E5:3 E4+A4+D5:1
F4+Bb4+Eb5:3 E4+A4+D5:3
D4+G4+C5:2 E4+A4+D5:3
C#4+F#4+B4:2 D4+G4+C5:2
C#4+E4+A4:6
''',
 lh='''
D3:2 A3:1 C#4:1 B3:1
Bb2:1.5 F3:.5 A3:1 C4:1
Eb3:2 Bb3:1 Db4:1 C4:2
Ab2:1.5 Eb3:.5 Gb3:1 Bb3:1 Ab3:1
A2:1 E3:1 G3:1
G2:2 D3:1 F#3:1 A3:1 B3:1
C3:1 G3:1 B3:1 D4:1
Db3:2 Ab3:1 C4:1 Bb3:1
B2:1.5 F#3:.5 A3:1 C#4:1
E3:2 B3:1 D4:1 C#4:2
C3:1 G3:1 Bb3:1 A3:2
F3:1 C4:.5 Bb3:1.5
G2:2 D3:1 F3:1 A3:1
B2:1.5 F#3:.5 A3:1 C#4:1
Bb2:2 F3:1 Ab3:1 C4:2
G2:1.5 D3:.5 F3:1 A3:2
A2:1 E3:1 G3:1 B3:1
D3+F#3:6
''',sections={1:'p',2:'mp',3:'p',4:'mp',5:'pp',6:'p',7:'mp',8:'p',9:'pp',10:'p',11:'mp',12:'pp',13:'p',14:'mp',15:'p',16:'pp',17:'pp'},words={1:'poco rubato',17:'poco rit.'},
 slurs=[(1,5),(6,9),(10,12),(13,18)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,15),(16,18)],
 hairpins=[('crescendo',1,2),('diminuendo',2,3),('diminuendo',4,5),('crescendo',6,7),('diminuendo',7,9),('crescendo',10,11),('diminuendo',11,12),('crescendo',13,14),('diminuendo',14,18)],tempo_changes={},group=3,
 performance=dict(rubato=[55,58,51,57,44,53,60,54,45,52,58,44,53,57,50,44,37,28],
  phrase_arcs=[[0,22.5,4],[23,41.5,4],[42,55.5,4],[56,86,-2]],
  lower_entries=[[5,10],[42,50],[76,80]],pedal_lift=.2,gate=.995,
  note='The chord tops carry the melody while the lower chord notes remain soft. The varying bar lengths follow longer swells and retreats. Bass movement is clearer during the two sustained chord fields; the closing shape contracts into a quiet major ninth.'))
,
dict(op=69,title='Wisteria Remainder',key='e',fifths=1,meter='7/4',bpm=57,
 description='Seagrass Relay’s first bass gesture becomes E–B–D-sharp–C-sharp beneath an E-minor melody. Two quick octatonic runs briefly brighten the slow seven-beat phrases: an ascent over altered E dominant resolves towards A minor, and a later descending answer over F dominant opens into B-flat. The final descent returns to an E-minor added ninth.',
 difficulty='Advanced octatonic nocturne',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='The eight sixteenth notes in bars 4 and 8 each occupy two beats. Their alternating semitone and whole-tone steps need a planned, even fingering, with the first run rising and the second falling. Keep them inside the larger slow phrase. Prepare the wider RH register rise before bar 8 during the preceding half note; the accompaniment remains slower throughout.',
 parent_opus=68,motif=dict(hand='lh',start_beat=0,end_beat=7,pitches=['E','B','D#','C#']),
 ancestry=dict(source_opus=68,source_hand='lh',source_start_beat=0,source_end_beat=5,source_pitches=['D','A','C#','B'],transposition_semitones=2),
 system_starts=[1,4,6,8,10,13],page_starts=[8],engraving=dict(spacing_system=13,pedal_offset_y=420),
 pedal_spans=[[b*7+s,b*7+e] for b in range(14) for s,e in [(0,2.78),(3,4.78),(5,6.78)]],
 rh='''
G4+B4+E5:3 D#5:1 C#5:1 B4:2
C5+E5+B5:4 A5:1 G5:2
F#5:3 G5:.5 A5:.5 B5:2 A5:1
E5:.25 F5:.25 G5:.25 Ab5:.25 Bb5:.25 B5:.25 Db6:.25 D6:.25 E6:3 D6:1 B5:1
C6:4 B5:1 A5:2
G5:3 F#5:1 E5:3
D5+G5+C6:3 B5:1 A5:1 G5:2
F6:.25 Eb6:.25 D6:.25 C6:.25 B5:.25 A5:.25 Ab5:.25 Gb5:.25 F5:3 Eb5:1 C5:1
Bb4+D5+A5:4 G5:1 F5:2
Eb5:3 D5:.5 C5:.5 B4:2 A4:1
G4+B4+E5:4 F#5:1 G5:2
F#5:2 E5:1 D#5:1 C#5:3
B4:3 A4:1 G4:1 F#4:2
E4+G4+B4:7
''',
 lh='''
E3:2 B3:1 D#4:1 C#4:3
C3:2 G3:1 B3:1 E4:1 D4:1 C4:1
B2:1.5 F#3:.5 A3:1 C#4:1 B3:1 F#3:1 A3:1
E3:3 Bb3:1 D4:1 G#3:2
A2:2 E3:1 G3:1 B3:1 C4:1 D4:1
D3:2 A3:1 C4:1 E4:1 B3:2
G2:2 D3:1 F#3:1 A3:1 B3:2
F3:3 B3:1 Eb4:1 A3:2
Bb2:1.5 F3:.5 A3:1 C4:1 D4:1 C4:2
A2:2 E3:1 G3:1 Bb3:1 C#4:1 B3:1
E3:2 B3:1 D4:1 C#4:1 A3:2
F#2:2 C#3:1 E3:1 G3:1 B3:1 A3:1
B2:2 F#3:1 A3:1 C4:1 B3:1 A3:1
E3:4 F#3:3
''',sections={1:'p',2:'mp',3:'p',4:'mp',5:'p',6:'pp',7:'p',8:'mp',9:'p',10:'pp',11:'p',12:'mp',13:'pp'},words={1:'poco rubato',13:'poco rit.'},
 slurs=[(1,3),(4,6),(7,10),(11,14)],lower_phrases=[(1,3),(4,6),(7,9),(10,12),(13,14)],
 hairpins=[('crescendo',1,2),('diminuendo',2,3),('diminuendo',4,6),('crescendo',7,8),('diminuendo',8,10),('crescendo',11,12),('diminuendo',12,14)],tempo_changes={},group=3,
 performance=dict(rubato=[57,60,53,59,54,46,55,61,52,44,54,58,42,29],
  phrase_arcs=[[0,20.5,4],[21,41.5,4],[42,69.5,4],[70,98,-2]],
  lower_entries=[[0,7],[35,42],[63,70],[91,98]],pedal_lift=.22,gate=.985,
  note='The two brief runs remain light and even, each gathering into a longer held arrival. Their altered dominant colours release into warmer neighbouring harmonies. The bass moves forward during the held upper phrases; the final E-minor ninth decays gently with a little room reverb.'))
]
