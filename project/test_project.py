import pytest

from decimal import Decimal, ROUND_UP, ROUND_HALF_UP, ROUND_DOWN

from project import rounding, pretty_term, parse_term_str, calc_principal

principal = Decimal("100000.00")
interest = Decimal("0.01")
term = 360
payment = Decimal("1028.62")

def test_pretty_term():
    assert pretty_term(360) == "30 Years"
    assert pretty_term(363) == "30 Years, 3 Months"
    assert pretty_term(1)   == "1 Month"
    assert pretty_term(2)   == "2 Months"
    assert pretty_term(12)  == "1 Year"
    assert pretty_term(13)  == "1 Year, 1 Month"

def test_parse_term_string():
    assert parse_term_str("30") == 360
    assert parse_term_str("30 yr") == 360
    assert parse_term_str("30 yrs") == 360
    assert parse_term_str("30 Year") == 360
    assert parse_term_str("30 years") == 360
    assert parse_term_str("30 mo") == 30
    assert parse_term_str("30 mos") == 30
    assert parse_term_str("30 Month") == 30
    assert parse_term_str("30 months") == 30
    assert parse_term_str("5 yr 6 mo") == 66
    assert parse_term_str("16 Years, 8 Months") == 200
    assert parse_term_str("100 yr") == 1200

def test_calc_principal():
    assert()