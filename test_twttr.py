from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("Yacine") == "Ycn"
    assert shorten("ahmendura") == "hmndr"