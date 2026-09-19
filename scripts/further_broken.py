"""Individually authored Broken Dances, CWS Op. 371–380."""
from weather_common import make_study
PIECES=[]
def study(**kwargs):
    p=make_study(**kwargs);PIECES.append(p);return p

p=study(op=371,title='Hawthorn Vacancy',key='g',fifths=-2,meter='3/4',bpm=54,parent=285,
 source=dict(source_opus=285,source_hand='lh',source_start_beat=22,source_end_beat=25,source_pitches=['Bb','A','G','F'],transposition_semitones=0),motif=dict(hand='rh',start_beat=1,end_beat=3,pitches=['Bb','A','G','F']),
 description='A waltz leaves the first beat of selected arrivals silent, then answers late within the unchanged bar. Its incomplete refrain opens into a longer, more continuous song. The refrain returns with altered harmony and a longer aftermath, while its absent downbeats acquire different destinations. An unaccompanied answer remains after the dance support has stopped.',
 technical='Maintain the imagined first beat through the fully written silence; do not shorten the bar or hurry the late entry. Shape the long middle song across the smaller accompaniment gestures. Preserve the independent releases and let the final unaccompanied response follow the last bass sound after its full rest.',
 rh='''R:1 Bb4:.5 A4:.5 G4:.5 F4:.5
D5:1 C5:1 A4:1
Bb4:.75 C5:.25 D5:1 F5:1
R:1 Eb5:1 D5:1
C5:.5 Bb4:.5 A4:1 F#4:1
R:1 G4:1 R:1
D5:1 F5:.5 Eb5:.5 D5:1
C5:1 Bb4:.5 A4:.5 G4:1
F4:.5 G4:.5 A4:1 C5:1
Bb4:1 A4:1 G4:1
F4:1 A4:.5 C5:.5 Eb5:1
D5:2 C5:1
Bb4:.5 A4:.5 G4:1 F4:1
E4:1 G4:.5 A4:.5 C5:1
B4:1 A4:1 G4:1
F#4:1 A4:1 C5:1
D5:.5 E5:.5 F5:1 A5:1
G5:1 F5:.5 Eb5:.5 D5:1
C5:.75 D5:.25 Eb5:1 G5:1
F5:1 Eb5:1 C5:1
Bb4:1 D5:.5 C5:.5 Bb4:1
A4:1 G4:1 F4:1
Eb4:1 F4:.5 G4:.5 A4:1
G4:2 R:1
R:1 Bb4:.5 A4:.5 G4:.5 F4:.5
D5:1 C5:1 A4:1
Bb4:.75 C5:.25 D5:1 F5:1
R:1 Eb5:1 Db5:1
C5:.5 Bb4:.5 Ab4:1 G4:1
F4:1 Ab4:1 C5:1
Bb4:1 Ab4:.5 G4:.5 F4:1
R:1 Eb4:1 R:1
R:1 G4:1 Bb4:1
A4:.5 G4:.5 F4:1 Eb4:1
F4:1 G4:.5 A4:.5 Bb4:1
G4:2 R:1''',
 lh='''R:1 G3+Bb3:.5 R:.5 D3:.5 R:.5
Eb3:.5 R:.5 G3+Bb3:.5 R:.5 F3:1
D3:.5 R:.5 F3+A3:.5 R:.5 C3:.5 R:.5
R:1 C3+G3:.5 R:.5 Bb2:1
D3:.5 R:.5 F#3+A3:.5 R:.5 C3:.5 R:.5
R:1 G2+D3:1 R:1
Bb2:1 F3:.5 A3:.5 D3:1
Eb3:1 Bb3:1 G3:1
F3:1 C4:1 A3:1
G3:1 D3:.5 F3:.5 Bb3:1
F3:1 C4:1 A3:1
Bb2:1 F3:1 A3:1
Eb3:1 G3:.5 Bb3:.5 D4:1
C3:1 G3:1 E3:1
G3:1 D3:1 B2:1
D3:1 F#3:.5 A3:.5 C4:1
Bb3:1 A3:1 F3:1
Eb3:1 Bb3:1 G3:1
C3:1 G3:1 Bb3:1
F3:1 C4:.5 Eb4:.5 A3:1
Bb3:1 F3:1 D3:1
D3:1 A3:.5 C4:.5 F#3:1
C3:1 G3:1 F#3:1
G3:2 R:1
R:1 Eb3+G3:.5 R:.5 Bb2:.5 R:.5
Bb2:.5 R:.5 D3+F3:.5 R:.5 A2:1
G2:.5 R:.5 Bb2+D3:.5 R:.5 F3:.5 R:.5
R:1 Ab2+Eb3:.5 R:.5 Db3:1
F3:.5 R:.5 Ab3+C4:.5 R:.5 Eb3:.5 R:.5
Db3:.5 R:.5 F3+Ab3:.5 R:.5 C3:1
Bb2:.5 R:.5 Db3+F3:.5 R:.5 Ab2:.5 R:.5
R:1 C3+G3:1 R:1
R:3
R:3
R:3
R:3''',
 tempos=[54,55,56,54,55,54,56,57,58,57,58,59,57,58,57,56,58,59,58,57,56,55,54,54,54,55,56,54,55,56,55,54,54,55,54,54],
 phrases=[(1,3),(4,6),(7,12),(13,18),(19,24),(25,27),(28,32),(33,36)],lower_phrases=[(7,12),(13,18),(19,24)],
 sections={1:'p',7:'p',11:'mp',16:'p',19:'mp',23:'p',25:'p',28:'pp',33:'p'},lower_sections={1:'pp',7:'p',13:'pp',17:'p',23:'pp',25:'pp'},
 pedal=sorted([[i*3+1.05,i*3+1.8] for i in [0,3,5,24,27,31]]+[[i*3+.05,i*3+.8] for i in [1,2,4,25,26,28,29,30]]+[[i*3+.05,i*3+2.8] for i in range(6,23)]+[[69.05,70.8],[97.05,98.8],[99.05,101.8],[102.05,104.8],[105.05,106.8]]),
 hairpins=[('crescendo',7,10),('diminuendo',11,12),('crescendo',16,18),('diminuendo',20,22)])

