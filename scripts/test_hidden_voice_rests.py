"""Check additional-voice rests against an actual three-voice score."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OPUS = 99
catalogue = json.loads((ROOT / 'data/catalog.json').read_text())
piece = next(p for p in catalogue if p['op'] == OPUS)

with tempfile.TemporaryDirectory(prefix='hidden-voice-check-', dir=ROOT / 'work') as folder:
    fixture = Path(folder)
    for name in ('scripts', 'data', 'pieces', 'work'):
        (fixture / name).mkdir()
    for name in ('validate.py', 'meter_plan.py'):
        shutil.copy2(ROOT / 'scripts' / name, fixture / 'scripts' / name)
    shutil.copytree(ROOT / 'pieces' / piece['folder'], fixture / 'pieces' / piece['folder'])
    (fixture / 'data/catalog.json').write_text(json.dumps(catalogue))
    score_path = fixture / 'pieces' / piece['folder'] / (piece['stem'] + '.musicxml')
    original = score_path.read_bytes()

    def run_case(name, mutation=None, expected_error=None):
        score_path.write_bytes(original)
        if mutation:
            tree = ET.parse(score_path)
            rest = tree.getroot().find('.//note[@id="cws99-lh-m15-n1001"]')
            mutation(rest)
            tree.write(score_path, encoding='utf-8', xml_declaration=True)
        result = subprocess.run(
            [sys.executable, str(fixture / 'scripts/validate.py'), '--opus', str(OPUS)],
            capture_output=True, text=True,
        )
        if expected_error:
            assert result.returncode != 0 and expected_error in result.stderr, (name, result.stdout, result.stderr)
        else:
            assert result.returncode == 0, (name, result.stdout, result.stderr)
        print(f'PASS: {name}')

    run_case('tenor rest uses the actual exported third voice')
    run_case('hidden rest reassigned to the bass is rejected',
             lambda n: setattr(n.find('voice'), 'text', '2'),
             'Hidden rest is not in its declared additional voice')
    run_case('hidden rest reassigned to the upper staff is rejected',
             lambda n: setattr(n.find('staff'), 'text', '1'),
             'Hidden rest is not on its declared staff')
