"""Explicit Second Studies compositions, continuing the CWS opus sequence."""

PIECES = [
dict(op=241,title='Salt Interruption',key='b',fifths=2,meter='4/4',meters=['4/4']*10+['3/4']*8+['5/4']*6+['4/4']*6,bpm=55,final_fermata=False,
 description='The song is first heard in incomplete glimpses, separated by silence and falling figures. Brief three-beat flights widen into five-beat phrases. Only in the final six bars does the ancestral melody appear whole, over a gentler harmony, before it trails off into a plain descent.',
 difficulty='Advanced fragmentary form, register changes and free phrase continuity',technique_limits=dict(chord_span=12,melodic_leap=18,rapid_leap=9),technical_note='Hold the sense of one long phrase through the written interruptions. The three-beat section is a brief flowing release, not a new fixed accompaniment. The bass relocates from C4 to G2 after the five-beat silence of bar 24, with ample time to prepare the released hand. The complete B–D–C-sharp–A phrase first appears in bar 25; earlier openings deliberately stop short of it.',
 parent_opus=233,motif=dict(hand='rh',start_beat=94,end_beat=98,pitches=['B','D','C#','A']),ancestry=dict(source_opus=233,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=5,source_pitches=['B','D','C#','A'],transposition_semitones=0),
 system_starts=list(range(1,31,2)),page_starts=[7,13,19,25],engraving=dict(spacing_system=18,spacing_staff=16,pedal_offset_y=570),
 rh='''B4:1 D5:1 R:2
C#5:2 R:2
R:4
F#4:1 A4:.5 C#5:.5 E5:1 D5:1
B4:2 R:2
G4+B4+D5:3 R:1
A4:.5 B4:.5 C#5:.5 D5:.5 F#5:1 E5:1
D5:1 B4:1 R:2
C#5:3 R:1
R:4
B4:.25 D5:.25 F#5:.25 A5:.25 G5:.5 F#5:.5 E5:.5 D5:.5
C#5:.25 E5:.25 G5:.25 B5:.25 A5:.5 G5:.5 F#5:.5 E5:.5
D5:.25 F#5:.25 A5:.25 C#6:.25 B5:.5 A5:.5 G5:.5 F#5:.5
E5:.5 G5:.5 B5:1 A5:1
G5:.5 F#5:.5 E5:.5 D5:.5 C#5:.5 B4:.5
A4:.25 C#5:.25 E5:.25 G5:.25 F#5:.5 E5:.5 D5:1
C#5:2 R:1
R:3
B4:2 D5:1 R:2
F#5:3 E5:2
D5:2 C#5:1 B4:2
A4:1 C5:1 E5:2 D5:1
C5:2 A4:1 R:2
R:5
B4:1 D5:1 C#5:1 A4:1
G4:1 B4:.5 D5:.5 E5:2
F#5:1 E5:1 D5:2
C#5:1 B4:1 A4:1 G4:1
F#4:2 A4:1 R:1
B4:1 A4:1 F#4:1 D4:1''',
 lh='''B2+F#3:2 R:2
A2+E3:2 R:2
R:4
D3:1 A3:.5 F#3:.5 E3:1 F#3:1
G2+D3:2 R:2
E3+B3:3 R:1
F#3:1 C#4:1 A3:1 G3:1
B2+F#3:2 R:2
A2+E3:3 R:1
R:4
G3:1 D4:1 B3:1
A3:1 E4:1 C#4:1
B3:1 F#4:1 D4:1
C4:1 G4:1 E4:1
B3:1 F#4:1 D4:1
A3:1 E4:1 C#4:1
F#3+C#4:2 R:1
R:3
G2+D3:3 R:2
D3:1 A3:1 C#4:1 A3:1 F#3:1
E3:1 B3:1 D4:1 B3:1 G3:1
F3:1 C4:1 E4:1 C4:1 A3:1
E3:1 A3:1 C4:1 R:2
R:5
G2:1 D3:.5 F#3:.5 B3:1 A3:1
C3:1 G3:.5 B3:.5 E4:1 D4:1
D3:1 A3:.5 C#4:.5 F#4:1 E4:1
E3:1 B3:.5 G3:.5 F#3:1 E3:1
D3:1 A3:1 F#3:1 R:1
B2:1 F#3:1 R:2''',
 sections={1:'p',4:'p',6:'pp',11:'mp',19:'pp',20:'p',25:'p',29:'pp'},lower_sections={1:'pp',11:'p',19:'pp'},words={11:'poco rubato',25:'a tempo'},slurs=[(1,1),(4,4),(7,8),(11,13),(14,17),(20,23),(25,28),(30,30)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[start+a,start+b-.18] for i,(start,length) in enumerate(zip([i*4 for i in range(10)]+[40+i*3 for i in range(8)]+[64+i*5 for i in range(6)]+[94+i*4 for i in range(6)],[4]*10+[3]*8+[5]*6+[4]*6)) if i not in [2,9,17,23,29] for a,b in ([(0,2)] if i in [0,1,4,7,16] else [(0,3)] if i in [5,8,18,22] else [(0,2),(2,3)] if i==28 else [(0,2),(2,length)])],
 performance=dict(rubato=[55,49,46,56,49,47,58,50,45,43,62,64,66,64,62,60,49,45,50,54,55,54,48,44,55,56,57,55,52,53],phrase_arcs=[[0,8,2],[12,20,3],[24,32,4],[40,49,5],[49,61,4],[69,89,4],[94,110,4]],lower_entries=[],pedal_lift=.18,gate=.98,note='Silence belongs to the phrase. The late complete melody is a quiet recognition; the final descent keeps moving after the bass has left.')),
dict(op=242,title='Lichen Lacuna',key='g',fifths=-2,meter='4/4',bpm=49,
 description='A high bell keeps returning while a quieter song searches underneath. The hands draw closer in the upper register, then a single seven-note fall breaks the stillness. After a long gap, the complete G-minor phrase is finally heard; its ending is a softly unresolved ninth.',
 difficulty='Advanced register-sensitive voicing and a seven-to-six falling gesture',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='The LH moves into treble clef for bars 9–14, where it carries the lower song beneath high RH notes. Bar 17 contains seven equal eighth-note tuplets over three quarter beats, followed by silence. The complete ancestral phrase is reserved for bar 21.',
 parent_opus=234,motif=dict(hand='rh',start_beat=80,end_beat=84,pitches=['G','Bb','A','F']),ancestry=dict(source_opus=234,source_hand='rh',source_start_beat=0,source_end_beat=5.5,source_pitches=['C','Eb','D','Bb'],transposition_semitones=7),
 system_starts=list(range(1,27,2)),page_starts=[9,17,23],engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=580),clef_changes=dict(lh={9:'treble',15:'bass'}),
 tuplet_spans=[dict(hand='rh',start_beat=64,end_beat=67,actual=7,normal=6,stem='down',show_number='both')],
 rh='''Bb5:2 R:2
Bb5:1 A5:1 R:2
F5:3 R:1
R:4
G4+Bb4+D5:2 R:2
A4:1 C5:.5 Eb5:.5 D5:1 Bb4:1
A4:2 R:2
F5:1 A5:1 R:2
G5:4
F5:4
Eb5:4
Ab5:4
G5:3 F5:1
G5:1 F5:1 E5:1 D5:1
D5:2 F5:2
Eb5:1 G5:.5 Bb5:.5 A5:1 F5:1
C6:3/7 Bb5:3/7 A5:3/7 G5:3/7 F5:3/7 E5:3/7 D5:3/7 R:1
G5:3 R:1
R:4
R:4
G5:.5 Bb5:.5 A5:1 F5:2
Eb5:1 G5:1 A5:1 Bb5:1
C6:2 Bb5:1 G5:1
F5:1 Eb5:1 D5:1 C5:1
Bb4:2 A4:1 R:1
Bb4+D5+A5:4''',
 lh='''G3:1 D4:1 Bb3:2
F3:1 C4:1 A3:2
Eb3:1 Bb3:1 G3:1 R:1
R:4
C3+G3:2 R:2
F3:1 C4:1 Ab3:1 G3:1
D3+A3:2 R:2
F3:1 C4:1 R:2
Eb4:1 G4:1 A4:1 Bb4:1
D4:1 F4:1 G4:1 A4:1
C4:1 Eb4:1 F4:1 G4:1
F4:1 Ab4:1 Bb4:1 C5:1
E4:1 G4:1 A4:1 B4:1
F4:1 A4:1 G4:1 E4:1
D3+A3:2 Bb2+F3:2
Eb3:1 Bb3:1 G3:1 F3:1
F3+C4:3 R:1
Eb3+Bb3:3 R:1
R:4
G3:1 Bb3:1 D4:1 R:1
Eb3:1 Bb3:.5 D4:.5 G4:1 F4:1
C4:1 G4:.5 Eb4:.5 D4:1 C4:1
F3:1 C4:.5 Eb4:.5 A4:1 G4:1
Bb3:1 F4:.5 D4:.5 C4:1 Bb3:1
A3:1 D4:1 F3:1 R:1
G3+D4:4''',
 sections={1:'pp',5:'p',9:'pp',15:'p',17:'mp',18:'pp',21:'p',25:'pp'},lower_sections={1:'p',5:'pp',9:'p',15:'pp',20:'p',21:'pp'},words={17:'poco rubato',21:'a tempo'},slurs=[(2,2),(6,6),(8,8),(13,14),(15,17),(21,24)],lower_phrases=[(1,3),(9,11),(12,14),(20,20)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*4+a,i*4+b-.18] for i in range(26) if i not in [3,18] for a,b in ([(0,4)] if i==25 else [(0,2)] if i in [4,6,7] else [(0,3)] if i in [16,17,19] else [(0,2),(2,3)] if i in [2,24] else [(0,2),(2,4)])],
 performance=dict(rubato=[49,48,44,42,47,52,45,48,51,52,51,53,52,49,50,54,60,44,42,46,50,52,54,51,45,37],phrase_arcs=[[0,11,2],[20,24,3],[32,44,3],[44,56,4],[56,67,5],[80,96,4]],lower_entries=[[0,11],[32,56],[76,79]],pedal_lift=.18,gate=.99,note='The high bell is distant, the lower line intimate. Keep the single falling tuplet supple and the silences measured; the last ninth remains open.')),
