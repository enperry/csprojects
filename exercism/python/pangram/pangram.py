import string

def is_pangram(sentence):
    sentence = set(sentence.lower())
    letters = set(string.ascii_lowercase)
    return letters.issubset(sentence)