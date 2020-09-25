from string import ascii_lowercase as abc
from textwrap import wrap

tr = str.maketrans(abc, abc[::-1])

def encode(plain_text):
    s = "".join(filter(str.isalnum, plain_text.lower()))
    return " ".join(wrap(s.translate(tr), 5))


def decode(ciphered_text):
    return ciphered_text.replace(" ", "").translate(tr)

    
