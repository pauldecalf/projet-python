def somme(x, y):
    return x + y


def test_somme_true():
    assert somme(2, 3) == 5
    assert somme(1, 1) == 2


def test_somme_false():
    assert somme(2, 3) == 1
    assert somme(1, 1) == 4