dict(op=243,title='Willow Erratum',key='a',fifths=0,meter='5/4',bpm=56,final_fermata=False,
 description='An unfinished conversation is interrupted by a single unaccompanied flight. Fragments return changed, sometimes seeming to correct what came before. The melody eventually arrives in the left hand, with the right hand silent for its first complete statement. A brief minor-ninth chord ends the conversation.',
 difficulty='Advanced unaccompanied passagework and delayed bass-song revelation',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Bars 9–12 form one unaccompanied RH cadenza written in measured sixteenths. Shape it as a continuous contour rather than four separate patterns. The complete ancestral melody first appears alone in the LH at bar 19; let the following chords enter underneath its expressive weight.',
 parent_opus=231,motif=dict(hand='lh',start_beat=90,end_beat=95,pitches=['A','C','B','E']),ancestry=dict(source_opus=231,source_hand='rh',source_start_beat=0,source_end_beat=8,source_pitches=['D','F','E','A'],transposition_semitones=-17),
 system_starts=list(range(1,25,2)),page_starts=[7,13,19],engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=580),
 rh='''E5:2 G5:1 R:2
D5:1 F5:1 A5:2 R:1
R:5
C5+E5+G5:3 R:2
B4:1 D5:.5 F5:.5 E5:1 C5:2
A4:2 C5:1 R:2
D5:2 E5:1 G5:1 R:1
R:5
'''+ '\n'.join(' '.join(n+':.25' for n in row.split()) for row in '''A4 B4 C5 E5 G5 F5 E5 D5 C5 B4 A4 C5 E5 G5 A5 G5 E5 D5 C5 B4
C5 D5 E5 G5 B5 A5 G5 F5 E5 D5 C5 E5 G5 B5 C6 B5 G5 F5 E5 D5
F5 G5 A5 C6 E6 D6 C6 B5 A5 G5 F5 A5 C6 D6 C6 A5 G5 F5 E5 D5
E5 F5 G5 B5 D6 C6 B5 A5 G5 F5 E5 D5 C5 B4 A4 G4 F4 E4 D4 C4'''.splitlines())+'''
E4:2 R:3
C4+E4+A4:3 D4+F4+B4:2
E4+G4+C5:2 F4+A4+D5:2 R:1
C5:1 E5:1 G5:2 R:1
F5:2 D5:1 R:2
R:5
R:5
E4+G4+C5:5
F4+B4+D5:3 E4+A4+C5:2
E4+G4+C5:3 F4+A4+D5:2
E4+G4+C5:2 D4+F4+B4:2 R:1
E4+G4+A4+B4:2 R:3''',
 lh='''A2:1 E3:1 G3:1 R:2
F3:1 C4:1 A3:2 R:1
R:5
C3+G3:3 R:2
G2:1 D3:1 F3:1 E3:2
F2+C3:3 R:2
G2+D3:3 E3:1 R:1
R:5
R:5
R:5
R:5
R:5
R:5
F2+C3:3 G2+D3:2
A2+E3:2 D3+A3:2 R:1
C3:1 G3:1 E3:2 R:1
Bb2:1 F3:1 D3:1 R:2
R:5
A3:1.5 C4:.5 B3:1 E4:2
D4:1 C4:1 B3:1 A3:2
G3:1 B3:1 D4:1 C4:2
B3:1 G3:1 E3:1 F3:2
E3:1 G3:1 A3:2 R:1
A2+E3:2 R:3''',
 sections={1:'p',4:'pp',5:'p',9:'mp',13:'pp',14:'p',19:'pp'},lower_sections={1:'pp',19:'p',24:'pp'},words={9:'poco rubato',19:'a tempo'},slurs=[(1,1),(2,2),(5,6),(7,7),(9,12),(14,17),(20,23)],lower_phrases=[(19,21),(22,23)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*5+a,i*5+b-.18] for i in range(24) if i not in [2,7,12,17,18] for a,b in ([(0,2)] if i==23 else [(0,3)] if i in [0,3,5,16] else [(0,2),(2,4)] if i in [1,6,14,15,22] else [(0,1),(1,2),(2,3),(3,4),(4,5)] if 8<=i<=11 else [(0,3),(3,5)] if i in [13,20,21] else [(0,2),(2,5)])],
 performance=dict(rubato=[56,54,48,51,57,51,54,47,64,66,68,62,46,53,54,55,48,45,54,55,56,54,51,53],phrase_arcs=[[0,9,3],[20,29,3],[40,60,5],[65,84,3],[95,114,1]],lower_entries=[[90,114]],pedal_lift=.18,gate=.98,note='The cadenza is a single breath. The late unaccompanied bass melody should sound newly clear; its final chord is brief and followed by three beats of silence.')),
