from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # base knowledge
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),

    # logic
    # technically i could use biconditionals - although this is longer it's easier to understand
    # if a's a knight, both must be true (we know that this can't be true, though!)
    Implication(AKnight, And(AKnight, AKnave)),
    # if a's a knave, both cannot be true. therefore, a is a knave
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # base knowledge
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),

    # logic, same thing about biconditionals
    # if a is a knight, both of them are knaves. but isn't this a contradiction since a is supposedly a knight?!
    Implication(AKnight, And(AKnave, BKnave)),
    # if a is a knave, it is false that both are knaves. 
    Implication(AKnave, Not(And(AKnave, BKnave)))
    # since we now know that a is a knave, b must be a knight.
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # base knowledge
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    # logic. again, thing about biconditionals
    # i'd elaborate but this is kind of self-explanatory
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave))))
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # base knowledge
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    Implication(CKnight, Not(CKnave)),
    Implication(CKnave, Not(CKnight)),
    # logic. for a final time thing about biconditionals
    # if b is a knight, and if a said that they are a knave, a must be a knight. opposite is true
    Implication(BKnight, And(Implication(AKnight, AKnave), Implication(AKnave, AKnight))),
    # if b is a knave, a must be a knight. anything they say is true
    Implication(BKnave, And(Implication(AKnight, AKnight), Implication(AKnave, AKnave))),
    # if b is a knight, then c is a knave.
    Implication(BKnight, CKnave),
    # if b is a knave, then c is a knight.
    Implication(BKnave, CKnight),
    # if c is a knight, then a is a knight.
    Implication(CKnight, AKnight),
    # if c is a knave, then a is a knave.
    Implication(CKnave, AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
