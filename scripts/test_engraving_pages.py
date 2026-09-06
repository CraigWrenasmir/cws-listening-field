"""Verify that a shorter score removes only obsolete generated SVG pages."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
piece = next(p for p in json.loads((ROOT / 'data/catalog.json').read_text()) if p['op'] == 103)
with tempfile.TemporaryDirectory(prefix='engraving-page-check-', dir=ROOT / 'work') as folder:
    fixture = Path(folder)
    for name in ('scripts', 'data', 'pieces', 'work'):
        (fixture / name).mkdir()
    shutil.copy2(ROOT / 'scripts/engrave.py', fixture / 'scripts/engrave.py')
    (fixture / 'data/catalog.json').write_text(json.dumps([piece]))
    target = fixture / 'pieces' / piece['folder']
    shutil.copytree(ROOT / 'pieces' / piece['folder'], target)
    for index in (3, 99):
        (target / f'{piece["stem"]}_page_{index}.svg').write_text('<svg>obsolete generated page</svg>')
    unrelated = target / 'composer-notes.svg'
    unrelated.write_text('<svg>unrelated document</svg>')
    result = subprocess.run([sys.executable, str(fixture / 'scripts/engrave.py'), '--opus', '103'], capture_output=True, text=True)
    assert result.returncode == 0, (result.stdout, result.stderr)
    expected = {f'{piece["stem"]}_page_1.svg', f'{piece["stem"]}_page_2.svg'}
    assert {p.name for p in target.glob(piece['stem'] + '_page_*.svg')} == expected
    assert len(PdfReader(target / (piece['stem'] + '.pdf')).pages) == 2
    assert unrelated.read_text() == '<svg>unrelated document</svg>'
    print('PASS: a real two-page re-engraving removes stale numbered pages and preserves an unrelated SVG')
