def steps(number):
    if(number <= 0):
        raise ValueError("Nope.")
    
    if(number == 1):
        return 0

    else:
        number = number / 2 if number % 2 == 0 else 3 * number + 1
        return 1 + steps(number)