dict(op=244,title='Orchid Switchback',key='c#',fifths=4,meter='4/4',bpm=58,
 description='Held notes outlast their first harmony, then a stream of five-note figures carries them into another room. Fragments and paired octaves circle the still-missing melody. Its complete C-sharp-minor shape finally appears near the end, before the harmony settles unexpectedly in E major.',
 difficulty='Advanced quintuplet accompaniment, sustained ties and octave projection',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='The opening E5 lasts six quarter beats across the bar line. In bars 8–15, LH quintuplets flow beneath sustained upper notes; the final bar of that passage stops after its first group. Bars 21–25 project a restrained octave melody. The complete ancestral phrase arrives in bar 27.',
 parent_opus=237,motif=dict(hand='rh',start_beat=104,end_beat=108,pitches=['C#','E','D#','G#']),ancestry=dict(source_opus=237,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['F#','A','G#','C#'],transposition_semitones=-5),
 system_starts=list(range(1,33,2)),page_starts=[7,13,21,27],engraving=dict(spacing_system=18,spacing_staff=18,pedal_offset_y=580),
 tuplet_spans=[dict(hand='lh',start_beat=i*4+j,end_beat=i*4+j+2,actual=5,normal=4,stem='up',show_number='both') for i in range(7,15) for j in ([0] if i==14 else [0,2])],
 rh='''E5:4~
E5:2 R:2
D#5:3 R:1
F#5:2 G#5:1 R:1
E4+G#4+B4:4
F#4+A4+C#5:2 R:2
R:4
G#5:4
F#5:4
E5:4
D#5:4
F#5:4
E5:2 D#5:2
C#5:4
B4:2 R:2
E4+G#4+C#5:2 D#4+F#4+B4:2
D4+F#4+A4:3 R:1
C#5:2 R:2
F#5:1 E5:1 D#5:1 R:1
R:4
G#4+G#5:1 B4+B5:1 A4+A5:2
F#4+F#5:1 A4+A5:1 G#4+G#5:2
E4+E5:1 G#4+G#5:1 F#4+F#5:2
D#4+D#5:1 F#4+F#5:1 E4+E5:2
C#4+C#5:2 D#4+D#5:1 E4+E5:1
F#4:2 R:2
C#5:1 E5:.5 D#5:.5 G#5:2
F#5:1 E5:1 C#5:2
B4:1 D#5:.5 F#5:.5 G#5:2
A5:1 G#5:1 F#5:1 E5:1
D#5:1 B4:1 G#4:1 R:1
G#4+B4+D#5+F#5:4''',
 lh='''C#3+G#3:4
A2+E3:2 R:2
G#2+D#3:3 R:1
B2+F#3:3 R:1
E3+B3:4
D3+A3:2 R:2
R:4
'''+ '\n'.join(' '.join(n+':2/5' if ':' not in n else n for n in row.split()) for row in '''C#3 E3 G#3 B3 G#3 F#3 E3 D#3 C#3 E3
B2 D#3 F#3 A3 F#3 E3 D#3 C#3 B2 D#3
A2 C#3 E3 G#3 E3 D#3 C#3 B2 A2 C#3
G#2 B2 D#3 F#3 D#3 C#3 B2 A2 G#2 B2
B2 D#3 F#3 A3 F#3 E3 D#3 C#3 B2 D#3
A2 C#3 E3 G#3 E3 D#3 C#3 B2 A2 C#3
F#2 A2 C#3 E3 C#3 B2 A2 G#2 F#2 A2
G#2 B2 D#3 F#3 G#3 R:2'''.splitlines())+'''
A2+E3:2 B2+F#3:2
D3+A3:3 R:1
F#3+C#4:2 R:2
G#3:1 D#4:1 B3:1 R:1
R:4
E3:1 B3:1 G#3:1 F#3:1
D3:1 A3:1 F#3:1 E3:1
C#3:1 G#3:1 E3:1 D#3:1
B2:1 F#3:1 D#3:1 C#3:1
A2:1 E3:1 C#3:1 B2:1
G#2+D#3:2 R:2
A2:1 E3:.5 G#3:.5 C#4:1 B3:1
F#3:1 C#4:.5 A3:.5 G#3:1 F#3:1
E3:1 B3:.5 G#3:.5 F#3:1 E3:1
D3:1 A3:.5 F#3:.5 E3:1 D3:1
B2:1 F#3:1 A3:1 R:1
E3+B3:4''',
 sections={1:'p',5:'pp',8:'p',16:'pp',21:'mp',27:'p',31:'pp'},lower_sections={1:'pp',21:'p',27:'pp'},words={8:'poco rubato',27:'a tempo'},slurs=[(4,4),(13,15),(16,17),(19,19),(21,25),(27,30)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*4+a,i*4+b-.18] for i in range(32) if i not in [6,19] for a,b in ([(0,4)] if i==31 else [(0,2)] if i in [1,5,14,17,25] else [(0,3)] if i in [2,3,16,18,30] else [(0,2),(2,4)])],
 performance=dict(rubato=[58,52,51,55,52,49,45,59,60,61,60,61,59,56,49,51,48,47,53,45,61,62,61,59,56,48,57,58,60,58,49,39],phrase_arcs=[[0,6,2],[28,44,3],[44,58,4],[80,100,4],[104,120,4]],lower_entries=[],pedal_lift=.18,gate=.99,note='Let the tied note survive its change of bass, and keep the quintuplets soft. The octave passage is a contained outpouring; E major is a quiet surprise at the end.')),
dict(op=245,title='Bracken Ellipsis',key='d',fifths=-1,meter='4/4',meters=['4/4']*28+['5/4'],bpm=52,final_fermata=False,
 description='Chords seem to remember a song that has not yet been sung. A light triplet passage briefly gives them momentum, then the hands fall into an interrupted conversation. Only the final two bars name the missing melody: four unaccompanied notes, ending with the question still open.',
 difficulty='Advanced continuity through interrupted textures and triplet cantabile',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='The five-bar triplet passage should emerge lightly from the preceding chords. Later silence separates answers between the hands. The final two bars contain the complete ancestral D–C–A–G phrase alone in the RH; the last bar expands to five beats and keeps the pulse.',
 parent_opus=238,motif=dict(hand='rh',start_beat=108,end_beat=117,pitches=['D','C','A','G']),ancestry=dict(source_opus=238,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=5,source_pitches=['D','C','A','G'],transposition_semitones=12),
 system_starts=list(range(1,30,2)),page_starts=[7,13,19,25],engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=580),
 tuplet_spans=[dict(hand='rh',start_beat=i*4+j,end_beat=i*4+j+1,actual=3,normal=2,stem='down') for i in range(8,13) for j in range(3 if i==12 else 4)],
 rh='''F4+A4+C5:3 R:1
G4+Bb4+D5:2 F4+A4+C5:1 R:1
R:4
A4:2 C5:1 R:1
Bb4:1 D5:1 F5:2
E5:2 D5:1 R:1
F4+A4+D5:2 E4+G4+C5:1 R:1
R:4
'''+ '\n'.join(' '.join(n+':1/3' if ':' not in n else n for n in row.split()) for row in '''A4 C5 E5 F5 E5 C5 D5 C5 A4 G4 A4 C5
Bb4 D5 F5 G5 F5 D5 E5 D5 Bb4 A4 Bb4 D5
C5 Eb5 G5 Ab5 G5 Eb5 F5 Eb5 C5 Bb4 C5 Eb5
D5 F5 A5 Bb5 A5 F5 G5 F5 D5 C5 D5 F5
E5 G5 Bb5 A5 G5 E5 D5 C5 A4 R:1'''.splitlines())+'''
G4:3 R:1
R:4
R:4
A4:1 C5:1 R:2
R:4
Bb4:2 D5:1 R:1
R:4
F5:2 E5:1 D5:1
C5:1 A4:1 R:2
G4:1 Bb4:1 C5:1 R:1
F4+A4+D5:2 E4+G4+C5:2
D4+F4+Bb4:3 R:1
E4+G4+A4:2 R:2
R:4
D5:2 C5:2
A4:2 G4:3''',
 lh='''D3+A3:3 R:1
C3+G3:2 F3+C4:1 R:1
Bb2:1 F3:1 D3:1 R:1
R:4
G2:1 D3:1 Bb2:1 D3:1
A2+E3:3 R:1
Bb2+F3:2 C3+G3:1 R:1
R:4
F3:1 C4:1 A3:1 G3:1
G3:1 D4:1 Bb3:1 A3:1
Ab3:1 Eb4:1 C4:1 Bb3:1
Bb3:1 F4:1 D4:1 C4:1
A3:1 E4:1 G3:1 R:1
C3+G3:3 R:1
F3:1 A3:1 C4:1 R:1
R:4
R:4
G3:1 Bb3:1 D4:1 R:1
R:4
A3:1 C4:1 E4:1 R:1
Bb3:1 F3:1 D3:1 F3:1
A2+E3:2 R:2
G2+D3:3 R:1
Bb2+F3:2 C3+G3:2
G2+D3:3 R:1
A2+E3:2 R:2
R:4
R:4
R:5''',
 sections={1:'pp',5:'p',9:'mp',14:'pp',17:'p',24:'pp'},lower_sections={1:'pp',3:'p',5:'pp',15:'p',21:'pp'},words={9:'poco rubato',28:'a tempo'},slurs=[(2,2),(5,6),(7,7),(9,11),(12,13),(17,17),(19,19),(21,23),(24,26),(28,29)],lower_phrases=[(3,3),(15,15),(18,18),(20,20)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*4+a,i*4+b-.18] for i in range(26) if i not in [3,7,15,16,18] for a,b in ([(0,2)] if i in [21,25] else [(0,3)] if i in [0,1,2,5,6,12,13,14,17,19,22,24] else [(0,2),(2,4)])],
 performance=dict(rubato=[52,51,49,47,54,50,48,45,58,60,61,60,53,46,50,44,51,51,49,52,54,50,49,48,46,45,44,50,50],phrase_arcs=[[0,7,2],[16,23,3],[32,44,4],[44,51,4],[64,92,3],[92,104,2],[108,117,2]],lower_entries=[[8,11],[56,59],[68,71],[76,79]],pedal_lift=.18,gate=.98,note='Keep the unanswered spaces alive. The four notes at the end are a plain statement in tempo, with no accompaniment or final fermata.')),