p=study(op=372,title='Poppy Reversal',key='c',fifths=-3,meter='3/4',bpm=53,parent=275,
 source=dict(source_opus=275,source_hand='rh',source_start_beat=0,source_end_beat=2.5,source_pitches=['D','C','A','G'],transposition_semitones=-2),motif=dict(hand='rh',start_beat=0,end_beat=2.5,pitches=['C','Bb','G','F']),
 description='A four-bar melody leans on unequal durations and small silences. After a longer opening dance and a two-bar harmonic hinge, its pitch order returns with the complete rhythm-and-rest sequence reversed. A newly shaped bass changes the meaning of those shifted emphases. The later dance develops beyond this exact transformation, ending with a shortened version of the former closing gesture.',
 technical='Distinguish the first four-bar phrase from its rhythmic reversal at bars 14–17: pitch order stays intact but the long notes and gaps move. Keep each written gap exact without losing the waltz pulse. Let the changed bass shape the second panel, and release the final abbreviated gesture cleanly without an added slowing.',
 rh='''C5:.5 Bb4:.5 G4:.5 F4:1 R:.5
Ab4:1 G4:.5 Eb4:.5 F4:1
G4:1.5 Bb4:.5 C5:.5 R:.5
D5:.5 C5:1 G4:1 R:.5
Ab4:.5 Bb4:.5 C5:1 Eb5:1
D5:1 C5:.5 Bb4:.5 G4:1
F4:1 Ab4:1 C5:1
Bb4:.75 A4:.25 G4:1 F4:1
Eb4:1 G4:.5 Bb4:.5 D5:1
C5:1 Bb4:1 Ab4:1
G4:2 R:1
Eb4+G4+Bb4:2 R:1
D4+F4+A4:2 R:1
R:.5 C5:1 Bb4:1 G4:.5
R:.5 F4:.5 Ab4:.5 G4:1.5
Eb4:1 F4:.5 G4:.5 Bb4:1
R:.5 C5:1 D5:.5 C5:.5 G4:.5
A4:1 C5:.5 D5:.5 F5:1
E5:1 D5:1 C5:1
Bb4:.5 A4:.5 G4:1 F4:1
E4:1 G4:.5 A4:.5 C5:1
D5:1.5 C5:.5 Bb4:1
A4:1 G4:.5 F4:.5 E4:1
D4:1 F4:1 A4:1
Bb4:.5 C5:.5 D5:1 F5:1
Eb5:1 D5:1 C5:1
Bb4:1 Ab4:.5 G4:.5 F4:1
Eb4:1 G4:.5 Bb4:.5 C5:1
D5:1 C5:.5 Bb4:.5 G4:1
Ab4:1 G4:1 F4:1
G4:2 R:1
C5:.5 Bb4:.5 G4:.5 F4:1 R:.5
Ab4:1 G4:.5 Eb4:.5 F4:1
G4:1 Bb4:1 C5:1
Ab4:1 F4:1 D4:1
D5:.5 C5:.5 G4:.5 R:1.5''',
 lh='''C3:1 G3:.5 Bb3:.5 Eb3:1
F3:1 C4:1 Ab3:1
Ab2:1 Eb3:1 G3:1
G2:1 D3:1 B3:1
F3:.5 R:.5 Ab3+C4:.5 R:.5 Eb3:1
G3:1 D3:.5 F3:.5 Bb3:1
Db3:1 Ab3:1 F3:1
D3:.5 R:.5 F#3+A3:.5 R:.5 C3:1
Eb3:1 Bb3:1 G3:1
Ab2:1 Eb3:.5 G3:.5 C4:1
C3:2 R:1
C3:2 R:1
Bb2:2 R:1
Ab2:.5 R:.5 C3+Eb3:1 G3:1
D3:1 A3:1 F3:1
Bb2:1 F3:1 Ab3:1
C3:.5 R:.5 E3+G3:1 Bb3:1
F3:1 C4:1 A3:1
C3:1 G3:.5 Bb3:.5 E3:1
D3:1 A3:1 C4:1
A2:1 E3:1 G3:1
Bb2:1 F3:1 A3:1
C3:1 G3:.5 Bb3:.5 E3:1
D3:1 A3:1 F3:1
Bb2:.5 R:.5 D3+F3:.5 R:.5 A2:1
Eb3:1 Bb3:1 G3:1
Ab2:1 Eb3:.5 G3:.5 C4:1
C3:1 G3:1 Bb3:1
G2:1 D3:.5 F3:.5 B3:1
F3:1 C4:1 Ab3:1
C3:2 R:1
Ab2:1 Eb3:.5 G3:.5 C4:.5 R:.5
F3:1 C4:1 Ab3:1
Eb3:1 Bb3:1 G3:1
F3:1 Ab3:1 B3:1
C3:.5 G3:.5 Eb3:.5 R:1.5''',
 tempos=[53,54,55,53,55,56,55,54,55,54,53,53,53,54,55,56,54,55,56,55,56,57,56,55,56,57,56,55,54,54,53,54,55,54,53,53],
 phrases=[(1,4),(5,8),(9,11),(14,17),(18,24),(25,31),(32,36)],lower_phrases=[(1,4),(6,7),(9,11),(14,17),(18,24),(26,31),(32,36)],
 sections={1:'p',5:'mp',9:'p',12:'pp',14:'p',18:'mp',25:'p',32:'p'},lower_sections={1:'pp',5:'p',9:'pp',14:'p',18:'p',25:'pp',32:'pp'},
 pedal=sorted([[i*3+.05,i*3+2.8] for i in [1,4,5,6,7,8,9,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,33,34]]+[[i*3+.05,i*3+2.3] for i in [0,2,3,31]]+[[i*3+.05,i*3+1.8] for i in [10,11,12,30]]+[[105.05,106.3]]),
 hairpins=[('crescendo',5,7),('diminuendo',9,11),('crescendo',18,21),('diminuendo',28,30)])

p=study(op=373,title='Foxglove Concourse',key='g',fifths=-2,meter='3/4',bpm=55,parent=271,
 source=dict(source_opus=271,source_hand='rh',source_start_beat=3,source_end_beat=6,source_pitches=['A','C','F','G'],transposition_semitones=-2),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['G','Bb','Eb','F']),
 description='The first dance sentence closes with space after its arrival. When it returns, that arrival also begins a new sentence, followed by two further phrase overlaps. The cadence notes are single attacks shared by the adjoining phrases. A lyrical episode restores separated endings before one final dance finds a complete, unelided cadence.',
 technical='At the phrase meetings in bar 10, bar 13 and the last beat of bar 15, sound the shared note once and let its continuation begin the next sentence. Do not add a fresh attack or an extra pause there. Give the separated lyrical cadences their complete written rests, and keep the final dance connected to its quiet release.',
 rh='''G4:1 Bb4:.5 Eb5:.5 F5:1
Eb5:1 D5:1 Bb4:1
Ab4:.5 G4:.5 F4:1 D4:1
G4:2 R:1
Bb4:1 A4:.5 G4:.5 F4:1
D4:1 F4:1 R:1
G4:1 Bb4:.5 Eb5:.5 F5:1
Eb5:1 D5:1 Bb4:1
Ab4:.5 G4:.5 F4:1 D4:1
G4:1 Bb4:1 D5:1
C5:1 A4:.5 Bb4:.5 G4:1
F4:1 D4:1 F4:1
Bb4:1 C5:.5 D5:.5 F5:1
Eb5:1 D5:.5 C5:.5 Bb4:1
A4:1 C5:1 D5:1
C5:1 Bb4:1 A4:1
G4:2 R:1
Eb5:2 D5:1
C5:1 Bb4:2
A4:1 C5:.5 D5:.5 F5:1
Eb5:1 D5:1 C5:1
Bb4:2 R:1
G4:1 Bb4:1 Eb5:1
D5:1 C5:.5 Bb4:.5 A4:1
G4:1 F#4:1 A4:1
C5:1 Bb4:.5 A4:.5 G4:1
F4:1 Eb4:1 D4:1
G4:2 R:1
G4:1 Bb4:.5 Eb5:.5 F5:1
Eb5:1 D5:1 Bb4:1
Ab4:.5 G4:.5 F4:1 D4:1
Eb4:1 G4:1 Bb4:1
C5:1 Bb4:.5 A4:.5 G4:1
F#4:1 A4:1 C5:1
Bb4:1 A4:1 F#4:1
G4:2 R:1''',
 lh='''G2:1 D3:.5 G3:.5 Bb3:1
Eb3:1 Bb3:1 G3:1
C3:1 G3:1 D3:1
G2+D3:2 R:1
Eb3:.5 R:.5 G3+Bb3:.5 R:.5 F3:1
D3:1 A3:1 R:1
G2:1 D3:.5 G3:.5 Bb3:1
Eb3:1 Bb3:1 G3:1
D3:1 A3:.5 C4:.5 F#3:1
G3:1 D3:.5 G3:.5 Bb3:1
A3:1 E3:.5 G3:.5 C4:1
Bb2:1 F3:1 A3:1
Bb3:1 F3:.5 A3:.5 D3:1
C3:1 G3:1 Eb3:1
D3:1 A3:1 D3:1
F3:1 C4:1 A3:1
G3:2 R:1
C3+G3:3
Eb3+Bb3:3
F3+C4:3
G3+D4:3
Bb2+F3:2 R:1
Eb3+Bb3:3
C3+G3:3
D3+A3:3
G3+D4:3
C3:1 G3:1 F#3:1
G2+D3:2 R:1
Eb3:1 Bb3:.5 D4:.5 G3:1
Bb2:1 F3:1 A3:1
D3:1 A3:.5 C4:.5 F#3:1
C3:1 G3:1 Bb3:1
Eb3:1 Bb3:1 G3:1
D3:1 A3:.5 C4:.5 F#3:1
G3:1 D3:1 F#3:1
G2+D3:2 R:1''',
 tempos=[55,56,55,54,55,54,56,57,56,57,58,57,58,59,58,57,55,55,56,57,56,55,56,57,56,55,55,54,56,57,56,57,56,55,55,55],
 phrases=[(1,4),(5,6),(7,17),(18,22),(23,28),(29,36)],lower_phrases=[(1,4),(7,17),(18,22),(23,28),(29,36)],
 sections={1:'p',5:'pp',7:'p',13:'mp',18:'p',23:'p',29:'p'},lower_sections={1:'pp',7:'p',18:'pp',29:'pp'},
 pedal=sorted([[i*3+.05,i*3+2.8] for i in list(range(6,16))+list(range(17,21))+list(range(22,27))+list(range(28,35))+[0,1,2,4]]+[[i*3+.05,i*3+1.8] for i in [3,5,16,21,27,35]]),
 hairpins=[('crescendo',7,12),('diminuendo',14,16),('crescendo',18,20),('diminuendo',24,27)])

