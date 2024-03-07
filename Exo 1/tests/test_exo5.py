from exo5 import rotate_right


def test_rotate_right():
    assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3], "Should be [4, 5, 1, 2, 3]"
    assert rotate_right([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2], "Should be [3, 4, 5, 1, 2]"
    assert rotate_right([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5], "Should be [1, 2, 3, 4, 5]"
