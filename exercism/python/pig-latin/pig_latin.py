import re

def translate(text):
    return " ".join(map(encode, text.split()))

def encode(word):
    # pylint is being fussy, so this will shut it up
    prefix = None
    return word[len(prefix := re.search("(y|.*?(qu)?)([aeiouy]|xr|yt)", word).group(1)):] + prefix + "ay"

