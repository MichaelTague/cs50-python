import pytest
from fuel import convert, gauge

def test_empty():
    assert convert("1/200") == 1