p=study(op=374,title='Rowan Underpass',key='F',fifths=-1,meter='3/4',bpm=59,parent=284,
 source=dict(source_opus=284,source_hand='lh',source_start_beat=0,source_end_beat=5.5,source_pitches=['F','C','G','C'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=5,pitches=['F','C','G','C']),
 description='A four-bar melody returns three times against the same bass-and-chord pattern. The bass begins on the beat, then half a beat later, then a full beat later, while the melody keeps its complete pitch and rhythm identity. Exposed treble passages separate the changing alignments. A brief restoration of the original alignment gives way to a final bass response after the upper song has ended.',
 technical='Keep the returning upper phrase steady through each written displacement of the lower pattern. Prepare the bass-to-chord relocations lightly and preserve their rests. The delayed patterns are fully written, not a tempo change. Let the final lower response begin after the upper line has released, without restarting the dance.',
 rh='''F4:1 A4:.5 C5:.5 D5:1
C5:1 B4:.5 A4:.5 G4:1
E5:1 D5:.5 C5:.5 B4:1
A4:1 G4:1 F4:1
E4:1 G4:.5 A4:.5 B4:1
A4:1 D5:1 C5:1
G4:1 F4:.5 E4:.5 D4:1
D4:2 R:1
F4:1 A4:1 C5:1
E5:1 D5:.5 C5:.5 Bb4:1
Bb4:1 A4:1 G4:1
F4:1 E4:.5 D4:.5 C4:1
E4:2 R:1
F4:1 A4:.5 C5:.5 D5:1
C5:1 B4:.5 A4:.5 G4:1
E5:1 D5:.5 C5:.5 B4:1
A4:1 G4:1 F4:1
Bb4:1 D5:.5 E5:.5 F5:1
E5:1 D5:1 C5:1
Bb4:1 G4:1 E4:1
F4:1 A4:.5 Bb4:.5 C5:1
B4:1 A4:1 G4:1
C5:2 R:1
E5:.5 D5:.5 C5:1 G4:1
A4:1 Bb4:1 C5:1
D5:2 R:1
F4:1 A4:.5 C5:.5 D5:1
C5:1 B4:.5 A4:.5 G4:1
E5:1 D5:.5 C5:.5 B4:1
A4:1 G4:1 F4:1
D5:1 C5:1 Bb4:1
A4:1 C5:.5 D5:.5 F5:1
E5:1 D5:1 C5:1
Bb4:1 A4:1 G4:1
F4:1 A4:.5 C5:.5 D5:1
C5:2 R:1
R:3
R:3
R:3
R:3''',
 lh='''F2:1 R:.5 G3+C4:.5 R:1
G2:1 R:.5 E3+C4:.5 R:1
A2:1 R:.5 G3+B3:.5 R:1
D3:1 R:.5 F3+A3:.5 R:1
C3:1 G3:.5 Bb3:.5 E3:1
D3:1 A3:.5 C4:.5 F3:1
Bb2:1 F3:1 A3:1
C3:1 G3:1 R:1
R:3
R:3
R:3
R:3
R:3
R:.5 F2:1 R:.5 G3+C4:.5 R:.5
R:.5 G2:1 R:.5 E3+C4:.5 R:.5
R:.5 A2:1 R:.5 G3+B3:.5 R:.5
R:.5 D3:1 R:.5 F3+A3:.5 R:.5
G3:1 D3:.5 F3:.5 Bb3:1
C3:1 G3:.5 Bb3:.5 E3:1
A2:1 E3:1 G3:1
D3:1 A3:.5 C4:.5 F3:1
G3:1 D3:1 B2:1
C3:1 G3:1 R:1
R:3
R:3
R:3
R:1 F2:1 R:.5 G3+C4:.5
R:1 G2:1 R:.5 E3+C4:.5
R:1 A2:1 R:.5 G3+B3:.5
R:1 D3:1 R:.5 F3+A3:.5
F3:1 C4:1 A3:1
D3:1 A3:1 C4:1
C3:1 G3:1 Bb3:1
G2:1 D3:1 F3:1
F2:1 R:.5 G3+C4:.5 R:1
G2:1 R:.5 E3+C4:.5 R:1
R:1 F3:1 C4:1
Bb3:1 A3:.5 G3:.5 F3:1
E3:1 G3:.5 A3:.5 C4:1
F3:2 R:1''',
 tempos=[59,60,61,60,61,62,60,59,59,60,61,60,59,59,60,61,60,61,62,61,62,61,59,59,60,59,59,60,61,60,61,62,61,60,59,59,59,60,59,59],
 phrases=[(1,4),(5,8),(9,13),(14,17),(18,23),(24,26),(27,30),(31,36)],lower_phrases=[(5,8),(18,23),(31,34),(37,40)],
 sections={1:'p',5:'mp',9:'p',14:'p',18:'mp',24:'p',27:'p',31:'mp',35:'p'},lower_sections={1:'pp',5:'p',14:'pp',18:'p',27:'pp',31:'p',35:'pp',37:'p'},
 pedal=sorted([[i*3+.05,i*3+.8] for i in [0,1,2,3,34,35]]+[[i*3+.55,i*3+1.3] for i in [13,14,15,16]]+[[i*3+1.05,i*3+1.8] for i in [26,27,28,29]]+[[i*3+.05,i*3+2.8] for i in [4,5,6,8,9,10,11,17,18,19,20,21,23,24,30,31,32,33,37,38]]+[[i*3+.05,i*3+1.8] for i in [7,12,22,25,39]]+[[109.05,110.8]]),
 hairpins=[('crescendo',5,6),('diminuendo',7,8),('crescendo',18,20),('diminuendo',21,23),('crescendo',31,33)])
p['performance']['lower_entries']=[[109,119]]

p=study(op=375,title='Gorse Pavement',key='d',fifths=-1,meter='6/8',bpm=63,parent=272,
 source=dict(source_opus=272,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['G','F#','E','D'],transposition_semitones=-2),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['F','E','D','C']),
 description='A long-short dance opens into an even, broader song before returning with the short and long values exchanged. Both hands keep the first three bars of pitch material through these changes of gait. The spacious middle develops its own harmonic weight, and the shorter final dance releases its lilt into a few even closing steps.',
 technical='Differentiate the written long-short pairs, equal quarters and short-long pairs without adding an automatic swing. Keep the quarter-note pace continuous through the changes of metre. Let the broader middle sing in longer spans, then make the changed lilt light enough to settle into the final even notes.',
 meters=['6/8']*9+['4/4']*15+['6/8']*8+['4/4']*4,
 rh='''F5:1 E5:.5 D5:1 C5:.5
D5:1 F5:.5 A5:1 G5:.5
F5:1 D5:.5 C5:1 A4:.5
Bb4:1 C5:.5 D5:1 F5:.5
E5:1 D5:.5 C5:1 Bb4:.5
A4:1 C5:.5 E5:1 D5:.5
C5:1 Bb4:.5 A4:1 G4:.5
F4:1 A4:.5 C5:1 E5:.5
D5:1.5 R:1.5
F5:1 E5:1 D5:1 C5:1
D5:1 F5:1 A5:1 G5:1
F5:1 D5:1 C5:1 A4:1
Bb4:2 D5:1 F5:1
E5:1 D5:1 C5:2
B4:1 D5:.5 E5:.5 G5:2
F#5:1 E5:.5 D5:.5 C5:1 B4:1
A4:2 C5:1 E5:1
D5:1 C5:.5 Bb4:.5 A4:2
G4:1 Bb4:1 D5:2
C5:1 Bb4:1 A4:2
G4:1 A4:.5 Bb4:.5 C5:1 D5:1
E5:2 D5:1 C5:1
Bb4:1 A4:1 G4:1 E4:1
D4:3 R:1
F5:.5 E5:1 D5:.5 C5:1
D5:.5 F5:1 A5:.5 G5:1
F5:.5 D5:1 C5:.5 A4:1
Bb4:.5 C5:1 D5:.5 Eb5:1
D5:.5 C5:1 Bb4:.5 A4:1
G4:.5 Bb4:1 D5:.5 C5:1
Bb4:.5 A4:1 G4:.5 F4:1
E4:1.5 R:1.5
F4:1 A4:1 C5:1 D5:1
C5:1 Bb4:1 A4:1 G4:1
F4:1 E4:1 D4:1 C4:1
D4:1 F4:1 R:2''',
 lh='''D3:1 A3:.5 F3:1 G3:.5
Bb2:1 F3:.5 D3:1 C3:.5
G2:1 D3:.5 Bb2:1 F3:.5
Bb2:1 F3:.5 D3:1 C3:.5
C3:1 G3:.5 E3:1 E3:.5
A2:1 E3:.5 G3:1 F3:.5
Bb2:1 F3:.5 D3:1 C3:.5
A2:1 E3:.5 G3:1 F3:.5
D3:1.5 R:1.5
D3:1 A3:1 F3:1 G3:1
Bb2:1 F3:1 D3:1 C3:1
G2:1 D3:1 Bb2:1 F3:1
Bb2+F3:4
C3+G3:4
G3+D4:2 E3+B3:2
D3+A3:2 G3+D4:2
A2+E3:4
D3+A3:4
Eb3+Bb3:4
F3+C4:4
G3+D4:2 F3+C4:2
A2+E3:4
Bb2:1 F3:1 C3:1 E3:1
D3:3 R:1
D3:.5 A3:1 F3:.5 G3:1
Bb2:.5 F3:1 D3:.5 C3:1
G2:.5 D3:1 Bb2:.5 F3:1
Eb3:.5 Bb3:1 G3:.5 D4:1
Bb2:.5 F3:1 D3:.5 C3:1
Eb3:.5 Bb3:1 G3:.5 D4:1
G3:.5 D3:1 Bb2:.5 F3:1
C3:1.5 R:1.5
D3:1 A3:1 F3:1 G3:1
Bb2:1 F3:1 D3:1 C3:1
G2:1 D3:1 A2:1 E3:1
D3:1 A2:1 R:2''',
 tempos=[63,64,65,64,65,64,63,63,62,63,64,65,64,65,66,65,64,65,64,65,64,63,63,62,63,64,65,64,65,64,63,62,63,64,63,63],
 phrases=[(1,4),(5,9),(10,14),(15,20),(21,24),(25,28),(29,32),(33,36)],lower_phrases=[(1,4),(5,9),(10,14),(15,20),(21,24),(25,28),(29,32),(33,36)],
 sections={1:'p',5:'mp',9:'p',10:'p',15:'mp',21:'p',25:'p',29:'pp',33:'p'},lower_sections={1:'pp',5:'p',9:'pp',10:'p',15:'p',21:'pp',25:'pp',33:'pp'},
 pedal=[],hairpins=[('crescendo',2,4),('diminuendo',6,8),('crescendo',15,18),('diminuendo',21,23)])
