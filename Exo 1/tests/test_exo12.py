from exo12 import count_palindromes


def test_count_palindromes():
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor"]) == 5, "Should be 5"
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello"]) == 5, "Should be 5"
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello", "world"]) == 5, "Should be 5"
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello", "world", "madam"]) == 6, "Should be 6"
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello", "world", "madam", "racecar"]) == 7, "Should be 7"
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello", "world", "madam", "racecar", "civic"]) == 8, "Should be 8"
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello", "world", "madam", "racecar", "civic", "deified"]) == 9, "Should be 9"
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello", "world", "madam", "racecar", "civic", "deified", "noon"]) == 10, "Should be 10"
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello", "world", "madam", "racecar", "civic", "deified", "noon", "stats"]) == 11, "Should be 11"
