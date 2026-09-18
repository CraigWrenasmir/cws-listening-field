"""Singing Returns, Op. 321–330: individually authored two-hand piano works."""
PIECES=[]

def song(*,op,title,key,fifths,meter,bpm,parent,source,motif,rh,lh,description,technical,tempos,phrases,sections,pedal=None,**extras):
    """Shared engraving defaults only; pitches, rhythms and forms are explicit."""
    n=len(rh.strip().splitlines());beats=int(meter.split('/')[0])*4/int(meter.split('/')[1])
    assert len(lh.strip().splitlines())==n and len(tempos)==n
    p=dict(op=op,title=title,key=key,fifths=fifths,meter=meter,bpm=bpm,parent_opus=parent,ancestry=source,motif=motif,rh=rh,lh=lh,
      description=description,difficulty='Lyrical advanced study',technical_note=technical,
      technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),
      system_starts=list(range(1,n+1,2)),page_starts=list(range(9,n+1,8)),
      engraving=dict(spacing_system=19,spacing_staff=19,pedal_offset_y=610),
      sections=sections,lower_sections={1:'p'},words={1:'cantabile'},slurs=phrases,lower_phrases=[],hairpins=[],tempo_changes={},group=3,final_fermata=False,
      performance=dict(rubato=tempos,phrase_arcs=[[(a-1)*beats,b*beats,3] for a,b in phrases],lower_entries=[],pedal_lift=.2,gate=.97,note='Authored phrase breathing and melodic voicing; independent rhythm is written in the score, with a shared tempo map.'),pedal_spans=sorted(pedal or []))
    p.update(extras)
    if p.get('meters'):
        lengths=[int(m.split('/')[0])*4/int(m.split('/')[1]) for m in p['meters']];assert len(lengths)==n
        offsets=[sum(lengths[:i]) for i in range(n+1)]
        p['performance']['phrase_arcs']=[[offsets[a-1],offsets[b],3] for a,b in phrases]
    PIECES.append(p)
    return p

song(op=321,title='Willow Cantilena',key='Eb',fifths=-3,meter='12/8',bpm=74,parent=292,
 source=dict(source_opus=292,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=6,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Eb','D','C','Bb']),
 description='A six-bar song returns three times over a quiet compound pulse: first direct, then embroidered, finally supported by a changed bass. A four-bar excursion supplies the single high point; the last return keeps its warmth and loses its final ornament.',
 technical='Carry long melody notes over a light bass-and-chord sway. The left hand relocates between groups; review its up-to-octave movement at the unhurried eighth-note rate. Ornament groups belong to the melodic breath.',
 rh='''Eb5:1.5 D5:.5 C5:1 Bb4:3
G4:1.5 Bb4:.5 C5:1 D5:1.5 Eb5:1.5
F5:3 Eb5:1 D5:.5 C5:1.5
Bb4:1.5 G4:1.5 Ab4:1 Bb4:.5 C5:1.5
D5:1.5 F5:1.5 Eb5:1.5 D5:.5 C5:1
Bb4:3 R:3
Eb5:1 D5:.25 Eb5:.25 D5:.5 C5:1 Bb4:3
G4:1 Bb4:.5 C5:1 D5:.5 Eb5:2 D5:.5 Eb5:.5
F5:2 G5:.5 F5:.5 Eb5:1 D5:.5 C5:1.5
Bb4:1.5 G4:1 Ab4:.5 Bb4:1 C5:.5 D5:1.5
F5:1.5 Eb5:.5 D5:1 C5:1.5 Bb4:1.5
G4:3 R:3
Ab4:1.5 C5:1.5 Eb5:3
F5:1.5 G5:1.5 Ab5:2 G5:.5 F5:.5
Eb5:1.5 D5:.5 C5:1 Bb4:1.5 A4:1.5
Bb4:3 R:3
Eb5:1.5 D5:.5 C5:1 Bb4:3
G4:1.5 Bb4:.5 C5:1 Eb5:2 D5:.5 C5:.5
F5:2 Eb5:.5 F5:.5 Eb5:1 D5:.5 C5:1.5
Bb4:1.5 G4:1.5 Ab4:1 Bb4:.5 C5:1.5
D5:1.5 C5:1.5 Bb4:1.5 G4:1.5
F4:1.5 G4:1.5 Eb4:3
G4:3 F4:1.5 Eb4:1.5
Eb4:4.5 R:1.5''',
 lh='''Eb3:.5 G3+Bb3:.5 G3+Bb3:.5 Bb2:.5 G3+Bb3:.5 G3+Bb3:.5 Eb3:.5 G3+Bb3:.5 G3+Bb3:.5 Bb2:.5 G3+Bb3:.5 G3+Bb3:.5
C3:.5 Eb3+G3:.5 Eb3+G3:.5 G2:.5 Eb3+G3:.5 Eb3+G3:.5 C3:.5 Eb3+G3:.5 Eb3+G3:.5 G2:.5 Eb3+G3:.5 Eb3+G3:.5
F3:.5 Ab3+C4:.5 Ab3+C4:.5 C3:.5 Ab3+C4:.5 Ab3+C4:.5 Bb2:.5 D3+Ab3:.5 D3+Ab3:.5 F3:.5 D3+Ab3:.5 D3+Ab3:.5
Eb3:.5 G3+Bb3:.5 G3+Bb3:.5 Bb2:.5 G3+Bb3:.5 G3+Bb3:.5 Ab2:.5 C3+G3:.5 C3+G3:.5 Eb3:.5 C3+G3:.5 C3+G3:.5
Bb2:.5 D3+Ab3:.5 D3+Ab3:.5 F3:.5 D3+Ab3:.5 D3+Ab3:.5 Bb2:.5 D3+Ab3:.5 D3+Ab3:.5 F3:.5 D3+Ab3:.5 D3+Ab3:.5
Eb3:1 G3+Bb3:.5 Bb2:1 G3+Bb3:.5 Eb3:1 G3+Bb3:.5 Bb2:1 R:.5
Eb3:.5 G3+Bb3:.5 G3+Bb3:.5 Bb2:.5 G3+Bb3:.5 G3+Bb3:.5 Eb3:.5 G3+Bb3:.5 G3+Bb3:.5 Bb2:.5 G3+Bb3:.5 G3+Bb3:.5
C3:1 Eb3+G3:.5 G2:1 Eb3+G3:.5 C3:1 Eb3+G3:.5 G2:1 Eb3+G3:.5
F3:.5 Ab3+C4:.5 Ab3+C4:.5 C3:.5 Ab3+C4:.5 Ab3+C4:.5 Bb2:.5 D3+Ab3:.5 D3+Ab3:.5 F3:.5 D3+Ab3:.5 D3+Ab3:.5
Eb3:1 G3+Bb3:.5 Bb2:1 G3+Bb3:.5 Ab2:1 C3+G3:.5 Eb3:1 C3+G3:.5
Bb2:.5 D3+Ab3:.5 D3+Ab3:.5 F3:.5 D3+Ab3:.5 D3+Ab3:.5 G2:.5 B2+F3:.5 B2+F3:.5 D3:.5 B2+F3:.5 B2+F3:.5
C3:1 Eb3+G3:.5 G2:1 Eb3+G3:.5 C3:1 Eb3+G3:.5 G2:1 R:.5
Ab2:1 C3+Eb3:.5 Eb3:1 Ab3+C4:.5 Ab2:1 C3+Eb3:.5 Eb3:1 Ab3+C4:.5
Db3:1 F3+Ab3:.5 Ab2:1 F3+Ab3:.5 Db3:1 F3+Ab3:.5 Ab2:1 F3+Ab3:.5
F3:1 Ab3+C4:.5 C3:1 Ab3+C4:.5 F3:1 A3+C4:.5 C3:1 A3+C4:.5
Bb2:1 D3+Ab3:.5 F3:1 D3+Ab3:.5 Bb2:1 D3+Ab3:.5 F3:1 R:.5
C3:1 Eb3+G3:.5 G2:1 Eb3+G3:.5 C3:1 Eb3+G3:.5 G2:1 Eb3+G3:.5
Ab2:1 C3+G3:.5 Eb3:1 C3+G3:.5 Ab2:1 C3+G3:.5 Eb3:1 C3+G3:.5
F3:1 Ab3+C4:.5 C3:1 Ab3+C4:.5 Bb2:1 D3+Ab3:.5 F3:1 D3+Ab3:.5
G2:1 D3+F3:.5 Bb2:1 D3+F3:.5 Ab2:1 C3+G3:.5 Eb3:1 C3+G3:.5
Bb2:1 D3+Ab3:.5 F3:1 D3+Ab3:.5 Bb2:1 D3+Ab3:.5 F3:1 D3+Ab3:.5
Eb3:1 G3+Bb3:.5 Bb2:1 G3+Bb3:.5 Eb3:1 G3+Bb3:.5 Bb2:1 G3+Bb3:.5
Ab2:1 C3+Eb3:.5 Eb3:1 C3+Eb3:.5 Bb2:1 D3+Ab3:.5 F3:1 D3+Ab3:.5
Eb3+G3+Bb3:4.5 R:1.5''',
 tempos=[74,75,75,74,73,70,74,75,76,74,73,70,75,78,75,71,74,75,74,73,72,71,69,67],
 phrases=[(1,3),(4,6),(7,9),(10,12),(13,16),(17,19),(20,22),(23,24)],sections={1:'p',7:'mp',13:'mp',14:'f',15:'mp',17:'p',23:'pp'},lower_sections={1:'pp',13:'p',17:'pp'},
 hairpins=[('crescendo',1,3),('diminuendo',4,6),('crescendo',13,14),('diminuendo',14,16)],
 technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=12),
 pedal=[[i*6+.05,i*6+2.85] for i in range(23)]+[[i*6+3.05,i*6+5.45] for i in range(23)]+[[138.05,142.4]])
