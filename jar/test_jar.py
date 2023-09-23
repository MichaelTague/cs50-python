import pytest

from jar import minutes_since, int_to_minutes_string

def test_minutes_since():
    assert minutes_since("2023-09-01", "2022-09-01") == 525600
    assert minutes_since("2000-01-01", "1999-12-31") == 1440

def test_int_to_minutes():
    assert int_to_minutes_string(1440) == "One thousand, four hundred forty minutes"
    assert int_to_minutes_string(525600) == "Five hundred twenty-five thousand, six hundred minutes"

def test_invalid():
    with pytest.raises(SystemExit) as exit_info:
        minutes_since("2000-01-01", "Dec 31, 1999")
    assert exit_info.value.args[0] == "Invalid date"