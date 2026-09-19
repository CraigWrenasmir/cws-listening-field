"""Distant Rooms, CWS Op. 341–350. Individually authored harmonic journeys."""
from weather_common import make_study
PIECES=[]
def study(**kwargs):
    p=make_study(**kwargs);PIECES.append(p);return p

study(op=341,title='Linden Meridian',key='d',fifths=-1,meter='4/4',bpm=55,parent=333,
 source=dict(source_opus=333,source_hand='lh',source_start_beat=0,source_end_beat=5,source_pitches=['D','F','E','A'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','F','E','A']),
 description='An E-flat neighbour first bends a D-minor song and resolves immediately. It returns with increasing weight until the bass claims it, opening a path through E-flat seventh into A-flat. The song does not go home: its opening gesture finds a quieter belonging in the new key.',
 technical='Distinguish the early E-flat neighbour from its later harmonic arrivals. Shape the through-composed melody without treating each bass change as a new beginning. Let the low-voice entries speak gently beneath the held upper notes, and keep the final A-flat phrase in tempo.',
 rh='''D5:1 F5:.5 E5:.5 A5:2
G5:1 F5:1 Eb5:.5 D5:.5 C5:1
Bb4:2 D5:1 F5:1
E5:1 D5:1 C#5:2
D5:2 F5:1 E5:1
Eb5:1 D5:1 C5:1 Bb4:1
A4:3 R:1
D5:1 F5:1 Eb5:2
D5:1 C5:1 Bb4:2
G4:1 Bb4:1 D5:2
Eb5:2 F5:1 G5:1
A5:1 G5:1 F5:1 Eb5:1
D5:2 Eb5:2
F5:1 G5:1 A5:1 Bb5:1
G5:3 R:1
Eb5:2 D5:1 C5:1
Bb4:2 Db5:2
G5:2 F5:1 Eb5:1
Db5:2 Bb4:2
Ab4:3 C5:1
Eb5:2 Db5:1 C5:1
Bb4:1 Ab4:1 G4:2
Ab4:3 R:1
C5:2 Eb5:1 F5:1
G5:1 Ab5:1 Bb5:2
Ab5:2 G5:1 F5:1
Eb5:1 Db5:1 C5:2
Bb4:2 Db5:1 F5:1
Eb5:3 R:1
Ab4:1 C5:.5 Bb4:.5 Eb5:2
Db5:2 C5:1 Bb4:1
Ab4:2 C5:1 Eb5:1
F5:2 Eb5:1 Db5:1
C5:1 Bb4:1 Ab4:2
Bb4:2 G4:2
Ab4:4''',
 lh='''D3:1 A3:.5 F3:1 E3:.5 A2:1
Bb2:1 F3:.5 D3:1 A2:.5 F3:1
G2:1 D3:.5 Bb2:1 F3:.5 D3:1
A2:1 E3:.5 G3:1 C#3:.5 E3:1
D3:1 A3:.5 F3:1 C3:.5 F3:1
Bb2:1 F3:.5 D3:1 C3:.5 E3:1
A2:1 C#3+G3:2 R:1
D3:1 A3:1 F3:2
G2:1 D3:1 Bb2:2
G3:1 F3:1 Eb3:2
C3:1 G3:1 Eb3:2
F3:1 C4:1 A3:2
Bb2:1 F3:1 Ab3:2
Eb3:1 Bb3:1 G3:2
Eb3+G3+Bb3:3 R:1
Eb3:1 G3:1 Bb3:1 Db4:1
Db3:1 Ab3:1 F3:1 C3:1
Eb3:1 G3:1 Bb3:1 Db4:1
Eb3+G3+Db4:4
Ab3+C4:1 Eb3:1 C3:1 Bb2:1
F3:1 Eb3:1 Db3:1 C3:1
Bb2:1 Db3:1 Eb3:1 G3:1
Ab2+C3+Eb3:3 R:1
Ab2:1 Eb3:.5 C3:1 Bb2:.5 Eb3:1
Db3:1 Ab3:.5 F3:1 Eb3:.5 Ab2:1
F3:1 C4:.5 Ab3:1 G3:.5 C3:1
Eb3:1 Bb3:.5 G3:1 F3:.5 Bb2:1
Db3:1 Ab3:.5 F3:1 Eb3:.5 Ab2:1
Eb3:1 G3+Db4:2 R:1
Ab2:1 Eb3:.5 C3:1 Bb2:.5 Eb3:1
Db3:1 Ab3:.5 F3:1 Eb3:.5 Ab2:1
Ab2:1 Eb3:1 C3:2
Db3:1 Ab3:1 F3:2
Ab2+C3+Eb3:2 F3+Ab3:2
Db3+F3+Ab3:2 Eb3+G3+Bb3:2
Ab2+C3+Eb3:4''',
 tempos=[55,56,55,54,55,54,52,55,56,56,57,58,56,58,54,55,54,56,53,54,55,54,52,56,58,57,56,55,52,54,55,54,55,54,53,53],
 phrases=[(1,7),(8,10),(11,15),(16,19),(20,23),(24,29),(30,36)],sections={1:'p',8:'mp',11:'mp',14:'mf',16:'p',20:'pp',24:'mp',25:'mf',27:'p',30:'pp'},lower_sections={1:'pp',11:'p',16:'mp',20:'p',24:'pp',30:'pp'},
 lower_phrases=[(16,19),(20,23)],pedal=sorted([[i*4+.05,i*4+(2.8 if i in [6,14,22,28] else 3.8)] for i in range(36) if i!=34]+[[136.05,137.8],[138.05,139.8]]),hairpins=[('crescendo',11,14),('diminuendo',18,19)],page_starts=[9,17,25,33])

p=study(op=342,title='Aster Vestibule',key='a',fifths=0,meter='4/4',bpm=57,parent=339,
 source=dict(source_opus=339,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['E','G','F#','B'],transposition_semitones=5),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['A','C','B','E']),
 description='A recurring bass phrase supports an A-minor song whose F-sharp first appears as a passing brightness. Unequal variations give that note a more lasting role, until it becomes the centre of a D-major passage. The original bass returns, but the melody keeps its raised sixth and the last harmony preserves the change.',
 technical='Keep the recurring bass recognisable through its altered rhythm and register. The central lower-hand melody needs a singing foreground beneath soft upper intervals. In the final variation, let the active upper figures relax into the raised sixth without making the returning bass heavy.',
 rh='''A4:1 C5:.5 B4:.5 E5:2
D5:1 C5:1 B4:2
A4:1 C5:1 F#5:1 G5:1
E5:2 D5:1 C5:1
B4:1 D5:1 F5:1 E5:1
D5:1 C5:1 B4:1 G#4:1
A4:3 R:1
A4:1 C5:.5 B4:.5 E5:1 D5:1
C5:.5 D5:.5 E5:1 G5:1 E5:1
F#5:2 E5:1 D5:1
E5:1 F#5:1 A5:1 G5:1
F#5:3 R:1
F#4+A4:4
E4+G4:4
F#4+A4:2 G4+B4:2
A4+C#5:4
G4+B4:2 F#4+A4:2
E4+G4:4
F#4+A4:2 E4+G4:2
E4+A4:4
F#4+A4:3 R:1
A4:1 C5:.5 B4:.5 E5:1 F#5:1
G5:.5 F#5:.5 E5:1 D5:.5 C5:.5 B4:1
A4:.5 B4:.5 C5:1 E5:.5 F#5:.5 G5:1
F#5:2 E5:.5 D5:.5 C5:1
B4:.5 C5:.5 D5:1 F#5:.5 E5:.5 D5:1
C5:1 B4:.5 A4:.5 G#4:1 B4:1
A4:2 C5:1 E5:1
F#5:3 R:1
E5:2 C5:1 B4:1
A4:2 C5:2
B4:2 G#4:2
F#4+A4:4''',
 lh='''A2:1 E3:.5 C3:1 G2:.5 B2:1
F2:1 C3:.5 A2:1 E3:.5 C3:1
D3:1 A3:.5 F#3:1 E3:.5 A2:1
A2:1 E3:.5 C3:1 G2:.5 B2:1
B2:1 F3:.5 D3:1 A2:.5 D3:1
E3:1 B3:.5 G#3:1 F3:.5 B2:1
A2+C3+E3:3 R:1
A2:1.5 E3:.5 C3:1 G2:1
F2:1.5 C3:.5 A2:1 E3:1
D3:1.5 A3:.5 F#3:1 C3:1
A2:1.5 E3:.5 C#3:1 G3:1
D3+F#3+A3:3 R:1
D3:1 F#3:1 E3:1 A3:1
G3:1 F#3:.5 E3:.5 D3:2
C#3:1 E3:1 G3:1 B3:1
A3:2 G3:1 F#3:1
E3:1 G3:1 F#3:1 D3:1
C#3:1 B2:1 A2:2
B2:1 D3:1 E3:1 G3:1
A3:1 G3:1 E3:1 C#3:1
D3:3 R:1
A2:1 E3:.5 C3:1 G2:.5 B2:1
F2:1 C3:.5 A2:1 E3:.5 C3:1
A2:1 E3:.5 C3:1 G2:.5 B2:1
D3:1 A3:.5 F#3:1 E3:.5 A2:1
B2:1 F#3:.5 D3:1 A2:.5 D3:1
E3:1 B3:.5 G#3:1 F3:.5 B2:1
A2:1 E3:1 C3:2
D3+F#3+A3:3 R:1
F2+A2+C3:2 E3+G#3:2
A2+C3+E3:4
E3+G#3+B3:4
A2+C3+E3:4''',
 tempos=[57,58,59,58,57,56,54,58,59,59,60,55,57,58,59,60,59,57,58,57,54,58,59,60,59,58,57,56,54,55,55,54,54],
 phrases=[(1,7),(8,12),(22,25),(26,29),(30,33)],lower_phrases=[(13,16),(17,21)],sections={1:'p',8:'mp',11:'mf',13:'pp',22:'mp',24:'mf',26:'mp',30:'pp'},lower_sections={1:'pp',13:'mp',17:'p',22:'pp'},
 pedal=sorted([[i*4+.05,i*4+(2.8 if i in [6,11,20,28] else 3.8)] for i in range(33) if i!=29]+[[116.05,117.8],[118.05,119.8]]),
 hairpins=[('crescendo',8,11),('diminuendo',26,29)],page_starts=[8,14,22,28],system_starts=[1,3,5,7,8,10,12,14,16,18,20,22,24,26,28,30,32])
p['performance']['lower_entries']=[[48,84]]

study(op=343,title='Cedar Threshold',key='F',fifths=-1,meter='4/4',bpm=68,parent=336,
 source=dict(source_opus=336,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4,source_pitches=['F','E','D','C'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['F','E','D','C']),
 description='B natural first brightens an F-major song, then draws its phrases towards C. A complete second song establishes that rival centre before flowing passagework unsettles it. The shortened F-major return accepts the same B-to-C motion, finally resolving it inside the recovered tonic.',
 technical='Keep the lyrical phrases distinct from their quicker connecting figures. The single sixteenth-note passage should remain light, with the bass providing a steady frame. Hear B natural moving towards C throughout the tonal journey; in the last bar it resolves over a held F-major chord.',
 rh='''F5:1 E5:.5 D5:.5 C5:2
A4:1 C5:1 D5:1 E5:1
F5:1 A5:1 B5:.5 C6:1.5
D6:1 C6:1 Bb5:1 A5:1
G5:1 Bb5:1 A5:1 F5:1
E5:1 G5:1 B5:1 D6:1
C6:1 D6:.5 C6:.5 B5:1 G5:1
F5:1 E5:1 D5:1 C5:1
Bb4:1 A4:1 G4:1 E4:1
F4:3 R:1
A4:1 C5:1 E5:1 G5:1
A5:.5 G5:.5 F5:.5 E5:.5 D5:.5 E5:.5 B4:.5 C5:.5
D5:1 F5:1 A5:1 C6:1
B5:1 A5:1 G5:1 F5:1
E5:1 G5:1 B5:1 D6:1
C6:3 R:1
C6:1 B5:.5 A5:.5 G5:2
E5:1 G5:1 A5:1 B5:1
D6:1 C6:1 B5:1 A5:1
G5:2 E5:1 D5:1
F5:1 A5:1 G5:1 E5:1
D5:1 F5:1 E5:1 C5:1
B4:1 D5:1 G5:1 F5:1
E5:3 R:1
A5:.25 G5:.25 F5:.25 E5:.25 D5:.25 E5:.25 F5:.25 G5:.25 A5:.25 C6:.25 B5:.25 A5:.25 G5:.25 F5:.25 E5:.25 D5:.25
C5:2 E5:1 G5:1
F5:.5 G5:.5 A5:.5 Bb5:.5 C6:.5 D6:.5 E6:.5 D6:.5
C6:2 Bb5:1 A5:1
G5:.5 F5:.5 E5:.5 D5:.5 C5:.5 D5:.5 E5:.5 F5:.5
C5:1 E5:1 G5:1 B5:1
D6:1 C6:1 B5:1 A5:1
G5:3 R:1
F5:1 E5:.5 D5:.5 C5:2
A4:1 C5:1 D5:1 E5:1
F5:1 A5:1 B5:.5 C6:1.5
Bb5:1 A5:1 G5:1 F5:1
E5:1 D5:1 C5:1 Bb4:1
A4:1 C5:1 D5:1 E5:1
F5:2 E5:1 D5:1
B4:1 C5:3''',
 lh='''F3:1 C4:.5 A3:.5 G3:1 C3:1
D3:1 A3:.5 F3:.5 E3:1 A2:1
F3:1 C4:.5 A3:.5 G3:1 C3:1
Bb2:1 F3:.5 D3:.5 C3:1 F3:1
G2:1 D3:.5 Bb2:.5 A2:1 D3:1
C3:1 G3:.5 E3:.5 D3:1 G2:1
A2:1 E3:.5 C3:.5 B2:1 E3:1
D3:1 A3:.5 F3:.5 E3:1 A2:1
C3:1 G3:.5 Bb3:.5 E3:1 G3:1
F3+A3+C4:3 R:1
F3:.5 A3:.5 C4:.5 A3:.5 E3:.5 G3:.5 C4:.5 G3:.5
D3:.5 F3:.5 A3:.5 F3:.5 C3:.5 E3:.5 G3:.5 E3:.5
D3:.5 F3:.5 A3:.5 D3:.5 G2:.5 B2:.5 D3:.5 C3:.5
G2:1 B2:1 D3:1 F3:1
G2:1 D3:1 F3:1 B2:1
C3+E3+G3:3 R:1
C3:1 G3:.5 E3:.5 D3:1 G2:1
A2:1 E3:.5 C3:.5 B2:1 E3:1
D3:1 A3:.5 F3:.5 E3:1 A2:1
C3:1 G3:.5 E3:.5 D3:1 G2:1
F3:1 C4:.5 A3:.5 G3:1 C3:1
D3:1 A3:.5 F3:.5 E3:1 A2:1
G2:1 D3:.5 F3:.5 B2:1 D3:1
C3+E3+G3:3 R:1
D3:1 A3:1 F3:1 A2:1
A2:.5 C3:.5 E3:.5 C3:.5 G2:.5 B2:.5 E3:.5 B2:.5
Bb2:1 F3:1 D3:1 F3:1
F3:.5 A3:.5 C4:.5 A3:.5 E3:.5 G3:.5 Bb3:.5 G3:.5
C3:1 G3:1 E3:1 G2:1
A2:.5 C3:.5 E3:.5 C3:.5 G2:.5 B2:.5 D3:.5 B2:.5
G2:1 B2:1 D3:1 F3:1
C3+E3+Bb3:3 R:1
F3:1 C4:.5 A3:.5 G3:1 C3:1
D3:1 A3:.5 F3:.5 E3:1 A2:1
F3:1 C4:.5 A3:.5 G3:1 C3:1
Bb2:1 F3:.5 D3:.5 C3:1 F3:1
C3:1 G3:.5 E3:.5 Bb2:1 D3:1
D3:1 A3:.5 F3:.5 E3:1 A2:1
Bb2+D3+F3:2 C3+E3+G3:2
F3+A3+C4:4''',
 tempos=[68,69,70,70,69,70,70,69,67,64,70,72,72,71,70,66,68,69,70,69,70,69,68,65,68,69,72,71,70,71,70,66,68,69,70,69,68,67,66,66],
 phrases=[(1,5),(6,10),(11,16),(17,20),(21,24),(25,28),(29,32),(33,36),(37,40)],sections={1:'p',6:'mp',11:'mp',15:'mf',17:'p',25:'mp',27:'f',29:'mf',33:'p',37:'pp'},lower_sections={1:'pp',11:'p',17:'pp',25:'p',33:'pp'},
 pedal=sorted([[i*4+.05,i*4+(2.8 if i in [9,15,23,31] else 3.8)] for i in range(40) if i!=38]+[[152.05,153.8],[154.05,155.8]]),hairpins=[('crescendo',11,15),('diminuendo',29,32)],page_starts=[9,17,25,33])

p=study(op=344,title='Moss Parallax',key='C',fifths=0,meter='4/4',bpm=55,parent=336,
 source=dict(source_opus=336,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4,source_pitches=['F','E','D','C'],transposition_semitones=7),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['C','B','A','G']),
 description='A chordal C-major phrase admits B-flat as a soft shadow. That note then becomes the third of G minor, where the texture opens into two exposed songs of unequal length. Only the earlier cadence comes back: its B-flat falls to A above a quiet C-sixth harmony.',
 technical='Bring out the top line of the opening intervals without equal weight in every chord tone. In the longer G-minor panel, follow the separate phrase lengths of both hands. Let the final B-flat resolve to A gently, without an added rallentando.',
 rh='''E4+G4+C5:1 D4+G4+B4:1 C4+E4+A4:1 B3+E4+G4:1
C4+F4+A4:2 D4+G4+B4:2
E4+G4+C5:2 F4+A4+D5:1 E4+G4+C5:1
D4+G4+Bb4:3 E4+G4+A4:1
F4+A4+C5:2 E4+G4+B4:2
D4+G4+A4:1 E4+G4+C5:2 R:1
G4+C5+E5:2 A4+C5+F5:2
G4+B4+D5:1 F4+A4+C5:1 E4+G4+B4:2
D4+F4+Bb4:2 C4+E4+A4:2
D4+G4+Bb4:4
Eb4+G4+C5:2 F4+A4+D5:2
F#4+A4+C5:3 R:1
G5:2 F5:1 D5:1
Eb5:1 D5:.5 C5:.5 Bb4:2
A4:1 Bb4:1 C5:1 Eb5:1
D5:2 F#5:1 A5:1
G5:3 R:1
R:1 D5:1 Eb5:1 F5:1
G5:1 A5:.5 Bb5:.5 A5:1 G5:1
F5:2 Eb5:1 D5:1
C5:1 D5:1 Eb5:1 G5:1
F#5:2 A5:1 C6:1
Bb5:2 A5:1 G5:1
Eb5:1 D5:1 C5:2
D5:1 F5:1 Eb5:1 C5:1
Bb4:2 A4:1 G4:1
F#4:2 A4:1 C5:1
Bb4:1 D5:1 G5:2
F5:2 Eb5:1 D5:1
C5:2 Bb4:2
A4:2 G4:1 F4:1
E4:3 R:1
F4+A4+C5:2 E4+G4+B4:2
D4+G4+Bb4:2 E4+G4+A4:2
E4+G4+A4:3 R:1''',
 lh='''C3:2 E3:2
F2+A2:2 G2+B2:2
C3+E3:2 D3+F3:1 C3+E3:1
G2:2 C3:2
F2+A2:2 E3+G3:2
G2+B2:1 C3+E3:2 R:1
C3:2 F3:2
G2:2 E3:2
Bb2:2 A2:2
G2:1 D3:1 F3:1 Bb3:1
Eb3:1 Bb3:1 A3:1 F3:1
D3:1 A3:1 C4:1 R:1
G3:1 Bb3:1 A3:1 F3:1
Eb3:2 G3:1 Bb3:1
C4:1 Bb3:1 A3:1 G3:1
F#3:1 D3:1 E3:1 F#3:1
G3:1 D3:1 Bb2:2
C3:2 Eb3:1 F3:1
Eb3:2 D3:2
Bb2:1 D3:1 G3:2
A3:1 G3:.5 F3:.5 Eb3:1 C3:1
D3:2 F#3:1 A3:1
G3:1 Bb3:1 A3:1 G3:1
C3:2 Eb3:1 G3:1
Bb2:1 C3:1 D3:1 Eb3:1
G3:2 Eb3:1 C3:1
D3:1 F#3:1 A3:1 D4:1
G3:2 Bb3:1 A3:1
Ab3:2 G3:1 F3:1
Eb3:1 G3:1 C4:1 Bb3:1
F3:1 A3:1 G3:1 D3:1
C3+G3:3 R:1
F3:2 E3:2
G2:2 C3:2
C3+G3:3 R:1''',
 tempos=[55,56,57,55,56,53,57,56,55,54,55,52,56,57,58,57,55,56,58,57,58,59,57,56,57,55,56,57,56,55,54,53,54,54,54],
 phrases=[(1,6),(7,12),(13,17),(18,23),(24,28),(29,32),(33,35)],lower_phrases=[(13,16),(17,21),(22,27),(28,32)],sections={1:'p',7:'mp',10:'p',13:'mp',18:'p',21:'mf',24:'mp',29:'p',33:'pp'},lower_sections={1:'pp',13:'p',17:'mp',22:'p',28:'mp',33:'pp'},
 pedal=sorted([[i*4+.05,i*4+(2.8 if i in [5,11,31,34] else 3.8)] for i in range(35) if i not in [1,2,4,6,7,8,10,32,33]]+[[i*4+.05,i*4+1.8] for i in [1,4,6,8,10,32,33]]+[[i*4+2.05,i*4+3.8] for i in [1,4,6,8,10,32,33]]+[[8.05,9.8],[10.05,10.85],[11.05,11.85],[28.05,28.85],[29.05,29.85],[30.05,31.8]]),
 hairpins=[('crescendo',18,22),('diminuendo',29,32)],page_starts=[9,17,25,33])
p['performance']['lower_entries']=[[64,84],[108,128]]

p=study(op=345,title='Fennel Hinterland',key='C',fifths=0,meter='6/4',bpm=59,parent=344,
 source=dict(source_opus=344,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['C','B','A','G'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=6,pitches=['C','B','A','G']),
 description='A six-bar ground returns in spans of nine and ten bars. A-flat begins as borrowed colour over C; prolonged passages gradually give it authority as a new home. The bass finally falls silent, leaving the upper intervals to complete the arrival without their old support.',
 technical='Project the long melody above the held inner notes in the first cycle. Preserve the identity of the bass through inserted bars and displaced entries. The final four bars belong to the upper hand alone; retain their pulse and clear the pedal between the changing harmonies.',
 rh='''G5:3 E5:1 D5:2
C5:2 D5:1 E5:1 F5:1 Eb5:1
D5:2 C5:1 Bb4:1 A4:2
Ab4:3 Bb4:1 C5:2
F4:2 G4:1 Ab4:1 G4:2
G4:2 A4:1 B4:1 D5:2
G5:2 F5:1 E5:1 D5:1 C5:1
Eb5:3 D5:1 C5:2
D5:2 F5:1 Eb5:1 D5:2
C5:1 D5:1 Eb5:1 F5:1 Ab5:2
G5:2 F5:1 Eb5:1 C5:2
Ab4:2 C5:1 Eb5:1 D5:2
C5:1 Bb4:1 Ab4:1 G4:1 F4:2
G4:3 A4:1 B4:2
D5:3 B4:1 R:2
G5:1 E5:2 D5:1 C5:2
Eb5:2 G5:1 Ab5:1 G5:2
F5:1 D5:2 C5:1 Bb4:2
D5:2 F5:1 Ab5:1 G5:2
Ab5:3 G5:1 F5:2
Eb5:1 Db5:1 C5:2 Bb4:2
Ab4:2 C5:1 Eb5:1 F5:2
G5:2 F5:1 Eb5:1 Db5:2
Bb4:2 Db5:2 G5:2
Ab5:3 Eb5:1 C5:2
Ab4+C5:3 Bb4+Db5:1 C5+Eb5:2
Db5+F5:2 C5+Eb5:1 Bb4+Db5:1 Ab4+C5:2
G4+Bb4+Db5:3 Ab4+C5:3
Ab4+C5+Eb5:6''',
 lh='''C3:2 B2:1 A2:1 G2:2
C3:3 G3:1 Ab3:2
Bb2:2 F3:1 Eb3:1 D3:2
Ab2:3 Eb3:1 F3:2
F2:2 C3:1 D3:1 Ab2:2
G2:2 D3:1 F3:1 B2:2
C3:2 B2:1 A2:1 G2:2
C3:3 G3:1 Ab3:2
Bb2:2 F3:1 Eb3:1 D3:2
Bb2:3 D3:1 F3:1 Ab3:1
Ab2:3 Eb3:1 F3:2
F2:2 C3:1 D3:1 Ab2:2
F2:3 C3:1 Eb3:2
G2:2 D3:1 F3:1 B2:2
G2:2 D3+F3:2 R:2
R:1 C3:1 B2:1 A2:1 G2:2
C3:2 G3:2 Ab3:2
Bb2:1 F3:2 Eb3:1 D3:2
Bb2:3 F3:1 Ab3:2
Ab2:2 Eb3:2 F3:2
Ab2:3 C3:1 Eb3:2
F2:1 C3:2 D3:1 Ab2:2
G2:3 Bb2:1 Db3:2
Eb3:2 Bb3:1 G3:1 Db4:2
Ab3+C4:6
R:6
R:6
R:6
R:6''',
 rh_inner='''G4:6
Ab4:6
F4:6
Eb4:6
C4:6
D4:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6''',hidden_voice_rests={'inner':list(range(7,30))},
 tempos=[59,60,59,58,59,57,60,59,61,62,60,59,58,59,57,60,61,60,61,62,60,59,58,57,56,57,58,57,57],
 phrases=[(1,6),(7,11),(12,15),(16,20),(21,25),(26,29)],sections={1:'p',7:'mp',10:'mf',12:'p',16:'mp',19:'mf',21:'mp',24:'p',26:'pp'},lower_sections={1:'p',7:'mp',12:'p',16:'mp',24:'p'},
 pedal=sorted([[i*6+.05,i*6+(3.8 if i==14 else 5.8)] for i in range(29) if i not in [25,26,27]]+[[150.05,152.8],[153.05,153.85],[154.05,155.8],[156.05,157.8],[158.05,158.85],[159.05,159.85],[160.05,161.8],[162.05,164.8],[165.05,167.8]]),
 hairpins=[('crescendo',7,10),('diminuendo',20,25)],page_starts=[7,13,19,25],engraving=dict(spacing_system=20,spacing_staff=23,pedal_offset_y=680))

p=study(op=346,title='Willow Refraction',key='C',fifths=0,meter='4/4',bpm=57,parent=334,
 source=dict(source_opus=334,source_hand='rh',source_start_beat=0,source_end_beat=4.5,source_pitches=['Db','C','Bb','Ab'],transposition_semitones=-1),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['C','B','A','G']),
 description='A single uninterrupted cantilena travels from C through B minor to D major. F-sharp recurs at changing points in the melody and in a quiet tenor strand: first a luminous tension, then a dominant support, finally the third of the new tonic. The last phrase resolves simply, without restating the opening.',
 technical='Carry the melody across the tied bar lines and the changes of harmonic field. Sustain the occasional tenor F-sharps with the left hand while releasing its bass notes independently. Keep the brief faster figures inside the continuous phrase rather than presenting them as separate flourishes.',
 rh='''C5:1 B4:.5 A4:.5 G4:2~
G4:1 E5:1 F#5:2
G5:2 E5:1 D5:1
C5:1 B4:1 D5:1 F#5:1~
F#5:1 G5:1 E5:1 D5:1
C#5:1 E5:1 A#4:1 F#5:1~
F#5:1 D5:2 C#5:1
B4:2 D5:1 E5:1
F#5:1 A5:.5 G5:.5 F#5:1 E5:1
D5:3 C#5:1
B4:1 C#5:1 D5:1 F#5:1~
F#5:2 E5:1 C#5:1
A#4:1 C#5:1 E5:1 G5:1
F#5:2 D5:1 B4:1
C#5:.5 D5:.5 E5:.5 F#5:.5 G5:.5 F#5:.5 E5:.5 D5:.5
C#5:1 B4:1 A#4:1 F#5:1
B5:2 A5:1 F#5:1
G5:1 A5:1 B5:1 C#6:1
D6:2 C#6:1 B5:1
A5:1 G5:1 F#5:1 E5:1
D5:1 E5:1 C#5:1 F#5:1~
F#5:1 E5:1 G5:1 C#5:1
D5:2 F#5:1 A5:1
B5:1 A5:1 G5:1 F#5:1
E5:2 D5:1 B4:1
A4:1 C#5:1 F#5:2~
F#5:1 G5:.5 A5:.5 B5:1 A5:1
G5:2 E5:1 C#5:1
D5:1 F#5:1 E5:1 D5:1
C#5:2 B4:1 A4:1
G4:1 A4:1 C#5:2
D5:2 F#5:1 E5:1
D5:4''',
 lh='''C3:2 E3:1 G3:1
C3:1 E3:1 D3:2
E3:2 B2:1 D3:1
C3:2 E3:2
E3:1 G3:1 B2:1 D3:1
F#2:2 C#3+E3+A#3:2
B2:1 D3:1 E3:2
G2:2 D3:1 B2:1
E3:1 B2:1 D3:1 G3:1
B2:2 D3:2
G2:1 D3:1 B2:1 E3:1
A2:2 E3:1 G3:1
F#2:1 C#3:1 E3:2
B2:2 F#3:1 D3:1
E3:1 B2:1 G3:1 E3:1
F#2:2 C#3:1 E3:1
B2:1 F#3:1 D3:2
G2:2 D3:1 B2:1
B2:2 D3:1 E3:1
E3:1 B2:1 G3:1 E3:1
G2:1 D3:1 B2:1 E3:1
A2:1 E3:1 G3:1 E3:1
D3:1 A2:1 D3:2
G2:2 D3:1 B2:1
E3:2 B2:1 G3:1
D3:2 A2:2
G2:1 D3:1 B2:1 E3:1
A2:2 E3:1 G3:1
B2:2 D3:1 F#3:1
D3:1 A2:1 B2:1 D3:1
A2:2 E3:1 G3:1
D3:2 A2:2
D3+A3:4''',
 lh_upper='''R:4
F#3:4
R:4
F#3:4
R:4
R:4
F#3:4
R:4
R:4
F#3:4
R:4
R:4
F#3:4
R:4
R:4
F#3:4
R:4
R:4
F#3:4
R:4
R:4
R:4
F#3:4
R:4
R:4
F#3:4
R:4
R:4
R:4
F#3:4
R:4
F#3:4
F#3:4''',hidden_voice_rests={'tenor':[1,3,5,6,8,9,11,12,14,15,17,18,20,21,22,24,25,27,28,29,31]},
 tempos=[57,58,59,58,59,58,57,58,59,57,58,59,58,57,59,58,60,61,62,60,59,58,58,59,58,57,59,58,57,57,56,56,56],
 phrases=[(1,6),(7,12),(13,16),(17,22),(23,28),(29,33)],sections={1:'p',7:'mp',13:'p',17:'mf',20:'mp',23:'p',27:'mp',29:'p',31:'pp'},lower_sections={1:'pp',7:'p',17:'p',23:'pp'},
 pedal=[[i*4+.05,i*4+3.8] for i in range(33)],hairpins=[('crescendo',13,18),('diminuendo',27,31)],page_starts=[9,17,25,31],system_starts=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33])
