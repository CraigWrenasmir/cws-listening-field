"""Interwoven Songs, CWS Op. 351–360. Explicitly authored counterpoint."""
from weather_common import make_study
PIECES=[]
def study(**kwargs):
    p=make_study(**kwargs);PIECES.append(p);return p

p=study(op=351,title='Quince Tandem',key='d',fifths=-1,meter='3/4',bpm=53,parent=349,
 source=dict(source_opus=349,source_hand='rh',source_start_beat=0,source_end_beat=7,source_pitches=['F','Ab','G','C'],transposition_semitones=-3),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['D','F','E','A']),
 description='A seven-bar upper song and a five-bar lower song are heard alone before meeting. The lower phrase finishes sooner and gives its partner room to close. After a brief episode the original upper song moves down an octave and the lower one up an octave, reversing their positions. A short shared cadence finally introduces a deeper bass.',
 technical='Let the two unaccompanied openings establish different phrase rhythms. Preserve both melodic identities in the first combination and their later register exchange. The lower hand begins in the treble clef; prepare its return to the bass clef at the short final cadence without making the new depth heavy.',
 rh='''D5:1 F5:.5 E5:.5 A5:1
G5:1 F5:1 E5:1
F5:2 D5:1
E5:1 G5:1 F5:1
D5:1 C#5:1 E5:1
F5:1 E5:1 D5:1
C#5:1 D5:2
R:3
R:3
R:3
R:3
R:3
D5:1 F5:.5 E5:.5 A5:1
G5:1 F5:1 E5:1
F5:2 D5:1
E5:1 G5:1 F5:1
D5:1 C#5:1 E5:1
F5:1 E5:1 D5:1
C#5:1 D5:2
G5:1 Bb5:.5 A5:.5 G5:1
F5:1 Eb5:1 D5:1
C#5:1 E5:1 G5:1
F5:2 R:1
F5:1 G5:1.5 F5:.5
E5:1.5 D5:.5 C#5:1
D5:1 F5:1.5 A5:.5
G5:1 E5:1.5 D5:.5
F5:1 E5:.5 D5:.5 C#5:1
Bb4:1 C5:1 F5:1
E5:1 D5:2
D5:1 F5:.5 E5:.5 A5:1
G5:1 F5:1 E5:1
D5:1 Bb4:1 G4:1
A4:1 G4:1 E4:1
F4+A4:2 R:1''',
 lh='''R:3
R:3
R:3
R:3
R:3
R:3
R:3
F4:1 G4:1.5 F4:.5
E4:1.5 D4:.5 C#4:1
D4:1 F4:1.5 A4:.5
G4:1 E4:1.5 D4:.5
F4:1 E4:.5 D4:.5 C#4:1
F4:1 G4:1.5 F4:.5
E4:1.5 D4:.5 C#4:1
D4:1 F4:1.5 A4:.5
G4:1 E4:1.5 D4:.5
F4:1 E4:.5 D4:.5 C#4:1
Bb3:1 C4:1 F4:1
E4:1 D4:2
Eb4:1 D4:1 Bb3:1
D4:1 F4:1 Bb4:1
A4:1 G4:1 E4:1
A3:2 R:1
D4:1 F4:.5 E4:.5 A4:1
G4:1 F4:1 E4:1
F4:2 D4:1
E4:1 G4:1 F4:1
D4:1 C#4:1 E4:1
F4:1 E4:1 D4:1
C#4:1 D4:2
D3:1 F3:.5 E3:.5 A3:1
Bb2:1 F3:1 D3:1
G2:1 D3:1 Bb2:1
A2:1 C#3:1 G3:1
D3+A3+B3:2 R:1''',
 tempos=[53,54,53,54,52,53,51,53,54,55,54,52,54,55,54,55,53,54,52,56,55,54,52,54,55,54,55,53,54,52,53,54,53,52,52],
 phrases=[(1,7),(13,19),(20,23),(24,28),(29,30),(31,35)],lower_phrases=[(8,12),(13,17),(18,19),(20,23),(24,30),(31,35)],sections={1:'p',13:'mp',20:'mp',24:'mp',29:'p',31:'p',34:'pp'},lower_sections={1:'p',8:'mp',13:'p',20:'p',24:'mp',31:'pp'},
 clef_changes={'lh':{1:'treble',31:'bass'}},pedal=[[i*3+.05,i*3+(1.8 if i in [22,34] else 2.8)] for i in range(35)],hairpins=[('crescendo',13,16),('diminuendo',24,28)],page_starts=[9,17,25,31],system_starts=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35])
p['performance']['lower_entries']=[[21,36],[69,90]]

