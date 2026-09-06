"""Exercise exact elevenths and scoped MusicXML precision on real scores."""
from fractions import Fraction
from pathlib import Path
import tempfile
import xml.etree.ElementTree as ET

from music21 import defaults
from compose import PIECES, ROOT, make_score, write_musicxml

previous = defaults.divisionsPerQuarter
assert previous == 10080
for piece in PIECES:
    if piece['op'] <= 101:
        for voice in ('rh', 'rh_inner', 'lh', 'lh_upper'):
            for token in piece.get(voice, '').split():
                assert previous % Fraction(token.split(':')[1].rstrip('~')).denominator == 0
print('PASS: all Op. 1–101 written durations retain their existing precision')

with tempfile.TemporaryDirectory(prefix='xml-precision-', dir=ROOT / 'work') as folder:
    path = Path(folder) / 'score.musicxml'
    piece = next(p for p in PIECES if p['op'] == 102)
    score, _ = make_score(piece)
    write_musicxml(score, piece, path)
    assert defaults.divisionsPerQuarter == previous
    root = ET.parse(path).getroot()
    assert {int(n.text) for n in root.findall('.//divisions')} == {110880}
    for bar in (6, 14):
        measure = root.find(f'.//measure[@number="{bar}"]')
        notes = [n for n in measure.findall('note') if n.findtext('time-modification/actual-notes') == '11']
        assert len(notes) == 11
        assert all(int(n.findtext('duration')) == 40320 for n in notes)
        assert sum(int(n.findtext('duration')) for n in notes) == 4 * 110880
    print('PASS: both eleven-note groups fill exactly four beats in the exported score')

    ordinary = next(p for p in PIECES if p['op'] == 97)
    score, _ = make_score(ordinary)
    write_musicxml(score, ordinary, path)
    assert defaults.divisionsPerQuarter == previous
    assert {int(n.text) for n in ET.parse(path).getroot().findall('.//divisions')} == {10080}
    print('PASS: a following quintuplet score returns to its original precision')

    class InterruptedExport:
        def write(self, *args, **kwargs):
            assert defaults.divisionsPerQuarter == 110880
            raise RuntimeError('fixture export interruption')

    try:
        write_musicxml(InterruptedExport(), piece, path)
    except RuntimeError as error:
        assert str(error) == 'fixture export interruption'
    else:
        raise AssertionError('The export interruption was swallowed')
    assert defaults.divisionsPerQuarter == previous
    print('PASS: precision is restored after an interrupted export')