song(op=322,title='Myrtle Reverie',key='d',fifths=-1,meter='6/8',bpm=48,parent=291,
 source=dict(source_opus=291,source_hand='lh',source_start_beat=0,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['D','F','E','A']),
 description='A minor-key song breathes across a small six-eight current. Its three-plus-five-bar opening returns first with turns and then with a late arrival above a brighter bass. Two short interludes expand the yearning without replacing the tune; the last note is left unaccompanied.',
 technical='Keep the left arpeggio light and even while tied melody notes span the bar line. The delayed third statement is explicitly written. Shape the small sixteenths as part of the line and clear the pedal before the final exposed note.',
 rh='''D5:1 F5:.5 E5:.5 A5:1
G5:.5 F5:.5 E5:1 D5:1
C5:1.5 E5:.5 D5:1~
D5:2 R:1
R:.5 A4:.5 C5:.5 D5:.5 E5:1
F5:1 E5:.5 D5:.5 C5:1
Bb4:1.5 A4:.5 G4:1
A4:2 R:1
Bb4:1 D5:.5 F5:.5 E5:1
D5:1 C5:.5 Bb4:.5 A4:1
G4:1 Bb4:.5 A4:.5 G4:.5 E4:.5
A4:1.5 C#5:.5 E5:1
D5:.75 F5:.25 E5:.5 A5:1.5
G5:.5 F5:.25 E5:.25 F5:.5 E5:.5 D5:1
C5:1.5 E5:.25 F5:.25 E5:.5 D5:.5~
D5:2 R:1
R:.5 A4:.25 Bb4:.25 C5:.5 D5:.5 E5:1
F5:1 E5:.5 D5:.25 E5:.25 C5:1
Bb4:1 A4:.5 G4:.5 F4:.5 E4:.5
A4:2 R:1
G5:1 F5:.5 E5:.5 D5:1
E5:1 G5:.5 A5:.5 Bb5:1
A5:.5 G5:.5 F5:1 E5:1
C#5:1 E5:.5 D5:.5 C#5:.5 A4:.5
R:.5 D5:.5 F5:.5 E5:.5 A5:1
G5:.5 F5:.5 E5:1 D5:1
C5:1 E5:.5 D5:1.5~
D5:2 R:1
R:.5 A4:.5 C5:.5 D5:.5 E5:1
F5:1 E5:.5 D5:.5 C5:1
Bb4:1 A4:.5 G4:.5 E4:1
D5:2 R:1''',
 lh='''D3:.5 F3:.5 A3:.5 F3:.5 E3:.5 D3:.5
Bb2:.5 D3:.5 F3:.5 D3:.5 C3:.5 D3:.5
C3:.5 E3:.5 G3:.5 E3:.5 D3:.5 E3:.5
D3:.5 F3:.5 A3:.5 F3:.5 E3:.5 R:.5
A2:.5 E3:.5 G3:.5 E3:.5 C#3:.5 E3:.5
D3:.5 F3:.5 A3:.5 F3:.5 E3:.5 D3:.5
G2:.5 D3:.5 F3:.5 D3:.5 Bb2:.5 D3:.5
A2:.5 E3:.5 G3:.5 E3:.5 C#3:.5 R:.5
Bb2:.5 D3:.5 F3:.5 D3:.5 A2:.5 D3:.5
F3:.5 A3:.5 C4:.5 A3:.5 G3:.5 F3:.5
G3:.5 Bb3:.5 D4:.5 Bb3:.5 G3:.5 E3:.5
A2:.5 E3:.5 G3:.5 E3:.5 C#3:.5 E3:.5
D3:.5 F3:.5 A3:.5 F3:.5 E3:.5 D3:.5
Bb2:.5 D3:.5 F3:.5 D3:.5 C3:.5 D3:.5
C3:.5 E3:.5 G3:.5 E3:.5 D3:.5 E3:.5
D3:.5 F3:.5 A3:.5 F3:.5 E3:.5 R:.5
A2:.5 E3:.5 G3:.5 E3:.5 C#3:.5 E3:.5
D3:.5 F3:.5 A3:.5 F3:.5 E3:.5 D3:.5
G2:.5 D3:.5 F3:.5 D3:.5 Bb2:.5 D3:.5
A2:.5 E3:.5 G3:.5 E3:.5 C#3:.5 R:.5
C3:.5 E3:.5 G3:.5 E3:.5 D3:.5 E3:.5
G3:.5 Bb3:.5 D4:.5 Bb3:.5 A3:.5 G3:.5
F3:.5 A3:.5 C4:.5 A3:.5 G3:.5 F3:.5
A2:.5 C#3:.5 E3:.5 G3:.5 E3:.5 C#3:.5
Bb2:.5 D3:.5 F3:.5 A3:.5 F3:.5 D3:.5
G2:.5 B2:.5 D3:.5 F3:.5 D3:.5 B2:.5
C3:.5 E3:.5 G3:.5 E3:.5 D3:.5 E3:.5
D3:.5 F3:.5 A3:.5 F3:.5 E3:.5 R:.5
A2:.5 E3:.5 G3:.5 E3:.5 C#3:.5 E3:.5
D3:.5 F3:.5 A3:.5 F3:.5 E3:.5 D3:.5
G2:.5 D3:.5 F3:.5 A2:.5 C#3:.5 E3:.5
R:3''',
 tempos=[48,49,48,46,48,49,48,46,49,50,49,47,48,49,49,46,48,49,48,46,50,52,49,46,48,49,48,46,48,47,46,47],
 phrases=[(1,3),(5,8),(9,12),(13,15),(17,20),(21,24),(25,27),(29,32)],sections={1:'p',9:'mp',13:'p',21:'mf',22:'f',23:'mp',25:'p',29:'pp'},lower_sections={1:'pp',9:'p',13:'pp',21:'p',25:'pp'},
 pedal=[[i*3+.05,i*3+2.4] for i in range(31)],hairpins=[('crescendo',21,22),('diminuendo',23,24)])
