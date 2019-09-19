from spaceman import *

def test_is_guess_in_word():
    assert is_guess_in_word('y','axe') == False
    assert is_guess_in_word('x','axe') == True

def test_get_guessed_word():
    assert get_guessed_word('axe',['a','x','c']) == "ax_ "
    assert get_guessed_word('axe',['a','x','e']) == "axe"

def test_is_word_guessed():
    assert is_word_guessed("hello",['h','e','l','a']) == False
    assert is_word_guessed("hello",['h','e','l','o']) == True
    
  
