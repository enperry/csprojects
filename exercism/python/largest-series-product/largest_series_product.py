from functools import reduce
from operator import mul

def largest_product(series, size):
    if(size < 0):
        raise ValueError(size)

    chunks = (series[i:i + size] for i in range(0, len(series) + 1 - size))

    def score(chunk):
        return reduce(mul, map(int, chunk), 1)

    return max(map(score, chunks))