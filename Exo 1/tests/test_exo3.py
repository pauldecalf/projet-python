from exo3 import sum_two_numbers


def test_sum_two_numbers():
    # Teste la fonction avec deux nombres
    assert sum_two_numbers(1, 2) == 3, "Should be 3"
    assert sum_two_numbers(-1, -1) == -2, "Should be -2"
    assert sum_two_numbers(0, 0) == 0, "Should be 0"
