from string import ascii_uppercase

def rows(letter):
    idx = ascii_uppercase.index(letter)
    letters = ascii_uppercase[ : idx] + ascii_uppercase[idx :: -1]
    locations = ascii_uppercase[idx :: -1] + ascii_uppercase[1 : idx + 1]
    return [("".join(c if c == char else " " for c in locations))
            for char in letters]