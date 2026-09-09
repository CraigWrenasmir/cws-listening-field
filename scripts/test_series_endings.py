"""Exercise the first series boundary and a real final silent staff without exporting assets."""
import unittest
from music21 import expressions
from compose import PIECES, make_score
from series_rules import series_for

class SeriesEndings(unittest.TestCase):
    def test_boundary(self):
        self.assertEqual(series_for(200)['note_limit'],256)
        self.assertEqual(series_for(200)['page_limit'],4)
        self.assertEqual(series_for(201)['note_limit'],768)
        self.assertEqual(series_for(201)['page_limit'],6)
        for op in [0,401]:
            with self.assertRaises(ValueError):series_for(op)

    def test_solo_ending_and_ordinary_chord_ending(self):
        for op in [203,204]:
            piece=next(p for p in PIECES if p['op']==op)
            score,events=make_score(piece)
            for index,hand in enumerate(['rh','lh']):
                final=score.parts[index].getElementsByClass('Measure')[-1]
                fermatas=[x for n in final.notesAndRests for x in n.expressions if isinstance(x,expressions.Fermata)]
                silent=op==204 and hand=='lh'
                self.assertEqual(len(fermatas),0 if silent else 1)
                self.assertEqual(len(final.notes)==0,silent)
                self.assertEqual(final.rightBarline.type,'final')
            if op==204:self.assertFalse(any(e['hand']=='lh' and e['offset']>=168 for e in events))

if __name__=='__main__':unittest.main()
