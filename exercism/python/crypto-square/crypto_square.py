import re
from math import sqrt, ceil
from itertools import zip_longest

def cipher_text(plain_text):
    msg = re.sub(r"\W", "", plain_text.lower())
    size = ceil(sqrt(len(msg)))
    square = zip_longest(*[iter(msg)] * size, fillvalue = " ")
    return " ".join(map("".join, zip_longest(*square, fillvalue = "")))