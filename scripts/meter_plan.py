"""Quarter-beat bar boundaries for fixed or explicitly changing metres."""
from fractions import Fraction


def bar_plan(piece, count=None):
    count = piece['bars'] if count is None else count
    metres = piece.get('meters', [piece['meter']] * count)
    assert len(metres) == count and count > 0, 'One metre is required per bar'
    assert metres[0] == piece['meter'], 'Opening metre must match meter'
    lengths = []
    for signature in metres:
        numerator, denominator = map(int, signature.split('/'))
        assert numerator > 0 and denominator > 0 and denominator & (denominator - 1) == 0
        lengths.append(float(Fraction(4 * numerator, denominator)))
    starts = []
    total = 0.0
    for length in lengths:
        starts.append(total)
        total += length
    return list(metres), lengths, starts, total
