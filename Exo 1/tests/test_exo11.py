from exo11 import decode_message

def test_decode_message():
    assert decode_message("72 101 108 108 111") == "Hello", "Should be Hello"
    assert decode_message("72 101 108 108 111 32 87 111 114 108 100") == "Hello World", "Should be Hello World"
    assert decode_message("72 101 108 108 111 32 87 111 114 108 100 33") == "Hello World!", "Should be Hello World!"
