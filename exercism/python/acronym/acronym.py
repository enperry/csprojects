def abbreviate(words):
    words = words.split()
    acronym = ""

    for i in words:
        acronym = acronym + i[0]

    return acronym.upper()
