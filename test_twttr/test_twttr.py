from twttr import shorten

def test_lower():
    assert shorten("supercalifragilisticexpialidocious") == "sprclfrglstcxpldcs"

def test_upper():
    assert shorten("QUEUE") == "Q"