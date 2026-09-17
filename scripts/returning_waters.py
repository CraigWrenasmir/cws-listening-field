"""Op. 251–270: individually authored studies informed by Craig's piano references.

The private recordings supplied broad compositional prompts, not verified scores.
Every note below is newly specified; catalogue ancestry is independently documented.
"""
PIECES=[]

def study(*, op, title, key, fifths, meter, bpm, parent, source, motif, rh, lh,
          description, technical, tempos, phrases, sections, pedal=None, **extras):
    """Apply shared score presentation to an explicitly composed work."""
    n=len(rh.strip().splitlines())
    beats=int(meter.split('/')[0])*4/int(meter.split('/')[1])
    assert len(lh.strip().splitlines())==n and len(tempos)==n
    entry=dict(op=op,title=title,key=key,fifths=fifths,meter=meter,bpm=bpm,
      parent_opus=parent,ancestry=source,motif=motif,rh=rh,lh=lh,
      description=description,difficulty='Advanced lyrical study',
      technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),technical_note=technical,
      system_starts=list(range(1,n+1,2)),page_starts=list(range(9,n+1,8)),
      engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=570),
      sections=sections,lower_sections={1:'pp'},words={1:'poco rubato'},slurs=phrases,
      hairpins=[],tempo_changes={},group=3,final_fermata=False,
      performance=dict(rubato=tempos,phrase_arcs=[[(a-1)*beats,b*beats,3] for a,b in phrases],
        lower_entries=[],pedal_lift=.2,gate=.98,
        note='Authored phrase breathing and independent note lengths; no random timing offsets.'))
    if pedal is not None:entry['pedal_spans']=pedal
    entry.update(extras)
    PIECES.append(entry)
    return entry

study(op=251,title='Alder Rill',key='d',fifths=-1,meter='4/4',bpm=52,parent=246,
 source=dict(source_opus=246,source_hand='rh',source_start_beat=0,source_end_beat=5,source_pitches=['D','F','E','A'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=.5,end_beat=4,pitches=['D','F','E','A']),
 description='A delayed four-note song opens above a quietly uneven bass. Its held notes outlast the first harmonies; the lower figure changes its accent while the melody remembers longer phrases. A warmer middle passage returns to D minor, then the bass leaves the final answer alone.',
 technical='Keep the six-note lower cell even in tone while its long-short timing shifts. The RH repeatedly sustains through a bar line; follow its phrase independently of the recurring accompaniment. Later thirds are softly voiced. The final unaccompanied answer remains in tempo.',
 rh='''R:.5 D5:.5 F5:.5 E5:.5 A4:2
C5:1.5 E5:.5 G5:2~
G5:1 F5:.5 E5:1.5 D5:1
C5:1 A4:.5 G4:.5 F4:1 R:1
R:1 A4:.5 C5:.5 E5:2~
E5:1 D5:.5 C5:1.5 A4:1
Bb4:1.5 D5:.5 F5:1 E5:1
D5:2 C5:1 R:1
F5:1 E5:.5 C5:.5 A4:2
G4:1 A4:.5 C5:.5 D5:2~
D5:1 E5:.5 G5:.5 F5:1 D5:1
C5:2 A4:1 R:1
E5:1 G5:.5 A5:.5 C6:1 B5:1
A5:1.5 G5:.5 E5:1 D5:1
F5:.5 A5:.5 G5:1 E5:1 C5:1
D5:2 E5:1 R:1
R:.5 D5:.5 F5:.5 E5:.5 A4:2
C5:1.5 E5:.5 G5:2~
G5:1 F5:.5 E5:1.5 D5:1
C5:1 A4:.5 G4:.5 F4:1 R:1
A4+C5:1 C5+E5:.5 D5+F5:.5 C5+E5:2
Bb4+D5:1 A4+C5:.5 G4+Bb4:.5 F4+A4:2
E4+G4:1 G4+Bb4:.5 A4+C5:.5 G4+Bb4:1 E4+G4:1
F4+A4:2 E4+G4:1 R:1
D5:1 F5:.5 E5:.5 A4:2
C5:1 E5:1 D5:1 C5:1
A4:1 G4:.5 F4:.5 E4:1 R:1
F4:1 E4:.5 D4:1.5 R:1''',
 lh='''D3:.75 A3:.25 F3:.5 G3:.5 A3:1 E3:1
C3:.75 G3:.25 E3:.5 F3:.5 G3:1 D3:1
Bb2:1 F3:.75 D3:.25 E3:.5 F3:.5 A3:1
D3:1 A3:.5 F3:.5 E3:1 R:1
F3:.75 C4:.25 A3:.5 G3:.5 E3:1 G3:1
C3:1 G3:.75 E3:.25 D3:.5 E3:.5 G3:1
G2:.75 D3:.25 Bb3:.5 A3:.5 G3:1 F3:1
A2:1 E3:.5 G3:.5 C#4:1 R:1
F3:1 A3:.5 C4:.5 G3:1 E3:1
E3:.75 B3:.25 G3:.5 A3:.5 B3:1 F3:1
D3:1 A3:.75 F3:.25 G3:.5 A3:.5 C4:1
C3:1 G3:.5 E3:.5 D3:1 R:1
A3:1 C4:1 E4:1 D4:1
G3:.75 D4:.25 B3:.5 A3:.5 G3:1 D3:1
F3:1 C4:.5 A3:.5 G3:1 E3:1
G3:1 B3:1 A3:1 R:1
Bb2:.75 F3:.25 D3:.5 E3:.5 F3:1 A3:1
A2:.75 E3:.25 C3:.5 D3:.5 E3:1 G3:1
G2:1 D3:.75 B2:.25 C3:.5 D3:.5 F3:1
F3:1 C4:.5 A3:.5 G3:1 R:1
D3:.75 A3:.25 F3:.5 G3:.5 A3:1 E3:1
Bb2:1 F3:.75 D3:.25 E3:.5 F3:.5 A3:1
C3:.75 G3:.25 E3:.5 F3:.5 G3:1 D3:1
A2:1 E3:.5 G3:.5 C#4:1 R:1
D3:1 A3:1 F3:1 E3:1
C3:1 G3:1 E3:1 D3:1
Bb2:1 F3:1 A2:1 R:1
R:4''',
 tempos=[52,53,51,48,52,54,53,48,54,55,53,49,56,55,53,48,52,53,51,48,54,53,52,48,51,50,48,49],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,27),(28,28)],
 sections={1:'p',9:'p',13:'mp',17:'p',21:'mp',25:'pp'},
 pedal=[[i*4,i*4+(2.8 if i in [3,7,11,15,19,23,26] else 3.8)] for i in range(27)])