song(op=323,title='Amber Promenade',key='F',fifths=-1,meter='4/4',bpm=54,parent=296,
 source=dict(source_opus=296,source_hand='lh',source_start_beat=0,source_end_beat=4,source_pitches=['F','E','D','C'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['F','E','D','C']),
 description='A clear F-major song learns to lean against offbeat chords. The second statement enters late and grows small dotted turns; a flat-side bridge leads to one bright crest. The last statement keeps the original outline over warmer ninths and ends on the major seventh.',
 technical='Distinguish the sustained melody from the clipped accompaniment. Dotted pairs are written, not an automatic swing effect. Keep the chromatic approach tones soft and release short left-hand chords with the notated rests.',
 rh='''F5:1 E5:.5 D5:.5 C5:2
A4:1 C5:1 D5:1 E5:1
G5:2 F5:.75 E5:.25 D5:1
C5:3 R:1
Bb4:1 D5:.75 E5:.25 F5:2
E5:1 D5:.5 C5:.5 A4:2
G4:1 Bb4:1 A4:1 G4:1
C5:2 R:2
R:.5 F5:.75 E5:.25 D5:.5 C5:2
A4:.75 Bb4:.25 C5:1 D5:1 E5:1
G5:1 A5:.25 G5:.25 F5:.5 E5:.75 D5:.25 E5:1
C5:2.5 R:1.5
Bb4:.75 C5:.25 D5:.75 E5:.25 F5:2
E5:1 D5:.75 C5:.25 A4:1 G4:.75 A4:.25
G4:1 Bb4:.75 A4:.25 G4:1 E4:1
C5:2 R:2
G5:2 F5:1 Eb5:1
C5:1 Eb5:.75 F5:.25 G5:2
A5:1 Bb5:.75 A5:.25 G5:1 F5:1
E5:1 D5:.75 Db5:.25 C5:1 R:1
F5:1 E5:.5 D5:.5 C5:2
A4:1 C5:1 D5:.75 E5:.25 F5:1
G5:2 F5:.75 E5:.25 D5:1
C5:2 Bb4:1 A4:1
Bb4:1 D5:.75 E5:.25 F5:2
E5:1 D5:1 C5:1 A4:1
G4:1 Bb4:1 C5:1 D5:1
E5:3 R:1''',
 lh='''F3:1 R:.5 A3+C4:.5 R:.5 G3+C4:.5 A3+C4:1
D3:1 R:.5 F3+C4:.5 R:.5 F3+A3:.5 E3+A3:1
G3:1 R:.5 Bb3+D4:.5 R:.5 A3+D4:.5 Bb3+D4:1
C3:1 R:.5 E3+Bb3:.5 R:2
Bb2:1 R:.5 D3+A3:.5 R:.5 F3+A3:.5 D3+A3:1
A2:1 R:.5 E3+G3:.5 R:.5 C3+G3:.5 E3+G3:1
G2:1 R:.5 D3+F3:.5 C3:1 E3+Bb3:1
C3:1 E3+Bb3:1 R:2
F3:1 R:.5 A3+C4:.5 R:.5 G3+C4:.5 A3+C4:1
D3:1 R:.5 F3+C4:.5 R:.5 F3+A3:.5 E3+A3:1
G3:1 R:.5 Bb3+D4:.5 R:.5 A3+D4:.5 Bb3+D4:1
C3:1 R:.5 E3+Bb3:.5 R:2
Bb2:1 R:.5 D3+A3:.5 R:.5 F3+A3:.5 D3+A3:1
A2:1 R:.5 E3+G3:.5 R:.5 C3+G3:.5 E3+G3:1
G2:1 R:.5 D3+F3:.5 C3:1 E3+Bb3:1
F3:1 A3+C4:1 R:2
Eb3:1 R:.5 G3+Bb3:.5 R:.5 F3+Bb3:.5 G3+Bb3:1
Ab2:1 R:.5 C3+G3:.5 R:.5 Eb3+G3:.5 C3+G3:1
G3:1 Bb3+D4:1 C3:1 E3+Bb3:1
C3:1 E3+Bb3:1 R:2
D3:1 R:.5 F3+A3:.5 R:.5 E3+A3:.5 F3+A3:1
G3:1 R:.5 B3+D4:.5 R:.5 A3+D4:.5 B3+D4:1
G3:1 R:.5 F3+Bb3:.5 C3:1 E3+Bb3:1
F3:1 R:.5 A3+C4:.5 R:.5 G3+C4:.5 A3+C4:1
Bb2:1 R:.5 D3+A3:.5 R:.5 F3+A3:.5 D3+A3:1
A2:1 E3+G3:1 D3:1 F3+C4:1
G2:1 D3+F3:1 C3:1 E3+Bb3:1
F3+A3+C4:3 R:1''',
 tempos=[54,55,56,52,54,55,54,51,54,56,57,52,54,55,54,51,55,57,58,52,54,55,55,53,54,53,52,50],phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28)],sections={1:'p',9:'mp',17:'mp',19:'f',20:'p',21:'mp',25:'p',28:'pp'},lower_sections={1:'pp',17:'p',21:'pp'},pedal=[[108.05,110.85]],hairpins=[('crescendo',17,19),('diminuendo',25,28)])
