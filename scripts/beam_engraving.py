"""Explicit short beam groups for equal, untied single notes."""


def apply_beam_spans(root, events, piece):
    notes = {n.get('id'): n for n in root.findall('.//part/measure/note') if n.get('id')}
    planned = []
    used = set()
    values = {'eighth': (.5, 1), '16th': (.25, 2), '32nd': (.125, 3)}
    for spec in piece.get('beam_spans', []):
        start, end = spec['start_beat'], spec['end_beat']
        step, levels = values[spec['note_type']]
        assert spec['stem'] in ('up', 'down')
        group = sorted((e for e in events if e['hand'] == spec['hand']
                        and (not spec.get('voice') or e.get('voice') == spec['voice'])
                        and start <= e['offset'] < end - 1e-8), key=lambda e: e['offset'])
        assert len(group) >= 2 and len({e['bar'] for e in group}) == 1
        assert abs(end - start - len(group) * step) < 1e-8
        for i, event in enumerate(group):
            assert event['id'] not in used and len(event['pitches']) == 1
            used.add(event['id'])
            assert abs(event['offset'] - start - i * step) < 1e-8
            assert abs(event['duration'] - step) < 1e-8
            n = notes[event['id']]
            assert n.findtext('type') == spec['note_type'] and n.find('tie') is None
            assert n.find('dot') is None and n.find('time-modification') is None
            assert n.find('stem') is not None
            assert [b.get('number') for b in n.findall('beam')] == [str(i+1) for i in range(levels)]
        planned.append((spec, group))
    # Cover each original beam completely so an edited boundary cannot strand a neighbour.
    for spec, group in planned:
        for event in group:
            line = sorted((e for e in events if e['hand'] == event['hand'] and e['bar'] == event['bar']
                           and e.get('voice') == event.get('voice')), key=lambda e: e['offset'])
            index = next(i for i, e in enumerate(line) if e['id'] == event['id'])
            mark = notes[event['id']].findtext('beam')
            if mark != 'begin': assert index > 0 and line[index-1]['id'] in used
            if mark != 'end': assert index+1 < len(line) and line[index+1]['id'] in used
    for spec, group in planned:
        for i, event in enumerate(group):
            n = notes[event['id']]
            n.find('stem').text = spec['stem']
            for beam in n.findall('beam'):
                beam.text = 'begin' if i == 0 else 'end' if i == len(group)-1 else 'continue'
