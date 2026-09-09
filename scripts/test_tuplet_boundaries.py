"""Dense consecutive triplets retain boundary notes and exact written timing."""
import collections
import copy
from pathlib import Path
import tempfile
import xml.etree.ElementTree as ET

from music21 import converter, note
from compose import PIECES, make_score, write_musicxml
from tuplet_engraving import apply_tuplet_spans

ROOT = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='triplet-boundaries-', dir=ROOT / 'work') as folder:
    path = Path(folder) / 'score.musicxml'
    for opus in (221, 120, 77):
        piece = next(p for p in PIECES if p['op'] == opus)
        score, events = make_score(piece)
        if opus == 221:
            # Three additions of one third do not always land on an exact integer.
            boundary = next(e for e in events if e['hand'] == 'lh' and e['bar'] == 1
                            and abs(e['offset'] - 2) < 1e-8)
            assert boundary['offset'] < 2
        write_musicxml(score, piece, path)
        raw = ET.parse(path).getroot()
        fixed = copy.deepcopy(raw)
        apply_tuplet_spans(fixed, events, piece)
        for spec in piece['tuplet_spans']:
            members = [e for e in events if e['hand'] == spec['hand']
                       and (not spec.get('voice') or e.get('voice') == spec['voice'])
                       and spec['start_beat'] - 1e-8 <= e['offset'] < spec['end_beat'] - 1e-8]
            assert len(members) == spec['actual']
            for event, kind in ((members[0], 'start'), (members[-1], 'stop')):
                assert fixed.find(f'.//note[@id="{event["id"]}"]/notations/tuplet[@type="{kind}"]') is not None
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
        if opus == 221:
            invalid = copy.deepcopy(piece)
            invalid['tuplet_spans'][0]['start_beat'] += 1/32
            try:
                apply_tuplet_spans(copy.deepcopy(raw), events, invalid)
            except AssertionError:
                pass
            else:
                raise AssertionError('A materially shifted boundary was accepted')
        print(f'PASS Op. {opus}: paired brackets, complete groups, exact score pitches/onsets')
