from exo6 import tuple_with_most_elements


def test_tuple_with_most_elements():
    assert tuple_with_most_elements([(1, 2, 3), (4, 5), (6, 7, 8, 9)]) == (6, 7, 8, 9), "Should be (6, 7, 8, 9)"
    assert tuple_with_most_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)]) == (1, 2, 3), "Should be (1, 2, 3)"
    assert tuple_with_most_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13)]) == (10, 11, 12, 13), "Should be (10, 11, 12, 13)"
