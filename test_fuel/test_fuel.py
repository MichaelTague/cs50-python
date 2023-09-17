from fuel import convert, gauge
import pytest

def test_empty():
    assert convert("1/200") == 1

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/100")


