"""Round-trip Op. 120's eight groups and reject unsafe bracket numbering."""
import collections
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

from music21 import converter, note
from compose import PIECES, make_score, write_musicxml
from tuplet_engraving import apply_tuplet_spans

ROOT = Path(__file__).resolve().parents[1]
piece = next(p for p in PIECES if p['op'] == 120)
score, events = make_score(piece)
with tempfile.TemporaryDirectory(prefix='tuplet-numbers-', dir=ROOT / 'work') as folder:
    path = Path(folder) / 'source.musicxml'
    write_musicxml(score, piece, path)
    fixed = ET.parse(path).getroot()
    apply_tuplet_spans(fixed, events, piece)
    legacy = copy.deepcopy(fixed)
    for ordinal, spec in enumerate(piece['tuplet_spans'], 1):
        members = [e for e in events if e['hand'] == spec['hand']
                   and spec['start_beat'] <= e['offset'] < spec['end_beat'] - 1e-8]
        members.sort(key=lambda e: e['offset'])
        expected_number = '1' if spec['hand'] == 'rh' else '2'
        for ident, kind in [(members[0]['id'], 'start'), (members[-1]['id'], 'stop')]:
            mark = fixed.find(f'.//note[@id="{ident}"]/notations/tuplet[@type="{kind}"]')
            assert mark is not None and mark.get('number') == expected_number
            legacy.find(f'.//note[@id="{ident}"]/notations/tuplet[@type="{kind}"]').set('number', str(ordinal))
    ET.ElementTree(legacy).write(path, encoding='utf-8', xml_declaration=True)
    try:
        converter.parse(path, forceSource=True)
    except IndexError:
        pass
    else:
        raise AssertionError('The real eight-group importer regression was not reproduced')
    ET.ElementTree(fixed).write(path, encoding='utf-8', xml_declaration=True)
    parsed = converter.parse(path, forceSource=True)
    actual = []
    for part in parsed.parts:
        for n in part.flatten().notes:
            for cn in ([n] if isinstance(n, note.Note) else n.notes):
                if cn.tie is None or cn.tie.type == 'start':
                    actual.append((round(float(n.offset) * 960), cn.pitch.midi))
    expected = [(round(e['offset'] * 960), pitch) for e in events for pitch in e['pitches']]
    assert collections.Counter(actual) == collections.Counter(expected)
    for root in (legacy, fixed):
        for mark in root.findall('.//notations/tuplet'):
            mark.attrib.pop('number', None)
    assert ET.tostring(legacy) == ET.tostring(fixed)
    print('PASS: reproduced importer failure, eight paired groups, exact score onsets/pitches, all other XML preserved')

    # A real earlier score keeps its original six unique bracket identifiers.
    earlier = next(p for p in PIECES if p['op'] == 77)
    old_score, old_events = make_score(earlier)
    write_musicxml(old_score, earlier, path)
    old_xml = ET.parse(path).getroot()
    apply_tuplet_spans(old_xml, old_events, earlier)
    assert sorted(int(m.get('number')) for m in old_xml.findall('.//notations/tuplet[@type="start"]')) == list(range(1, 7))
    print('PASS: Op. 77 retains its six original bracket numbers')

catalogue = json.loads((ROOT / 'data/catalog.json').read_text())
rendered = next(p for p in catalogue if p['op'] == 120)
with tempfile.TemporaryDirectory(prefix='tuplet-number-validator-', dir=ROOT / 'work') as folder:
    fixture = Path(folder)
    for name in ('scripts', 'data', 'pieces', 'work'):
        (fixture / name).mkdir()
    for name in ('validate.py', 'meter_plan.py'):
        shutil.copy2(ROOT / 'scripts' / name, fixture / 'scripts' / name)
    shutil.copytree(ROOT / 'pieces' / rendered['folder'], fixture / 'pieces' / rendered['folder'])
    (fixture / 'data/catalog.json').write_text(json.dumps(catalogue))
    path = fixture / 'pieces' / rendered['folder'] / (rendered['stem'] + '.musicxml')
    original = path.read_bytes()
    for label, duplicate in [('complete score passes', False), ('reusing a bracket number in one bar is rejected', True)]:
        path.write_bytes(original)
        if duplicate:
            tree = ET.parse(path)
            for mark in tree.findall('.//measure[@number="14"]/note/notations/tuplet'):
                mark.set('number', '1')
            tree.write(path, encoding='utf-8', xml_declaration=True)
        result = subprocess.run([sys.executable, str(fixture / 'scripts/validate.py'), '--opus', '120'], capture_output=True, text=True)
        if duplicate:
            assert result.returncode != 0 and 'Unsafe tuplet bracket number' in result.stderr, result.stderr
        else:
            assert result.returncode == 0, result.stderr
        print('PASS: ' + label)