dict(op=246,title='Sedge Meridian',key='d',fifths=-1,meter='5/4',bpm=58,final_fermata=False,
 description='A seven-note ground turns beneath a song in five beats. The song leaves that orbit for a spacious chordal passage, then gathers its energy into a brighter, higher arc. The returning ground becomes slower and more transparent, and the last phrase finds an unhurried major light.',
 difficulty='Advanced evolving ground, chord voicing and sustained melodic development',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='The opening seven LH bars carry ten complete repetitions of a seven-note cell across the five-beat barlines. The middle chordal passage opens the phrasing before a four-bar sixteenth-note crest. Keep that movement below the melody; the closing ground uses longer values.',
 parent_opus=235,motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['D','F','E','A']),ancestry=dict(source_opus=235,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),
 system_starts=list(range(1,37,2)),page_starts=[7,13,19,25,31],engraving=dict(spacing_system=18,spacing_staff=16,pedal_offset_y=570),
 rh='''D5:1 F5:.5 E5:.5 A5:3
G5:2 F5:1 E5:1 D5:1~
D5:2 C5:1 A4:2
Bb4:1 D5:1 F5:2 E5:1
D5:2 F5:.5 E5:.5 C5:2
A4:1 C5:1 E5:1 G5:2
F5:1 E5:1 D5:2 C5:1
A4:3 G4:1 R:1
F4+A4+D5:3 G4+Bb4+E5:2
A4+C5+F5:2 G4+Bb4+E5:1 F4+A4+D5:2
E4+G4+C5:3 F4+A4+D5:2
D4+F4+Bb4:2 E4+G4+C5:1 F4+A4+D5:2
G4+B4+E5:3 A4+C5+F#5:2
B4+D5+G5:2 A4+C5+F#5:1 G4+B4+E5:2
F#4+A4+D5:3 E4+G4+C5:2
D4+F4+A4:3 R:2
A4:1 D5:.5 F5:.5 E5:1 A5:2
G5:1 F5:.5 E5:.5 D5:1 C5:2
Bb4:1 D5:.5 F5:.5 A5:1 G5:2
F5:1 E5:.5 D5:.5 C5:1 A4:2
C5:1 F5:.5 A5:.5 G5:1 Bb5:2
A5:1 G5:.5 F5:.5 E5:1 D5:2
F5:1 A5:.5 C6:.5 Bb5:1 A5:2
G5:1 F5:.5 E5:.5 D5:1 C5:2
D5+F5+Bb5:2 C5+E5+A5:1 Bb4+D5+G5:2
A4+C5+F5:2 G4+Bb4+E5:1 F4+A4+D5:2
E4+G4+C5:3 F4+A4+D5:2
G4+Bb4+E5:2 F4+A4+D5:1 E4+G4+C5:2
D5:2 F5:1 E5:2
A5:2 G5:1 F5:2
E5:1 D5:1 C5:1 A4:2
G4:1 Bb4:1 D5:2 C5:1
B4:2 A4:1 F#4:2
G4:2 A4:1 D5:2
C#5:2 B4:1 A4:2
F#4+A4+D5:5''',
 lh='\n'.join(' '.join(n+':.5' for n in ('D3 F3 A3 C4 A3 F3 E3'.split()*10)[i*10:(i+1)*10]) for i in range(7))+'''
D3:1 A3:1 F3:1 E3:1 R:1
Bb2+F3:3 C3+G3:2
D3+A3:2 C3+G3:1 Bb2+F3:2
A2+E3:3 G2+D3:2
G2+D3:2 A2+E3:1 Bb2+F3:2
C3+G3:3 D3+A3:2
E3+B3:2 D3+A3:1 C3+G3:2
B2+F#3:3 A2+E3:2
D3+A3:3 R:2
D3:.5 F3:.5 A3:.5 C4:.5 A3:.5 F3:.5 E3:.5 D3:.5 F3:.5 A3:.5
C3:.5 E3:.5 G3:.5 Bb3:.5 G3:.5 E3:.5 D3:.5 C3:.5 E3:.5 G3:.5
Bb2:.5 D3:.5 F3:.5 A3:.5 F3:.5 D3:.5 C3:.5 Bb2:.5 D3:.5 F3:.5
A2:.5 C3:.5 E3:.5 G3:.5 E3:.5 C3:.5 B2:.5 A2:.5 C3:.5 E3:.5
'''+ '\n'.join(' '.join(n+':.25' for n in row.split()) for row in '''F3 A3 C4 E4 C4 A3 G3 F3 A3 C4 E4 C4 A3 G3 F3 A3 C4 E4 C4 A3
G3 Bb3 D4 F4 D4 Bb3 A3 G3 Bb3 D4 F4 D4 Bb3 A3 G3 Bb3 D4 F4 D4 Bb3
A3 C4 E4 G4 E4 C4 B3 A3 C4 E4 G4 E4 C4 B3 A3 C4 E4 G4 E4 C4
G3 Bb3 D4 F4 D4 Bb3 A3 G3 Bb3 D4 F4 D4 Bb3 A3 G3 Bb3 D4 F4 D4 Bb3'''.splitlines())+'''
Bb2+F3:2 C3+G3:1 D3+A3:2
F3+C4:2 E3+B3:1 D3+A3:2
C3+G3:3 Bb2+F3:2
A2+E3:2 Bb2+F3:1 C3+G3:2
D3:1 F3:1 A3:1 C4:1 A3:1
F3:1 E3:1 D3:1 F3:1 A3:1
C4:1 A3:1 F3:1 E3:1 D3:1
G2:1 D3:1 Bb3:1 A3:1 G3:1
G2+D3:3 B2+F#3:2
E3+B3:3 D3+A3:2
A2+E3:3 A3+E4:2
D3+A3:5''',
 sections={1:'p',9:'pp',13:'p',17:'mp',21:'mf',25:'mp',29:'p',33:'pp'},lower_sections={1:'pp',17:'p',21:'mp',25:'p',29:'pp'},words={},slurs=[(1,3),(4,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32),(33,36)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*5+a,i*5+b-.18] for i in range(36) for a,b in ([(0,4)] if i==7 else [(0,3)] if i==15 else [(0,3),(3,5)] if i in [8,10,12,14,26,32,33,34] else [(0,2),(2,3),(3,5)] if i in [9,11,13,24,25,27] else [(0,5)] if i==35 else [(0,2),(2,5)])],
 performance=dict(rubato=[58,59,58,59,58,59,57,53,54,55,54,53,56,57,55,51,59,60,61,60,63,64,65,62,59,58,56,55,57,56,55,54,54,53,53,52],phrase_arcs=[[0,15,3],[15,39,4],[40,60,3],[60,78,4],[80,100,5],[100,120,6],[120,140,4],[140,160,3],[160,180,2]],lower_entries=[],pedal_lift=.18,gate=.98,note='Grow through the long phrases, allowing the chordal space to breathe. The last chord settles within the continuing pulse, without an added fermata.')),