# Pedal spans follow the changing actual bar lengths; refresh at the paired pulses.
_lengths=[3]*9+[4]*15+[3]*8+[4]*4
_offsets=[sum(_lengths[:i]) for i in range(len(_lengths))]
p['pedal_spans']=sorted([[s+.05,s+1.3] for i,s in enumerate(_offsets) if i<9 or 24<=i<32]+[[s+1.55,s+2.8] for i,s in enumerate(_offsets) if (i<8 or 24<=i<31)]+[[s+.05,s+3.8] for i,s in enumerate(_offsets) if i in [9,10,11,12,13,16,17,18,19,21,22,32,33,34]]+[[s+.05,s+1.8] for i,s in enumerate(_offsets) if i in [14,15,20,35]]+[[s+2.05,s+3.8] for i,s in enumerate(_offsets) if i in [14,15,20]]+[[83.05,85.8]])

p=study(op=376,title='Hazel Transfer',key='d',fifths=-1,meter='6/8',bpm=90,parent=277,
 source=dict(source_opus=277,source_hand='lh',source_start_beat=24,source_end_beat=27,source_pitches=['D','C','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['D','C','A','G']),
 description='A compound dance carries its dotted-quarter pulse into a broader three-step song: the old dotted quarter becomes the new quarter at bar 21. One upper note remains tied across that shared change of pace. The second region follows its own longer melodic path towards a brighter destination, ending with a plain sentence in the lower register.',
 technical='Keep the final old dotted-quarter pulses equal to the first new quarters: the printed dotted-quarter 60 becomes quarter 60 at bar 21. Carry the tied G across the boundary without a new attack. Both hands change pace together; the later phrase breathing resumes within the new pulse. Give the low final sentence clear voicing and a quiet coordinated release.',
 meters=['6/8']*20+['3/4']*28,
 tempo_pivots={21:dict(bpm=60,previous_beat='3/2',new_beat='1')},
 rh='''D5:1 C5:.5 A4:.5 G4:1
A4:.5 C5:.5 D5:.5 F5:1 E5:.5
D5:1 A4:.5 G4:1 F4:.5
E4:.5 G4:.5 A4:.5 C5:1 B4:.5
A4:1 D5:.5 E5:.5 F5:1
G5:.5 F5:.5 E5:.5 D5:1 C5:.5
B4:1 D5:.5 F5:1 E5:.5
D5:1.5 R:1.5
F5:1 A5:.5 G5:1 E5:.5
D5:.5 F5:.5 G5:.5 A5:1 C6:.5
Bb5:1 A5:.5 G5:1 F5:.5
E5:.5 D5:.5 C5:.5 A4:1 G4:.5
F4:1 A4:.5 C5:1 E5:.5
D5:1 C5:.5 Bb4:1 A4:.5
G4:.5 Bb4:.5 D5:.5 F5:1 E5:.5
D5:1.5 R:1.5
A4:1 C5:.5 E5:1 D5:.5
C5:1 B4:.5 A4:1 G4:.5
F4:.5 A4:.5 C5:.5 D5:1 E5:.5
A4:1.5 G4:1.5~
G4:1 A4:1 C5:1
E5:1 D5:1 C5:1
B4:1 D5:.5 E5:.5 G5:1
F#5:1 E5:1 D5:1
C5:1 A4:1 F4:1
E4:1 G4:1 B4:1
A4:1.5 C5:.5 D5:1
E5:2 R:1
G5:1 F5:.5 E5:.5 D5:1
C5:1 Bb4:1 A4:1
G4:1 B4:1 D5:1
C5:1 A4:.5 G4:.5 F4:1
E4:1 G4:.5 A4:.5 C5:1
B4:1 A4:1 G4:1
F#4:1 A4:1 C5:1
B4:2 R:1
D5:1 E5:.5 F#5:.5 A5:1
G5:1 F#5:1 E5:1
D5:1 B4:.5 C5:.5 E5:1
D5:1 C5:1 B4:1
A4:1 C5:.5 D5:.5 E5:1
D5:1 B4:1 G4:1
F#4:1 A4:1 C5:1
B4:2 R:1
D4:1 F#4:1 A4:1
G4:1 F#4:1 E4:1
D4:1 B3:1 A3:1
G3:2 R:1''',
 lh='''D3+A3:1.5 C3+G3:1.5
Bb2+F3:1.5 A2+E3:1.5
G2+D3:1.5 D3+A3:1.5
C3+G3:1.5 E3+B3:1.5
D3+A3:1.5 Bb2+F3:1.5
C3+G3:1.5 F3+C4:1.5
G3+D4:1.5 A3+E4:1.5
D3+A3:1.5 R:1.5
Bb2+F3:1.5 C3+G3:1.5
D3+A3:1.5 F3+C4:1.5
G3+D4:1.5 Bb3+F4:1.5
A3+E4:1.5 C3+G3:1.5
F3+C4:1.5 A3+E4:1.5
Bb3+F4:1.5 D3+A3:1.5
G3+D4:1.5 C3+G3:1.5
D3+A3:1.5 R:1.5
A2+E3:1.5 D3+A3:1.5
C3+G3:1.5 G2+D3:1.5
F2+C3:1.5 A2+E3:1.5
D3+A3:1.5 G2+D3:1.5
F3:1 C4:1 A3:1
C3:1 G3:1 Bb3:1
G3:1 D4:1 B3:1
D3:1 A3:1 C4:1
F3:1 C4:1 A3:1
E3:1 B3:1 G3:1
A2:1 E3:1 G3:1
C3+G3:2 R:1
E3:1 B3:1 G3:1
F3:1 C4:1 A3:1
G3:1 D4:1 F3:1
A2:1 E3:1 G3:1
C3:1 G3:1 E3:1
G2:1 D3:1 B2:1
D3:1 A3:1 C4:1
G2+D3:2 R:1
B2:1 F#3:1 A3:1
E3:1 B3:1 G3:1
C3:1 G3:1 B3:1
G3:1 D3:1 B2:1
A2:1 E3:1 G3:1
G2:1 D3:1 B2:1
D3:1 A3:1 C4:1
G2+D3:2 R:1
B2+F#3:3
E3+B3:3
C3+G3:2 D3+F#3:1
G2+B2:2 R:1''',
 tempos=[90,91,92,91,92,93,91,90,91,92,93,92,91,92,91,90,91,90,90,90,60,60,61,62,61,62,61,60,61,62,63,62,61,62,61,60,61,62,63,62,61,61,60,60,60,61,60,60],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,24),(25,28),(29,36),(37,44),(45,48)],lower_phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,28),(29,36),(37,44),(45,48)],
 sections={1:'p',5:'mp',9:'p',13:'mp',17:'p',21:'p',25:'mp',29:'p',37:'mp',45:'pp'},lower_sections={1:'pp',9:'p',17:'pp',21:'p',29:'pp',37:'p',45:'pp'},
 pedal=sorted([[i*3+.05,i*3+1.3] for i in range(20)]+[[i*3+1.55,i*3+2.8] for i in range(20) if i not in [7,15]]+[[i*3+.05,i*3+2.8] for i in range(20,47) if i not in [27,35,43,46]]+[[i*3+.05,i*3+1.8] for i in [27,35,43,46,47]]+[[140.05,140.8]]),
 hairpins=[('crescendo',2,4),('diminuendo',6,8),('crescendo',9,12),('diminuendo',14,16),('crescendo',21,23),('diminuendo',25,28),('crescendo',37,40),('diminuendo',41,44)])
