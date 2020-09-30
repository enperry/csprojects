def square(number):
    if(not 0 < number < 65):
        raise ValueError("Number should be between 1 and 64.")
    return 1 << (number - 1)

def total():
    return sum(square(i) for i in range(1, 65))
