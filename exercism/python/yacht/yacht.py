"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 15
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 10
FOUR_OF_A_KIND = 11
LITTLE_STRAIGHT = 12
BIG_STRAIGHT = 13
CHOICE = 14


def score(dice, category):
    points = 0
    if(category in range(ONES, SIXES + 1)):
        points = category * dice.count(category)
    elif(category == FULL_HOUSE):
        uniques = list(set(dice))
        if(len(uniques) == 2 and dice.count(uniques[0]) in (2,3)):
            points = sum(dice)
    elif(category == FOUR_OF_A_KIND):
        uniques = list(set(dice))
        for p in uniques:
            if(dice.count(p) >= 4):
                points = 4 * p
                break
    elif(category == LITTLE_STRAIGHT and sorted(dice) == [1,2,3,4,5]):
        points = 30
    elif(category == BIG_STRAIGHT and sorted(dice) == [2,3,4,5,6]):
        points = 30
    elif(category == CHOICE):
        points = sum(dice)
    elif(category == YACHT and len(set(dice)) == 1):
        points = 50
    else:
        points = 0
    
    return points