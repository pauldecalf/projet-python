from exo16 import symmetric_difference


def test_symmetric_difference():
    assert symmetric_difference({1, 2, 3}, {2, 3, 4}) == {1, 4}
