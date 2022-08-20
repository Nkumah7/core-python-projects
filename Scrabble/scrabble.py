"""A Scrabble game using english words from the Natural Language Toolkit (nltk) Python library"""

import math
import random
from dictionary_words import english_words


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
# Alphabets and coresponding points for each letter
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def main():
    print("Loading list of words...")
    print(len(english_words), "words loaded\n")

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
        1, or
        7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
        and n is the hand length when the word was played
    
    '*' represents wildcard - if a star is found in the word, it is skipped
    '!' 
    """
    letters_points = 0
    for letter in word.lower():
        if letter == "*":
            continue
        elif letter == "!":
            continue
        letters_points += SCRABBLE_LETTER_VALUES[letter]
        
    return letters_points * max(1, (7 * len(word)) - 3 * (n - len(word)))

def display_hand(hand):
    """
    Displays the letters currently in the hand.
    Example:
       display_hand({'e': 1, '*': 1, 'i': 1, 'b': 3, 'r': 1, 'g': 2}) -> e * i b b b r g g
    """
    # Loop through the keys in hand
    for letter in hand.keys():
        # Loop through the range of number of values (points) for each letter
        for _ in range(hand[letter]):
            print(letter, end=' ') # print all on the same line
    print() # print an empty line

def deal_hand(n):
    """
    Returns a dictionary of random hand containing n lowercase letters.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
    """
    
    hand={} # Create an empty dictionary to store lowercase letters and each point
    num_vowels = int(math.ceil(n / 3)) # Get the smallest integer not less than n/3

    # Loop through the number of vowels and store random vowels with each point
    # Add a wild card and its point after storing the vowels. A wild card is 1 point
    for _ in range(num_vowels-1):
        x = random.choice(VOWELS)    
        hand[x] = SCRABBLE_LETTER_VALUES[x]
        hand.update({"*": 1})
        
    # Loop through the remaining n number of letters and store consonants 
    for _ in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = SCRABBLE_LETTER_VALUES[x]
    
    return hand

    


if __name__ == "__main__":
    main()