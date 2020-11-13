day_and_verse = [
    ("first", "a Partridge in a Pear Tree."),
    ("second", "two Turtle Doves, and "),
    ("third", "three French Hens, "),
    ("fourth", "four Calling Birds, "),
    ("fifth", "five Gold Rings, "),
    ("sixth", "six Geese-a-Laying, "),
    ("seventh", "seven Swans-a-Swimming, "),
    ("eighth", "eight Maids-a-Milking, "),
    ("ninth", "nine Ladies Dancing, "),
    ("tenth", "ten Lords-a-Leaping, "),
    ("eleventh", "eleven Pipers Piping, "),
    ("twelfth", "twelve Drummers Drumming, ")
]

def construct_verse(n):
    day = day_and_verse[n][0]
    gift = "".join(g[1] for g in day_and_verse[n :: -1])
    return f"On the {day} day of Christmas my true love gave to me: {gift}"

def recite(start_verse, end_verse):
    return [construct_verse(n) for n in range(start_verse - 1, end_verse)]