from fuel import convert, gauge

def test_empty():
    assert convert("1/200") ==

def test_one_letter():
    assert is_valid("A23") == False

def test_two_letters():
    assert is_valid("AB3") == True

def test_leading_zero():
    assert is_valid("AB0123") == False

def test_leading_digit():
    assert is_valid("AB123") == True

def test_short():
    assert is_valid("A") == False
    assert is_valid("AA") == True

def test_too_long():
    assert is_valid("AAAAAAA") == False
    assert is_valid("AAAAAA") == True

def test_num_out_of_place():
    assert is_valid("AA12BB") == False
    assert is_valid("AABB12") == True

def test_bad_alpha():
    assert is_valid("AB,12") == False
    assert is_valid("AB12") == True