p=study(op=352,title='Larch Crossroads',key='Bb',fifths=-2,meter='6/4',bpm=56,parent=350,
 source=dict(source_opus=350,source_hand='rh',source_start_beat=60,source_end_beat=63,source_pitches=['E','D#','C#','B'],transposition_semitones=6),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Bb','A','G','F']),
 description='A five-bar upper song is answered by a more mobile four-bar lower song. The first then moves down an octave with every duration doubled, occupying ten bars. Its partner returns above it and develops instead of repeating in a loop. The upper voice withdraws two bars before the slower phrase completes its own arrival.',
 technical='Keep the augmented lower line continuous through the upper voice’s shorter gestures. Its tied A spans a bar line and must remain a single held note. Allow the upper voice to leave without slowing the final two lower-hand bars; the last B-flat completes the long melody alone.',
 rh='''Bb4:2 A4:1 G4:1 F4:2
D5:3 C5:1 Bb4:2
A4:2 C5:1 Eb5:1 D5:2
C5:1 Bb4:1 A4:2 F4:2
G4:2 A4:1 Bb4:3
R:6
R:6
R:6
R:6
D5:1 F5:.5 G5:.5 A5:1 F5:1 Eb5:2
D5:1 C5:1 Bb4:.5 A4:.5 Bb4:1 D5:1 F5:1
G5:1 Bb5:1 A5:.5 G5:.5 F5:1 Eb5:1 D5:1
C5:1 Eb5:.5 D5:.5 C5:1 A4:1 Bb4:2
F5:1 G5:.5 A5:.5 C6:1 Bb5:1 A5:2
G5:2 F5:1 Eb5:1 D5:1 C5:1
D5:1 F5:.5 Eb5:.5 D5:1 C5:1 A4:2
Bb4:2 A4:1 G4:1 F4:2
R:6
R:6''',
 lh='''R:6
R:6
R:6
R:6
R:6
D3:1 F3:.5 G3:.5 A3:1 F3:1 Eb3:2
D3:1 C3:1 Bb2:.5 A2:.5 Bb2:1 D3:1 F3:1
G3:1 Bb3:1 A3:.5 G3:.5 F3:1 Eb3:1 D3:1
C3:1 Eb3:.5 D3:.5 C3:1 A2:1 Bb2:2
Bb3:4 A3:2
G3:2 F3:4
D4:6
C4:2 Bb3:4
A3:4 C4:2
Eb4:2 D4:4
C4:2 Bb3:2 A3:2~
A3:2 F3:4
G3:4 A3:2
Bb3:6''',
 tempos=[56,57,56,55,54,57,58,59,56,57,58,59,58,60,58,57,56,56,56],
 phrases=[(1,5),(10,13),(14,17)],lower_phrases=[(6,9),(10,19)],sections={1:'p',10:'mp',14:'mf',16:'p'},lower_sections={1:'p',6:'mp',10:'p',14:'mp',17:'pp'},
 pedal=[[i*6+.05,i*6+5.8] for i in range(19)],hairpins=[('crescendo',10,14),('diminuendo',15,17)],page_starts=[9,17])
p['performance']['lower_entries']=[[30,54],[54,114]]

p=study(op=353,title='Briar Braid',key='F',fifths=-1,meter='3/4',bpm=46,parent=352,
 source=dict(source_opus=352,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['Bb','A','G','F'],transposition_semitones=7),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['F','E','D','C']),
 description='A song in three quarter-note pulses meets an ascending lower song in two dotted pulses. The latter is introduced in six-eight before both retain their own rhythms within three-four. A later statement brings the lower melody forward beneath a changed upper line. The last four bars bring both hands into three shared pulses.',
 technical='Keep the quarter-note pace through the changes between three-four and six-eight. In combination, hear the lower dotted pulse crossing the upper song’s three steps. Use the separate phrasing and staff dynamics to change the foreground without speeding up either melody.',
 rh='''F5:1 E5:1 D5:1
C5:1 A4:1 C5:1
D5:1 E5:1 G5:1
F5:1 E5:1 D5:1
Bb4:1 D5:1 F5:1
E5:1 D5:1 C5:1
Bb4:1 A4:1 G4:1
A4:1 C5:1 F5:1
A4+C5:3
Bb4+D5:3
C5+E5:3
D5+F5:3
D5+F5:3
E5+G5:3
F5:1 E5:1 D5:1
C5:1 A4:1 C5:1
D5:1 E5:1 G5:1
F5:1 E5:1 D5:1
Bb4:1 D5:1 F5:1
E5:1 D5:1 C5:1
Bb4:1 A4:1 G4:1
A4:1 C5:1 F5:1
F5:1 E5:1 D5:1
C5:1 D5:1 E5:1
F5:1 A5:1 G5:1
F5:1 Eb5:1 D5:1
F5:1 G5:1 A5:1
G5:1 F5:1 E5:1
F5:1 E5:1 D5:1
C5:1 Bb4:1 A4:1
G4:1 Bb4:1 E5:1
F4+A4+C5:2 R:1''',
 lh='''F3+A3+C4:3
A2+E3+G3:3
Bb2+D3+F3:3
D3+F3+A3:3
G2+Bb2+D3:3
C3+E3+Bb3:3
C3+G3+Bb3:3
F3+A3+C4:3
D3:1.5 F3:1.5
E3:1.5 G3:1.5
F3:1.5 A3:1.5
G3:1.5 Bb3:1.5
Bb3:1.5 D4:1.5
G3:1.5 C3:1.5
D3:1.5 F3:1.5
E3:1.5 G3:1.5
F3:1.5 A3:1.5
G3:1.5 Bb3:1.5
Bb3:1.5 D4:1.5
G3:1.5 C3:1.5
F3:1.5 E3:1.5
C3:1.5 F3:1.5
D3:1.5 F3:1.5
E3:1.5 G3:1.5
F3:1.5 A3:1.5
G3:1.5 Bb3:1.5
Bb3:1.5 D4:1.5
G3:1.5 C3:1.5
Bb2:1 D3:1 F3:1
A2:1 C3:1 F3:1
C3:1 G3:1 Bb3:1
F3+A3:2 R:1''',
 tempos=[46,47,48,47,48,47,46,46,46,47,48,48,47,46,46,47,48,47,48,47,46,46,46,47,48,48,47,46,46,47,46,46],
 meters=['3/4']*8+['6/8']*6+['3/4']*18,
 phrases=[(1,3),(4,8),(15,17),(18,22),(23,28),(29,32)],lower_phrases=[(9,10),(11,14),(15,16),(17,20),(21,22),(23,28),(29,32)],sections={1:'p',9:'pp',15:'mp',19:'mf',21:'p',23:'pp',29:'p',31:'pp'},lower_sections={1:'pp',9:'mp',15:'p',19:'p',23:'mp',27:'mf',29:'p',31:'pp'},
 pedal=[[i*3+.05,i*3+(1.8 if i==31 else 2.8)] for i in range(32)],hairpins=[('crescendo',15,19),('diminuendo',29,31)])
