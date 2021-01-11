from itertools import combinations

def maximum_value(maximum_weight, items):
    value = 0
    for i in range(len(items), -1, -1):
        for c in combinations(items, i):
            if(sum([x["weight"] for x in c]) <= maximum_weight and (val := sum([x["value"] for x in c])) > value):
                value = val
    return value