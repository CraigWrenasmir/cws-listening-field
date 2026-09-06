"""Exercise separate staff dynamics against the real Op. 108 score and MIDI."""
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

import mido

ROOT = Path(__file__).resolve().parents[1]
catalogue = json.loads((ROOT / 'data/catalog.json').read_text())
piece = next(p for p in catalogue if p['op'] == 108)

with tempfile.TemporaryDirectory(prefix='staff-dynamics-', dir=ROOT / 'work') as folder:
    fixture = Path(folder)
    for name in ('scripts', 'data', 'pieces', 'work'):
        (fixture / name).mkdir()
    for name in ('validate.py', 'meter_plan.py'):
        shutil.copy2(ROOT / 'scripts' / name, fixture / 'scripts' / name)
    shutil.copytree(ROOT / 'pieces' / piece['folder'], fixture / 'pieces' / piece['folder'])
    base = fixture / 'pieces' / piece['folder'] / piece['stem']
    score_path = base.with_suffix('.musicxml')
    midi_path = base.with_suffix('.mid')
    original_score, original_midi = score_path.read_bytes(), midi_path.read_bytes()

    def run_case(name, mutation=None, expected_error=None):
        score_path.write_bytes(original_score)
        midi_path.write_bytes(original_midi)
        data = copy.deepcopy(catalogue)
        if mutation:
            mutation(data)
        (fixture / 'data/catalog.json').write_text(json.dumps(data))
        result = subprocess.run([sys.executable, str(fixture / 'scripts/validate.py'),
                                 '--opus', '108'], capture_output=True, text=True)
        if expected_error:
            assert result.returncode != 0 and expected_error in result.stderr, (name, result.stdout, result.stderr)
        else:
            assert result.returncode == 0, (name, result.stdout, result.stderr)
        print(f'PASS: {name}')

    def change_printed_dynamic(data):
        tree = ET.parse(score_path)
        direction = next(d for d in tree.findall('.//measure[@number="1"]/direction')
                         if d.findtext('staff') == '2' and d.find('direction-type/dynamics') is not None)
        direction.find('direction-type/dynamics')[0].tag = 'pp'
        tree.write(score_path, encoding='utf-8', xml_declaration=True)

    def change_midi_velocity(data):
        midi = mido.MidiFile(midi_path)
        note = next(m for t in midi.tracks for m in t
                    if m.type == 'note_on' and m.channel == 1 and m.note == 54 and m.velocity > 0)
        note.velocity += 1
        midi.save(midi_path)

    def change_event_dynamic(data):
        p = next(p for p in data if p['op'] == 108)
        e = next(e for e in p['events'] if e['hand'] == 'lh')
        e['notated_dynamic'] = 'pp'

    run_case('separate printed and performed staff dynamics agree')
    run_case('changed lower printed dynamic is rejected', change_printed_dynamic,
             'Printed staff dynamics differ')
    run_case('changed tenor MIDI velocity is rejected', change_midi_velocity,
             'MIDI voicing differs')
    run_case('stale performed dynamic is rejected', change_event_dynamic,
             'Performed staff dynamic differs')

from compose import PIECES, make_score

source = next(p for p in PIECES if p['op'] == 108)
for label, changes, error in [
    ('missing initial lower dynamic', {9: 'pp'}, 'Lower staff dynamics must begin at bar 1'),
    ('unsupported lower dynamic', {1: 'ffff'}, 'Invalid lower staff dynamics'),
]:
    candidate = copy.deepcopy(source)
    candidate['lower_sections'] = changes
    try:
        make_score(candidate)
    except AssertionError as exc:
        assert error in str(exc), (label, exc)
    else:
        raise AssertionError(f'Accepted {label}')
    print(f'PASS: {label} is rejected')
