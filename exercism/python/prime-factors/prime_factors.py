def factors(value):
    factors = []
    i = 2
    while(value != 1):
        while((value % i) == 0):
            factors.append(i)
            value = value // i
        i = i + 1
    return factors