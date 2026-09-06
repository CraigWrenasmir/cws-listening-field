"""Give overlapping phrases distinct MusicXML slur numbers across voices."""
import re


def normalise_slur_numbers(root, events):
    source = {e['id']: e for e in events}
    opened = {}
    pairs = []
    notes = [(int(measure.get('number')), note) for measure in root.findall('.//part/measure')
             for note in measure.findall('note')]
    for bar, note in notes:
        for mark in note.findall('notations/slur'):
            key = (note.findtext('staff', '1'), note.findtext('voice', '1'), mark.get('number', '1'))
            match = re.match(r'(cws\d+-(?:rh|lh)-m\d+-n\d+)', note.get('id', ''))
            assert match, ('Slur endpoint has no source event', note.get('id'))
            event = source[match[1]]
            kind = mark.get('type')
            assert kind in ('start', 'stop'), ('Unsupported slur mark', kind)
            if kind == 'start':
                assert key not in opened, ('Overlapping source slur number within one voice', key)
                opened[key] = (mark, event['offset'], bar)
            else:
                assert key in opened, ('Unmatched source slur endpoint', key, note.get('id'))
                beginning, start, start_bar = opened.pop(key)
                end = event['offset'] + event['duration']
                assert start < end
                # Reserve a number for the whole measures occupied. XML voices
                # are serialised in groups, so reuse within a bar can otherwise
                # put a new start before the previous voice's stop in the file.
                pairs.append((start_bar, bar, beginning, mark))
    assert not opened, ('Unclosed source slurs', list(opened))
    active = {}
    for start, end, beginning, ending in sorted(pairs, key=lambda p: (p[0], p[1])):
        active = {number: stop for number, stop in active.items() if stop >= start}
        number = next((n for n in range(1, 17) if n not in active), None)
        assert number is not None, 'Too many simultaneous slurs'
        active[number] = end
        beginning.set('number', str(number))
        ending.set('number', str(number))
