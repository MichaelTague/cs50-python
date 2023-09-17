import pytest
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

def test_value_exception1():
    with pytest.raises(ValueError):
        convert("cat/100")

def test_value_exception2():
    with pytest.raises(ValueError):
        convert("3/dog")

def test_value_exception3():
    with pytest.raises(ValueError):
        convert("4/3")
