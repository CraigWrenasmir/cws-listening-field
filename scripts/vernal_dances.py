"""Vernal Dances, Op. 271–290. Explicitly authored spring piano dances."""
PIECES = []

def dance(*, op, title, key, fifths, meter, bpm, parent, source, motif, rh, lh,
          description, technical, tempos, phrases, sections, pedal=None, **extras):
    """Shared typography and performance defaults; each work supplies its own music."""
    n = len(rh.strip().splitlines())
    beats = int(meter.split('/')[0])*4/int(meter.split('/')[1])
    assert len(lh.strip().splitlines()) == n and len(tempos) == n
    entry = dict(op=op,title=title,key=key,fifths=fifths,meter=meter,bpm=bpm,
        parent_opus=parent,ancestry=source,motif=motif,rh=rh,lh=lh,
        description=description,difficulty='Advanced dance study',
        technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),
        technical_note=technical,system_starts=list(range(1,n+1,2)),
        page_starts=list(range(9,n+1,8)),
        engraving=dict(spacing_system=18,spacing_staff=17,pedal_offset_y=570),
        sections=sections,lower_sections={1:'p'},words={1:'grazioso'},
        slurs=phrases,lower_phrases=[],hairpins=[],tempo_changes={},group=3,
        final_fermata=False,
        performance=dict(rubato=tempos,
            phrase_arcs=[[(a-1)*beats,b*beats,3] for a,b in phrases],
            lower_entries=[],pedal_lift=.25,gate=.91,
            note='Deliberate dance pulse, shaped phrases and terraced dynamics; no random timing.'))
    entry['pedal_spans'] = pedal if pedal is not None else []
    entry.update(extras)
    if entry.get('meters'):
        lengths = [int(m.split('/')[0])*4/int(m.split('/')[1]) for m in entry['meters']]
        assert len(lengths) == n
        offsets = [sum(lengths[:i]) for i in range(n+1)]
        entry['performance']['phrase_arcs'] = [[offsets[a-1],offsets[b],3] for a,b in phrases]
    PIECES.append(entry)
    return entry

# Each descendant quotes a declared pitch fragment, with new rhythm and harmony.
dance(op=271,title='Apricot Promenade',key='F',fifths=-1,meter='3/4',bpm=88,parent=240,
 source=dict(source_opus=240,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['F','E','D','C'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['F','E','D','C']),
 description='An F-major waltz opens with a falling ribbon, answered by a rising sixth. A five-bar refrain gives way to light displaced chords, then a more radiant high-register turn. The opening returns above a changed bass; two quiet steps end with an unexpectedly bright chord.',
 technical='Float the melody over detached bass-and-chord steps. Keep the offbeat dyads light, project the top of the central thirds and release the written pauses cleanly. The final chord returns to the opening pulse.',
 rh='''F5:.5 E5:.5 D5:1 C5:1
A4:1 C5:.5 F5:.5 G5:1
A5:1.5 G5:.5 F5:1
E5:.5 D5:.5 C5:1 A4:1
G4:1 A4:.5 C5:.5 F5:1
R:.5 A4+C5:.5 R:.5 Bb4+D5:.5 C5+E5:1
D5+F5:1 C5+E5:.5 Bb4+D5:.5 A4+C5:1
G4+Bb4:1 A4+C5:1 R:1
C5:.5 F5:.5 A5:1 G5:.5 F5:.5
E5:1 G5:.5 Bb5:.5 A5:1
G5:1.5 E5:.5 C5:1
D5:.5 F5:.5 A5:1 G5:1
A5+C6:1 G5+Bb5:.5 F5+A5:.5 E5+G5:1
D5+F5:1 E5+G5:1 C5+F5:1
Bb4+D5:.5 C5+E5:.5 D5+F5:1 E5+G5:1
C5+F5+A5:2 R:1
F5:.5 E5:.5 D5:1 C5:1
A4:1 C5:.5 F5:.5 G5:1
A5:1 G5:.5 F5:.5 D5:1
E5:.5 D5:.5 C5:1 A4:1
Bb4:1 C5:.5 D5:.5 F5:1
E5:1 D5:.5 C5:.5 A4:1
G4:1 R:.5 A4:.5 C5:1
F4+A4+C5:1 R:2''',
 lh='''F3:1 A3+C4:.5 R:.5 A3+C4:1
D3:1 A3+C4:1 F3:1
Bb2:1 F3+A3:1 F3+A3:1
C3:1 G3+Bb3:.5 R:.5 E3:1
F3:1 A3+C4:1 G3+C4:1
D3:1 F3+A3:1 G3+Bb3:1
G3:1 Bb3+D4:1 F3:1
C3:1 E3+Bb3:1 R:1
F3:1 A3+C4:1 F3:1
E3:1 G3+Bb3:1 C4:1
A2:1 E3+G3:1 C4:1
D3:1 F3+A3:1 C4:1
Bb2:1 F3+A3:1 G3:1
G3:1 Bb3+D4:1 A3+C4:1
C3:1 G3+Bb3:1 E3:1
F3+A3:2 R:1
D3:1 F3+A3:1 C4:1
Bb2:1 F3+A3:1 C4:1
G3:1 Bb3+D4:1 A3:1
C3:1 G3+Bb3:1 E3:1
Bb2:1 F3+A3:1 D4:1
C3:1 G3+Bb3:1 E3:1
F3:1 R:.5 A3:.5 C4:1
F3+C4:1 R:2''',
 tempos=[88,88,90,88,86,88,89,86,90,90,90,91,92,92,90,88,88,88,90,88,88,86,84,88],
 phrases=[(1,5),(6,8),(9,12),(13,16),(17,20),(21,23)],
 sections={1:'p',6:'pp',9:'mp',13:'mf',17:'p',21:'pp',24:'mf'},
 lower_sections={1:'p',6:'pp',9:'p',13:'mp',17:'p',21:'pp',24:'mf'},
 hairpins=[('crescendo',9,13),('diminuendo',14,16)],
 pedal=[[i*3,i*3+2.7] for i in [2,9,12,13,14,18]])

dance(op=272,title='Clover Skipping',key='G',fifths=1,meter='6/8',bpm=104,parent=271,
 source=dict(source_opus=271,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['F','E','D','C'],transposition_semitones=2),
 motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['G','F#','E','D']),
 description='A skipping compound-time dance in G. The first three-bar question leaves its answer late; brief rests puncture the bass while the upper voice keeps travelling. A quieter E-minor pocket grows into ringing sixths, then a six-bar return closes with a single buoyant step.',
 technical='Feel two dotted beats through the varied eighth-note groupings. The accompaniment sometimes arrives after the melody; keep those arrivals light. The upper sixths need a singing top note without tightening the pulse.',
 rh='''G5:1 F#5:.5 E5:.5 D5:1
B4:.5 D5:.5 G5:.5 A5:1 B5:.5
A5:1.5 G5:1 R:.5
R:.5 E5:.5 F#5:.5 G5:1 D5:.5
E5:1 C5:.5 D5:1 B4:.5
A4:.5 C5:.5 E5:.5 G5:1 F#5:.5
E5:.5 D5:.5 B4:.5 A4:1 G4:.5
B4:1.5 D5:1 R:.5
G5:.5 B5:.5 A5:.5 G5:.5 F#5:.5 E5:.5
D5:1 F#5:.5 A5:1 G5:.5
E5:.5 G5:.5 B5:.5 C6:1 B5:.5
A5:1 G5:.5 E5:1 R:.5
B4:1.5 E5:1 D5:.5
C5:.5 E5:.5 G5:.5 F#5:1 E5:.5
D5:1.5 B4:.5 A4:.5 G4:.5
F#4:1 A4:.5 B4:1 R:.5
E5:.5 G5:.5 B5:.5 A5:.5 G5:.5 F#5:.5
E5:1 D5:.5 B4:1 G4:.5
A4:.5 C5:.5 E5:.5 D5:.5 F#5:.5 A5:.5
G5:1.5 D5:1 R:.5
B4+G5:1 A4+F#5:.5 G4+E5:1 F#4+D5:.5
G4+E5:.5 A4+F#5:.5 B4+G5:.5 D5+B5:1 C5+A5:.5
B4+G5:1.5 A4+F#5:1 R:.5
G4+E5:.5 A4+F#5:.5 B4+G5:.5 C5+A5:1 B4+G5:.5
A4+F#5:.5 G4+E5:.5 F#4+D5:.5 G4+E5:1 A4+F#5:.5
B4+G5:1.5 R:1.5
G5:1 F#5:.5 E5:.5 D5:1
B4:.5 D5:.5 G5:.5 A5:1 B5:.5
A5:1.5 G5:1 D5:.5
E5:1 C5:.5 D5:1 B4:.5
A4:.5 C5:.5 E5:.5 D5:1 F#5:.5
G4+B4+D5:1.5 R:1.5''',
 lh='''G3:1.5 B3+D4:1 R:.5
E3:1 B3:.5 G3:1.5
C3:1.5 G3+B3:1 R:.5
G3:1 B3:.5 D4:1 R:.5
C3:1 E3:.5 G3:1 E3:.5
A2:1.5 E3+G3:1.5
D3:1 A3:.5 F#3:1 A3:.5
G3:1.5 B3:1 R:.5
G3:1 B3:.5 D4:1 B3:.5
D3:1.5 F#3+A3:1.5
E3:1 B3:.5 G3:1 G3:.5
C3:1.5 G3+B3:1 R:.5
E3:1 B3:.5 G3:1.5
A2:1.5 E3+G3:1.5
G3:1 D4:.5 B3:1 G3:.5
B2:1.5 F#3+A3:1 R:.5
E3:1 G3:.5 B3:1 G3:.5
C3:1.5 G3+B3:1.5
A2:1 E3:.5 D3:1 F#3:.5
G3:1.5 B3:1 R:.5
G3:1.5 D4:1 B3:.5
E3:1 B3:.5 G3:1.5
D3:1.5 A3:1 R:.5
C3:1 G3:.5 E3:1 G3:.5
D3:1 A3:.5 F#3:1 A3:.5
G3+B3:1.5 R:1.5
E3:1.5 G3+B3:1 R:.5
C3:1 G3:.5 E3:1.5
G3:1.5 B3+D4:1.5
C3:1 G3:.5 E3:1 G3:.5
D3:1 A3:.5 F#3:1 A3:.5
G3+D4:1.5 R:1.5''',
 tempos=[104,104,102,104,104,106,104,102,108,108,108,104,96,96,98,96,100,102,104,104,108,108,106,108,106,104,104,104,106,104,102,104],
 phrases=[(1,3),(4,8),(9,12),(13,16),(17,20),(21,23),(24,26),(27,32)],
 sections={1:'p',9:'mf',13:'pp',17:'mp',21:'mf',27:'p',32:'mp'},
 lower_sections={1:'p',9:'mp',13:'pp',17:'p',21:'mp',27:'p'},
 hairpins=[('crescendo',17,20),('diminuendo',24,26)],
 pedal=[[36,38.8],[39,41.8],[42,44.8],[60,61.3],[63,64.3],[66,67.3]])

