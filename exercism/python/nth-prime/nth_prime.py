def prime(number):
    if(number < 1):
        raise ValueError("enter a positive integer")
    primes = []
    nextPrime = 2

    while(len(primes) < number):
        isPrime = True
        for i in primes:
            if(nextPrime % i == 0):
                isPrime = False
                break
        if(isPrime == True):
            primes.append(nextPrime)
        nextPrime = nextPrime + 1
    return primes[-1]