"""The seventh volume: individually authored piano studies, beginning at Op. 145."""

PIECES = [
dict(op=145,title='Linden Vestibule',key='C',fifths=0,meter='6/4',bpm=62,
 description='A modal hymn whose upper chords repeatedly arrive ahead of the bass. Elder Horizon’s F–G–F becomes C–D–C. The upper hand carries a late chord across each phrase boundary, letting the next lower harmony arrive beneath it before the upper notes move on. The close opens into G major.',
 difficulty='Advanced anticipations and sustained chord changes',technique_limits=dict(chord_span=12,melodic_leap=17,rapid_leap=9),
 technical_note='All events are chords of at least three pitches. The late RH chords in bars 2, 6 and 10 continue into the following bar without another attack; each new LH chord begins underneath those held notes. Keep the anticipations soft enough to feel like part of the next breath.',
 parent_opus=144,motif=dict(hand='rh',start_beat=0,end_beat=6,pitches=['C','D','C']),ancestry=dict(source_opus=144,source_hand='rh',source_start_beat=0,source_end_beat=6,source_pitches=['F','G','F'],transposition_semitones=-5),
 system_starts=[1,3,5,7,9,11],page_starts=[7],engraving=dict(spacing_system=14,pedal_offset_y=440),lower_sections={1:'p',5:'pp',9:'p',11:'pp'},
 pedal_spans=[[i*6+a,i*6+b-.2] for i,cuts in enumerate([[0,2,3,6],[0,3,6],[0,1,3.5,6],[0,3,6],[0,6],[0,3,6],[0,1,3.5,6],[0,3,6],[0,6],[0,3,6],[0,1,3,6],[0,6]]) for a,b in zip(cuts,cuts[1:])],
 rh='''
E4+G4+C5:2 F4+A4+D5:1 E4+G4+C5:3
R:.5 E4+G4+B4:2.5 F4+A4+C5:3~
F4+A4+C5:1 G4+B4+D5:2.5 A4+C5+E5:2.5
G4+B4+D5:3 F4+A4+C5:3
Eb4+G4+Bb4:6
R:.5 D4+F4+A4:2.5 Eb4+G4+Bb4:3~
Eb4+G4+Bb4:1 F4+Ab4+C5:2.5 G4+Bb4+D5:2.5
F4+Ab4+C5:3 E4+G4+B4:3
E4+G4+C5:6
R:.5 F#4+A4+C5:2.5 G4+B4+D5:3~
G4+B4+D5:1 F#4+A4+C5:2 E4+G4+B4:3
F#4+A4+B4+D5:6
''',lh='''
C3+E3+G3:2 Bb2+D3+F3:1 A2+C3+E3:3
E3+G3+B3:3 F3+A3+C4:3
G2+B2+D3:6
C3+E3+G3:3 F3+A3+C4:3
Eb3+G3+Bb3:6
D3+F3+A3:3 Eb3+G3+Bb3:3
Ab2+C3+Eb3:6
F3+Ab3+C4:3 E3+G3+B3:3
C3+E3+G3:6
D3+F#3+C4:3 G2+B2+D3:3
C3+E3+G3:3 D3+F#3+C4:3
G2+B2+D3:6
''',sections={1:'p',5:'pp',7:'mp',9:'p',11:'pp'},words={1:'dolce',11:'poco rit.'},slurs=[(1,4),(5,8),(9,12)],lower_phrases=[],hairpins=[('crescendo',6,7),('diminuendo',9,11)],tempo_changes={},group=2,
 performance=dict(rubato=[62,59,62,54,57,56,61,52,57,53,43,29],phrase_arcs=[[0,24,2],[24,48,3],[48,72,-1]],lower_entries=[],pedal_lift=.2,gate=.995,note='The upper anticipations pass gently over the bar line. Keep their keys held as the pedal clears, so the bass can change the colour beneath them.'))
]