p['performance']['lower_entries']=[[24,42],[66,84]]

p=study(op=354,title='Celandine Interleaf',key='e',fifths=1,meter='5/4',bpm=58,parent=351,
 source=dict(source_opus=351,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['D','F','E','A'],transposition_semitones=2),motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['E','G','F#','B']),
 description='An E-minor song meets a lower phrase with a brighter inflection. Reflecting the upper song’s pitches around E5 turns its minor-third rise into a falling minor third, bringing C-sharp into the melody while preserving every duration. Later the original upper song meets the lower phrase reflected around E3. The two outcomes lead by separate steps into a quiet, widely spaced E–G.',
 technical='Preserve the recognisable rhythms through the two exact pitch inversions. Distinguish the inverted upper phrase in bars ten to fourteen from the later inverted lower phrase. Keep their changing chromatic tones directed towards the next note rather than isolated as accents.',
 rh='''E5:1 G5:1 F#5:1 B5:2
A5:2 G5:1 E5:1 D5:1
F#5:1 A5:1 G5:1 F#5:2
E5:2 D5:1 C5:1 B4:1
D#5:1 E5:4
A4+C#5:5
B4+D5:5
F#4+A4:5
G#4+B4:5
E5:1 C#5:1 D5:1 A4:2
B4:2 C#5:1 E5:1 F#5:1
D5:1 B4:1 C#5:1 D5:2
E5:2 F#5:1 G#5:1 A5:1
F5:1 E5:4
G5:1 F5:1 E5:1 C5:2
D5:.5 E5:.5 F#5:1 G5:1 A5:2
G5:2 F#5:1 E5:1 D#5:1
E5:4 R:1
E5:1 G5:1 F#5:1 B5:2
A5:2 G5:1 E5:1 D5:1
F#5:1 A5:1 G5:1 F#5:2
E5:2 D5:1 C5:1 B4:1
D#5:1 E5:4
F#5:1 E5:1 D5:1 C5:1 A4:1
G4:5''',
 lh='''E3+G3+B3:5
C3+G3+B3:5
D3+F#3+A3:5
A2+C3+E3:5
B2+D#3+A3:1 E3+G3+B3:4
A3:1.5 B3:.5 A3:1 F#3:2
G#3:2 E3:1 F#3:1 A3:1
F#3:1 G#3:.5 A3:.5 B3:1 F#3:2
G#3:1 B3:1 A3:1 F#3:1 E3:1
A3:1.5 B3:.5 A3:1 F#3:2
G#3:2 E3:1 F#3:1 A3:1
F#3:1 G#3:.5 A3:.5 B3:1 F#3:2
G#3:1 B3:1 A3:1 F#3:1 E3:1
A3:1 G#3:2 E3:2
C3:2 E3:1 G3:2
D3:2 A3:1 F#3:2
B2:2 F#3:1 A3:1 D#3:1
E3+B3:4 R:1
B2:1.5 A2:.5 B2:1 D3:2
C3:2 E3:1 D3:1 B2:1
D3:1 C3:.5 B2:.5 A2:1 D3:2
C3:1 A2:1 B2:1 D3:1 E3:1
B2:1 C3:2 E3:2
A2:1 C3:1 E3:1 F#3:1 D3:1
E3+B3:3 E3:2''',
 tempos=[58,59,60,58,56,58,59,60,57,59,60,61,60,58,60,62,60,57,58,59,60,58,56,57,57],
 phrases=[(1,5),(10,14),(15,18),(19,23),(24,25)],lower_phrases=[(6,9),(10,13),(15,18),(19,22),(24,25)],sections={1:'p',6:'pp',10:'mp',15:'mp',17:'mf',19:'p',24:'pp'},lower_sections={1:'pp',6:'mp',10:'p',15:'p',19:'mp',24:'pp'},
 pedal=sorted([[i*5+.05,i*5+(3.8 if i==17 else 4.8)] for i in range(25) if i not in [4,13,22]]+[[20.05,20.85],[21.05,24.8],[65.05,65.85],[66.05,67.85],[68.05,69.8],[110.05,110.85],[111.05,112.85],[113.05,114.8]]),hairpins=[('crescendo',10,13),('diminuendo',19,23)],page_starts=[9,17,23],system_starts=[1,3,5,7,9,11,13,15,17,19,21,23,25])
p['performance']['lower_entries']=[[25,45],[90,110]]

