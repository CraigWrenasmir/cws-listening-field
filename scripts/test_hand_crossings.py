"""Exercise crossed-hand validation with a real score in an isolated copy."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
OPUS = 88
catalogue = json.loads((ROOT / 'data/catalog.json').read_text())
piece = next(p for p in catalogue if p['op'] == OPUS)
(ROOT / 'work').mkdir(exist_ok=True)

with tempfile.TemporaryDirectory(prefix='hand-crossing-check-', dir=ROOT / 'work') as folder:
    fixture = Path(folder)
    for name in ('scripts', 'data', 'pieces', 'work'):
        (fixture / name).mkdir()
    for name in ('validate.py', 'meter_plan.py'):
        shutil.copy2(ROOT / 'scripts' / name, fixture / 'scripts' / name)
    shutil.copytree(ROOT / 'pieces' / piece['folder'], fixture / 'pieces' / piece['folder'])

    def run_case(name, mutate=None, expected_error=None):
        data = deepcopy(catalogue)
        target = next(p for p in data if p['op'] == OPUS)
        if mutate:
            mutate(target)
        (fixture / 'data/catalog.json').write_text(json.dumps(data))
        result = subprocess.run(
            [sys.executable, str(fixture / 'scripts/validate.py'), '--opus', str(OPUS)],
            capture_output=True, text=True,
        )
        if expected_error:
            assert result.returncode != 0 and expected_error in result.stderr, (name, result.stdout, result.stderr)
        else:
            assert result.returncode == 0, (name, result.stdout, result.stderr)
        print(f'PASS: {name}')

    run_case('declared exchange, written rests and printed hand labels')
    def undeclare(p):
        p.pop('hand_crossings')
        p['technique_limits']['melodic_leap'] = 20

    run_case('undeclared reversed hand order is rejected', undeclare, 'Hand order')
    run_case('an occupied transition interval is rejected',
             lambda p: p['hand_crossings'][0].update(rest_before=2),
             'Hand-crossing transition needs written silence')
    run_case('a missing RH entry label is rejected',
             lambda p: p['hand_labels']['rh'].pop('7'),
             'Missing hand label at register exchange')

    def lower_regular_limit(p):
        p['technique_limits']['melodic_leap'] = 15
        p['hand_crossings'][0]['max_transition_leap'] = 99

    run_case('transition exceptions do not relax ordinary register moves',
             lower_regular_limit, 'cws88-lh-m11-n1')
