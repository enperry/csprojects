def smallest(min_factor, max_factor):
    return extreme(min_factor, max_factor)


def largest(min_factor, max_factor):
    return extreme(min_factor, max_factor, step = -1)


def extreme(mini, maxi, step = 1):
    if(maxi < mini):
        raise ValueError("invalid input")
    for total in range(2 * mini, 2 * maxi + 1)[::step]:
        start, stop = ((total + 1) // 2, maxi) if step < 0 else (mini, total // 2)
        for a in range(start, stop + 1):
            number = a * (total - a)
            if(is_palindrome(number)):
                a, b = (a, total - a)[::step]
                factors = [[k, number // k] for k in range(a, b + 1) if number % k == 0]
                return number, factors
    return None, []


def is_palindrome(number):
    stg = str(number)
    return stg == stg[::-1]