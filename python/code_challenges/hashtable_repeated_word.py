from data_structures.hashtable import Hashtable
import string


def first_repeated_word(text):
    """
    .maketrans() create translation table mapping each ASCII punctuation char to None
    .translate() returns new string with punctuation chars removed

    """
    words = [word.translate(text.maketrans('', '', string.punctuation)).lower()
             for word in text.split()
             ]
    hash_map = Hashtable()
    # iterate through each word in words
    for word in words:
        # if our hashmap has word, already appeared, return that word
        if hash_map.has(word):
            return word
        # else set word in hashmap, word = key value = None
        hash_map.set(word, None)