study(op=252,title='Fennel Slipstream',key='C',fifths=0,meter='9/8',bpm=65,parent=240,
 source=dict(source_opus=240,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['F','E','D','C'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4.5,pitches=['F','E','D','C']),
 description='A descending melody drifts over three unequal breaths in each bar. The accompaniment alternates E and G with a recurring F-major window, while a five-bar song gradually acquires small rising answers. A central brightening gives way to a lower, more spacious return and an open sixth.',
 technical='Shape the 9/8 as a flexible long phrase. LH dotted-quarter anchors alternate with short paired notes, and the RH ties ignore some bar lines. Keep the late octave descent connected without accenting it; the final sixth has no extra fermata.',
 rh='''F5:1 E5:.5 D5:1.5 C5:1.5
B4:1.5 D5:.5 E5:1 G5:1.5~
G5:1.5 F5:.5 E5:1 D5:1.5
C5:1 A4:.5 G4:1.5 E4:1.5
G4:1.5 A4:1 C5:.5 D5:1 R:.5
E5:1.5 G5:.5 A5:1 G5:1.5
F5:1.5 E5:.5 D5:1 C5:1.5~
C5:1 B4:.5 A4:1.5 G4:1.5
A4:.5 C5:.5 E5:.5 D5:1.5 B4:1.5
G4:2 E4:1 R:1.5
F5:1 E5:.5 D5:1.5 C5:1.5
E5:1.5 G5:.5 B5:1 A5:1.5
G5:1 E5:.5 D5:1.5 C5:1.5
B4:1.5 D5:.5 E5:1 F5:1.5~
F5:1 E5:.5 D5:1 C5:.5 A4:1 R:.5
C5:.5 E5:.5 G5:.5 A5:.5 B5:.5 C6:.5 B5:1.5
A5:1 G5:.5 E5:1 D5:.5 C5:1.5
D5:.5 F5:.5 A5:.5 G5:1.5 E5:1.5
F5:1.5 D5:1 C5:.5 A4:1.5
B4:2 G4:1 R:1.5
F4:1 E4:.5 D4:1.5 C4:1.5
E4:1.5 G4:.5 B4:1 A4:1.5
G4:1.5 E4:.5 D4:1 C4:1.5
D4:1.5 F4:.5 G4:1 A4:1.5~
A4:1 G4:.5 E4:1 D4:.5 C4:1 R:.5
G4:1.5 C5:.5 E5:1 D5:1.5
C5:1 A4:.5 G4:1.5 E4:1.5
F4:1.5 A4:1 G4:.5 E4:1.5
D4:1 E4:.5 G4:1.5 A4:1.5
E4+A4:4.5''',
 lh='''F2:1.5 C3:1 A3:.5 G3:1.5
E2:1.5 B2:1 G3:.5 D3:1.5
G2:1 D3:.5 B3:1.5 A3:1 G2:.5
E2:1.5 B2:1 G3:.5 D3:1.5
F2:1.5 C3:1 A3:.5 G3:1 R:.5
G2:1.5 D3:.5 B3:1 A3:1.5
F2:1.5 C3:1 A3:.5 G3:1.5
E2:1 B2:.5 G3:1.5 E3:1 D3:.5
G2:1.5 D3:1 B3:.5 A3:1.5
E3:1.5 B2:1 G3:.5 R:1.5
F2:1.5 C3:1 A3:.5 G3:1.5
G2:1.5 D3:1 B3:.5 A3:1.5
E3:1 B2:.5 G3:1.5 D3:1 E2:.5
F2:1.5 C3:1 A3:.5 G3:1.5
G2:1.5 D3:1 B3:.5 A3:1 R:.5
A2:1.5 E3:1 C4:.5 B3:1.5
G2:1.5 D3:1 B3:.5 A3:1.5
F2:1.5 C3:1 A3:.5 G3:1.5
D3:1.5 A3:1 F3:.5 E3:1.5
G2:1.5 D3:1 G3:.5 R:1.5
F2:1.5 C3:1 A3:.5 G3:1.5
E2:1.5 B2:1 G3:.5 D3:1.5
G2:1.5 D3:1 B3:.5 A3:1.5
F2:1.5 C3:1 A3:.5 G3:1.5
E2:1.5 B2:1 G3:.5 E3:1 R:.5
C3:1.5 G3:1 E3:.5 D3:1.5
A2:1.5 E3:1 C3:.5 B2:1.5
F2:1.5 C3:1 A3:.5 G3:1.5
G2:1.5 D3:1 B3:.5 A3:1.5
C3+G3:4.5''',
 tempos=[65,66,64,62,59,65,64,63,62,58,65,67,66,64,60,68,67,65,63,58,61,63,62,63,59,62,61,60,59,59],
 phrases=[(1,5),(6,10),(11,15),(16,20),(21,25),(26,30)],sections={1:'p',11:'p',16:'mp',21:'pp',26:'p',29:'pp'},
 pedal=[[i*4.5,i*4.5+(2.8 if i in [9,19] else 3.8 if i in [4,14,24] else 4.3)] for i in range(30)])
study(op=253,title='Myrtle Backwater',key='g',fifths=-2,meter='6/4',bpm=58,parent=239,
 source=dict(source_opus=239,source_hand='rh',source_start_beat=0,source_end_beat=7,source_pitches=['G','Bb','A','D'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['G','Bb','A','D']),
 description='A broad G-minor song turns above a six-note lower phrase. Its third phrase arrives a little early, and the bass changes underneath sustained melodic notes. E-flat and C-minor warmth opens a more active middle passage before the opening returns over a different bass and releases into a solitary D.',
 technical='Sustain the upper line across the lower six-note turns. The irregular three-, five- and four-bar phrases should remain continuous. Softly articulate the central eighths without turning the accompaniment into an accent grid; keep the final bass release distinct from the still-held melody.',
 rh='''G5:2 Bb5:1 A5:1 D5:2
F5:1.5 Eb5:.5 D5:2 C5:2~
C5:2 Bb4:1 G4:2 R:1
R:1 Bb4:1 D5:1 F5:3~
F5:1 Eb5:1 D5:1 C5:1 Bb4:2
G4:1.5 Bb4:.5 C5:2 Eb5:2
D5:2 F5:1 G5:1 A5:2
G5:3 F5:1 D5:1 R:1
Eb5:2 G5:1 Bb5:1 A5:2
G5:1.5 F5:.5 Eb5:1 D5:1 C5:2~
C5:1 Eb5:.5 G5:.5 F5:2 D5:2
Bb4:2 A4:1 G4:2 R:1
C5:.5 Eb5:.5 G5:1 Bb5:.5 A5:.5 G5:1 F5:1 Eb5:1
D5:1 F5:.5 A5:.5 C6:1 Bb5:1 A5:1 G5:1
F5:1 Eb5:.5 D5:.5 C5:1 Eb5:1 G5:2
F5:2 D5:1 C5:1 Bb4:1 R:1
G5:2 Bb5:1 A5:1 D5:2
F5:1.5 Eb5:.5 D5:2 C5:2~
C5:2 Bb4:1 G4:2 F4:1
G4:2 Bb4:1 D5:3
Eb5:2 D5:1 C5:1 Bb4:2
A4:1.5 C5:.5 D5:2 F5:2
Eb5:2 D5:1 Bb4:2 R:1
D5:6''',
 lh='''G3:1 D4:1 Bb3:1 A3:1 G3:1 F3:1
Eb3:1 Bb3:1 G3:1 F3:1 Eb3:1 D3:1
C3:1 G3:1 Eb3:1 D3:1 C3:1 R:1
Bb2:1 F3:1 D3:1 F3:1 A3:1 C4:1
Ab2:1 Eb3:1 C4:1 Bb3:1 Ab3:1 G3:1
C3:1 G3:1 Eb3:1 F3:1 G3:1 Bb3:1
D3:1 A3:1 F3:1 E3:1 D3:1 C3:1
G2:1 D3:1 Bb3:1 A3:1 G3:1 R:1
Eb3:1 Bb3:1 G3:1 F3:1 Eb3:1 D3:1
Bb2:1 F3:1 D3:1 Eb3:1 F3:1 A3:1
Ab2:1 Eb3:1 C4:1 Bb3:1 Ab3:1 G3:1
D3:1 A3:1 F#3:1 E3:1 D3:1 R:1
C3:1.5 G3:.5 Eb3:1 Bb3:1 G3:1 F3:1
D3:1.5 A3:.5 F3:1 C4:1 A3:1 G3:1
Eb3:1.5 Bb3:.5 G3:1 F3:1 Eb3:1 D3:1
F3:1 C4:1 A3:1 G3:1 F3:1 R:1
Eb3:1 Bb3:1 G3:1 F3:1 Eb3:1 D3:1
C3:1 G3:1 Eb3:1 D3:1 C3:1 Bb2:1
Ab2:1 Eb3:1 C4:1 Bb3:1 Ab3:1 G3:1
G2:1 D3:1 Bb3:1 A3:1 G3:1 F3:1
C3:2 G3:1 Eb3:1 F3:2
D3:2 A3:1 C4:1 F#3:2
Eb3:2 Bb3:1 G3:2 R:1
G2+D3:2 R:4''',
 tempos=[58,57,53,57,59,58,60,54,58,57,58,53,61,63,61,54,57,56,54,56,54,55,52,53],
 phrases=[(1,3),(4,8),(9,12),(13,16),(17,20),(21,24)],sections={1:'p',9:'p',13:'mp',17:'p',21:'pp'},
 pedal=[[i*6,i*6+(4.8 if i in [2,7,11,15,22] else 1.8 if i==23 else 5.8)] for i in range(24)])
study(op=254,title='Reed Meander',key='C',fifths=0,meter='5/4',bpm=56,parent=238,
 source=dict(source_opus=238,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=5,source_pitches=['D','C','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=1,end_beat=5,pitches=['D','C','A','G']),
 description='The tune begins one beat after a quiet lower turn. Five-beat bars allow its long notes to drift across the accompaniment; brief paired notes gather into a more fluent middle. The return removes some of the expected downbeats, and the left hand supplies the last small, questioning answer.',
 technical='Maintain the melody through off-beat ties and the changing placement of the lower long note. Keep the central sixteenth turns light and even. The two final bars transfer attention from RH to LH without a tempo break.',
 rh='''R:1 D5:1 C5:1 A4:1 G4:1
E5:2 G5:.5 F5:.5 E5:2~
E5:1 D5:.5 C5:.5 A4:2 G4:1
A4:1 C5:.5 D5:.5 E5:2 R:1
R:.5 G4:1.5 A4:.5 C5:.5 D5:2~
D5:1 E5:.5 F5:.5 G5:2 E5:1
F5:2 E5:1 C5:1 A4:1
B4:2 G4:1 E4:1 R:1
D5:1 C5:1 A4:1 G4:2
C5:1 E5:.5 G5:.5 A5:2 G5:1
F5:1.5 E5:.5 D5:1 C5:2~
C5:1 B4:1 A4:2 R:1
E5:.5 G5:.5 A5:.5 B5:.5 C6:1 B5:1 G5:1
A5:.5 G5:.5 E5:.5 D5:.5 C5:1 E5:1 G5:1
F5:.25 G5:.25 A5:.25 G5:.25 F5:.5 E5:.5 D5:1 C5:1 A4:1
B4:1 D5:.5 E5:.5 F5:1 E5:1 D5:1
G5:2 E5:1 C5:1 A4:1
G4:2 E4:1 D4:1 R:1
R:1 D5:1 C5:1 A4:1 G4:1
E5:2 G5:.5 F5:.5 E5:2~
E5:1 D5:.5 C5:.5 A4:2 G4:1
A4:1 C5:.5 D5:.5 E5:2 R:1
R:1 G4:1 A4:1 C5:2~
C5:2 B4:.5 A4:.5 G4:2
E4+G4:2 F4+A4:1 G4+B4:2
A4+C5:1 G4+B4:1 F4+A4:2 R:1
E4+G4:3 R:2
R:5''',
 lh='''F3:1.5 C4:.5 A3:1 E3:1 G3:1
C3:1 G3:1.5 E3:.5 A3:1 B3:1
A2:1 E3:1 C4:1.5 B3:.5 A3:1
G2:1 D3:1 B3:1 A3:1 R:1
E3:1.5 B3:.5 G3:1 D3:1 F3:1
D3:1 A3:1.5 F3:.5 C4:1 E4:1
F3:1 C4:1 A3:1.5 G3:.5 F3:1
E3:1 B3:1 G3:1 D3:1 R:1
D3:1.5 A3:.5 F3:1 C3:1 E3:1
A2:1 E3:1.5 C4:.5 G3:1 A3:1
Bb2:1 F3:1 D4:1.5 C4:.5 Bb3:1
G3:1 D4:1 B3:1 A3:1 R:1
C4:1 G4:1 E4:1 D4:1 C4:1
A3:1 E4:1 C4:1 B3:1 A3:1
F3:1 C4:1 A3:1 G3:1 F3:1
G3:1 D4:1 B3:1 A3:1 G3:1
C3:1 G3:1 E3:1 D3:1 C3:1
A2:1 E3:1 C3:1 B2:1 R:1
Bb2:1.5 F3:.5 D3:1 A3:1 C4:1
A2:1 E3:1.5 C3:.5 G3:1 B3:1
G2:1 D3:1 B2:1.5 C3:.5 D3:1
F3:1 C4:1 A3:1 G3:1 R:1
E3:1 B3:1 G3:1 F3:1 E3:1
D3:1 A3:1 F3:1 E3:1 D3:1
C3+G3:2 D3+A3:1 E3+B3:2
F3+C4:1 E3+B3:1 D3+A3:2 R:1
C3+G3:3 R:2
D3:.5 E3:.5 G3:1 A3:1 C4:1 B3:1''',
 tempos=[56,57,55,51,56,58,57,52,57,59,56,52,61,62,60,59,56,51,55,56,54,51,54,53,52,50,49,51],
 phrases=[(1,4),(5,8),(9,12),(13,18),(19,22),(23,26)],sections={1:'p',9:'p',13:'mp',19:'p',23:'pp'},
 lower_sections={1:'pp',28:'p'},lower_phrases=[(28,28)],
 pedal=[[i*5,i*5+(3.8 if i in [3,7,11,17,21,25] else 2.8 if i==26 else 4.8)] for i in range(27)])
study(op=255,title='Clover Driftway',key='a',fifths=0,meter='3/4',bpm=44,parent=243,
 source=dict(source_opus=243,source_hand='lh',source_start_beat=90,source_end_beat=95,source_pitches=['A','C','B','E'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['A','C','B','E']),
 description='An A-minor melody floats above a small, uneven three-beat figure. Its five-bar sentences avoid a square waltz pattern, and the bass sometimes arrives after the tune. Paired notes briefly enrich the central song; an altered return makes room for a quiet ninth at the close.',
 technical='Let the short opening notes lead into the longer E rather than accenting the bar. The accompaniment alternates a dotted cell, held shells and delayed bass entries. Voice the top of the middle dyads and allow the written silences to interrupt the pulse naturally.',
 rh='''A5:.5 C6:.5 B5:1 E5:1
G5:1 E5:.5 D5:.5 C5:1~
C5:1 B4:.5 A4:.5 G4:1
E5:1.5 D5:.5 C5:1
B4:1 A4:1 R:1
R:.5 E5:.5 G5:1 A5:1
C6:1 B5:.5 A5:.5 G5:1
F5:1 E5:.5 D5:.5 C5:1~
C5:1.5 D5:.5 E5:1
A4:2 R:1
C5+E5:1 E5+G5:.5 F5+A5:.5 E5+G5:1
D5+F5:1 C5+E5:1 A4+C5:1
B4+D5:1 D5+F5:.5 E5+G5:.5 D5+F5:1
C5+E5:1 B4+D5:.5 A4+C5:.5 G4+B4:1
A4+C5:2 R:1
A5:.5 C6:.5 B5:1 E5:1
G5:1 E5:.5 D5:.5 C5:1
D5:.5 F5:.5 A5:1 G5:1
E5:1 D5:.5 C5:.5 A4:1
B4:2 R:1
A4:.5 C5:.5 B4:1 E4:1
G4:1 E4:.5 D4:.5 C4:1~
C4:1 D4:.5 E4:.5 G4:1
A4:1.5 G4:.5 E4:1
D4:1 E4:1 R:1
E5:1 G5:.5 A5:.5 B5:1
A5:1 G5:.5 E5:.5 D5:1
C5:1 A4:.5 G4:.5 E4:1
G4:1 A4:1 B4:1
B4+E5:3''',
 lh='''A2:.75 E3:.25 C4:1 B3:1
G2:.75 D3:.25 B3:1 A3:1
F2:1 C3+A3:2
R:.5 E3:1.5 G3+B3:1
A2:1 E3:1 R:1
F2:.75 C3:.25 A3:1 G3:1
G2:1 D3+B3:2
E3:.75 B3:.25 G3:1 F3:1
R:.5 D3:1.5 F3+A3:1
A2:1 E3:1 R:1
C3:.75 G3:.25 E3:1 D3:1
D3:1 A3:1 F3:1
G2:.75 D3:.25 B3:1 A3:1
E3:1 B3:1 G3:1
A2:1 E3:1 R:1
F3:.75 C4:.25 A3:1 G3:1
E3:.75 B3:.25 G3:1 F3:1
D3:1 A3:1 F3:1
C3:1 G3:1 E3:1
G2:1 D3:1 R:1
F2:.75 C3:.25 A3:1 G3:1
E2:.75 B2:.25 G3:1 F3:1
D3:1 A3:1 F3:1
R:.5 C3:1.5 G3:1
B2:1 F3:1 R:1
C3:.75 G3:.25 E3:1 D3:1
F3:1 C4:1 A3:1
E3:1 B3:1 G3:1
D3:1 A3:1 G3:1
A2+E3:3''',
 tempos=[44,45,43,42,39,44,46,44,43,39,46,47,46,44,40,45,46,45,43,39,42,43,42,41,39,43,44,42,40,40],
 phrases=[(1,5),(6,10),(11,15),(16,20),(21,25),(26,30)],sections={1:'p',11:'mp',16:'p',21:'pp',26:'p',29:'pp'},
 pedal=[[i*3+(.5 if i in [3,8,23] else 0),i*3+(1.8 if i in [4,9,14,19,24] else 2.8)] for i in range(30)])
study(op=256,title='Camellia Fenlight',key='c',fifths=-3,meter='4/4',bpm=46,parent=236,
 source=dict(source_opus=236,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=8,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['Eb','D','C','Bb']),
 description='A descending song sits inside a quiet three-voice chorale. The inner line continues while the melody rests, changing the colour of otherwise simple chords. A brief E-flat-major opening of the texture subsides into the original song, now heard against A-flat and F-minor support.',
 technical='The RH carries two independent voices. Keep its upper line distinct through the held notes and release the inner dyads without interrupting it. The complete combined reach remains within an octave. The closing inner movement continues after the upper phrase has finished.',
 rh='''Eb5:1 D5:1 C5:1 Bb4:1
D5:2 F5:2
Eb5:3 D5:1
C5:2 Bb4:1 R:1
G5:3 F5:1
Eb5:2 D5:2~
D5:2 C5:1 Bb4:1
C5:3 R:1
Eb5:2 G5:2
F5:1 Eb5:1 D5:2
C5:1 Eb5:1 F5:2~
F5:1 Eb5:1 D5:1 R:1
G5:2 Bb5:2
Ab5:3 G5:1
F5:2 Eb5:1 D5:1
C5:2 Bb4:1 R:1
Eb5:1 D5:1 C5:1 Bb4:1
D5:2 F5:2
Eb5:3 D5:1
C5:2 Bb4:1 R:1
G5:2 F5:1 Eb5:1
D5:2 C5:2
Eb5:2 D5:1 C5:1
Bb4:3 R:1
C5:2 R:2
R:4''',
 rh_inner='''G4:2 Ab4:2
A4:1.5 G4:.5 A4:2
G4:1 Bb4:1 Ab4:2
Eb4+G4:2 F4+Ab4:1 R:1
Bb4:2 D5:2
G4+Bb4:2 F4+Ab4:2
F4+Ab4:1 G4:1 Eb4:2
Eb4+G4:2 F4:1 R:1
G4+Bb4:2 Bb4+D5:2
A4+C5:1 G4+Bb4:1 F4+Ab4:2
Eb4+G4:1 G4+Bb4:1 Ab4+C5:2
Ab4+C5:1 G4+Bb4:1 F4+Ab4:1 R:1
Eb5:1 D5:1 F5:2
C5+Eb5:2 D5+F5:2
Bb4+D5:2 G4+Bb4:1 F4+Ab4:1
Eb4+G4:2 D4+F4:1 R:1
G4:2 Ab4:2
A4:1.5 G4:.5 A4:2
G4:1 Bb4:1 Ab4:2
Eb4+G4:2 F4+Ab4:1 R:1
Bb4+D5:2 Ab4+C5:1 G4+Bb4:1
F4+Ab4:2 Eb4+G4:2
G4+Bb4:2 F4+Ab4:1 Eb4+G4:1
D4+F4:2 Eb4+G4:1 R:1
Eb4+G4:2 F4+Ab4:1 G4+Bb4:1
Ab4:1 G4:1 F4:1 Eb4:1''',
 lh='''C3+G3:4
Bb2+F3:4
Ab2+Eb3:2 Bb2+F3:2
C3+G3:3 R:1
Eb3+Bb3:4
Bb2+F3:2 G2+D3:2
Ab2+Eb3:2 Bb2+F3:2
C3+G3:3 R:1
Eb3+Bb3:2 G3+D4:2
F3+C4:2 Bb2+F3:2
Ab2+Eb3:2 F3+C4:2
Bb2+F3:3 R:1
Eb3+Bb3:2 G3+D4:2
Ab3+Eb4:2 Bb3+F4:2
Bb2+F3:2 Eb3+Bb3:2
Ab2+Eb3:2 G2+D3:1 R:1
Ab2+Eb3:2 F3+C4:2
Bb2+F3:4
C3+G3:2 G2+D3:2
Ab2+Eb3:3 R:1
Eb3+Bb3:2 F3+C4:2
Bb2+F3:2 Ab2+Eb3:2
G2+D3:2 Bb2+F3:2
Eb3+Bb3:3 R:1
Ab2+Eb3:4
C3+G3:4''',
 tempos=[46,47,45,42,47,46,44,41,47,48,47,43,50,49,46,42,45,46,44,41,45,44,43,40,42,42],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],sections={1:'p',9:'p',13:'mp',17:'p',21:'pp'},
 pedal=[[i*4+a,i*4+b-.2] for i in range(26) for a,b in ([(0,2),(2,3)] if i in [3,7,11,15,19,23] else [(0,2),(2,4)])])
study(op=257,title='Hazel Spillway',key='d',fifths=-1,meter='5/4',bpm=50,parent=251,
 source=dict(source_opus=251,source_hand='rh',source_start_beat=.5,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['D','F','E','A']),
 description='An entire song made from chords: a minor seventh opens into sixths and suspended colours, with the top note carrying the tune. The chord changes arrive at unequal intervals, occasionally leaving the bass behind. A fuller high-register phrase returns in a quieter spacing and comes to rest in a warm minor sixth.',
 technical='Every sounded event is a chord. Voice the upper note and release each voicing as a single relaxed gesture. Follow the unequal chord durations rather than imposing a repeated five-beat accent. The separated hands leave space for ninths without requiring wide stretches.',
 rh='''F4+A4+D5:1 A4+C5+F5:1 G4+B4+E5:1 E4+G4+A4:2
E4+A4+C5:2 G4+C5+E5:3
F4+A4+D5:1.5 E4+G4+C5:.5 D4+F4+A4:3
F4+A4+C5:3 E4+G4+B4:2
D4+F4+A4:3 E4+G4+C5:1 R:1
F4+A4+D5:2 A4+C5+F5:1 G4+B4+E5:2
A4+C5+F5:2 C5+E5+A5:3
Bb4+D5+G5:1 A4+C5+F5:1 G4+Bb4+E5:3
F4+A4+D5:3 E4+G4+C5:1 R:1
A4+C5+E5:1.5 C5+E5+G5:.5 D5+F5+A5:3
C5+E5+G5:2 Bb4+D5+F5:1 A4+C5+E5:2
G4+B4+D5:1.5 A4+C5+E5:.5 G4+B4+D5:3
F4+A4+C5:3 E4+G4+B4:1 R:1
A4+D5+F5:2 C5+F5+A5:1 Bb4+E5+G5:2
C5+E5+A5:1 E5+G5+C6:2 D5+F5+B5:2
C5+E5+A5:3 B4+D5+G5:2
A4+C5+F5:2 G4+Bb4+E5:1 F4+A4+D5:2
E4+G4+C5:3 D4+F4+A4:1 R:1
F4+A4+D5:1 A4+C5+F5:1 G4+B4+E5:1 E4+G4+A4:2
E4+A4+C5:2 G4+C5+E5:3
F4+A4+D5:1.5 E4+G4+C5:.5 D4+F4+A4:3
E4+G4+C5:2 F4+A4+D5:1 G4+B4+E5:2
F4+A4+D5:2 E4+G4+C5:2 R:1
F4+A4+B4:5''',
 lh='''D3+A3:1 C3+G3:1 B2+F3:1 A2+E3:2
A2+E3:2 C3+G3:3
Bb2+F3:2 G2+D3:3
F3+C4:3 E3+B3:2
D3+A3:3 C3+G3:1 R:1
Bb2+F3:2 D3+A3:1 C3+G3:2
F3+C4:2 A3+E4:3
G3+D4:2 C3+G3:3
Bb2+F3:3 A2+E3:1 R:1
A2+E3:2 C3+G3:3
E3+B3:2 D3+A3:1 C3+G3:2
G2+D3:2 A2+E3:3
Bb2+F3:3 E3+B3:1 R:1
D3+A3:2 F3+C4:1 E3+B3:2
A3+E4:1 C4+G4:2 B3+F4:2
A3+E4:3 G3+D4:2
F3+C4:2 E3+B3:1 D3+A3:2
C3+G3:3 Bb2+F3:1 R:1
D3+A3:1 C3+G3:1 B2+F3:1 A2+E3:2
F3+C4:2 E3+B3:3
Bb2+F3:2 G2+D3:3
C3+G3:2 Bb2+F3:1 A2+E3:2
G2+D3:2 A2+E3:2 R:1
D3+A3:5''',
 tempos=[50,51,49,48,44,50,52,51,45,53,52,50,45,54,56,53,51,45,49,50,48,47,44,43],
 phrases=[(1,5),(6,9),(10,13),(14,18),(19,24)],sections={1:'p',6:'p',10:'mp',14:'mp',19:'p',23:'pp'},
 pedal=[[i*5+a,i*5+b-.2] for i in range(24) for a,b in ([(0,1),(1,2),(2,3),(3,5)] if i in [0,18] else [(0,3),(3,4)] if i in [4,8,12,17] else [(0,2),(2,4)] if i==22 else [(0,5)] if i==23 else [(0,2),(2,5)])])
study(op=258,title='Moss Rainroom',key='f',fifths=-4,meter='6/4',bpm=54,parent=237,
 source=dict(source_opus=237,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['F#','A','G#','C#'],transposition_semitones=-1),motif=dict(hand='lh',voice='tenor',start_beat=0,end_beat=6,pitches=['F','Ab','G','C']),
 description='The melody is heard in the left hand above a held bass, with quiet upper chords opening and closing around it. Its minor colour passes through D-flat and A-flat light, then a more active tenor line briefly fills the space. The final phrase withdraws into a plain F beneath a still-sounding upper ninth.',
 technical='The LH carries bass and tenor independently. Sustain its low note while allowing the tenor fingers to phrase freely; the combined stretch never exceeds an octave. The RH chords should remain behind the lower melody. Every held tone and shared-key occupation is checked across both lower voices.',
 rh='''C5+Eb5+Ab5:3 Bb4+Db5+G5:3
Bb4+Db5+G5:3 Ab4+C5+F5:3
G4+Bb4+E5:3 Bb4+C5+G5:3
Ab4+C5+F5:5 R:1
Bb4+Eb5+G5:3 C5+F5+Ab5:3
C5+Eb5+Ab5:3 Bb4+Db5+G5:3
Ab4+C5+F5:3 G4+Bb4+Eb5:3
G4+Bb4+E5:5 R:1
Ab4+C5+F5:3 C5+Eb5+Ab5:3
Bb4+Db5+G5:3 Ab4+C5+F5:3
G4+Bb4+Eb5:3 F4+Ab4+Db5:3
G4+Bb4+E5:5 R:1
C5+Eb5+Ab5:2 Db5+F5+Bb5:2 C5+Eb5+Ab5:2
Bb4+Db5+G5:2 C5+Eb5+Ab5:2 Bb4+Db5+G5:2
Ab4+C5+F5:2 Bb4+Db5+G5:2 Ab4+C5+F5:2
G4+Bb4+E5:3 Ab4+C5+F5:2 R:1
C5+Eb5+Ab5:3 Bb4+Db5+G5:3
Bb4+Db5+G5:3 Ab4+C5+F5:3
G4+Bb4+E5:3 Bb4+C5+G5:3
Ab4+C5+F5:5 R:1
Ab4+C5+F5:3 G4+Bb4+Eb5:3
F4+Ab4+Db5:3 G4+Bb4+E5:3
Ab4+C5+F5:4 G4+Bb4+Eb5:1 R:1
Ab4+C5+G5:6''',
 lh='''Ab2:6
Bb2:6
C3:6
Db3:5 R:1
Eb3:6
Ab2:6
Bb2:3 Eb3:3
C3:5 R:1
Db3:6
Bb2:6
Ab2:3 Bb2:3
C3:5 R:1
Ab2:6
Bb2:6
Db3:6
C3:3 Db3:2 R:1
Ab2:6
Bb2:6
C3:6
Db3:5 R:1
F2:3 G2:3
Ab2:3 C3:3
Db3:4 C3:1 R:1
F2:6''',
 lh_upper='''F3:1 Ab3:1 G3:1 C3:3
Eb3:2 G3:1 F3:1 Db3:2
E3:2 G3:1 Bb3:1 G3:2
F3:2 Ab3:1 C4:2 R:1
G3:2 Bb3:1 Db4:1 C4:2
F3:2 Ab3:1 G3:1 C3:2
Db3:2 F3:1 G3:1 Bb3:2
E3:3 G3:2 R:1
F3:2 Ab3:1 C4:1 Bb3:2
F3:2 G3:1 Ab3:1 Db3:2
C3:2 Eb3:1 Db3:1 F3:2
E3:2 G3:1 Bb3:2 R:1
F3:.5 G3:.5 Ab3:1 G3:1 F3:1 Eb3:1 C3:1
Db3:.5 Eb3:.5 F3:1 G3:1 Ab3:1 G3:1 F3:1
Ab3:.5 Bb3:.5 C4:1 Bb3:1 Ab3:1 F3:1 Eb3:1
E3:1 G3:1 Bb3:1 Ab3:1 F3:1 R:1
F3:1 Ab3:1 G3:1 C3:3
Eb3:2 G3:1 F3:1 Db3:2
E3:2 G3:1 Bb3:1 G3:2
F3:2 Ab3:1 C4:2 R:1
C3:2 Eb3:1 D3:1 F3:2
Eb3:2 F3:1 E3:1 G3:2
F3:2 Ab3:1 G3:1 E3:1 R:1
C3:2 Eb3:1 F3:3''',
 tempos=[54,55,53,49,55,54,53,49,54,55,53,48,57,58,56,50,53,54,52,48,51,50,47,47],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],sections={1:'pp',13:'p',17:'pp'},lower_sections={1:'p',13:'mp',17:'p',21:'pp'},
 pedal=[[i*6+a,i*6+b-.2] for i in range(24) for a,b in ([(0,3),(3,5)] if i in [3,7,11,15,19,22] else [(0,3),(3,6)])])
PIECES[-1]['performance']['tenor_entries']=[[0,144]]
study(op=259,title='Willow Mooring',key='g',fifths=-2,meter='3/4',bpm=48,parent=242,
 source=dict(source_opus=242,source_hand='rh',source_start_beat=80,source_end_beat=84,source_pitches=['G','Bb','A','F'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['G','Bb','A','F']),
 description='Small chords arrive like delayed answers in a slow three-beat dance. A minor melody moves through sixths and ninths, sometimes held across the next bass change. The centre briefly brightens, and the return leaves more empty beats before coming to rest on E-flat-major colour.',
 technical='Every attack is chordal, but the upper note should remain a continuous tune. Several chords enter half a beat late or sustain into the next bar. Release fully into the written rests; the pedal does not bridge those shared silences.',
 rh='''D4+G4:.5 F4+Bb4:.5 E4+A4:1 C4+F4:1
D4+G4+Bb4:1.5 C4+F4+A4:.5 Eb4+G4+Bb4:1
R:.5 F4+A4+C5:1.5 Eb4+G4+Bb4:1~
Eb4+G4+Bb4:1 D4+F4+A4:1 C4+Eb4+G4:1
D4+G4+Bb4:2 R:1
R:.5 G4+Bb4+D5:1.5 F4+A4+C5:1
Eb4+G4+Bb4:1 D4+F4+A4:.5 C4+Eb4+G4:1.5
D4+F4+Bb4:1 E4+G4+C5:2~
E4+G4+C5:1 F4+A4+D5:1 Eb4+G4+C5:1
D4+F4+Bb4:2 R:1
G4+Bb4+Eb5:1 F4+A4+D5:1 Eb4+G4+C5:1
R:.5 F4+A4+C5:1.5 G4+Bb4+D5:1
G4+B4+E5:1.5 F4+A4+D5:.5 E4+G4+C5:1
F4+A4+D5:1 G4+B4+E5:1 A4+C5+F5:1
G4+Bb4+Eb5:2 R:1
F4+A4+D5:1 Eb4+G4+C5:1 D4+F4+Bb4:1
D4+G4:.5 F4+Bb4:.5 E4+A4:1 C4+F4:1
D4+G4+Bb4:1.5 C4+F4+A4:.5 Eb4+G4+Bb4:1
R:.5 F4+A4+C5:1.5 Eb4+G4+Bb4:1~
Eb4+G4+Bb4:1 D4+F4+A4:1 C4+Eb4+G4:1
D4+G4+Bb4:2 R:1
R:1 G4+Bb4+D5:2
F4+A4+C5:1 Eb4+G4+Bb4:2~
Eb4+G4+Bb4:1 D4+F4+A4:1 R:1
R:.5 C4+Eb4+G4:1.5 D4+F4+A4:1
Eb4+G4+Bb4:1 F4+A4+C5:2
G4+Bb4+D5:1 F4+A4+C5:.5 Eb4+G4+Bb4:1.5
D4+F4+A4:2 R:1
C4+Eb4+G4:1 Eb4+G4+Bb4:1 F4+A4+C5:1
Eb4+G4+Bb4:1 D4+F4+A4:2
C4+Eb4+G4:1 D4+F4+A4:1 R:1
D4+G4+Bb4:3''',
 lh='''G2+D3:1 Eb3+Bb3:.5 D3+A3:.5 C3+G3:1
Bb2+F3:1.5 A2+E3:.5 G2+D3:1
F3+C4:1.5 Eb3+Bb3:.5 C3+G3:1
Ab2+Eb3:1 Bb2+F3:1 C3+G3:1
G2+D3:2 R:1
Eb3+Bb3:1.5 D3+A3:.5 C3+G3:1
Ab2+Eb3:1 Bb2+F3:.5 C3+G3:1.5
Bb2+F3:1 C3+G3:2
A2+E3:1 D3+A3:1 C3+G3:1
Bb2+F3:2 R:1
Eb3+Bb3:1 D3+A3:1 C3+G3:1
F2+C3:1.5 G2+D3:.5 Bb2+F3:1
C3+G3:1.5 B2+F#3:.5 A2+E3:1
D3+A3:1 C3+G3:1 F3+C4:1
Eb3+Bb3:2 R:1
Bb2+F3:1 Ab2+Eb3:1 G2+D3:1
Eb3+Bb3:1 C3+G3:.5 Bb2+F3:.5 A2+E3:1
G2+D3:1.5 F2+C3:.5 Eb3+Bb3:1
D3+A3:1.5 C3+G3:.5 Bb2+F3:1
Ab2+Eb3:1 Bb2+F3:1 C3+G3:1
G2+D3:2 R:1
R:1 Eb3+Bb3:2
D3+A3:1 C3+G3:2
Ab2+Eb3:1 Bb2+F3:1 R:1
C3+G3:1.5 D3+A3:.5 Bb2+F3:1
Eb3+Bb3:1 F3+C4:2
G2+D3:1 F2+C3:.5 Eb3+Bb3:1.5
D3+A3:2 R:1
C3+G3:1 Ab2+Eb3:1 F2+C3:1
G2+D3:1 Bb2+F3:2
Ab2+Eb3:1 Bb2+F3:1 R:1
Eb3+Bb3:3''',
 tempos=[48,49,47,46,43,48,49,48,46,42,49,50,52,53,47,46,48,49,47,45,42,46,47,43,46,48,47,42,45,44,41,41],
 phrases=[(1,5),(6,10),(11,16),(17,21),(22,24),(25,28),(29,32)],sections={1:'p',11:'p',13:'mp',17:'p',22:'pp',29:'pp'},
 pedal=sorted([[i*3,i*3+(1.8 if i in [4,9,14,20,23,27,30] else 2.8)] for i in range(32) if i!=21]+[[64,65.8]]))

study(op=260,title='Pearl Stillwater',key='d',fifths=-1,meter='7/4',bpm=60,parent=250,
 source=dict(source_opus=250,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['D','C','A','G'],transposition_semitones=0),motif=dict(hand='rh',voice='inner',start_beat=0,end_beat=7,pitches=['D','C','A','G']),
 description='An inner melody moves beneath a suspended upper light. Seven slow beats give each harmony room to change its meaning. A brief flowing interior opens into a return over different bass notes, ending with the inner voice alone above the remaining open fifth.',
 technical='Balance three layers: the sustained upper note, the quieter bass shells and the foreground inner melody. Hold only the written durations; the RH spans remain within an octave. The seven-beat measures breathe in changing groups rather than equal accents.',
 rh='''E5:7
D5:7
C5:7
Bb4:6 R:1
G5:7
F5:7
E5:7
D5:6 R:1
A5:7
G5:7
F5:7
E5:6 R:1
G5:3 F5:4
F5:3 E5:4
E5:3 D5:4
D5:6 R:1
E5:7
D5:7
C5:7
Bb4:6 R:1
D5:7
C5:7
Bb4:6 R:1
A4:3 R:4''',
 rh_inner='''D5:1 C5:2 A4:2 G4:2
C5:2 Bb4:1 G4:2 F4:2
Bb4:1 A4:2 F4:2 E4:2
A4:2 G4:2 E4:1 D4:1 R:1
F5:2 E5:1 C5:2 B4:2
E5:1 D5:2 Bb4:2 A4:2
D5:2 C5:1 A4:2 G4:2
C5:2 A4:2 G4:1 F4:1 R:1
G5:1 F5:2 D5:2 C5:2
F5:2 E5:1 C5:2 B4:2
E5:1 D5:2 Bb4:2 A4:2
D5:2 C5:2 A4:1 G4:1 R:1
F5:.5 E5:.5 D5:1 C5:1 A4:1 C5:1 D5:2
E5:.5 D5:.5 C5:1 Bb4:1 G4:1 Bb4:1 C5:2
D5:.5 C5:.5 Bb4:1 A4:1 F4:1 A4:1 C5:2
C5:1 A4:1 G4:2 F4:2 R:1
D5:1 C5:2 A4:2 G4:2
C5:2 Bb4:1 G4:2 F4:2
Bb4:1 A4:2 F4:2 E4:2
A4:2 G4:2 E4:1 D4:1 R:1
C5:1 Bb4:2 A4:2 F4:2
Bb4:2 A4:1 G4:2 E4:2
A4:1 G4:2 F4:2 E4:1 R:1
G4:1 F4:2 E4:1 D4:3''',
 lh='''D3+A3:3 F3+C4:2 G3+D4:2
Bb2+F3:3 C3+G3:2 D3+A3:2
C3+G3:3 D3+A3:2 E3+B3:2
G2+D3:3 A2+E3:3 R:1
F3+C4:3 G3+D4:2 E3+B3:2
D3+A3:3 Eb3+Bb3:2 F3+C4:2
Bb2+F3:3 C3+G3:2 A2+E3:2
D3+A3:3 C3+G3:3 R:1
G3+D4:3 F3+C4:2 Eb3+Bb3:2
C3+G3:3 D3+A3:2 E3+B3:2
Bb2+F3:3 C3+G3:2 D3+A3:2
A2+E3:3 C3+G3:3 R:1
D3+A3:3 F3+C4:2 Bb2+F3:2
C3+G3:3 Eb3+Bb3:2 G2+D3:2
Bb2+F3:3 D3+A3:2 G2+D3:2
A2+E3:3 C3+G3:3 R:1
Bb2+F3:3 G2+D3:2 A2+E3:2
A2+E3:3 G2+D3:2 F2+C3:2
G2+D3:3 A2+E3:2 C3+G3:2
D3+A3:3 A2+E3:3 R:1
Bb2+F3:3 D3+A3:2 F3+C4:2
C3+G3:3 Bb2+F3:2 A2+E3:2
G2+D3:3 A2+E3:3 R:1
D3+A3:7''',
 tempos=[60,61,60,56,61,62,60,55,62,63,61,56,64,65,63,57,59,60,58,54,57,55,52,52],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],sections={1:'pp',9:'p',13:'p',17:'pp'},
 pedal=[[i*7+a,i*7+b-.2] for i in range(24) for a,b in ([(0,3),(3,6)] if i in [3,7,11,15,19,22] else [(0,3),(3,5),(5,7)])])
PIECES[-1]['performance']['inner_entries']=[[0,168]]

study(op=261,title='Linden Waterwheel',key='a',fifths=0,meter='4/4',bpm=62,parent=255,
 source=dict(source_opus=255,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['A','C','B','E'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['A','C','B','E']),
 description='A small turning figure grows over E, G and F bass anchors. The first melody leaves long gaps; the central variations fill those gaps with flowing detail without changing the harmonic ground. At the return the wheel keeps moving beneath a much simpler song.',
 technical='Let the increasing subdivisions create momentum without an increase in weight. The left hand passes from spacious shells to eighths and short sixteenth turns. The final four bars return to the opening tempo, with the last figure continuing quietly into silence.',
 rh='''A4:.75 C5:.25 B4:1 E5:2
D5:1 B4:1 G4:2
B4:.75 D5:.25 C5:1 G5:2
F5:1 D5:1 B4:2
A4:.75 C5:.25 E5:1 G5:2~
G5:1 E5:.5 D5:.5 C5:1 A4:1
B4:1 D5:.5 E5:.5 G5:1 F5:1
E5:2 D5:1 R:1
A4:.5 C5:.5 B4:.5 E5:.5 D5:1 B4:1
G4:.5 B4:.5 D5:.5 E5:.5 G5:1 E5:1
B4:.5 D5:.5 C5:.5 G5:.5 F5:1 D5:1
B4:.5 C5:.5 D5:.5 F5:.5 E5:1 C5:1
A4:.5 C5:.5 E5:.5 G5:.5 A5:1 G5:1
E5:.5 D5:.5 C5:.5 A4:.5 B4:1 D5:1
E5:.5 G5:.5 F5:.5 E5:.5 D5:1 B4:1
C5:1 B4:.5 A4:.5 G4:1 R:1
A4:.25 B4:.25 C5:.5 E5:.5 G5:.5 A5:1 G5:.5 E5:.5
D5:.25 E5:.25 G5:.5 B5:.5 A5:.5 G5:1 E5:.5 D5:.5
B4:.25 C5:.25 D5:.5 G5:.5 A5:.5 B5:1 A5:.5 G5:.5
F5:.25 G5:.25 A5:.5 C6:.5 B5:.5 A5:1 G5:.5 E5:.5
E5:.5 G5:.5 A5:.5 G5:.5 E5:1 D5:.5 C5:.5
D5:.5 E5:.5 G5:.5 F5:.5 E5:1 R:1
A4:.75 C5:.25 B4:1 E5:2
D5:1 B4:1 G4:2
B4:.75 D5:.25 C5:1 G5:2
F5:1 D5:1 B4:2
A4:.75 C5:.25 E5:1 G5:2
E5:1 D5:1 C5:1 R:1
B4:1 D5:1 E5:2
G4:1 B4:.5 D5:.5 E5:2
A4:1 C5:1 B4:1 G4:1
A4:.75 C5:.25 B4:1 E5:1 R:1''',
 lh='''E3:1 B3:1 G3+D4:2
E3:1 G3+B3:2 D3:1
G2:1 D3:1 B3+E4:2
G3:1 B3+D4:2 F3:1
F3:1 C4:1 A3+E4:2
F3:1 A3+C4:2 E3:1
E3:1 B3:1 G3+D4:2
E3:1 G3+B3:2 R:1
E3:.5 B3:.5 G3:.5 D4:.5 B3:1 G3:1
E3:.5 B3:.5 G3:.5 A3:.5 B3:1 D3:1
G3:.5 D4:.5 B3:.5 E4:.5 D4:1 B3:1
G3:.5 D4:.5 B3:.5 C4:.5 D4:1 F3:1
F3:.5 C4:.5 A3:.5 E4:.5 C4:1 A3:1
F3:.5 C4:.5 A3:.5 G3:.5 A3:1 E3:1
E3:.5 B3:.5 G3:.5 D4:.5 B3:1 G3:1
E3:.5 B3:.5 G3:.5 A3:.5 B3:1 R:1
E3:.5 G3:.25 A3:.25 B3:.5 D4:.5 E4:.5 D4:.5 B3:.5 G3:.5
E3:.5 G3:.25 A3:.25 B3:.5 D4:.5 E4:.5 G4:.5 E4:.5 D4:.5
G3:.5 B3:.25 C4:.25 D4:.5 E4:.5 G4:.5 E4:.5 D4:.5 B3:.5
F3:.5 A3:.25 B3:.25 C4:.5 E4:.5 F4:.5 E4:.5 C4:.5 A3:.5
F3:.5 A3:.25 B3:.25 C4:.5 E4:.5 G4:.5 E4:.5 C4:.5 A3:.5
E3:.5 G3:.25 A3:.25 B3:.5 D4:.5 E4:1 R:1
E3:.5 G3:.5 B3:.5 D4:.5 B3:.5 G3:.5 B3:.5 G3:.5
E3:.5 G3:.5 B3:.5 D4:.5 B3:.5 A3:.5 G3:.5 D3:.5
G3:.5 B3:.5 D4:.5 E4:.5 D4:.5 B3:.5 D4:.5 B3:.5
G3:.5 B3:.5 D4:.5 F4:.5 D4:.5 B3:.5 A3:.5 G3:.5
F3:.5 A3:.5 C4:.5 E4:.5 C4:.5 A3:.5 C4:.5 A3:.5
F3:.5 A3:.5 C4:.5 E4:.5 D4:1 R:1
E3:1 B3:1 G3+D4:2
G3:1 D4:1 B3+E4:2
F3:1 C4:1 A3+E4:2
E3:.75 G3:.25 B3:1 E4:1 R:1''',
 tempos=[62,63,62,61,62,63,61,58,63,64,63,62,64,65,63,59,66,67,66,67,65,59,63,64,63,62,63,58,61,61,60,60],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,22),(23,28),(29,32)],sections={1:'p',9:'p',17:'mf',23:'p',29:'pp'},lower_sections={1:'pp',9:'p',17:'mp',23:'pp'},
 pedal=[[i*4,i*4+(2.8 if i in [7,15,21,27,31] else 3.8)] for i in range(32)])

study(op=262,title='Sedge Undertide',key='d',fifths=-1,meter='12/8',bpm=62,parent=251,
 source=dict(source_opus=251,source_hand='rh',source_start_beat=.5,source_end_beat=4,source_pitches=['D','F','E','A'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['D','F','E','A']),
 description='A long-short melody sways above a four-pulse bass. The middle introduces even quarter-note steps against that compound pulse, then brief running figures. Five-bar sentences return to a low register, and the last bass reply settles while the upper ninth remains open.',
 technical='Keep the dotted-quarter pulse gentle. In the middle, even quarters cross its accents without changing speed; the following eighths should feel like a release. The final three measures are a separate low-register reply, without a ritardando.',
 rh='''D5:1 F5:.5 E5:1.5 A4:3
C5:1 E5:.5 G5:1.5 F5:1 E5:.5 D5:1.5
C5:1 A4:.5 G4:1.5 A4:3~
A4:1.5 C5:1 D5:.5 E5:1.5 G5:1.5
F5:1 E5:.5 D5:3 R:1.5
D5:1 F5:.5 E5:1.5 A5:3
G5:1 E5:.5 D5:1.5 C5:1 D5:.5 F5:1.5
E5:1 C5:.5 A4:1.5 G4:3~
G4:1.5 A4:1 C5:.5 D5:1.5 E5:1.5
C5:1 B4:.5 A4:3 R:1.5
D5:1 E5:1 F5:1 A5:1 G5:1 E5:1
C5:1 D5:1 E5:1 G5:1 F5:1 D5:1
Bb4:1 C5:1 D5:1 F5:1 E5:1 C5:1
A4:.5 C5:.5 E5:.5 G5:.5 A5:.5 G5:.5 E5:1 D5:.5 C5:1.5
Bb4:.5 D5:.5 F5:.5 A5:.5 Bb5:.5 A5:.5 G5:1 F5:.5 E5:1.5
D5:.5 E5:.5 F5:.5 A5:.5 G5:.5 E5:.5 D5:1.5 R:1.5
D5:1 F5:.5 E5:1.5 A4:3
C5:1 E5:.5 G5:1.5 F5:1 E5:.5 D5:1.5
C5:1 A4:.5 G4:1.5 F4:3
E4:1 G4:.5 A4:1.5 C5:1.5 B4:1.5
A4:1 G4:.5 F4:3 R:1.5
E4:1 G4:.5 A4:1.5 C5:3
B4:1 A4:.5 G4:1.5 E4:3
F4+A4+E5:6''',
 lh='''D3:1.5 A3:1.5 F3:1.5 C4:1.5
C3:1.5 G3:1.5 E3:1.5 Bb3:1.5
F3:1.5 C4:1.5 A3:1.5 E3:1.5
A2:1.5 E3:1.5 G3:1.5 C4:1.5
D3:1.5 A3:1.5 F3:1.5 R:1.5
Bb2:1.5 F3:1.5 D3:1.5 A3:1.5
C3:1.5 G3:1.5 E3:1.5 Bb3:1.5
F3:1.5 C4:1.5 A3:1.5 G3:1.5
E3:1.5 B3:1.5 G3:1.5 D3:1.5
A2:1.5 E3:1.5 C4:1.5 R:1.5
D3:1 A3:.5 F3:1 A3:.5 C4:1 A3:.5 F3:1 E3:.5
C3:1 G3:.5 E3:1 G3:.5 Bb3:1 G3:.5 E3:1 D3:.5
Bb2:1 F3:.5 D3:1 F3:.5 A3:1 F3:.5 D3:1 C3:.5
F3:1.5 C4:1 A3:.5 E4:1.5 C4:1 A3:.5
G3:1.5 D4:1 Bb3:.5 F4:1.5 D4:1 Bb3:.5
A3:1.5 E4:1 C4:.5 G3:1.5 R:1.5
D3:1 A3:.5 F3:1 A3:.5 C4:1 A3:.5 F3:1 E3:.5
C3:1 G3:.5 E3:1 G3:.5 Bb3:1 G3:.5 E3:1 D3:.5
Bb2:1 F3:.5 D3:1 F3:.5 A3:1 F3:.5 D3:1 C3:.5
A2:1 E3:.5 C3:1 E3:.5 G3:1 E3:.5 C3:1 B2:.5
D3:1 A3:.5 F3:1 A3:.5 C4:1.5 R:1.5
C3:1.5 G3:1.5 E3:3
A2:1.5 E3:1.5 G3:3
D3:1 A3:.5 F3:1 E3:.5 D3:3''',
 tempos=[62,63,62,61,57,63,64,62,61,57,64,65,64,66,67,58,62,63,61,60,56,59,59,59],
 phrases=[(1,5),(6,10),(11,16),(17,21),(22,24)],sections={1:'p',6:'p',11:'mp',14:'mf',17:'p',22:'pp'},lower_sections={1:'pp',11:'p',17:'pp'},
 pedal=[[i*6+a,i*6+b-.2] for i in range(24) for a,b in ([(0,3),(3,4.5)] if i in [4,9,15,20] else [(0,3),(3,6)])])

study(op=263,title='Alder Sluice',key='g',fifths=-2,meter='4/4',bpm=56,parent=253,
 source=dict(source_opus=253,source_hand='rh',source_start_beat=0,source_end_beat=7,source_pitches=['G','Bb','A','D'],transposition_semitones=0),motif=dict(hand='rh',start_beat=1,end_beat=4,pitches=['G','Bb','A','D']),
 description='A late melody crosses a repeating lower figure whose dotted notes resist the bar accents. G, E-flat and C remain the three familiar places while the melody grows into longer ribbons. The original late entry returns, followed by a seven-bar descent to a bare fifth.',
 technical='Keep the three dotted eighths light and equal within the lower pattern; avoid accenting its restart. The right hand grows from isolated phrases into eight-note lines. Leave the shared breaths completely clear of pedal.',
 rh='''R:1 G4:1 Bb4:.5 A4:.5 D5:1
C5:1.5 Bb4:.5 G4:2
A4:.5 C5:.5 Eb5:1 D5:2~
D5:1 C5:.5 Bb4:.5 A4:1 G4:1
F4:1 A4:1 G4:1 R:1
R:.5 Bb4:.5 D5:1 F5:2
Eb5:1.5 D5:.5 Bb4:2
C5:.5 Eb5:.5 G5:1 F5:2~
F5:1 Eb5:.5 D5:.5 C5:1 Bb4:1
A4:1 C5:1 Bb4:1 R:1
G4:.5 Bb4:.5 D5:.5 F5:.5 G5:.5 F5:.5 D5:.5 Bb4:.5
C5:.5 Eb5:.5 G5:.5 Bb5:.5 A5:.5 G5:.5 F5:.5 Eb5:.5
D5:.5 F5:.5 A5:.5 C6:.5 Bb5:.5 A5:.5 G5:.5 F5:.5
Eb5:.5 G5:.5 Bb5:.5 A5:.5 G5:1 F5:.5 Eb5:.5
D5:.5 F5:.5 A5:.5 G5:.5 F5:1 Eb5:.5 D5:.5
C5:1 Bb4:.5 A4:.5 G4:1 R:1
R:1 G4:1 Bb4:.5 A4:.5 D5:1
C5:1.5 Bb4:.5 G4:2
A4:.5 C5:.5 Eb5:1 D5:2~
D5:1 C5:.5 Bb4:.5 A4:1 G4:1
F4:1 A4:1 G4:1 R:1
Bb4:1 A4:.5 G4:.5 F4:2
A4:1 G4:.5 F4:.5 Eb4:2
G4:1 F4:.5 Eb4:.5 D4:2
F4:1 Eb4:.5 D4:.5 C4:2
Eb4:1 D4:.5 C4:.5 Bb3:1 R:1
D4:1 F4:1 Eb4:1 C4:1
D4+G4:4''',
 lh='''G3:.75 D4:.75 Bb3:.75 D4:.75 F3:1
G3:.75 D4:.75 Bb3:.75 C4:.75 D3:1
Eb3:.75 Bb3:.75 G3:.75 Bb3:.75 D3:1
C3:.75 G3:.75 Eb3:.75 G3:.75 Bb2:1
G2:.75 D3:.75 Bb2:.5 D3:1 R:1
G3:.75 D4:.75 Bb3:.75 D4:.75 F3:1
Eb3:.75 Bb3:.75 G3:.75 Bb3:.75 D3:1
C3:.75 G3:.75 Eb3:.75 G3:.75 Bb2:1
Eb3:.75 Bb3:.75 G3:.75 A3:.75 Bb2:1
F3:.75 C4:.75 A3:.5 C4:1 R:1
G3:.5 Bb3:.25 C4:.25 D4:.5 F4:.5 D4:.5 Bb3:.5 A3:.5 G3:.5
Eb3:.5 G3:.25 A3:.25 Bb3:.5 D4:.5 Bb3:.5 G3:.5 F3:.5 Eb3:.5
D3:.5 F3:.25 G3:.25 A3:.5 C4:.5 A3:.5 F3:.5 E3:.5 D3:.5
Eb3:.5 G3:.25 A3:.25 Bb3:.5 D4:.5 Eb4:.5 D4:.5 Bb3:.5 G3:.5
C3:.5 Eb3:.25 F3:.25 G3:.5 Bb3:.5 C4:.5 Bb3:.5 G3:.5 Eb3:.5
D3:.5 F3:.5 A3:.5 C4:.5 Bb3:1 R:1
Eb3:.75 Bb3:.75 G3:.75 Bb3:.75 D3:1
C3:.75 G3:.75 Eb3:.75 G3:.75 Bb2:1
Eb3:.75 Bb3:.75 G3:.75 Bb3:.75 D3:1
D3:.75 A3:.75 F3:.75 A3:.75 C3:1
G2:.75 D3:.75 Bb2:.5 D3:1 R:1
G2:1 D3:1 Bb2:2
F2:1 C3:1 A2:2
Eb2:1 Bb2:1 G2:2
D2:1 A2:1 F2:2
C2:1 G2:1 Eb2:1 R:1
Bb2:1 F3:1 A2:1 E3:1
G2+D3:4''',
 tempos=[56,57,56,55,51,57,58,57,55,51,59,60,61,60,58,52,56,57,56,54,50,54,54,53,53,49,52,52],
 phrases=[(1,5),(6,10),(11,16),(17,21),(22,28)],sections={1:'p',6:'p',11:'mf',17:'p',22:'pp'},lower_sections={1:'pp',11:'mp',17:'pp'},
 pedal=[[i*4,i*4+(2.8 if i in [4,9,15,20,25] else 3.8)] for i in range(28)])

study(op=264,title='Orchid Floodplain',key='f',fifths=-4,meter='5/4',bpm=60,parent=258,
 source=dict(source_opus=258,source_hand='lh',source_voice='tenor',source_start_beat=0,source_end_beat=6,source_pitches=['F','Ab','G','C'],transposition_semitones=0),motif=dict(hand='lh',start_beat=0,end_beat=5,pitches=['F','Ab','G','C']),
 description='The tune begins in the left hand under a quiet suspended chord. It rises into the treble while the bass becomes a repeated figure; at the crest both hands move through their own versions. The last phrase returns the tune below, but finds D-flat beneath the final C.',
 technical='Exchange the foreground between hands at bars 7 and 19. Unequal five-beat shapes must keep their long line. At the central crest the short lower turns remain softer than the right-hand answer; they are not accents or tempo changes.',
 rh='''G4+C5:5
F4+Bb4:3 Eb4+Ab4:2
Eb4+G4:2 Db4+F4:3
F4+Ab4:3 G4+Bb4:2
Ab4+C5:2 G4+Bb4:2 F4+Ab4:1
Eb4+G4:3 F4+Ab4:1 R:1
F5:1 Ab5:.5 G5:.5 C5:3
Eb5:1 G5:.5 F5:.5 Bb4:3
Db5:1 F5:.5 Eb5:.5 Ab4:3
C5:1 Eb5:.5 Db5:.5 F5:2 G5:1
Ab5:1 G5:.5 F5:.5 Eb5:1 C5:2
Db5:1 Eb5:1 F5:2 R:1
F5:.5 G5:.5 Ab5:.5 C6:.5 Bb5:1 Ab5:.5 G5:.5 F5:1
Eb5:.5 F5:.5 G5:.5 Bb5:.5 Ab5:1 G5:.5 F5:.5 Eb5:1
Db5:.5 Eb5:.5 F5:.5 Ab5:.5 G5:1 F5:.5 Eb5:.5 Db5:1
C5:.5 Db5:.5 Eb5:.5 G5:.5 F5:1 Eb5:.5 Db5:.5 C5:1
F5:1 Ab5:.5 G5:.5 C6:1 Bb5:.5 Ab5:.5 G5:1
F5:1 Eb5:.5 Db5:.5 C5:2 R:1
G4+C5:5
F4+Bb4:3 Eb4+Ab4:2
Eb4+G4:2 Db4+F4:3
F4+Ab4:3 G4+Bb4:2
Ab4+C5:2 G4+Bb4:1 F4+Ab4:1 R:1
C5:5''',
 lh='''F3:1 Ab3:.5 G3:.5 C3:3
Eb3:1 G3:.5 F3:.5 Bb2:3
Db3:1 F3:.5 Eb3:.5 Ab2:3
C3:1 Eb3:.5 Db3:.5 F3:2 G3:1
Ab3:1 G3:.5 F3:.5 Eb3:1 C3:2
Db3:1 Eb3:1 F3:2 R:1
F3:.75 C4:.25 Ab3:.5 G3:.5 F3:1 C3:2
Eb3:.75 Bb3:.25 G3:.5 F3:.5 Eb3:1 Bb2:2
Db3:.75 Ab3:.25 F3:.5 Eb3:.5 Db3:1 Ab2:2
C3:.75 G3:.25 Eb3:.5 Db3:.5 C3:1 G2:2
Db3:.75 Ab3:.25 F3:.5 Eb3:.5 Db3:1 F3:2
C3:.75 G3:.25 Bb3:.5 G3:.5 F3:2 R:1
F3:.5 Ab3:.25 Bb3:.25 C4:.5 Eb4:.5 F4:1 Eb4:.5 C4:.5 Ab3:1
Eb3:.5 G3:.25 Ab3:.25 Bb3:.5 Db4:.5 Eb4:1 Db4:.5 Bb3:.5 G3:1
Db3:.5 F3:.25 G3:.25 Ab3:.5 C4:.5 Db4:1 C4:.5 Ab3:.5 F3:1
C3:.5 Eb3:.25 F3:.25 G3:.5 Bb3:.5 C4:1 Bb3:.5 G3:.5 Eb3:1
Db3:.5 F3:.5 Ab3:.5 C4:.5 Db4:1 C4:.5 Ab3:.5 F3:1
C3:.5 Eb3:.5 G3:.5 Bb3:.5 F3:2 R:1
F3:1 Ab3:.5 G3:.5 C3:3
Eb3:1 G3:.5 F3:.5 Bb2:3
Db3:1 F3:.5 Eb3:.5 Ab2:3
C3:1 Eb3:.5 Db3:.5 F3:2 G3:1
Ab3:1 G3:.5 F3:.5 Eb3:1 C3:1 R:1
Db3+Ab3:5''',
 tempos=[60,61,60,59,60,55,61,62,61,60,61,55,63,64,63,64,62,55,59,60,59,57,53,53],
 phrases=[(1,6),(7,12),(13,18),(19,24)],sections={1:'pp',7:'p',13:'mf',19:'pp'},lower_sections={1:'p',7:'pp',13:'mp',19:'p',24:'pp'},
 pedal=[[i*5+a,i*5+b-.2] for i in range(24) for a,b in ([(0,2),(2,4)] if i in [5,11,17,22] else [(0,2),(2,5)])])

study(op=265,title='Bracken Overflow',key='d',fifths=-1,meter='4/4',bpm=60,parent=260,
 source=dict(source_opus=260,source_hand='rh',source_voice='inner',source_start_beat=0,source_end_beat=7,source_pitches=['D','C','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','C','A','G']),
 description='A descending four-note thought gradually spills into its surrounding beats. A seven-bar opening and a shorter answer lead to eight bars of triplet turns over even eighths. The return removes the ornament, then the lower line continues after the treble has said its last word.',
 technical='Keep triplet eighths distinct from the even LH eighths at bars 13–20. Each little turn belongs to a larger phrase and should not receive an extra accent. At the close the RH releases before the bass completes its quiet descending answer.',
 rh='''D5:1 C5:.5 A4:.5 G4:2
A4:1 C5:.5 D5:.5 F5:2~
F5:1 E5:.5 D5:.5 C5:1 A4:1
Bb4:1 D5:.5 F5:.5 E5:2
D5:1 C5:.5 A4:.5 G4:2
A4:.5 C5:.5 D5:1 E5:1 G5:1
F5:2 E5:1 R:1
G5:1 F5:.5 D5:.5 C5:2
D5:1 F5:.5 G5:.5 A5:2
Bb5:1 A5:.5 G5:.5 F5:1 D5:1
E5:.5 G5:.5 A5:1 G5:1 E5:1
D5:2 C5:1 R:1
D5:1/3 E5:1/3 F5:1/3 A5:.5 G5:.5 F5:.5 E5:.5 D5:1
C5:1/3 D5:1/3 E5:1/3 G5:.5 F5:.5 E5:.5 D5:.5 C5:1
Bb4:1/3 C5:1/3 D5:1/3 F5:.5 E5:.5 D5:.5 C5:.5 Bb4:1
A4:1/3 B4:1/3 C5:1/3 E5:.5 D5:.5 C5:.5 B4:.5 A4:1
D5:1/3 E5:1/3 F5:1/3 A5:.5 C6:.5 Bb5:.5 A5:.5 G5:1
F5:1/3 G5:1/3 A5:1/3 C6:.5 Bb5:.5 A5:.5 G5:.5 F5:1
E5:1/3 F5:1/3 G5:1/3 Bb5:.5 A5:.5 G5:.5 F5:.5 E5:1
D5:1/3 E5:1/3 F5:1/3 A5:1 G5:1 R:1
D5:1 C5:.5 A4:.5 G4:2
A4:1 C5:.5 D5:.5 F5:2~
F5:1 E5:.5 D5:.5 C5:1 A4:1
Bb4:1 D5:.5 F5:.5 E5:2
D5:1 C5:.5 A4:.5 G4:2
A4:2 G4:1 R:1
F4+A4:2 E4+G4:1 D4+F4:1
E4+G4:2 G4+Bb4:1 A4+C5:1
Bb4+D5:1 A4+C5:1 G4+Bb4:1 F4+A4:1
E4+G4:2 F4+A4:2
D5:1 C5:1 A4:2
G4:1 F4:1 E4:1 R:1''',
 lh='''D3:1 A3:1 F3:2
C3:1 G3:1 E3:2
Bb2:1 F3:1 D3:2
G2:1 D3:1 Bb2:2
D3:1 A3:1 F3:2
C3:1 G3:.5 E3:.5 F3:1 G3:1
A2:1 E3:1 G3:1 R:1
C3:.5 G3:.5 E3:.5 G3:.5 Bb3:1 G3:1
Bb2:.5 F3:.5 D3:.5 F3:.5 A3:1 F3:1
G3:.5 D4:.5 Bb3:.5 D4:.5 F4:1 D4:1
C3:.5 G3:.5 E3:.5 G3:.5 A3:1 B3:1
D3:.5 A3:.5 F3:.5 A3:.5 C4:1 R:1
D3:.5 F3:.5 A3:.5 C4:.5 D4:.5 C4:.5 A3:.5 F3:.5
C3:.5 E3:.5 G3:.5 Bb3:.5 C4:.5 Bb3:.5 G3:.5 E3:.5
Bb2:.5 D3:.5 F3:.5 A3:.5 Bb3:.5 A3:.5 F3:.5 D3:.5
A2:.5 C3:.5 E3:.5 G3:.5 A3:.5 G3:.5 E3:.5 C3:.5
D3:.5 F3:.5 A3:.5 C4:.5 E4:.5 D4:.5 C4:.5 A3:.5
F3:.5 A3:.5 C4:.5 E4:.5 G4:.5 E4:.5 C4:.5 A3:.5
G3:.5 Bb3:.5 D4:.5 F4:.5 A4:.5 F4:.5 D4:.5 Bb3:.5
A3:.5 C4:.5 E4:.5 D4:.5 C4:1 R:1
Bb2:1 F3:.5 D3:.5 A3:2
A2:1 E3:.5 C3:.5 G3:2
G2:1 D3:.5 Bb2:.5 F3:2
C3:1 G3:.5 E3:.5 Bb3:2
D3:1 A3:.5 F3:.5 C4:2
C3:1 G3:1 E3:1 R:1
Bb2+F3:2 C3+G3:2
A2+E3:2 Bb2+F3:2
G2+D3:2 A2+E3:2
C3+G3:2 D3+A3:2
Bb2:1 F3:1 D3:1 A2:1
C3:1 Bb2:1 A2:1 D3:1''',
 tempos=[60,61,60,59,60,61,55,62,63,62,61,55,64,65,64,63,66,67,65,57,60,61,60,58,59,54,57,58,57,55,54,54],
 phrases=[(1,7),(8,12),(13,20),(21,26),(27,32)],sections={1:'p',8:'mp',13:'mp',17:'mf',21:'p',27:'pp'},lower_sections={1:'pp',8:'p',13:'p',17:'mp',21:'pp'},
 tuplet_spans=[dict(hand='rh',start_beat=i*4,end_beat=i*4+1,actual=3,normal=2,stem='down') for i in range(12,20)],
 pedal=[[i*4+a,i*4+b-.2] for i in range(32) for a,b in ([(0,3)] if i in [6,11,19,25] else [(0,2),(2,4)])])

study(op=266,title='Juniper Offing',key='a',fifths=0,meter='6/4',bpm=52,parent=261,
 source=dict(source_opus=261,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['A','C','B','E'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['A','C','B','E']),
 description='Two single lines begin at different moments and gradually learn each other’s melody. Their phrases overlap without a continuous accompaniment. A brief central conversation becomes more animated before the opening returns with the bass speaking first.',
 technical='Shape each hand as a separate singer. The lower entries have their own slurs and dynamic changes; do not shorten a held note just because the other hand begins. Shared silences at the larger boundaries clear the resonance.',
 rh='''A4:1 C5:2 B4:1 E5:2
D5:3 C5:1 B4:1 G4:1
A4:2 B4:1 C5:2 R:1
R:2 E5:1 G5:1 F5:2
E5:2 D5:1 B4:3~
B4:1 C5:1 D5:2 E5:1 G5:1
F5:2 E5:2 D5:1 R:1
C5:1 E5:2 D5:1 G5:2
F5:3 E5:1 D5:1 B4:1
C5:2 B4:1 A4:2 R:1
R:1 E5:.5 G5:.5 A5:1 G5:1 E5:2
D5:1 F5:.5 A5:.5 G5:1 F5:1 D5:2
C5:1 E5:.5 G5:.5 F5:1 E5:1 C5:2
B4:1 D5:.5 F5:.5 E5:1 D5:1 B4:2
C5:1 E5:1 D5:1 B4:2 R:1
R:3 A4:1 C5:1 B4:1
E5:2 D5:2 C5:1 B4:1
G4:2 A4:1 C5:3~
C5:1 B4:1 A4:3 R:1
E5:2 D5:1 C5:3
B4:2 A4:1 G4:3
A4:2 C5:1 B4:3
G4:2 E4:1 F4:2 R:1
E4:2 A4:4''',
 lh='''R:3 A3:1 C4:1 B3:1
E4:2 D4:2 C4:1 B3:1
G3:2 A3:1 C4:2 R:1
A3:1 C4:2 B3:1 E4:2
D4:3 C4:1 B3:1 G3:1
A3:2 B3:1 C4:3~
C4:1 B3:1 A3:3 R:1
R:3 C3:1 E3:1 D3:1
G3:2 F3:2 E3:1 D3:1
B2:2 C3:1 E3:2 R:1
A3:2 C4:1 B3:1 G3:2
R:1 D3:.5 F3:.5 A3:1 G3:1 E3:2
C3:1 E3:.5 G3:.5 B3:1 A3:1 G3:2
F3:1 A3:.5 C4:.5 B3:1 A3:1 F3:2
E3:1 G3:1 B3:1 A3:2 R:1
A3:1 C4:2 B3:1 E4:2
D4:3 C4:1 B3:1 G3:1
A3:2 B3:1 C4:3
E3:2 G3:1 A3:2 R:1
C3:1 E3:2 D3:1 G3:2
F3:3 E3:1 D3:1 B2:1
C3:2 E3:1 G3:3
A2:2 C3:1 D3:2 R:1
E3:2 A2:4''',
 tempos=[52,53,49,52,53,52,48,53,54,49,54,55,54,53,48,52,53,52,48,51,52,50,46,46],
 phrases=[(1,3),(4,7),(8,10),(11,15),(16,19),(20,24)],lower_phrases=[(1,3),(4,7),(8,10),(11,15),(16,19),(20,24)],
 sections={1:'p',4:'pp',8:'p',11:'mp',16:'pp',20:'p',23:'pp'},lower_sections={1:'pp',4:'p',8:'pp',11:'p',16:'p',20:'pp'},
 pedal=[[i*6,i*6+(4.8 if i in [2,6,9,14,18,22] else 5.8)] for i in range(24)])

study(op=267,title='Camellia Soundings',key='c',fifths=-3,meter='4/4',bpm=48,parent=256,
 source=dict(source_opus=256,source_hand='rh',source_voice='upper',source_start_beat=0,source_end_beat=4,source_pitches=['Eb','D','C','Bb'],transposition_semitones=0),motif=dict(hand='rh',voice='upper',start_beat=0,end_beat=4,pitches=['Eb','D','C','Bb']),
 description='Four quiet lines turn a falling melody into changing harmony. The alto enters late, the tenor answers below, and the bass moves least of all. A small central rise gives way to the opening shape over a different foundation; the final voices find E-flat without a dominant flourish.',
 technical='Practise the four lines separately, then balance their overlaps. The inner RH and LH tenor have independent slurs; sustain the other fingers only for their written values. Whole-hand occupation stays within an octave even under held notes.',
 rh='''Eb5:1 D5:1 C5:1 Bb4:1
C5:1.5 Eb5:.5 D5:2
G5:2 F5:1 Eb5:1
D5:2 C5:1 R:1
F5:1 Eb5:1 D5:1 C5:1
D5:1.5 F5:.5 Eb5:2
Ab5:2 G5:1 F5:1
Eb5:2 D5:1 R:1
G5:1 F5:1 Eb5:1 D5:1
Eb5:1.5 G5:.5 F5:2
Bb5:2 Ab5:1 G5:1
F5:2 Eb5:1 R:1
G5:2 F5:2
F5:2 Eb5:2
Eb5:2 D5:2
D5:2 C5:1 R:1
Eb5:1 D5:1 C5:1 Bb4:1
C5:1.5 Eb5:.5 D5:2
G5:2 F5:1 Eb5:1
D5:2 C5:1 R:1
C5:2 Bb4:1 Ab4:1
Bb4:2 C5:1 D5:1
Eb5:1 D5:1 C5:1 R:1
Bb4:4''',
 rh_inner='''R:1 G4:1 F4:2
Ab4:2 G4:1 Bb4:1
C5:1 Bb4:1 Ab4:2
G4:1 Bb4:1 Ab4:1 R:1
R:1 A4:1 G4:2
Bb4:2 A4:1 C5:1
Db5:1 C5:1 Bb4:2
Ab4:1 C5:1 Bb4:1 R:1
R:1 B4:1 Bb4:2
C5:2 Bb4:1 D5:1
Eb5:1 Db5:1 C5:2
Bb4:1 Db5:1 C5:1 R:1
Eb5:.5 D5:.5 C5:1 Bb4:1 D5:1
D5:.5 C5:.5 Bb4:1 Ab4:1 C5:1
C5:.5 Bb4:.5 Ab4:1 G4:1 Bb4:1
Bb4:.5 Ab4:.5 G4:1 Eb4:1 R:1
R:1 G4:1 F4:2
Ab4:2 G4:1 Bb4:1
C5:1 Bb4:1 Ab4:2
G4:1 Bb4:1 Ab4:1 R:1
G4:1 F4:1 Eb4:2
F4:1 G4:1 Ab4:2
Bb4:1 Ab4:1 G4:1 R:1
G4:2 Eb4:2''',
 lh='''C3:4
Ab2:4
F3:4
G2:3 R:1
Bb2:4
G2:4
Ab3:4
Bb2:3 R:1
C3:4
Ab3:4
Eb3:4
Bb2:3 R:1
C3:4
Bb2:4
Ab2:4
G2:3 R:1
Ab2:4
F2:4
F3:4
G2:3 R:1
Ab2:4
Bb2:4
C3:3 R:1
Eb3:4''',
 lh_upper='''Eb3:2 G3:2
C3:1 Eb3:2 F3:1
Ab3:2 C4:1 Bb3:1
B2:1 D3:1 F3:1 R:1
D3:2 F3:2
B2:1 D3:2 F3:1
C4:2 Eb4:1 Db4:1
D3:1 F3:1 Ab3:1 R:1
Eb3:2 G3:2
C4:1 Eb4:2 D4:1
G3:2 Bb3:1 Ab3:1
D3:1 F3:1 Ab3:1 R:1
Eb3:1 G3:.5 Ab3:.5 Bb3:2
D3:1 F3:.5 G3:.5 Ab3:2
C3:1 Eb3:.5 F3:.5 G3:2
B2:1 D3:1 F3:1 R:1
C3:2 Eb3:2
Ab2:1 C3:2 Eb3:1
Ab3:2 C4:1 Bb3:1
B2:1 D3:1 F3:1 R:1
C3:1 Eb3:1 F3:2
D3:1 F3:1 Ab3:2
Eb3:1 G3:1 Bb3:1 R:1
G3:1 F3:1 Bb3:2''',
 tempos=[48,49,48,44,49,50,49,45,50,51,50,45,51,50,49,44,47,48,47,43,46,46,42,42],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],lower_phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],
 voice_phrases=[dict(voice=v,start_beat=a,end_beat=b,swell=3) for v in ['inner','tenor'] for a,b in ([(1,15),(17,31),(33,47),(48,63),(65,79),(80,91),(92,96)] if v=='inner' else [(0,15),(16,31),(32,47),(48,63),(64,79),(80,91),(92,96)])],
 sections={1:'p',9:'mp',17:'p',21:'pp'},lower_sections={1:'pp',9:'p',17:'pp'},
 engraving=dict(spacing_system=21,spacing_staff=23,pedal_offset_y=640),
 pedal=[[i*4+a,i*4+b-.2] for i in range(24) for a,b in ([(0,3)] if i in [3,7,11,15,19,22] else [(0,2),(2,4)])])
PIECES[-1]['performance']['inner_entries']=[[48,64]]
PIECES[-1]['performance']['tenor_entries']=[[80,96]]

study(op=268,title='Reed Tributary',key='d',fifths=-1,meter='5/4',bpm=50,parent=254,
 source=dict(source_opus=254,source_hand='rh',source_start_beat=1,source_end_beat=5,source_pitches=['D','C','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['D','C','A','G']),
 description='A descending call leaves room for a low answer. Later exchanges arrive sooner, with chromatic approach notes gently leaning into the next harmony. The middle flows across the five-beat measure before the two hands recover their separate speaking spaces.',
 technical='Allow the rests to shape the dialogue. Do not rush a reply into the other hand’s last note. Small chromatic approaches resolve within the line; the written pedal changes should keep them from accumulating beneath the next harmony.',
 rh='''D5:2 C5:.5 A4:.5 G4:2
F4+A4:3 R:2
R:2 C5:1 E5:.5 D5:.5 A4:1
G4+B4:3 F4+A4:2
E4+G4:2 C#5:.5 D5:1.5 C5:1
A4:2 G4:1 F4:1 R:1
G5:2 F5:.5 D5:.5 C5:2
Bb4+D5:3 R:2
R:1 E5:1 G5:.5 F#5:.5 E5:2
D5+F5:2 C5+E5:1 Bb4+D5:2
A4+C5:2 G#4:.5 A4:1.5 C5:1
D5:2 E5:1 F5:1 R:1
D5:.5 F5:.5 A5:.5 G5:.5 F5:1 E5:.5 D5:.5 C5:1
C5:.5 E5:.5 G5:.5 F5:.5 E5:1 D5:.5 C5:.5 Bb4:1
Bb4:.5 D5:.5 F5:.5 E5:.5 D5:1 C5:.5 Bb4:.5 A4:1
A4:.5 C5:.5 E5:.5 D5:.5 C5:1 B4:.5 Bb4:.5 A4:1
G4:1 Bb4:.5 D5:.5 F5:1 E5:.5 D5:.5 C5:1
C#5:.5 D5:.5 E5:1 D5:2 R:1
D5:2 C5:.5 A4:.5 G4:2
F4+A4:3 R:2
R:2 C5:1 E5:.5 D5:.5 A4:1
G4:2 F4:1 E4:1 R:1
F4+A4:2 G4+Bb4:3
A4+C5:2 G4+Bb4:1 F4+A4:2
E4+G4:3 D4+F4:2
E4+A4:2 R:3''',
 lh='''R:3 D3:1 C3:.5 A2:.5
G2:2 D3:1 F3:1 A3:1
C3:2 R:1 E3:.5 G3:.5 A3:1
G3:1 F3:.5 D3:.5 C3:3
Bb2+F3:2 A2+E3:3
D3:1 F3:1 E3:1 D3:1 R:1
R:3 G3:1 F3:.5 D3:.5
C3:2 G3:1 Bb3:1 D4:1
A2+E3:3 G3:1 B3:1
D3:1 F3:.5 A3:.5 C4:3
F3:2 E3:.5 F3:1.5 A3:1
Bb2:1 D3:1 C3:1 A2:1 R:1
D3:2 A3:.5 G3:.5 F3:1 E3:1
C3:1 G3:.5 Bb3:.5 E3:2 D3:1
Bb2:2 F3:.5 A3:.5 D3:1 C3:1
A2:1 E3:.5 G3:.5 C3:2 B2:1
G2:1 D3:.5 F3:.5 Bb3:1 A3:.5 G3:.5 E3:1
A2:1 E3:.5 G3:.5 D3:2 R:1
R:3 D3:1 C3:.5 A2:.5
Bb2:2 F3:1 A3:1 C4:1
F3:2 R:1 A3:.5 G3:.5 E3:1
C3:1 G3:1 Bb2:1 C3:1 R:1
D3:1 F3:.5 A3:.5 G3:3
F3:1 A3:.5 C4:.5 Bb3:1 G3:2
C3:1 G3:1 Bb2:1 A2:2
D3:1 F3:1 E3:.5 D3:1.5 R:1''',
 tempos=[50,51,50,49,50,45,51,52,51,50,51,46,53,54,53,52,51,46,49,50,49,44,48,48,46,46],
 phrases=[(1,6),(7,12),(13,18),(19,22),(23,26)],lower_phrases=[(1,6),(7,12),(13,18),(19,22),(23,26)],sections={1:'p',7:'mp',13:'mp',19:'p',23:'pp'},lower_sections={1:'p',7:'p',13:'p',19:'p',23:'pp'},
 pedal=[[i*5+a,i*5+b-.2] for i in range(26) for a,b in ([(0,2),(2,4)] if i in [5,11,17,21,25] else [(0,2),(2,5)])])
PIECES[-1]['system_starts']=[1,3,5,7,9,11,13,15,18,20,22,24]
PIECES[-1]['page_starts']=[9,18]

study(op=269,title='Velvet Rainpath',key='g',fifths=-2,meter='3/4',bpm=54,parent=263,
 source=dict(source_opus=263,source_hand='rh',source_start_beat=1,source_end_beat=4,source_pitches=['G','Bb','A','D'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['G','Bb','A','D']),
 description='Three-beat departures open into five-beat answers. A tied melody ignores some of these boundaries while the bass changes its rhythm beneath it. The middle grows warmer and higher before a low, newly harmonised return; the last answer rises instead of closing downward.',
 technical='Maintain a continuous quarter-note pulse across the alternating metres. Tied melody notes belong to the preceding gesture even when the bass changes. The longer bars are spaces for the answer, not an instruction to slow down.',
 rh='''G5:.5 Bb5:.5 A5:1 D5:1~
D5:1 C5:1 Bb4:1 A4:2
G4:2 R:1
R:1 Bb4:.5 D5:.5 F5:2 D5:1
Eb5:1 D5:.5 C5:.5 Bb4:1~
Bb4:1 A4:1 G4:1 F4:2
G4:1 Bb4:1 D5:1
C5:2 Bb4:1 A4:1 R:1
G5:.5 A5:.5 Bb5:.5 D6:.5 C6:1
Bb5:1 A5:.5 G5:.5 F5:1 D5:2
Eb5:.5 F5:.5 G5:.5 Bb5:.5 A5:1
G5:1 F5:.5 Eb5:.5 D5:1 C5:2
D5:.5 F5:.5 A5:.5 G5:.5 F5:1
Eb5:1 D5:.5 C5:.5 Bb4:2 R:1
G5:.5 Bb5:.5 A5:1 D5:1~
D5:1 C5:1 Bb4:1 A4:2
G4:2 R:1
R:1 Bb4:.5 D5:.5 F5:2 D5:1
Eb5:1 D5:.5 C5:.5 Bb4:1
A4:2 G4:1 F4:1 R:1
G4+Bb4:1 A4+C5:1 Bb4+D5:1
A4+C5:2 G4+Bb4:1 F4+A4:2
G4+Bb4:1 F4+A4:1 Eb4+G4:1
F4+A4:2 G4+Bb4:1 A4+C5:2
Bb4:1 A4:.5 G4:.5 F4:1
Eb4:1 G4:.5 Bb4:.5 A4:2 R:1
G4:1 Bb4:1 C5:1
D5:2 F5:3''',
 lh='''G3:.75 D4:.25 Bb3:1 D4:1
Eb3:.75 Bb3:.25 G3:1 C4:1 Bb3:2
C3:1 G3:1 R:1
Eb3:1 Bb3:.5 G3:.5 F3:1 D3:2
Bb2:.75 F3:.25 D3:1 F3:1
F3:.75 C4:.25 A3:1 Eb4:1 C4:2
Eb3:1 G3:1 Bb3:1
D3:1 A3:1 F3:1 C3:1 R:1
G3:.5 Bb3:.5 D4:.5 F4:.5 D4:1
Eb3:.5 G3:.5 Bb3:.5 D4:.5 Eb4:1 D4:1 Bb3:1
C3:.5 Eb3:.5 G3:.5 Bb3:.5 G3:1
Ab2:.5 C3:.5 Eb3:.5 G3:.5 Ab3:1 G3:1 Eb3:1
Bb2:.5 D3:.5 F3:.5 A3:.5 F3:1
C3:.5 Eb3:.5 G3:.5 Bb3:.5 D4:1 C4:1 R:1
Eb3:.75 Bb3:.25 G3:1 Bb3:1
C3:.75 G3:.25 Eb3:1 A3:1 G3:2
Bb2:1 F3:1 R:1
Ab2:1 Eb3:.5 C3:.5 Bb2:1 G2:2
Eb3:.75 Bb3:.25 G3:1 F3:1
D3:1 A3:1 F3:1 C3:1 R:1
G2:1 D3:1 Bb2:1
F2:1 C3:1 A2:1 D3:2
Eb2:1 Bb2:1 G2:1
D2:1 A2:1 F2:1 C3:2
C3:1 G3:.5 Eb3:.5 D3:1
Ab2:1 Eb3:1 G2:1 Bb2:1 R:1
Eb3:1 G3:1 Ab3:1
Bb2+F3:5''',
 meters=['3/4','5/4']*14,
 tempos=[54,55,51,54,55,54,53,49,56,57,56,57,55,49,54,55,51,54,53,48,52,53,52,51,50,46,49,49],
 phrases=[(1,4),(5,8),(9,14),(15,20),(21,28)],lower_phrases=[(1,4),(5,8),(9,14),(15,20),(21,28)],sections={1:'p',9:'mp',15:'p',21:'pp'},lower_sections={1:'pp',9:'p',15:'pp'})
_offsets=[0]
for _length in [3,5]*14:_offsets.append(_offsets[-1]+_length)
PIECES[-1]['performance']['phrase_arcs']=[[_offsets[a-1],_offsets[b],3] for a,b in PIECES[-1]['slurs']]
PIECES[-1]['pedal_spans']=[[_offsets[i],_offsets[i+1]-(1.2 if i in [2,7,13,16,19,25] else .2)] for i in range(28)]

study(op=270,title='Myrtle Homewater',key='d',fifths=-1,meter='4/4',bpm=52,parent=265,
 source=dict(source_opus=265,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','C','A','G'],transposition_semitones=0),motif=dict(hand='rh',start_beat=0,end_beat=4,pitches=['D','C','A','G']),
 description='A descending melody finds its way through a returning bass, a bright chordal answer and two unhurried five-note flourishes. When the bass takes up the tune, the treble becomes a quiet shelter. The closing phrase leaves an added ninth in place above D.',
 technical='Give the dotted lower figure a supple, even touch. Two explicitly notated quintuplets spread five eighths over two quarter beats. At bar 19 the melody moves below: keep the upper dyads quiet. The final added ninth is sustained without an automatic fermata.',
 rh='''D5:1.5 C5:.5 A4:1 G4:1
A4:.5 C5:.5 E5:1 D5:2~
D5:1 C5:.5 A4:.5 G4:2
F4:1 A4:.5 C5:.5 E5:2
D5:1 F5:.5 E5:.5 C5:2~
C5:1 Bb4:.5 A4:.5 G4:1 E4:1
F4:1 A4:1 G4:1 R:1
A4+C5:1 C5+E5:.5 D5+F5:.5 E5+G5:2
D5+F5:1 C5+E5:.5 Bb4+D5:.5 A4+C5:2
G4+Bb4:1 Bb4+D5:.5 C5+E5:.5 D5+F5:2
C5+E5:1 Bb4+D5:.5 A4+C5:.5 G4+Bb4:2
F4+A4:1 G4+Bb4:1 A4+C5:1 R:1
D5:.5 F5:.5 A5:1 G5:.5 F5:.5 E5:1
D5:2/5 E5:2/5 F5:2/5 A5:2/5 G5:2/5 E5:1 C5:1
Bb4:.5 D5:.5 F5:1 E5:.5 D5:.5 C5:1
A4:2/5 B4:2/5 C5:2/5 E5:2/5 D5:2/5 C5:1 A4:1
G4:.5 Bb4:.5 D5:1 F5:.5 E5:.5 D5:1
C#5:.5 D5:.5 E5:1 D5:1 R:1
F4+A4:4
G4+B4:2 A4+C5:2
E4+G4:4
F4+A4:2 G4+Bb4:2
A4+C5:4
G4+Bb4:2 F4+A4:2
E4+G4:2 F4+A4:1 R:1
D5:1.5 C5:.5 A4:1 G4:1
A4:.5 C5:.5 E5:1 D5:2
F5:1 E5:.5 D5:.5 C5:2
Bb4:1 D5:.5 F5:.5 E5:2
D5:1 C5:.5 A4:.5 G4:1 R:1
F4:1 A4:1 C5:1 E5:1
E4+A4+D5:4''',
 lh='''D3:.75 A3:.25 F3:.5 E3:.5 G3:1 A3:1
C3:1 G3:.5 E3:.5 D3:1 G3:1
Bb2:.75 F3:.25 D3:.5 C3:.5 E3:1 F3:1
F3:1 C4:.5 A3:.5 G3:1 E3:1
G3:.75 D4:.25 Bb3:.5 A3:.5 C4:1 D3:1
A2:1 E3:.5 G3:.5 C4:1 Bb3:1
D3:1 A3:1 F3:1 R:1
F3+A3:2 E3+G3:2
D3+F3:2 C3+E3:2
Bb2+D3:2 A2+C3:2
G2+Bb2:2 C3+E3:2
F3+A3:1 G3+Bb3:1 A3+C4:1 R:1
D3:1 A3:.5 F3:.5 C4:1 A3:1
C3:1 G3:1 Bb3:1 E3:1
Bb2:1 F3:.5 D3:.5 A3:1 F3:1
A2:1 E3:1 G3:1 C3:1
G2:1 D3:.5 Bb2:.5 F3:1 E3:1
A2:1 E3:.5 G3:.5 D3:1 R:1
D3:1.5 C3:.5 A2:1 G2:1
A2:.5 C3:.5 E3:1 D3:2~
D3:1 C3:.5 A2:.5 G2:2
F2:1 A2:.5 C3:.5 E3:2
D3:1 F3:.5 E3:.5 C3:2~
C3:1 Bb2:.5 A2:.5 G2:1 E2:1
F2:1 A2:1 G2:1 R:1
Bb2:.75 F3:.25 D3:.5 C3:.5 E3:1 F3:1
A2:1 E3:.5 C3:.5 B2:1 E3:1
G2:.75 D3:.25 Bb2:.5 A2:.5 C3:1 D3:1
C3:1 G3:.5 E3:.5 Bb3:1 A3:1
D3:1 A3:1 F3:1 R:1
Bb2:1 F3:1 A2:1 E3:1
D3:2 A2:1 D3:1''',
 tempos=[52,53,52,53,54,52,47,54,55,54,53,48,56,56,55,55,54,48,51,52,51,52,53,51,46,51,52,51,50,46,49,49],
 phrases=[(1,7),(8,12),(13,18),(19,25),(26,32)],lower_phrases=[(1,7),(8,12),(13,18),(19,25),(26,32)],sections={1:'p',8:'mp',13:'mp',19:'pp',26:'p',31:'pp'},lower_sections={1:'pp',8:'p',13:'p',19:'p',26:'pp'},
 tuplet_spans=[dict(hand='rh',start_beat=i*4,end_beat=i*4+2,actual=5,normal=4,stem='down') for i in [13,15]],
 pedal=[[i*4+a,i*4+b-.2] for i in range(32) for a,b in ([(0,3)] if i in [6,11,17,24,29] else [(0,2),(2,4)])])
