from fuel import convert, gauge
import pytest

def test_empty():
    assert gauge("1/200") == "E"

def test_full():
    assert gauge("195/200") == "F"

def test_value_error1():
    with pytest.raises(ValueError):
        convert("cat/100")

def test_value_error2():
    with pytest.raises(ValueError):
        convert("1/dog")

def test_value_error3():
    with pytest.raises(ValueError):
        convert("4/3")

