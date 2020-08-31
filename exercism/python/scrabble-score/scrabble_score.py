scores = {"AEIOULNRST": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
values = {char: score for (chars, score) in scores.items() for char in chars}

def score(word):
    return sum(values[ch] for ch in word.upper())
    
