import pytest

from working import convert

def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_odd_numbers():
    assert convert("009 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_chars():
    assert validate("a.2.3.4") == False
    assert validate("1.2.c.4") == False
    assert validate("1.2b.3.4") == False
