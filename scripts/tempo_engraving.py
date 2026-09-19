"""Numeric quarter/dotted-quarter marks for opt-in tempo-pivot studies."""
from fractions import Fraction
import math
from pathlib import Path
import xml.etree.ElementTree as ET

from tempo_pivots import normalise_tempo_pivots


SVG = '{http://www.w3.org/2000/svg}'
MEI = '{http://www.music-encoding.org/ns/mei}'
XML_ID = '{http://www.w3.org/XML/1998/namespace}id'


def tempo_mark_plan(piece, count=None):
    """Return every printed numeric mark only when a pivot is declared."""
    pivots = normalise_tempo_pivots(piece, count=count)
    if not pivots:
        return {}
    opening_beat = '3/2' if piece['meter'] in ('6/8', '9/8', '12/8') else '1'
    values = {1: dict(bpm=piece['bpm'], new_beat=opening_beat), **pivots}
    plan = {}
    for bar, value in values.items():
        beat = Fraction(value['new_beat'])
        assert beat in (Fraction(1), Fraction(3, 2)), 'Unsupported printed tempo referent'
        number = Fraction(str(value['bpm'])) / beat
        plan[bar] = dict(
            id=f'cws{piece["op"]}-tempo-m{bar}',
            metronome_id=f'cws{piece["op"]}-metronome-m{bar}',
            bpm=value['bpm'], beat=beat,
            number=float(number) if number.denominator != 1 else number.numerator,
        )
    return plan


def assign_tempo_direction_ids(path, piece, count=None):
    """Give source MusicXML directions deterministic, verifiable identities."""
    plan = tempo_mark_plan(piece, count=count)
    if not plan:
        return
    tree = ET.parse(path)
    found = set()
    for measure in tree.getroot().findall('.//part/measure'):
        for direction in measure.findall('direction'):
            metronome = direction.find('direction-type/metronome')
            if metronome is None:
                continue
            bar = int(measure.get('number'))
            assert bar in plan and bar not in found, ('Unexpected numeric tempo mark', bar)
            mark = plan[bar]
            assert metronome.get('id') == mark['metronome_id'], ('Tempo metronome ID mismatch', bar)
            assert direction.findtext('staff', '1') == '1', ('Tempo mark belongs on upper staff', bar)
            direction.set('id', mark['id'])
            found.add(bar)
    assert found == set(plan), ('Missing numeric tempo marks', set(plan) - found)
    tree.write(path, encoding='utf-8', xml_declaration=True)


def imported_tempo_ids(mei, piece):
    """Bind Verovio IDs to exact bar/staff/beat/tempo identities.

    Verovio 6.3's MusicXML importer does not retain direction/metronome IDs.
    Validate the imported marks in their owning measures before associating
    their generated IDs with the stable source identities. No order heuristic
    or re-import of MEI is needed.
    """
    plan = tempo_mark_plan(piece)
    root = ET.fromstring(mei)
    bound = {}
    found = set()
    for measure in root.findall('.//' + MEI + 'measure'):
        for tempo in measure.findall('.//' + MEI + 'tempo'):
            bar = int(measure.get('n'))
            assert bar in plan and bar not in found, ('Unexpected imported tempo bar', bar)
            mark = plan[bar]
            assert tempo.get('staff') == '1' and Fraction(tempo.get('tstamp', '0')) == 1, ('Imported tempo position mismatch', bar)
            assert tempo.get('mm.unit') == '4', ('Imported tempo referent mismatch', bar)
            assert int(tempo.get('mm.dots', '0')) == (mark['beat'] == Fraction(3, 2)), ('Imported tempo dot mismatch', bar)
            # Verovio serialises these numeric MEI attributes to six significant
            # digits. Allow that roundoff only; referents and positions stay exact.
            assert math.isclose(float(tempo.get('mm', '0')), float(mark['number']), rel_tol=5e-6, abs_tol=1e-9), ('Imported numeric tempo mismatch', bar)
            assert math.isclose(float(tempo.get('midi.bpm', '0')), float(mark['bpm']), rel_tol=5e-6, abs_tol=1e-9), ('Imported sounding tempo mismatch', bar)
            source_id = tempo.get(XML_ID)
            assert source_id and source_id not in bound, ('Missing or duplicate imported tempo ID', bar)
            bound[source_id] = mark['id']
            found.add(bar)
    assert found == set(plan), ('Missing imported tempo marks', set(plan) - found)
    return bound


def render_pivot_tempo_glyphs(root, piece, glyph_path, imported_ids=None):
    """Replace each declared mark with its own vector glyph and number.

    Imported MEI supplies the association: neither the opening metre nor the
    order/page of SVG tempo groups determines a mark. Give output SVG groups
    the stable MusicXML source IDs after resolving Verovio's generated IDs.
    Return the IDs rendered on this page so the caller can verify coverage.
    """
    plan = {value['id']: value for value in tempo_mark_plan(piece).values()}
    assert plan, 'Opt-in tempo rendering requires tempo_pivots'
    seen = []
    for group in root.findall('.//' + SVG + 'g[@class="tempo"]'):
        source_id = group.get('id')
        mark_id = source_id if imported_ids is None else imported_ids.get(source_id)
        assert mark_id in plan, ('Unknown rendered tempo mark', mark_id)
        assert mark_id not in seen, ('Duplicate rendered tempo mark', mark_id)
        mark = plan[mark_id]
        group.set('id', mark_id)
        text = group.find(SVG + 'text')
        assert text is not None, ('Tempo mark has no positioned text', mark_id)
        x, y = text.get('x'), text.get('y')
        assert x is not None and y is not None, ('Tempo mark lacks coordinates', mark_id)
        for child in list(group):
            group.remove(child)
        glyph_group = ET.SubElement(group, SVG + 'g', transform=f'translate({x},{y})')
        glyph = ET.parse(Path(glyph_path)).getroot()
        glyph.attrib.pop('id', None)
        glyph.tag = SVG + 'g'
        glyph.set('transform', 'scale(0.72)')
        for element in glyph:
            element.tag = SVG + 'path'
        glyph_group.append(glyph)
        dotted = mark['beat'] == Fraction(3, 2)
        if dotted:
            ET.SubElement(glyph_group, SVG + 'circle', cx='305', cy='-100', r='34', fill='black')
        number = ET.SubElement(
            glyph_group, SVG + 'text', x='410' if dotted else '300', y='0',
            attrib={'font-size': '405px', 'font-family': 'Times, serif'},
        )
        number.text = f'= {mark["number"]}'
        seen.append(mark_id)
    return seen
