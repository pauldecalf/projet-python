from exo9 import print_pyramid


def test_print_pyramid(capsys):
    height = 3
    expected_output = "  *\n ***\n*****\n"
    print_pyramid(height)
    captured = capsys.readouterr()
    assert captured.out == expected_output

    height = 5
    expected_output = "    *\n   ***\n  *****\n *******\n*********\n"
    print_pyramid(height)
    captured = capsys.readouterr()
    assert captured.out == expected_output
