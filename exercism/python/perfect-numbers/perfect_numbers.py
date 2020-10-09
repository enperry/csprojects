def classify(number):
    if(number < 1):
        raise ValueError("non-natural number")
    if((sum([i for i in range(1, number) if number % i == 0])) > number):
        return "abundant"
    elif((sum([i for i in range(1, number) if number % i == 0])) < number):
        return "deficient"
    else:
        return "perfect"