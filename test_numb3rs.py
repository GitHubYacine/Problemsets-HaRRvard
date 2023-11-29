from numb3rs import validate

def test_validate_numbers():
    assert validate(256) == False
    assert validate(421) == False
    assert validate(23) == True
    
def test_validate_chars():
    assert validate("hello") == False
    assert validate("!") == False
    
    
#STILL DONT UNDERSTAND FULLY HOW TO TEST CODE MYSELF WITHOUT USING GPT!!!