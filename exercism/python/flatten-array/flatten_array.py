def flatten(iterable):
    result = []
    for item in iterable:
        if(item != None):
            if(type(item) == list):
                result = result + flatten(item)
            else:
                result = result + [item]
    return result