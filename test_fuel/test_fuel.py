from fuel import convert, gauge

def test_empty():
    assert convert("1/200") == 1
    assert gauge(1) == "E"

def test_full():
    assert convert("199/200") == 100
    assert gauge(100) == "F"

def test_middle():
    assert convert("50/100") == 50
    assert gauge(50) == "50%"