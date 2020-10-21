from itertools import permutations as P

NATIONALITIES = 'Norwegian Englishman Ukrainian Spaniard Japanese'.split()
X = range(5)

WATER, ZEBRA = next(
    (water, zebra)
    for (red, green, ivory, yellow, blue) in P(X)
    if(green - ivory == 1)

    for (norway, english, ukraine, spain, japan) in P(X)
    if(all((norway == 0, english == red)))

    for (dog, fox, snails, horse, zebra) in P(X)
    if(spain == dog)

    for (coffee, tea, milk, orange, water) in P(X)
    if(all((coffee == green, ukraine == tea, milk == 2)))

    for (oldgold, kools, chesterfield, luckystrike, parliaments) in P(X)
    if(all((
        oldgold == snails, kools == yellow, parliaments == japan,
        abs(chesterfield - fox) == abs(kools - horse) == abs(norway - blue) == 1,
        luckystrike == orange
    ))))


def drinks_water():
    return NATIONALITIES[WATER]


def owns_zebra():
    return NATIONALITIES[ZEBRA]