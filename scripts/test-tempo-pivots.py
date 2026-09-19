"""Portable regression: python scripts/test-tempo-pivots.py (pipeline Python deps).

All generated music/catalogue fixtures live in TemporaryDirectory. The real renderer saves MIDI;
its first FluidSynth call is intercepted, so no soundfont/audio tools are needed.
No catalogue, baseline snapshot, existing piece assets, Cairo or Poppler needed.
"""
from copy import deepcopy
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
import verovio
from compose import make_score, write_musicxml
from meter_plan import bar_plan
from tempo_pivots import normalise_tempo_pivots, validate_tempo_pivots
from tempo_engraving import MEI, SVG, imported_tempo_ids, render_pivot_tempo_glyphs

SCRIPTS = Path(__file__).resolve().parent


def fixture(mixed=False, pivot=True, fermata=False):
    first, length = ('5/8', '5/2') if mixed else ('6/8', '3')
    piece = dict(
        op=9990, title='Metric regression', key='C', fifths=0, bpm=90, bars=4,
        meter=first, meters=[first, '6/8', '3/4', '3/4'], final_fermata=fermata,
        rh=f'E5:{length}\nE5:3\nF5:1 E5:1 D5:1\nE5:3',
        lh=f'C3:{length}\nC3:3\nF3:1 C3:1 G3:1\nC3:3',
        rh_inner=f'R:{length}\nC5:3~\nC5:1 R:2\nR:3',
        sections={1:'p'}, words={}, slurs=[], lower_phrases=[], hairpins=[],
        tempo_changes={}, group=4, system_starts=[1], pedal_spans=[],
        performance=dict(rubato=[90,90,60,60], gate=1, phrase_arcs=[], lower_entries=[]),
    )
    if pivot:
        piece['tempo_pivots'] = {3:dict(bpm=60, previous_beat='3/2', new_beat='1')}
    return piece


def absolute_messages(midi):
    for number, track in enumerate(midi.tracks):
        tick = 0
        for message in track:
            tick += message.time
            yield number, tick, message


def tempo_map(midi):
    return [(tick, message.tempo) for track, tick, message in absolute_messages(midi)
            if message.type == 'set_tempo']


def seconds_at(midi, tick):
    marks = tempo_map(midi)
    return sum(max(0, min(tick, marks[i+1][0] if i+1 < len(marks) else tick)-start)
               * value / 1e6 / midi.ticks_per_beat for i, (start, value) in enumerate(marks))


def export(piece, root):
    """Exercise production MusicXML and MIDI exports with a synthetic catalogue."""
    root.mkdir()
    for name in ('scripts', 'data', 'pieces'): (root/name).mkdir()
    shutil.copy2(SCRIPTS/'render_audio.py', root/'scripts/render_audio.py')
    piece = deepcopy(piece)
    score, piece['events'] = make_score(piece)
    piece.update(folder='fixture', stem='fixture')
    folder = root/'pieces/fixture'; folder.mkdir()
    xml = folder/'fixture.musicxml'
    write_musicxml(score, piece, xml)
    (root/'data/catalog.json').write_text(json.dumps([piece]))
    (root/'data/library_style.json').write_text(json.dumps(dict(
        reverb=dict(room_size=.45, damp=.65, level=.23))))
    midi_path = folder/'fixture.mid'

    class MidiSaved(Exception): pass

    def stop_audio(command, **kwargs):
        assert command[0] == 'fluidsynth' and Path(command[-1]).resolve() == midi_path.resolve()
        assert midi_path.is_file(), 'Renderer did not save its real MIDI export'
        raise MidiSaved

    with patch.object(sys, 'argv', ['render_audio.py']), patch('subprocess.run', side_effect=stop_audio):
        try:
            runpy.run_path(str(root/'scripts/render_audio.py'), run_name='__main__')
        except MidiSaved:
            pass
        else:
            raise AssertionError('Expected to stop exactly at the audio-render boundary')
    midi = mido.MidiFile(midi_path)
    piece['tempo_map'] = [dict(beat=tick/midi.ticks_per_beat, microseconds=value)
                          for tick, value in tempo_map(midi)]
    return piece, midi, ET.parse(xml).getroot()


