from itertools import product
from sage.all import ZZ, matrix
from vinal import GetIntegerPoints


def test_fundamental_parallelepipeds():
    examples = [
        [[2, 0], [0, 3]],
        [[2, 1], [1, 3]],
        [[-2, 1], [0, 3]],
        [[3, -2, 1], [0, 2, 1], [0, 0, -2]],
        [[1, 20], [0, 1]],
    ]
    for entries in examples:
        m = matrix(ZZ, entries)
        points = GetIntegerPoints(m)
        assert len(points) == abs(m.det())
        assert len(set(points)) == len(points)
        inverse = m.inverse()
        for point in points:
            coefficients = matrix(ZZ, [point]) * inverse
            assert all(0 <= x < 1 for x in coefficients.list())
