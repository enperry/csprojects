from typing import List
from collections import Counter

def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    word = word.lower()
    word_counter = Counter(word)
    return list(filter(lambda candidate: Counter(candidate.lower()) == word_counter and candidate.lower() != word, candidates))