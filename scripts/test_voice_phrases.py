"""Check the actual seven-beat tenor phrases in Op. 109."""
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

from compose import PIECES, make_score

ROOT = Path(__file__).resolve().parents[1]
catalogue = json.loads((ROOT / 'data/catalog.json').read_text())
piece = next(p for p in catalogue if p['op'] == 109)
source = next(p for p in PIECES if p['op'] == 109)

with tempfile.TemporaryDirectory(prefix='voice-phrases-', dir=ROOT / 'work') as folder:
    fixture = Path(folder)
    for name in ('scripts', 'data', 'pieces', 'work'):
        (fixture / name).mkdir()
    for name in ('validate.py', 'meter_plan.py'):
        shutil.copy2(ROOT / 'scripts' / name, fixture / 'scripts' / name)
    shutil.copytree(ROOT / 'pieces' / piece['folder'], fixture / 'pieces' / piece['folder'])
    (fixture / 'data/catalog.json').write_text(json.dumps(catalogue))
    path = fixture / 'pieces' / piece['folder'] / (piece['stem'] + '.musicxml')
    for mutated in (False, True):
        if mutated:
            tree = ET.parse(path)
            old = tree.find('.//note[@id="cws109-lh-m6-n1001"]/notations')
            stop = old.find('slur[@type="stop"]')
            assert stop is not None
            old.remove(stop)
            new = tree.find('.//note[@id="cws109-lh-m6-n1002"]/notations')
            new.append(stop)
            tree.write(path, encoding='utf-8', xml_declaration=True)
        result = subprocess.run([sys.executable, str(fixture / 'scripts/validate.py'),
                                 '--opus', '109'], capture_output=True, text=True)
        if mutated:
            assert result.returncode != 0 and 'Independent voice phrase slur differs' in result.stderr, result.stderr
        else:
            assert result.returncode == 0, result.stderr
        print('PASS: shifted tenor phrase endpoint rejected' if mutated else 'PASS: five seven-beat tenor slurs verified')

for label, mutation, error in [
    ('boundary inside a held note', lambda p: p['voice_phrases'][0].update(end_beat=26), 'Voice phrase boundaries must match notes'),
    ('overlapping phrases', lambda p: p['voice_phrases'][1].update(start_beat=25), 'Overlapping voice phrases'),
]:
    candidate = copy.deepcopy(source)
    mutation(candidate)
    try:
        make_score(candidate)
    except AssertionError as exc:
        assert error in str(exc), (label, exc)
    else:
        raise AssertionError(f'Accepted {label}')
    print(f'PASS: {label} rejected')

# These values are calculated independently for selected phrase beginnings
# and middles, including their written staff dynamic and global hairpin.
for beat, expected in [(27,56),(28.5,58),(34,60),(35.5,54),(41,52),(48,47)]:
    event = next(e for e in piece['events'] if e.get('voice') == 'tenor' and e['offset'] == beat)
    assert event['velocity'] == expected, (beat, event['velocity'], expected)
print('PASS: six independently calculated tenor phrase velocities')
