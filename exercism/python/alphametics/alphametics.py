from itertools import permutations
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def solve(puzzle):
    chars = [ch for ch in uppercase if ch in puzzle]
    digits = range(10)
    for sol in permutations(digits, len(chars)):
        test = puzzle
        for key, val in zip(chars, sol):
            test = test.replace(key, str(val))
        if(test[0] != "0" and " 0" not in test and eval(test)):
            return dict(zip(chars, sol))
    return None     
