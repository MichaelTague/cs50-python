from fuel import convert, gauge
import pytest

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/100")