song(op=324,title='Birch Aubade',key='A',fifths=3,meter='3/4',bpm=54,parent=305,
 source=dict(source_opus=305,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','G#','F#','E'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','G#','F#','E']),
 description='A morning waltz lets a descending song cross the dance pulse. Two brief minor-coloured windows separate three statements. The second acquires a small turn, the third moves above a descending bass, and a quiet four-bar coda keeps only the final three notes.',
 technical='Keep the bass buoyant and the repeated chords subordinate. Sustain ties without a fresh accent at the bar line. The melody should retain its identity through the changed bass and the small sixteenth-note turns.',
 rh='''A4:1 G#4:.5 F#4:.5 E4:1
C#5:.5 B4:.5 A4:2
B4:1 D5:1 C#5:1~
C#5:1 B4:1 R:1
E5:1 F#5:.5 E5:.5 C#5:1
D5:1 C#5:.5 B4:.5 A4:1
G#4:.5 A4:.5 B4:1 G#4:1
A4:2 R:1
C5:1 E5:1 D5:1
C5:1 A4:1 G4:1
F4:1 A4:.5 B4:.5 C5:1
B4:1 G#4:1 R:1
A4:.75 B4:.25 A4:.5 G#4:.5 F#4:.5 E4:.5
C#5:.5 B4:.25 A4:.25 B4:.5 A4:1.5
B4:1 D5:.75 E5:.25 C#5:1~
C#5:1 B4:1 R:1
E5:1 F#5:.25 G#5:.25 F#5:.5 E5:.5 C#5:.5
D5:1 C#5:.5 B4:.5 A4:1
G#4:.5 A4:.5 B4:.75 A4:.25 G#4:1
A4:2 R:1
C#5:1 E5:1 F#5:1
E5:1 D5:1 C#5:1
B4:.5 D5:.5 F#5:1 G#5:1
F#5:1 E5:1 R:1
A4:1 G#4:.5 F#4:.5 E4:1
C#5:.5 B4:.5 A4:2
B4:1 D5:1 C#5:1~
C#5:1 B4:1 R:1
E5:1 F#5:.5 E5:.5 C#5:1
D5:1 C#5:.5 B4:.5 A4:1
G#4:.5 A4:.5 B4:1 G#4:1
A4:2 R:1
C#5:2 B4:1
A4:1 G#4:1 F#4:1
E4:2 C#4:1
E4:3''',
 lh='''A2:1 E3+A3:1 E3+G#3:1
F#2:1 C#3+A3:1 E3+A3:1
B2:1 F#3+A3:1 F#3+A3:1
E3:1 G#3+D4:1 R:1
A2:1 E3+A3:1 E3+G#3:1
D3:1 F#3+A3:1 F#3+A3:1
E3:1 G#3+B3:1 G#3+D4:1
A2:1 E3+A3:1 R:1
F3:1 A3+C4:1 A3+C4:1
C3:1 E3+G3:1 E3+G3:1
D3:1 F3+A3:1 F3+A3:1
E3:1 G#3+B3:1 R:1
A2:1 E3+A3:1 E3+G#3:1
F#2:1 C#3+A3:1 E3+A3:1
B2:1 F#3+A3:1 F#3+A3:1
E3:1 G#3+D4:1 R:1
A2:1 E3+A3:1 E3+G#3:1
D3:1 F#3+A3:1 F#3+A3:1
E3:1 G#3+B3:1 G#3+D4:1
A2:1 E3+A3:1 R:1
F#2:1 C#3+A3:1 E3+A3:1
B2:1 D3+A3:1 F#3+A3:1
E3:1 G#3+B3:1 G#3+D4:1
E3:1 G#3+D4:1 R:1
A3:1 C#3+E3:1 C#3+E3:1
G#3:1 C#3+E3:1 C#3+E3:1
F#3:1 B2+D3:1 B2+D3:1
E3:1 B2+D3:1 R:1
D3:1 F#3+A3:1 E3+A3:1
D3:1 F#3+A3:1 F#3+A3:1
E3:1 G#3+B3:1 G#3+D4:1
A2:1 E3+A3:1 R:1
F#2:1 C#3+A3:1 E3+A3:1
D3:1 F#3+A3:1 C#3+G#3:1
B2:1 E3+G#3:1 B2+D3:1
A2+C#3+A3:3''',
 tempos=[54,55,55,52,55,56,54,51,53,54,53,50,54,55,56,52,55,56,54,51,55,56,58,52,54,55,55,52,54,54,53,51,52,51,50,49],phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32),(33,36)],sections={1:'p',9:'pp',13:'mp',21:'mp',23:'f',24:'p',25:'p',33:'pp'},lower_sections={1:'pp',21:'p',25:'pp'},
 pedal=[[i*3+.05,i*3+(1.85 if i+1 in [4,8,12,16,20,24,28,32] else 2.85)] for i in range(36)],hairpins=[('crescendo',21,23),('diminuendo',33,36)])
song(op=325,title='Sedge Lantern',key='c',fifths=-3,meter='9/8',bpm=60,parent=306,
 source=dict(source_opus=306,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['G','F','D','C'],transposition_semitones=5),motif=dict(hand='rh',start_beat=0,end_beat=4.5,pitches=['C','Bb','G','F']),
 description='A nine-eight lantern song holds its questioning fourth before resolving. Three statements move from plain melody through delicate turns to a quieter, partly stripped return. A six-bar middle climbs through chromatic bass notes towards one high C, then makes room for the tune again.',
 technical='Hear three broad pulses without stressing every bass arrival. Let the upper fourth lean gently into the next bar. Long pedal spans are split where the harmony moves, and all melodic turns are fully written.',
 rh='''C5:.5 Bb4:1 G4:1 F4:2
Eb4:1.5 G4:.5 Bb4:1 C5:1.5
D5:2 Eb5:.5 D5:.5 C5:1.5
Bb4:1.5 G4:1.5 R:1.5
Ab4:1.5 C5:1 D5:.5 Eb5:1.5
D5:1.5 B4:1 C5:2
G5:1.5 F5:1.5 Eb5:1.5
D5:1.5 B4:1.5 R:1.5
C5:.5 Bb4:.75 A4:.25 G4:1 F4:2
Eb4:1 G4:.5 Bb4:.5 C5:1 D5:.5 C5:1
D5:1.5 Eb5:.25 F5:.25 Eb5:.5 D5:.5 C5:1.5
Bb4:1 G4:.5 Ab4:.5 G4:.5 F4:1.5 R:.5
Ab4:1 C5:.5 D5:.5 Eb5:1 F5:.5 Eb5:1
D5:1.5 B4:.75 C5:.25 D5:.5 C5:1.5
Eb5:1.5 G5:1.5 F5:1.5
E5:1.5 F5:1.5 Ab5:1.5
G5:1.5 F5:1.5 Eb5:1.5
F5:1 G5:.5 Ab5:1.5 C6:1.5
Bb5:.5 Ab5:.5 G5:.5 F5:1.5 Eb5:1.5
D5:1.5 B4:1.5 R:1.5
C5:.5 Bb4:1 G4:1 F4:2
Eb4:1.5 G4:.5 Bb4:1 C5:1.5
D5:2 Eb5:.5 D5:.5 C5:1.5
Bb4:1.5 G4:1.5 R:1.5
Ab4:1.5 C5:1 D5:.5 Eb5:1.5
D5:1.5 B4:1 C5:2
G4:1.5 F4:1.5 Eb4:1.5
D4:1.5 C4:2 R:1''',
 lh='''C3:.5 Eb3+G3:1 G2:.5 Eb3+Bb3:1 C3:.5 Eb3+G3:1
Ab2:.5 C3+G3:1 Eb3:.5 C3+G3:1 Ab2:.5 C3+G3:1
F3:.5 Ab3+C4:1 Bb2:.5 D3+Ab3:1 Eb3:.5 G3+Bb3:1
G2:.5 D3+F3:1 G2:.5 D3+F3:1 R:1.5
Ab2:.5 C3+Eb3:1 F3:.5 Ab3+C4:1 F3:.5 Ab3+C4:1
G2:.5 D3+F3:1 G2:.5 B2+F3:1 C3:.5 Eb3+G3:1
Eb3:.5 G3+Bb3:1 D3:.5 F3+Bb3:1 C3:.5 Eb3+G3:1
G2:.5 B2+F3:1 G2:.5 D3+F3:1 R:1.5
C3:.5 Eb3+G3:1 G2:.5 Eb3+Bb3:1 C3:.5 Eb3+G3:1
Ab2:.5 C3+G3:1 Eb3:.5 C3+G3:1 Ab2:.5 C3+G3:1
F3:.5 Ab3+C4:1 Bb2:.5 D3+Ab3:1 Eb3:.5 G3+Bb3:1
G2:.5 D3+F3:1 G2:.5 D3+F3:1 R:1.5
Ab2:.5 C3+Eb3:1 F3:.5 Ab3+C4:1 F3:.5 Ab3+C4:1
G2:.5 B2+F3:1 D3:.5 B2+F3:1 C3:.5 Eb3+G3:1
Ab2:.5 C3+G3:1 Eb3:.5 C3+G3:1 Ab2:.5 C3+G3:1
A2:.5 C3+F3:1 F3:.5 A3+C4:1 F3:.5 A3+C4:1
Bb2:.5 D3+Ab3:1 F3:.5 D3+Ab3:1 Bb2:.5 D3+Ab3:1
B2:.5 D3+Ab3:1 F3:.5 D3+Ab3:1 C3:.5 Eb3+G3:1
Ab2:.5 C3+G3:1 F3:.5 Ab3+C4:1 F3:.5 Ab3+C4:1
G2:.5 B2+F3:1 D3:.5 B2+F3:1 R:1.5
Ab2:.5 C3+G3:1 Eb3:.5 C3+G3:1 Ab2:.5 C3+G3:1
C3:.5 Eb3+G3:1 G2:.5 Eb3+Bb3:1 C3:.5 Eb3+G3:1
F3:.5 Ab3+C4:1 Bb2:.5 D3+Ab3:1 Eb3:.5 G3+Bb3:1
G2:.5 D3+F3:1 G2:.5 D3+F3:1 R:1.5
Ab2:.5 C3+Eb3:1 F3:.5 Ab3+C4:1 F3:.5 Ab3+C4:1
G2:.5 B2+F3:1 D3:.5 B2+F3:1 C3:.5 Eb3+G3:1
Ab2:.5 C3+Eb3:1 Bb2:.5 D3+Ab3:1 G2:.5 B2+F3:1
C3+Eb3+G3:3.5 R:1''',
 tempos=[60,61,62,58,60,59,60,57,60,62,62,59,61,60,61,63,64,65,61,57,59,60,61,57,59,58,56,55],phrases=[(1,4),(5,6),(7,8),(9,12),(13,14),(15,18),(19,20),(21,24),(25,28)],sections={1:'p',9:'mp',15:'mp',18:'f',19:'mp',21:'p',25:'pp'},lower_sections={1:'pp',15:'p',21:'pp'},
 pedal=[[i*4.5+j+.05,i*4.5+j+1.35] for i in range(27) for j in [0,1.5,3] if not(i+1 in [4,8,12,20,24] and j==3)]+[[121.55,124.85]],hairpins=[('crescendo',15,18),('diminuendo',19,20)])