dance(op=273,title='Birch Turnstile',key='D',fifths=2,meter='2/4',bpm=82,parent=272,
 source=dict(source_opus=272,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['G','F#','E','D'],transposition_semitones=-5),
 motif=dict(hand='rh',start_beat=0,end_beat=2,pitches=['D','C#','B','A']),
 description='A dry, lightly syncopated two-step turns through seven-bar questions and nine-bar replies. Its bass repeatedly moves before the treble chord, and a quiet central exchange briefly removes the beat. The returning tune gathers into small, bright block chords.',
 technical='Keep the semiquaver pickups crisp without hurrying the longer notes. In the quiet exchange, pass the line between hands without sustaining across the silences. Voice the concluding chords toward their top note.',
 rh='''D5:.5 C#5:.5 B4:.5 A4:.5
F#4:.75 A4:.25 D5:1
E5:.5 R:.5 F#5:.75 E5:.25
D5:1 A4:.5 B4:.5
C#5:.75 D5:.25 E5:.5 G5:.5
F#5:.5 E5:.5 D5:.75 C#5:.25
D5:1 R:1
R:.5 B4+D5:.5 R:.5 C#5+E5:.5
D5+F#5:1 E5+G5:.5 F#5+A5:.5
E5+G5:.75 D5+F#5:.25 C#5+E5:1
B4+D5:.5 A4+C#5:.5 G4+B4:1
A4+C#5:.75 B4+D5:.25 C#5+E5:1
D5:.5 F#5:.5 A5:.75 G5:.25
F#5:.5 E5:.5 D5:.5 B4:.5
C#5:1 E5:.5 C#5:.5
D5:1 R:1
F#5:.5 R:1.5
R:1 E5:.5 D5:.5
B4:1 R:1
R:.5 C#5:.5 E5:1
D5:.5 R:.5 A4:1
B4:.75 C#5:.25 D5:1
E5:.5 F#5:.5 G5:.5 E5:.5
F#5:1 R:1
D5:.5 C#5:.5 B4:.5 A4:.5
F#4:.75 A4:.25 D5:1
E5:.5 F#5:.5 A5:.75 G5:.25
F#5:1 D5:1
G4+B4:1 A4+C#5:1
B4+D5:.5 C#5+E5:.5 D5+F#5:.5 E5+G5:.5
D5+F#5:1 C#5+E5:1
A4+D5+F#5:2''',
 lh='''D3:.5 R:.5 F#3+A3:1
B2:.5 R:.5 F#3+A3:1
G3:.5 B3:.5 A3:.5 G3:.5
D3:.5 R:.5 F#3+A3:1
A2:.5 E3:.5 G3:1
G3:.5 B3:.5 A3:1
D3+A3:1 R:1
G3:1 A3:1
D3:1 F#3+A3:1
C#3:1 G3+A3:1
G3:.5 D4:.5 B3:1
A2:.5 E3:.5 G3:1
D3:1 F#3+A3:1
B2:.5 F#3:.5 A3:1
A2:.5 E3:.5 G3:1
D3:1 R:1
R:.5 D3:.5 F#3:.5 A3:.5
B3:.5 A3:.5 R:1
R:1 G3:.5 B3:.5
A3:.5 R:1.5
R:1 F#3:.5 E3:.5
D3:.5 F#3:.5 B3:1
A3:.5 G3:.5 E3:.5 C#3:.5
D3:1 R:1
B2:.5 R:.5 F#3+A3:1
G3:.5 R:.5 B3+D4:1
A2:.5 E3:.5 G3:1
D3:1 F#3+A3:1
G3:1 A3:1
B2:1 F#3+A3:1
G3:1 A3:1
D3+F#3:2''',
 tempos=[82,82,84,82,84,82,80,82,84,84,82,82,86,84,82,80,76,76,76,78,78,80,82,80,82,82,84,84,82,84,82,82],
 phrases=[(1,3),(4,7),(8,12),(13,16),(18,18),(20,20),(21,24),(25,28),(29,32)],
 sections={1:'mp',8:'p',13:'mf',17:'pp',21:'p',25:'mp',29:'mf'},
 lower_sections={1:'p',8:'pp',13:'mp',17:'mp',21:'p',25:'p',29:'mp'},
 hairpins=[('crescendo',8,10),('diminuendo',14,16),('crescendo',29,32)],
 lower_phrases=[(17,18),(19,20),(21,23)])

dance(op=274,title='Magnolia Esplanade',key='Bb',fifths=-2,meter='3/4',bpm=72,parent=271,
 source=dict(source_opus=271,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['F','E','D','C'],transposition_semitones=5),
 motif=dict(hand='rh',start_beat=0,end_beat=3,pitches=['Bb','A','G','F']),
 description='A broad waltz lets two-beat bass steps drift across its three-beat bars. A falling melody expands into warm sixths and ninths; an E-natural window brightens the middle without abandoning B-flat. The return is quieter, ending on a gently suspended sixth.',
 technical='Maintain the waltz underneath the bass hemiolas. Balance the upper chord tones as a continuous melody and release the pedal before the written rests. The hand shapes remain compact while harmony changes beneath held upper tones.',
 rh='''Bb5:.5 A5:.5 G5:1 F5:1
D5:2 F5:1
G5:1 F5:.5 Eb5:.5 D5:1
C5:2 A4:1
Bb4+D5:1 D5+F5:1 F5+A5:1
Eb5+G5:2 D5+F5:1
C5+Eb5:1 Bb4+D5:1 A4+C5:1
Bb4+D5+F5:2 R:1
D5+F5+A5:2 C5+E5+G5:1
B4+D5+F5:1 A4+C5+E5:2
G4+B4+D5:2 A4+C5+F5:1
Bb4+D5+G5:1 C5+E5+A5:2
D5+F5+Bb5:1 C5+Eb5+A5:1 Bb4+D5+G5:1
A4+C5+F5:2 G4+Bb4+Eb5:1
F4+A4+D5:1 G4+Bb4+Eb5:1 A4+C5+F5:1
Bb4+D5+G5:2 R:1
Bb5:.5 A5:.5 G5:1 F5:1
D5:2 F5:1
G5:1 F5:.5 Eb5:.5 D5:1
C5:1 A4:1 F4:1
G4+Bb4+D5:2 F4+A4+C5:1
Eb4+G4+Bb4:1 F4+A4+C5:2
G4+Bb4+Eb5:1 A4+C5+F5:1 Bb4+D5+G5:1
G4+Bb4+D5:3''',
 lh='''Bb2+F3:2 C3+G3:1
D3+A3:1 Eb3+Bb3:2
G3:1 Bb3+D4:1 F3:1
F3:1 A3+Eb4:1 C4:1
Bb2:1 F3+A3:1 D4:1
Eb3:1 G3+Bb3:1 F3:1
F3:2 C3:1
Bb2+F3:2 R:1
D3+A3:2 C3+G3:1
B2+F3:1 A2+E3:2
G3:1 B3+D4:1 D3:1
C3:1 G3:1 E3:1
Bb2:1 F3:1 D4:1
F3:1 C4:1 A3:1
D3:1 G3:1 F3:1
Eb3+Bb3:2 R:1
G2+D3:2 A2+E3:1
Bb2+F3:1 C3+G3:2
Eb3:1 G3+Bb3:1 D4:1
F3:1 A3:1 Eb3:1
G3:2 F3:1
Eb3:1 C3:2
Eb3:1 F3:1 G3:1
Bb2+F3:3''',
 tempos=[72,72,74,72,74,74,72,70,76,76,76,78,78,76,74,72,72,72,74,72,70,70,72,70],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],
 sections={1:'p',5:'mp',9:'pp',13:'mf',17:'p',21:'pp'},
 lower_sections={1:'p',5:'p',9:'pp',13:'mp',17:'pp'},
 hairpins=[('crescendo',9,13),('diminuendo',14,16),('diminuendo',21,24)],
 pedal=[[i*3,i*3+(1.8 if i in [7,15] else 2.8)] for i in range(24)])

