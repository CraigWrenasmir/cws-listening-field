"""Portable regression: python scripts/test-pedal-resonance.py.

Synthetic fixtures use TemporaryDirectory and the real composer/MIDI renderer.
The first FluidSynth call is intercepted after MIDI save: no soundfont, audio
tools, existing catalogue assets, private paths, Cairo or Poppler are needed.
"""
from copy import deepcopy
from io import BytesIO
from pathlib import Path
import json
import runpy
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

import mido
from compose import make_score, write_musicxml
from pedal_resonance import validate_pedal_resonance

SCRIPTS = Path(__file__).resolve().parent
FIELD = 'pedal_resonance_windows'


def fixture():
    return dict(
        op=9991, title='Pedal regression', key='C', fifths=0,
        bpm=60, bars=4, meter='4/4', final_fermata=False,
        rh='E5:4\nR:4\nE5:4\nE5:4',
        lh='C3:4\nR:4\nC3:4\nC3:4',
        sections={1: 'p'}, words={}, slurs=[], lower_phrases=[], hairpins=[],
        tempo_changes={}, group=4, system_starts=[1], pedal_spans=[[3, 8]],
        pedal_resonance_windows=[[4, 8]],
        performance=dict(rubato=[60] * 4, gate=.97, phrase_arcs=[], lower_entries=[]),
    )


def absolute_messages(midi):
    for number, track in enumerate(midi.tracks):
        tick = 0
        for message in track:
            tick += message.time
            yield number, tick, message


def midi_bytes(midi):
    out = BytesIO()
    midi.save(file=out)
    return out.getvalue()


def change_midi(midi, change, pedal_first=False):
    """Alter actual exported messages while retaining absolute event times."""
    result = deepcopy(midi)
    for index, track in enumerate(result.tracks):
        tick = 0
        events = []
        for ordinal, message in enumerate(track):
            tick += message.time
            edited = change(index, tick, message.copy(time=0))
            if edited is None:
                continue
            when, msg = edited
            priority = -3
            if msg.type == 'control_change' and msg.control == 64:
                priority = (-2 if pedal_first else 2) if msg.value >= 64 else -1
            elif msg.type == 'note_off' or msg.type == 'note_on' and msg.velocity == 0:
                priority = 0
            elif msg.type == 'note_on':
                priority = 1
            elif msg.type == 'end_of_track':
                priority = 3
            events.append((when, priority, ordinal, msg))
        track.clear()
        previous = 0
        for when, _, _, message in sorted(events, key=lambda value: value[:3]):
            message.time = when - previous
            track.append(message)
            previous = when
    return result


def export(piece, root, check=True):
    """Exercise real MusicXML/MIDI export without proceeding into audio."""
    root.mkdir()
    for name in ('scripts', 'data', 'pieces'):
        (root / name).mkdir()
    shutil.copy2(SCRIPTS / 'render_audio.py', root / 'scripts/render_audio.py')
    piece = deepcopy(piece)
    score, piece['events'] = make_score(piece)
    piece.update(folder='fixture', stem='fixture')
    folder = root / 'pieces/fixture'
    folder.mkdir()
    xml_path = folder / 'fixture.musicxml'
    write_musicxml(score, piece, xml_path)
    (root / 'data/catalog.json').write_text(json.dumps([piece]))
    (root / 'data/library_style.json').write_text(json.dumps(dict(
        reverb=dict(room_size=.45, damp=.65, level=.23))))
    midi_path = folder / 'fixture.mid'

    class MidiSaved(Exception):
        pass

    def stop_audio(command, **kwargs):
        assert command[0] == 'fluidsynth'
        assert Path(command[-1]).resolve() == midi_path.resolve()
        assert midi_path.is_file(), 'Renderer did not save its real MIDI export'
        raise MidiSaved

    with patch.object(sys, 'argv', ['render_audio.py']), patch('subprocess.run', side_effect=stop_audio):
        try:
            runpy.run_path(str(root / 'scripts/render_audio.py'), run_name='__main__')
        except MidiSaved:
            pass
        else:
            raise AssertionError('Expected the exact audio-render boundary')
    midi = mido.MidiFile(midi_path)
    if check:
        validate_pedal_resonance(piece, midi)
    return piece, midi, ET.parse(xml_path).getroot()


