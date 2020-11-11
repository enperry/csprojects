def score(x, y):
    dist = (x ** 2 + y ** 2) ** (1/2)
    if(dist > 10):
        return 0
    elif(dist > 5):
        return 1
    elif(dist > 1):
        return 5
    else:
        return 10