dance(op=275,title='Sorrel Detour',key='C',fifths=0,meter='5/8',bpm=78,parent=254,
 source=dict(source_opus=254,source_hand='rh',source_start_beat=1,source_end_beat=5,source_pitches=['D','C','A','G'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=0,end_beat=2.5,pitches=['D','C','A','G']),
 description='Five small steps make a crooked garden dance. The bass alternates a long-short gait with its reverse while a modal tune curls around C. Brief Lydian flashes and soft empty beats lead to a chordal crest; the ending leaves the dance mid-gesture on a clear ninth.',
 technical='Distinguish the alternating three-plus-two and two-plus-three subdivisions without exaggerating them. Keep the short rests audible, and let the melodic phrase continue when the bass changes its grouping.',
 rh='''D5:.5 C5:.5 A4:.5 G4:1
E4:1 G4:.5 C5:1
D5:1 E5:.5 G5:.5 E5:.5
F5:.5 E5:.5 D5:.5 C5:1
B4:.5 A4:.5 G4:.5 E4:.5 R:.5
R:.5 G4:.5 A4:.5 C5:1
D5:.5 E5:.5 F#5:.5 G5:1
E5:1 D5:1 R:.5
G5:.5 E5:.5 D5:1 C5:.5
A4:1.5 C5:1
B4:.5 D5:.5 F5:.5 E5:1
D5:1 C5:.5 A4:1
G4:.5 A4:.5 C5:.5 D5:.5 E5:.5
F#5:1 E5:.5 D5:1
C5:.5 B4:.5 A4:.5 G4:1
E4:1 R:1.5
A4+C5:1 G4+B4:.5 F4+A4:1
E4+G4:.5 F4+A4:.5 G4+B4:.5 A4+C5:1
B4+D5:.5 C5+E5:.5 D5+F#5:.5 E5+G5:1
D5+F5:1 C5+E5:1 R:.5
B4+D5:1.5 A4+C5:1
G4+B4:.5 A4+C5:.5 B4+D5:.5 C5+E5:1
D5+F5:.5 E5+G5:.5 F5+A5:.5 E5+G5:1
C5+E5:1 R:1.5
D5:.5 C5:.5 A4:.5 G4:1
E4:1 G4:.5 C5:1
D5:1 E5:.5 G5:.5 E5:.5
F5:1 E5:1 R:.5
D5:.5 C5:.5 A4:.5 G4:1
A4:1 C5:.5 E5:1
D5:1 B4:.5 G4:1
G4+B4+D5:2.5''',
 lh='''C3:1.5 G3:1
A2:1 E3:1.5
F3:1.5 A3:1
D3:1 F3:1.5
G3:1 D3:1 R:.5
E3:1.5 G3:1
D3:1 A3:1.5
G3:1 B3:1 R:.5
C3:1.5 G3:1
F3:1 A3:1.5
G3:1.5 B3:1
A2:1 E3:1.5
F3:1.5 A3:1
D3:1 A3:1.5
G3:1 D3:1.5
C3:1 R:1.5
F3:1.5 C3:1
C3:1 G3:1.5
D3:1.5 A3:1
G3:1 B3:1 R:.5
E3:1.5 B3:1
A2:1 E3:1.5
F3:1.5 G3:1
C3+G3:1 R:1.5
A2:1.5 E3:1
F3:1 C3:1.5
D3:1.5 A3:1
G3:1 B3:1 R:.5
C3:1.5 G3:1
F3:1 A3:1.5
G3:1 D3:1.5
C3+G3:2.5''',
 tempos=[78,78,80,80,78,78,82,78,80,80,82,80,84,84,80,78,74,74,78,78,80,82,84,80,78,78,80,78,76,76,76,78],
 phrases=[(1,5),(6,8),(9,15),(17,20),(21,24),(25,29),(30,32)],
 sections={1:'p',6:'mp',9:'p',13:'mf',17:'pp',21:'mp',23:'mf',25:'p',29:'pp'},
 lower_sections={1:'p',6:'p',13:'mp',17:'pp',21:'p',23:'mp',25:'p',29:'pp'},
 hairpins=[('crescendo',9,13),('crescendo',21,23),('diminuendo',29,32)],
 pedal=[[40,42.3],[42.5,44.8],[77.5,79.8]])

dance(op=276,title='Wisteria Carousel',key='A',fifths=3,meter='3/4',bpm=86,parent=273,
 source=dict(source_opus=273,source_hand='rh',source_start_beat=0,source_end_beat=2,source_pitches=['D','C#','B','A'],transposition_semitones=7),
 motif=dict(hand='lh',start_beat=36,end_beat=39,pitches=['A','G#','F#','E']),
 description='A rising waltz in A circles around a held E before slipping through a brief minor-subdominant shade. The inherited falling phrase appears halfway through in the bass, under still upper thirds. A compressed reprise grows brighter and ends with a small upward flick.',
 technical='Shape the rising sixth without striking the arrival. Preserve the written long-short lilt, and bring out the bass melody in the central eight bars. The borrowed-minor colours should retain the same light pulse.',
 rh='''C#5:1 E5:.75 A5:.25 G#5:1
F#5:1.5 E5:.5 C#5:1
B4:1 D5:.75 F#5:.25 E5:1
C#5:2 B4:.5 A4:.5
G#4:.75 A4:.25 B4:1 E5:1
F#5:1 E5:.5 C#5:.5 A4:1
B4:.75 C#5:.25 D5:1 E5:1
C#5:2 R:1
F5:1 A5:.5 G5:.5 F5:1
E5:1.5 D5:.5 C5:1
Bb4:.75 D5:.25 F5:1 E5:1
C#5:1 B4:1 R:1
C#5+E5:3
B4+D5:2 A4+C#5:1
G#4+B4:1 A4+C#5:2
B4+D5:2 R:1
C#5+F#5:2 B4+E5:1
A4+D5:1 G#4+C#5:2
F#4+B4:2 E4+A4:1
G#4+B4+E5:2 R:1
C#5:1 E5:.75 A5:.25 G#5:1
F#5:1 E5:.5 C#5:.5 B4:1
C#5:.5 E5:.5 F#5:1 G#5:.5 A5:.5
B5:.5 A5:.5 E5:.5 C#5:.5 A4:1''',
 lh='''A2:1 E3+A3:1 C#4:1
F#3:1 A3+C#4:1 E3:1
D3:1 A3:1 F#3:1
A2:1 E3+A3:1 C#4:1
E3:1 G#3+B3:1 D4:1
F#3:1 A3:1 E3:1
D3:1 F#3+A3:1 E3:1
A2:2 R:1
D3:1 F3+A3:1 C4:1
C3:1 G3:1 E3:1
Bb2:1 F3:1 A3:1
E3:1 G#3:1 R:1
A3:1 G#3:.5 F#3:.5 E3:1
F#3:1 A3:.5 B3:.5 C#4:1
B3:1 G#3:1 E3:1
F#3:1 E3:1 R:1
D3:.75 F#3:.25 A3:1 B3:1
C#4:1 B3:.5 A3:.5 G#3:1
F#3:1 D3:1 A2:1
E3:1 B3:1 R:1
A2:1 E3+A3:1 C#4:1
D3:1 F#3+A3:1 B3:1
E3:1 G#3+B3:1 D4:1
A3:1 E3:1 A2:1''',
 tempos=[86,86,88,86,88,90,88,84,80,80,82,82,84,84,86,84,86,88,86,84,88,90,92,90],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],
 lower_phrases=[(13,16),(17,20)],
 sections={1:'mp',5:'mf',9:'pp',13:'p',17:'pp',21:'mp',23:'mf'},
 lower_sections={1:'p',5:'mp',9:'pp',13:'mp',17:'mp',21:'p',23:'mp'},
 hairpins=[('crescendo',1,5),('diminuendo',6,8),('crescendo',21,24)],
 pedal=[[i*3,i*3+(1.8 if i in [7,11,15,19] else 2.8)] for i in [0,1,3,5,7,8,9,10,12,13,14,16,17,18,20,21]])

dance(op=277,title='Fennel Footbridge',key='F',fifths=-1,meter='6/8',bpm=96,parent=275,
 source=dict(source_opus=275,source_hand='rh',source_start_beat=0,source_end_beat=2.5,source_pitches=['D','C','A','G'],transposition_semitones=0),
 motif=dict(hand='lh',start_beat=24,end_beat=27,pitches=['D','C','A','G']),
 description='A lilting melody crosses a stream of lower eighths. The hands momentarily hear the bar differently: three upper steps over two lower pulses. A bare bass quotation interrupts the motion, then the same arpeggios return under a more radiant melody before both hands dissolve into a quiet open fifth.',
 technical='Keep the continuous lower eighths supple and unaccented. Maintain the upper three-beat figures against the compound metre, and distinguish the bare central bass from the surrounding accompaniment. Release each short phrase without slowing every bar.',
 rh='''A5:1 G5:1 F5:1
E5:1.5 G5:1 F5:.5
D5:1 F5:1 A5:1
G5:1.5 E5:1 R:.5
C5:.5 F5:.5 A5:.5 G5:.5 F5:.5 E5:.5
D5:1.5 E5:.5 G5:.5 F5:.5
E5:1 D5:1 C5:1
A4:1.5 R:1.5
R:3
C5:1.5 E5:1 D5:.5
A4:1 C5:1 F5:1
E5:1.5 D5:1 R:.5
F5:1 A5:1 C6:1
B5:1.5 A5:.5 G5:.5 E5:.5
D5:1 G5:1 B5:1
A5:1.5 G5:1 R:.5
A5:1 G5:1 F5:1
E5:.5 G5:.5 Bb5:.5 A5:1 G5:.5
F5:1 D5:1 A4:1
G4:1.5 A4:1 C5:.5
D5:.5 F5:.5 A5:.5 G5:1 E5:.5
F5:1 D5:1 C5:1
A4:1.5 G4:1 E4:.5
F4+C5:3''',
 lh='''F3:.5 A3:.5 C4:.5 A3:.5 G3:.5 A3:.5
C3:.5 E3:.5 G3:.5 Bb3:.5 G3:.5 E3:.5
D3:.5 F3:.5 A3:.5 C4:.5 A3:.5 F3:.5
C3:.5 E3:.5 G3:.5 C4:1 R:.5
F3:.5 A3:.5 C4:.5 Bb3:.5 A3:.5 G3:.5
Bb2:.5 D3:.5 F3:.5 A3:.5 F3:.5 D3:.5
C3:.5 E3:.5 G3:.5 Bb3:.5 G3:.5 E3:.5
F3:1.5 R:1.5
D3:.5 C3:.5 A2:1 G2:1
C3:1.5 G3:1 E3:.5
F3:1 A3:1 D3:1
C3:1.5 G3:1 R:.5
F3:.5 A3:.5 C4:.5 A3:.5 G3:.5 E3:.5
E3:.5 G3:.5 B3:.5 D4:.5 B3:.5 G3:.5
G3:.5 B3:.5 D4:.5 B3:.5 A3:.5 G3:.5
F3:.5 A3:.5 C4:.5 A3:1 R:.5
D3:.5 F3:.5 A3:.5 C4:.5 A3:.5 F3:.5
C3:.5 E3:.5 G3:.5 Bb3:.5 G3:.5 E3:.5
Bb2:.5 D3:.5 F3:.5 A3:.5 F3:.5 D3:.5
C3:.5 E3:.5 G3:.5 A3:1 G3:.5
D3:.5 F3:.5 A3:.5 C4:.5 A3:.5 F3:.5
Bb2:.5 D3:.5 F3:.5 A3:.5 F3:.5 D3:.5
C3:1.5 G3:1 E3:.5
F3:3''',
 tempos=[96,96,98,96,100,100,98,94,88,90,92,92,100,102,102,98,98,100,98,96,98,96,92,92],
 phrases=[(1,4),(5,8),(10,12),(13,16),(17,20),(21,24)],lower_phrases=[(9,12)],
 sections={1:'p',5:'mp',9:'pp',13:'mf',17:'mp',21:'p',24:'pp'},
 lower_sections={1:'pp',5:'p',9:'mp',13:'mp',17:'p',21:'pp'},
 hairpins=[('crescendo',1,3),('crescendo',13,15),('diminuendo',21,24)],
 pedal=[[0,2.7],[6,8.7],[36,38.7],[42,44.7],[48,50.7],[69,71.7]])

