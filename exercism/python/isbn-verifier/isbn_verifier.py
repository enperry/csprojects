def is_valid(isbn):
    nums = [i for i in isbn if i.isdigit()]
    if(len(nums) == 9 and isbn[-1] in ('x', 'X')):
        nums.append(10)
    elif(len(nums) != 10):
        return False
        
    return sum((int(j) * (10 - i) for i, j in enumerate(nums))) % 11 == 0