p=study(op=355,title='Bluebell Commonage',key='D',fifths=2,meter='9/8',bpm=54,parent=353,
 source=dict(source_opus=353,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['F','E','D','C'],transposition_semitones=9),motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4.5,pitches=['D','C#','B','A']),
 description='Three small songs are introduced in different registers: a lilting upper line, a mobile bass and a slower middle voice. Their three possible pairings prepare a meeting of all three. The middle voice remains within the right hand’s span as the outer lines move around it, and finally continues alone after their shared cadence.',
 technical='Keep the middle voice held under the right hand’s moving upper notes, within the written octave span. Give each song its own phrase ending in the pairwise passages. The final middle-voice statement should retain its identity after the other two voices have fallen silent.',
 rh='''D5:1.5 C#5:.75 B4:.75 A4:1.5
B4:1.5 A4:.75 G4:.75 A4:1.5
G4:1.5 B4:1.5 D5:1.5
A4+C#5:4.5
B4+D5:4.5
A4+C#5:4.5
R:4.5
R:4.5
D5:1.5 C#5:.75 B4:.75 A4:1.5
B4:1.5 A4:.75 G4:.75 A4:1.5
G4:1.5 B4:1.5 D5:1.5
R:4.5
R:4.5
R:4.5
D5:1.5 C#5:.75 B4:.75 A4:1.5
B4:1.5 A4:.75 G4:.75 A4:1.5
G4:1.5 B4:1.5 D5:1.5
D5:1.5 C#5:.75 B4:.75 A4:1.5
B4:1.5 A4:.75 G4:.75 A4:1.5
G4:1.5 B4:1.5 D5:1.5
C#5:1.5 B4:.75 A4:.75 B4:1.5
D5:1.5 C#5:.75 B4:.75 A4:1.5
G4:1.5 F#4:1.5 R:1.5
R:4.5
R:4.5''',
 lh='''D3+A3:4.5
B2+F#3:4.5
G2+D3:4.5
B2:1 F#3:.5 D3:1 E3:.5 F#3:1.5
G2:1 D3:.5 B2:1 C#3:.5 E3:1.5
E3:1 G3:.5 F#3:1 E3:.5 D3:1.5
R:4.5
R:4.5
B2:1 F#3:.5 D3:1 E3:.5 F#3:1.5
G2:1 D3:.5 B2:1 C#3:.5 E3:1.5
E3:1 G3:.5 F#3:1 E3:.5 D3:1.5
B2:1 F#3:.5 D3:1 E3:.5 F#3:1.5
G2:1 D3:.5 B2:1 C#3:.5 E3:1.5
E3:1 G3:.5 F#3:1 E3:.5 D3:1.5
R:4.5
R:4.5
R:4.5
B2:1 F#3:.5 D3:1 E3:.5 F#3:1.5
G2:1 D3:.5 B2:1 C#3:.5 E3:1.5
E3:1 G3:.5 F#3:1 E3:.5 D3:1.5
A2:1 E3:.5 C#3:1 D3:.5 E3:1.5
G2:1 D3:.5 B2:1 A2:.5 C#3:1.5
D3:3 R:1.5
R:4.5
R:4.5''',
 rh_inner='''R:4.5
R:4.5
R:4.5
R:4.5
R:4.5
R:4.5
D4:1.5 E4:1.5 F#4:1.5
E4:3 D4:1.5
R:4.5
R:4.5
R:4.5
D4:1.5 E4:1.5 F#4:1.5
E4:3 D4:1.5
E4:1.5 D4:1.5 F#4:1.5
D4:1.5 E4:1.5 F#4:1.5
E4:3 D4:1.5
E4:1.5 D4:1.5 F#4:1.5
D4:1.5 E4:1.5 F#4:1.5
E4:3 D4:1.5
E4:1.5 D4:1.5 F#4:1.5
E4:1.5 F#4:1.5 E4:1.5
F#4:1.5 E4:1.5 D4:1.5
D4:3 R:1.5
D4:1.5 E4:1.5 F#4:1.5
E4:3 D4:1.5''',hidden_voice_rests={'inner':[1,2,3,4,5,6,9,10,11]},
 tempos=[54,55,53,55,56,54,53,52,55,56,54,55,56,54,55,56,54,57,58,56,58,57,54,54,54],
 phrases=[(1,3),(9,11),(15,17),(18,20),(21,23)],lower_phrases=[(4,6),(9,11),(12,14),(18,20),(21,23)],
 voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=s) for a,b,s in [(27,36,2),(49.5,63,3),(63,76.5,2),(76.5,90,3),(90,102,2),(103.5,112.5,2)]],
 sections={1:'p',4:'pp',7:'p',9:'mp',12:'p',15:'mp',18:'mf',21:'mp',23:'p',24:'pp'},lower_sections={1:'pp',4:'mp',7:'pp',9:'p',12:'mp',18:'p',21:'mp',23:'pp'},
 pedal=[[i*4.5+.05,i*4.5+(2.8 if i==22 else 4.3)] for i in range(25)],hairpins=[('crescendo',18,20),('diminuendo',21,23)],page_starts=[7,13,19,25],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=680))
p['performance']['lower_entries']=[[13.5,27],[49.5,63],[76.5,90]]
p['performance']['inner_entries']=[[27,36],[49.5,63],[103.5,112.5]]