dance(op=278,title='Lilac Belvedere',key='Eb',fifths=-3,meter='6/4',bpm=82,parent=274,
 source=dict(source_opus=274,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['Bb','A','G','F'],transposition_semitones=5),
 motif=dict(hand='rh',voice='upper',start_beat=96,end_beat=102,pitches=['Eb','D','C','Bb']),
 description='An expansive double waltz unfolds in E-flat. Long upper phrases first float over paired dance steps; an independent middle voice then turns beneath them, bringing the music into fuller sunlight. The inherited descent arrives only on the return, followed by a quiet, open-ended coda.',
 technical='Hear two broad waltz measures inside each 6/4 bar. In the central section, sustain the upper voice while the inner fingers keep dancing; give the inner line less weight. Keep pedal changes distinct from finger legato.',
 rh='''G5:2 Bb5:1 Ab5:2 F5:1
Eb5:3 D5:1 Eb5:1 G5:1
F5:2 Ab5:1 C6:2 Bb5:1
G5:3 F5:2 R:1
Eb5:1 G5:1 Bb5:1 A5:2 G5:1
F5:2 Eb5:1 D5:2 C5:1
Bb4:2 D5:1 F5:2 G5:1
Eb5:4 R:2
G5:3 F5:3
Eb5:2 F5:1 G5:3
Ab5:3 G5:2 F5:1
Eb5:4 D5:2
F5:2 G5:1 Ab5:3
G5:3 Bb5:3
Ab5:2 G5:1 F5:2 Eb5:1
F5:3 Eb5:2 R:1
Eb5:1 D5:1 C5:2 Bb4:2
G4:2 Bb4:1 Eb5:3
F5:2 Ab5:1 G5:2 F5:1
Eb5:3 D5:2 R:1
G5:2 Bb5:1 Ab5:2 F5:1
Eb5:3 G5:2 F5:1
D5:2 Eb5:1 G5:2 Bb5:1
G5:3 F5:3''',
 rh_inner='''R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6
Bb4:1 D5:1 Eb5:1 D5:1 C5:1 D5:1
G4:1 Bb4:1 C5:1 Bb4:1 Eb5:1 D5:1
C5:1 Eb5:1 F5:1 Eb5:1 D5:1 C5:1
G4:1 Bb4:1 C5:1 Bb4:1 A4:1 Bb4:1
Ab4:1 C5:1 D5:1 C5:1 Eb5:1 D5:1
Bb4:1 D5:1 Eb5:1 D5:1 F5:1 Eb5:1
C5:1 Eb5:1 D5:1 C5:1 Bb4:1 G4:1
Ab4:1 C5:1 Bb4:1 G4:1 Bb4:1 R:1
R:6
R:6
R:6
R:6
R:6
R:6
R:6
R:6''',
 lh='''Eb3:1 G3+Bb3:2 D3:1 F3+Ab3:2
C3:1 G3+Bb3:2 Bb2:1 F3+Ab3:2
Ab2:1 Eb3+G3:2 F3:1 Ab3+C4:2
Bb2:1 F3+Ab3:2 Eb3:1 R:2
Eb3:1 G3+Bb3:2 F3:1 A3+C4:2
Bb2:1 F3+Ab3:2 C3:1 Eb3+G3:2
G3:1 Bb3:2 Bb2:1 F3+Ab3:2
Eb3+Bb3:4 R:2
Eb3:2 Bb3:1 D3:2 Bb3:1
C3:2 G3:1 Eb3:2 Bb3:1
Ab2:2 Eb3:1 C3:2 G3:1
Bb2:2 F3:1 D3:2 F3:1
F3:2 C4:1 Ab3:2 F3:1
Eb3:2 Bb3:1 G3:2 Bb3:1
Ab2:2 Eb3:1 Bb2:2 F3:1
Bb2:2 F3:1 Eb3:2 R:1
C3:1 G3+Bb3:2 Ab2:1 Eb3+G3:2
Eb3:1 G3+Bb3:2 C3:1 G3+Bb3:2
Ab2:1 Eb3+G3:2 Bb2:1 F3+Ab3:2
Eb3:1 G3+Bb3:2 Bb2:2 R:1
Eb3:1 G3+Bb3:2 D3:1 F3+Ab3:2
C3:1 G3+Bb3:2 Eb3:1 G3+Bb3:2
Bb2:1 F3+Ab3:2 Eb3:1 G3+Bb3:2
Eb3+Bb3:6''',
 tempos=[82,82,84,80,84,84,82,80,84,84,86,84,86,88,86,82,80,80,82,80,82,82,80,78],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],
 sections={1:'p',5:'mp',9:'p',13:'mf',17:'pp',21:'p',24:'pp'},
 lower_sections={1:'pp',5:'p',9:'pp',13:'mp',17:'pp'},
 hairpins=[('crescendo',9,13),('diminuendo',14,16),('diminuendo',21,24)],
 hidden_voice_rests={'inner':list(range(1,9))+list(range(17,25))},
 voice_phrases=[dict(voice='inner',start_beat=48,end_beat=72,swell=2),dict(voice='inner',start_beat=72,end_beat=95,swell=3)],
 engraving=dict(spacing_system=20,spacing_staff=21,pedal_offset_y=640),
 pedal=[[i*6,i*6+2.8] for i in range(24)]+[])

dance(op=279,title='Acacia Switchback',key='D',fifths=2,meter='7/8',bpm=94,parent=273,
 source=dict(source_opus=273,source_hand='rh',source_start_beat=0,source_end_beat=2,source_pitches=['D','C#','B','A'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=21,end_beat=24.5,pitches=['D','C#','B','A']),
 description='A bright seven-eighth dance keeps moving its longer step. An ascending call is answered by clipped chord pairs, then the bass shifts the balance from two-two-three to three-two-two. The middle briefly opens into Lydian colour; the final ascent stops cleanly rather than fading.',
 technical='Let the changing long beat remain buoyant. Keep the right-hand offbeat chords separate from the lower anchors and avoid accenting every short note. The register moves are prepared by longer notes or rests.',
 rh='''F#5:1 A5:1 E5:1.5
D5:.5 F#5:.5 G5:1 A5:1 R:.5
B5:1 A5:.5 F#5:1 E5:1
D5:1.5 C#5:1 B4:1
A4:.5 C#5:.5 E5:.5 F#5:1 E5:1
D5:2 R:1.5
D5:1 C#5:.5 B4:1 A4:1
F#4:.5 A4:.5 D5:.5 E5:1 F#5:1
R:.5 B4+D5:1 C#5+E5:1 D5+F#5:1
E5+G5:1.5 D5+F#5:1 C#5+E5:1
B4+D5:.5 C#5+E5:.5 D5+F#5:.5 E5+G5:1 F#5+A5:1
E5+G5:2 R:1.5
G#5:1 B5:1 A5:1.5
F#5:.5 G#5:.5 A5:.5 B5:1 C#6:1
B5:1 A5:1 G#5:1.5
F#5:1 E5:.5 D5:1 C#5:1
B4:.5 D5:.5 F#5:.5 A5:1 G5:1
E5:2 R:1.5
F#5:1 A5:1 E5:1.5
D5:.5 F#5:.5 G5:1 A5:1 R:.5
B5:1 A5:.5 F#5:1 D5:1
C#5:1.5 B4:1 A4:1
D5:.5 E5:.5 F#5:.5 A5:1 B5:1
A5:1 D6:1 R:1.5''',
 lh='''D3:1 F#3+A3:1 E3:1.5
G3:1 B3:1 A3:1 R:.5
E3:1.5 G3+B3:1 A3:1
B2:1 F#3+A3:1 E3:1.5
A2:1.5 E3:1 G3:1
D3+A3:2 R:1.5
G3:1 B3+D4:1 F#3:1.5
D3:1.5 F#3+A3:1 G3:1
B2:1.5 F#3+A3:1 E3:1
A2:1 E3+G3:1 C#4:1.5
G3:1.5 B3+D4:1 A3:1
E3+B3:2 R:1.5
E3:1 G#3+B3:1 F#3:1.5
F#3:1.5 A3+C#4:1 E3:1
G#3:1 B3:1 E3:1.5
F#3:1.5 A3:1 D3:1
G3:1 B3:1 A3:1.5
A2+E3:2 R:1.5
D3:1 F#3+A3:1 E3:1.5
G3:1 B3:1 A3:1 R:.5
E3:1.5 G3+B3:1 F#3:1
A2:1 E3+G3:1 C#4:1.5
B2:1.5 F#3+A3:1 E3:1
D3+A3:2 R:1.5''',
 tempos=[94,94,96,94,96,92,94,96,92,94,96,94,98,100,100,98,96,94,96,96,98,96,100,98],
 phrases=[(1,6),(7,8),(9,12),(13,18),(19,24)],
 sections={1:'mp',5:'mf',7:'p',9:'pp',13:'mp',15:'mf',19:'p',23:'mf'},
 lower_sections={1:'p',5:'mp',7:'p',9:'pp',13:'p',15:'mp',19:'p',23:'mf'},
 hairpins=[('crescendo',1,5),('crescendo',13,15),('diminuendo',16,18),('crescendo',19,23)],
 pedal=[[42,45.3],[45.5,48.8],[49,52.3]])

dance(op=280,title='Daisy Crosswalk',key='G',fifths=1,meter='2/4',bpm=76,parent=273,
 source=dict(source_opus=273,source_hand='rh',source_start_beat=0,source_end_beat=2,source_pitches=['D','C#','B','A'],transposition_semitones=5),
 motif=dict(hand='lh',start_beat=0,end_beat=2,pitches=['G','F#','E','D']),
 description='An offbeat two-step begins with the tune below the chords. Ties carry bright dyads across the downbeat, then a spare walking bass takes over. A rising middle phrase briefly opens the register before the clipped opening returns, ending with a tiny echo.',
 technical='Keep the tied syncopations alive without reattacking them at the bar line. Give the bass quotation a clear line, and separate short chord replies from sustained harmony. The final echo is softer but stays in tempo.',
 rh='''R:.5 G4+B4:.5 R:.5 F#4+A4:.5
E4+G4:.5 R:.5 G4+B4:1
A4+C5:1 B4+D5:.5 C5+E5:.5
B4+D5:1 A4+C5:1
R:.5 G4+B4:1.5~
G4+B4:.5 A4+C5:.5 B4+D5:1
A4+C5:.75 G4+B4:.25 F#4+A4:.5 G4+B4:.5
E4+G4:1 R:1
R:.5 B4+D5:1.5~
B4+D5:.5 C5+E5:.5 D5+F#5:1
E5+G5:.5 D5+F#5:.5 C5+E5:1
B4+D5:1 R:1
D5:.5 G5:.5 B5:1
A5:.75 G5:.25 E5:.5 D5:.5
C5:.5 E5:.5 G5:.5 A5:.5
F#5:1 D5:1
B4:1 R:1
R:.5 C5:.5 D5:1
E5:1 R:1
R:.5 D5:.5 B4:1
A4:.5 B4:.5 C5:.5 D5:.5
E5:.75 F#5:.25 G5:1
F#5:.5 E5:.5 D5:.5 C5:.5
B4:1 R:1
R:.5 G4+B4:.5 R:.5 F#4+A4:.5
E4+G4:.5 R:.5 G4+B4:1
A4+C5:1 B4+D5:.5 C5+E5:.5
B4+D5:1 A4+C5:1
R:.5 G4+B4:1.5~
G4+B4:.5 A4+C5:.5 B4+D5:1
G4+B4+D5:1 R:1
B4:.5 G4:.5 R:1''',
 lh='''G3:.5 F#3:.5 E3:.5 D3:.5
C3:.5 E3:.5 G3:1
D3:.5 F#3:.5 A3:1
G3:.5 D3:.5 E3:1
C3:.5 G3:.5 E3:1
E3:.5 B3:.5 G3:1
D3:.5 A3:.5 F#3:.5 D3:.5
C3:1 R:1
G3:.5 D3:.5 F#3:1
B2:.5 F#3:.5 A3:1
C3:.5 G3:.5 E3:1
G3:1 R:1
G3:.5 B3:.5 D4:1
E3:.5 G3:.5 B3:1
C3:.5 E3:.5 G3:1
D3:.5 F#3:.5 A3:1
G3:.5 D3:.5 B2:.5 D3:.5
E3:.5 F#3:.5 G3:.5 E3:.5
C3:.5 E3:.5 G3:.5 A3:.5
B3:.5 A3:.5 G3:.5 D3:.5
F#3:.5 E3:.5 D3:.5 C3:.5
B2:.5 D3:.5 E3:.5 G3:.5
D3:.5 E3:.5 F#3:.5 A3:.5
G3:1 R:1
G3:.5 F#3:.5 E3:.5 D3:.5
C3:.5 E3:.5 G3:1
D3:.5 F#3:.5 A3:1
G3:.5 D3:.5 E3:1
C3:.5 G3:.5 E3:1
D3:.5 A3:.5 F#3:1
G3:1 R:1
R:2''',
 tempos=[76,76,78,76,76,78,78,74,78,80,80,76,82,82,84,80,74,74,76,76,78,80,78,76,76,76,78,76,76,78,76,76],
 phrases=[(1,4),(5,8),(9,12),(13,16),(18,18),(20,24),(25,28),(29,31),(32,32)],
 lower_phrases=[(1,4),(17,20),(21,24)],
 sections={1:'p',5:'mp',9:'p',13:'mf',17:'pp',21:'p',25:'mp',31:'mf',32:'pp'},
 lower_sections={1:'mp',5:'p',9:'pp',13:'mp',17:'mp',21:'p',25:'mp',31:'mf',32:'pp'},
 hairpins=[('crescendo',9,11),('diminuendo',14,16),('crescendo',21,23)])

dance(op=281,title='Primrose Threshold',key='d',fifths=-1,meter='9/8',bpm=88,parent=270,
 source=dict(source_opus=270,source_hand='rh',source_start_beat=0,source_end_beat=4,source_pitches=['D','C','A','G'],transposition_semitones=0),
 motif=dict(hand='lh',start_beat=54,end_beat=58.5,pitches=['D','C','A','G']),
 description='A spring dance in rainlight: three lilting pulses carry a minor melody that keeps reaching upward. The bass takes the inherited descent during a quiet interlude. Dorian brightness then gathers around the returning tune, and its final third opens into major.',
 technical='Keep three large beats through the written dotted rhythms. Bring out the bass interlude without making the accompanying upper dyads heavy. Allow the final major third to appear naturally within the same pulse.',
 rh='''F5:1.5 A5:1 D6:.5 C6:1.5
A5:1 G5:.5 F5:1.5 E5:1.5
D5:1.5 F5:.5 A5:1 G5:1.5
E5:1.5 C#5:1 D5:.5 R:1.5
F5:.5 A5:.5 C6:.5 Bb5:1.5 A5:1.5
G5:1.5 E5:1 D5:.5 C5:1.5
B4:1.5 D5:.5 F5:1 A5:1.5
G5:1.5 E5:1.5 R:1.5
A5:1.5 C6:1 B5:.5 A5:1.5
G5:1 F5:.5 E5:1.5 D5:1.5
F5:1.5 A5:.5 G5:1 E5:1.5
D5:3 R:1.5
F4+A4:3~ F4+A4:1.5
E4+G4:3 F4+A4:1.5
G4+B4:1.5 A4+C5:1.5 B4+D5:1.5
G4+C#5:3 R:1.5
F5:1.5 A5:1 D6:.5 C6:1.5
B5:1 A5:.5 G5:1.5 E5:1.5
D5:1.5 F5:.5 A5:1 B5:1.5
A5:1.5 F5:1.5 R:1.5
E5:.5 G5:.5 B5:.5 A5:1.5 F5:1.5
E5:1.5 D5:1 C5:.5 A4:1.5
B4:1.5 C#5:1.5 E5:1.5
F#4+A4+D5:3~ F#4+A4+D5:1.5''',
 lh='''D3:1.5 A3:1 F3:.5 E3:1.5
Bb2:1.5 F3+A3:1.5 C4:1.5
G3:1.5 Bb3:1 A3:.5 F3:1.5
A2:1.5 E3+G3:1.5 R:1.5
F3:1.5 A3:1 G3:.5 E3:1.5
C3:1.5 G3+Bb3:1.5 E3:1.5
G3:1.5 B3:1 A3:.5 F3:1.5
A2:1.5 E3:1.5 R:1.5
F3:1.5 A3+C4:1.5 E3:1.5
G3:1.5 B3:1 A3:.5 E3:1.5
D3:1.5 A3:1 F3:.5 E3:1.5
D3+A3:3 R:1.5
D3:1 C3:.5 A2:1.5 G2:1.5
C3:1.5 E3:.5 G3:1 F3:1.5
E3:1 F3:.5 G3:1.5 B3:1.5
A3:1.5 E3:1.5 R:1.5
D3:1.5 A3:1 F3:.5 E3:1.5
G3:1.5 B3:1 A3:.5 F3:1.5
E3:1.5 G3+B3:1.5 D3:1.5
D3:1.5 A3:1.5 R:1.5
G3:1.5 B3:1 A3:.5 E3:1.5
C3:1.5 G3:1 E3:.5 F3:1.5
G3:1.5 A3:1.5 E3:1.5
D3+A3:3~ D3+A3:1.5''',
 tempos=[88,88,90,86,90,90,92,88,92,92,90,86,82,82,84,84,90,92,94,90,92,90,88,88],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],lower_phrases=[(13,16)],
 sections={1:'p',5:'mp',9:'mf',13:'pp',17:'mp',21:'mf',24:'p'},
 lower_sections={1:'pp',5:'p',9:'mp',13:'mp',17:'p',21:'mp',24:'p'},
 hairpins=[('crescendo',5,9),('diminuendo',10,12),('crescendo',17,19),('diminuendo',22,24)],
 pedal=[[i*4.5,i*4.5+(2.8 if i in [3,7,11,15,19] else 4.2)] for i in range(24)])

