from dictionary_words import ENGLISH_WORDS
from word_game import get_word_score, update_hand, is_valid_word


def test_get_word_score():
    assert get_word_score("", 7) == 0
    assert get_word_score("scored", 7) == 351
    assert get_word_score("FORK", 4) == 308
    
    
def test_update_hand():
    assert update_hand({'h': 1, 'e': 1, 'l': 2, 'o': 1}, "HELLO") == {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    assert update_hand({'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}, "quail") == {'a': 0, 'q': 0, 'l': 1, 'm': 1, 'u': 0, 'i': 0}
    assert update_hand({'e':1, 'v':2, 'n':1, 'i':1, 'l':2}, "Evil") == {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    
    
def test_is_valid_word():
    assert is_valid_word("honey", {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}, ENGLISH_WORDS) == True
    assert is_valid_word("honey", {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}, ENGLISH_WORDS) == False
    assert is_valid_word("Rapture", {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}, ENGLISH_WORDS) == False
    
    
def test_wildcard():     
    assert is_valid_word("h*ney", {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}, ENGLISH_WORDS) == True  
    assert is_valid_word("c*wz", {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}, ENGLISH_WORDS) == False
    assert is_valid_word("e*m", {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}, ENGLISH_WORDS) == False
    