p=study(op=356,title='Ash Colloquy',key='f',fifths=-4,meter='2/2',bpm=64,parent=351,
 source=dict(source_opus=351,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['D','F','E','A'],transposition_semitones=3),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['F','Ab','G','C']),
 description='A four-bar upper subject and a three-bar bass countersubject first meet without haste. The upper subject then begins again in the bass before its first statement has finished: first two bars later, then only one. These closer entries change the harmonic conversation without a corresponding rise in loudness. A plain final pairing restores the original distance between the songs.',
 technical='Keep the two half-note pulses buoyant. In the two stretto passages, let each hand phrase the complete subject independently of the other hand’s entry. The final return retains the pulse and the original theme rather than slowing into a chordal close.',
 rh='''F5:1 Ab5:.5 G5:.5 C5:2
Db5:1 C5:1 Ab4:1 Bb4:1
C5:1 Eb5:1 Db5:1 C5:1
Bb4:1 G4:1 Ab4:2
R:4
R:4
R:4
F5:1 Ab5:.5 G5:.5 C5:2
Db5:1 C5:1 Ab4:1 Bb4:1
C5:1 Eb5:1 Db5:1 C5:1
Bb4:1 G4:1 Ab4:2
G4:1 Bb4:.5 Ab4:.5 Eb5:2
F5:1 Eb5:1 Db5:1 C5:1
Db5:1 Bb4:1 C5:1 R:1
F5:1 Ab5:.5 G5:.5 C5:2
Db5:1 C5:1 Ab4:1 Bb4:1
C5:1 Eb5:1 Db5:1 C5:1
Bb4:1 G4:1 Ab4:2
Ab4:2 G4:1 Ab4:1
G4:1 Eb4:1 F4:2
Ab4:1 Bb4:1 Db5:2
C5:1 Bb4:1 G4:2
Ab4:1 G4:1 F4:1 R:1
F5:1 Ab5:.5 G5:.5 C5:2
Db5:1 C5:1 Ab4:1 Bb4:1
C5:1 Eb5:1 Db5:1 C5:1
Bb4:1 G4:1 Ab4:2
Db5:1 C5:1 F5:1 Eb5:1
F5:1 Ab5:.5 G5:.5 C5:2
Db5:1 C5:1 Ab4:1 Bb4:1
C5:1 Eb5:1 Db5:1 C5:1
Bb4:1 G4:1 Ab4:2''',
 lh='''R:4
R:4
R:4
R:4
F3:2 Eb3:1 Db3:1
Eb3:1 F3:1 G3:2
Ab3:1 G3:1 F3:2
F3:2 Eb3:1 Db3:1
Eb3:1 F3:1 G3:2
Ab3:1 G3:1 F3:2
Db3:1 Eb3:1 F3:2
Eb3:2 G3:1 F3:1
Db3:2 F3:1 Ab3:1
G3:1 F3:1 E3:1 R:1
F3:2 Eb3:1 Db3:1
Eb3:1 F3:1 G3:2
F3:1 Ab3:.5 G3:.5 C3:2
Db3:1 C3:1 Ab2:1 Bb2:1
C3:1 Eb3:1 Db3:1 C3:1
Bb2:1 G2:1 Ab2:2
Bb2:2 Db3:1 F3:1
Eb3:2 C3:1 Eb3:1
Db3:1 Bb2:1 C3:1 R:1
F3:2 Eb3:1 Db3:1
F3:1 Ab3:.5 G3:.5 C3:2
Db3:1 C3:1 Ab2:1 Bb2:1
C3:1 Eb3:1 Db3:1 C3:1
Bb2:1 G2:1 Ab2:2
F3:2 Eb3:1 Db3:1
Eb3:1 F3:1 G3:2
Ab3:1 G3:1 F3:2
Db3:1 Eb3:1 F3:2''',
 tempos=[64,65,64,62,63,65,63,64,66,65,63,65,67,64,65,66,67,66,65,64,65,66,64,65,66,67,66,64,64,65,64,64],
 phrases=[(1,4),(8,11),(12,14),(15,18),(19,20),(21,23),(24,27),(29,32)],lower_phrases=[(5,7),(8,10),(12,14),(15,16),(17,20),(21,23),(25,28),(29,31)],
 sections={1:'p',5:'pp',8:'mp',12:'p',15:'mp',19:'p',21:'p',24:'mp',28:'p',29:'p'},lower_sections={1:'pp',5:'mp',8:'p',12:'p',15:'p',17:'mp',21:'p',25:'mp',29:'p'},
 pedal=[[i*4+.05,i*4+(2.8 if i in [13,22] else 3.8)] for i in range(32)],hairpins=[('crescendo',8,10),('diminuendo',12,14),('diminuendo',29,32)])
p['performance']['lower_entries']=[[16,28],[64,80],[96,112]]

p=study(op=357,title='Dogwood Accord',key='d',fifths=-1,meter='3/2',bpm=58,parent=354,
 source=dict(source_opus=354,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['E','G','F#','B'],transposition_semitones=-2),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['D','F','E','A']),
 description='The upper song learns to linger: a note prepared in one harmony remains while the bass changes, then resolves down a step. A separately introduced bass melody gives those suspensions a moving partner. Their meeting opens into a longer chain of fourths, sevenths and ninths, each resolving in its own voice. The final bass continues after the upper line has settled.',
 technical='Hold each tied suspension with the fingers while clearing the pedal at the bass change. The chain in bars 14–17 needs a quiet preparation and a distinct, unforced resolution. Keep the bass melody shaped independently; its last short statement follows the upper voice’s release.',
 rh='''D5:2 F5:1 E5:1 A4:2
Bb4:2 A4:1 G4:1 F4:2~
F4:2 E4:1 F4:1 E4:2~
E4:2 D4:4
R:6
R:6
R:6
C#4:2 E4:2 A4:2
D5:2 F5:1 E5:1 A4:2
Bb4:2 A4:1 G4:1 F4:2~
F4:2 E4:1 F4:1 E4:2~
E4:2 D4:4
G4:2 A4:2 D5:2~
D5:2 C#5:2 E5:2~
E5:2 D5:2 F5:2~
F5:2 E5:2 G5:2~
G5:2 F5:2 E5:2
D5:2 C#5:1 D5:1 A4:2
D5:2 F5:1 E5:1 A4:2
Bb4:2 A4:1 G4:1 F4:2~
F4:2 E4:1 F4:1 E4:2~
E4:2 D4:4
F4:2 E4:1 D4:3
R:6''',
 lh='''D3+A3:6
Bb2+F3:6
G3:4 C3:2
D3:6
D3:2 A3:2 F3:2
Bb2:2 F3:2 Bb3:2
G3:4 C3:2
A2:2 E3:2 G3:2
D3:2 A3:2 F3:2
Bb2:2 F3:2 Bb3:2
G3:4 C3:2
D3:6
G3:2 F3:2 G3:2
A3:6
D3+A3:6
C3+G3:6
A3:6
Bb3:2 A3:2 F3:2
D3:2 A3:2 F3:2
Bb2:2 F3:2 Bb3:2
G3:4 C3:2
D3:6
Bb2:2 C3:2 D3:2~
D3:2 A2:2 D3:2''',
 tempos=[58,59,58,56,58,60,58,57,59,60,59,57,59,60,61,60,59,58,58,59,58,57,58,58],
 phrases=[(1,4),(8,12),(13,18),(19,22),(23,23)],lower_phrases=[(5,7),(9,11),(13,18),(19,21),(23,24)],
 sections={1:'p',5:'pp',8:'p',9:'mp',13:'p',15:'mf',18:'mp',19:'p',23:'pp'},lower_sections={1:'pp',5:'mp',8:'p',9:'p',13:'mp',18:'p',19:'mp',22:'p',23:'pp'},
 pedal=sorted([[i*6+.05,i*6+5.8] for i in [0,1,4,5,7,8,9,12,17,18,19]]+[[i*6+.05,i*6+1.8] for i in [2,3,10,11,13,14,15,16,20,21,22,23]]+[[i*6+2.05,i*6+3.8] for i in [2,10,13,14,15,16,20,22,23]]+[[i*6+4.05,i*6+5.8] for i in [2,6,10,13,14,15,16,20,22,23]]+[[36.05,39.8],[20.05,23.8],[68.05,71.8],[128.05,131.8]]),
 hairpins=[('crescendo',13,15),('diminuendo',16,18)],page_starts=[7,13,19],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=680))
