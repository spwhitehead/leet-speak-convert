import pytest

from leet_speak_convert import convert

def test_convert():
    assert convert("Speak") == "5p3@k"
    assert convert("Hello") == "H3110"
    assert convert("") == ""
    assert convert("1234") == "1234"
    assert convert("pizza") == "p!zz@"


test_convert()