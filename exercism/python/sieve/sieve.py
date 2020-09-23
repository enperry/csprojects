def primes(limit):
    numbers = [False, False] + list(range(2, limit + 1))

    for number in numbers:
        if(number):
            for i in range(number ** 2, limit + 1, number):
                numbers[i] = False

    return [prime for prime in numbers if prime]