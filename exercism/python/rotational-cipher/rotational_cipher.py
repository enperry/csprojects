def rotate(text, key):
    cipher = ""
    for t in text:
        if(t.isupper()):
            cipher += chr((ord(t) - 65 + key) % 26 + 65)
        elif(t.islower()):
            cipher += chr((ord(t) - 97 + key) % 26 + 97)
        else:
            cipher += t
    return cipher
