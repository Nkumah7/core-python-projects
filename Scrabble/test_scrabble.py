from scrabble import get_word_score

def test_get_word_score():
    assert get_word_score("", 7) == 0
    assert get_word_score("scored", 7) == 351
    assert get_word_score("FORK", 4) == 308