dance(op=282,title='Peach Vestibule',key='E',fifths=4,meter='3/4',bpm=80,parent=276,
 source=dict(source_opus=276,source_hand='lh',source_start_beat=36,source_end_beat=39,source_pitches=['A','G#','F#','E'],transposition_semitones=7),
 motif=dict(hand='rh',start_beat=12,end_beat=15,pitches=['E','D#','C#','B']),
 description='A five-bar waltz phrase hovers around E, opening its doors a little late. Chordal replies pass through C-sharp minor and a brief warm C-major reflection. On returning, the melody changes direction and climbs into a bright, spacious ending.',
 technical='Keep the five-bar phrases continuous. Voice the tied dyads without repeating their downbeat, and make the chromatic colour changes with a relaxed hand. The final register change follows a full written breath.',
 rh='''R:.5 G#5:.5 B5:1 F#5:1
E5:1.5 G#5:.5 F#5:1
C#5:.75 E5:.25 A5:1 G#5:1
F#5:1 E5:.5 D#5:.5 C#5:1
E5:.75 D#5:.25 C#5:1 B4:1
A4+C#5:1 B4+D#5:1 C#5+E5:1
B4+D#5:1.5 A4+C#5:.5 G#4+B4:1
F#4+A4:1 G#4+B4:1 R:1
G#4+C#5:2 B4+E5:1~
B4+E5:1 A4+D#5:1 G#4+C#5:1
F#4+B4:1.5 E4+A4:.5 D#4+G#4:1
E4+G#4:2 R:1
G4:1 C5:.75 E5:.25 D5:1
C5:1.5 B4:.5 A4:1
G4:1 B4:.5 D5:.5 F5:1
D#5:1 B4:1 R:1
R:.5 G#5:.5 B5:1 F#5:1
E5:1.5 G#5:.5 A5:1
B5:1 A5:.5 G#5:.5 F#5:1
E5:.75 F#5:.25 G#5:1 B5:1
A5:1 G#5:1 F#5:1
G#5:1 B5:1 E6:1
D#6:1 C#6:.5 B5:.5 A5:1
G#5:1 F#5:1 E5:1
C#5+E5:1 B4+D#5:1 A4+C#5:1
G#4+B4:1 F#4+A4:1 G#4+B4:1
A4+C#5:1 B4+D#5:1 R:1
G#5+B5+E6:3''',
 lh='''E3:1 G#3+B3:1 F#3:1
C#3:1 G#3+B3:1 E3:1
A2:1 E3+G#3:1 C#4:1
B2:1 F#3+A3:1 D#3:1
E3:1 G#3+B3:1 F#3:1
A2:1 E3:1 C#4:1
B2:1 F#3:1 A3:1
E3:1 B3:1 R:1
C#3:1 G#3:1 E3:1
F#3:1 A3:1 B3:1
D#3:1 F#3:1 B2:1
E3:2 R:1
C3:1 E3+G3:1 B3:1
A2:1 E3+G3:1 C4:1
G3:1 B3:1 D4:1
B2:1 F#3:1 R:1
E3:1 G#3+B3:1 F#3:1
C#3:1 G#3+B3:1 E3:1
F#3:1 A3+C#4:1 E3:1
E3:1 G#3+B3:1 F#3:1
A2:1 E3+G#3:1 C#4:1
E3:1 G#3:1 B3:1
F#3:1 A3:1 C#4:1
B2:1 F#3+A3:1 D#3:1
A2:1 E3:1 C#4:1
E3:1 B3:1 G#3:1
F#3:1 B3:1 R:1
E3+B3:3''',
 tempos=[80,80,82,80,78,82,82,80,78,78,80,78,76,76,78,78,80,82,84,84,82,86,86,84,80,80,78,80],
 phrases=[(1,5),(6,8),(9,12),(13,16),(17,21),(22,24),(25,27)],
 sections={1:'p',6:'mp',9:'pp',13:'p',17:'mp',22:'mf',25:'pp',28:'mf'},
 lower_sections={1:'pp',6:'p',9:'pp',13:'pp',17:'p',22:'mp',25:'pp',28:'mp'},
 hairpins=[('crescendo',17,22),('diminuendo',23,24)],
 pedal=[[i*3,i*3+2.8] for i in [0,1,2,3,4,8,9,10,12,13,14,16,17,18,19,20,21,22,23,27]])

