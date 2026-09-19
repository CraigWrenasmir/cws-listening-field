"""Individually authored Resonant Absences, CWS Op. 381–390."""
from weather_common import make_study
PIECES=[]
def study(**kwargs):
    p=make_study(**kwargs);PIECES.append(p);return p

p=study(op=381,title='Ash Stillroom',key='g',fifths=-2,meter='4/4',bpm=53,parent=267,
 source=dict(source_opus=267,source_hand='rh',source_voice='inner',source_start_beat=33,source_end_beat=39,source_pitches=['B','Bb','C','Bb'],transposition_semitones=0),motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=6,pitches=['B','Bb','C','Bb']),
 description='An inner melody continues through the withdrawal of its two outer frames. The exposed B and B-flat first change the meaning of a G bass; later held tones invite new bass routes through E-flat, C minor and a brief flat-side region. Unequal connected spans keep the retained line moving rather than inserting a separate solo episode. It makes one last continuation above the settled bass before all voices release together.',
 technical='Give the interior line its own connected tone, sustaining the marked ties with the fingers while the outer gestures stop. In the dry openings, release both outer voices exactly without lifting the retained inner key. Keep the upper frame lighter than the principal inner song; later pedal spans may colour the harmony but must not substitute for held notes.',
 rh='''G4:.5 R:3.5
D4:1 R:3
F4:1 R:1 Eb4:1 R:1
G4:1 R:3
A4:1 G4:1 R:2
F4:1 R:1 Eb4:1 R:1
D4:2 R:2
G4:1 Bb4:1 R:2
A4:1 R:3
G4:1 F4:1 R:2
Eb4:1 R:3
F4:1 R:1 F4:1 R:1
A4:1 C5:1 R:2
Bb4:1 R:3
Ab4:1 G4:1 R:2
F4:1 R:3
Ab4:1 C5:1 R:2
Bb4:1 R:1 Ab4:1 R:1
Bb4:1 R:3
F4:1 A4:1 R:2
G4:2 R:2
Bb4:1 A4:1 R:2
G4:1 R:3
F4:1 R:1 Eb4:1 R:1
G4:1 R:3
A4:1 G4:1 R:2
F4:1 A4:1 G4:1 F4:1
G4:3 R:1''',
 rh_inner='''B3:1 Bb3:2 C4:1~
C4:1 Bb3:1 A3:2
Bb3:2 C4:1 D4:1~
D4:2 C4:1 Bb3:1
C4:1 D4:1 E4:2
D4:2 C4:1 Bb3:1
A3:3 R:1
Eb4:1 F4:1 G4:2~
G4:2 F4:1 Eb4:1
D4:2 C4:2
Bb3:1 C4:1 D4:2~
D4:1 C4:1 Bb3:1 A3:1
F4:1 G4:1 A4:2~
A4:2 G4:1 F4:1
Eb4:2 Db4:1 C4:1
Db4:1 Eb4:1 F4:2~
F4:2 Eb4:1 Db4:1
Eb4:2 F4:1 G4:1~
G4:1 F4:1 Eb4:2
D4:1 E4:1 F4:2
Eb4:3 R:1
G4:1 F4:1 Eb4:2~
Eb4:2 D4:1 C4:1
Bb3:2 C4:1 D4:1~
D4:2 C4:1 Bb3:1
C4:1 D4:1 E4:2
D4:2 C4:1 D4:1
Eb4:1 D4:2 R:1''',
 lh='''G2+D3:.5 R:3.5
Eb3+G3:1 R:3
G2:1 D3:1 R:2
Bb2+F3:1 R:3
A2+E3:1 R:1 G2:1 R:1
F3:1 A3:1 R:2
D3+F#3:2 R:2
C3+G3:1 R:3
Eb3+Bb3:1 R:3
F3:1 A3:1 R:2
G2+D3:1 R:3
D3+F#3:1 R:1 A2:1 R:1
D3+A3:1 R:3
Bb2+F3:1 R:3
C3:1 Eb3:1 R:2
Db3+Ab3:1 R:3
Bb2+F3:1 R:3
Eb3+Bb3:1 R:1 C3:1 R:1
C3+G3:1 R:3
D3:1 A3:1 R:2
Eb3+Bb3:2 R:2
C3:1 G3:1 R:2
Eb3+Bb3:1 R:3
G2:1 D3:1 R:2
Bb2+F3:1 R:3
A2+E3:1 R:1 C3:1 R:1
D3:1 A3:1 F#3:1 D3:1
G2+Bb2:3 R:1''',
 tempos=[53,54,55,54,55,54,52,53,54,55,54,52,53,54,55,54,55,54,53,52,51,52,53,54,53,52,53,52],
 phrases=[(1,7),(8,12),(13,21),(22,28)],lower_phrases=[(1,7),(8,12),(13,21),(22,28)],
 sections={1:'pp',8:'pp',13:'p',22:'pp'},lower_sections={1:'pp',8:'pp',13:'p',22:'pp'},
 voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=3) for a,b in [(0,27),(28,48),(48,83),(84,111)]],
 page_starts=[7,13,19,25],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=710),
 pedal=[[12.05,12.8],[28.05,28.8],[32.05,32.8],[48.05,48.8],[52.05,52.8],[60.05,60.8],[64.05,64.8],[72.05,72.8],[88.05,88.8],[96.05,96.8],[108.05,110.8]],hairpins=[])
p['performance']['inner_entries']=[[0,111]]
p['performance']['gate']=1
p['performance']['phrase_arcs']=[[0,28,0],[28,48,0],[48,84,0],[84,112,0]]

