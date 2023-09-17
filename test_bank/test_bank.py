from bank import value

def test_hello():
    assert value("hello there") == 0

def test_h_word():
    assert value("help me!") == 20

def test_other():
    assert value("76 trombones") == 100