dict(op=247,title='Camellia Reach',key='e',fifths=1,meter='7/4',bpm=60,
 description='An uneven chorale opens into a long view. Its upper melody remains spacious while the interior voices quietly alter the harmony. A remote B-flat passage and a rising cantabile lead back to the first song, now supported by different bass notes; the ending rests in an unexpected A-major light.',
 difficulty='Advanced three-voice cantabile and chromatic chord balance',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=8),technical_note='Separate the RH singing line from the written inner dyads. The wide seven-beat bars allow the interior harmony to change beneath sustained notes. The middle rising phrase is supported by a more mobile LH; the return should remember the opening without copying its weight.',
 parent_opus=239,motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=7,pitches=['E','G','F#','B']),ancestry=dict(source_opus=239,source_hand='rh',source_start_beat=0,source_end_beat=7,source_pitches=['G','Bb','A','D'],transposition_semitones=-3),
 system_starts=list(range(1,29,2)),page_starts=[7,13,19,25],engraving=dict(spacing_system=19,spacing_staff=25,pedal_offset_y=610),
 rh='''E5:2 G5:1 F#5:2 B5:2
A5:3 G5:2 E5:2
F#5:4 E5:1 D5:2
C5:3 B4:2 A4:2
E5:4 G5:3
F#5:3 E5:2 D5:2
C5:2 E5:1 D5:2 B4:2
A4:4 R:3
D5:3 F5:2 A5:2
G5:4 F5:1 E5:2
Eb5:3 D5:2 C5:2
Bb4:4 A4:3
G4:3 Bb4:2 D5:2
C5:3 A4:2 R:2
B4:2 E5:1 F#5:1 G5:3
A5:3 G5:2 F#5:2
E5:2 G5:1 A5:1 B5:3
C6:3 B5:2 A5:2
G5:3 F#5:2 E5:2
D5:2 F#5:1 E5:2 C5:2
B4:3 D5:2 F#5:2
E5:4 R:3
E5:2 G5:1 F#5:2 B5:2
A5:3 G5:2 E5:2
D5:3 C#5:2 B4:2
A4:3 B4:2 E5:2
D5:3 B4:2 G#4:2
C#5:7''',
 rh_inner='''G4+B4:2 B4+D5:1 A4+C5:2 D5+F#5:2
C5+E5:2 C#5+E5:1 B4+D5:2 G4+B4:2
A4+C5:2 A#4+C#5:2 G4+B4:1 F#4+A4:2
E4+G4:3 D4+F#4:2 C4+E4:2
G4+B4:2 G#4+B4:2 B4+D5:3
A4+C5:2 A#4+C#5:1 G4+B4:2 F#4+A4:2
E4+G4:2 G4+B4:1 F#4+A4:2 D4+F#4:2
C4+E4:2 C4+F4:2 R:3
F4+A4:3 A4+C5:2 C5+E5:2
Bb4+D5:2 B4+D5:2 A4+C5:1 G4+B4:2
G4+Bb4:3 F4+A4:2 Eb4+G4:2
D4+F4:2 Eb4+G4:2 C4+E4:3
Bb3+D4:3 D4+F4:2 F4+A4:2
E4+G4:3 C4+E4:2 R:2
D4+F#4:2 G4+B4:1 A4+C5:1 B4+D5:3
C5+E5:3 B4+D5:2 A4+C5:2
G4+B4:2 B4+D5:1 C5+E5:1 D5+F#5:3
E5+G5:3 D5+F#5:2 C5+E5:2
B4+D5:3 A4+C5:2 G4+B4:2
F#4+A4:2 A4+C5:1 G4+B4:2 E4+G4:2
D4+F#4:3 F#4+A4:2 A4+C5:2
G4+B4:2 F#4+A4:2 R:3
G4+B4:2 B4+D5:1 A4+C5:2 D5+F#5:2
C5+E5:2 C#5+E5:1 B4+D5:2 G4+B4:2
F#4+A4:3 E4+G#4:2 D4+F#4:2
C#4+E4:3 D4+F#4:2 G#4+B4:2
F#4+A4:3 D4+F#4:2 B3+E4:2
G#4+B4:7''',
 lh='''E3+B3:3 D3+A3:2 C3+G3:2
A2+E3:3 B2+F#3:2 C3+G3:2
D3+A3:4 C3+G3:1 B2+F#3:2
A2+E3:3 G2+D3:2 F#2+C#3:2
C3+G3:4 E3+B3:3
D3+A3:3 C3+G3:2 B2+F#3:2
A2+E3:3 B2+F#3:2 G2+D3:2
F#2+C#3:4 R:3
Bb2+F3:3 D3+A3:2 F3+C4:2
Eb3+Bb3:4 D3+A3:1 C3+G3:2
Ab2+Eb3:3 Bb2+F3:2 C3+G3:2
G2+D3:4 F2+C3:3
Eb2+Bb2:3 F2+C3:2 G2+D3:2
A2+E3:3 F#2+C#3:2 R:2
E3:1 B3:1 G3:1 D4:1 B3:1 A3:1 G3:1
F#3:1 C4:1 A3:1 E4:1 C4:1 B3:1 A3:1
G3:1 D4:1 B3:1 F#4:1 D4:1 C4:1 B3:1
A3:1 E4:1 C4:1 G4:1 E4:1 D4:1 C4:1
B2:1 F#3:1 D3:1 A3:1 F#3:1 E3:1 D3:1
C3:1 G3:1 E3:1 B2:1 A2:1 G2:1 E3:1
F#3:1 C4:1 A3:1 G3:1 F#3:1 E3:1 D3:1
E3+B3:4 R:3
C3+G3:3 D3+A3:2 G3+D4:2
F#3+C4:3 E3+B3:2 A2+E3:2
B2+F#3:3 A2+E3:2 G#2+D#3:2
F#2+C#3:3 G#2+D#3:2 C#3+G#3:2
B2+F#3:3 E3+B3:2 E2+B2:2
A2+E3:7''',
 sections={1:'p',5:'pp',9:'p',15:'mp',17:'mf',19:'mp',23:'p',25:'pp'},lower_sections={1:'pp',15:'p',17:'mp',19:'p',23:'pp'},words={28:'poco rit.'},slurs=[(1,4),(5,8),(9,12),(13,14),(15,18),(19,22),(23,24),(25,28)],hairpins=[],tempo_changes={},group=3,
 voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=2) for a,b in [(0,28),(28,53),(56,84),(98,126),(154,168),(168,189)]],
 pedal_spans=[[i*7+a,i*7+b-.2] for i in range(28) for a,b in ([(0,2),(2,3),(3,5),(5,7)] if i in [0,1,5,6,10,14,16,19,22,23] else [(0,2),(2,4),(4,5),(5,7)] if i in [2,9] else [(0,2),(2,4)] if i in [7,21] else [(0,2),(2,4),(4,7)] if i in [4,11] else [(0,3),(3,5)] if i==13 else [(0,7)] if i==27 else [(0,3),(3,5),(5,7)])],
 performance=dict(rubato=[60,61,60,58,59,60,58,54,59,60,58,56,57,53,61,62,64,65,62,61,59,55,60,59,57,56,54,50],phrase_arcs=[[0,28,3],[28,53,3],[56,84,4],[84,96,2],[98,126,6],[126,151,4],[154,168,3],[168,196,2]],lower_entries=[[98,147]],inner_entries=[[0,28],[28,53],[56,84],[154,189]],pedal_lift=.2,gate=1.0,note='Bring the upper phrase through changing inner colours. The six-bar LH ascent builds one long crest, then releases its energy before the transformed return.')),
