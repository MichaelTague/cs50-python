import pytest

from project import pretty_term

def test_pretty_term():
    assert pretty_term(360) == "30 Years"
    assert pretty_term(363) == "30 Years, 3 Months"
    assert pretty_term(1)   == "1 Month"
    assert pretty_term(2)   == "2 Months"
    assert pretty_term(12)  == "1 Year"
    assert pretty_term(13)  == "1 Year, 1 Month"


