"""Individually authored Returning Light, CWS Op.391–400."""
from weather_common import make_study
PIECES=[]
def study(**kwargs):
    p=make_study(**kwargs);PIECES.append(p);return p

p=study(op=391,title='Linden Lucency',key='c',fifths=-3,meter='4/4',bpm=56,parent=321,
 source=dict(source_opus=321,source_hand='rh',source_start_beat=55.5,source_end_beat=58.5,source_pitches=['G','Ab','Bb','C'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['G','Ab','Bb','C']),
 description='A seven-bar melody first moves above four long bass sonorities and ends over a waiting G. Its complete return keeps every melodic pitch and duration while more frequent changes of harmony lead its final G into an E-flat-major arrival. A two-bar turn opens a longer new continuation, whose wider tonal route eventually finds a modest rise and a settled E-flat sonority.',
 technical='Preserve the same melodic breath through both complete statements, even as the harmony changes more often beneath the second. Hold the opening bass ties with the fingers. Make each later bass change a quiet shift of colour, clearing pedal at the written boundaries without accenting every new chord. Allow the new continuation to grow in direction rather than weight.',
 rh='''G4:1 Ab4:.5 Bb4:1 C5:.5 Eb5:1
D5:1 C5:.5 Bb4:.5 G4:2
Ab4:2 G4:.5 F4:.5 Eb4:1
F4:1 Ab4:.5 C5:.5 Bb4:2
G4:1 Bb4:.5 D5:.5 C5:2
Ab4:1 G4:.5 F4:.5 Eb4:2
D4:1 F4:1 G4:2
G4:1 Ab4:.5 Bb4:1 C5:.5 Eb5:1
D5:1 C5:.5 Bb4:.5 G4:2
Ab4:2 G4:.5 F4:.5 Eb4:1
F4:1 Ab4:.5 C5:.5 Bb4:2
G4:1 Bb4:.5 D5:.5 C5:2
Ab4:1 G4:.5 F4:.5 Eb4:2
D4:1 F4:1 G4:2
Bb4:1 Ab4:.5 G4:.5 F4:2
Eb4:1 F4:1 G4:1 R:1
Ab4:1 C5:.5 Eb5:2.5
Db5:1 C5:.5 Bb4:.5 Ab4:2
Gb4:1 Bb4:.5 Db5:.5 F5:2
Eb5:2 Db5:1 C5:1
Bb4:1 Ab4:.5 Gb4:.5 F4:2
Eb4:1 F4:.5 Ab4:.5 C5:2
Bb4:1 G4:.5 Eb4:.5 F4:2
G4:1 Bb4:.5 D5:.5 C5:2
Ab4:1 G4:.5 F4:.5 Eb4:2
D4:1 F4:.5 Ab4:.5 G4:2
Eb4:1 G4:.5 Bb4:.5 C5:2
Bb4:1 Ab4:.5 G4:.5 F4:2
G4:1 Ab4:.5 Bb4:.5 D5:1 C5:1
Eb4+G4:3 R:1''',
 lh='''C3+G3:4~
C3+G3:4
Ab2+Eb3:4~
Ab2+Eb3:4
F3+Ab3:4
G2+D3:4~
G2+D3:4
Eb3+Bb3:2 F3+Ab3:2
G3+B3:1 C3+Eb3:1 Ab2+Eb3:2
Db3+F3:2 Eb3+G3:1 Ab2+C3:1
Bb2+F3:2 Eb3+G3:2
C3+Eb3:1 D3+F3:1 Eb3+G3:2
Ab2+Eb3:1 Bb2+F3:1 C3+G3:2
Bb2+D3:2 Eb3+Bb3:2
Ab2:1 Eb3:1 F3:1 Bb2:1
Eb3:1 Bb2:1 Eb3:1 R:1
Ab2:1 Eb3:.5 G3:.5 C4:2
Db3:1 Ab2:.5 C3:.5 F3:2
Gb2:1 Db3:.5 F3:.5 Bb3:2
Ab3:1 Gb3:1 Db3:2
Eb3:1 Bb2:.5 Db3:.5 F3:2
Ab2:1 Eb3:.5 G3:.5 C4:2
Eb3:1 Bb2:.5 D3:.5 Ab3:2
C3:1 G3:.5 Bb3:.5 E3:2
F3:1 C3:.5 Eb3:.5 Ab3:2
Bb2:1 F3:.5 Ab3:.5 D3:2
Eb3:1 Bb2:.5 D3:.5 G3:2
Ab2:1 Eb3:.5 G3:.5 C4:2
Bb2:1 F3:.5 Ab3:.5 Eb3:1 Bb2:1
Eb3+Bb3:3 R:1''',
 tempos=[56,57,58,57,56,55,54,56,57,58,59,58,57,56,55,54,56,57,58,59,58,57,56,57,56,55,56,55,54,54],
 phrases=[(1,7),(8,14),(15,16),(17,23),(24,30)],lower_phrases=[(15,16),(17,23),(24,30)],
 sections={1:'p',8:'p',12:'mp',15:'p',17:'p',20:'mp',24:'p',28:'pp'},lower_sections={1:'pp',8:'p',17:'p',24:'pp'},
 pedal=sorted([[4*i+.05,4*i+3.8] for i in list(range(7))+list(range(16,29))]+[[28.05,29.8],[30.05,31.8],[32.05,32.8],[33.05,33.8],[34.05,35.8],[36.05,37.8],[38.05,38.8],[39.05,39.8],[40.05,41.8],[42.05,43.8],[44.05,44.8],[45.05,45.8],[46.05,47.8],[48.05,48.8],[49.05,49.8],[50.05,51.8],[52.05,53.8],[54.05,55.8],[56.05,59.8],[60.05,62.8],[116.05,118.8]]),
 hairpins=[('crescendo',2,4),('diminuendo',5,7),('crescendo',9,11),('diminuendo',13,14),('crescendo',18,19),('diminuendo',21,23),('crescendo',25,27),('diminuendo',28,30)])

p=study(op=392,title='Pear Parterre',key='G',fifths=1,meter='6/4',bpm=72,parent=239,
 source=dict(source_opus=239,source_hand='lh',source_start_beat=61,source_end_beat=70,source_pitches=['D','E','F#','G'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=9,pitches=['D','E','F#','G']),
 description='Two chord songs undergo linked variations. The first rises in unequal long values; the second begins with a quicker, more widely spaced reply and a distinctive cadential rhythm. The first variation retains its opening but adopts the second song’s closing rhythm. The second variation keeps its melodic head while drawing its upper chords into thirds and borrowing the first song’s ascending bass head one octave lower. Four shared closing bars lead to a coordinated C-major chord.',
 technical='Voice the top of each chord as a melody, keeping all written pitches together without added rolls. Distinguish the generous first song from the lighter, drier second. In the second variation, coordinate the differently timed chord changes of the hands without disturbing either line. Use the selective pedal only where marked; preserve finger connection and complete the final shared release.',
 rh='''B4+D5:2 C5+E5:3 D5+F#5:1~
D5+F#5:1 E5+G5:2 D5+F#5:1 C5+E5:2
B4+D5:1.5 A4+C5:.5 G4+B4:2 A4+D5:2
B4+E5:2 C5+F#5:1 D5+G5:3
B4+D5:3 G4+B4:2 R:1
C5+E5:1.5 D5+G5:.5 Bb4+F5:2 A4+D5:2
G4+C5:2 A4+D5:1 B4+E5:3
C5+F5:1 E5+G5:1 D5+F5:2 B4+E5:2
A4+C5:.5 G4+B4:.5 F4+A4:1 E4+G4:3 R:1
B4+D5:2 C5+E5:3 D5+F#5:1~
D5+F#5:1 E5+G5:2 F5+A5:1 E5+G5:2
D5+F#5:1.5 C5+E5:.5 B4+D5:2 A4+C5:2
G4+B4:2 A4+C5:1 B4+D5:3
C5+E5:2 D5+F5:1 E5+G5:3
D5+F5:1 C5+E5:1 B4+D5:2 A4+C5:2
G4+B4:.5 F4+A4:.5 E4+G4:1 E4+C5:3 R:1
C5+E5:1.5 E5+G5:.5 D5+F5:2 B4+D5:2
A4+C5:2 B4+D5:1 C5+E5:3
D5+F5:1 E5+G5:1 F5+A5:2 E5+G5:2
D5+F5:2 C5+E5:1 B4+D5:3
A4+C5:1 G4+B4:1 F4+A4:2 G4+C5:2
G4+B4:3 E4+G4:2 R:1
C5+E5:2 D5+F#5:1 E5+G5:3
D5+F5:1 C5+E5:1 B4+D5:2 A4+C5:2
G4+B4:.5 F4+A4:.5 E4+G4:1 D4+F4:3 R:1
E4+G4:5 R:1''',
 lh='''G3+D4:2 A3+E4:3 B3+F#4:1~
B3+F#4:1 C4+G4:2 D3+A3:1 C3+G3:2
G2+D3:1.5 A2+E3:.5 B2+F#3:2 D3+F#3:2
C3+G3:2 D3+A3:1 G3+B3:3
G3+D4:3 G2+D3:2 R:1
A2+E3:1.5 C3+G3:.5 D3+A3:2 F3+A3:2
E3+G3:2 F3+A3:1 G3+B3:3
A2+E3:1 C3+G3:1 D3+A3:2 E3+G3:2
F3+A3:.5 E3+G3:.5 D3+F3:1 C3+G3:3 R:1
E3+G3:2 F3+A3:3 G3+B3:1~
G3+B3:1 A3+C4:2 D3+A3:1 C3+G3:2
D3+A3:1.5 E3+B3:.5 F#3+A3:2 G3+B3:2
E3+G3:2 F3+A3:1 G3+B3:3
A3+C4:2 Bb3+D4:1 C3+G3:3
Bb2+F3:1 A2+E3:1 G2+D3:2 F2+C3:2
E3+G3:.5 D3+F3:.5 C3+E3:1 C3+G3:3 R:1
G2+D3:2 A2+E3:3 B2+F#3:1~
B2+F#3:1 C3+G3:2 D3+A3:1 E3+B3:2
D3+A3:1 C3+G3:1 F3+A3:2 E3+G3:2
Bb2+F3:2 C3+G3:1 G2+D3:3
A2+E3:1 B2+F#3:1 C3+G3:2 F3+A3:2
E3+G3:3 C3+G3:2 R:1
A2+E3:2 D3+A3:1 G2+D3:3
Bb2+F3:2 C3+G3:2 D3+A3:2
G2+D3:.5 A2+E3:.5 Bb2+F3:1 G2+F3:3 R:1
C3+G3:5 R:1''',
 tempos=[72,73,74,73,71,72,74,73,71,72,74,75,74,75,73,71,72,73,75,74,72,71,72,71,70,70],
 phrases=[(1,5),(6,9),(10,16),(17,22),(23,26)],lower_phrases=[(1,5),(6,9),(10,16),(17,22),(23,26)],
 sections={1:'p',6:'p',10:'mp',14:'p',17:'p',19:'mp',23:'p',25:'pp'},lower_sections={1:'pp',6:'p',10:'p',17:'p',23:'pp'},
 pedal=[[.05,1.8],[2.05,4.8],[5.05,6.8],[7.05,8.8],[9.05,9.8],[10.05,11.8],[18.05,19.8],[20.05,20.8],[21.05,23.8],[24.05,26.8],[27.05,28.8],[72.05,73.8],[74.05,74.8],[75.05,77.8],[78.05,79.8],[80.05,80.8],[81.05,83.8],[92.05,94.8],[126.05,128.8],[129.05,130.8],[146.05,148.8],[150.05,154.8]],
 hairpins=[('crescendo',2,3),('diminuendo',4,5),('crescendo',7,8),('crescendo',11,13),('diminuendo',14,16),('crescendo',17,18),('diminuendo',20,22),('diminuendo',23,26)])

p=study(op=393,title='Aster Camber',key='e',fifths=1,meter='3/4',bpm=48,parent=355,
 source=dict(source_opus=355,source_hand='rh',source_voice='inner',source_start_beat=90,source_end_beat=96,source_pitches=['E','F#','E','F#'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['E','F#','E','F#']),
 description='An E–F-sharp oscillation grows into a first song with Dorian warmth. Its complete four-note figure then expands by a factor of four around E: the two-semitone reach becomes an eight-semitone reach to C, with the same rhythm and direction. C and F foundations make that wider interval a harmonic opening. Freely composed continuations explore the new space. The narrow figure returns above a C foundation and keeps that destination in its compact ending.',
 technical='Give the narrow opening a connected, uninsistent tone. Prepare the wider E-to-C reach during the dotted-quarter pulse without accenting either arrival. The exact interval expansion belongs to bars ten and eleven; let the following song develop freely. On the return, preserve the opening rhythm while allowing the changed bass to alter its colour. End with the modest E over C fully settled.',
 rh='''E4:1.5 F#4:1.5
E4:1.5 F#4:1.5
G4:1 F#4:.5 E4:1.5
B4:1 A4:.5 G4:.5 F#4:1
E4:1 G4:.5 C#5:1.5
B4:1 A4:.5 F#4:1.5
G4:1 A4:.5 B4:.5 D5:1
C#5:1 B4:.5 A4:.5 G4:1
F#4:1.5 E4:1 R:.5
E4:1.5 C5:1.5
E4:1.5 C5:1.5
D5:1 C5:.5 B4:.5 A4:1
G4:1 B4:.5 E5:1.5
D5:1 F5:.5 E5:1.5
C5:1 Bb4:.5 A4:.5 G4:1
F4:1 A4:.5 D5:1.5
C5:1 Eb5:.5 D5:1.5
Bb4:1 A4:.5 G4:.5 F4:1
E4:1 G4:.5 C5:1.5
B4:1 D5:.5 C5:1.5
A4:1 G4:.5 F#4:.5 E4:1
D4:1 F4:.5 B4:1.5
A4:1 G4:.5 F4:.5 E4:1
D4:1 F#4:1 G4:.5 R:.5
E4:1.5 F#4:1.5
E4:1.5 F#4:1.5
G4:1 F#4:.5 E4:1.5
D4:1 E4:.5 G4:1.5
F#4:1 E4:.5 D4:.5 C4:1
E4:1 G4:.5 A4:1.5
G4:1 F#4:.5 E4:.5 D4:1
E4:2 R:1''',
 lh='''E3+B3:3
D3+A3:3
C#3:1 E3:.5 G3:1.5
D3:1 A3:.5 F#3:1.5
A2:1 E3:.5 G3:1.5
B2:1 F#3:.5 A3:1.5
E3:1 G3:.5 B3:.5 F#3:1
A2:1 E3:.5 G3:.5 B2:1
E3+B3:2.5 R:.5
C3+G3:3
F3+A3:3
G2:1 D3:.5 F3:.5 B2:1
C3:1 E3:.5 G3:1.5
F3:1 A3:.5 C4:1.5
Bb2:1 F3:.5 A3:.5 D3:1
D3:1 A3:.5 C4:1.5
G3:1 D3:.5 F3:1.5
Eb3:1 Bb2:.5 D3:.5 Ab3:1
A2:1 E3:.5 G3:1.5
D3:1 A3:.5 C4:1.5
G3:1 D3:.5 F#3:.5 A3:1
G2+F3:3
C3:1 E3:.5 G3:.5 Bb2:1
D3:1 F#3:1 G3:.5 R:.5
C3+G3:3
E3+G3:3
F3:1 A3:.5 C3:1.5
G2:1 B2:.5 F3:1.5
A2:1 C3:.5 F3:.5 E3:1
F3:1 C3:.5 E3:1.5
G2:1 D3:.5 F3:.5 B2:1
C3+G3:2 R:1''',
 tempos=[48,49,50,49,50,49,48,47,46,48,49,50,51,52,51,50,51,50,49,50,49,48,47,46,48,49,48,47,48,47,46,46],
 phrases=[(1,9),(10,15),(16,24),(25,32)],lower_phrases=[(3,9),(12,15),(16,24),(27,32)],
 sections={1:'p',5:'mp',10:'p',13:'mp',16:'p',20:'mp',25:'p',29:'pp'},lower_sections={1:'pp',10:'p',16:'p',25:'pp'},
 pedal=[[.05,2.8],[3.05,5.8],[24.05,26.3],[27.05,29.8],[30.05,32.8],[72.05,74.8],[75.05,77.8],[93.05,94.8]],
 hairpins=[('crescendo',2,4),('diminuendo',6,9),('crescendo',10,12),('diminuendo',14,15),('crescendo',17,19),('diminuendo',21,24),('diminuendo',26,28)])
p['engraving']['pedal_offset_y']=710

p=study(op=394,title='Quince Skylane',key='C',fifths=0,meter='4/4',bpm=62,parent=339,
 source=dict(source_opus=339,source_hand='lh',source_start_beat=52,source_end_beat=56,source_pitches=['C','E','G','B'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['C','E','G','B']),
 description='The fourth quaver of each of the first eight bars carries an authored secondary line: E, D, G, F, A, G, E, D. A five-bar transition lets portions of that line emerge from the flowing surface. Its complete eight-pitch sequence then becomes a sixteen-beat song with newly written durations and a different bass route, followed by nine further bars of cantabile. The closing four bars keep the song moving into a voiced C-major arrival instead of reinstating the arpeggios.',
 technical='Keep the opening quavers supple and even, shaping the whole line rather than accenting each contour peak. Allow the transition to reveal longer direction without stopping the pulse. In the cantabile, sustain the broad melody independently of the changing bass and use the written pedal changes to clarify its new harmony. Keep the final climb buoyant and the closing chord lightly voiced.',
 rh='''C5:.5 G4:.5 B4:.5 E5:.5 D5:.5 B4:.5 G4:.5 C5:.5
B4:.5 F4:.5 A4:.5 D5:.5 C5:.5 A4:.5 F4:.5 B4:.5
E5:.5 B4:.5 D5:.5 G5:.5 F#5:.5 D5:.5 B4:.5 E5:.5
D5:.5 A4:.5 C5:.5 F5:.5 E5:.5 C5:.5 A4:.5 D5:.5
F5:.5 C5:.5 E5:.5 A5:.5 G5:.5 E5:.5 C5:.5 F5:.5
E5:.5 B4:.5 D5:.5 G5:.5 F#5:.5 D5:.5 B4:.5 E5:.5
C5:.5 G4:.5 B4:.5 E5:.5 D5:.5 B4:.5 G4:.5 C5:.5
B4:.5 F4:.5 A4:.5 D5:.5 C5:.5 A4:.5 F4:.5 B4:.5
G4:.5 B4:.5 D5:.5 F5:.5 E5:.5 D5:.5 B4:.5 A4:.5
G4:.5 B4:.5 D5:.5 E5:.5 G5:.5 E5:.5 D5:.5 B4:.5
E5:1 D5:1 B4:.5 A4:.5 G4:1
G5:1 F5:1 E5:.5 D5:.5 C5:1
A5:1 G5:1 E5:.5 D5:.5 C5:1
E5:1 D5:1 C5:.5 B4:.5 A4:1
G4:1 B4:.5 D5:.5 E5:1 R:1
E5:2 D5:2
G5:3 F5:1
A5:3 G5:1
E5:2 D5:2
C5:1 E5:.5 G5:.5 F5:2
Eb5:1 D5:.5 C5:.5 Bb4:2
Ab4:1 C5:.5 Eb5:.5 G5:2
F5:1 Eb5:.5 D5:.5 C5:2
Bb4:1 D5:.5 F5:.5 E5:2
D5:1 C5:.5 B4:.5 A4:2
G4:1 B4:.5 D5:.5 F5:2
E5:1 D5:.5 C5:.5 B4:2
A4:1 G4:.5 F#4:.5 G4:1 R:1
C5:1 E5:.5 G5:.5 A5:2
G5:1 F5:.5 E5:.5 D5:2
C5:1 B4:.5 A4:.5 G4:1 E4:1
G4+C5:3 R:1''',
 lh='''C3:1 E3:1 G3:1 B3:1
D3:1 A3:1 C4:1 F3:1
E3:1 B3:1 D4:1 G3:1
F3:1 C4:1 E3:1 A3:1
D3:1 A3:1 C4:1 F3:1
G3:1 B3:1 D4:1 A3:1
A2:1 E3:1 G3:1 C4:1
D3:1 A3:1 C4:1 F3:1
G2:1 D3:1 F3:1 B3:1
C3:1 G3:1 E3:1 B2:1
A2:1 E3:1 G3:2
D3:1 A3:1 C4:2
F3:1 C3:1 E3:2
G2:1 D3:1 F3:2
C3:1 G3:.5 B3:.5 E3:1 R:1
A2+E3:2 F3+A3:2
C3+G3:3 D3+A3:1
F3+A3:3 G3+B3:1
A3+C4:2 Bb2+F3:2
C3+G3:2 F3+A3:2
G2+D3:2 C3+Eb3:2
Ab2+Eb3:2 F3+Ab3:2
Bb2+F3:2 Eb3+G3:2
G2+D3:2 C3+E3:2
D3+A3:2 F3+A3:2
G2+D3:2 G3+B3:2
C3+G3:2 A2+E3:2
D3+A3:2 G3+B3:1 R:1
F3+A3:2 D3+A3:2
G2+D3:2 F3+B3:2
E3+G3:2 D3+F3:1 G2+F3:1
C3+G3:3 R:1''',
 tempos=[62,63,64,63,64,63,62,63,62,61,60,61,62,61,60,62,63,64,63,64,63,62,63,62,61,62,61,60,62,61,60,59],
 phrases=[(1,5),(6,10),(11,15),(16,22),(23,28),(29,32)],lower_phrases=[(1,5),(6,10),(11,15),(16,22),(23,28),(29,32)],
 sections={1:'p',5:'mp',6:'p',11:'p',16:'p',19:'mp',23:'p',29:'mp',31:'pp'},lower_sections={1:'pp',11:'p',16:'pp',23:'p',29:'pp'},
 pedal=sorted([[4*i+.05,4*i+3.8] for i in range(10)]+[[60.05,61.8],[62.05,63.8],[64.05,66.8],[67.05,67.8],[68.05,70.8],[71.05,71.8]]+[[4*i+a+.05,4*i+a+1.8] for i in range(18,27) for a in [0,2]]+[[108.05,109.8],[110.05,110.8],[112.05,113.8],[114.05,115.8],[116.05,117.8],[118.05,119.8],[120.05,121.8],[122.05,122.8],[123.05,123.8],[124.05,126.8]]),
 hairpins=[('crescendo',2,4),('diminuendo',7,10),('crescendo',12,13),('diminuendo',14,15),('crescendo',16,18),('diminuendo',20,22),('crescendo',24,26),('diminuendo',27,28),('diminuendo',29,30)])

p=study(op=395,title='Hazel Palisade',key='Bb',fifths=-2,meter='5/4',bpm=67,parent=247,
 source=dict(source_opus=247,source_hand='rh',source_voice='inner',source_start_beat=84,source_end_beat=94,source_pitches=['D','F','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=10,pitches=['D','F','A','G']),
 description='Four opening dyads belong to the harmonic-root route B-flat, D, F, E. A long outward song then crosses several brighter and darker rooms. On its return the roots run E, F, D, B-flat, now in first-inversion left-hand triads under a newly composed melody; E has changed from minor to major. The reversal concerns these four harmonic roots only. A short continuation keeps moving forward and brings the borrowed E-natural home as B-flat’s raised fourth.',
 technical='Let the opening dyads sing without treating the root route as a pattern to accent. Shape the long outward line through its changes of colour. In bars eighteen to twenty-one, voice the first-inversion left-hand triads softly beneath the new melody; their harmonic roots are independent of the lowest sounding notes. Retain the final E-natural as a quiet colour within the B-flat sonority and release both hands into the written rest.',
 rh='''Bb3+D4:3 D4+F4:2
F4+A4:2 E4+G4:3
C5:1 D5:.5 F5:.5 E5:1 D5:2
Bb4:2 A4:1 G4:.5 F4:1.5
E4:1 G4:1 F4:2 R:1
A4:1 C5:.5 D5:.5 F5:1 E5:2
D5:1 C5:.5 A4:.5 G4:1 F4:2
Eb5:1 D5:.5 C5:.5 Bb4:1 Ab4:2
F5:1 Eb5:.5 Db5:.5 C5:1 Bb4:2
Eb5:1 G5:.5 F5:.5 Eb5:1 D5:2
D5:1 F5:.5 E5:.5 D5:1 B4:2
C5:1 E5:.5 G5:.5 F#5:1 E5:2
C#5:1 E5:.5 G5:.5 F#5:1 E5:2
D5:1 F5:.5 A5:.5 G5:1 F5:2
E5:1 D5:.5 C5:.5 Bb4:1 A4:2
D5:1 F5:.5 E5:.5 D5:1 C#5:2
F#4:1 A4:1 G#4:.5 F#4:.5 E4:1 R:1
E5:2 D5:1 C#5:.5 B4:1.5
C5:1 E5:1 G5:.5 F5:.5 E5:2
A4:2 C5:1 E5:.5 D5:1.5
F4:1 A4:1 C5:.5 Bb4:.5 A4:2
G4:1 Bb4:.5 D5:.5 C5:3
A4:1 C5:.5 E5:.5 D5:3
E5:1 D5:.5 C5:.5 B4:3
A4:1 G4:.5 F4:.5 E4:2 R:1
D4:1 F4:1 A4:.5 G4:2.5
E4:1 G4:1 F4:.5 E4:.5 D4:1 R:1
E4+D5:3 R:2''',
 lh='''Bb2+F3:3 D3+A3:2
F3+C4:2 E3+B3:3
A2:1 E3:1 G3:1 C4:2
Bb2:1 F3:1 A3:1 D3:2
C3+E3:2 F3+A3:2 R:1
F3:1 A3:1 C4:1 G3:2
D3:1 A3:1 C4:1 F3:2
Ab2:1 Eb3:1 G3:1 C4:2
Db3:1 Ab2:1 C3:1 F3:2
C3:1 G3:1 Bb3:1 Eb3:2
G2:1 D3:1 F3:1 B2:2
C3:1 G3:1 B3:1 E3:2
A2:1 E3:1 G3:1 C#3:2
D3:1 A3:1 C4:1 F3:2
Bb2:1 F3:1 A3:1 D3:2
B2:1 F3:1 A3:1 D3:2
B2:1 F#3:1 A3:1 D#3:1 R:1
G#3+B3+E4:5
A3+C4+F4:5
F3+A3+D4:5
D3+F3+Bb3:5
Eb3+Bb3:2 C3+G3:3
F3+A3:2 G3+B3:3
C3+G3:2 A2+E3:3
D3+A3:2 G2+F3:2 R:1
Bb2+F3:2 Eb3+G3:3
C3+E3:2 F3+A3:1 Bb2+F3:1 R:1
Bb2+F3:3 R:2''',
 tempos=[67,68,69,68,66,67,68,69,70,69,68,69,70,69,68,67,66,67,68,69,68,67,68,67,66,67,66,65],
 phrases=[(1,5),(6,11),(12,17),(18,25),(26,28)],lower_phrases=[(1,5),(6,11),(12,17),(18,25),(26,28)],
 sections={1:'p',6:'p',9:'mp',12:'p',14:'mp',18:'p',23:'mp',26:'p',28:'pp'},lower_sections={1:'p',6:'pp',12:'p',18:'pp',26:'pp'},
 pedal=sorted([[.05,2.8],[3.05,4.8],[5.05,6.8],[7.05,9.8],[10.05,14.8],[15.05,19.8],[20.05,21.8],[22.05,23.8]]+[[5*i+.05,5*i+4.8] for i in range(5,16)]+[[80.05,83.8]]+[[5*i+.05,5*i+4.8] for i in range(17,21)]+[[5*i+.05,5*i+1.8] for i in range(21,26)]+[[5*i+2.05,5*i+4.8] for i in [21,22,23,25]]+[[122.05,123.8],[130.05,131.8],[132.05,132.8],[133.05,133.8],[135.05,137.8]]),
 hairpins=[('crescendo',2,3),('diminuendo',4,5),('crescendo',6,8),('diminuendo',10,11),('crescendo',12,13),('diminuendo',15,17),('crescendo',19,22),('diminuendo',24,25)])
p['engraving']['pedal_offset_y']=710

p=study(op=396,title='Dogwood Glimmer',key='bb',fifths=-5,meter='6/4',bpm=76,parent=315,
 source=dict(source_opus=315,source_hand='lh',source_voice='tenor',source_start_beat=78,source_end_beat=82,source_pitches=['Bb','Db','Eb','F'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['Bb','Db','Eb','F']),
 description='A low song and restrained upper replies complete a ten-bar paragraph in B-flat minor, including a shared release. When the same upper third returns above a new G-flat foundation it becomes part of a major-seventh harmony and opens a longer duet. One brief flowing expansion sits inside that second song. The upper voice finishes before a small bass answer settles the larger piece in A-flat major.',
 technical='Give the opening lower song its own breath and keep the upper replies light. Let the first cadence finish completely, observing the shared rest before the new bass changes the meaning of the returning third. Make the longer duet continuous without making it louder by default. At the close, release the upper C before the bass answer begins; the final low third should have its own quiet finish.',
 rh='''R:4 Db4+F4:2
R:3 Eb4+Ab4:3
R:2 F4+Ab4:2 R:2
R:3 G4+Bb4:3
Ab4:2 G4:1 F4:1 Eb4:2
R:2 F4+Ab4:2 R:2
R:3 F4+Ab4:3
R:2 Eb4+Gb4:2 R:2
R:2 Eb4+F4:2 G4+A4:2
Db4+F4:5 R:1
Db4+F4:2 Ab4:.5 Gb4:.5 F4:1 Eb4:2
Ab4:2 Bb4:1 Db5:1 C5:2
Bb4:1 Ab4:1 Gb4:1 F4:1 Eb4:2
F4:1 Ab4:.5 C5:.5 Eb5:2 Db5:2
C5:2 Bb4:1 Ab4:1 Gb4:2
F4:1 Gb4:1 Ab4:1 C5:1 Bb4:2
Eb5:2 Db5:1 C5:1 Bb4:2
Ab4:1 Bb4:.5 C5:.5 Db5:1 Eb5:1 F5:2
Eb5:1 Db5:1 C5:1 Ab4:1 Bb4:2
F5:.5 Eb5:.5 Db5:.5 C5:.5 Bb4:.5 Ab4:.5 Gb4:.5 F4:.5 Eb4:.5 F4:.5 Ab4:.5 C5:.5
Bb4:2 Ab4:1 Gb4:1 F4:2
Eb4:1 F4:1 Ab4:1 C5:1 Bb4:2
G4:1 Bb4:.5 Db5:.5 C5:2 Bb4:2
C5:1 Eb5:1 Db5:1 C5:1 Bb4:2
C5:3 R:3
R:6''',
 lh='''Bb2:1 Db3:1 Eb3:1 F3:1 Ab3:1 F3:1
Eb3:2 F3:1 Ab3:1 C4:2
Db4:2 C4:1 Ab3:1 F3:2
Eb3:2 G3:1 Bb3:1 Db4:2
C4:1 Bb3:1 Ab3:1 G3:1 F3:2
Ab3:2 C4:1 Db4:1 Eb4:2
Db4:2 C4:1 Bb3:1 Ab3:2
Gb3:2 Ab3:1 Bb3:1 C4:2
F3:2 A3:1 C4:1 Eb4:2
Bb2+F3:5 R:1
Gb2+Bb2+Db3:6
Db3:2 Ab3:1 C4:1 F3:2
Eb3:2 Bb2:1 Db3:1 Gb3:2
Ab2:2 Eb3:1 Gb3:1 C3:2
Db3:2 Ab2:1 C3:1 F3:2
Bb2:2 F3:1 Ab3:1 D3:2
Eb3:2 Bb2:1 Db3:1 G3:2
Ab2:2 Eb3:1 G3:1 C4:2
F3:2 C3:1 Eb3:1 Ab3:2
Gb2:2 Db3:1 F3:1 Bb3:2
Eb3:2 Bb2:1 Db3:1 G3:2
Ab2:2 Eb3:1 G3:1 C4:2
Eb3:2 Bb2:1 Db3:1 G3:2
Ab2:2 Eb3:1 G3:1 C4:2
Ab2+Eb3:3 Bb2:1 C3:1 Eb3:1
Ab2+C3:4 R:2''',
 tempos=[76,77,78,77,78,79,78,77,76,75,76,77,78,79,78,79,80,81,80,79,78,79,78,77,76,75],
 phrases=[(5,5),(9,10),(11,17),(18,24)],lower_phrases=[(1,5),(6,10),(11,17),(18,24),(25,26)],
 sections={1:'pp',5:'p',9:'p',10:'pp',11:'p',15:'mp',18:'p',21:'mp',24:'p',25:'pp'},lower_sections={1:'p',6:'mp',10:'pp',11:'p',18:'p',25:'pp'},
 pedal=sorted([[54.05,58.8],[60.05,61.8],[62.05,65.8]]+[[6*i+a+.05,6*i+a+1.8] for i in range(11,24) for a in [0,2,4]]+[[144.05,146.8],[147.05,149.8],[150.05,153.8]]),
 hairpins=[('crescendo',12,14),('diminuendo',16,17),('crescendo',18,20),('diminuendo',22,24)])
p['performance']['lower_entries']=[[0,54],[147,154]]
p['engraving']['pedal_offset_y']=710

p=study(op=397,title='Osier Promenade',key='e',fifths=1,meter='4/4',bpm=68,parent=342,
 source=dict(source_opus=342,source_hand='rh',source_start_beat=40,source_end_beat=44,source_pitches=['E','F#','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['E','F#','A','G']),
 description='Two separate songs suggest different continuations: an upward head and a quieter descending close. A longer connective development explores their intervals and passes through a brief soft semiquaver turn. The final nine-bar melody grafts the complete two-bar head of the first song to the complete three-bar tail of the second, with four newly composed bars joining them. The inherited tail retains its full rhythm and rest while a new bass lets its final E settle above C.',
 technical='Give the two initial songs different breadth while maintaining a walking pulse. Keep the development’s brief semiquaver turn light and close to the keys. In the final song, sustain one continuous melodic intention through the newly written joining phrase; the familiar head and tail should belong to a single line. Voice the changed bass softly and preserve the final rest in tempo.',
 rh='''E5:1 F#5:1 A5:1 G5:1
F#5:1 E5:.5 D5:.5 B4:2
C5:1 D5:.5 E5:.5 G5:2
F#5:1 E5:.5 D5:.5 C5:2
B4:1 D5:.5 F#5:.5 E5:2
D5:1 C5:.5 B4:.5 A4:2
G4:1 A4:.5 B4:.5 E5:1 R:1
C5:2 B4:.5 A4:.5 G4:1
F4:1 A4:.5 C5:.5 B4:2
A4:1 G4:.5 F4:.5 E4:2
G4:1 A4:.5 B4:.5 D5:2
C5:1 B4:.5 A4:.5 G4:1 F#4:1
G4:1 F#4:1 E4:1 R:1
E5:1 G5:.5 A5:.5 G5:2
F5:1 E5:.5 D5:.5 C5:2
Bb4:1 D5:.5 F5:.5 E5:2
Eb5:1 D5:.5 C5:.5 Bb4:2
Ab4:1 C5:.5 Eb5:.5 G5:2
F5:1 Eb5:.5 D5:.5 C5:2
B4:1 D5:.5 F5:.5 E5:2
A4:1 C5:.5 E5:.5 D5:2
G4:1 B4:.5 D5:.5 F#5:2
E5:1 D5:.5 B4:.5 A4:2
G4:1 F#4:.5 E4:.5 D4:1 E4:1
C5:.25 B4:.25 A4:.25 G4:.25 F#4:.25 E4:.25 D4:.25 E4:.25 F#4:.25 A4:.25 B4:.25 D5:.25 E5:.25 G5:.25 F#5:.25 E5:.25
E5:1 F#5:1 A5:1 G5:1
F#5:1 E5:.5 D5:.5 B4:2
C5:1 E5:.5 G5:.5 F5:2
D5:1 C5:.5 Bb4:.5 A4:2
G4:1 Bb4:.5 D5:.5 C5:2
B4:1 A4:.5 G4:.5 F#4:1 E4:1
G4:1 A4:.5 B4:.5 D5:2
C5:1 B4:.5 A4:.5 G4:1 F#4:1
G4:1 F#4:1 E4:1 R:1''',
 lh='''E3:1 B3:.5 D4:.5 G3:2
D3:1 A3:.5 C4:.5 F#3:2
C3:1 G3:.5 B3:.5 E3:2
A2:1 E3:.5 G3:.5 C3:2
B2:1 F#3:.5 A3:.5 D3:2
F3:1 C3:.5 E3:.5 A3:2
B2:1 D#3:.5 F#3:.5 E3:1 R:1
A2+E3:2 C3+G3:2
D3+A3:2 G3+B3:2
C3+G3:2 A2+E3:2
C3+G3:2 D3+A3:2
A2+E3:2 B2+F#3:2
E3+B3:3 R:1
C3:1 G3:.5 B3:.5 E3:2
F3:1 C3:.5 E3:.5 A3:2
Bb2:1 F3:.5 A3:.5 D3:2
Eb3:1 Bb2:.5 D3:.5 G3:2
Ab2:1 Eb3:.5 G3:.5 C4:2
Db3:1 Ab2:.5 C3:.5 F3:2
G2:1 D3:.5 F3:.5 B2:2
A2:1 E3:.5 G3:.5 C3:2
B2:1 F#3:.5 A3:.5 D3:2
E3:1 B2:.5 D3:.5 G3:2
D3:1 A2:.5 C3:.5 F#3:2
C3+G3:2 B2+F#3:2
C3+G3:2 D3+A3:2
G3+B3:2 E3+G3:2
A2+E3:2 D3+A3:2
Bb2+F3:2 F3+A3:2
Eb3+Bb3:2 F3+A3:2
G2+D3:2 G3+B3:2
A2+E3:2 F3+A3:2
G2+D3:2 G3+B3:2
C3+G3:3 R:1''',
 tempos=[68,69,70,69,68,67,66,68,69,68,69,68,66,68,69,70,71,70,69,70,69,70,69,68,68,69,70,71,70,69,68,69,68,67],
 phrases=[(1,7),(8,13),(14,19),(20,25),(26,31),(32,34)],lower_phrases=[(1,7),(8,13),(14,19),(20,25),(26,31),(32,34)],
 sections={1:'p',5:'mp',8:'p',14:'p',17:'mp',20:'p',25:'p',26:'mp',30:'p',33:'pp'},lower_sections={1:'pp',8:'p',14:'pp',20:'p',26:'pp'},
 pedal=sorted([[4*i+.05,4*i+3.8] for i in list(range(6))+list(range(13,24))]+[[24.05,26.8],[48.05,50.8],[132.05,134.8]]+[[4*i+a+.05,4*i+a+1.8] for i in list(range(7,12))+list(range(24,33)) for a in [0,2]]),
 hairpins=[('crescendo',2,4),('diminuendo',5,7),('crescendo',9,11),('diminuendo',12,13),('crescendo',14,16),('diminuendo',17,19),('crescendo',21,23),('diminuendo',24,25),('diminuendo',27,29),('diminuendo',30,32)])
p['engraving']['pedal_offset_y']=710

p=study(op=398,title='Camellia Hearthwater',key='Eb',fifths=-3,meter='7/4',bpm=78,parent=349,
 source=dict(source_opus=349,source_hand='lh',source_start_beat=103,source_end_beat=112,source_pitches=['G','Ab','Eb','C'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=9,pitches=['G','Ab','Eb','C']),
 description='Three unequal songs reach the same G in the same melodic register. A bass-led five-bar phrase finds it as the third of E-flat major; an eight-bar upper song makes it the fifth of C major; a nine-bar dialogue brings it home as the tonic of G major. Their approaches and bass destinations differ, and each cadence has its own complete release. A two-bar afterthought settles on a small sixth drawn from the last arrival.',
 technical='Let the first bass phrase carry the direction beneath the upper replies. Shape the broad seven-beat bars through the written note lengths rather than accenting an extra beat. Each repeated cadential G should be a fresh arrival, voiced above its particular bass. Keep the chordal middle paragraph spacious and the later quaver replies light. Clear pedal before each full rest; allow the closing sixth to release together.',
 rh='''R:2 C5:3 Bb4:2
G4:2 Ab4:1 C5:1 Bb4:3
G4:1 Bb4:1 Eb5:2 D5:1 C5:2
Ab4:2 F4:1 D4:1 F4:3
G4:5 R:2
E5:2 G5:1 A5:1 G5:3
F5:1 E5:1 D5:2 C5:3
B4:2 D5:1 F5:1 E5:3
D5:1 C5:1 Bb4:2 A4:3
C5:2 E5:1 G5:1 F5:3
E5:1 D5:1 C5:2 B4:3
A4:2 F4:1 E4:1 D4:3
G4:5 R:2
B4:2 D5:1 E5:.5 F#5:.5 G5:3
F#5:1 E5:1 D5:2 B4:3
C5:1 E5:.5 G5:.5 A5:2 G5:1 E5:2
D5:2 B4:1 A4:1 G4:3
F4:1 A4:1 C5:2 B4:3
A4:2 G4:1 F#4:1 E4:3
D4:1 G4:.5 B4:.5 D5:2 C5:1 B4:2
A4:2 C5:1 B4:1 F#4:3
G4:5 R:2
B4:2 A4:1 F#4:1 G4:3
G4:5 R:2''',
 lh='''G3:2 Ab2:3 Eb3:2
C3:2 D3:1 F3:1 Eb3:3
Ab2:2 Eb3:2 F3:1 Bb2:2
F3:2 D3:1 Bb2:1 Bb2+Ab3:3
Eb3+Bb3:5 R:2
C3+G3:3 E3+B3:4
D3+A3:2 A2+E3:2 F3+A3:3
G2+D3:3 C3+G3:4
Bb2+F3:2 F3+A3:2 D3+A3:3
A2+E3:3 D3+A3:4
F3+A3:2 G2+D3:2 G3+B3:3
D3:2 A2:1 B2:1 G2+B2+D3:3
C3+E3:5 R:2
G3:2 D3:1 F#3:1 B3:3
E3:1 B2:1 D3:2 G3:3
A3:1 E3:.5 G3:.5 C4:2 B3:1 A3:2
G3:2 D3:1 F3:1 B3:3
D3:1 A2:1 C3:2 G3:3
F#3:2 B2:1 D3:1 G3:3
B2:1 D3:.5 G3:.5 B3:2 A3:1 G3:2
C3:2 E3:1 G3:1 D3+F#3+A3:3
G3+B3+D4:5 R:2
G3:2 D3:1 C3:1 B2:3
B3:5 R:2''',
 tempos=[78,79,80,78,76,78,79,80,79,80,79,78,76,78,79,80,81,80,79,80,78,76,78,77],
 phrases=[(1,5),(6,9),(10,13),(14,18),(19,22),(23,24)],lower_phrases=[(1,5),(14,18),(19,22),(23,24)],
 sections={1:'p',4:'p',5:'pp',6:'p',9:'mp',12:'p',13:'pp',14:'p',17:'mp',20:'p',22:'pp',23:'p',24:'pp'},lower_sections={1:'p',6:'pp',14:'p',19:'p',23:'pp'},
 pedal=sorted([[28.05,32.8],[84.05,88.8],[147.05,151.8],[161.05,165.8]]+[[7*i+a+.05,7*i+b-.2] for i in [5,7,9] for a,b in [(0,3),(3,7)]]+[[7*i+a+.05,7*i+b-.2] for i in [6,8,10] for a,b in [(0,2),(2,4),(4,7)]]+[[77.05,78.8],[81.05,83.8],[91.05,92.8],[93.05,94.8],[95.05,97.8],[98.05,99.8],[100.05,101.8],[102.05,104.8],[105.05,106.8],[107.05,108.8],[109.05,111.8],[112.05,113.8],[114.05,115.8],[116.05,118.8],[119.05,120.8],[121.05,122.8],[123.05,125.8],[126.05,127.8],[128.05,129.8],[130.05,132.8],[133.05,134.8],[135.05,136.8],[137.05,139.8],[140.05,141.8],[142.05,143.8],[144.05,146.8],[154.05,155.8],[158.05,160.8]]),
 hairpins=[('crescendo',1,3),('crescendo',6,8),('diminuendo',10,12),('crescendo',14,16),('diminuendo',17,18),('crescendo',19,20)])
p['performance']['lower_entries']=[[0,28]]
p['engraving']['pedal_offset_y']=710

p=study(op=399,title='Willow Daymark',key='b',fifths=2,meter='4/4',bpm=64,parent=369,
 source=dict(source_opus=369,source_hand='rh',source_start_beat=40,source_end_beat=43,source_pitches=['F#','A','B','D'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['F#','A','B','D']),
 description='At one unchanged quarter-note tempo, a light semiquaver surface gives way to measured triplets, ordinary quavers and a plain upper song. The four quarter-beat positions of one complete bar retain F-sharp, A, B and D in each of those four textures, while their decoration and harmonic surroundings change. Each region has a newly composed continuation. A brief quicker echo renews the motion before a coordinated G-major sixth chord closes the study in tempo.',
 technical='Keep the quarter pulse unchanged through all four written subdivisions. Let the first note of each small group carry the emerging line without a hard accent. Release the fingers freely in the semiquavers and distinguish true triplets from swung quavers. Shape each continuation over its own bass changes; the broad final song needs the same forward intention as the opening. Give the last small echo buoyancy and release the final chord together.',
 rh='''F#4:1 A4:.5 B4:.5 D5:1 E5:.25 D5:.25 B4:.25 A4:.25
F#4:.25 G4:.25 A4:.25 G4:.25 A4:.25 B4:.25 C#5:.25 A4:.25 B4:.25 D5:.25 E5:.25 D5:.25 D5:.25 E5:.25 F#5:.25 E5:.25
B4:.25 D5:.25 F#5:.25 E5:.25 D5:.25 B4:.25 A4:.25 G4:.25 E4:.25 G4:.25 B4:.25 A4:.25 G4:.25 F#4:.25 E4:.25 D4:.25
F#4:.5 A4:.5 D5:.25 C#5:.25 B4:.25 A4:.25 G4:1 F#4:1
E4:.25 G4:.25 A4:.25 B4:.25 D5:.25 C5:.25 B4:.25 A4:.25 G4:1 B4:1
D5:.5 F#5:.5 E5:.5 D5:.5 C#5:1 A4:1
B4:2 F#4:1 R:1
F#4:1/3 A4:1/3 G4:1/3 A4:1/3 C5:1/3 B4:1/3 B4:1/3 D5:1/3 C5:1/3 D5:1/3 F#5:1/3 E5:1/3
G5:1/3 F#5:1/3 E5:1/3 D5:1/3 C5:1/3 B4:1/3 A4:2
C5:1/3 E5:1/3 D5:1/3 F5:1/3 A5:1/3 G5:1/3 E5:1/3 D5:1/3 C5:1/3 B4:1
A4:1/3 C5:1/3 B4:1/3 D5:1/3 F5:1/3 E5:1/3 D5:1 C5:1
B4:1/3 D5:1/3 F#5:1/3 A5:1/3 G5:1/3 F#5:1/3 E5:1/3 D5:1/3 B4:1/3 A4:1/3 G4:1/3 F#4:1/3
E4:1/3 G4:1/3 A4:1/3 B4:1/3 D5:1/3 C5:1/3 A4:1/3 G4:1/3 F#4:1/3 E4:1
G4:1/3 A4:1/3 B4:1/3 A4:1 D4:1 R:1
F#4:.5 A4:.5 A4:.5 C5:.5 B4:.5 D5:.5 D5:.5 F#5:.5
G5:.5 E5:.5 D5:.5 C5:.5 B4:1 G4:1
A4:.5 C5:.5 D5:.5 E5:.5 F5:1 E5:1
D5:.5 B4:.5 A4:.5 G4:.5 F4:1 A4:1
C5:.5 D5:.5 E5:.5 G5:.5 F5:1 D5:1
E5:.5 D5:.5 C5:.5 B4:.5 A4:1 G4:1
F#4:.5 A4:.5 D5:.5 C5:.5 B4:1 A4:1
G4:.5 B4:.5 D5:.5 E5:.5 D5:1 R:1
F#4:1 A4:1 B4:1 D5:1
E5:2 D5:1 B4:1
C5:1 E5:1 G5:2
F5:2 E5:1 D5:1
B4:1 D5:1 F#5:2
E5:1 D5:1 B4:1 A4:1
G4:2 B4:1 D5:1
C5:1 A4:1 F#4:2
G4:.25 B4:.25 D5:.25 E5:.25 F#5:.5 E5:.5 D5:1 B4:1
B4+E5:3 R:1''',
 lh='''B2+F#3:3 A2+E3:1
D3+A3:4
G2+D3:2 E3+G3:2
A2+E3:2 D3+F#3:2
C3+G3:2 E3+G3:2
F#2+C#3:2 A2+E3:2
B2+F#3:3 R:1
E3+G3+D4:4
C3+G3:2 A2+E3:2
F3+A3:2 D3+A3:2
G2+D3:2 C3+G3:2
D3+A3:2 B2+F#3:2
C3+G3:2 A2+E3:2
D3+F#3:3 R:1
D3+F#3:2 G3+B3:2
E3+G3:2 C3+G3:2
F3+A3:2 D3+A3:2
G2+D3:2 D3+F3:2
C3+G3:2 F3+A3:2
A2+E3:2 C3+G3:2
D3+A3:2 G3+B3:2
C3+G3:2 G2+D3:1 R:1
B2+F#3:2 G3+B3:2
C3:1 G3:1 B3:2
A2:1 E3:1 G3:2
D3:1 A3:1 C4:2
G3:1 D3:1 F#3:2
C3:1 G3:1 B3:2
E3:1 B2:1 D3:2
D3:1 A2:1 D3+F#3:2
G3:1 D3:1 F#3:1 D3:1
G3+D4:3 R:1''',
 tempos=[64]*32,
 phrases=[(1,4),(5,7),(8,11),(12,14),(15,18),(19,22),(23,26),(27,30),(31,32)],lower_phrases=[(23,26),(27,30),(31,32)],
 sections={1:'p',5:'mp',7:'p',8:'p',11:'mp',13:'p',15:'p',19:'mp',22:'p',23:'p',27:'mp',30:'p',31:'mp',32:'p'},lower_sections={1:'pp',8:'pp',15:'pp',23:'p',31:'p'},
 tuplet_spans=[dict(hand='rh',start_beat=s,end_beat=s+1,actual=3,normal=2,stem='down') for s in [28,29,30,31,32,33,36,37,38,40,41,44,45,46,47,48,49,50,52]],
 pedal=sorted([[.05,2.8],[3.05,3.8],[4.05,7.8],[24.05,26.8],[28.05,31.8],[52.05,54.8],[84.05,85.8],[86.05,86.8],[124.05,126.8]]+[[4*i+a+.05,4*i+a+1.8] for i in list(range(2,6))+list(range(8,13))+list(range(14,21))+list(range(22,30)) for a in [0,2]]+[[120.05,120.8],[121.05,121.8],[122.05,122.8],[123.05,123.8]]),
 hairpins=[('crescendo',2,4),('diminuendo',5,6),('crescendo',8,10),('diminuendo',11,12),('crescendo',16,18),('diminuendo',19,21),('crescendo',24,26),('diminuendo',27,29)])
p['engraving']['pedal_offset_y']=710

p=study(op=400,title='Velvet Clearing',key='d',fifths=-1,meter='4/4',bpm=56,parent=201,
 source=dict(source_opus=201,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['D','F','E','A']),
 description='The complete opening thought of Fennel Daybreak returns two octaves lower, connecting this last Second Study through Op. 201 and Op. 200 to Velvet Estuary. It becomes a developing bass melody beneath a new upper song. An eleven-bar verse leads to an eight-bar inward duet, a nine-bar changed continuation and four settling bars. The return broadens only the opening D–F–E head; the bass proceeds freely rather than repeating a ground. The upper song finishes first, and a small lower answer closes on F and A before the shared final silence.',
 technical='Give the opening lower melody a singing direction and keep the upper replies warm and unforced. Balance the duet as two continuous lines, using the marked pedal changes to preserve their harmonic movement. Let the broadened lower head retain its identity without making the whole return heavier. Finish the upper D with a complete finger and pedal release before the final bass answer; the last third should be quiet and evenly voiced, with its rest kept in time.',
 rh='''R:2 F4:1 A4:1
G4:1 E4:.5 F4:.5 D4:2
F4:2 E4:1 C4:1
D4:1 F4:.5 A4:.5 G4:2
E4:1 G4:.5 Bb4:.5 A4:2
G4:2 E4:1 F4:1
A4:1 C5:.5 B4:.5 G4:2
F4:1 A4:.5 C5:.5 Bb4:2
G4:2 F4:1 E4:1
D4:1 E4:.5 F4:.5 E4:1 C#4:1
F4+A4:3 R:1
C5:2 B4:1 A4:1
G4:1 Bb4:.5 D5:.5 C5:2
Bb4:1 Ab4:.5 G4:.5 F4:2
Eb4:1 G4:.5 Bb4:.5 C5:2
Ab4:2 G4:1 F4:1
E4:1 G4:.5 Bb4:.5 A4:2
G4:1 F4:.5 E4:.5 D4:2
C#4:1 E4:1 G4:1 R:1
A4:2 G4:1 F4:1
E4:1 G4:.5 A4:.5 Bb4:2
C5:1 E5:.5 D5:.5 B4:2
A4:1 G4:.5 F4:.5 E4:2
G4:2 Bb4:1 A4:1
F4:1 A4:.5 C5:.5 B4:2
G4:1 E4:.5 F4:.5 A4:2
G4:2 E4:1 D4:1
F4:1 E4:.5 D4:.5 C#4:2
D4:1 F4:.5 A4:.5 G4:2
G4:1 F4:1 E4:1 D4:1
R:4
R:4''',
 lh='''D3:1 F3:.5 E3:.5 A2:2
G2:1 A2:.5 C3:.5 F3:2
Eb3:1 F3:1 G3:2
Bb2:1 D3:.5 F3:.5 E3:2
A2:1 C3:.5 E3:.5 F3:2
G3:1 D3:.5 F3:.5 B2:2
C3:1 E3:.5 G3:.5 A3:2
F3:1 C3:.5 Eb3:.5 D3:2
G2:1 Bb2:.5 D3:.5 F3:2
A2:1 E3:.5 G3:.5 C#3:2
D3+A3:3 R:1
F3:1 C3:1 E3:2
Eb3:1 Bb2:.5 D3:.5 G3:2
Ab2:1 Eb3:.5 G3:.5 C4:2
F3:1 C3:.5 Eb3:.5 Ab3:2
Db3:1 Ab2:1 C3:2
G2:1 D3:.5 F3:.5 B2:2
C3:1 G3:.5 Bb3:.5 F3:2
A2:1 C#3:1 E3:1 R:1
D3:2 F3:1 E3:1
C3:1 A2:1 Bb2:2
A2:1 E3:.5 G3:.5 C4:2
D3:1 A2:.5 C3:.5 F3:2
Bb2:1 F3:1 D3:2
G2:1 D3:.5 F3:.5 B2:2
C3:1 G3:.5 Bb3:.5 F3:2
E3:1 Bb2:1 G2:2
A2:1 E3:.5 G3:.5 C#3:2
D3:1 A2:.5 C3:.5 F3:2
G3:1 F3:1 E3:1 A2:1
D3:1 C3:.5 Bb2:.5 A2:2
F3+A3:3 R:1''',
 tempos=[56,57,58,57,56,55,56,57,56,55,54,56,57,58,57,56,57,56,55,56,57,58,57,56,57,56,55,54,55,54,54,53],
 phrases=[(1,6),(7,11),(12,16),(17,19),(20,24),(25,28),(29,30)],lower_phrases=[(1,6),(7,11),(12,16),(17,19),(20,24),(25,28),(29,32)],
 sections={1:'p',5:'mp',8:'p',11:'pp',12:'p',15:'mp',18:'p',20:'p',24:'mp',27:'p',29:'p',30:'pp'},lower_sections={1:'p',7:'p',12:'pp',20:'p',25:'p',29:'pp'},
 pedal=sorted([[4*i+a+.05,4*i+b-.2] for i in list(range(10))+list(range(11,18))+list(range(19,29)) for a,b in [(0,2),(2,4)]]+[[40.05,42.8],[72.05,74.8],[116.05,116.8],[117.05,117.8],[118.05,118.8],[119.05,119.8],[120.05,120.8],[121.05,121.8],[122.05,123.8],[124.05,126.8]]),
 hairpins=[('crescendo',2,4),('diminuendo',5,6),('diminuendo',8,10),('crescendo',12,14),('diminuendo',15,17),('crescendo',20,22),('diminuendo',23,24),('diminuendo',25,26)])
p['performance']['lower_entries']=[[0,40],[76,112],[120,127]]
p['engraving']['pedal_offset_y']=710