dance(op=283,title='Iris Tramline',key='C',fifths=0,meter='3/8',bpm=72,parent=275,
 source=dict(source_opus=275,source_hand='rh',source_start_beat=0,source_end_beat=2.5,source_pitches=['D','C','A','G'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=12,end_beat=15,pitches=['D','C','A','G']),
 description='A tiny fast-turning waltz alternates three light steps with two longer ones. The tune flickers between single notes and paired thirds; a sudden soft passage stretches the same gait before a bright return. Its final three-note answer is deliberately small.',
 technical='Keep the two-against-three bars even: the dotted eighths divide the entire bar into two. The LH remains light throughout. Do not add pedal or extra time to the clipped rests and final answer.',
 rh='''E5:.75 G5:.75
C6:.5 B5:.5 A5:.5
G5:1 F5:.5
E5:.75 D5:.75
C5:.5 E5:.5 G5:.5
A5:1 R:.5
F5:.75 E5:.75
D5:1 R:.5
D5:.5 C5:.5 A4:.5
G4:1.5
A4:.5 C5:.5 E5:.5
G5:1 R:.5
A4+C5:.75 B4+D5:.75
C5+E5:.5 D5+F5:.5 E5+G5:.5
D5+F5:1 C5+E5:.5
B4+D5:.75 A4+C5:.75
G4+B4:.5 A4+C5:.5 B4+D5:.5
C5+E5:1 R:.5
E5:1.5
D5:.75 B4:.75
C5:1.5
A4:.75 G4:.75
F4:.5 A4:.5 C5:.5
B4:1 R:.5
D5:.5 E5:.5 F#5:.5
G5:.75 A5:.75
B5:.5 A5:.5 G5:.5
E5:1 R:.5
E5:.75 G5:.75
C6:.5 B5:.5 A5:.5
G5:1 E5:.5
D5:.75 C5:.75
B4:.5 D5:.5 F5:.5
E5:1 R:.5
G5:.5 E5:.5 C5:.5
G4:1.5''',
 lh='''C3:.5 E3:.5 G3:.5
A3:.5 G3:.5 E3:.5
C3:.5 G3:.5 E3:.5
G3:.5 D3:.5 B2:.5
C3:.5 E3:.5 G3:.5
F3:1 R:.5
D3:.5 F3:.5 A3:.5
G3:1 R:.5
F3:.5 E3:.5 C3:.5
C3:1.5
A2:.5 C3:.5 E3:.5
G3:1 R:.5
F3:.5 A3:.5 G3:.5
C3:.5 E3:.5 G3:.5
D3:.5 A3:.5 F3:.5
G3:.5 D3:.5 B2:.5
E3:.5 G3:.5 D3:.5
C3:1 R:.5
C3:.5 G3:.5 E3:.5
G3:.5 D3:.5 B2:.5
A2:.5 E3:.5 C3:.5
F3:.5 C3:.5 A2:.5
D3:.5 F3:.5 A3:.5
G3:1 R:.5
D3:.5 F#3:.5 A3:.5
G3:.5 B3:.5 D4:.5
B3:.5 G3:.5 D3:.5
C3:1 R:.5
C3:.5 E3:.5 G3:.5
A3:.5 G3:.5 E3:.5
F3:.5 C3:.5 A2:.5
D3:.5 F3:.5 A3:.5
G3:.5 D3:.5 B2:.5
C3:1 R:.5
C3:.5 E3:.5 G3:.5
C3:1.5''',
 tempos=[72,72,74,72,74,72,72,70,72,70,74,72,76,78,78,76,78,74,64,64,66,66,68,68,72,74,76,72,74,76,76,74,72,72,74,72],
 phrases=[(1,6),(7,8),(9,12),(13,18),(19,24),(25,28),(29,34),(35,36)],
 sections={1:'p',5:'mp',9:'p',13:'mf',19:'pp',25:'mp',29:'mf',35:'pp'},
 lower_sections={1:'pp',5:'p',9:'pp',13:'mp',19:'pp',25:'p',29:'mp',35:'pp'},
 hairpins=[('crescendo',13,15),('diminuendo',16,18),('crescendo',25,27)],
 system_starts=list(range(1,37,3)),page_starts=[13,25])

dance(op=284,title='Marigold Courtyard',key='F',fifths=-1,meter='4/4',bpm=84,parent=271,
 source=dict(source_opus=271,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['F','E','D','C'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=40,end_beat=44,pitches=['F','E','D','C']),
 description='A gently syncopated courtyard dance places the bass in three-three-two steps. The melody hangs behind it, gathering sixths and ninths before a quiet descending recollection. A broad chordal middle gives way to a lighter return; the last bass step sounds after the melody has gone.',
 technical='Keep the three-three-two bass cell steady while the RH enters late and ties over bar lines. Voice the chordal middle from the top, and leave the final bass note clear of pedal and upper sound.',
 rh='''R:.5 A4:.5 F5:1.5 E5:.5 D5:1
C5:1.5 E5:.5 G5:2~
G5:1 F5:.5 E5:.5 D5:1 A4:1
Bb4:1 C5:.5 D5:.5 E5:1 R:1
A4:.5 C5:.5 F5:1 G5:.5 A5:.5 C6:1
B5:1.5 G5:.5 E5:1 D5:1
C5:.5 E5:.5 G5:1 A5:.5 G5:.5 F5:1
E5:2 D5:1 R:1
A4+C5:2 G4+B4:1 A4+C5:1
Bb4+D5:1.5 A4+C5:.5 G4+Bb4:2
F5:1 E5:1 D5:1 C5:1
A4:2 G4:1 R:1
A4+C5+F5:1.5 C5+E5+G5:1.5 D5+F5+A5:1
C5+E5+G5:2 Bb4+D5+F5:1 A4+C5+E5:1
G4+Bb4+D5:1.5 A4+C5+E5:1.5 Bb4+D5+F5:1
A4+C5+F5:3 R:1
R:.5 A4:.5 F5:1.5 E5:.5 D5:1
C5:1.5 E5:.5 G5:2~
G5:1 A5:.5 G5:.5 F5:1 D5:1
E5:1 C5:.5 A4:.5 G4:1 R:1
Bb4:1 D5:.5 F5:.5 A5:1 G5:1
F5:1 E5:.5 D5:.5 C5:1 A4:1
G4:1 A4:.5 C5:.5 F5:1 E5:1
F5:2 R:2''',
 lh='''F3:1.5 A3+C4:1.5 G3:1
C3:1.5 G3+Bb3:1.5 E3:1
D3:1.5 F3+A3:1.5 C4:1
C3:1.5 G3:1.5 R:1
F3:1.5 A3+C4:1.5 E3:1
E3:1.5 G3+B3:1.5 D4:1
C3:1.5 G3+Bb3:1.5 A3:1
C3:1.5 G3:1.5 R:1
F3:2 C3:1 E3:1
Bb2:1.5 F3:1.5 D3:1
Bb2:1.5 F3+A3:1.5 C4:1
C3:2 E3:1 R:1
F3:1.5 C4:1.5 A3:1
E3:1.5 Bb3:1.5 G3:1
G3:1.5 D4:1.5 Bb3:1
F3+C4:3 R:1
D3:1.5 F3+A3:1.5 C4:1
C3:1.5 G3+Bb3:1.5 E3:1
Bb2:1.5 F3+A3:1.5 G3:1
C3:1.5 G3:1.5 R:1
Bb2:1.5 F3+A3:1.5 C4:1
C3:1.5 G3+Bb3:1.5 E3:1
F3:1.5 A3+C4:1.5 G3:1
F3:2 R:1 C3:1''',
 tempos=[84,84,86,82,88,88,90,84,78,78,80,78,86,86,88,84,84,84,86,82,86,84,82,82],
 phrases=[(1,4),(5,8),(9,10),(11,12),(13,16),(17,20),(21,24)],
 sections={1:'p',5:'mf',9:'pp',13:'mf',17:'p',21:'mp',24:'pp'},
 lower_sections={1:'p',5:'mp',9:'pp',13:'mp',17:'p',21:'p',24:'pp'},
 hairpins=[('crescendo',1,3),('diminuendo',6,8),('crescendo',13,15),('diminuendo',21,24)],
 pedal=[[i*4,i*4+2.8] for i in [0,1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,22]])

dance(op=285,title='Apple Roundabout',key='Bb',fifths=-2,meter='3/4',bpm=88,parent=274,
 source=dict(source_opus=274,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['Bb','A','G','F'],transposition_semitones=0),
 motif=dict(hand='lh',start_beat=22,end_beat=25,pitches=['Bb','A','G','F']),
 description='Three waltz bars repeatedly lose a step in their fourth. A rising tune makes the shortened turn feel playful rather than abrupt; the bass later reveals a falling relative beneath quiet chords. The reprise changes its harmony, and a bright short bar closes the circle.',
 technical='Keep the quarter-note pulse constant through the 3/4 and 2/4 changes. The missing beat is part of the dance, not a cue to hesitate. Bring the central bass phrase forward and keep the closing chords light.',
 rh='''D5:1 F5:.5 Bb5:.5 A5:1
G5:1.5 F5:.5 D5:1
Eb5:.5 G5:.5 F5:1 D5:1
C5:1 R:1
Bb4:1 D5:.5 F5:.5 G5:1
A5:1 G5:.5 F5:.5 Eb5:1
D5:1 C5:.5 Bb4:.5 A4:1
Bb4:1 R:1
D5+F5:3
C5+Eb5:2 Bb4+D5:1
A4+C5:1 Bb4+D5:1 C5+Eb5:1
D5+F5:1 R:1
G5:1 Bb5:.5 A5:.5 G5:1
F5:1.5 Eb5:.5 D5:1
C5:.5 Eb5:.5 G5:1 F5:1
E5:1 R:1
D5:1 F5:.5 Bb5:.5 A5:1
G5:1.5 F5:.5 D5:1
Eb5:.5 G5:.5 A5:1 Bb5:1
F5:1 R:1
D5+F5:1 Eb5+G5:.5 F5+A5:.5 G5+Bb5:1
F5+A5:1 Eb5+G5:.5 D5+F5:.5 C5+Eb5:1
Bb4+D5:1 A4+C5:1 C5+Eb5:1
Bb4+D5+F5:2''',
 lh='''Bb2:1 F3+A3:1 D4:1
Eb3:1 G3+Bb3:1 F3:1
C3:1 G3+Bb3:1 Eb3:1
F3:1 R:1
G3:1 Bb3+D4:1 F3:1
F3:1 A3+C4:1 G3:1
Eb3:1 G3+Bb3:1 F3:1
Bb2:1 R:1
Bb3:.5 A3:.5 G3:1 F3:1
Eb3:1 G3:.5 Bb3:.5 A3:1
G3:1 F3:.5 Eb3:.5 C3:1
Bb2:1 R:1
G3:1 Bb3+D4:1 A3:1
F3:1 A3+C4:1 G3:1
C3:1 G3+Bb3:1 F3:1
C3:1 R:1
G3:1 Bb3+D4:1 F3:1
Eb3:1 G3+Bb3:1 F3:1
C3:1 G3+Bb3:1 F3:1
F3:1 R:1
Bb2:1 F3:1 G3:1
D3:1 F3:1 A3:1
Eb3:1 F3:1 C3:1
Bb2+F3:2''',
 meters=['3/4','3/4','3/4','2/4']*6,
 tempos=[88,88,90,88,90,92,90,88,82,82,84,82,92,94,94,90,88,88,90,88,92,94,92,90],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],lower_phrases=[(9,12)],
 sections={1:'p',5:'mp',9:'pp',13:'mf',17:'p',21:'mf'},
 lower_sections={1:'p',5:'p',9:'mp',13:'mp',17:'p',21:'mp'},
 hairpins=[('crescendo',5,7),('diminuendo',14,16),('crescendo',21,23)],
 pedal=[[22,24.8],[25,27.8],[28,30.8]])

dance(op=286,title='Willow Kiteway',key='D',fifths=2,meter='6/8',bpm=108,parent=285,
 source=dict(source_opus=285,source_hand='lh',source_start_beat=22,source_end_beat=25,source_pitches=['Bb','A','G','F'],transposition_semitones=4),
 motif=dict(hand='rh',start_beat=24,end_beat=27,pitches=['D','C#','B','A']),
 description='A high, wind-borne dance opens in wide melodic arcs, then gathers quick turning figures. A lower recollection briefly grounds it before rising thirds and sixteenth-note curls lift the tune again. The final gesture lands lightly on an open D.',
 technical='Treat the semiquaver turns as small continuous motions, with a loose wrist. Keep the bass in two large pulses while the melody alternates flowing runs and broader thirds. The quiet recollection should retain its momentum.',
 rh='''F#5:.5 A5:.5 D6:.5 E6:1 D6:.5
C#6:1 B5:.5 A5:1 F#5:.5
G5:.5 B5:.5 D6:.5 C#6:1 B5:.5
A5:1 F#5:.5 E5:1 R:.5
D5:.25 E5:.25 F#5:.25 G5:.25 A5:1 B5:.5 A5:.5
G5:.25 F#5:.25 E5:.25 D5:.25 C#5:1 E5:.5 F#5:.5
G5:.5 A5:.5 B5:.5 A5:.25 G5:.25 F#5:.5 E5:.5
D5:1.5 R:1.5
D5:.5 C#5:.5 B4:.5 A4:1.5
F#4:1 A4:.5 D5:1 E5:.5
F#5:1 E5:.5 C#5:1 B4:.5
A4:1.5 R:1.5
D5+F#5:1 E5+G5:.5 F#5+A5:1 G5+B5:.5
A5+C#6:1 G5+B5:.5 F#5+A5:1 E5+G5:.5
D5+F#5:.5 E5+G5:.5 F#5+A5:.5 G5+B5:1 F#5+A5:.5
E5+G5:1.5 D5+F#5:1 R:.5
F#5:.25 G#5:.25 A5:.25 B5:.25 C#6:1 B5:.5 A5:.5
G#5:1 F#5:.5 E5:.25 F#5:.25 G#5:.25 A5:.25 B5:.5
A5:.5 G5:.5 F#5:.5 E5:.5 D5:.5 C#5:.5
D5:1.5 R:1.5
F#5:.5 A5:.5 D6:.5 E6:1 D6:.5
C#6:1 B5:.5 A5:1 F#5:.5
G5:.25 F#5:.25 E5:.25 D5:.25 C#5:1 E5:1
D5:1.5 R:1.5''',
 lh='''D3:1.5 A3:1 F#3:.5
A2:1.5 E3+G3:1.5
G3:1.5 B3:1 A3:.5
D3:1.5 A3:1 R:.5
D3:1 F#3:.5 A3:1 F#3:.5
A2:1 E3:.5 G3:1 E3:.5
G3:1 B3:.5 A3:1 F#3:.5
D3:1.5 R:1.5
B2:1.5 F#3+A3:1.5
G3:1.5 B3:1 A3:.5
E3:1.5 G3+B3:1.5
A2:1.5 R:1.5
D3:1.5 A3:1 F#3:.5
A2:1.5 E3+G3:1.5
G3:1 B3:.5 A3:1 F#3:.5
D3:1.5 A3:1 R:.5
F#3:1.5 A3+C#4:1.5
E3:1.5 G#3+B3:1.5
G3:1 B3:.5 A3:1 F#3:.5
D3:1.5 R:1.5
D3:1.5 A3:1 F#3:.5
A2:1.5 E3+G3:1.5
G3:1 B3:.5 A3:1 E3:.5
D3+A3:1.5 R:1.5''',
 tempos=[108,108,110,106,112,112,114,108,98,98,100,98,110,112,114,110,114,114,112,108,110,110,108,108],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],
 sections={1:'mp',5:'mf',9:'pp',13:'mp',17:'mf',21:'mp',24:'p'},
 lower_sections={1:'p',5:'mp',9:'pp',13:'p',17:'mp',21:'p',24:'p'},
 hairpins=[('crescendo',1,3),('crescendo',13,15),('diminuendo',18,20)],
 pedal=[[24,26.8],[27,29.8],[30,32.8],[48,50.8],[51,53.8]])