p['performance']['lower_entries']=[[24,42],[48,66],[108,126],[132,144]]

p=study(op=358,title='Teasel Exchange',key='G',fifths=1,meter='7/8',bpm=55,parent=355,
 source=dict(source_opus=355,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4.5,source_pitches=['D','C#','B','A'],transposition_semitones=5),motif=dict(hand='rh',start_beat=0,end_beat=3.5,pitches=['G','F#','E','D']),
 description='Two interrupted songs are introduced separately, then fitted together so that one hand fills the other’s silence. Their uneven groups of seven eighths shift emphasis from phrase to phrase. First the upper notes lengthen across the lower entries, then the lower notes do the same. A later exchange of registers restores the original gaps; the two closing gestures release at different times.',
 technical='Treat the opening rests as part of each melody. In the first combined passage the hands alternate cleanly without pedal. Later overlapping versions retain the pitch order while extending selected durations. Prepare the left hand’s treble-clef phrase and return without accenting the register change.',
 rh='''G5:.5 R:.5 F#5:.5 R:.5 E5:.5 R:.5 D5:.5
C5:1 R:.5 D5:.5 R:.5 E5:1
R:.5 F#5:.5 E5:.5 R:1 D5:1
C5:.5 R:.5 B4:.5 R:.5 A4:1 R:.5
R:3.5
R:3.5
R:3.5
R:3.5
G5:.5 R:.5 F#5:.5 R:.5 E5:.5 R:.5 D5:.5
C5:1 R:.5 D5:.5 R:.5 E5:1
R:.5 F#5:.5 E5:.5 R:1 D5:1
C5:.5 R:.5 B4:.5 R:.5 A4:1 R:.5
G5:1 F#5:1 E5:1 D5:.5
C5:1.5 D5:1 E5:1
R:.5 F#5:.5 E5:1.5 D5:1
C5:1 B4:1 A4:1.5
G5:.5 R:.5 F#5:.5 R:.5 E5:.5 R:.5 D5:.5
C5:1 R:.5 D5:.5 R:.5 E5:1
R:.5 F#5:.5 E5:.5 R:1 D5:1
C5:.5 R:.5 B4:.5 R:.5 A4:1 R:.5
E5:1.5 G5:.5 F#5:.5 E5:1
D5:1 F#5:1 E5:.5 D5:1
C5:.5 E5:.5 D5:1 B4:1.5
A4:1 B4:.5 C5:.5 D5:1 R:.5
R:.5 B4:.5 R:.5 A4:.5 R:.5 G4:.5 R:.5
R:1 E4:.5 R:.5 F#4:.5 R:1
B4:.5 R:1 A4:1 R:1
R:.5 E4:.5 R:.5 F#4:.5 R:1 G4:.5
E5:.5 R:.5 D5:.5 R:.5 B4:1.5
R:.5 A4:1.5 G4:1.5
F#4:1 G4:1.5 R:1
R:3.5''',
 lh='''R:3.5
R:3.5
R:3.5
R:3.5
R:.5 B3:.5 R:.5 A3:.5 R:.5 G3:.5 R:.5
R:1 E3:.5 R:.5 F#3:.5 R:1
B3:.5 R:1 A3:1 R:1
R:.5 E3:.5 R:.5 F#3:.5 R:1 G3:.5
R:.5 B3:.5 R:.5 A3:.5 R:.5 G3:.5 R:.5
R:1 E3:.5 R:.5 F#3:.5 R:1
B3:.5 R:1 A3:1 R:1
R:.5 E3:.5 R:.5 F#3:.5 R:1 G3:.5
R:.5 B3:.5 R:.5 A3:.5 R:.5 G3:.5 R:.5
R:1 E3:.5 R:.5 F#3:.5 R:1
B3:.5 R:1 A3:1 R:1
R:.5 E3:.5 R:.5 F#3:.5 R:1 G3:.5
R:.5 B3:1 A3:1 G3:1
R:1 E3:1 F#3:1.5
B3:1.5 A3:2
R:.5 E3:1 F#3:1.5 G3:.5
C3:.5 G3:1 E3:.5 G3:1.5
B2:1 F#3:.5 A3:1 F#3:1
A2:.5 E3:.5 G3:1 E3:1.5
D3:1 F#3:.5 G3:.5 A3:1 R:.5
G4:.5 R:.5 F#4:.5 R:.5 E4:.5 R:.5 D4:.5
C4:1 R:.5 D4:.5 R:.5 E4:1
R:.5 F#4:.5 E4:.5 R:1 D4:1
C4:.5 R:.5 B3:.5 R:.5 A3:1 R:.5
R:.5 G3:.5 R:.5 F#3:.5 R:1.5
D3:.5 R:3
C3:1 D3:1 R:1.5
G2:1.5 D3:.5 G3:.5 R:1''',
 tempos=[55,56,57,55,55,56,57,55,57,58,59,56,58,59,60,58,58,59,60,58,60,61,59,57,56,57,58,56,55,54,54,54],
 phrases=[(1,4),(9,12),(13,16),(17,20),(21,24),(25,28),(29,31)],lower_phrases=[(5,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32)],
 sections={1:'p',5:'pp',9:'mp',13:'p',17:'mp',21:'mf',24:'p',25:'p',29:'pp'},lower_sections={1:'pp',5:'p',9:'mp',13:'mp',17:'p',21:'mp',24:'p',25:'mp',29:'pp'},
 pedal=[[i*3.5+.05,i*3.5+3.3] for i in range(12,20)],hairpins=[('crescendo',21,22),('diminuendo',23,24)],clef_changes={'lh':{1:'bass',25:'treble',29:'bass'}})
