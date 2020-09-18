def is_armstrong_number(number):
    n = str(number)
    return number == sum(int(d) ** len(n) for d in n)
    