p['engraving']['pedal_offset_y']=710

p=study(op=377,title='Celandine Forecourt',key='Bb',fifths=-2,meter='3/4',bpm=50,parent=288,
 source=dict(source_opus=288,source_hand='lh',source_voice='tenor',source_start_beat=24,source_end_beat=26.5,source_pitches=['D','G','F#','E'],transposition_semitones=3),motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=3,pitches=['F','Bb','A','G']),
 description='An uneven upper song gives its first nine beats of rhythm to an exposed bass reply. The bass then supports a longer dance while a new upper melody adopts the opening accompaniment’s plain quarter-note pulse. A quiet interior voice colours this second song, which moves through a flat-side region before returning to a gentler B-flat. The bass withdraws before the final upper solo.',
 technical='Keep the first song flexible inside the written beat. Recognise its durations when they move into the bass, without carrying its pitches across. In the second dance sustain the quiet interior line beneath the plain upper steps; differentiate its releases from both the melody and bass.',
 rh='''F4:.5 Bb4:.5 A4:1 G4:1
D5:1 C5:.5 Bb4:.5 A4:1
G4:.5 A4:.5 C5:1 Bb4:1
A4:1 F4:1 R:1
G4:1 Bb4:.5 C5:.5 D5:1
C5:1 A4:.5 G4:.5 F4:1
E4:.5 G4:.5 Bb4:1 A4:1
F4:2 R:1
R:3
R:3
R:3
R:3
F4:1 Bb4:1 A4:1
D5:1 C5:1 Bb4:1
G4:1 A4:1 C5:1
Bb4:2 A4:1
F4:1 G4:1 A4:1
Bb4:1 D5:1 C5:1
A4:1 C5:1 Bb4:1
G4:2 F4:1
E4:1 G4:1 Bb4:1
A4:2 G4:1
F4:1 Ab4:1 C5:1
Bb4:2 Ab4:1
Gb4:1 F4:1 Eb4:1
F4:1 Ab4:1 C5:1
Bb4:1 A4:1 G4:1
F4:1 A4:1 C5:1
Bb4:2 R:1
R:1 Bb4:1 F4:1
G4:.5 A4:.5 Bb4:1 D5:1
C5:1 Bb4:.5 A4:.5 G4:1
F4:1 Bb4:1 R:1''',
 rh_inner='''R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
D4:3
F4:3
Eb4:3
D4:3
C4:3
F4:3
E4:3
C4:3
C4:3
Eb4:3
Db4:3
Eb4:3
Bb3:3
Db4:3
Eb4:3
D4:3
D4:2 R:1
R:3
R:3
R:3
R:3''',
 lh='''Bb2:1 F3:1 D3:1
G2:1 D3:1 F3:1
Eb3:1 Bb3:1 G3:1
F3:1 C3:1 R:1
Eb3:1 G3:1 Bb3:1
D3:1 F3:1 A3:1
C3:1 G3:1 E3:1
F3:2 R:1
F3:.5 Bb3:.5 A3:1 G3:1
D4:1 C4:.5 Bb3:.5 A3:1
G3:.5 A3:.5 C4:1 Bb3:1
F3:1 Eb3:1 R:1
Bb2:.5 D3:.5 F3:1 G3:1
D3:1 F3:.5 G3:.5 A3:1
Eb3:.5 F3:.5 G3:1 Bb3:1
F3:1 D3:.5 C3:.5 Bb2:1
A2:.5 C3:.5 F3:1 E3:1
G2:1 D3:.5 F3:.5 A3:1
C3:.5 E3:.5 G3:1 Bb3:1
F3:1 D3:.5 C3:.5 A2:1
C3:.5 E3:.5 G3:1 Bb3:1
F3:1 Eb3:.5 C3:.5 A2:1
Db3:.5 F3:.5 Ab3:1 C4:1
Eb3:1 G3:.5 Bb3:.5 G3:1
Gb3:.5 Db3:.5 Bb2:1 Db3:1
Ab2:1 Eb3:.5 F3:.5 Ab3:1
C3:.5 Eb3:.5 F3:1 A3:1
F3:1 D3:.5 C3:.5 A2:1
Bb2:2 R:1
R:3
R:3
R:3
R:3''',
 tempos=[50,51,52,50,51,52,51,49,50,51,52,49,50,51,52,51,52,53,52,51,50,49,50,51,50,51,50,49,48,49,50,49,48],
 phrases=[(1,4),(5,8),(13,16),(17,22),(23,29),(30,33)],lower_phrases=[(1,4),(5,8),(9,12),(13,16),(17,22),(23,29)],
 sections={1:'p',5:'mp',13:'p',17:'mp',23:'p',30:'pp'},lower_sections={1:'pp',9:'p',13:'p',23:'pp'},
 hidden_voice_rests={'inner':[1,2,3,4,5,6,7,8,30,31,32,33]},
 voice_phrases=[dict(voice='inner',start_beat=36,end_beat=48,swell=-1),dict(voice='inner',start_beat=48,end_beat=66,swell=-1),dict(voice='inner',start_beat=66,end_beat=86,swell=-1)],
 page_starts=[7,13,19,25,31],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=710),
 pedal=sorted([[i*3+.05,i*3+2.8] for i in list(range(12,28))+[0,1,2,4,5,6,8,9,10,30,31]]+[[i*3+.05,i*3+1.8] for i in [3,7,11,28,32]]),
 hairpins=[('crescendo',2,3),('diminuendo',6,8),('crescendo',17,19),('diminuendo',20,22),('diminuendo',26,29)])