p=song(op=326,title='Iris Portico',key='Db',fifths=-5,meter='4/4',bpm=60,parent=297,
 source=dict(source_opus=297,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['Db','C','Bb','Ab'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=4,pitches=['Db','C','Bb','Ab']),
 description='The left hand sings beneath quiet upper chords. Its first eight-bar statement is plain, the second decorated, and the last keeps the melody while the right-hand harmony moves through borrowed colours. A short high-register opening in the middle brightens the texture before the song returns to its original register.',
 technical='Bring out the left-hand line without making the upper chords heavy. Keep the two hands on separate keys; the melody briefly changes clef near its high point. Short written gaps in the accompaniment allow the long line to remain audible.',
 lh='''Db4:1 C4:.5 Bb3:.5 Ab3:2
F3:1 Ab3:.5 Bb3:.5 C4:2
Eb4:2 Db4:.5 C4:.5 Bb3:1
Ab3:3 R:1
Gb3:1 Bb3:.5 C4:.5 Db4:2
C4:1 Ab3:1 Gb3:1 F3:1
Eb3:1 F3:1 Ab3:1 Bb3:1
Ab3:3 R:1
Bb3:2 Db4:1 Eb4:1
C4:2 Bb3:1 Ab3:1
Gb3:1 Bb3:1 Db4:2
C4:2 Ab3:1 R:1
Db4:.75 Eb4:.25 Db4:.5 C4:.5 Bb3:.5 Ab3:1.5
F3:1 Ab3:.5 Bb3:.25 C4:.25 Db4:.5 C4:1.5
Eb4:1 F4:.5 Eb4:.5 Db4:.5 C4:.5 Bb3:1
Ab3:2 Bb3:.5 Ab3:.5 R:1
Gb3:1 Bb3:.5 C4:.25 Db4:.25 Eb4:.5 Db4:1.5
C4:1 Ab3:.75 Gb3:.25 F3:1 Ab3:1
Eb3:1 F3:.5 Gb3:.5 Ab3:.5 Bb3:.5 C4:1
Ab3:3 R:1
Bb3:1 Db4:1 Eb4:2
F4:2 Eb4:1 Db4:1
C4:1 Bb3:1 Ab3:1 Gb3:1
Eb3:1 G3:1 Ab3:1 R:1
Db4:1 C4:.5 Bb3:.5 Ab3:2
F3:1 Ab3:.5 Bb3:.5 C4:2
Eb4:2 Db4:.5 C4:.5 Bb3:1
Ab3:3 R:1
Gb3:1 Bb3:.5 C4:.5 Db4:2
C4:1 Ab3:1 Gb3:1 F3:1
Eb3:1 F3:1 Ab3:1 C4:1
Db4:3 R:1''',
 rh='''F4+Ab4+Db5:2 Eb4+Ab4+C5:2
F4+Bb4+Db5:2 R:1 F4+Ab4+C5:1
Gb4+Bb4+Eb5:2 E4+Ab4+C5:2
F4+Ab4+Db5:2 R:2
Gb4+Bb4+Db5:2 F4+Ab4+Db5:2
Eb4+Ab4+C5:2 R:1 F4+Ab4+Db5:1
Gb4+Bb4+Eb5:2 G4+Bb4+Db5:2
Gb4+Ab4+C5:3 R:1
Gb4+Bb4+Db5:2 F4+Bb4+Db5:2
Eb4+Ab4+C5:2 Eb4+Gb4+C5:2
Gb4+Bb4+Db5:2 F4+Bb4+Db5:2
Gb4+Ab4+C5:3 R:1
F4+Ab4+Db5:2 Eb4+Ab4+C5:2
F4+Bb4+Db5:2 R:1 F4+Ab4+C5:1
Gb4+Bb4+Eb5:2 E4+Ab4+C5:2
F4+Ab4+Db5:2 R:2
Gb4+Bb4+Db5:2 F4+Ab4+Db5:2
Eb4+Ab4+C5:2 R:1 F4+Ab4+Db5:1
Gb4+Bb4+Eb5:2 G4+Bb4+Db5:2
Gb4+Ab4+C5:3 R:1
Gb4+Bb4+Eb5:2 Ab4+Db5+F5:2
Ab4+Db5+F5:2 Ab4+C5+Eb5:2
Gb4+Bb4+Eb5:2 Gb4+Bb4+Db5:2
G4+Bb4+Db5:3 R:1
F4+Bb4+Db5:2 F4+Ab4+C5:2
Fb4+Ab4+Cb5:2 R:1 Eb4+Ab4+Cb5:1
Gb4+Bb4+Eb5:2 E4+Ab4+C5:2
F4+Ab4+Db5:2 R:2
Gb4+Bb4+Db5:2 F4+Ab4+Db5:2
Eb4+Ab4+C5:2 R:1 F4+Ab4+Db5:1
Gb4+Bb4+Eb5:2 Gb4+Ab4+C5:2
F4+Ab4+Eb5:3 R:1''',
 tempos=[60,61,61,58,60,61,59,57,61,62,60,57,60,62,62,58,61,62,60,57,62,64,60,56,59,60,60,57,59,58,57,55],phrases=[],lower_phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32)],sections={1:'pp',21:'p',25:'pp'},lower_sections={1:'mp',9:'p',13:'mp',21:'mf',22:'f',23:'mp',25:'p',29:'pp'},clef_changes={'lh':{21:'treble',23:'bass'}},
 pedal=[[i*4+.05,i*4+1.85] for i in range(32)]+[[i*4+2.05,i*4+2.85] for i in range(32) if i+1 not in [4,16,28]],hairpins=[])
