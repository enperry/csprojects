import re
from math import gcd

def encode(plain_text, a, b):
    if(gcd(a, 26) > 1):
        raise ValueError("a and m must be co-prime")

    text = re.sub(r"\W", "", plain_text).lower()
    encoded_text = ""
    for i, char in enumerate(text):
        if(i % 5 == 0):
            encoded_text = encoded_text + " "
        if(char.isdigit()):
            encoded_text = encoded_text + char
        else:
            encoded_text = encoded_text + chr((a * (ord(char) - 97) + b) % 26 + 97)
    return encoded_text.strip()

def decode(ciphered_text, a, b):
    if(gcd(a, 26) > 1):
        raise ValueError("a and m must be co-prime")

    decoded_text = ""
    for char in ciphered_text.replace(" ", ""):
        if(char.isdigit()):
            decoded_text = decoded_text + char
        else:
            decoded_text = decoded_text + chr(pow(a, -1, 26) * (ord(char) - 97 - b) % 26 + 97)
    return decoded_text