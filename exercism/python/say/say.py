from num2words import num2words

def say(number):
    if(number < 0 or number >= 1e12):
        raise ValueError(number)
    return num2words(number).replace(",", "").replace(" and ", " ")