dance(op=287,title='Dogwood Pavilion',key='C',fifths=0,meter='5/4',bpm=84,parent=277,
 source=dict(source_opus=277,source_hand='lh',source_start_beat=24,source_end_beat=27,source_pitches=['D','C','A','G'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=0,end_beat=5,pitches=['D','C','A','G']),
 description='Every attack is a chord. A three-step turn and two-step reply carry the music from pale C-major ninths to a warmer, unexpected flat-side passage. The return thickens briefly, then ends in a quiet sixth, with the melody held inside the final harmony.',
 technical='Project the top line through changing chord shapes. Keep the three-plus-two gait supple and avoid accenting every bass change. Both hands remain within an octave; prepare the soft return during the written rests.',
 rh='''A4+D5:.5 G4+C5:.5 F4+A4:2 E4+G4:2
G4+B4+E5:3 F4+A4+D5:2
E4+G4+C5:2 F4+A4+D5:1 G4+B4+E5:2
F4+A4+C5:3 R:2
A4+C5+F5:1.5 G4+B4+E5:1.5 F4+A4+D5:2
E4+G4+C5:2 D4+F4+B4:1 E4+G4+C5:2
F4+A4+D5:1 G4+B4+E5:1 A4+C5+F5:1 B4+D5+G5:2
G4+B4+E5:3 R:2
Ab4+C5+Eb5:3 G4+Bb4+D5:2
F4+Ab4+C5:2 Eb4+G4+Bb4:1 Db4+F4+Ab4:2
Eb4+G4+C5:1 F4+Ab4+Db5:1 G4+Bb4+Eb5:1 Ab4+C5+F5:2
G4+B4+D5:3 R:2
C5+E5+A5:1.5 B4+D5+G5:1.5 A4+C5+F5:2
G4+B4+E5:2 F4+A4+D5:1 E4+G4+C5:2
F4+A4+D5:1 G4+B4+E5:1 A4+C5+F5:1 G4+B4+E5:2
F4+A4+D5:3 R:2
A4+D5:.5 G4+C5:.5 F4+A4:2 E4+G4:2
G4+B4+E5:3 F4+A4+D5:2
E4+G4+C5:2 F4+A4+D5:1 G4+B4+E5:2
F4+A4+C5:3 R:2
A4+C5+F5:2 G4+B4+E5:1 F4+A4+D5:2
E4+G4+C5:3 D4+F4+B4:2
E4+G4+C5:1 F4+A4+D5:1 G4+B4+E5:1 A4+C5+F5:2
E4+G4+A4:3~ E4+G4+A4:2''',
 lh='''C3+G3:3 F3+C4:2
E3+B3:3 D3+A3:2
C3+G3:2 D3+A3:1 E3+B3:2
F3+C4:3 R:2
F3+C4:3 D3+A3:2
C3+G3:2 G2+D3:1 C3+G3:2
D3+A3:1 E3+B3:1 F3+C4:1 G3+D4:2
C3+G3:3 R:2
Ab2+Eb3:3 G2+D3:2
F3+C4:2 Eb3+Bb3:1 Db3+Ab3:2
C3+G3:1 Db3+Ab3:1 Eb3+Bb3:1 F3+C4:2
G2+D3:3 R:2
A2+E3:3 G2+D3:2
C3+G3:2 D3+A3:1 E3+B3:2
D3+A3:1 E3+B3:1 F3+C4:1 E3+B3:2
D3+A3:3 R:2
F3+C4:3 C3+G3:2
E3+B3:3 D3+A3:2
C3+G3:2 D3+A3:1 E3+B3:2
F3+C4:3 R:2
F3+C4:2 E3+B3:1 D3+A3:2
C3+G3:3 G2+D3:2
C3+G3:1 D3+A3:1 E3+B3:1 F3+C4:2
C3+G3:3~ C3+G3:2''',
 tempos=[84,84,86,82,88,88,90,84,78,78,80,80,90,90,92,86,84,84,86,82,84,82,80,80],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],
 sections={1:'p',5:'mp',9:'pp',13:'mf',17:'p',21:'mp',24:'pp'},
 lower_sections={1:'pp',5:'p',9:'pp',13:'mp',17:'pp',21:'p',24:'pp'},
 hairpins=[('crescendo',5,7),('crescendo',9,11),('diminuendo',14,16),('diminuendo',21,24)],
 pedal=[[i*5,i*5+2.8] for i in range(24)])

dance(op=288,title='Linden Maywalk',key='G',fifths=1,meter='3/4',bpm=78,parent=280,
 source=dict(source_opus=280,source_hand='lh',source_start_beat=0,source_end_beat=2,source_pitches=['G','F#','E','D'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=48,end_beat=51,pitches=['G','F#','E','D']),
 description='A gently ambling waltz begins with a descending answer rather than a grand entrance. In the centre, the left hand divides into a held bass and a moving tenor, while the melody opens above them. The later falling quotation restores a simpler texture, ending on the warm side of an unresolved ninth.',
 technical='Balance the central three voices separately. Hold the bass with the little finger while the tenor moves without reattacking the held key; all complete hand spans remain within an octave. Keep the return light after the fuller middle.',
 rh='''D5:2 B4:.5 G4:.5
A4:1 C5:.5 E5:.5 D5:1
B4:1.5 D5:.5 G5:1
F#5:1 E5:1 R:1
D5:.5 G5:.5 B5:1 A5:1
G5:1 F#5:.5 E5:.5 D5:1
C5:1.5 B4:.5 A4:1
D5:2 R:1
B4:2 D5:1
E5:1 G5:2
E5:1.5 D5:.5 C5:1
A4:1 C5:1 D5:1
E5:2 G5:1
F#5:1 D5:2
C5:1 E5:.5 G5:.5 F#5:1
D5:2 R:1
G5:1 F#5:.5 E5:.5 D5:1
B4:1 D5:.5 G5:.5 A5:1
B5:1 A5:.5 G5:.5 E5:1
D5:1 B4:1 R:1
C5:1 E5:.5 G5:.5 A5:1
F#5:1 D5:.5 C5:.5 A4:1
B4:1 D5:1 G5:1
A4+B4+D5:3''',
 lh='''G3:1 B3:1 D4:1
C3:1 G3:1 E3:1
E3:1 G3+B3:1 D4:1
D3:1 A3:1 R:1
G3:1 B3+D4:1 F#3:1
E3:1 G3+B3:1 D3:1
C3:1 G3:1 E3:1
D3:2 R:1
G2:3
E2:3
C3:3
D3:3
C3:3
B2:3
A2:3
D3:2 R:1
E3:1 G3+B3:1 D3:1
C3:1 G3+B3:1 E3:1
G3:1 B3+D4:1 A3:1
D3:1 A3:1 R:1
C3:1 G3:1 E3:1
D3:1 A3:1 F#3:1
G3:1 D3:1 B2:1
G2+D3:3''',
 lh_upper='''R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3
D3:.5 G3:.5 F#3:1 E3:.5 D3:.5
G2:.5 B2:.5 D3:1 B2:.5 G2:.5
E3:.5 G3:.5 B3:1 A3:.5 G3:.5
F#3:.5 A3:.5 C4:1 A3:.5 F#3:.5
E3:1 G3:.5 A3:.5 G3:1
D3:.5 F#3:.5 A3:1 F#3:.5 D3:.5
C3:.5 E3:.5 G3:1 E3:.5 C3:.5
F#3:1 A3:1 R:1
R:3
R:3
R:3
R:3
R:3
R:3
R:3
R:3''',
 tempos=[78,78,80,78,82,82,80,76,78,80,80,82,84,84,82,78,78,80,82,78,80,78,76,76],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24)],
 sections={1:'p',5:'mp',9:'p',13:'mf',17:'pp',21:'p',24:'pp'},
 lower_sections={1:'pp',5:'p',9:'p',13:'mp',17:'pp'},
 hairpins=[('crescendo',9,13),('diminuendo',14,16),('diminuendo',21,24)],
 hidden_voice_rests={'tenor':list(range(1,9))+list(range(17,25))},
 voice_phrases=[dict(voice='tenor',start_beat=24,end_beat=36,swell=3),dict(voice='tenor',start_beat=36,end_beat=47,swell=4)],
 engraving=dict(spacing_system=20,spacing_staff=21,pedal_offset_y=640),
 pedal=[[i*3,i*3+2.8] for i in [0,1,2,4,5,6,8,9,10,11,12,13,14,16,17,18,20,21,22,23]])
