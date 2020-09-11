import re 

def abbreviate(words):
    acronym = ""
    words = re.findall("[a-zA-Z']+", words.upper())
    acronymTemp = [i[0] for i in words]
    for i in acronymTemp:
        acronym = acronym + i
    return acronym