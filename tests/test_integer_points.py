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


def test_vinal_deferred_cosets():
    from sage.all import vector
    from vinal import VinAl

    gram = matrix(ZZ, [[-2, 0], [0, 2]])
    v0 = vector(ZZ, [1, 0])
    eager = VinAl(gram, v0, output=None)
    deferred = VinAl(gram, v0, output=None, initialize_cosets=False)
    assert deferred.W == []
    assert eager.V1 == deferred.V1
    assert eager.root_lengths == deferred.root_lengths
