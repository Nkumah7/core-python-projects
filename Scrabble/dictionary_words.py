# Reference - https://www.datasciencebytes.com/bytes/2014/11/03/get-a-list-of-all-english-words-in-python/


# import nltk - Import nltk to access nltk library
# nltk.download() - GUI will pop up to download and install nltk packages 
from nltk.corpus import words

english_words = words.words()