class MetricPivots(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        temporary = tempfile.TemporaryDirectory(prefix='cws-tempo-regression-')
        cls.addClassCleanup(temporary.cleanup)
        root = Path(temporary.name)
        legacy=fixture(pivot=False,fermata=True)
        legacy.pop('performance'); legacy['tempo_changes']={3:60}
        cls.exports = {name: export(piece, root/name) for name, piece in (
            ('pivot', fixture()), ('mixed', fixture(mixed=True)),
            ('default', fixture(pivot=False)), ('fermata', fixture(fermata=True)), ('legacy',legacy))}

    def test_abrupt_shared_midi_boundary_tie_and_equal_pulses(self):
        for name, boundary, previous in [('pivot',5760,2880), ('mixed',5280,2400)]:
            with self.subTest(fixture=name):
                piece, midi, xml = self.exports[name]
                validate_tempo_pivots(piece, midi, xml)
                self.assertEqual(midi.ticks_per_beat, 960)
                self.assertEqual(round(bar_plan(piece)[2][2]*960), boundary)
                self.assertEqual([value for tick,value in tempo_map(midi) if previous<=tick<boundary], [666667]*6)
                self.assertEqual([value for tick,value in tempo_map(midi) if tick==boundary], [1000000])
                self.assertTrue(all(track==0 for track,_,m in absolute_messages(midi) if m.type=='set_tempo'))
                attacks = [(track,m.note) for track,tick,m in absolute_messages(midi)
                           if tick==boundary and m.type=='note_on' and m.velocity]
                self.assertEqual(attacks, [(1,77),(2,53)])
                tied = [(tick,m.type) for track,tick,m in absolute_messages(midi)
                        if track==1 and m.type in ('note_on','note_off') and m.note==72]
                self.assertEqual(tied, [(previous,'note_on'),(boundary+960,'note_off')])
                old = seconds_at(midi,boundary)-seconds_at(midi,boundary-1440)
                new = seconds_at(midi,boundary+960)-seconds_at(midi,boundary)
                self.assertAlmostEqual(old,1.0000005,delta=1e-9)
                self.assertAlmostEqual(new,1.,delta=1e-9)
                self.assertLess(abs(old-new),1e-6)  # MIDI integer-tempo rounding only.

    def test_no_pivot_preserves_the_existing_interpolated_map(self):
        piece, midi, _ = self.exports['default']
        # Semantic expected ramp: the unmarked second bar approaches 60 from 90.
        rates = [90]*6 + [90,85,80,75,70,65] + [60]*12
        self.assertEqual(tempo_map(midi), [(i*480,mido.bpm2tempo(rate)) for i,rate in enumerate(rates)])
        self.assertEqual(normalise_tempo_pivots(piece), {})
        piece['tempo_pivots'] = {}
        self.assertEqual(normalise_tempo_pivots(piece), {})
        _,legacy,_=self.exports['legacy']
        self.assertEqual(tempo_map(legacy),[(i*2880,mido.bpm2tempo(rate))
                                          for i,rate in enumerate([90,90,60,67.5])])

    def test_fermata_changes_effective_destination_anchors(self):
        piece, midi, xml = self.exports['fermata']
        validate_tempo_pivots(piece,midi,xml)  # Nominal boundary contract still holds.
        self.assertEqual(piece['performance']['rubato'][2:], [60,60])
        self.assertEqual(dict(tempo_map(midi))[8640], mido.bpm2tempo(48))
        # The final fermata scales its anchor by .8, creating rubato after bar 3.
        self.assertAlmostEqual(seconds_at(midi,6720)-seconds_at(midi,5760),1.0172415,delta=1e-9)

    def test_invalid_metadata(self):
        cases = []
        for field, value in [('bpm',61),('bpm',0),('bpm',float('nan')),
                             ('previous_beat','1'),('new_beat','1/2'),('new_beat',True)]:
            piece=fixture(); piece['tempo_pivots'][3][field]=value; cases.append(piece)
        for bars in (1,5,True,'bad'):
            piece=fixture(); piece['tempo_pivots']={bars:piece['tempo_pivots'][3]}; cases.append(piece)
        piece=fixture(); piece['tempo_pivots']['3']=piece['tempo_pivots'][3]; cases.append(piece)
        piece=fixture(); piece['performance']['rubato']=[90,90,60]; cases.append(piece)
        piece=fixture(); piece['bpm']=91; cases.append(piece)
        piece=fixture(); piece.pop('performance'); cases.append(piece)
        piece=fixture(fermata=True); piece['tempo_pivots']={4:dict(bpm=60,previous_beat=1,new_beat=1)}; cases.append(piece)
        for index,piece in enumerate(cases):
            with self.subTest(case=index), self.assertRaises(ValueError): normalise_tempo_pivots(piece)

    def test_printed_referents_actual_mei_binding_and_svg_glyphs(self):
        piece, _, xml = self.exports['pivot']
        marks = []
        for measure in xml.findall('.//part/measure'):
            for direction in measure.findall('direction'):
                mark=direction.find('direction-type/metronome')
                if mark is not None:
                    marks.append((int(measure.get('number')),direction.get('id'),mark.findtext('beat-unit'),
                                  len(mark.findall('beat-unit-dot')),mark.findtext('per-minute'),
                                  direction.findtext('staff','1'),direction.find('sound').get('tempo')))
        self.assertEqual(marks, [(1,'cws9990-tempo-m1','quarter',1,'60','1','90'),
                                 (3,'cws9990-tempo-m3','quarter',0,'60','1','60')])
        toolkit=verovio.toolkit(); self.assertTrue(toolkit.loadData(ET.tostring(xml,encoding='unicode')))
        mei=toolkit.getMEI(); bound=imported_tempo_ids(mei,piece)
        self.assertEqual(set(bound.values()), {'cws9990-tempo-m1','cws9990-tempo-m3'})
        svg=ET.fromstring(toolkit.renderToSVG(1))
        glyph=Path(verovio.__file__).parent/'data/Leipzig/ECA5.xml'
        self.assertEqual(set(render_pivot_tempo_glyphs(svg,piece,glyph,bound)),set(bound.values()))
        ids=[element.get('id') for element in svg.iter() if element.get('id')]
        self.assertEqual(len(ids),len(set(ids)), 'Whole SVG must have unique element IDs')
        for group in svg.findall('.//'+SVG+'g[@class="tempo"]'):
            self.assertEqual(len(group.findall('.//'+SVG+'circle')),int(group.get('id').endswith('-m1')))
            self.assertTrue(group.findall('.//'+SVG+'path'))
            self.assertEqual([text.text for text in group.findall('.//'+SVG+'text')],['= 60'])
        for field,value in [('mm.dots','0'),('staff','2'),('tstamp','2'),('midi.bpm','60')]:
            wrong=ET.fromstring(mei); wrong.find('.//'+MEI+'tempo').set(field,value)
            with self.subTest(field=field), self.assertRaises(AssertionError):
                imported_tempo_ids(ET.tostring(wrong,encoding='unicode'),piece)

    def test_validator_rejects_a_self_consistent_wrong_approach_ramp(self):
        piece,midi,xml=deepcopy(self.exports['pivot'])
        tick=0
        for message in midi.tracks[0]:
            tick+=message.time
            if tick==5280 and message.type=='set_tempo': message.tempo=mido.bpm2tempo(65)
        next(mark for mark in piece['tempo_map'] if mark['beat']==5.5)['microseconds']=mido.bpm2tempo(65)
        with self.assertRaisesRegex(AssertionError,'interpolates'): validate_tempo_pivots(piece,midi,xml)


if __name__ == '__main__':
    unittest.main(verbosity=2)
