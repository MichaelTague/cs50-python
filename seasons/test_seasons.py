import pytest

from sessons import minutes_since, int_to_minutes_string

def test_since():
    assert minutes_since
    assert count("The humnan race") == 0

def test_leading_um():
    assert count("Um, what's up?") == 1
    assert count("Um, well, I'm just human.") == 1

def test_embeded_um():
    assert count("Well, um, I don't know.") == 1
    assert count("I guess, um, I'm just human") == 1
    assert count("But, I don't know um about you!") == 1

def test_trailing_up():
    assert count("Best two out of three?  Um?") == 1
    assert count("No, you cheat too much.  um") == 1

def test_multiple_ums():
    assert count("Um, some people um just really can't talk um much without saying um.") == 4