p['performance']['lower_entries']=[[0,128]]
p['performance']['phrase_arcs']=[[a*4,b*4,4] for a,b in [(0,4),(4,8),(8,12),(12,16),(16,20),(20,24),(24,28),(28,32)]]
song(op=327,title='Clover Reverie',key='G',fifths=1,meter='6/8',bpm=48,parent=294,
 source=dict(source_opus=294,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['G','F#','E','D'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['G','F#','E','D']),
 description='A small major-key song floats above widely spaced, quiet bells. Its decorated second return reaches the highest note without becoming loud. At the third return the accompaniment disappears for four bars: the same tune is suddenly exposed, before a descending bass gathers it home.',
 technical='Let the sparse bass intervals resonate without making the pulse heavy. The high point is marked only mezzo-forte. Preserve the line through the four unaccompanied bars and avoid accelerating when the accompaniment falls away.',
 rh='''G5:1 F#5:.5 E5:.5 D5:1
B4:1 D5:.5 E5:.5 F#5:1
A5:1 G5:.5 F#5:.5 E5:1
D5:2 R:1
C5:1 E5:.5 G5:.5 F#5:1
E5:1 D5:.5 C5:.5 B4:1
A4:1 C5:1 B4:.5 A4:.5
D5:2 R:1
Eb5:1 G5:.5 F5:.5 Eb5:1
D5:1 C5:.5 Bb4:.5 A4:1
G4:1 Bb4:.5 C5:.5 D5:1
F#5:1 E5:.5 D5:.5 C5:1
G5:.75 F#5:.25 E5:.5 D5:1.5
B4:.75 C5:.25 D5:.5 E5:.5 F#5:1
A5:1 B5:.25 A5:.25 G5:.5 F#5:.5 E5:.5
D5:2 R:1
C5:.75 D5:.25 E5:.5 G5:.5 A5:1
B5:.5 C6:.5 D6:1 C6:.5 B5:.5
A5:.5 G5:.5 F#5:1 E5:.5 D5:.5
D5:2 R:1
B4:1 A4:.5 G4:.5 F#4:1
E4:1 G4:1 B4:1
C5:1 B4:.5 A4:.5 G4:1
F#4:1 A4:.5 C5:.5 D5:1
G5:1 F#5:.5 E5:.5 D5:1
B4:1 D5:.5 E5:.5 F#5:1
A5:1 G5:.5 F#5:.5 E5:1
D5:2 R:1
C5:1 E5:.5 G5:.5 F#5:1
E5:1 D5:.5 C5:.5 B4:1
A4:1 C5:1 B4:.5 A4:.5
G4:2 R:1
A4:1 G4:.5 F#4:.5 E4:1
G4:2 R:1''',
 lh='''G2+D3:1.5 R:.5 B2+F#3:1
E3+B3:1.5 R:.5 D3+A3:1
C3+G3:1.5 R:.5 A2+E3:1
D3+A3:2 R:1
C3+G3:1.5 R:.5 D3+A3:1
E3+B3:1.5 R:.5 G2+D3:1
A2+E3:1.5 R:.5 C3+F#3:1
D3+A3:2 R:1
Eb3+Bb3:1.5 R:.5 C3+G3:1
Bb2+F3:1.5 R:.5 D3+A3:1
G2+D3:1.5 R:.5 Eb3+Bb3:1
D3+A3:2 R:1
G2+D3:1.5 R:.5 B2+F#3:1
E3+B3:1.5 R:.5 D3+A3:1
C3+G3:1.5 R:.5 A2+E3:1
D3+A3:2 R:1
C3+G3:1.5 R:.5 A2+E3:1
G2+D3:1.5 R:.5 B2+F#3:1
C3+G3:1.5 R:.5 A2+E3:1
D3+A3:2 R:1
G3:1 F#3:1 E3:1
C3:1 D3:1 E3:1
A2:1 B2:1 C3:1
D3:2 R:1
R:3
R:3
R:3
R:3
C3+G3:1.5 R:.5 B2+F#3:1
A2+E3:1.5 R:.5 G2+D3:1
C3+G3:1.5 R:.5 D3+A3:1
G2+B2+D3:2 R:1
C3+E3:1.5 D3+F#3:1.5
G2+B2+D3:2 R:1''',
 tempos=[48,49,48,46,48,49,48,46,49,49,48,47,48,49,49,46,49,50,48,46,48,48,47,46,48,49,48,46,48,47,46,45,45,43],
 phrases=[(1,3),(5,8),(9,12),(13,15),(17,20),(21,24),(25,27),(29,32),(33,34)],sections={1:'p',9:'mp',13:'p',17:'mp',18:'mf',19:'p',25:'pp'},lower_sections={1:'pp',21:'p',29:'pp'},
 hairpins=[('crescendo',17,18),('diminuendo',19,20)],
 pedal=[[i*3+.05,i*3+(1.9 if i in [3,7,11,15,19,23] else 2.4)] for i in range(24)]+[[i*3+.05,i*3+(1.9 if i in [31,33] else 2.4)] for i in range(28,34)])
song(op=328,title='Reed Noctilucence',key='b',fifths=2,meter='5/4',bpm=60,parent=295,
 source=dict(source_opus=295,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['B','D','C#','F#'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['B','D','C#','F#']),
 description='A song in five lets the melody lean past the accompaniment. Its six-bar statements retain the same outline while the supporting pulse changes from three-plus-two to two-plus-three, then becomes a slow descending ground. Chromatic neighbours lead to one brief, luminous crest before the last return settles into a soft minor close.',
 technical='Hear the five beats as a flexible long breath. Keep the melody continuous when the accompaniment changes grouping. The sixteenth-note turns are written explicitly; place the returning tune quietly above the falling bass.',
 rh='''B4:1 D5:.5 C#5:.5 F#5:3
E5:1.5 D5:.5 C#5:1 B4:2
A4:2 C#5:1 D5:1 E5:1
F#5:2 E5:1 D5:.5 C#5:.5 B4:1
G4:1 B4:1 D5:2 C#5:1
B4:3 R:2
G5:2 F#5:1 E5:1 D5:1
C#5:2 A#4:1 B4:1 R:1
B4:.75 D5:.25 C#5:.5 F#5:2.5 E5:.5 F#5:.5
E5:1 D5:.5 E5:.25 D5:.25 C#5:1 B4:2
A4:1.5 C#5:.5 D5:1 E5:1 F#5:.5 E5:.5
F#5:1 G5:.5 F#5:.5 E5:1 D5:.5 C#5:.5 B4:1
G4:1 B4:.5 C#5:.5 D5:2 C#5:.5 B4:.5
B4:3 R:2
G5:1 A5:1 B5:.5 C#6:.5 B5:1 A5:.5 G5:.5
F#5:1 E5:.5 D5:.5 C#5:1 A#4:1 R:1
R:.5 B4:.5 D5:.5 C#5:.5 F#5:3
E5:1.5 D5:.5 C#5:1 B4:2
A4:2 C#5:1 D5:1 E5:1
F#5:2 E5:1 D5:.5 C#5:.5 B4:1
G4:1 B4:1 D5:2 C#5:1
B4:2 A4:1 G#4:1 F#4:1
E4:1 F#4:1 A#4:1 C#5:1 B4:1
F#4:1 E4:1 D4:2 R:1''',
 lh='''B2:1.5 D3+F#3:1.5 F#2:1 D3+A3:1
G2:1.5 B2+D3:1.5 D3:1 B2+F#3:1
A2:1.5 C#3+E3:1.5 E3:1 C#3+G3:1
D3:1.5 F#3+A3:1.5 A2:1 F#3+A3:1
E3:1.5 G3+B3:1.5 C#3:1 E3+A#3:1
B2:1.5 D3+F#3:1.5 R:2
C3:1.5 E3+G3:1.5 E3:1 G3+B3:1
F#2:1.5 A#2+E3:1.5 B2:1 R:1
B2:1 D3+F#3:1 F#2:1.5 D3+A3:1.5
G2:1 B2+D3:1 D3:1.5 B2+F#3:1.5
A2:1 C#3+E3:1 E3:1.5 C#3+G3:1.5
D3:1 F#3+A3:1 A2:1.5 F#3+A3:1.5
E3:1 G3+B3:1 C#3:1.5 E3+A#3:1.5
B2:1 D3+F#3:2 R:2
E3:1 G3+B3:1 G3:1.5 B3+D4:1.5
F#3:1 A#3+C#4:1 E3:1.5 A#3+C#4:.5 R:1
G3+B3+D4:3 F#3+A3+C#4:2
E3+G3+B3:3 D3+F#3+A3:2
C#3+E3+A3:3 E3+G3+C#4:2
D3+F#3+A3:3 C#3+E3+G3:2
E3+G3+B3:3 F#3+A#3+C#4:2
B2+D3+F#3:3 E3+G#3+B3:2
C#3+E3:2 F#2+A#2+E3:2 B2:1
B2+F#3+A3:4 R:1''',
 tempos=[60,61,61,60,59,57,61,58,60,61,62,61,59,57,64,59,60,61,60,60,59,59,57,56],
 phrases=[(1,3),(4,6),(7,8),(9,11),(12,14),(15,16),(17,19),(20,22),(23,24)],sections={1:'p',7:'mp',9:'p',15:'f',16:'mp',17:'p',23:'pp'},lower_sections={1:'pp',15:'p',17:'pp'},hairpins=[('crescendo',12,13),('diminuendo',15,16)],
 pedal=[[i*5+.05,i*5+2.85] for i in range(8)]+[[i*5+3.05,i*5+(3.85 if i==7 else 4.8)] for i in [0,1,2,3,4,6,7]]+[[i*5+.05,i*5+1.85] for i in range(8,16)]+[[i*5+2.05,i*5+(2.85 if i==13 else 3.85 if i==15 else 4.8)] for i in range(8,16)]+[[i*5+.05,i*5+2.85] for i in range(16,23)]+[[i*5+3.05,i*5+4.8] for i in range(16,23)]+[[115.05,118.8]])
song(op=329,title='Alder Remanence',key='Ab',fifths=-4,meter='12/8',bpm=78,parent=321,
 source=dict(source_opus=321,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['Eb','D','C','Bb'],transposition_semitones=5),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['Ab','G','F','Eb']),
 description='A warm A-flat melody first sings alone, then returns in paired sixths and thirds, acquiring the intimacy of a duet. Its third statement sheds the doubling, but the bass has moved into darker colours. A single middle crest and an unhurried final cadence keep the larger texture within a quiet song.',
 technical='Voice the upper note of each right-hand interval while allowing the lower note to sing softly. Keep the left-hand compound pulse clear and light. The paired return asks for legato changes of sixths without stretching beyond an octave.',
 rh='''Ab5:1.5 G5:.5 F5:1 Eb5:3
C5:1.5 Eb5:1.5 F5:1.5 G5:1.5
Bb5:1.5 Ab5:1.5 G5:.5 F5:1 Eb5:1.5
Db5:3 C5:1.5 R:1.5
F5:1.5 Eb5:.5 Db5:1 C5:1.5 Bb4:1.5
Eb5:2 E5:.5 F5:.5 G5:1.5 Ab5:1.5
G5:1.5 F5:1.5 Eb5:1.5 Db5:1.5
C5:3 R:3
C5+Ab5:1.5 Bb4+G5:.5 Ab4+F5:1 G4+Eb5:3
Ab4+C5:1.5 C5+Eb5:1.5 Db5+F5:1.5 Eb5+G5:1.5
Db5+Bb5:1.5 C5+Ab5:1.5 Bb4+G5:.5 Ab4+F5:1 G4+Eb5:1.5
F4+Db5:3 Eb4+C5:1.5 R:1.5
Ab4+F5:1.5 G4+Eb5:.5 F4+Db5:1 Eb4+C5:1.5 Db4+Bb4:1.5
C5+Eb5:1.5 Db5+F5:1.5 Eb5+G5:1.5 F5+Ab5:.5 G5+Bb5:1
Eb5+G5:1.5 Db5+F5:1.5 C5+Eb5:1.5 Bb4+Db5:1.5
Ab4+C5:3 R:3
Ab5:1.5 G5:.5 F5:1 Eb5:3
C5:1.5 Eb5:1.5 F5:1.5 G5:1.5
Bb5:1.5 Ab5:1.5 G5:.5 F5:1 Eb5:1.5
Db5:3 C5:1.5 R:1.5
F5:1.5 Eb5:.5 Db5:1 C5:1.5 Bb4:1.5
Ab4:1.5 C5:1.5 Eb5:1.5 Db5:1.5
C5:1.5 Bb4:1.5 G4:1.5 Bb4:1.5
Ab4:4.5 R:1.5''',
 lh='''Ab2:1.5 C3+Eb3:1.5 Eb3:1.5 C3+G3:1.5
F3:1.5 Ab3+C4:1.5 C3:1.5 Ab3+C4:1.5
Db3:1.5 F3+Ab3:1.5 Bb2:1.5 Db3+F3:1.5
Eb3:1.5 G3+Bb3:1.5 Ab2:1.5 R:1.5
Db3:1.5 F3+Ab3:1.5 Bb2:1.5 Db3+F3:1.5
C3:1.5 E3+Bb3:1.5 F3:1.5 Ab3+C4:1.5
Bb2:1.5 Db3+F3:1.5 Eb3:1.5 G3+Db4:1.5
Ab2:1.5 C3+Eb3:1.5 R:3
Ab2:1.5 C3+Eb3:1.5 Eb3:1.5 C3+G3:1.5
F3:1.5 Ab3+C4:1.5 C3:1.5 Ab3+C4:1.5
Db3:1.5 F3+Ab3:1.5 Bb2:1.5 Db3+F3:1.5
Eb3:1.5 G3+Bb3:1.5 Ab2:1.5 R:1.5
Db3:1.5 F3+Ab3:1.5 Bb2:1.5 Db3+F3:1.5
F3:1.5 A3+C4:1.5 Bb2:1.5 D3+Ab3:1.5
Eb3:1.5 G3+Bb3:1.5 Eb3:1.5 G3+Db4:1.5
Ab2:1.5 C3+Eb3:1.5 R:3
F3:1.5 Ab3+C4:1.5 C3:1.5 Ab3+C4:1.5
Db3:1.5 F3+Ab3:1.5 Ab2:1.5 F3+Ab3:1.5
Bb2:1.5 Db3+F3:1.5 Db3:1.5 Fb3+Ab3:1.5
Eb3:1.5 G3+Bb3:1.5 Ab2:1.5 R:1.5
Db3:1.5 F3+Ab3:1.5 Bb2:1.5 Db3+F3:1.5
F3:1.5 Ab3+C4:1.5 Db3:1.5 F3+Ab3:1.5
Eb3:1.5 G3+Db4:1.5 Eb3:1.5 G3+Bb3:1.5
Ab2+C3+Eb3:4.5 R:1.5''',
 tempos=[78,79,78,75,78,80,78,74,78,79,79,75,78,82,78,74,78,79,78,75,77,76,74,71],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],sections={1:'p',9:'mp',13:'mp',14:'f',15:'mp',17:'p',23:'pp'},lower_sections={1:'pp',14:'p',17:'pp'},hairpins=[('crescendo',13,14),('diminuendo',15,16)],
 pedal=[[i*6+.05,i*6+2.85] for i in range(23)]+[[i*6+3.05,i*6+(4.35 if i in [3,11,19] else 5.85)] for i in range(23) if i not in [7,15]]+[[138.05,142.35]])
