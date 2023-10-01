import pytest

import project

def test_
def test_not_4():
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3") == False

def test_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("-1.2.4.5") == False
    assert validate("255.255.255.256") == False
    assert validate("275.3.6.28") == False

def test_invalid_chars():
    assert validate("a.2.3.4") == False
    assert validate("1.2.c.4") == False
    assert validate("1.2b.3.4") == False
