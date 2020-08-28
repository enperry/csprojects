import re
from collections import Counter

def count_words(sentence):
    sentence = re.sub(r"[!&@$%^&_]", " ", sentence)
    return Counter(re.findall(r"\b[a-zA-Z0-9\"]+\b", sentence.lower()))