p['performance']['lower_entries']=[[24,35],[36,86]]

p=study(op=378,title='Bracken Cutaway',key='g',fifths=-2,meter='3/4',bpm=51,parent=283,
 source=dict(source_opus=283,source_hand='rh',source_start_beat=12,source_end_beat=15,source_pitches=['D','C','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['D','C','A','G']),
 description='A complete waltz phrase returns first as two bars, then one, then only its first three and two attacks. Newly voiced links keep changing what these shortened approaches might reach. A sustained middle song recovers the lost breathing space through warmer harmony. The final remnant loosens into an exposed melodic tone after the accompaniment has finished.',
 technical='Preserve the lengths of the written gaps as the theme contracts. Let each new bass route change the weight of the remaining notes, rather than making every fragment an identical accent. Sustain the tied entrance to the broad song, release the dance support fully, and keep the final exposed tone quiet and unhurried.',
 rh='''D5:.5 C5:.5 A4:.5 G4:1.5
Bb4:1 A4:.5 G4:.5 F4:1
G4:1 Bb4:1 D5:1
C5:.5 Bb4:.5 A4:1 F#4:1
G4:2 A4:.5 Bb4:.5
D5:1 C5:1 R:1
G4:1 A4:.5 Bb4:.5 C5:1
A4:2 R:1
D5:.5 C5:.5 A4:.5 G4:1.5
Bb4:1 A4:.5 G4:.5 F4:1
Eb5:1 D5:1 Bb4:1
D5:.5 C5:.5 A4:.5 G4:1.5
F4:1 A4:1 C5:1
D5:.5 C5:.5 A4:.5 R:1.5
Ab4:1 C5:1 Eb5:1
D5:.5 C5:.5 R:2
R:3
G4:3~
G4:1 A4:1 Bb4:1
D5:2 C5:1
Bb4:1 A4:1 G4:1
F4:1 A4:1 C5:1
Eb5:2 D5:1
C5:1 Bb4:1 A4:1
G4:2 R:1
F4:1 Ab4:1 C5:1
Bb4:2 Ab4:1
G4:1 F4:1 Eb4:1
D4:1 F4:1 A4:1
G4:2 R:1
D5:.5 C5:.5 A4:2
Bb4:1 A4:1 G4:1
A4:2 R:1
D5:2 R:1''',
 lh='''G2:.5 R:.5 Bb3+D4:1 A3+C4:1
Eb3:.5 R:.5 G3+Bb3:1 D3:1
C3:.5 R:.5 Eb3+G3:1 Bb3:1
D3:.5 R:.5 F#3+A3:1 C4:1
Eb3:1 G3+Bb3:1 D3:1
F3:.5 R:.5 A3+C4:1 R:1
C3:1 E3+G3:1 Bb3:1
D3:1 F#3+A3:1 R:1
Eb3:.5 R:.5 G3+Bb3:1 C4:1
Bb2:1 F3+A3:1 D3:1
C3:.5 R:.5 Eb3+G3:1 Bb3:1
G2:1 D3+F3:1 Bb3:1
F3:.5 R:.5 A3+C4:1 Eb3:1
Bb2:1 D3+F3:.5 R:1.5
Ab2:1 Eb3+G3:1 C4:1
A2:1 R:2
D3:1 F#3+A3:1 R:1
G2:1 D3:1 Bb3:1
Eb3:1 G3:1 Bb3:1
Bb2:1 F3:1 A3:1
C3:1 Eb3:1 G3:1
F3:1 C4:1 A3:1
Eb3:1 Bb3:1 G3:1
D3:1 A3:1 F#3:1
G2:1 D3:1 R:1
Db3:1 Ab3:1 F3:1
Eb3:1 G3:1 Bb3:1
C3:1 Eb3:1 G3:1
D3:1 F#3:1 A3:1
G2:1 D3:1 R:1
Eb3+G3:3
R:3
R:3
R:3''',
 tempos=[51,52,53,52,51,52,51,50,52,53,54,53,52,51,52,50,48,49,50,51,50,51,52,51,50,49,50,51,50,49,50,49,48,48],
 phrases=[(1,6),(7,8),(9,10),(11,12),(13,14),(15,16),(18,25),(26,30),(31,34)],lower_phrases=[(1,6),(7,8),(9,12),(13,16),(18,25),(26,30)],
 sections={1:'p',5:'mp',9:'p',13:'mp',17:'pp',18:'p',23:'mp',26:'p',31:'pp'},lower_sections={1:'pp',9:'p',17:'pp',18:'pp',26:'pp'},
 pedal=sorted([[i*3+.05,i*3+2.8] for i in list(range(17,24))+list(range(25,29))+[0,1,2,3,4,6,8,9,10,11,12,14,30]]+[[i*3+.05,i*3+1.8] for i in [5,7,16,24,29]]+[[39.05,40.3],[45.05,45.8],[99.05,100.8]]),
 hairpins=[('crescendo',2,4),('diminuendo',5,6),('crescendo',18,21),('diminuendo',23,25),('diminuendo',27,30)])

p=study(op=379,title='Dogrose Margins',key='g',fifths=-2,meter='4/4',bpm=70,parent=287,
 source=dict(source_opus=287,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['D','C','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3.5,pitches=['D','C','A','G']),
 description='A chordal dance grows from four to five and then seven quarter beats. Its first statement acquires one extra attack-and-rest unit, then two more, each opening a further harmonic implication. A longer chorale thins that busy extension into sustained voice leading. Four compact triple bars finally settle the phrase with a coordinated release. Every sounded event is a chord.',
 technical='Voice the upper line through each chord without turning the short lower notes into accents. Count the added attack-and-rest units exactly, clearing the pedal before their gaps. Let the chorale remain connected through finger changes and small bass motions; keep its inner intervals softer than the principal line.',
 rh='''A4+D5:.5 G4+C5:.5 F4+A4:2 E4+G4:.5 R:.5
G4+Bb4:1 F4+A4:1 Eb4+G4:1 D4+F4:.5 R:.5
Eb4+G4:1 G4+Bb4:1 A4+C5:1 Bb4+D5:.5 R:.5
A4+C5:.5 G4+Bb4:.5 F#4+A4:2 E4+G4:.5 R:.5
D4+F4:1 F4+A4:1 G4+Bb4:1 A4+C5:.5 R:.5
F#4+A4:1 E4+G4:1 D4+F#4:1 R:1
A4+D5:.5 G4+C5:.5 F4+A4:2 E4+G4:.5 R:.5 Bb4+D5:.5 R:.5
G4+Bb4:1 F4+A4:1 Eb4+G4:1 D4+F4:.5 R:.5 F4+Ab4:.5 R:.5
Eb4+G4:1 G4+Bb4:1 A4+C5:1 Bb4+D5:.5 R:.5 C5+Eb5:.5 R:.5
Bb4+D5:1 Ab4+C5:1 G4+Bb4:1 F4+Ab4:.5 R:.5 Eb4+G4:.5 R:.5
D4+F4:1 F4+Ab4:1 G4+Bb4:1 Ab4+C5:.5 R:.5 A4+C5:.5 R:.5
F#4+A4:1 A4+C5:1 G4+Bb4:1 F#4+A4:1 R:1
A4+D5:.5 G4+C5:.5 F4+A4:2 E4+G4:.5 R:.5 Bb4+D5:.5 R:.5 Eb5+G5:.5 R:.5 D5+F5:.5 R:.5
C5+Eb5:1 Bb4+D5:1 A4+C5:1 G4+Bb4:1 F4+A4:1 Eb4+G4:1 R:1
F4+Ab4:1 Ab4+C5:1 Bb4+Db5:1 C5+Eb5:1 Db5+F5:1 Eb5+G5:1 R:1
D5+F5:1 C5+Eb5:1 Bb4+D5:1 A4+C5:1 Ab4+B4:1 G4+Bb4:1 R:1
F4+A4:1 G4+Bb4:1 A4+C5:1 Bb4+D5:1 C5+Eb5:1 A4+C5:1 R:1
G4+Bb4:1 F#4+A4:1 G4+Bb4:2 A4+C5:1 D5+F#5:1 R:1
Bb4+D5:3 A4+C5:3
G4+Bb4:2 F4+A4:2 Eb4+G4:2
F4+Ab4:3 G4+Bb4:3
Ab4+C5:2 Bb4+Db5:2 C5+Eb5:2
Bb4+D5:3 A4+C5:3
G4+Bb4:2 F#4+A4:2 E4+G4:2
F4+A4:3 G4+Bb4:3
F#4+A4:2 G4+Bb4:2 A4+C5:1 R:1
Bb4+D5:1 A4+C5:1 G4+Bb4:1
F4+A4:1 Eb4+G4:1 D4+F4:1
E4+G4:1 F#4+A4:1 D4+F#4:1
D4+G4:2 R:1''',
 lh='''G2+D3:.5 A2+E3:.5 Bb2+F3:2 C3+G3:.5 R:.5
Eb3+Bb3:1 D3+A3:1 C3+G3:1 Bb2+F3:.5 R:.5
C3+G3:1 Eb3+Bb3:1 F3+C4:1 G3+D4:.5 R:.5
F3+C4:.5 Eb3+Bb3:.5 D3+A3:2 C3+G3:.5 R:.5
Bb2+F3:1 D3+A3:1 Eb3+Bb3:1 F3+C4:.5 R:.5
D3+A3:1 C3+G3:1 A2+E3:1 R:1
Eb3+Bb3:.5 F3+C4:.5 G3+D4:2 C3+G3:.5 R:.5 Bb2+F3:.5 R:.5
Eb3+Bb3:1 D3+A3:1 C3+G3:1 Bb2+F3:.5 R:.5 Db3+Ab3:.5 R:.5
C3+G3:1 Eb3+Bb3:1 F3+C4:1 G3+D4:.5 R:.5 Ab3+Eb4:.5 R:.5
G3+D4:1 F3+C4:1 Eb3+Bb3:1 Db3+Ab3:.5 R:.5 C3+G3:.5 R:.5
Bb2+F3:1 Db3+Ab3:1 Eb3+Bb3:1 F3+C4:.5 R:.5 F#3+C4:.5 R:.5
D3+A3:1 F#3+C4:1 Eb3+Bb3:1 D3+A3:1 R:1
Bb2+F3:.5 C3+G3:.5 D3+A3:2 C3+G3:.5 R:.5 Eb3+Bb3:.5 R:.5 C3+G3:.5 R:.5 Bb2+F3:.5 R:.5
Ab2+Eb3:1 G2+D3:1 F2+C3:1 Eb2+Bb2:1 D2+A2:1 C2+G2:1 R:1
Db3+Ab3:1 F3+C4:1 Gb3+Db4:1 Ab3+Eb4:1 Bb3+F4:1 C4+G4:1 R:1
Bb3+F4:1 Ab3+Eb4:1 G3+D4:1 F3+C4:1 D3+Ab3:1 Eb3+Bb3:1 R:1
D3+A3:1 Eb3+Bb3:1 F3+C4:1 G3+D4:1 Ab3+Eb4:1 F#3+C4:1 R:1
Eb3+Bb3:1 D3+A3:1 Eb3+Bb3:2 F#3+C4:1 A3+D4:1 R:1
G3+Bb3:3 F3+A3:3
Eb3+G3:2 D3+F3:2 C3+Eb3:2
Db3+F3:3 Eb3+G3:3
F3+Ab3:2 Gb3+Bb3:2 Ab3+C4:2
G3+Bb3:3 F3+A3:3
Eb3+G3:2 D3+F#3:2 C3+E3:2
D3+F3:3 Eb3+G3:3
D3+F#3:2 Eb3+G3:2 F#3+A3:1 R:1
G3+Bb3:1 F3+A3:1 Eb3+G3:1
D3+F3:1 C3+Eb3:1 Bb2+D3:1
C3+E3:1 D3+F#3:1 A2+D3:1
G2+B2:2 R:1''',
 meters=['4/4']*6+['5/4']*6+['7/4']*6+['3/2']*8+['3/4']*4,
 tempos=[70,71,72,71,70,68,70,71,72,71,70,69,70,71,72,73,72,70,69,70,71,70,69,70,69,68,69,70,69,68],
 phrases=[(1,6),(7,12),(13,18),(19,22),(23,26),(27,30)],lower_phrases=[(1,6),(7,12),(13,18),(19,22),(23,26),(27,30)],
 sections={1:'p',7:'p',13:'mp',19:'p',23:'mp',27:'pp'},lower_sections={1:'pp',7:'pp',13:'p',19:'pp',27:'pp'},
 pedal=[],hairpins=[('crescendo',2,4),('diminuendo',5,6),('crescendo',8,10),('diminuendo',11,12),('crescendo',14,16),('diminuendo',17,18),('crescendo',20,22),('diminuendo',24,26)])
_lengths=[4]*6+[5]*6+[7]*6+[6]*8+[3]*4
_starts=[sum(_lengths[:i]) for i in range(30)]
p['pedal_spans']=sorted([[s+.05,s+2.8] for i,s in enumerate(_starts) if i in [0,1,2,3,4,5,6,7,8,9,10,11,12]]+[[s+.05,s+5.8] for i,s in enumerate(_starts) if 13<=i<18]+[[s+.05,s+2.8] for i,s in enumerate(_starts) if i in [18,20,22,24]]+[[s+3.05,s+5.8] for i,s in enumerate(_starts) if i in [18,20,22,24]]+[[s+j+.05,s+j+1.8] for i,s in enumerate(_starts) if i in [19,21,23,25] for j in [0,2]]+[[s+.05,s+2.8] for i,s in enumerate(_starts) if i in [26,27,28]]+[[_starts[29]+.05,_starts[29]+1.8]])

p=study(op=380,title='Thistle Junction',key='d',fifths=-1,meter='3/4',bpm=70,parent=290,
 source=dict(source_opus=290,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['F','E','D','C'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['F','E','D','C']),
 description='A generous triple dance alternates with a shorter five-eighth answer. Its returns contract from eight to six to four bars, while the asymmetric answers grow from six to eight. A continuous four-beat song becomes the centre of gravity. The closing eleven-eighth bars join the three quarter steps and the answer’s long-short-long gesture through their unchanged eighth-note subdivision.',
 technical='Keep the same eighth-note subdivision through every change of metre. Let the five-eighth answer lean on its written long-short-long shape without an added swing setting. In the closing bars hear the three quarters followed by the complete five-eighth gesture, allowing their shared phrase to settle without slowing the final rest.',
 rh='''F5:1 E5:1 D5:1
C5:2 D5:1
A4:1 C5:1 E5:1
D5:2 C5:1
Bb4:1 A4:.5 G4:.5 F4:1
G4:1 A4:1 C5:1
B4:1 A4:1 G4:1
A4:2 R:1
D5:1 F5:.5 E5:1
C5:1 E5:.5 D5:1
Bb4:1 D5:.5 C5:1
A4:1 C5:.5 Bb4:1
G4:1 Bb4:.5 A4:1
F4:1 E4:.5 R:1
F5:1 E5:1 D5:1
C5:2 D5:1
Bb4:1 D5:1 F5:1
E5:2 D5:1
C5:1 Bb4:1 A4:1
G4:2 R:1
D5:1 F5:.5 E5:1
C5:1 E5:.5 D5:1
Bb4:1 Db5:.5 C5:1
Ab4:1 C5:.5 Bb4:1
Gb4:1 Bb4:.5 Ab4:1
F4:1 Ab4:.5 G4:1
E4:1 G4:.5 Bb4:1
A4:1 G4:.5 R:1
F4:1 A4:1 D5:2
C5:1 E5:1 G5:2
F5:2 E5:1 D5:1
C5:1 Bb4:1 A4:2
G4:1 B4:1 D5:2
C5:2 B4:1 A4:1
G4:1 F4:1 E4:1 G4:1
A4:3 R:1
F5:1 E5:1 D5:1
C5:2 D5:1
Bb4:1 A4:1 G4:1
A4:2 R:1
F5:1 E5:1 D5:1 C5:1 E5:.5 D5:1
Bb4:1 A4:1 G4:1 F4:1 A4:.5 G4:1
E4:1 G4:1 Bb4:1 A4:1 G4:.5 E4:1
D4+F4:3 R:2.5''',
 lh='''D3:1 A3:1 F3:1
C3:1 G3:1 E3:1
F3:1 C4:1 A3:1
Bb2:1 F3:1 A3:1
G2:1 D3:1 Bb3:1
C3:1 E3:1 G3:1
E3:1 B3:1 D4:1
A3:2 R:1
Bb3:1 A3:.5 F3:1
G3:1 F3:.5 D3:1
Eb3:1 G3:.5 A3:1
D3:1 F3:.5 G3:1
C3:1 E3:.5 F3:1
A2:1 C3:.5 R:1
D3:1 F3:1 A3:1
C3:1 E3:1 G3:1
Bb2:1 F3:1 A3:1
C3:1 G3:1 Bb3:1
F3:1 A3:1 C4:1
G3:2 R:1
Bb3:1 A3:.5 F3:1
G3:1 F3:.5 D3:1
Gb3:1 F3:.5 Db3:1
Eb3:1 G3:.5 Ab3:1
Cb3:1 Eb3:.5 F3:1
Bb2:1 Db3:.5 Eb3:1
C3:1 E3:.5 G3:1
A2:1 E3:.5 R:1
D3:1 F3:1 A3:1 C4:1
C3:1 G3:1 B3:1 E4:1
Bb3:1 A3:1 F3:1 D3:1
F3:1 C4:1 E4:1 C4:1
G3:1 D4:1 B3:1 A3:1
E3:1 G3:1 B3:1 D4:1
C4:1 A3:1 G3:1 E3:1
A2:1 E3:1 G3:1 R:1
D3:1 F3:1 A3:1
C3:1 E3:1 G3:1
G2:1 D3:1 Bb3:1
A3:2 R:1
Bb3:1 A3:1 F3:1 G3:1 F3:.5 D3:1
G2:1 Bb2:1 D3:1 Eb3:1 D3:.5 Bb2:1
C3:1 E3:1 G3:1 F#3:1 E3:.5 C#3:1
D3+A3:3 R:2.5''',
 meters=['3/4']*8+['5/8']*6+['3/4']*6+['5/8']*8+['4/4']*8+['3/4']*4+['11/8']*4,
 tempos=[70,71,72,71,72,71,70,69,70,71,72,71,70,69,70,71,72,71,70,69,70,71,72,73,72,71,70,69,68,69,70,71,70,69,68,68,69,70,69,68,69,69,68,68],
 phrases=[(1,4),(5,8),(9,14),(15,20),(21,28),(29,36),(37,40),(41,44)],lower_phrases=[(1,4),(5,8),(9,14),(15,20),(21,28),(29,36),(37,40),(41,44)],
 sections={1:'p',5:'mp',9:'p',15:'p',21:'mp',29:'p',33:'mp',37:'p',41:'pp'},lower_sections={1:'pp',9:'p',15:'pp',21:'p',29:'pp',37:'pp',41:'pp'},
 pedal=[],hairpins=[('crescendo',2,4),('diminuendo',6,8),('crescendo',16,18),('diminuendo',19,20),('crescendo',22,25),('diminuendo',26,28),('crescendo',30,32),('diminuendo',34,36),('diminuendo',42,43)])
_lengths=[3]*8+[2.5]*6+[3]*6+[2.5]*8+[4]*8+[3]*4+[5.5]*4
_starts=[sum(_lengths[:i]) for i in range(44)]
p['pedal_spans']=sorted([[s+.05,s+length-.2] for i,(s,length) in enumerate(zip(_starts,_lengths)) if i not in [7,13,19,27,35,39,40,41,42,43]]+[[s+.05,s+length-1.2] for i,(s,length) in enumerate(zip(_starts,_lengths)) if i in [7,13,19,27,35,39]]+[[s+.05,s+2.8] for i,s in enumerate(_starts) if i in [40,41,42,43]]+[[s+3.05,s+5.3] for i,s in enumerate(_starts) if i in [40,41,42]])
