"""Explicit notation for equal eighth-note tuplets within a single bar."""
import xml.etree.ElementTree as ET


def apply_tuplet_spans(root, events, piece):
    notes = {n.get('id'): n for n in root.findall('.//part/measure/note') if n.get('id')}
    used = set()
    for number, spec in enumerate(piece.get('tuplet_spans', []), 1):
        start, end = spec['start_beat'], spec['end_beat']
        count, normal = spec['actual'], spec['normal']
        group = sorted((e for e in events if e['hand'] == spec['hand']
                        and (not spec.get('voice') or e.get('voice') == spec['voice'])
                        and start <= e['offset'] < end - 1e-8), key=lambda e: e['offset'])
        assert len(group) == count and len({e['bar'] for e in group}) == 1
        assert abs(end - start - normal * .5) < 1e-8
        direction = spec.get('stem', 'down')
        assert direction in ('up', 'down')
        for i, event in enumerate(group):
            assert event['id'] not in used and len(event['pitches']) == 1
            used.add(event['id'])
            assert abs(event['offset'] - start - i * (end-start) / count) < 1e-8
            assert abs(event['duration'] - (end-start) / count) < 1e-8
            n = notes[event['id']]
            assert n.findtext('type') == 'eighth' and n.find('tie') is None
            tm = n.find('time-modification')
            assert int(tm.findtext('actual-notes')) == count
            assert int(tm.findtext('normal-notes')) == normal
            # music21 can infer a 128th-note normal-type for 4/9 quarter beats.
            # This span explicitly represents nine eighths in the time of eight.
            nt = tm.find('normal-type')
            if nt is None: nt = ET.SubElement(tm, 'normal-type')
            nt.text = 'eighth'
            stem = n.find('stem')
            if stem is None:
                stem = ET.Element('stem')
                before = next((x for x in n if x.tag in ('staff', 'beam', 'notations')), None)
                n.insert(list(n).index(before) if before is not None else len(n), stem)
            stem.text = direction
            for beam in n.findall('beam'): n.remove(beam)
            notation = n.find('notations')
            if notation is None: notation = ET.SubElement(n, 'notations')
            for tuplet in notation.findall('tuplet'): notation.remove(tuplet)
            beam = ET.Element('beam', number='1')
            beam.text = 'begin' if i == 0 else 'end' if i == count-1 else 'continue'
            n.insert(list(n).index(notation), beam)
            if i == 0:
                ET.SubElement(notation, 'tuplet', type='start', number=str(number),
                              bracket='yes', placement='above', **{'show-number': 'actual'})
            if i == count-1:
                ET.SubElement(notation, 'tuplet', type='stop', number=str(number))
