from exo7 import reverse_tuple_elements
def test_reverse_tuple_elements():
    assert reverse_tuple_elements([(1, 2, 3), (4, 5), (6, 7, 8, 9)]) == [(3, 2, 1), (5, 4), (9, 8, 7, 6)], "Should be [(3, 2, 1), (5, 4), (9, 8, 7, 6)]"
    assert reverse_tuple_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)]) == [(3, 2, 1), (6, 5, 4), (9, 8, 7)], "Should be [(3, 2, 1), (6, 5, 4), (9, 8, 7)]"
    assert reverse_tuple_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13)]) == [(3, 2, 1), (6, 5, 4), (9, 8, 7), (13, 12, 11, 10)], "Should be [(3, 2, 1), (6, 5, 4), (9, 8, 7), (13, 12, 11, 10)]"