dict(op=248,title='Lichen Outlook',key='d',fifths=-1,meter='4/4',bpm=52,final_fermata=False,
 description='A hesitant four-note song discovers a flowing triplet landscape, then gives its melody to the bass. The return opens into singing octaves above displaced left-hand chords. After that broad crest, quiet fragments gather into a plain, unresolved last line.',
 difficulty='Advanced triplet cantabile, singing octaves and displaced accompaniment',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='Let the triplet section form a continuous eight-bar thought, with the last beat released into silence. The later RH octaves need a singing top note over a lightly syncopated LH. Four unaccompanied bass bars prepare that return, and the last three bars withdraw the accompaniment again.',
 parent_opus=242,motif=dict(hand='rh',start_beat=0,end_beat=8,pitches=['D','F','E','C']),ancestry=dict(source_opus=242,source_hand='rh',source_start_beat=80,source_end_beat=84,source_pitches=['G','Bb','A','F'],transposition_semitones=-5),
 system_starts=list(range(1,39,2)),page_starts=[7,13,19,25,33],engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=580),
 tuplet_spans=[dict(hand='rh',start_beat=i*4+j,end_beat=i*4+j+1,actual=3,normal=2,stem='down') for i in range(6,14) for j in range(3 if i==13 else 4)],
 rh='''D5:2 R:2
F5:1 E5:1 C5:2
A4:3 R:1
G4:1 Bb4:1 D5:2
E5:2 C5:1 A4:1
D5:2 R:2
'''+ '\n'.join(' '.join(n+':1/3' if ':' not in n else n for n in row.split()) for row in '''A4 C5 E5 F5 E5 C5 D5 C5 A4 G4 A4 C5
Bb4 D5 F5 G5 F5 D5 E5 D5 Bb4 A4 Bb4 D5
C5 E5 G5 A5 G5 E5 F5 E5 C5 Bb4 C5 E5
D5 F5 A5 Bb5 A5 F5 G5 F5 D5 C5 D5 F5
Eb5 G5 Bb5 C6 Bb5 G5 Ab5 G5 Eb5 D5 Eb5 G5
D5 F#5 A5 B5 A5 F#5 G5 F#5 D5 C5 D5 F#5
C5 E5 G5 A5 G5 E5 F5 E5 C5 Bb4 C5 E5
Bb4 D5 F5 E5 D5 Bb4 A4 G4 F4 R:1'''.splitlines())+'''
R:4
R:4
R:4
R:4
D4+D5:1 F4+F5:.5 E4+E5:.5 C4+C5:2
A3+A4:1 C4+C5:1 D4+D5:2
F4+F5:1 A4+A5:.5 G4+G5:.5 E4+E5:2
D4+D5:1 F4+F5:1 G4+G5:2
A4+A5:1 C5+C6:.5 Bb4+Bb5:.5 G4+G5:2
F4+F5:1 A4+A5:1 G4+G5:2
E4+E5:1 G4+G5:.5 F4+F5:.5 D4+D5:2
C4+C5:1 A3+A4:1 R:2
F4+A4+D5:3 G4+Bb4+E5:1
A4+C5+F5:2 G4+Bb4+E5:2
E4+G4+C5:3 F4+A4+D5:1
D4+F4+Bb4:2 E4+G4+C5:2
F4+A4+D5:3 R:1
E4+G4+A4:2 R:2
D5:2 F5:1 E5:1
C5:3 A4:1
Bb4:2 G4:2
A4:2 C5:1 E5:1
D5:2 C5:1 A4:1
G4:4''',
 lh='''D3+A3:2 R:2
Bb2+F3:2 C3+G3:2
F3+C4:3 R:1
G2:1 D3:1 Bb2:1 D3:1
A2:1 E3:1 G3:1 E3:1
D3+A3:2 R:2
F3:1 C4:1 A3:1 G3:1
G3:1 D4:1 Bb3:1 A3:1
A3:1 E4:1 C4:1 B3:1
Bb3:1 F4:1 D4:1 C4:1
C4:1 G4:1 Eb4:1 D4:1
B3:1 F#4:1 D4:1 C4:1
A3:1 E4:1 C4:1 B3:1
G3:1 D4:1 Bb3:1 R:1
D3:2 F3:1 E3:1
C3:3 A2:1
Bb2:2 D3:1 F3:1
E3:2 C3:1 R:1
Bb2:.5 D3+F3:1.5 C3:.5 E3+G3:1.5
F2:.5 A2+C3:1.5 G2:.5 Bb2+D3:1.5
D3:.5 F3+A3:1.5 C3:.5 E3+G3:1.5
Bb2:.5 D3+F3:1.5 C3:.5 E3+G3:1.5
F3:.5 A3+C4:1.5 Eb3:.5 G3+Bb3:1.5
D3:.5 F3+A3:1.5 E3:.5 G3+B3:1.5
A2:.5 C3+E3:1.5 Bb2:.5 D3+F3:1.5
F2:.5 A2+C3:1.5 R:2
Bb2+F3:3 C3+G3:1
D3+A3:2 C3+G3:2
A2+E3:3 G2+D3:1
G2+D3:2 A2+E3:2
D3+A3:3 R:1
C3+G3:2 R:2
Bb2+F3:2 A2+E3:2
G2+D3:3 F2+C3:1
Eb2+Bb2:2 C3+G3:2
R:4
R:4
R:4''',
 sections={1:'pp',4:'p',7:'mp',11:'mf',14:'p',19:'mp',23:'mf',25:'p',27:'pp',33:'p',36:'pp'},lower_sections={1:'pp',15:'p',19:'pp',23:'p',27:'pp'},words={7:'poco rubato',19:'a tempo'},slurs=[(2,3),(4,6),(7,10),(11,14),(19,22),(23,26),(27,30),(31,32),(33,35),(36,38)],lower_phrases=[(15,18)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*4+a,i*4+b-.18] for i in range(35) for a,b in ([(0,2)] if i in [0,5,25,31] else [(0,3)] if i in [2,13,17,30] else [(0,3),(3,4)] if i in [26,28,33] else [(0,2),(2,4)])],
 performance=dict(rubato=[52,53,50,54,53,48,56,57,58,59,60,59,57,51,52,51,53,49,54,55,56,57,59,58,55,50,51,52,51,50,48,46,51,50,49,50,50,50],phrase_arcs=[[0,11,2],[12,22,3],[24,40,5],[40,55,5],[56,71,3],[72,88,4],[88,102,5],[104,120,3],[128,140,3],[140,152,2]],lower_entries=[[56,71]],pedal_lift=.18,gate=.98,note='Carry the motion through the triplet section and allow the written silence to open naturally. Return with broad, warm octaves, then let the final unaccompanied line keep its pulse.')),