p['performance']['lower_entries']=[[14,28],[56,70],[84,98],[108.5,111]]

p=study(op=359,title='Lupin Rendezvous',key='e',fifths=1,meter='4/4',bpm=58,parent=356,
 source=dict(source_opus=356,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['F','Ab','G','C'],transposition_semitones=-1),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['E','G','F#','B']),
 description='A five-bar melody and a shorter bass song meet before the upper melody turns back through its own notes and durations in reverse order. Newly written bass motion makes this reversal a different harmonic route. The original melody later returns over changed harmony; its companion begins late and continues beyond the upper line’s ending.',
 technical='Shape the reversed phrase as a new song, retaining its exact unequal durations. Give the returning melody a softer colour without losing its direction. When the bass enters late in the final statement, preserve its independent three-bar phrase beyond the upper voice’s release.',
 rh='''E5:1.5 G5:.5 F#5:1 B4:1
C5:1 B4:.5 A4:.5 G4:2
F#4:.5 A4:.5 B4:1 E5:2
D5:1 F#5:1 E5:.5 D5:.5 B4:1
C5:1.5 A4:.5 B4:2
R:4
R:4
R:4
E5:1.5 G5:.5 F#5:1 B4:1
C5:1 B4:.5 A4:.5 G4:2
F#4:.5 A4:.5 B4:1 E5:2
D5:1 F#5:1 E5:.5 D5:.5 B4:1
C5:1.5 A4:.5 B4:2
C5:1 E5:1 G5:2
F#5:.5 E5:.5 D5:1 B4:2
A4:1 C5:1 B4:1 R:1
B4:2 A4:.5 C5:1.5
B4:1 D5:.5 E5:.5 F#5:1 D5:1
E5:2 B4:1 A4:.5 F#4:.5
G4:2 A4:.5 B4:.5 C5:1
B4:1 F#5:1 G5:.5 E5:1.5
C5:2 B4:1 A4:1
G4:1 B4:1 A4:2
F#4:1 A4:1 B4:2
E5:1.5 G5:.5 F#5:1 B4:1
C5:1 B4:.5 A4:.5 G4:2
F#4:.5 A4:.5 B4:1 E5:2
D5:1 F#5:1 E5:.5 D5:.5 B4:1
C5:1.5 A4:.5 B4:2
R:4
R:4''',
 lh='''R:4
R:4
R:4
R:4
E3:4
E3:2 B3:1 A3:1
C3:1 G3:1 F#3:2
B2:1 F#3:1 G3:1 E3:1
E3:2 B3:1 A3:1
C3:1 G3:1 F#3:2
B2:1 F#3:1 G3:1 E3:1
A3:2 C4:1 B3:1
A3:1 F#3:1 E3:2
A2:1 E3:1 G3:2
D3:1 A3:1 F#3:2
C3:1 E3:1 F#3:1 R:1
E3:1 F#3:1 D3:1 E3:1
G3:1 B3:1 A3:1 F#3:1
C3:2 E3:1 F#3:.5 D3:.5
E3:2 D3:.5 G3:.5 A3:1
G3:1 D3:1 E3:.5 C3:1.5
E3:2 B3:1 A3:1
C3:1 G3:1 F#3:2
B2:1 F#3:1 G3:1 E3:1
C3:2 G3:1 E3:1
A2:1 E3:1 F#3:1 A3:1
G2:2 D3:1 B2:1
E3:2 B3:1 A3:1
C3:1 G3:1 F#3:2
B2:1 F#3:1 G3:1 E3:1
F#3:1 D3:1 E3:2''',
 tempos=[58,59,60,59,57,58,60,58,59,60,61,60,58,60,62,59,58,59,60,59,58,59,60,58,58,59,60,59,58,58,58],
 phrases=[(1,5),(9,13),(14,16),(17,21),(22,24),(25,29)],lower_phrases=[(6,8),(9,13),(14,16),(17,21),(22,24),(25,27),(28,30),(31,31)],
 sections={1:'p',6:'pp',9:'mp',14:'mf',17:'p',22:'p',25:'pp'},lower_sections={1:'pp',6:'mp',9:'p',14:'mp',17:'p',22:'mp',25:'p',28:'mp',31:'pp'},
 pedal=sorted([[i*4+.05,i*4+(2.8 if i==15 else 3.8)] for i in range(31) if i not in range(16,21)]+[[i*4+.05,i*4+1.8] for i in range(16,21)]+[[i*4+2.05,i*4+3.8] for i in range(16,21)]),hairpins=[('crescendo',17,19),('diminuendo',20,21),('diminuendo',25,29)])
p['performance']['lower_entries']=[[20,32],[84,96],[108,124]]

