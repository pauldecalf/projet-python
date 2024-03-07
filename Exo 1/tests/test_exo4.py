from exo4 import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
