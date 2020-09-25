def sum_of_multiples(limit, multiples):
    return sum({x for v in multiples if(v != 0) for x in range(v, limit, v)})