class PedalResonance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        temporary = tempfile.TemporaryDirectory(prefix='cws-pedal-regression-')
        cls.addClassCleanup(temporary.cleanup)
        cls.root = Path(temporary.name)
        cls.piece, cls.midi, cls.xml = export(fixture(), cls.root / 'valid')

    def test_early_pickup_preserves_written_rests_and_real_midi_capture(self):
        self.assertEqual(validate_pedal_resonance(self.piece, self.midi), [[4, 8]])
        self.assertEqual(validate_pedal_resonance(json.loads(json.dumps(self.piece)), self.midi), [[4, 8]])
        rests = self.xml.findall('.//measure[@number="2"]/note')
        self.assertEqual({note.findtext('staff', '1') for note in rests}, {'1', '2'})
        self.assertTrue(all(note.find('rest') is not None for note in rests))
        self.assertEqual(self.midi.ticks_per_beat, 960)
        for channel in (0, 1):
            controls = [(tick, msg.value) for _, tick, msg in absolute_messages(self.midi)
                        if msg.type == 'control_change' and msg.control == 64 and msg.channel == channel]
            self.assertEqual(controls[:2], [(2880, 80), (7680, 0)])
            releases = [tick for _, tick, msg in absolute_messages(self.midi)
                        if msg.type == 'note_off' and msg.channel == channel and tick < 7680]
            self.assertEqual(releases, [3725])  # round(4 * .97 * 960), before written rest at 3840.
        self.assertFalse(any(3840 <= tick < 7680 and msg.type == 'note_on' and msg.velocity
                             for _, tick, msg in absolute_messages(self.midi)))

    def test_gate_shortening_rejects_late_and_same_tick_pickup(self):
        # Both starts precede the written rest; neither precedes the actual key release.
        for name, start in [('late-pickup', 3.95), ('same-tick-pickup', 3725 / 960)]:
            with self.subTest(fixture=name):
                source = fixture()
                source['pedal_spans'][0][0] = start
                piece, midi, _ = export(source, self.root / name, check=False)
                down = [tick for _, tick, msg in absolute_messages(midi)
                        if msg.type == 'control_change' and msg.control == 64 and msg.value >= 64]
                self.assertEqual(down, [round(start * 960)] * 2)
                if name == 'same-tick-pickup':
                    at_release = [msg.type for track, tick, msg in absolute_messages(midi)
                                  if track == 1 and tick == 3725]
                    self.assertEqual(at_release, ['note_off', 'control_change'])
                self.assertEqual(validate_pedal_resonance(piece), [[4, 8]])
                with self.assertRaises(ValueError):
                    validate_pedal_resonance(piece, midi)
        # Ordinary same-tick order above came from the real renderer. Reversing
        # its order must not turn the same tick into an earlier pedal capture.
        reordered = change_midi(midi, lambda tr, tick, msg: (tick, msg), pedal_first=True)
        with self.assertRaises(ValueError):
            validate_pedal_resonance(piece, reordered)

    def test_partial_rest_resonance_releases_before_the_next_attack(self):
        source = fixture()
        source['pedal_spans'] = [[3, 7]]
        source[FIELD] = [[4, 7]]
        piece, midi, xml = export(source, self.root / 'partial-rest-window')
        self.assertEqual(validate_pedal_resonance(piece, midi), [[4, 7]])
        marks, divisions = [], None
        for measure in xml.findall('.//part/measure'):
            cursor = 0
            bar_start = (int(measure.get('number')) - 1) * 4  # This fixture is fixed 4/4.
            for element in measure:
                if element.tag == 'attributes' and element.find('divisions') is not None:
                    divisions = int(element.findtext('divisions'))
                elif element.tag == 'backup':
                    cursor -= int(element.findtext('duration'))
                elif element.tag == 'forward':
                    cursor += int(element.findtext('duration'))
                elif element.tag == 'note' and element.find('chord') is None:
                    cursor += int(element.findtext('duration'))
                elif element.tag == 'direction' and element.find('direction-type/pedal') is not None:
                    pedal = element.find('direction-type/pedal')
                    beat = bar_start + (cursor + float(element.findtext('offset', '0'))) / divisions
                    marks.append((beat, pedal.get('type'), element.findtext('staff', '1')))
        self.assertEqual(marks, [(3., 'start', '2'), (7., 'stop', '2')])
        for channel in (0, 1):
            controls = [(tick, msg.value) for _, tick, msg in absolute_messages(midi)
                        if msg.type == 'control_change' and msg.control == 64 and msg.channel == channel]
            self.assertEqual(controls[:2], [(2880, 80), (6720, 0)])
        self.assertFalse(any(6720 <= tick < 7680 and msg.type == 'note_on' and msg.velocity
                             for _, tick, msg in absolute_messages(midi)))
        late_lift = change_midi(midi, lambda tr, tick, msg:
            (7200 if tick == 6720 and msg.type == 'control_change' and msg.control == 64 else tick, msg))
        with self.assertRaises(ValueError):
            validate_pedal_resonance(piece, late_lift)

    def test_mixed_metre_boundaries_and_sub_tick_resonance_window(self):
        source = fixture()
        source.update(meter='5/8', meters=['5/8', '3/8', '4/4', '4/4'],
                      rh='E5:2.5\nR:1.5\nE5:4\nE5:4',
                      lh='C3:2.5\nR:1.5\nC3:4\nC3:4',
                      pedal_spans=[[2, 4]], pedal_resonance_windows=[[2.5, 4]])
        piece, midi, _ = export(source, self.root / 'mixed-metre-rest')
        self.assertEqual(validate_pedal_resonance(piece, midi), [[2.5, 4]])
        metres = [(tick, msg.numerator, msg.denominator) for _, tick, msg in absolute_messages(midi)
                  if msg.type == 'time_signature']
        self.assertEqual(metres, [(0, 5, 8), (2400, 3, 8), (3840, 4, 4)])
        self.assertFalse(any(2400 <= tick < 3840 and msg.type == 'note_on' and msg.velocity
                             for _, tick, msg in absolute_messages(midi)))
        tiny = fixture()
        tiny['pedal_spans'] = [[3, 4.00025]]
        tiny[FIELD] = [[4, 4.00025]]
        piece, midi, _ = export(tiny, self.root / 'sub-tick-window', check=False)
        self.assertEqual(validate_pedal_resonance(piece), [[4, 4.00025]])
        self.assertEqual(round(4 * midi.ticks_per_beat), round(4.00025 * midi.ticks_per_beat))
        with self.assertRaises(ValueError):
            validate_pedal_resonance(piece, midi)

    def test_window_coverage_rejects_stale_overbroad_fake_and_duplicate_declarations(self):
        for windows in ([[4, 7]], [[3, 8]], [[8, 9]], [[4, 8], [9, 10]], [[4, 8], [4, 8]]):
            with self.subTest(windows=windows):
                piece = deepcopy(self.piece)
                piece[FIELD] = windows
                with self.assertRaises(ValueError):
                    validate_pedal_resonance(piece)
        piece = deepcopy(self.piece)
        piece['pedal_spans'] = [[3, 7]]
        with self.assertRaises(ValueError):
            validate_pedal_resonance(piece)

    def test_initial_rest_has_no_capture_and_trailing_rest_needs_exact_coverage(self):
        initial = fixture()
        initial['rh'] = 'R:4\nE5:4\nE5:4\nE5:4'
        initial['lh'] = 'R:4\nC3:4\nC3:4\nC3:4'
        initial['pedal_spans'] = [[0, 4]]
        initial[FIELD] = [[0, 4]]
        with self.assertRaises(ValueError):
            export(initial, self.root / 'initial-without-capture')
        trailing = fixture()
        trailing['rh'] = 'E5:4\nR:4\nE5:4\nR:4'
        trailing['lh'] = 'C3:4\nR:4\nC3:4\nR:4'
        trailing['pedal_spans'] = [[3, 8], [11, 16]]
        trailing[FIELD] = [[4, 8], [12, 16]]
        piece, midi, _ = export(trailing, self.root / 'trailing-valid')
        self.assertEqual(validate_pedal_resonance(piece, midi), [[4, 8], [12, 16]])
        piece[FIELD] = [[4, 8]]
        with self.assertRaises(ValueError):
            validate_pedal_resonance(piece)
        dry = deepcopy(trailing)
        dry['pedal_spans'] = [[3, 8]]
        dry[FIELD] = [[4, 8]]
        piece, midi, _ = export(dry, self.root / 'trailing-dry')
        self.assertEqual(validate_pedal_resonance(piece, midi), [[4, 8]])
        # Carrying pedal through the next attack must not contaminate the later
        # undeclared shared rest, even though that rest has no note attacks.
        wrong = change_midi(midi, lambda tr, tick, msg:
            (12480 if tick == 7680 and msg.type == 'control_change' and msg.control == 64 else tick, msg))
        with self.assertRaises(ValueError):
            validate_pedal_resonance(piece, wrong)

    def test_additional_tied_voice_prevents_a_shared_written_rest(self):
        piece = fixture()
        piece['rh_inner'] = 'C5:4~\nC5:4\nR:4\nR:4'
        with self.assertRaises(ValueError):
            export(piece, self.root / 'tied-inner-voice')
        # Validate against an explicit held source event as well as tied-source export.
        piece = deepcopy(self.piece)
        piece['events'].append(dict(id='held-inner', hand='rh', voice='inner', bar=1,
                                    offset=0, duration=8, pitches=[72], spellings=['C5']))
        with self.assertRaises(ValueError):
            validate_pedal_resonance(piece)

    def test_wrong_midi_keys_capture_and_control_states_are_rejected(self):
        cases = {
            'missing-left-pedal': lambda tr, tick, msg: None if msg.type == 'control_change' and msg.control == 64 and msg.channel == 1 else (tick, msg),
            'early-pedal-release': lambda tr, tick, msg: (7200 if tick == 7680 and msg.type == 'control_change' and msg.control == 64 else tick, msg),
            'late-pedal-release': lambda tr, tick, msg: (8160 if tick == 7680 and msg.type == 'control_change' and msg.control == 64 else tick, msg),
            'key-held-into-rest': lambda tr, tick, msg: (4000 if tick == 3725 and msg.type == 'note_off' else tick, msg),
            'wrong-pitch': lambda tr, tick, msg: (tick, msg.copy(note=msg.note + 1)) if tick == 0 and msg.type == 'note_on' else (tick, msg),
            'wrong-hand-channel': lambda tr, tick, msg: (tick, msg.copy(channel=1)) if tick == 0 and msg.type == 'note_on' and msg.channel == 0 else (tick, msg),
            'missing-note-off': lambda tr, tick, msg: None if tick == 3725 and msg.type == 'note_off' else (tick, msg),
        }
        for name, change in cases.items():
            with self.subTest(case=name), self.assertRaises(ValueError):
                validate_pedal_resonance(self.piece, change_midi(self.midi, change))

    def test_invalid_metadata_and_missing_explicit_pedal_spans(self):
        values = [False, 0, {}, '', [4, 8], [[4]], [[4, 8, 9]], [[-1, 8]],
                  [[4, 17]], [[4, 4]], [[8, 4]], [[True, 8]],
                  [[float('nan'), 8]], [[4, float('inf')]]]
        for value in values:
            with self.subTest(value=value):
                piece = deepcopy(self.piece)
                piece[FIELD] = value
                with self.assertRaises(ValueError):
                    validate_pedal_resonance(piece)
        for spans in (None, []):
            piece = deepcopy(self.piece)
            if spans is None:
                piece.pop('pedal_spans')
            else:
                piece['pedal_spans'] = spans
            with self.subTest(spans=spans), self.assertRaises(ValueError):
                validate_pedal_resonance(piece)

    def test_no_opt_in_is_a_no_op_and_preserves_actual_midi_bytes(self):
        for value in (None, [], ()):
            piece = deepcopy(self.piece)
            piece[FIELD] = value
            self.assertEqual(validate_pedal_resonance(piece, self.midi), [])
        piece = deepcopy(self.piece)
        piece.pop(FIELD)
        self.assertEqual(validate_pedal_resonance(piece, self.midi), [])
        legacy = fixture()
        legacy.pop(FIELD)
        _, midi, xml = export(legacy, self.root / 'legacy-no-opt-in')
        self.assertEqual(midi_bytes(midi), midi_bytes(self.midi))
        self.assertEqual(len(xml.findall('.//direction-type/pedal')), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
