"""Opt-in proof of written finger-rests carried by ordinary sustain pedal.

All positions are absolute quarter-note beats. A declaration must cover exactly
the shared written rests intersecting explicit pedal spans. MIDI validation
proves key release and pedal capture, not acoustic loudness or waveform silence.
Pieces without a nonempty declaration retain their existing validation path.
"""
from collections import Counter
from math import isfinite
from numbers import Real

from meter_plan import bar_plan

EPSILON = 1e-8


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _number(value):
    return isinstance(value, Real) and not isinstance(value, bool) and isfinite(value)


def _spans(raw, total, name):
    _require(isinstance(raw, (list, tuple)), f'{name} must be a list of beat pairs')
    result = []
    for span in raw:
        _require(isinstance(span, (list, tuple)) and len(span) == 2
                 and all(_number(value) for value in span), f'Invalid {name} pair')
        start, end = map(float, span)
        _require(0 <= start < end <= total, f'{name} outside score or empty/reversed')
        _require(not result or start >= result[-1][1], f'{name} unordered or overlapping')
        result.append([start, end])
    return result


def _merge(spans):
    result = []
    for start, end in sorted(spans):
        if result and start <= result[-1][1] + EPSILON:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result


def _written_rests(piece, total):
    sounding = []
    for event in piece['events']:
        if not event['pitches']:
            continue
        start, duration = event['offset'], event['duration']
        _require(_number(start) and _number(duration) and 0 <= start
                 and duration > 0 and start + duration <= total + EPSILON,
                 'Invalid sounding event in pedal-resonance score')
        sounding.append([float(start), min(total, float(start + duration))])
    rests, cursor = [], 0.
    for start, end in _merge(sounding):
        if start > cursor + EPSILON:
            rests.append([cursor, start])
        cursor = end
    if cursor < total - EPSILON:
        rests.append([cursor, total])
    return rests


def validate_pedal_resonance(piece, midi=None):
    """Return checked maximal windows; reject stale or unproved opt-in metadata.

    With MIDI, both hand channels must reproduce the explicit pedal spans and
    score attacks. During every shared written rest all keys must be released;
    a declared window requires a previously released note captured with CC64
    already down at an earlier tick. Other shared rests require pedal/capture
    release. Endpoints are half-open, with actual same-tick MIDI order retained.
    """
    raw = piece.get('pedal_resonance_windows')
    if raw is None:
        return []
    _require(isinstance(raw, (list, tuple)), 'pedal_resonance_windows must be a list')
    if not raw:
        return []
    total = float(bar_plan(piece)[3])
    windows = _spans(raw, total, 'pedal_resonance_windows')
    _require('pedal_spans' in piece, 'Resonance windows require explicit pedal_spans')
    pedal = _spans(piece['pedal_spans'], total, 'pedal_spans')
    rests = _written_rests(piece, total)
    expected = _merge([[max(a, c), min(b, d)] for a, b in rests for c, d in pedal
                       if min(b, d) > max(a, c) + EPSILON])
    _require(len(windows) == len(expected)
             and all(abs(a-c) <= EPSILON and abs(b-d) <= EPSILON
                     for (a, b), (c, d) in zip(windows, expected)),
             'Resonance windows must exactly cover shared written rest/pedal intersections')
    if midi is None:
        return windows

    tick = lambda beat: round(float(beat) * midi.ticks_per_beat)
    for start, end in windows + pedal:
        _require(tick(start) < tick(end), 'Pedal/resonance span vanishes at MIDI resolution')
    rest_ticks = [(tick(a), tick(b)) for a, b in rests if tick(a) < tick(b)]
    window_ticks = [(tick(a), tick(b)) for a, b in windows]
    expected_attacks = Counter((tick(event['offset']), 0 if event['hand'] == 'rh' else 1, pitch)
                               for event in piece['events'] for pitch in event['pitches'])
    messages, actual_attacks = {}, Counter()
    for track_number, track in enumerate(midi.tracks):
        position = 0
        for index, message in enumerate(track):
            position += message.time
            relevant = message.type in ('note_on', 'note_off') or (
                message.type == 'control_change' and message.control == 64)
            if relevant:
                _require(message.channel in (0, 1), 'Unexpected MIDI hand channel')
                messages.setdefault(position, []).append((track_number, index, message))
            if message.type == 'note_on' and message.velocity:
                actual_attacks[(position, message.channel, message.note)] += 1
    _require(actual_attacks == expected_attacks, 'Resonance MIDI attacks differ from score/hands')
    # Keep each track's exact message order; independent channels need no
    # synthetic note-off/pedal priority that could hide a same-tick pickup.
    marks = sorted({0, tick(total), *messages,
                    *(value for span in rest_ticks + window_ticks for value in span)})
    keys = [set(), set()]
    captured = [set(), set()]
    down = [None, None]
    actual_pedal = [[], []]
    for i, position in enumerate(marks):
        for _, _, message in sorted(messages.get(position, [])):
            channel = message.channel
            if message.type == 'control_change':
                if message.value >= 64 and down[channel] is None:
                    down[channel] = position
                elif message.value < 64:
                    if down[channel] is not None:
                        actual_pedal[channel].append((down[channel], position))
                    down[channel] = None
                    captured[channel].clear()
            elif message.type == 'note_on' and message.velocity:
                _require(message.note not in keys[channel], 'Duplicate held MIDI key')
                keys[channel].add(message.note)
                captured[channel].discard(message.note)
            else:
                _require(message.note in keys[channel], 'MIDI note-off has no held key')
                keys[channel].remove(message.note)
                if down[channel] is not None and down[channel] < position:
                    captured[channel].add(message.note)
        if position == tick(total):
            _require(not any(keys) and down == [None, None] and not any(captured),
                     'MIDI keys/pedal must release by score end')
        if i + 1 == len(marks) or not any(a <= position < b for a, b in rest_ticks):
            continue
        _require(not any(keys), f'MIDI key held inside shared written rest at tick {position}')
        if any(a <= position < b for a, b in window_ticks):
            _require(all(value is not None for value in down) and any(captured),
                     f'Resonance has no earlier MIDI pedal capture at tick {position}')
        else:
            _require(down == [None, None] and not any(captured),
                     f'MIDI pedal/capture covers undeclared shared rest at tick {position}')
    expected_pedal = [(tick(a), tick(b)) for a, b in pedal]
    _require(down == [None, None] and not any(keys), 'Unreleased MIDI keys/pedal')
    _require(all(spans == expected_pedal for spans in actual_pedal),
             'Resonance MIDI pedal spans differ from explicit spans on both hands')
    return windows
