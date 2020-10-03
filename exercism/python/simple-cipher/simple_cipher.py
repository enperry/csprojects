import random
import string

class Cipher:
    def __init__(self, key=None):
        if(key is None):
            key = "".join([random.choice(string.ascii_lowercase) for i in range(100)])
        self.key = key

    def encode(self, text):
        return "".join([chr(ord("a") + (ord(text[i]) + ord(self.key[i % len(self.key)]) - 2 * ord("a")) % 26) for i in range(len(text))])


    def decode(self, text):
        return "".join([chr(ord("a") + (ord(text[i]) - ord(self.key[i % len(self.key)])) % 26) for i in range(len(text))])