p=study(op=382,title='Laurel Airwell',key='d',fifths=-1,meter='3/2',bpm=70,parent=256,
 source=dict(source_opus=256,source_hand='rh',source_voice='inner',source_start_beat=5.5,source_end_beat=10,source_pitches=['G','A','G','Bb'],transposition_semitones=0),motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4.5,pitches=['G','A','G','Bb']),
 description='A small melody opens into chorale variations governed by release order. Four sonorities first lose their upper note, then their inner note, leaving the bass. Later the same pitches and simultaneous attacks lose the bass first, leaving a different pair and finally the upper note alone. A longer final variation lets these remaining intervals guide a new harmonic route, ending with a coordinated chord release.',
 technical='Play the release variations without pedal. Sound the three notes together, then lift each finger at its own written rest while keeping the others held. Preserve the changing interval as a musical line rather than demonstrating the releases with accents. Keep the last shared release exactly placed and allow the complete final rest.',
 rh='''G4:.5 A4:2 G4:1 Bb4:1 C5:1.5
D5:2 C5:1 Bb4:1 A4:2
F5:2 E5:1 D5:1 C5:2
A4:1 C5:1 Bb4:2 G4:2
A4:2 G4:2 F4:1 R:1
C5:2 R:4
D5:2 R:4
E5:2 R:4
F5:2 R:4
B4:3 R:3
E4:2 R:4
A4:3 R:3
C5:6
D5:6
E5:6
F5:6
G4:3 R:3
C5:4 R:2
Bb4:3 R:3
A4:4 R:2
G4:3 R:3
F4:2 R:4
E4:4 R:2
F4:5 R:1''',
 rh_inner='''E4:3 F4:3
G4:3 F4:3
Bb4:3 A4:3
F4:3 E4:3
C4:3 D4:2 R:1
A4:4 R:2
B4:4 R:2
C5:4 R:2
D5:4 R:2
G4:5 R:1
C#4:4 R:2
F4:5 R:1
A4:4 R:2
B4:4 R:2
C5:4 R:2
D5:4 R:2
E4:4.5 R:1.5
A4:2 R:4
G4:5 R:1
F4:2 R:4
Eb4:5 R:1
D4:4 R:2
C#4:2 R:4
D4:5 R:1''',
 lh='''C3:3 D3:3
G2:3 F3:3
Bb2:3 C3:3
F3:3 C3:3
F3:2 E3:2 D3:1 R:1
F3:6
G3:6
A3:6
Bb3:6
E3:6
A2:6
D3:6
F3:2 R:4
G3:2 R:4
A3:2 R:4
Bb3:2 R:4
C3:6
F3:6
Eb3:6
D3:6
C3:6
Bb2:6
A2:6
D3:5 R:1''',
 tempos=[70,71,72,71,69,70,71,72,71,70,69,68,70,71,72,71,70,71,72,71,70,69,68,68],
 phrases=[(1,5),(6,12),(13,16),(17,24)],lower_phrases=[(1,5),(6,12),(13,16),(17,24)],
 sections={1:'p',6:'p',13:'p',17:'p',21:'pp'},lower_sections={1:'pp',6:'p',13:'p',17:'pp'},
 voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=2) for a,b in [(0,29),(30,71),(72,94),(96,116),(120,143)]],
 page_starts=[7,13,19],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=610),
 pedal=[],hairpins=[])
p['performance']['gate']=1
p['performance']['phrase_arcs']=[[0,30,2],[30,72,2],[72,96,2],[96,144,2]]

