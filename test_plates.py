from plates import is_valid

def test_is_valid_length():
    assert is_valid("AB12") == True
    assert is_valid("AB12ABA") == False
    assert is_valid("") == False
    
def test_is_valid_letters():
    assert is_valid("AB1%#%") == False
    assert is_valid("AA##BC") == False
    assert is_valid("AB12  ") == False
    assert is_valid("ABCDF") == True
