from exo10 import max_of_three_numbers


def test_max_of_three_numbers():
    assert max_of_three_numbers(1, 2, 3) == 3, "Should be 3"
    assert max_of_three_numbers(3, 2, 1) == 3, "Should be 3"
    assert max_of_three_numbers(2, 3, 1) == 3, "Should be 3"
