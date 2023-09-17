from fuel import convert, gauge
import pytest

def test_empty():
    assert gauge("1/200") == "E"

def test_full():
    assert gauge("195/200") == "F"

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/100")