p['performance']['tenor_entries']=[[4,8],[12,16],[24,28],[36,40],[48,52],[60,64],[72,76],[88,92],[100,104],[116,120],[124,132]]

study(op=347,title='Hazel Doorway',key='a',fifths=0,meter='3/2',bpm=61,parent=337,
 source=dict(source_opus=337,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['B','D','C#','F#'],transposition_semitones=-2),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['A','C','B','E']),
 description='An A-minor song reaches a diminished seventh and returns safely home. When the same keys sound again, their voices choose another exit: D rises to E-flat, F to G-flat and C-flat falls to B-flat. The first-inversion arrival settles into root-position E-flat minor, where the longer second song remains.',
 technical='Voice each of the four notes in the two diminished-chord resolutions. They use the same keys in the same register, but every line takes a different step at the second outcome. Clear the pedal at both resolutions and preserve the upper arrival as E-flat subsequently enters the bass.',
 rh='''A4:2 C5:1 B4:1 E5:2
F5:2 E5:1 D5:1 C5:1 B4:1
A4:3 G4:1 F4:1 E4:1
D5:2 F5:1 E5:1 G#5:1 B5:1
E5:2 D5:1 C5:1 B4:1 G#4:1
F4+B4:6
E4+C5:6
C5:1 E5:1 A5:2 G5:1 F5:1
D5:2 F5:1 E5:1 D5:1 B4:1
C5:2 A4:1 G4:1 F4:1 E4:1
D4+F4:2 E4+G#4:2 F4+B4:2
F4+Cb5:6
Gb4+Bb4:6
Bb4:2 Eb5:2 Db5:1 Cb5:1
Bb4:3 Ab4:1 Gb4:2
F4:2 Ab4:1 Cb5:1 Eb5:2
D5:2 F5:1 Ab5:1 Gb5:2
Gb5:3 F5:1 Eb5:2
Db5:1 Eb5:1 F5:2 Ab5:2
Gb5:2 Bb5:2 Ab5:1 Gb5:1
F5:2 Eb5:1 Db5:1 Cb5:2
Bb4:3 Ab4:1 Gb4:2
F4:1 Ab4:1 Cb5:1 Bb4:1 Ab4:1 F4:1
Gb4:3 Bb4:1 Eb5:2
Db5:2 Cb5:1 Bb4:1 Ab4:2
F4:2 Ab4:2 D5:2
Eb5:2 Gb5:1 F5:1 Eb5:2
Gb4+Bb4+Eb5:4 R:2''',
 lh='''A2:2 E3:1 C3:1 B2:2
D3:2 A3:1 F3:1 E3:2
F2:3 C3:1 D3:1 C3:1
D3:2 A3:1 F3:1 E3:1 B2:1
E3:2 B2:1 G#2:1 D3:2
G#2+D3:6
A2+C3:6
A2:2 E3:1 C3:1 F3:2
D3:3 A3:1 G#3:2
F3:2 C3:1 A2:1 D3:2
F2+A2:2 E2+B2:2 G#2+D3:2
Ab2+D3:6
Gb2+Eb3:6
Eb3:2 Bb3:2 Gb3:2
Cb3:2 Gb3:2 Eb3:2
Ab2:3 Eb3:1 Cb3:2
Bb2:2 F3:1 Ab3:1 D3:2
Eb3:3 Bb3:1 Gb3:2
Db3:2 F3:1 Ab3:1 Cb3:2
Gb3:2 Bb3:1 Db4:1 Bb3:2
Ab2:2 Eb3:1 Cb3:1 Gb3:2
Eb3:2 Bb2:1 Gb2:1 Bb2:2
Bb2:3 D3:1 Ab3:2
Eb3:2 Bb3:1 Gb3:1 Eb3:2
Cb3:2 Gb3:1 Eb3:1 Ab2:2
Bb2:2 F3:2 Ab3:2
Eb3:2 Bb3:1 Gb3:1 Eb3:2
Eb3+Bb3:4 R:2''',
 tempos=[61,62,61,63,61,58,59,62,63,61,60,58,58,60,61,62,63,61,62,64,62,61,60,61,60,59,59,59],
 phrases=[(1,5),(6,7),(8,11),(12,13),(14,18),(19,24),(25,28)],sections={1:'p',4:'mp',6:'pp',8:'mp',10:'p',12:'pp',14:'p',17:'mp',19:'mp',20:'mf',22:'p',25:'pp'},lower_sections={1:'pp',6:'p',8:'pp',12:'p',14:'pp',19:'p',25:'pp'},
 pedal=sorted([[i*6+.05,i*6+(3.8 if i==27 else 5.8)] for i in range(28) if i!=10]+[[60.05,61.8],[62.05,63.8],[64.05,65.8]]),hairpins=[('crescendo',14,17),('diminuendo',20,24)])

