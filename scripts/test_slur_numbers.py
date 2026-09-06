"""Check overlapping slurs using the real four-voice Op. 114 score."""
import copy
from pathlib import Path
import tempfile
import xml.etree.ElementTree as ET

from compose import PIECES, make_score, write_musicxml
from slur_engraving import normalise_slur_numbers

ROOT = Path(__file__).resolve().parents[1]
piece = next(p for p in PIECES if p['op'] == 114)
score, events = make_score(piece)
with tempfile.TemporaryDirectory(prefix='slur-numbers-', dir=ROOT / 'work') as folder:
    path = Path(folder) / 'source.musicxml'
    write_musicxml(score, piece, path)
    raw = ET.parse(path).getroot()

def mark(root, ident, kind):
    return root.find(f'.//note[@id="{ident}"]/notations/slur[@type="{kind}"]')

# Deliberately reproduce reuse between two simultaneously sounding RH voices.
for ident, kind in [('cws114-rh-m1-n1','start'),('cws114-rh-m2-n2','stop'),
                    ('cws114-rh-m1-n1002','start'),('cws114-rh-m2-n1003','stop')]:
    mark(raw, ident, kind).set('number', '1')
fixed = copy.deepcopy(raw)
normalise_slur_numbers(fixed, events)
opened = {}
pairs = set()
for n in fixed.findall('.//part/measure/note'):
    for slur in n.findall('notations/slur'):
        number = slur.get('number')
        assert 1 <= int(number) <= 16
        if slur.get('type') == 'start':
            assert number not in opened
            opened[number] = n.get('id')
        else:
            assert number in opened
            pairs.add((opened.pop(number), n.get('id')))
assert not opened and len(pairs) == 16
assert {
    ('cws114-rh-m1-n1','cws114-rh-m2-n2'),
    ('cws114-rh-m1-n1002','cws114-rh-m2-n1003'),
    ('cws114-lh-m3-n2','cws114-lh-m4-n3'),
    ('cws114-lh-m3-n1001','cws114-lh-m4-n1002'),
} <= pairs
# Removing just the slur numbers must recover the entire original XML tree.
for tree in (raw, fixed):
    for slur in tree.findall('.//notations/slur'):
        slur.attrib.pop('number', None)
assert ET.tostring(raw) == ET.tostring(fixed)
print('PASS: sixteen phrase pairs, four known overlapping endpoints, and all other XML preserved')

broken = copy.deepcopy(raw)
note = broken.find('.//note[@id="cws114-rh-m1-n1002"]/notations')
note.remove(note.find('slur[@type="start"]'))
try:
    normalise_slur_numbers(broken, events)
except AssertionError as exc:
    assert 'Unmatched source slur endpoint' in str(exc), exc
else:
    raise AssertionError('Accepted an orphaned slur endpoint')
print('PASS: missing inner-voice start rejected')
