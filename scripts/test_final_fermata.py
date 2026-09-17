"""Check optional open endings without changing historical score defaults."""
from copy import deepcopy
from pathlib import Path
import json
import mido
from compose import PIECES, make_score

root = Path(__file__).resolve().parents[1]
p = next(p for p in PIECES if p['op'] == 230)
score, events = make_score(p)
count = lambda s: sum(type(e).__name__ == 'Fermata' for n in s.recurse().notes for e in n.expressions)
assert count(score) == 2
explicit = deepcopy(p)
explicit['final_fermata'] = True
assert count(make_score(explicit)[0]) == 2
explicit['final_fermata'] = False
open_score, open_events = make_score(explicit)
assert count(open_score) == 0
assert events == open_events, 'Changing the ending must preserve written pitches and durations'
cat = json.loads((root / 'data/catalog.json').read_text())
for p in cat:
    if p.get('final_fermata') is not False:
        continue
    from xml.etree import ElementTree as ET
    folder = root / 'pieces' / p['folder']
    assert not ET.parse(folder / (p['stem'] + '.musicxml')).findall('.//fermata')
    midi = mido.MidiFile(folder / (p['stem'] + '.mid'))
    tempos = [m.tempo for m in midi.tracks[0] if m.type == 'set_tempo']
    assert tempos[-1] == mido.bpm2tempo(p['performance']['rubato'][-1]), p['op']
print('Final-fermatas passed: historical defaults, unchanged note events, explicit open endings and performed final tempi.')