dict(op=249,title='Orchid Headland',key='c#',fifths=4,meter='8/4',meters=['8/4']*18+['6/4']*8,bpm=62,final_fermata=False,
 description='Broad chords move in uneven breaths above an even harmonic floor. A rippling quintuplet passage opens the view, followed by a melody in thirds that gradually loses its weight. Six-beat phrases carry the return into a softer landscape, where a short minor chord keeps a little brightness in reserve.',
 difficulty='Advanced chordal grouping, quintuplet accompaniment and melodic thirds',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='After the four-note opening, the RH chords breathe in groups of three, three and two beats above two-beat LH changes. Bars 9–12 place five LH notes inside each two-beat group. Let the later thirds sing as one line, and feel the contraction from eight beats to six before the close.',
 parent_opus=244,motif=dict(hand='rh',start_beat=0,end_beat=8,pitches=['C#','E','D#','G#']),ancestry=dict(source_opus=244,source_hand='rh',source_start_beat=104,source_end_beat=108,source_pitches=['C#','E','D#','G#'],transposition_semitones=0),
 system_starts=list(range(1,27,2)),page_starts=[7,13,19,25],engraving=dict(spacing_system=18,spacing_staff=21,pedal_offset_y=600),
 tuplet_spans=[dict(hand='lh',start_beat=i*8+j,end_beat=i*8+j+2,actual=5,normal=4,stem='down',placement='below') for i in range(8,12) for j in [0,2,4,6]],
 rh='''E4+G#4+C#5:2 G#4+B4+E5:2 F#4+A4+D#5:2 B4+D#5+G#5:2
A4+C#5+F#5:3 G#4+B4+E5:3 E4+G#4+C#5:2
F#4+A4+D#5:3 E4+G#4+C#5:3 D#4+F#4+B4:2
C#4+E4+A4:3 D#4+F#4+B4:3 E4+G#4+C#5:2
F#4+A4+D5:3 A4+C#5+F#5:3 G#4+B4+E5:2
G4+B4+E5:3 F#4+A4+D5:3 E4+G4+C5:2
F4+A4+D5:3 E4+G4+C5:3 D4+F4+Bb4:2
E4+G#4+B4:3 F#4+A4+C#5:3 R:2
C#5:2 E5:1 D#5:1 G#5:2 F#5:2
E5:2 G#5:1 B5:1 A5:2 G#5:2
F#5:2 A5:1 C#6:1 B5:2 A5:2
G#5:2 F#5:1 E5:1 D#5:2 C#5:2
E5+G#5:1 D#5+F#5:.5 C#5+E5:.5 B4+D#5:1 C#5+E5:2 D#5+F#5:1 E5+G#5:2
F#5+A5:1 E5+G#5:.5 D#5+F#5:.5 C#5+E5:1 B4+D#5:2 A4+C#5:1 G#4+B4:2
A4+C#5:1 B4+D#5:.5 C#5+E5:.5 D#5+F#5:1 E5+G#5:2 D#5+F#5:1 C#5+E5:2
B4+D#5:1 A4+C#5:.5 G#4+B4:.5 F#4+A4:1 E4+G#4:2 F#4+A4:1 G#4+B4:2
A4+C#5:2 G#4+B4:1 F#4+A4:1 E4+G#4:2 D#4+F#4:2
E4+G#4:3 F#4+A4:2 G#4+B4:1 R:2
E4+G#4+C#5:3 F#4+A4+D#5:3
G#4+B4+E5:2 F#4+A4+D#5:2 E4+G#4+C#5:2
D#4+F#4+B4:3 E4+G#4+C#5:3
C#4+E4+A4:2 D#4+F#4+B4:2 E4+G#4+C#5:2
D#5:2 E5:1 G#5:3
F#5:2 E5:1 C#5:3
B4:2 G#4:2 F#4:2
E4+G#4+D#5:4 R:2''',
 lh='''C#3+G#3:2 E3+B3:2 B2+F#3:2 A2+E3:2
D3+A3:2 F#3+C#4:2 E3+B3:2 C#3+G#3:2
B2+F#3:2 A2+E3:2 G#2+D#3:2 F#2+C#3:2
F#2+C#3:2 G#2+D#3:2 A2+E3:2 B2+F#3:2
B2+F#3:2 D3+A3:2 C#3+G#3:2 B2+F#3:2
C3+G3:2 B2+F#3:2 A2+E3:2 G2+D3:2
Bb2+F3:2 A2+E3:2 G2+D3:2 F2+C3:2
E2+B2:2 G#2+D#3:2 F#2+C#3:2 R:2
'''+ '\n'.join(' '.join(n+':2/5' for n in row.split()) for row in '''C#3 E3 G#3 B3 G#3 E3 F#3 A3 C#4 A3 F#3 G#3 B3 D#4 B3 G#3 E3 F#3 G#3 B3
A3 C#4 E4 G#4 E4 C#4 B3 C#4 E4 G#4 E4 C#4 A3 B3 C#4 E4 C#4 B3 A3 G#3
B3 D4 F#4 A4 F#4 D4 C#4 D4 F#4 A4 F#4 D4 B3 C#4 D4 F#4 D4 C#4 B3 A3
G#3 B3 D#4 F#4 D#4 B3 A3 B3 D#4 F#4 D#4 B3 G#3 A3 B3 D#4 B3 A3 G#3 F#3'''.splitlines())+'''
E3:1 B3:1 G#3:1 F#3:1 A3:1 C#4:1 B3:1 G#3:1
F#3:1 C#4:1 A3:1 G#3:1 E3:1 B3:1 G#3:1 F#3:1
D3:1 A3:1 F#3:1 E3:1 C#3:1 G#3:1 E3:1 D#3:1
B2:1 F#3:1 D#3:1 C#3:1 A2:1 E3:1 C#3:1 B2:1
F#2:1 C#3:1 A2:1 B2:1 C#3:1 D#3:1 E3:1 F#3:1
G#2+B2:3 A2+C#3:2 B2+D#3:1 R:2
A2+E3:3 B2+F#3:3
C#3+G#3:2 B2+F#3:2 A2+E3:2
G#2+D#3:3 F#2+C#3:3
F#2+C#3:2 G#2+D#3:2 A2+E3:2
B2:1 F#3:1 D#3:1 A3:1 G#3:1 F#3:1
A2:1 E3:1 C#3:1 G#3:1 F#3:1 E3:1
G#2+D#3:2 F#2+C#3:2 B2+F#3:2
C#3+A#3:4 R:2''',
 sections={1:'p',5:'pp',9:'mp',11:'mf',13:'mp',17:'p',19:'pp',23:'p',25:'pp'},lower_sections={1:'pp',9:'p',11:'mp',13:'p',17:'pp'},words={9:'poco rubato',19:'a tempo'},slurs=[(1,4),(5,8),(9,12),(13,14),(15,16),(17,18),(19,22),(23,26)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[start+a,start+b-.18] for i,(start,length) in enumerate(zip([i*8 for i in range(18)]+[144+i*6 for i in range(8)],[8]*18+[6]*8)) for a,b in ([(0,4)] if i==25 else [(0,2),(2,3),(3,4),(4,6)] if i in [7,17] else [(0,2),(2,3),(3,4),(4,6),(6,8)] if 1<=i<=6 else [(0,3),(3,6)] if i in [18,20] else [(j,j+2) for j in range(0,length,2)])],
 performance=dict(rubato=[62,63,61,59,60,59,58,54,64,65,67,64,63,64,63,61,59,55,60,59,58,57,60,59,58,58],phrase_arcs=[[0,32,4],[32,62,3],[64,96,6],[96,112,4],[112,128,4],[128,142,3],[144,168,3],[168,190,2]],lower_entries=[],pedal_lift=.18,gate=.98,note='Allow the broad chordal rhythm and the interior pulse to coexist. The quintuplets crest once; the final six-beat section contracts the space, ending in tempo with written silence.')),
