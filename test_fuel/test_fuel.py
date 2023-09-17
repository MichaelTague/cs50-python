from fuel import convert, gauge
import pytest

def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_ints():
    assert convert("1/200") == 0
    assert convert("2/200") == 1

def test_value_error1():
    with pytest.raises(ValueError):
        convert("cat/100")

def test_value_error2():
    with pytest.raises(ValueError):
        convert("1/dog")

def test_value_error3():
    with pytest.raises(ValueError):
        convert("4/3")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