PIECES[-1]['performance']['tenor_entries']=[[24,47]]

dance(op=289,title='Quince Semaphore',key='F',fifths=-1,meter='2/4',bpm=88,parent=284,
 source=dict(source_opus=284,source_hand='rh',source_start_beat=40,source_end_beat=44,source_pitches=['F','E','D','C'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=48,end_beat=50,pitches=['F','E','D','C']),
 description='A quick exchange of bright signals passes between the hands. Small chromatic turns enliven the tune; a complete bar of silence opens the way to a chordal response. The familiar descending fragment appears near the end, and the last two chords answer each other across a breath.',
 technical='Maintain one pulse through the alternating hands and the silent bar. Keep the chromatic sixteenth notes light. Release the bright chords completely, including the gap before the final reply.',
 rh='''C5:.5 F5:.5 A5:1
R:1 G5:.5 F5:.5
E5:.5 G5:.5 Bb5:1
A5:1 R:1
F5:.25 E5:.25 Eb5:.25 D5:.25 C5:1
R:.5 D5:.5 F5:1
G5:.5 A5:.5 C6:.5 Bb5:.5
A5:1 R:1
R:1 F5:.5 E5:.5
D5:1 R:1
R:.5 C5:.5 E5:.5 G5:.5
F5:1 R:1
A4:.25 Bb4:.25 B4:.25 C5:.25 D5:.5 E5:.5
F5:.5 A5:.5 G5:.5 E5:.5
F5:1 R:1
R:2
A4+C5+F5:1 C5+E5+G5:1
D5+F5+A5:.5 C5+E5+G5:.5 Bb4+D5+F5:1
A4+C5+E5:.5 G4+Bb4+D5:.5 F4+A4+C5:1
G4+Bb4+E5:1 R:1
A4+C5+F5:1 G4+B4+E5:1
F4+A4+D5:.5 G4+B4+E5:.5 A4+C5+F5:1
Bb4+D5+G5:1 G4+Bb4+E5:1
A4+C5+F5:1 R:1
F5:.5 E5:.5 D5:.5 C5:.5
A4:1 C5:.5 F5:.5
G5:.25 A5:.25 Bb5:.25 A5:.25 G5:.5 E5:.5
F5:1 R:1
R:.5 A4:.5 C5:1
D5:.5 E5:.5 G5:1
A4+C5+F5:1 R:1
A4+C5+F5:1 R:1''',
 lh='''F3:1 A3:1
C3:.5 E3:.5 G3:1
C3:1 G3:1
F3:1 R:1
D3:1 F3:1
G3:.5 Bb3:.5 A3:1
C3:.5 E3:.5 G3:1
F3:1 R:1
D3:.5 F3:.5 A3:1
Bb2:.5 D3:.5 F3:1
C3:.5 G3:.5 E3:1
F3:1 R:1
F3:1 C3:1
G3:.5 A3:.5 Bb3:.5 G3:.5
F3:1 R:1
R:2
F3+C4:1 E3+Bb3:1
D3+A3:1 G3+B3:1
C3+G3:1 D3+A3:1
C3+G3:1 R:1
F3+C4:1 E3+B3:1
D3+A3:1 E3+B3:1
G3+D4:1 C3+G3:1
F3+C4:1 R:1
D3:.5 F3:.5 A3:.5 F3:.5
Bb2:1 F3:1
C3:.5 E3:.5 G3:1
F3:1 R:1
C3:.5 E3:.5 G3:1
Bb2:.5 D3:.5 C3:1
F3+C4:1 R:1
F3+C4:1 R:1''',
 tempos=[88,88,90,88,92,92,94,90,84,84,86,84,92,94,90,90,94,94,96,92,94,96,94,92,88,88,92,88,86,88,90,90],
 phrases=[(1,4),(5,8),(9,12),(13,15),(17,20),(21,24),(25,28),(29,30)],
 lower_phrases=[(9,12)],
 sections={1:'mp',5:'mf',9:'pp',13:'mp',17:'mf',21:'mp',25:'p',31:'mf',32:'pp'},
 lower_sections={1:'p',5:'mp',9:'mp',13:'p',17:'mp',21:'p',25:'pp',31:'mf',32:'pp'},
 hairpins=[('crescendo',5,7),('crescendo',17,19),('diminuendo',26,28)])

dance(op=290,title='Apricot Commons',key='F',fifths=-1,meter='6/4',bpm=88,parent=271,
 source=dict(source_opus=271,source_hand='rh',source_start_beat=0,source_end_beat=3,source_pitches=['F','E','D','C'],transposition_semitones=0),
 motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['F','E','D','C']),
 description='The opening dance returns as a wider spring gathering. Its descending ribbon now spans two waltz turns; a singing bass leads the quiet middle, then flowing lower figures carry the melody toward a fuller chordal crest. The coda remembers the opening without withdrawing, finishing on a luminous added ninth.',
 technical='Sustain the long melodic arc across two waltz pulses per bar. Bring the bass forward in the quiet middle, then keep the returning arpeggios below the tune. The final chord is full but unforced, and the pulse remains alive to the end.',
 rh='''F5:1 E5:1 D5:2 C5:2
A4:2 C5:1 F5:2 G5:1
A5:3 G5:1 F5:1 E5:1
D5:2 F5:1 A5:2 G5:1
E5:1 G5:.5 A5:.5 C6:2 B5:1 A5:1
G5:1 F5:1 E5:1 D5:2 C5:1
D5:1 E5:1 F5:1 G5:1 A5:1 C6:1
F5:3 E5:2 R:1
A4+C5:3 G4+B4:3
F4+A4:2 G4+Bb4:1 A4+C5:3
Bb4+D5:3 A4+C5:2 G4+Bb4:1
F4+A4:3 E4+G4:2 R:1
F4+A4+D5:2 G4+Bb4+E5:1 A4+C5+F5:3
G4+B4+E5:3 F4+A4+D5:3
E4+G4+C5:2 F4+A4+D5:1 G4+B4+E5:2 A4+C5+F5:1
G4+Bb4+E5:3 F4+A4+C5:2 R:1
F5:1 E5:1 D5:2 C5:2
A4:1 C5:.5 E5:.5 F5:2 G5:1 A5:1
Bb5:2 A5:1 G5:1 F5:1 D5:1
E5:3 C5:2 R:1
F5:.5 A5:.5 C6:1 B5:1 A5:1 G5:1 E5:1
D5:1 F5:.5 A5:.5 G5:2 E5:1 C5:1
D5:1 E5:1 F5:1 A5:1 G5:1 E5:1
F5:3 C5:2 R:1
A4+C5+F5:2 C5+E5+G5:1 D5+F5+A5:3
C5+E5+G5:2 Bb4+D5+F5:1 A4+C5+E5:3
G4+Bb4+D5:1 A4+C5+E5:1 Bb4+D5+F5:1 C5+E5+G5:2 D5+F5+A5:1
C5+F5+A5:3 Bb4+D5+G5:2 R:1
F5:1 E5:1 D5:2 C5:2
A4:2 C5:1 F5:1 G5:1 A5:1
Bb5:1 A5:1 G5:1 F5:1 E5:1 C5:1
A4+C5+F5+G5:6''',
 lh='''F3:1 A3+C4:2 D3:1 F3+A3:2
Bb2:1 F3+A3:2 C3:1 G3+Bb3:2
F3:1 A3+C4:2 E3:1 G3+Bb3:2
D3:1 F3+A3:2 G3:1 Bb3+D4:2
A2:1 E3+G3:2 G3:1 B3+D4:2
C3:1 G3+Bb3:2 Bb2:1 F3+A3:2
G3:1 Bb3+D4:2 C3:1 G3+Bb3:2
F3:1 A3+C4:2 C3:2 R:1
F3:1 A3:1 C4:1 B3:1 G3:1 E3:1
D3:1 F3:.5 G3:.5 A3:2 G3:1 F3:1
Bb2:1 D3:1 F3:1 A3:1 G3:1 E3:1
F3:1 A3:1 C4:1 G3:2 R:1
D3:1 F3:1 A3:1 C4:1 A3:1 F3:1
E3:1 G3:.5 A3:.5 B3:2 A3:1 F3:1
C3:1 E3:1 G3:1 A3:1 B3:1 C4:1
C3:1 G3:1 Bb3:1 F3:2 R:1
D3:.5 F3:.5 A3:.5 C4:.5 A3:.5 F3:.5 E3:1 F3:1 A3:1
Bb2:.5 D3:.5 F3:.5 A3:.5 F3:.5 D3:.5 C3:1 E3:1 G3:1
G3:.5 Bb3:.5 D4:.5 Bb3:.5 A3:.5 G3:.5 F3:1 A3:1 D3:1
C3:.5 E3:.5 G3:.5 Bb3:.5 G3:.5 E3:.5 C3:2 R:1
F3:.5 A3:.5 C4:.5 A3:.5 G3:.5 E3:.5 D3:1 G3:1 B3:1
D3:.5 F3:.5 A3:.5 C4:.5 A3:.5 F3:.5 E3:1 G3:1 C3:1
Bb2:.5 D3:.5 F3:.5 A3:.5 F3:.5 D3:.5 C3:1 E3:1 G3:1
F3:.5 A3:.5 C4:.5 A3:.5 G3:.5 F3:.5 C3:2 R:1
F3+C4:3 D3+A3:3
C3+G3:3 Bb2+F3:3
G3+D4:1 A3+E4:1 G3+D4:1 C3+G3:2 D3+A3:1
F3+C4:3 G3+D4:2 R:1
Bb2:1 F3+A3:2 C3:1 G3+Bb3:2
D3:1 F3+A3:2 F3:1 A3+C4:2
G3:1 Bb3+D4:2 C3:1 G3+Bb3:2
F2+C3+F3:6''',
 tempos=[88,88,90,90,92,92,94,88,80,80,82,80,84,86,86,82,90,92,94,90,96,96,94,90,94,94,96,92,88,90,92,90],
 phrases=[(1,4),(5,8),(9,12),(13,16),(17,20),(21,24),(25,28),(29,32)],
 lower_phrases=[(9,12),(13,16)],
 sections={1:'p',5:'mp',9:'pp',13:'p',17:'mp',21:'mf',25:'mf',29:'p',32:'mf'},
 lower_sections={1:'pp',5:'p',9:'mp',13:'mp',17:'p',21:'mp',25:'mf',29:'p',32:'mf'},
 hairpins=[('crescendo',1,7),('crescendo',13,15),('crescendo',17,21),('diminuendo',26,28),('crescendo',29,32)],
 pedal=[[i*6+a,i*6+b] for i in range(32) for a,b in [(0,2.8),(3,4.8 if i in [7,11,15,19,23,27] else 5.8)]])