p=study(op=383,title='Tamarisk Aperture',key='e',fifths=1,meter='5/4',bpm=69,parent=261,
 source=dict(source_opus=261,source_hand='lh',source_start_beat=64,source_end_beat=65.5,source_pitches=['E','G','A','B'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=3,pitches=['E','G','A','B']),
 description='An established five-beat bass cell returns with its minor third omitted, then with its flat sixth omitted. The missing attacks keep their full temporal places: the melody can briefly admit G-sharp and later C-sharp without the former bass member sounding beneath them. Longer newly composed routes lead into a freely sustained song. A compressed return restores the complete cell once before the bass stops and the upper line finishes alone.',
 technical='Maintain the complete five-beat cell through its internal rests; do not displace the later attacks to fill a gap. Keep the opening and omission passages free of pedal so the absent bass members remain absent. Let the long upper phrase breathe across the cycle, and sustain its tied arrival independently of the moving bass.',
 rh='''E5:3 D5:1 C5:1
B4:2 A4:1 G4:2
A4:1 B4:1 D5:2 C5:1
B4:3 A4:1 R:1
G#4:1 B4:1 E5:2 D5:1
C5:2 B4:1 A4:2
G4:1 A4:1 C5:2 B4:1
A4:2 G4:1 F#4:2
E4:1 G4:1 B4:2 A4:1
D5:3 E5:2~
E5:1 F#5:1 G5:1 F#5:1 E5:1
B4:1 C#5:3 B4:1
A4:2 G4:1 F#4:2
E4:1 F#4:1 A4:2 C#5:1
B4:2 A4:1 G4:2
F#4:1 A4:1 C5:2 B4:1
G4:3 F#4:1 R:1
E4:1 G4:1 B4:3~
B4:1 C5:1 D5:1 E5:2
F#5:2 E5:1 D5:2
C5:1 B4:1 A4:3
G4:2 B4:1 D5:2
C5:2 B4:1 A4:2
G4:1 A4:1 B4:1 C#5:2
D5:2 C#5:1 B4:2
A4:2 G4:1 F#4:1 R:1
E5:3 D5:1 C5:1
B4:2 A4:1 G4:2
F#4:1 A4:1 B4:2 R:1
G4:1 B4:1 E5:2 D5:1
C5:1 B4:1 A4:1 G4:2
F#4:1 G4:1 E4:2 R:1''',
 lh='''E3:.5 G3:.5 A3:1 B3:1 C4:1 B3:1
D3:.5 F#3:.5 G3:1 A3:1 B3:1 A3:1
C3:.5 E3:.5 F#3:1 G3:1 A3:1 G3:1
B2:.5 D3:.5 E3:1 F#3:1 A3:1 R:1
E3:.5 R:.5 A3:1 B3:1 C4:1 B3:1
A2:.5 C3:.5 E3:1 G3:1 B3:1 G3:1
C3:.5 R:.5 F3:1 G3:1 A3:1 G3:1
D3:.5 F#3:.5 G3:1 A3:1 C4:1 A3:1
E3:.5 R:.5 A3:1 B3:1 D4:1 B3:1
G3:.5 B3:.5 C4:1 D4:1 F#4:1 D4:1
C3:.5 E3:.5 G3:1 B3:1 A3:1 G3:1
E3:.5 G3:.5 A3:1 B3:1 R:1 B3:1
D3:.5 F#3:.5 G3:1 A3:1 R:1 A3:1
C#3:.5 E3:.5 F#3:1 G3:1 R:1 A3:1
B2:.5 D3:.5 E3:1 F#3:1 R:1 F#3:1
A2:.5 C3:.5 D3:1 E3:1 G3:1 E3:1
B2:.5 D3:.5 F#3:1 A3:1 B3:1 R:1
E3:2 B3:1 G3:2
C3:2 G3:1 B3:2
D3:2 A3:1 C4:2
F3:2 C4:1 A3:2
G3:2 D4:1 B3:2
E3:2 B3:1 G3:2
A2:2 E3:1 G3:2
D3:2 A3:1 C4:2
B2:2 F#3:1 A3:1 R:1
E3:.5 G3:.5 A3:1 B3:1 C4:1 B3:1
D3:.5 F#3:.5 G3:1 A3:1 R:1 A3:1
B2:.5 D3:.5 E3:1 F#3:2 R:1
R:5
R:5
R:5''',
 tempos=[69,70,71,69,70,71,72,71,70,71,70,69,70,71,70,69,68,69,70,71,70,69,70,71,70,68,69,70,68,69,68,67],
 phrases=[(1,4),(5,11),(12,17),(18,26),(27,29),(30,32)],lower_phrases=[(1,4),(5,11),(12,17),(18,26),(27,29)],
 sections={1:'p',5:'p',9:'mp',12:'p',18:'p',22:'mp',27:'p',30:'pp'},lower_sections={1:'p',5:'p',12:'p',18:'pp',27:'p'},
 pedal=sorted([[i*5+.05,i*5+4.8] for i in range(17,25)]+[[125.05,128.8],[145.05,149.8],[150.05,154.8],[155.05,158.8]]),
 hairpins=[('crescendo',6,8),('diminuendo',9,11),('crescendo',13,15),('diminuendo',16,17),('crescendo',19,21),('diminuendo',23,26)])

p=study(op=384,title='Bilberry Echo',key='C',fifths=0,meter='6/8',bpm=54,parent=251,
 source=dict(source_opus=251,source_hand='rh',source_start_beat=4,source_end_beat=9.5,source_pitches=['C','E','G','F'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=5.5,pitches=['C','E','G','F']),
 description='The opening phrase and its complete two-hand gap are first dry, then return unchanged with the gap carried by pedal resonance. The held G distinguishes finger sustain from the following released-key resonance. A longer resonant region chooses harmonies compatible with its lingering notes, including a brief flat-side opening. A shorter dry return retains the changed route. At the end both hands release before the final pedal lift, with no further attack.',
 technical='Keep the dry passages free of pedal. In the marked spans catch the still-held notes before the fingers release; preserve the written rests even while the pedal carries their sound. Clear each marked lift completely before the next harmony. At the end release both hands after the quarter note, then lift the pedal at its written endpoint and retain the remaining rest.',
 rh='''C5:1.5 E5:.5 G5:1~
G5:2 F5:.5 R:.5
E5:1 D5:1 C5:1
A4:2 R:1
D5:1.5 F5:.5 E5:1
C5:2 R:1
B4:1 D5:1 G4:1
C5:1 R:2
C5:1.5 E5:.5 G5:1~
G5:2 F5:.5 R:.5
E5:1 D5:1 C5:1
A4:2 R:1
Bb4:1 D5:1 F5:1
E5:1 D5:1 R:1
C5:1.5 Eb5:.5 G5:1~
G5:1 F5:1 R:1
F5:1 Ab5:.5 G5:1.5
Eb5:2 R:1
D5:1 F5:1 A5:1
G5:1 F5:1 R:1
E5:1 G5:.5 F5:1.5
D5:2 R:1
C5:1 E5:1 G5:1
F5:1 E5:1 D5:1
C5:2 R:1
C5:1.5 E5:.5 G5:1~
G5:2 F5:.5 R:.5
E5:1 D5:1 B4:1
C5:2 R:1
A4:1 C5:.5 D5:1.5
E5:2 R:1
D5:1 B4:1 G4:1
A4:2 R:1
G4:1 C5:1 E5:1
D5:2 R:1
C5:1 R:2''',
 lh='''C3:1.5 G3:.5 B3:1~
B3:2 A3:.5 R:.5
A3:1 G3:1 E3:1
F3:2 R:1
G3:1.5 B3:.5 C4:1
A3:2 R:1
G3:1 F3:1 D3:1
C3:1 R:2
C3:1.5 G3:.5 B3:1~
B3:2 A3:.5 R:.5
A3:1 G3:1 E3:1
F3:2 R:1
Eb3:1 G3:1 Bb3:1
C4:1 B3:1 R:1
C3:1.5 Eb3:.5 G3:1~
G3:1 F3:1 R:1
Db3:1 F3:.5 Ab3:1.5
Bb3:2 R:1
Bb2:1 D3:1 F3:1
G3:1 A3:1 R:1
C4:1 E4:.5 A3:1.5
G3:2 R:1
C3:1 G3:1 B3:1
A3:1 G3:1 F3:1
E3:2 R:1
C3:1.5 G3:.5 B3:1~
B3:2 A3:.5 R:.5
A3:1 G3:1 D3:1
E3:2 R:1
F3:1 A3:.5 B3:1.5
C4:2 R:1
G3:1 F3:1 D3:1
F3:2 R:1
E3:1 G3:1 C4:1
G3:2 R:1
C3+G3:1 R:2''',
 tempos=[54,55,56,54,55,54,53,52,54,55,56,54,55,54,53,52,53,54,55,54,53,52,53,54,52,53,54,55,53,54,53,52,53,54,53,52],
 phrases=[(1,4),(5,8),(9,12),(13,18),(19,25),(26,29),(30,36)],lower_phrases=[(1,4),(5,8),(9,12),(13,18),(19,25),(26,29),(30,36)],
 sections={1:'p',5:'mp',9:'p',13:'mp',15:'p',19:'mp',23:'p',26:'pp',30:'p',36:'pp'},lower_sections={1:'pp',9:'p',15:'pp',19:'p',26:'pp'},
 pedal=[[27.05,30],[33.05,35.8],[36.05,38.8],[39.05,42],[45.05,47.8],[48.05,50.8],[51.05,54],[54.05,56.8],[57.05,59.8],[60.05,62.8],[63.05,66],[66.05,68.8],[69.05,71.8],[72.05,74.8],[105.05,107.5]],
 pedal_resonance_windows=[[29.5,30],[35,35.8],[41,42],[47,47.8],[53,54],[59,59.8],[65,66],[74,74.8],[106,107.5]],
 engraving=dict(spacing_system=19,spacing_staff=19,pedal_offset_y=710),
 hairpins=[('crescendo',2,3),('diminuendo',5,8),('crescendo',10,12),('diminuendo',16,18),('crescendo',20,22),('diminuendo',23,25),('diminuendo',32,35)])

p=study(op=385,title='Rowan Hollow',key='g',fifths=-2,meter='4/4',bpm=62,parent=260,
 source=dict(source_opus=260,source_hand='rh',source_voice='inner',source_start_beat=56,source_end_beat=63,source_pitches=['G','F','D','C'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=7,pitches=['G','F','D','C']),
 description='A two-bar phrase head opens a complete eight-bar sentence. After a long contrasting song, the head’s full eight-beat place is left silent in both hands; the original six-bar upper continuation then resumes at its appointed time over new harmony. The closing head is unaccompanied and has no continuation. These complementary omissions give the same remembered material two different formal meanings.',
 technical='Retain the full two silent bars before the return, with fingers released and pedal up. Imagine the absent opening without shortening its time, then allow the continuation to enter naturally. In the last two bars let the exposed head end plainly; do not supply an extra answer or prolong the final written rest.',
 rh='''G4:1 F4:2 D4:1~
D4:1 C4:2 R:1
Eb4:1 F4:1 G4:2
Bb4:2 A4:1 G4:1
F4:1 A4:1 C5:2
Bb4:1 A4:1 G4:1 F4:1
Eb4:1 G4:1 A4:1 F#4:1
G4:3 R:1
D5:2 F5:1 Eb5:1
C5:1 D5:1 F5:2
Eb5:2 D5:1 C5:1
Bb4:1 D5:1 F5:2
E5:1 D5:1 C5:2
A4:3 R:1
C5:1 Eb5:1 G5:2
F5:2 Eb5:1 D5:1
Db5:1 F5:1 Ab5:2
G5:2 F5:1 Eb5:1
D5:1 F5:1 A5:2
G5:2 F5:1 Eb5:1
C5:1 D5:1 F5:2
D5:4
R:4
R:4
Eb4:1 F4:1 G4:2
Bb4:2 A4:1 G4:1
F4:1 A4:1 C5:2
Bb4:1 A4:1 G4:1 F4:1
Eb4:1 G4:1 A4:1 F#4:1
G4:3 R:1
G4:1 F4:2 D4:1~
D4:1 C4:2 R:1''',
 lh='''G2:1 D3:2 Bb2:1~
Bb2:1 F3:2 R:1
C3:1 G3:1 Bb3:2
Eb3:2 G3:1 Bb3:1
F3:1 C4:1 A3:2
Bb2:1 F3:1 D3:1 A2:1
C3:1 Eb3:1 D3:1 A2:1
G2:1 D3:1 Bb2:1 R:1
Bb2:1 F3:1 A3:2
F3:1 A3:1 C4:2
Ab2:1 Eb3:1 G3:2
G2:1 D3:1 F3:2
C3:1 G3:1 Bb3:2
F3:3 R:1
Ab2:1 Eb3:1 G3:2
Bb2:1 F3:1 Ab3:2
Db3:1 Ab3:1 C4:2
C3:1 G3:1 Bb3:2
Bb2:1 F3:1 A3:2
Eb3:1 Bb3:1 G3:2
C3:1 G3:1 A3:2
G3+B3:4
R:4
R:4
Ab2:1 Eb3:1 G3:2
G2:1 D3:1 F3:2
D3:1 A3:1 F3:2
Eb3:1 G3:1 Bb3:1 A3:1
C3:1 E3:1 D3:1 A2:1
G2:1 D3:1 B2:1 R:1
R:4
R:4''',
 tempos=[62,63,64,65,64,63,62,61,62,63,64,65,64,62,63,64,65,64,63,64,63,62,62,62,62,63,64,63,62,61,62,61],
 phrases=[(1,8),(9,14),(15,22),(25,30),(31,32)],lower_phrases=[(1,8),(9,14),(15,22),(25,30)],
 sections={1:'p',5:'mp',9:'p',13:'mp',15:'p',19:'mp',25:'p',31:'pp'},lower_sections={1:'pp',9:'p',15:'pp',25:'pp'},
 pedal=sorted([[i*4+.05,i*4+3.8] for i in list(range(2,7))+list(range(8,13))+list(range(14,22))+list(range(24,29))+[0]]+[[i*4+.05,i*4+2.8] for i in [1,7,13,29]]),
 hairpins=[('crescendo',2,4),('diminuendo',5,8),('crescendo',10,12),('diminuendo',13,14),('crescendo',16,18),('diminuendo',19,22),('diminuendo',27,30)])
p['performance']['gate']=1
# Clear the borrowed E-flat before the new bass E-natural, then again before F-sharp.
p['pedal_spans']=sorted([span for span in p['pedal_spans'] if span[0]!=112.05]+[[112.05,112.8],[113.05,114.8]])

p=study(op=386,title='Larch Dormer',key='Db',fifths=-5,meter='12/8',bpm=84,parent=264,
 source=dict(source_opus=264,source_hand='lh',source_start_beat=10,source_end_beat=15,source_pitches=['Db','F','Eb','Ab'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=5,pitches=['Db','F','Eb','Ab']),
 description='Two outer lines leave the middle register entirely unused through the first eighteen bars. Two cadential gestures contain only C and G, withholding a third that would settle their quality. After a complete breath, a new middle-register E-flat supplies that member in a C-minor sonority. The closing song moves into the formerly empty space and ends there on a quiet third, without recovering a deep bass.',
 technical='Let the outer lines remain intimate despite their separation in register. Prepare the move into the middle during the full written rest; make the new E-flat audible without an accent. Shape the closing duet as one connected song, keeping the two hands distinct at their adjacent-key handovers and clearing changed chord members with the written pedal lifts.',
 rh='''Ab5:3 F5:2 Eb5:1
Db5:2 Eb5:1 F5:3
Ab5:1.5 Gb5:.5 F5:1 Eb5:3
Db5:3 C5:2 R:1
Eb5:2 G5:1 Bb5:3
Ab5:3 G5:1 F5:2
Eb5:2 D5:1 C5:3
G5:3 C5:2 R:1
Db5:2 F5:1 Ab5:3
Gb5:2 F5:1 Eb5:3
Db5:1 Eb5:1 F5:1 Ab5:3
G5:3 F5:2 R:1
Eb5:2 D5:1 C5:3
G5:3 C5:2 R:1
Eb5:1 G5:1 Bb5:1 Ab5:3
Gb5:2 F5:1 Eb5:3
D5:1 F5:1 Ab5:1 G5:3
G5:3 R:3
G5:3 C5:3
Bb4:2 Ab4:1 G4:3
F4:1 Ab4:1 C5:1 Bb4:3
G4:2 F4:1 Eb4:3
D4:1 F4:1 Ab4:1 G4:3
C5:2 Bb4:1 Ab4:3
G4:2 Bb4:1 D5:3
C5:2 Bb4:1 G4:3
Ab4:2 G4:1 F4:3
Eb4:1 G4:1 Bb4:1 Ab4:3
G4:2 F4:1 D4:3
G4:3 R:3''',
 lh='''Db3:1 F3:.5 Eb3:.5 Ab2:3 Bb2:1
F3:2 Ab2:1 Db3:3
Gb2:2 Db3:1 F3:3
Ab2:2 Eb3:1 Gb3:2 R:1
C3:2 G3:1 Bb2:3
F3:2 C3:1 Eb3:3
G2:2 D3:1 F3:3
C3+G3:5 R:1
Bb2:2 F3:1 Ab2:3
Eb3:2 Bb2:1 Db3:3
Ab2:2 Eb3:1 Gb3:3
D3:2 A2:1 C3:2 R:1
G2:2 D3:1 F3:3
C3+G3:5 R:1
Ab2:2 Eb3:1 G3:3
Db3:2 Ab2:1 C3:3
D3:2 Ab2:1 F3:3
G3:3 R:3
C4+Eb4:6
C4:2 Eb4:1 F4:3
Db4:3 Eb4:3
Bb3:2 D4:1 C4:3
Bb3:1 A3:1 F#3:1 G3:3
Ab3:2 C4:1 Eb4:3
G3:2 Bb3:1 D4:3
C4:2 Eb4:1 F4:3
Db4:2 Eb4:1 C4:3
C4:1 Eb4:1 G3:1 F3:3
Eb4:2 D4:1 Bb3:3
Eb4:3 R:3''',
 tempos=[84,85,86,84,85,86,85,83,84,85,86,84,85,83,84,85,84,82,83,84,85,84,85,86,85,84,83,84,83,82],
 phrases=[(1,4),(5,8),(9,14),(15,18),(19,24),(25,30)],lower_phrases=[(1,4),(5,8),(9,14),(15,18),(19,24),(25,30)],
 sections={1:'p',5:'mp',9:'p',15:'mp',19:'p',25:'p',29:'pp'},lower_sections={1:'pp',9:'pp',15:'p',19:'p',25:'pp'},
 pedal=sorted([[i*6+.05,i*6+5.8] for i in range(30) if i not in [3,7,11,13,17,22,28,29]]+[[i*6+.05,i*6+4.8] for i in [3,7,11,13]]+[[102.05,104.8],[132.05,134.8],[135.05,137.8],[168.05,169.8],[170.05,170.8],[171.05,173.8],[174.05,176.8]]),
 hairpins=[('crescendo',2,3),('diminuendo',6,8),('crescendo',10,12),('diminuendo',13,14),('crescendo',20,22),('diminuendo',23,24),('diminuendo',26,28)])

p=study(op=387,title='Osier Courtyard',key='e',fifths=1,meter='7/4',bpm=92,parent=266,
 source=dict(source_opus=266,source_hand='rh',source_start_beat=27,source_end_beat=35,source_pitches=['B','C','D','E'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=8,pitches=['B','C','D','E']),
 description='Two complete melodic lines take turns ending first. Their cutoffs gradually move farther apart, leaving the last few notes of one sentence to answer the empty space of the other. A single shared breath interrupts the eighteenth bar. The remaining ten bars sustain a longer duet, whose two voices finally arrive and release together.',
 technical='Sing both lines through the uneven seven-beat spans. Keep every early cutoff exact with the fingers: the unpedalled releases form the counterpoint. Let the last note of the surviving line continue naturally rather than accenting the other hand leaving. Sustain the later duet with lighter bass tone, then release the final fifth together.',
 rh='''B4:4 C5:1 D5:2
E5:1 G5:2 F#5:1 E5:2 R:1
D5:2 C5:1 B4:2 A4:1 R:1
G4:3 F#4:2 E4:2
B4:3 D5:1 F#5:1 R:2
E5:1 F#5:1 G5:3 F#5:2
E5:2 D5:1 C5:2 B4:2
A4:2 C5:1 B4:2 R:2
G4:1 A4:1 B4:1 D5:4
C5:2 B4:1 A4:2 R:2
G4:2 B4:1 D5:2 R:2
E5:1 F#5:1 G5:2 A5:1 G5:2
F#5:2 E5:1 D5:2 R:2
C5:1 D5:1 E5:3 G5:2
F5:2 E5:1 D5:1 R:3
C5:1 B4:1 A4:2 G4:3
F#4:1 A4:1 C5:1 B4:1 R:3
B4:2 E5:2 R:3
F#5:2 E5:1 D5:1 B4:3
C5:2 D5:1 E5:4
G5:3 F#5:1 E5:2 D5:1
C5:2 B4:1 A4:4
D5:1 E5:1 F#5:2 G5:3
F#5:2 E5:1 D5:2 C5:2
B4:2 D5:1 F#5:1 E5:3
D5:2 C5:1 B4:2 A4:2
G4:3 A4:1 F#4:1 E4:2
B4:5 R:2''',
 lh='''E3:2 G3:2 B3:2 R:1
A3:1 C4:2 B3:2 G3:2
F3:2 A3:1 C4:2 B3:2
E3:2 B3:2 G3:2 R:1
G3:2 B3:1 D4:2 F#4:2
C4:2 G3:1 E3:2 R:2
A2:2 E3:1 G3:2 R:2
F3:2 A3:1 C4:2 E4:2
G3:1 B3:1 D4:1 F4:2 R:2
A3:1 G3:1 E3:1 D3:2 C3:2
E3:2 G3:1 B3:2 D4:2
C4:2 B3:1 A3:2 R:2
B2:2 F#3:1 A3:2 C4:2
A3:2 G3:1 E3:2 R:2
D3:1 F3:1 A3:2 C4:3
F3:2 E3:1 C3:1 R:3
B2:1 D3:1 F#3:1 A3:2 D4:2
E3:2 G3:2 R:3
B3:1 A3:1 G3:2 E3:3
A2:2 E3:2 G3:1 B3:2
C4:2 B3:1 A3:2 G3:2
F3:2 A3:1 C4:2 E4:2
B3:1 A3:1 G3:2 E3:3
A3:2 C4:1 B3:1 G3:3
G3:2 B3:1 D4:2 C4:2
F3:2 A3:1 C4:2 B3:2
E3:2 G3:1 B3:1 A3:1 G3:2
E3:5 R:2''',
 tempos=[92,93,94,92,93,94,93,92,91,90,92,94,95,94,92,91,90,89,91,92,93,94,93,92,91,90,89,89],
 phrases=[(1,4),(5,10),(11,18),(19,28)],lower_phrases=[(1,4),(5,10),(11,18),(19,28)],
 sections={1:'p',5:'mp',11:'p',14:'mp',19:'p',23:'mp',27:'pp'},lower_sections={1:'p',5:'p',11:'mp',19:'p',27:'pp'},
 hairpins=[('crescendo',6,7),('diminuendo',9,10),('crescendo',12,14),('diminuendo',15,18),('crescendo',20,23),('diminuendo',24,28)])
p['performance']['gate']=1

p=study(op=388,title='Mallow Afterrain',key='c',fifths=-3,meter='5/4',bpm=66,parent=258,
 source=dict(source_opus=258,source_hand='lh',source_voice='tenor',source_start_beat=120,source_end_beat=126,source_pitches=['C','Eb','D','F'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=6,pitches=['C','Eb','D','F']),
 description='A low song carries the opening while an inner F learns to move down to E-flat above a C-minor foundation. In the longer second panel the same F stops instead: C, E-flat and G are already sounding and remain after its withdrawal. Their next bass destination grows into a new song. At the last return that quiet surviving harmony is the ending, and the inner voice never supplies its former resolution.',
 technical='Balance the three voices without blending their release times. In bars four and fourteen, keep the outer C-minor frame equally sustained so the difference between an inner step and an inner withdrawal is perceptible. Use finger legato throughout the dry score, preserving every held partner when the F releases. The last inner rest is the cadence; do not add an unmarked E-flat.',
 rh='''G4:3 Ab4:1 Bb4:1
C5:2 Bb4:1 Ab4:2
G4:2 F4:1 Ab4:1 G4:1
G4:5
Bb4:2 C5:1 D5:2
Eb5:2 D5:1 C5:2
Bb4:1 Ab4:1 G4:2 F4:1
G4:3 Ab4:1 Bb4:1
C5:2 D5:1 Eb5:2
D5:2 C5:1 Bb4:2
Ab4:1 G4:1 F4:1 G4:2
G4:4 R:1
C5:2 Bb4:1 Ab4:1 G4:1
G4:5
Ab4:2 Bb4:1 C5:2
D5:2 Eb5:1 D5:2
C5:1 Bb4:1 Ab4:1 G4:2
F4:1 G4:1 Ab4:2 Bb4:1
C5:3 Bb4:1 Ab4:1
G4:2 Bb4:1 D5:2
C5:2 Bb4:1 Ab4:2
G4:1 Ab4:1 Bb4:1 C5:2
D5:2 C5:1 Bb4:2
Ab4:2 G4:1 F4:2
G4:1 Bb4:1 C5:1 Ab4:2
G4:2 F4:1 G4:2
Ab4:1 Bb4:1 Ab4:1 G4:2
G4:5''',
 rh_inner='''Eb4:3 F4:2
G4:2 F4:1 Eb4:2
Eb4:2 D4:1 F4:1 Eb4:1
F4:2 Eb4:3
F4:2 Ab4:1 Bb4:2
Bb4:2 Ab4:1 G4:2
F4:1 Eb4:1 D4:2 C4:1
Eb4:3 F4:2
G4:2 Ab4:1 Bb4:2
Ab4:2 G4:1 F4:2
F4:1 Eb4:1 D4:1 Eb4:2
Eb4:4 R:1
G4:2 F4:2 Eb4:1
F4:2 R:3
Eb4:2 G4:1 Ab4:2
Ab4:2 Bb4:1 Ab4:2
G4:1 F4:1 Eb4:1 D4:2
Db4:1 Eb4:1 F4:2 G4:1
Ab4:3 G4:1 F4:1
D4:2 G4:1 Bb4:2
Ab4:2 G4:1 F4:2
Eb4:1 F4:1 G4:1 Ab4:2
Bb4:2 Ab4:1 G4:2
F4:2 Eb4:1 D4:2
Eb4:1 F4:1 Ab4:1 F4:2
Eb4:2 D4:1 Eb4:2
F4:1 G4:1 F4:1 Eb4:2
F4:2 R:3''',
 lh='''C3:2 Eb3:1 D3:1 F3:1~
F3:1 Ab3:1 G3:1 Eb3:2
Bb2:2 D3:1 F3:1 G3:1
C3+Eb3:5
Ab2:2 Eb3:1 G3:2
F3:2 Ab3:1 Bb3:2
Eb3:1 F3:1 G3:1 Bb2:2
C3:2 G3:1 Ab3:2
F3:1 G3:1 Ab3:1 C4:2
Bb3:2 Ab3:1 F3:2
D3:1 Eb3:1 F3:1 B2:2
C3+Eb3:4 R:1
Ab2:2 Eb3:1 F3:1 G3:1
C3+Eb3:5
Ab2+Eb3:2 Bb2:1 C3+Eb3:2
F3:2 Ab3:1 Bb3:2
Eb3:1 F3:1 G3:1 Bb2:2
Db3:2 Ab2:1 Db3:2
F3:2 Ab3:1 C4:2
G3:2 D3:1 F3:2
Ab2:2 Eb3:1 F3:2
C3:1 D3:1 Eb3:1 Ab2:2
Bb2:2 F3:1 Ab3:2
D3:2 Eb3:1 F3:2
C3:1 G3:1 Ab3:1 F3:2
Eb3:2 B2:1 C3:2
F3:1 Eb3:1 D3:1 G2:2
C3+Eb3:5''',
 tempos=[66,67,68,66,67,68,69,68,69,68,66,65,66,66,67,68,69,70,69,68,67,68,67,66,65,66,65,65],
 phrases=[(1,4),(5,12),(13,20),(21,28)],lower_phrases=[(1,4),(5,12),(13,20),(21,28)],
 sections={1:'p',5:'mp',9:'p',13:'p',17:'mp',21:'p',25:'pp'},lower_sections={1:'p',5:'mp',13:'p',17:'p',25:'pp'},
 voice_phrases=[dict(voice='inner',start_beat=a,end_beat=b,swell=2) for a,b in [(0,20),(20,59),(60,67),(70,100),(100,120),(120,137)]],
 page_starts=[7,13,19,25],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=610),
 pedal=[],hairpins=[('crescendo',6,8),('diminuendo',9,12),('crescendo',15,18),('diminuendo',19,20),('diminuendo',22,24)])
p['performance']['gate']=1

p=study(op=389,title='Lichen Causeway',key='G',fifths=1,meter='3/4',bpm=45,parent=254,
 source=dict(source_opus=254,source_hand='lh',source_start_beat=136,source_end_beat=140,source_pitches=['G','A','C','B'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['G','A','C','B']),
 description='A single unaccompanied line spends twenty-six bars discovering its harmonic route through G, E minor and a passing flat-side shadow. Changes of hand serve the line without interrupting it or adding a second voice. Only the final four bars admit simultaneous harmony: a small C-major opening in the accompaniment leads home to a quiet sixth.',
 technical='Make the unaccompanied line sufficient in tone, direction and breathing. Transfer between hands as one singer, preparing the next position during the preceding long note. Keep the rests of the absent hand exact and avoid pedal that would turn the monody into overlapping harmony. Let the final accompaniment enter softly, without changing the melodic scale or pace.',
 rh='''R:3
R:3
R:3
R:3
R:3
R:3
D4:1 E4:.5 G4:1.5
F#4:1 E4:.5 D4:1.5
B4:1.5 A4:.5 G4:1
F#4:.5 E4:.5 D4:1 B3:1
E4:1 G4:.5 B4:1.5
A4:1 G4:.5 F#4:.5 E4:1
C5:1.5 B4:.5 A4:1
G4:1 F4:.5 Eb4:1.5
D4:.5 F4:.5 Ab4:1 G4:1
F4:1 Eb4:.5 D4:.5 C4:1
R:3
R:3
R:3
R:3
R:3
R:3
D4:1 F#4:.5 A4:1.5
G4:1.5 F#4:.5 E4:1
D4:.5 E4:.5 G4:1 B4:1
A4:1 F#4:.5 G4:1.5
E5:1 D5:.5 C5:1.5
B4:1 A4:.5 F#4:1.5
G4:1 B4:.5 A4:.5 G4:1
G4:2 R:1''',
 lh='''G3:1 A3:1 C4:1
B3:1 D4:1 E4:1
D4:1.5 C4:.5 B3:1
A3:1 C4:.5 B3:1.5
G3:.5 A3:.5 B3:1 D4:1
C4:1.5 A3:.5 B3:1
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
Ab3:1 Bb3:.5 C4:1.5
G3:1 Bb3:.5 D4:1.5
C4:1 Bb3:.5 Ab3:.5 G3:1
F3:1 A3:.5 C4:1.5
B3:1 D4:.5 C4:.5 A3:1
G3:1.5 A3:.5 B3:1
R:3
R:3
R:3
R:3
C3+G3:3
D3+A3:1 C4:2
G3+B3:3
B3:2 R:1''',
 tempos=[45,46,45,44,45,44,45,46,47,46,45,46,45,44,43,42,43,44,43,44,45,44,45,46,45,44,45,44,43,43],
 phrases=[(7,10),(11,16),(23,26),(27,30)],lower_phrases=[(1,6),(17,22),(27,30)],
 sections={1:'p',7:'p',11:'mp',14:'p',23:'p',27:'p',29:'pp'},lower_sections={1:'p',17:'p',20:'mp',27:'pp'},pedal=[],
 hairpins=[('crescendo',7,9),('diminuendo',12,16),('crescendo',23,25),('diminuendo',27,29)])

p=study(op=390,title='Acacia Margin',key='d',fifths=-1,meter='4/4',bpm=50,parent=270,
 source=dict(source_opus=270,source_hand='lh',source_start_beat=72,source_end_beat=76,source_pitches=['D','C','A','G'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['D','C','A','G']),
 description='Five complete phrases contract from nine bars to seven, five, three and two. A recognisable upper head returns over a different bass, then loses its longer excursions as the harmonic destination shifts through D minor, B-flat, G minor, C and finally F. Each entire phrase occupies a smaller register than its predecessor. The underlying pulse remains unchanged; the last major third releases into a full written rest.',
 technical='Keep the same quiet pulse throughout all five phrases; their diminishing proportions must not become an accelerando or a ritardando. Retain the upper head as a remembered gesture over its changing bass. Make the shorter phrases complete in direction, leaving their written final breaths untouched. Prepare the last left-hand move into the middle register and release the final third together.',
 rh='''A4:1 C5:.5 Bb4:.5 G4:2
F4:1 A4:.5 D5:2.5
C5:1 Bb4:.5 A4:.5 G4:2
E5:2 D5:1 C5:1
F5:2 E5:.5 D5:.5 C5:1
Bb4:1 D5:.5 E5:.5 D5:2
A4:1 G4:.5 F4:.5 E4:2
F4:1 G4:.5 A4:.5 C#5:1 D5:1
A4:2 F4:1 R:1
A4:1 C5:.5 Bb4:.5 G4:2
F4:1 A4:.5 C5:.5 Eb5:2
D5:1 C5:.5 Bb4:.5 A4:2
G4:1 Bb4:.5 D5:.5 C5:2
Bb4:1 A4:.5 G4:.5 F4:2
Eb4:1 G4:.5 A4:.5 C5:1 Bb4:1
F4:2 D4:1 R:1
A4:1 C5:.5 Bb4:.5 G4:2
F4:1 G4:.5 A4:.5 Bb4:2
A4:1 G4:.5 F4:.5 Eb4:2
D4:1 F4:.5 A4:.5 Bb4:1 G4:1
Bb4:2 G4:1 R:1
A4:1 Bb4:.5 G4:.5 E4:2
F4:1 A4:.5 G4:.5 D4:1 E4:1
G4:2 E4:1 R:1
A4:1 G4:.5 F4:.5 E4:2
A4:2 R:2''',
 lh='''D3:1.5 C3:.5 A2:1 G2:1
Bb2:1 F3:.5 A3:.5 D3:2
G2:1 D3:.5 F3:.5 Bb2:2
C3:1 G3:.5 Bb3:.5 E3:2
F3:1 C3:.5 A2:.5 D3:2
G2:1 D3:.5 F3:.5 B2:2
A2:1 E3:.5 G3:.5 C#3:2
D3:1 E3:.5 F3:.5 A2:1 D3:1
D2:1 A2:1 D3:1 R:1
F3:1.5 Eb3:.5 C3:1 Bb2:1
F2:1 C3:.5 Eb3:.5 A2:2
Bb2:1 F3:.5 A3:.5 D3:2
Eb3:1 Bb2:.5 D3:.5 G3:2
C3:1 G3:.5 Bb3:.5 Eb3:2
F3:1 C3:.5 Eb3:.5 A2:1 Bb2:1
Bb2:1 F3:1 Bb3:1 R:1
Bb2:1.5 A2:.5 F3:1 Eb3:1
D3:1 F3:.5 A3:.5 Bb3:2
C3:1 G3:.5 Bb3:.5 F3:2
D3:1 A2:.5 C3:.5 F#3:1 G3:1
G3:1 D3:1 G3:1 R:1
C3:1.5 D3:.5 E3:1 G3:1
F3:1 C3:.5 D3:.5 G3:1 C4:1
C4:2 G3:1 R:1
F3:2 A3:1 C4:1
F4:2 R:2''',
 tempos=[50]*26,phrases=[(1,9),(10,16),(17,21),(22,24),(25,26)],lower_phrases=[(1,9),(10,16),(17,21),(22,24),(25,26)],
 sections={1:'p',5:'mp',10:'p',17:'p',22:'p',25:'pp'},lower_sections={1:'p',10:'p',17:'p',22:'pp'},
 pedal=sorted([[4*i+.05,4*i+3.8] for i in range(26) if i not in [7,8,14,15,19,20,23,25]]+[[4*i+.05,4*i+2.8] for i in [8,15,20,23]]+[[28.05,30.8],[31.05,31.8],[56.05,58.8],[59.05,59.8],[76.05,78.8],[79.05,79.8],[100.05,101.8]]),
 hairpins=[('crescendo',2,5),('diminuendo',6,9),('crescendo',11,13),('diminuendo',14,16),('diminuendo',18,21)])