dict(op=250,title='Bracken Horizon',key='d',fifths=-1,meter='6/4',bpm=56,final_fermata=False,
 description='A descending song follows a small revolving bass into an open landscape. Seven-note flights loosen the pulse before the hands pause to answer one another. The song returns as a broad chorale, with warmer bass notes and a fuller crest; its final descent is left alone, quietly within reach.',
 difficulty='Advanced septuplet cantabile, evolving ground and long-form chord voicing',technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note='The first five LH bars repeat a five-note quarter-note cell continuously across six-beat bars. Bars 9–16 place seven RH eighth-notes inside each three-beat group, explicitly marked 7:6; do not accent every group boundary. The later chordal return gathers the same downward song into a broader sound, then releases the accompaniment before the final bar.',
 parent_opus=245,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['D','C','A','G']),ancestry=dict(source_opus=245,source_hand='rh',source_start_beat=108,source_end_beat=117,source_pitches=['D','C','A','G'],transposition_semitones=0),
 system_starts=list(range(1,33,2)),page_starts=[7,13,19,25],engraving=dict(spacing_system=18,spacing_staff=19,pedal_offset_y=590),
 tuplet_spans=[dict(hand='rh',start_beat=i*6+j,end_beat=i*6+j+3,actual=7,normal=6,stem='down',show_number='both') for i in range(8,16) for j in [0,3]],
 rh='''D5:2 C5:1 A4:1 G4:2
A4:2 C5:1 E5:1 F5:2
E5:3 D5:1 C5:2
Bb4:2 D5:1 F5:1 E5:2
D5:2 F5:1 A5:1 G5:2
F5:1 E5:1 D5:2 C5:2
A4:2 C5:1 E5:1 D5:2
G4:3 A4:1 R:2
'''+ '\n'.join(' '.join(n+':3/7' for n in row.split()) for row in '''D5 F5 A5 G5 E5 D5 C5 A4 C5 E5 F5 E5 C5 A4
E5 G5 Bb5 A5 F5 E5 D5 Bb4 D5 F5 G5 F5 D5 Bb4
F5 A5 C6 Bb5 G5 F5 E5 C5 E5 G5 A5 G5 E5 C5
G5 Bb5 D6 C6 A5 G5 F5 D5 F5 A5 Bb5 A5 F5 D5
Ab5 C6 Eb6 D6 Bb5 Ab5 G5 Eb5 G5 Bb5 C6 Bb5 G5 Eb5
G5 B5 D6 C6 A5 G5 F#5 D5 F#5 A5 B5 A5 F#5 D5
F5 A5 C6 Bb5 G5 F5 E5 C5 E5 G5 A5 G5 E5 C5
E5 G5 Bb5 A5 F5 E5 D5 Bb4 D5 F5 E5 D5 Bb4 A4'''.splitlines())+'''
D5:2 C5:1 R:3
R:6
A4:2 G4:1 R:3
R:6
F4+A4+D5:3 E4+G4+C5:1 D4+F4+A4:2
E4+G4+C5:2 G4+Bb4+E5:1 A4+C5+F5:3
G4+B4+E5:3 F#4+A4+D5:1 E4+G4+C5:2
F4+A4+D5:2 A4+C5+F5:1 G4+Bb4+E5:3
A4+C5+F5:2 C5+E5+A5:1 Bb4+D5+G5:3
A4+C5+F5:1 G4+Bb4+E5:1 F4+A4+D5:2 E4+G4+C5:2
D4+F4+A4:2 E4+G4+C5:1 F4+A4+D5:3
E4+G4+C5:3 D4+F4+A4:1 R:2
D5:2 C5:1 A4:1 G4:2
A4:2 C5:1 E5:1 D5:2
C5:2 A4:1 F4:1 E4:2
G4:2 F4:1 E4:1 D4:2''',
 lh='\n'.join(' '.join(n+':1' for n in ('D3 A3 C4 F3 E3'.split()*6)[i*6:(i+1)*6]) for i in range(5))+'''
Bb2:1 F3:1 A3:1 D3:1 C3:1 Bb2:1
F3:1 C4:1 E4:1 A3:1 G3:1 F3:1
G2:1 D3:1 Bb3:1 A3:1 R:2
D3:1 A3:1 F3:1 E3:1 G3:1 A3:1
Eb3:1 Bb3:1 G3:1 F3:1 A3:1 Bb3:1
F3:1 C4:1 A3:1 G3:1 B3:1 C4:1
G3:1 D4:1 Bb3:1 A3:1 C4:1 D4:1
Ab3:1 Eb4:1 C4:1 Bb3:1 D4:1 Eb4:1
G3:1 D4:1 B3:1 A3:1 C4:1 D4:1
F3:1 C4:1 A3:1 G3:1 B3:1 C4:1
E3:1 Bb3:1 G3:1 F3:1 A3:1 Bb3:1
R:6
A3:2 G3:1 F3:2 R:1
R:6
E3:2 G3:1 A3:2 R:1
Bb2+F3:3 C3+G3:1 D3+A3:2
A2+E3:2 C3+G3:1 D3+A3:3
C3+G3:3 B2+F#3:1 A2+E3:2
Bb2+F3:2 D3+A3:1 C3+G3:3
F3+C4:2 A3+E4:1 G3+D4:3
F3+C4:1 E3+B3:1 D3+A3:2 C3+G3:2
Bb2+F3:2 C3+G3:1 D3+A3:3
A2+E3:3 Bb2+F3:1 R:2
G2+D3:2 A2+E3:2 Bb2+F3:2
F3+C4:2 E3+B3:2 D3+A3:2
C3+G3:2 Bb2+F3:2 A2+E3:2
R:6''',
 sections={1:'p',5:'mp',8:'p',9:'mp',13:'mf',16:'p',17:'pp',21:'p',25:'mf',27:'p',29:'pp'},lower_sections={1:'pp',9:'p',13:'mp',16:'pp',18:'p',21:'pp',25:'p',27:'pp'},words={9:'poco rubato',21:'a tempo'},slurs=[(1,4),(5,8),(9,12),(13,16),(17,17),(19,19),(21,24),(25,28),(29,31),(32,32)],lower_phrases=[(18,18),(20,20)],hairpins=[],tempo_changes={},group=3,
 pedal_spans=[[i*6+a,i*6+b-.18] for i in range(31) if i not in [16,18] for a,b in ([(0,2),(2,4)] if i==7 else [(0,5)] if i in [17,19] else [(0,3),(3,4)] if i==27 else [(0,3),(3,4),(4,6)] if i in [20,22] else [(0,2),(2,3),(3,6)] if i in [21,23,24,26] else [(0,1),(1,2),(2,4),(4,6)] if i==25 else [(0,2),(2,4),(4,6)])],
 performance=dict(rubato=[56,57,56,57,59,58,57,51,59,60,61,62,63,62,60,54,48,50,48,51,56,57,58,59,61,59,56,51,54,53,52,52],phrase_arcs=[[0,24,3],[24,46,4],[48,72,5],[72,96,6],[96,119,2],[120,144,4],[144,166,5],[168,186,2],[186,192,1]],lower_entries=[[102,107],[114,119]],pedal_lift=.18,gate=.98,note='Keep one long breath through each seven-note flight. The chordal return has a single crest, after which the last line becomes plain and unaccompanied, without an added fermata.'))
]
