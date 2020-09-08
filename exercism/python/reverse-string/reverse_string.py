def reverse(text):
    reversedString = ""
    text = text.split()
    for i in reversed(text):
        reversedString = reversedString + i
    return i