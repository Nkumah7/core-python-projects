"""A Word Game using english words from the Natural Language Toolkit (nltk) Python library"""

import math
import random
from dictionary_words import ENGLISH_WORDS


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
# Alphabets and coresponding points for each letter
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def main():
    print("Loading list of words...")
    print(len(ENGLISH_WORDS), "words loaded\n")
    play_game(ENGLISH_WORDS)

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
    
    '*' Represents wildcard - if a star is found in the word. It is skipped
    '!' User inputs this symbol twice if they want to quit,. It is also skipped
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
        hand[x] = hand.get(x, 0) + 1
        hand.update({"*": 1})
        
    # Loop through the remaining n number of letters and store consonants 
    for _ in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
            
    return hand

def update_hand(hand, word):
    """
    Returns a new hand using the letters in the given word 
    """
    hand_clone = hand.copy() # Create copy of data structure to avoid mutating original copy
    # Loop through word and decrement the number of letter in hand
    for letter in word.lower():
        if letter in hand_clone:
            hand_clone[letter] -= 1
    return hand_clone 

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is made of letters in the hand. 
    Returns False if word not in the word_list
    """
    
    new_word = "" # Store new word
    word_exist = "" # Store word to check if the word exist
    available_words = [] # Store the words that are made up of the available letters
    hand_clone = hand.copy() # Copy data structure to avoid mutating original copy 
    
    valid_word = False
    # Check if wild card (*) in word
    if "*" in word:
        # Loop through all the vowels and replace * with a vowel each loop and store words that exist in word list
        for vowel in VOWELS:
            new_word = word.replace("*", vowel)
            if new_word.lower() in word_list:
                available_words.append(new_word)
        # Check if there is a word or more stored. 
        # If none, then there is no word that exist with the available letters
        if len(available_words) < 1:
            return False
        valid_word = True # True when there is a word or more words
    
    # Loop through the word form a word from letters if they exist in the 'hand' data structure
    for letter in word.lower():
        if letter in hand_clone and hand_clone[letter] > 0:           
            hand_clone[letter] -= 1
            word_exist += letter     
    
    # Returns True if the word formed from 'hand' data structure and the word  
    # are the same and also exist in the word list. Returns False otherwise
    if len(word_exist) == len(word) and word.lower() in word_list or valid_word:
        return True
    return False


def calculate_handlen(hand):
    """ 
    Returns the amount of letters in the current hand.
    """    
    return sum(hand.values()) 


def play_hand(hand, word_list):
    
    """
    - The user plays a hand and it is displayed
    - Word entered by player albeit valid or invalid, uses up letters currently in hand
    - Invalid words are rejected and so they do not count towards score
    - Score for valid word is displayed with remaining letters, and player is asked to enter another word
    - The sum of the word scores is displayed when the hand finishes.
    - The hand finishes when there are no more unused letters.
    - The user can choose to end the game at any point. Player just has to input "!!" without a letter or word.
    """
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    letter_in_hand = True
    while letter_in_hand:
        # Display the hand
        print("\nCurrent Hand", end=": ")
        display_hand(hand)      
        # Ask user for input    
        try: 
            user_word = input("Enter word, or \"!!\" to indicate that you are finished: ")     
        
        # If the input is two exclamation points:
            if user_word == "!!":              
                break # End the game (break out of the loop)              
            # If the word is valid:
            if is_valid_word(user_word, hand, word_list):
                word_points = get_word_score(user_word, calculate_handlen(hand))  
                total_score += word_points     
                            
                # Tell the user how many points the word earned and the updated total score
                print(f"\"{user_word}\" earned {word_points} points. Total score: {total_score} points")

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
            else:
                raise ValueError
        except ValueError:
            print("That is not a valid word. Please choose another word.")
                
            # update the user's hand by removing the letters of their inputted word
        hand = update_hand(hand, user_word)
        
    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
        if calculate_handlen(hand) < 1:            
            letter_in_hand = False      
            print("\nRan out of letters")
            # print(f"Total score: {total_score} points")  

    # Return the total score as result of function
    return total_score

def substitute_hand(hand, letter):
    """ 
    Returns 'hand' data structure with substituted letter with regards to player's choice of substitution
    """
    
    hand_clone = hand.copy() # Copy hand to avoid mutation
    # Create list of letters with the letter player chose to substitute
    available_letters = [unused_letter for unused_letter in SCRABBLE_LETTER_VALUES.keys() if unused_letter != letter]
    # Choose a random letter from the list of available letters created
    new_letter = random.choice(available_letters)    
    hand_clone[new_letter] = hand_clone[letter] # Insert the letter into the 'hand' data structure    
    del hand_clone[letter] # Remove letter player wants to substitute from the 'hand' data structure
    
    return hand_clone

def user_input(user_ans, error_msg, input_type = str):
    """Helper function for user to enter digit information"""
    while True:
        try:
            return input_type(input(f"{user_ans} "))
        except (ValueError, KeyError, TypeError):
            print(error_msg)


def yes_input(user_ans, error_msg):
    """Helper function for user inputing yes/y or no/n"""
    sub_letter_yes = ["yes", "y"]
    sub_letter_no = ["no", "n"]
    while True:
        try:
            sub_letter = input(user_ans).lower().strip()             
            if sub_letter not in sub_letter_yes and sub_letter not in sub_letter_no:
                raise ValueError
            if sub_letter in sub_letter_yes:
                return True
            return False                
        except ValueError:
            print(error_msg)
            

def play_game(word_list):
    """
    The Game
    ----------------------
    Allow the user to play a series of hands      
    - Returns the total score for the series of hands
    """

    substitute_times = 1 # Save number of substitute times player has. Player will have only one chance to substitute hand    
    # Ask player for number of hands to play
    num_of_hands = user_input("Enter total number of hands:", "Please enter a number.", int)
    hand = deal_hand(HAND_SIZE) # Create the hand for player. Hand size for the game will be 7 as stored in HAND_SIZE variable.
    hand_clone = hand.copy() # Copy data to avoid mutation or original data
    total_score = 0 # Start will total score of 0 because user has no points till game starts and points will accumulate
    
    while num_of_hands:        
        print("Current Hand", end=": ")
        display_hand(hand) # Displays hand        
        
        while substitute_times:
            # If user has substitute times then, check player's response to substituting a letter. 
            # If yes/y then player can substitute a letter of choice from the hand displayed
            # If no/n then player moves on with the current hand            
            if yes_input("Would you like to substitute a letter (yes/y or no/n)? ", "Please enter yes/y or no/n"): 
                try:                
                    letter_replacement = input("Which letter would you like to replace: ").lower().strip()
                    hand = substitute_hand(hand, letter_replacement)
                    substitute_times -= 1     
                # If player inputs anything apart from a letter, player will be prompted to enter a valid letter           
                except KeyError:
                    print("Please enter a valid letter") 
            else: 
                break       
        
        score = play_hand(hand, word_list) # Save current score
        print(f"Total score of this hand: {score}")  # Displays current score 
        total_score += score  # Update total score with current score
        print("---------------------------")
        num_of_hands -= 1 # Decrement number of hands
        
        # Check if number of hands. End the game and display total score if it has finished
        if num_of_hands < 1:            
            print(f"Total score over all hands: {total_score}") 
            break      
        
        # Ask player if they would like to replay the hand that was shown in the previous hand.
        # If yes/y, display the previous hand
        # If no/n, display a different hand
        if yes_input("Would you like to replay the hand (yes/y or no/n)? ", "Please enter yes/y or no/n"):
            hand = hand_clone
        else:
            hand = deal_hand(HAND_SIZE)


if __name__ == "__main__":
    main()