p=study(op=348,title='Iris Convergence',key='C',fifths=0,meter='5/4',bpm=57,parent=345,
 source=dict(source_opus=345,source_hand='lh',source_start_beat=0,source_end_beat=6,source_pitches=['C','B','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['C','B','A','G']),
 description='The upper song hears F-sharp leaning towards G in C major; the lower song hears it as D major’s stable third. Their five-bar and four-bar phrases are introduced separately, then overlap with unequal endings. A shared six-bar span brings them to E minor, where F-sharp can remain a ninth while the upper neighbour resolves.',
 technical='Keep the two melodic identities audible as their phrase boundaries cross. Balance the lower song against soft upper intervals in its first entry. In the close, sustain the left-hand F-sharp while the upper hand resolves to G; both colours belong to the final E-minor-nine chord.',
 rh='''C5:1.5 B4:.5 A4:1 G4:2
G4:1 E5:1 F#5:1 G5:2
F5:2 E5:1 D5:1 E5:1
C5:1 B4:1 A4:1 F#4:1 G4:1
E4+G4+C5:4 R:1
F#4+A4:5
G4+B4:3 F#4+A4:2
E4+G4:3 E4+A4:2
F#4+A4:4 R:1
C5:1.5 B4:.5 A4:1 G4:2
G4:1 E5:1 F#5:1 G5:2
F5:2 E5:1 D5:1 E5:1
C5:1 B4:1 A4:1 F#4:1 G4:1
B4:2 D5:1 F#5:2
G5:3 E5:2
G5:1 F#5:1 E5:1 D5:2
C5:2 E5:1 G5:2
F#5:1 A5:1 G5:1 E5:2
D5:2 C5:1 B4:1 A4:1
F#4:1 G4:3 R:1
G5:1.5 F#5:.5 E5:1 B4:2
C5:2 B4:1 A4:1 G4:1
A4:1 C5:1 E5:1 F#5:2
G5:2 F#5:1 E5:1 D5:1
C5:2 B4:1 A4:1 F#4:1
G4:4 R:1
B4:2 A4:1 F#4:1 G4:1
F#4:2 G4:3
G4+B4+E5:5''',
 lh='''C3+G3:3 E3:2
C3:3 E3+G3:2
F3+A3:2 E3+G3:3
D3+A3:3 C3+E3:2
C3+G3:4 R:1
D3:1.5 F#3:.5 E3:1 A3:2
B3:1.5 A3:.5 G3:1 F#3:2
E3:1 G3:1 F#3:1 C#3:1 D3:1
F#3:1 A3:1 D4:2 R:1
D3:1.5 F#3:.5 E3:1 A3:2
B3:1.5 A3:.5 G3:1 F#3:2
E3:1 G3:1 F#3:1 C#3:1 D3:1
D3:1 F#3:1 A3:2 R:1
D3:1 E3:1 F#3:1 B3:2
A3:1 G3:1 F#3:1 E3:1 D3:1
C3:2 E3:1 G3:2
A3:2 G3:1 E3:1 D3:1
D3:1 F#3:1 A3:2 R:1
B2:1 D3:1 F#3:1 A3:2
E3:2 B2:1 D3:1 E3:1
E3:1.5 F#3:.5 G3:1 B3:2
A3:2 G3:1 F#3:1 E3:1
F#3:1 A3:1 C4:1 B3:2
E3:2 B2:1 D3:1 F#3:1
A3:2 F#3:1 D#3:1 B2:1
E3+F#3+B3:4 R:1
E3:2 B2:1 D3:1 F#3:1
E3+F#3+B3:5
E3+F#3+B3:5''',
 tempos=[57,58,57,56,54,57,58,57,55,58,59,58,57,59,60,59,60,61,59,57,58,59,60,59,57,56,57,57,57],
 phrases=[(1,5),(10,15),(16,20),(21,26),(27,29)],lower_phrases=[(6,9),(10,13),(14,18),(19,20),(21,26),(27,29)],sections={1:'p',6:'pp',10:'mp',16:'mf',19:'mp',21:'p',27:'pp'},lower_sections={1:'pp',6:'mp',10:'p',14:'mp',19:'p',21:'p',27:'pp'},
 pedal=sorted([[i*5+.05,i*5+(3.8 if i in [4,8,25] else 4.8)] for i in range(29) if i not in [0,1,2,3,6,7]]+[[i*5+.05,i*5+2.8] for i in [0,1,3,6,7]]+[[i*5+3.05,i*5+4.8] for i in [0,1,3,6,7]]+[[10.05,11.8],[12.05,14.8]]),hairpins=[('crescendo',10,15),('diminuendo',21,26)],page_starts=[9,17,25])
p['performance']['lower_entries']=[[25,45],[65,90],[100,130]]

study(op=349,title='Sedge Reconciliation',key='f',fifths=-4,meter='7/4',bpm=64,parent=341,
 source=dict(source_opus=341,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=3),motif=dict(hand='rh',start_beat=0,end_beat=7,pitches=['F','Ab','G','C']),
 description='Three unequal attempts at closure leave an F-minor song unsettled: a melodic arrival lands over D-flat, a later leading note remains suspended above the dominant, and a third approach breaks into silence. After the empty bar, the quiet E-to-F release finally receives its tonic bass. Only three bars are needed to finish.',
 technical='Maintain the long seven-quarter span without accenting every internal division. Distinguish the deceptive bass, the withheld melodic release and the complete written silence. The final resolution is soft and direct; give the pedal-free interruption its full duration.',
 rh='''F5:2 Ab5:1 G5:1 C6:3
Bb5:2 Ab5:1 G5:1 F5:1 E5:2
F5:4 Ab5:1 G5:2
Db5:2 F5:2 E5:3
E5:4 G5:1 Bb5:2
F5:5 R:2
Ab4+C5+Eb5:7
G4+Bb4+D5:4 Ab4+C5+Eb5:3
F4+Ab4+C5:3 G4+Bb4+D5:4
Eb5:1 G5:1 Bb5:2 Ab5:1 G5:2
Ab5:2 G5:1 F5:1 Eb5:3
D5:2 F5:1 Ab5:1 G5:3
E5:4 F5:.5 E5:.5 D5:1 C5:1
E5:7
R:1 G5:2 Bb5:1 Ab5:1 Db6:2
C6:2 Bb5:1 Ab5:1 G5:3
F5:2 Ab5:1 G5:1 Eb5:3
Db5:.5 Eb5:.5 F5:.5 G5:.5 Ab5:1 G5:1 F5:3
E5:3 G5:1 Bb5:1 C6:2
E5:3 R:4
R:7
E5:1 F5:4 Ab5:1 G5:1
F5:3 Eb5:1 Db5:1 C5:2
Ab4+C5+F5:5 R:2''',
 lh='''F3:3 C4:2 Ab3:2
Bb2:3 F3:2 Db3:2
F3:4 C4:1 Ab3:2
Db3+F3+Ab3:4 C3+E3+Bb3:3
C3:3 G3:1 Bb3:1 E3:2
Db3+F3+Ab3:5 R:2
Ab2:3 Eb3:2 C3:2
Bb2:4 Eb3:3
F3:3 G3:4
C3:2 Eb3:1 G3:2 Bb3:2
Db3:3 Ab3:2 F3:2
Bb2:3 F3:2 D3:2
C3:3 G3:1 Bb3:1 E3:2
C3+E3+Bb3:7
Eb3:3 Bb3:2 G3:2
Ab2:3 Eb3:2 C3:2
Db3:3 Ab3:2 F3:2
Bb2:2 Db3:1 F3:1 Ab3:3
C3:3 G3:1 Bb3:1 E3:2
C3+G3+Bb3:3 R:4
R:7
C3+E3+Bb3:1 F3+Ab3+C4:6
Bb2+Db3+F3:3 C3+G3+Bb3:4
F3+C4:5 R:2''',
 tempos=[64,65,64,63,62,60,64,65,66,67,65,64,63,61,65,66,65,64,63,61,61,62,62,62],
 phrases=[(1,6),(7,9),(10,14),(15,20),(22,24)],sections={1:'p',4:'mp',6:'pp',7:'p',10:'mp',13:'p',15:'mp',18:'mf',19:'mp',20:'pp',22:'pp'},lower_sections={1:'pp',4:'p',6:'pp',10:'p',14:'pp',15:'p',20:'pp'},
 pedal=sorted([[i*7+.05,i*7+(4.8 if i in [5,23] else 2.8 if i==19 else 6.8)] for i in range(24) if i not in [3,7,8,20,21,22]]+[[21.05,24.8],[25.05,27.8],[49.05,52.8],[53.05,55.8],[56.05,58.8],[59.05,62.8],[147.05,147.85],[148.05,153.8],[154.05,156.8],[157.05,160.8]]),hairpins=[('crescendo',15,18),('diminuendo',19,20)])

study(op=350,title='Velvet Distance',key='C',fifths=0,meter='3/4',bpm=58,parent=346,
 source=dict(source_opus=346,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['C','B','A','G'],transposition_semitones=4),motif=dict(hand='rh',start_beat=60,end_beat=63,pitches=['E','D#','C#','B']),
 description='D-sharp first appears as a brief neighbour to E above a C-major setting. Fragments gather into a partial song, then fall apart as their harmony changes. Only after a full silence does the complete E-major theme emerge; its leading note makes the opening colour intelligible. The final statement descends into the middle register.',
 technical='Keep the early fragments connected through their silences without filling the rests with pedal. Give the late complete theme a continuous line, with its accompaniment gently in the background. Carry that line down into the quieter middle register and let the final written rest close the chapter.',
 rh='''R:1 D#5:.5 E5:1.5
G5:1 F5:.5 E5:.5 R:1
R:1 D#5:1 E5:1
E5:2 R:1
E5:1 D#5:.5 E5:.5 G5:1
A5:1 G5:1 E5:1
D5:1 F5:1 E5:1
B4:1 D5:1 G5:1
E5:2 R:1
E5:1 D#5:.5 E5:.5 G5:1
F5:1 A5:1 G5:1
F#5:1 E5:1 D#5:1
E5:2 R:1
G#5:1 F#5:1 E5:1
D#5:1 F#5:1 A5:1
G#5:1 R:2
R:1 D#5:1 E5:1
F#5:2 D#5:1
E5:2 R:1
R:3
E5:1 D#5:.5 C#5:.5 B4:1
G#4:1 B4:1 C#5:1
D#5:1 F#5:.5 E5:.5 D#5:1
C#5:2 B4:1
A4:1 C#5:1 B4:1
G#4:1 B4:1 D#5:1
E5:2 R:1
F#5:1 G#5:.5 A5:.5 B5:1
G#5:1 F#5:1 E5:1
D#5:.5 E5:.5 F#5:1 A5:1
G#5:2 F#5:1
E5:1 D#5:1 C#5:1
B4:2 R:1
E5:1 D#5:.5 C#5:.5 B4:1
G#4:1 B4:.5 C#5:.5 D#5:1
F#5:1 E5:1 D#5:1
C#5:1 B4:1 A4:1
G#4:1 F#4:1 E4:1
F#4:1 D#4:2
E4:2 R:1''',
 lh='''C3+G3:3
A2+E3:2 R:1
F3:1 C3:1 A2:1
C3+G3:2 R:1
C3:1 G3:1 E3:1
F3:1 C4:1 A3:1
D3:1 A3:1 F3:1
G2:1 D3:1 F3:1
C3+E3+G3:2 R:1
C3:1 G3:1 E3:1
D3:1 A3:1 F3:1
B2:1 F#3:1 A3:1
C3+G3:2 R:1
E3:1 B3:1 G#3:1
B2:1 F#3:1 A3:1
E3+B3:1 R:2
B2:1 F#3:1 G#3:1
B2:1 D#3:1 F#3:1
C#3+E3+G#3:2 R:1
R:3
E3:1 B3:1 G#3:1
C#3:1 G#3:1 E3:1
B2:1 F#3:1 A3:1
A2:1 E3:1 C#3:1
F#2:1 C#3:1 A3:1
B2:1 F#3:1 A3:1
E3+G#3+B3:2 R:1
A2:1 E3:1 C#3:1
E3:1 B3:1 G#3:1
B2:1 F#3:1 D#3:1
C#3:1 G#3:1 E3:1
A2:1 E3:1 C#3:1
B2+D#3+A3:2 R:1
A2:1 E3:1 C#3:1
E3:1 B3:1 G#3:1
F#2:1 C#3:1 A3:1
A2:1 E3:1 C#3:1
E3:1 G#3:1 B3:1
B2:1 F#3:1 A3:1
E3+G#3+B3:2 R:1''',
 tempos=[58,59,58,56,60,61,60,59,57,60,61,60,57,60,61,58,59,60,58,58,60,61,62,61,60,59,58,62,63,64,62,61,59,60,61,60,59,58,58,58],
 phrases=[(1,4),(5,9),(10,13),(14,16),(17,19),(21,27),(28,33),(34,40)],sections={1:'pp',5:'p',10:'mp',14:'mp',16:'pp',17:'p',21:'p',28:'mp',30:'mf',32:'p',34:'p',38:'pp'},lower_sections={1:'pp',14:'p',16:'pp',21:'pp',28:'p',34:'pp'},
 pedal=[[i*3+.05,i*3+(.8 if i==15 else 1.8 if i in [1,3,8,12,18,26,32,39] else 2.8)] for i in range(40) if i!=19],hairpins=[('crescendo',21,25),('diminuendo',34,39)],page_starts=[9,17,25,33])
