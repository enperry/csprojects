from re import sub

def decode(string):
    return sub(r'(\d+)(\D)', lambda m: m[2] * int(m[1]), string)


def encode(string):
    return sub(r'(.)\1+', lambda m: str(len(m[0])) + m[1], string)