p=study(op=360,title='Bilberry Chorus',key='c',fifths=-3,meter='4/4',bpm=66,parent=356,
 source=dict(source_opus=356,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['F','Ab','G','C'],transposition_semitones=-5),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['C','Eb','D','G']),
 description='Two themes receive separate imitative entrances before a longer development brings them together. Their combination travels into another register and key, exchanges upper and lower positions, and moves through a freer episode before returning. A final expansion into six-beat bars lengthens the first theme without changing its proportions. The bass falls silent while the upper voice holds its last note.',
 technical='Distinguish the two themes by articulation and phrase direction throughout their exchanges. The right-hand C4-to-F5 relocation into bar 21 follows a half-note duration; give its upper landing a light touch. Move the left hand between clefs without displacing the pulse. In the final six-beat phrase, preserve the theme’s one-and-a-half expansion and let the bass release while the final upper note remains held.',
 technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 rh='''C5:1 Eb5:.5 D5:.5 G4:2
Eb5:1 D5:1 C5:1 G4:1
Ab4:1 G4:.5 F4:.5 Eb4:2
F4:1 D4:1 C4:2
Eb5:2 D5:1 C5:1
Bb4:1 C5:1 Eb5:2
D5:1 C5:1 Bb4:1 G4:1
Ab4:1 G4:1 Eb4:2
R:4
R:4
R:4
R:4
Eb5:1 G5:1 F5:1 Eb5:1
G5:1 F5:1 Eb5:1 D5:1
C5:2 Bb4:1 Eb5:1
Bb4:1 D5:1 C5:2
C5:1 Eb5:.5 D5:.5 G4:2
Eb5:1 D5:1 C5:1 G4:1
Ab4:1 G4:.5 F4:.5 Eb4:2
F4:1 D4:1 C4:2
F5:1 Ab5:.5 G5:.5 C5:2
Ab5:1 G5:1 F5:1 C5:1
Db5:1 C5:.5 Bb4:.5 Ab4:2
Bb4:1 G4:1 F4:2
Eb5:1 G5:1 F5:1 Eb5:1
G5:1 F5:1 Eb5:1 D5:1
C5:2 Bb4:1 Eb5:1
Bb4:1 D5:1 C5:2
D5:1 F5:.5 Eb5:.5 Bb4:2
C5:1 Eb5:1 D5:1 Bb4:1
A4:1 C5:.5 Bb4:.5 F4:2
G4:1 A4:1 B4:1 D5:1
C5:1 Eb5:.5 D5:.5 G4:2
Eb5:1 D5:1 C5:1 G4:1
Ab4:1 G4:.5 F4:.5 Eb4:2
F4:1 D4:1 C4:2
C5:1.5 Eb5:.75 D5:.75 G4:3
Eb5:1.5 D5:1.5 C5:1.5 G4:1.5
Ab4:1.5 G4:.75 F4:.75 Eb4:3
F4:1.5 D4:1.5 C4:3''',
 lh='''R:4
R:4
R:4
R:4
C4:1 Eb4:.5 D4:.5 G3:2
Eb4:1 D4:1 C4:1 G3:1
Ab3:1 G3:.5 F3:.5 Eb3:2
F3:1 D3:1 C3:2
Eb3:1 G3:1 F3:1 Eb3:1
G3:1 F3:1 Eb3:1 D3:1
C3:2 Bb2:1 Eb3:1
Bb2:1 D3:1 C3:2
C3:4
Bb2:4
Ab2:2 G2:2
G2:2 C3:2
Eb3:1 G3:1 F3:1 Eb3:1
G3:1 F3:1 Eb3:1 D3:1
C3:2 Bb2:1 Eb3:1
Bb2:1 D3:1 C3:2
Ab3:1 C4:1 Bb3:1 Ab3:1
C4:1 Bb3:1 Ab3:1 G3:1
F3:2 Eb3:1 Ab3:1
Eb3:1 G3:1 F3:2
C4:1 Eb4:.5 D4:.5 G3:2
Eb4:1 D4:1 C4:1 G3:1
Ab3:1 G3:.5 F3:.5 Eb3:2
F3:1 D3:1 C3:2
G3:1 Bb3:1 A3:1 G3:1
Eb3:1 G3:1 F3:1 D3:1
F3:2 Eb3:1 A3:1
G3:1 F3:1 D3:1 B2:1
Eb3:1 G3:1 F3:1 Eb3:1
G3:1 F3:1 Eb3:1 D3:1
C3:2 Bb2:1 Eb3:1
Bb2:1 D3:1 C3:2
Eb3:1.5 G3:1.5 F3:1.5 Eb3:1.5
G3:1.5 F3:1.5 Eb3:1.5 D3:1.5
C3:3 Bb2:1.5 Eb3:1.5
Bb2:1.5 D3:1.5 C3:2 R:1''',meters=['4/4']*36+['6/4']*4,
 tempos=[66,67,66,64,66,67,66,64,66,68,67,65,67,68,67,65,67,68,67,65,68,70,69,67,67,68,67,65,69,70,69,67,66,67,66,64,64,65,64,64],
 phrases=[(1,4),(5,8),(13,16),(17,20),(21,24),(25,28),(29,32),(33,36),(37,40)],lower_phrases=[(5,8),(9,12),(17,20),(21,24),(25,28),(29,32),(33,36),(37,40)],
 sections={1:'p',5:'pp',9:'pp',13:'mp',17:'mp',21:'mf',25:'p',29:'mp',33:'p',37:'pp'},lower_sections={1:'pp',5:'mp',9:'mp',13:'pp',17:'p',21:'mp',25:'mp',29:'p',33:'mp',37:'pp'},
 pedal=[[i*4+.05,i*4+3.8] for i in range(36)]+[[144+i*6+.05,144+i*6+(4.8 if i==3 else 5.8)] for i in range(4)],hairpins=[('crescendo',17,19),('diminuendo',22,24),('diminuendo',33,36)],clef_changes={'lh':{1:'bass',5:'treble',9:'bass',25:'treble',29:'bass'}})
p['performance']['lower_entries']=[[16,48],[96,112],[128,144]]
