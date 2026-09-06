"""Explicit notation for equal eighth-note tuplets within a single bar."""
import xml.etree.ElementTree as ET


def apply_tuplet_spans(root, events, piece):
    notes = {n.get('id'): n for n in root.findall('.//part/measure/note') if n.get('id')}
    used = set()
    numbers_by_bar = {}
    spans = piece.get('tuplet_spans', [])
    for number, spec in enumerate(spans, 1):
        start, end = spec['start_beat'], spec['end_beat']
        count, normal = spec['actual'], spec['normal']
        group = sorted((e for e in events if e['hand'] == spec['hand']
                        and (not spec.get('voice') or e.get('voice') == spec['voice'])
                        and start <= e['offset'] < end - 1e-8), key=lambda e: e['offset'])
        assert len(group) == count and len({e['bar'] for e in group}) == 1
        if len(spans) > 6:
            # The score importer accepts bracket numbers 1–6. These groups
            # stay within one bar; reserve a number for the whole bar because
            # MusicXML serialises staves and voices in separate runs.
            bar_numbers = numbers_by_bar.setdefault(group[0]['bar'], set())
            available = set(range(1, 7)) - bar_numbers
            assert available, ('More than six explicit tuplet groups in one bar', piece['op'], group[0]['bar'])
            number = min(available)
            bar_numbers.add(number)
        assert abs(end - start - normal * .5) < 1e-8
        direction = spec.get('stem', 'down')
        assert direction in ('up', 'down')
        show_number = spec.get('show_number', 'actual')
        assert show_number in ('actual', 'both')
        placement = spec.get('placement', 'above')
        assert placement in ('above', 'below')
        for i, event in enumerate(group):
            assert event['id'] not in used and len(event['pitches']) == 1
            used.add(event['id'])
            assert abs(event['offset'] - start - i * (end-start) / count) < 1e-8
            assert abs(event['duration'] - (end-start) / count) < 1e-8
            n = notes[event['id']]
            assert n.findtext('type') == 'eighth' and n.find('tie') is None
            tm = n.find('time-modification')
            assert int(tm.findtext('actual-notes')) == count
            if int(tm.findtext('normal-notes')) != normal:
                # music21 spells 3/7 beats as dotted eighths at 7:4.
                # Undotted eighths at 7:6 have the same sounding duration.
                assert (count, normal, int(tm.findtext('normal-notes'))) == (7, 6, 4)
                assert len(n.findall('dot')) == len(tm.findall('normal-dot')) == 1
                n.remove(n.find('dot'))
                tm.remove(tm.find('normal-dot'))
                tm.find('normal-notes').text = str(normal)
            assert int(tm.findtext('normal-notes')) == normal
            assert n.find('dot') is None and tm.find('normal-dot') is None
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
                              bracket='yes', placement=placement, **{'show-number': show_number})
            if i == count-1:
                ET.SubElement(notation, 'tuplet', type='stop', number=str(number))
