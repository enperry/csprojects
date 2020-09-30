def solution(s):
    # checking for edge cases
    if(len(s) == 0):
        return 0
    elif(len(set(s)) == 1):
        return len(s)
    # the actual algo
    for i in range(0, len(s)):
        slice = s[:i]
        count = s.count(slice)
        if(len(slice) > len(s) / 2):
            return 1
        if(count * len(slice) == len(s)):
            return count
