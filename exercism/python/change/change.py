from itertools import combinations_with_replacement

def find_fewest_coins(coins, target):
    if(target == 0):
        return []
    if(target < min(coins)):
        raise ValueError("invalid target")
    
    for i in range(1, target // min(coins) + 1):
        for c in combinations_with_replacement(coins, i):
            if(sum(c) == target):
                return list(c)

    raise ValueError("not possible")