song(op=330,title='Orchid Reverie',key='e',fifths=1,meter='4/4',bpm=60,parent=320,
 source=dict(source_opus=320,source_hand='lh',source_voice='bass',source_start_beat=0,source_end_beat=6,source_pitches=['D','F','E','A'],transposition_semitones=2),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['E','G','F#','B']),
 description='A minor-key song returns first with small, quick turns and then with its durations enlarged into six-beat bars. The accompaniment moves from a flowing eighth-note thread to widely spaced chords. A six-bar excursion makes the only crest; the broadened final return and two plain closing bars let the original melody outlast its ornament.',
 technical='Keep the eighth-note accompaniment beneath the long melodic notes. The change from four to six is written augmentation, not a general slowing of every note: maintain the quarter-note pulse and allow the melody more room. Return to four for the short coda.',
 rh='''E5:1 G5:.5 F#5:.5 B5:2
A5:1 G5:1 F#5:1 E5:1
D5:1 F#5:1 G5:.5 F#5:.5 E5:1
B4:3 R:1
C5:1 E5:.5 G5:.5 F#5:2
E5:1 D5:1 C5:1 B4:1
A4:1 C5:1 B4:1 A4:1
B4:2 R:2
E5:.75 G5:.25 F#5:.5 B5:1.5 A5:.5 B5:.5
A5:.75 G5:.25 F#5:.5 G5:.5 F#5:1 E5:1
D5:.75 E5:.25 F#5:1 G5:.5 F#5:.5 E5:1
B4:3 R:1
C5:.75 D5:.25 E5:.5 G5:.5 F#5:1 E5:.5 F#5:.5
E5:1 D5:.5 E5:.5 C5:1 B4:1
A4:1 C5:.75 D5:.25 B4:1 A4:.5 G4:.5
B4:2 R:2
C5:1 E5:1 G5:1 A5:1
Bb5:1 A5:.5 G5:.5 F5:1 E5:1
G5:1 B5:.5 C6:.5 D6:1 C6:.5 B5:.5
A5:1 G5:1 F#5:1 E5:1
D5:1 C5:.5 B4:.5 A4:1 G4:1
F#4:1 A4:.5 B4:.5 D#5:1 R:1
E5:1.5 G5:.75 F#5:.75 B5:3
A5:1.5 G5:1.5 F#5:1.5 E5:1.5
D5:1.5 F#5:1.5 G5:.75 F#5:.75 E5:1.5
B4:4.5 R:1.5
C5:1.5 E5:.75 G5:.75 F#5:3
E5:1.5 D5:1.5 C5:1.5 B4:1.5
A4:1.5 C5:1.5 B4:1.5 A4:1.5
B4:3 R:3
B4:1 A4:1 G4:1 F#4:1
G4:1 F#4:1 E4:1 R:1''',
 lh='''E3:.5 G3:.5 B3:.5 G3:.5 F#3:.5 G3:.5 B3:.5 G3:.5
C3:.5 E3:.5 G3:.5 E3:.5 D3:.5 E3:.5 G3:.5 E3:.5
D3:.5 F#3:.5 A3:.5 F#3:.5 E3:.5 F#3:.5 A3:.5 F#3:.5
E3:.5 G3:.5 B3:.5 G3:.5 F#3:.5 E3:.5 R:1
A2:.5 C3:.5 E3:.5 C3:.5 D3:.5 E3:.5 A3:.5 E3:.5
C3:.5 E3:.5 G3:.5 E3:.5 B2:.5 D3:.5 G3:.5 D3:.5
A2:.5 C3:.5 E3:.5 C3:.5 B2:.5 D#3:.5 F#3:.5 D#3:.5
B2:.5 D#3:.5 F#3:.5 A3:.5 R:2
E3:.5 G3:.5 B3:.5 G3:.5 F#3:.5 G3:.5 B3:.5 G3:.5
C3:.5 E3:.5 G3:.5 E3:.5 D3:.5 E3:.5 G3:.5 E3:.5
D3:.5 F#3:.5 A3:.5 F#3:.5 E3:.5 F#3:.5 A3:.5 F#3:.5
E3:.5 G3:.5 B3:.5 G3:.5 F#3:.5 E3:.5 R:1
A2:.5 C3:.5 E3:.5 C3:.5 D3:.5 E3:.5 A3:.5 E3:.5
C3:.5 E3:.5 G3:.5 E3:.5 B2:.5 D3:.5 G3:.5 D3:.5
A2:.5 C3:.5 E3:.5 C3:.5 B2:.5 D#3:.5 F#3:.5 D#3:.5
B2:.5 D#3:.5 F#3:.5 A3:.5 R:2
A2:.5 C3:.5 E3:.5 G3:.5 F#3:.5 E3:.5 C3:.5 E3:.5
F3:.5 A3:.5 C4:.5 A3:.5 G3:.5 F3:.5 E3:.5 F3:.5
G3:.5 B3:.5 D4:.5 B3:.5 A3:.5 G3:.5 F#3:.5 G3:.5
D3:.5 F#3:.5 A3:.5 F#3:.5 E3:.5 F#3:.5 A3:.5 F#3:.5
A2:.5 C3:.5 E3:.5 G3:.5 E3:.5 C3:.5 B2:.5 D#3:.5
B2:.5 D#3:.5 F#3:.5 A3:.5 F#3:.5 D#3:.5 R:1
E3+G3+B3:3 B2+D3+F#3:3
C3+E3+G3:3 G2+B2+D3:3
D3+F#3+A3:3 A2+C3+E3:3
E3+G3+B3:4.5 R:1.5
A2+C3+E3:3 D3+F#3+A3:3
C3+E3+G3:3 B2+D3+G3:3
A2+C3+E3:3 B2+D#3+F#3:3
E3+G3+B3:3 R:3
C3+E3+G3:2 B2+D#3+A3:2
E3+G3+B3:3 R:1''',
 meters=['4/4']*22+['6/4']*8+['4/4']*2,
 tempos=[60,61,60,58,60,61,60,57,60,61,62,58,61,61,59,57,61,63,64,62,60,58,60,60,60,60,60,60,60,60,59,58],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,22),(23,26),(27,30),(31,32)],sections={1:'p',9:'mp',17:'mp',19:'mf',20:'mp',23:'p',27:'pp',31:'pp'},lower_sections={1:'pp',17:'p',23:'pp'},hairpins=[('crescendo',17,19),('diminuendo',20,22)],
 pedal=[[i*4+.05,i*4+(1.85 if i in [7,15] else 2.85 if i in [3,11,21] else 3.8)] for i in range(22)]+[[88+i*6+.05,88+i*6+2.85] for i in range(8)]+[[88+i*6+3.05,88+i*6+(4.35 if i==3 else 5.85)] for i in range(7)]+[[136.05,137.85],[138.05,139.85],[140.05,142.85]])
