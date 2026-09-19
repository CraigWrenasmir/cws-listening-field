"""Optional, shared tempo discontinuities at notated bar boundaries."""
from bisect import bisect_right
from collections.abc import Mapping
from fractions import Fraction
import math
from numbers import Real

import numpy as np

from meter_plan import bar_plan


def _number(value, label):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f'{label} must be a positive finite number')
    result = float(value)
    if not math.isfinite(result) or result <= 0:
        raise ValueError(f'{label} must be a positive finite number')
    return result


def normalise_tempo_pivots(piece, count=None):
    """Validate opt-in metadata; absent metadata leaves historical pieces alone.

    BPM is always quarter notes per minute. Beat referents are exact lengths in
    quarter units. Only quarter and dotted-quarter numeric marks are supported.
    """
    raw = piece.get('tempo_pivots')
    if raw is None:
        return {}
    if not isinstance(raw, Mapping):
        raise ValueError('tempo_pivots must be a map of destination bars')
    if not raw:
        return {}
    count = piece.get('bars') if count is None else count
    if not isinstance(count, int) or isinstance(count, bool) or count < 2:
        raise ValueError('tempo_pivots require at least two bars')
    performance = piece.get('performance')
    if not isinstance(performance, Mapping):
        raise ValueError('tempo_pivots require the shared performance tempo map')
    rubato = performance.get('rubato')
    if not isinstance(rubato, (list, tuple)) or len(rubato) != count:
        raise ValueError('tempo_pivots require one rubato tempo per bar')
    rates = [_number(value, 'rubato tempo') for value in rubato]
    if _number(piece['bpm'], 'opening BPM') != rates[0]:
        raise ValueError('Opening printed BPM must match the performed tempo')
    _, lengths, _, _ = bar_plan(piece, count)
    result = {}
    for key, mark in raw.items():
        if isinstance(key, bool) or not (isinstance(key, int) or isinstance(key, str) and key.isdigit()):
            raise ValueError('Tempo pivot bars must be integers or JSON integer keys')
        number = int(key)
        if number in result:
            raise ValueError('Duplicate normalised tempo pivot bar')
        if not 2 <= number <= count:
            raise ValueError('Tempo pivot must begin a destination bar after bar 1')
        if not isinstance(mark, Mapping) or set(mark) != {'bpm', 'previous_beat', 'new_beat'}:
            raise ValueError('A tempo pivot needs bpm, previous_beat and new_beat')
        bpm = _number(mark['bpm'], 'pivot BPM')
        if bpm != rates[number - 1]:
            raise ValueError('Pivot BPM disagrees with its rubato destination')
        beats = []
        for field in ('previous_beat', 'new_beat'):
            try:
                if isinstance(mark[field], bool):
                    raise ValueError
                value = Fraction(str(mark[field]))
            except (ValueError, ZeroDivisionError, TypeError):
                raise ValueError('Pivot referents must be quarter or dotted-quarter lengths') from None
            if value not in (Fraction(1), Fraction(3, 2)):
                raise ValueError('Only quarter and dotted-quarter pivot referents are supported')
            beats.append(value)
        if beats[0] / Fraction(str(rates[number - 2])) != beats[1] / Fraction(str(bpm)):
            raise ValueError('Tempo pivot does not preserve its declared beat relation')
        if beats[0] > lengths[number - 2] or beats[1] > lengths[number - 1]:
            raise ValueError('Pivot referents must fit the adjacent bars')
        if number == count and piece.get('final_fermata', True):
            raise ValueError('Final fermata would alter the declared pivot BPM')
        result[number] = dict(bpm=bpm, previous_beat=str(beats[0]), new_beat=str(beats[1]))
    return dict(sorted(result.items()))


def performance_tempo_at(beat, bar_starts, bar_bpms, pivots):
    """Preserve old interpolation except in the bar before an explicit jump."""
    if pivots:
        index = bisect_right(bar_starts, beat) - 1
        if index + 2 in pivots:
            return float(bar_bpms[index])
    return float(np.interp(beat, bar_starts, bar_bpms))


def validate_tempo_pivots(piece, midi, xml_root):
    """Independently check declared boundaries in the exported MIDI and score."""
    pivots = normalise_tempo_pivots(piece)
    if not pivots:
        return
    import mido

    _, _, starts, _ = bar_plan(piece)
    ticks_per_beat = midi.ticks_per_beat
    actual = []
    for track_number, track in enumerate(midi.tracks):
        tick = 0
        for message in track:
            tick += message.time
            if message.type == 'set_tempo':
                assert track_number == 0, 'Pivot tempi must use one shared conductor track'
                actual.append((tick, message.tempo))
    assert actual and actual[0][0] == 0, 'Missing initial shared tempo'
    for number, mark in pivots.items():
        boundary = round(starts[number - 1] * ticks_per_beat)
        previous = round(starts[number - 2] * ticks_per_beat)
        old_tempo = mido.bpm2tempo(piece['performance']['rubato'][number - 2])
        new_tempo = mido.bpm2tempo(mark['bpm'])
        before = [event for event in actual if event[0] <= previous]
        assert before and before[-1][1] == old_tempo, ('Wrong pre-pivot tempo', number)
        assert all(value == old_tempo for tick, value in actual if previous <= tick < boundary), ('Tempo interpolates before pivot', number)
        assert [value for tick, value in actual if tick == boundary] == [new_tempo], ('Wrong or duplicated pivot tempo', number)
    recorded = [(round(mark['beat'] * ticks_per_beat), mark['microseconds']) for mark in piece['tempo_map']]
    assert recorded == actual, 'Catalogue tempo map differs from the MIDI conductor'
    compound = piece['meter'] in ('6/8', '9/8', '12/8')
    expected = {1: (Fraction(3, 2) if compound else Fraction(1), float(piece['bpm']))}
    expected.update({number: (Fraction(mark['new_beat']), mark['bpm']) for number, mark in pivots.items()})
    printed = []
    for measure in xml_root.findall('.//part/measure'):
        for direction in measure.findall('direction'):
            for mark in direction.findall('direction-type/metronome'):
                assert float(direction.findtext('offset', '0')) == 0, 'Tempo mark is not at the bar start'
                assert direction.findtext('staff', '1') == '1', 'Tempo mark is not on the upper staff'
                assert mark.findtext('beat-unit') == 'quarter', 'Unsupported printed tempo referent'
                dots = len(mark.findall('beat-unit-dot'))
                assert dots in (0, 1), 'Unsupported printed tempo dots'
                beat = Fraction(3, 2) if dots else Fraction(1)
                qpm = float(mark.findtext('per-minute')) * float(beat)
                sound = direction.find('sound')
                assert sound is not None and math.isclose(float(sound.get('tempo')), qpm, rel_tol=1e-12, abs_tol=1e-9), 'Printed and MusicXML sound tempi differ'
                printed.append((int(measure.get('number')), beat, qpm))
    printed.sort()
    wanted = [(number, *values) for number, values in sorted(expected.items())]
    assert len(printed) == len(wanted) and all(
        actual[:2] == declared[:2] and math.isclose(actual[2], declared[2], rel_tol=1e-12, abs_tol=1e-9)
        for actual, declared in zip(printed, wanted)
    ), 'Printed tempo marks differ from declared pivots'
