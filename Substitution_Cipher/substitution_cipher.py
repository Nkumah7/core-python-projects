"""
Substitution Cipher using english words from the Natural Language Toolkit (NLTK) Python library
    -   Substitution Cipher is a way of hiding messages
    -   This method involves creating a hidden coding scheme, whereas a randomly selected letter is substituted
        for each original letter
"""

from permutations import get_permutations
from dictionary_words import ENGLISH_WORDS


VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


def is_word(word_list, word):
    """
    -   Determines if word is a valid word, ignoring
    capitalization and punctuation.
    -   Returns True if word is in word_list, and False otherwise
    """    
    word = word.lower()
    return word in word_list


class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list of english words from NLTK library)
        '''
        self.message_text = text
        self.valid_words = ENGLISH_WORDS
        
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
    
    def get_valid_words(self):
        """
        -   Returs a copy of self.valid_words
            *   This is to safely access valid words outside the class, 
                and avoid accidentally mutating class attributes.
        """
        return self.valid_words.copy()
    
    def build_transpose_dict(self, vowels_permutation):
        """
        -   Returns a dictionary mapping a letter (string) to 
            another letter (string).         
            *   Creates a dictionary that can be used to apply a cipher to a letter.
                The dictionary maps every uppercase and lowercase letter to an
                uppercase and lowercase letter, respectively. Vowels are shuffled 
                according to vowels_permutation.        
        """
        
        letter_map = {}
        letters = VOWELS_UPPER + CONSONANTS_UPPER + VOWELS_LOWER + CONSONANTS_LOWER
        for letter in letters:
            if letter in vowels_permutation.upper():
                letter_map[letter] = vowels_permutation[VOWELS_UPPER.find(letter)].upper()
            elif letter in vowels_permutation:
                letter_map[letter] = vowels_permutation[VOWELS_LOWER.find(letter)]
            
        return letter_map
    
    def apply_transpose(self, transpose_dict):
        """     
        Returns an encrypted version of the message text, based on the dictionary
        """
        encrypted_msg = ''  
        for letter in self.message_text:
            if letter in transpose_dict:
                encrypted_msg += transpose_dict[letter]
            else:
                encrypted_msg += letter
        return encrypted_msg
    
    
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list of english words from NLTK library)
        '''
        SubMessage.__init__(self, text)
        
    def decrypt_message(self):
        """
        -   Returns the best decrypted message         
            *   Each vowel permutation is tested on the encrypted message. Words formed from the decrypted text
                are checked in each permutation for valid English words.
            *   Returns the decrypted message that formed valid words.        
            *   Returns the original string if no good permutations are found. If there are
            *   If multiple permutations that forms maximum number or words, one of them is returned.
        """
        
        valid_words = []        
        decrypted_message = []
        sentences = {}
        perms = get_permutations(VOWELS_LOWER) # Get each permutation of vowels
        
        for i, perm in enumerate(perms): # Loop through each vowel permutaion)
            transpose_dict = self.build_transpose_dict(perm) # Get transpose dict for each vowel permutaion
            transposed_msg = self.apply_transpose(transpose_dict) # Get possible decrypted message
            decrypted_message.append(transposed_msg.split()) # Split the possible decrypted message into a list and store each in a list 
            for word in transposed_msg.split(): # Loop through each possible decrypted message
                if is_word(self.valid_words, word): # Check for valid words in each possible decrypted message
                    valid_words.append(word) # Store each valid word 
            sentences[len(valid_words)] = i # Store group of valid words for each vowel permutation in a dictionary (for faster access)
            valid_words = [] # Restore valid words list back to empty list to store valid words for next vowel permutation
        
        # Return the original string if no good permutations are found 
        if sum(sentences.keys()) < 1:
            return self.message_text
        
        # Use the 'keys' method to get the index of the sentence with the highest number of valid words
        decrypted_msg_index = sentences[max(sentences.keys())]         
            
        # Join the words in the list and return
        return " ".join(decrypted_message[decrypted_msg_index])
    

if __name__ == "__main__":
    print("Loading list of words...")
    print(len(ENGLISH_WORDS), "words loaded\n")
    msg = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = msg.build_transpose_dict(permutation)
    print("Original message:", msg.get_message_text(), "\nPermutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", msg.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(msg.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())