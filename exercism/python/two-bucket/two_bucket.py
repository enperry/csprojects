def measure(bucket_one, bucket_two, goal, start_bucket):
    # initialisation
    bucket = {"one": 0, "two": 0}
    memo = {}

    # memoisation
    bucket[start_bucket] = bucket_one if start_bucket == "one" else bucket_two
    memo[f"{bucket['one']}{bucket['two']}"] = True
    if bucket["one"] == 0:
        memo[f"{bucket_one}0"] = True
    else:
        memo[f"0{bucket_two}"] = True

    # algo
    def step(n: int):
        b1, b2 = bucket["one"], bucket["two"]
        if(b1 == goal or b2 == goal):
            goal_bucket = "one" if b1 == goal else "two"
            other_bucket_level = b2 if b1 == goal else b1
            return (n, goal_bucket, other_bucket_level)
        for i in range(6):
            tmp1, tmp2 = b1, b2
            if(i == 0):
                if(b1 == bucket_one):
                    continue
                tmp1 = bucket_one
            elif(i == 1):
                if(b2 == bucket_two):
                    continue
                tmp2 = bucket_two
            elif(i == 2):
                if(b1 == 0):
                    continue
                tmp1 = 0
            elif(i == 3):
                if(b2 == 0):
                    continue
                tmp2 = 0
            elif(i == 4):
                if(b1 == 0 or b2 == bucket_two):
                    continue
                tmp1 = max(b1 + b2 - bucket_two, 0)
                tmp2 = min(b1 + b2, bucket_two)
            elif(i == 5):
                if(b2 == 0 or b1 == bucket_one):
                    continue
                tmp1 = min(b1 + b2, bucket_one)
                tmp2 = max(b1 + b2 - bucket_one, 0)
            if(memo.get(f"{tmp1}{tmp2}", False)):
                continue
            bucket["one"], bucket["two"] = tmp1, tmp2
            memo[f"{tmp1}{tmp2}"] = True
            if((result := step(n + 1)) is not None):
                return result
            bucket["one"], bucket["two"] = b1, b2
        return None
    return step(1)
