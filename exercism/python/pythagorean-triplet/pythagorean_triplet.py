def triplets_with_sum(number):
    return [[a, b, number - a - b] for a in range(number // 3) for b in range(a + 1, number // 2) if is_triplet([a, b, number - a - b])]

# this function isn't even used and im not quite sure what its for since its not in documentation
def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2
