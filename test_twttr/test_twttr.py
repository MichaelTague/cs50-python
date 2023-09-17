from twttr import shorten

def test_lower():
    assert shorten("supercalifragilisticexpialidocious") == "sprclfrglstcxpldcs"

def test_upper():
    assert shorten("QUEUE") == "Q"

def test_number():
    assert shorten("10four") == "10fr"

def test_punctuation():
    assert shorten("10-four") == "10-fr"