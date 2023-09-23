import pytest

from working import convert

def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_bad_numbers():
    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("1 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5:95 PM")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


    assert convert("009 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_chars():
    assert validate("a.2.3.4") == False
    assert validate("1.2.c.4") == False
    assert validate("1.2b.3.4") == False
