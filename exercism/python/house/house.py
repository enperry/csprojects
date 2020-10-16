rhymes = {
    1: " house that Jack built.",
    2: " malt that lay in the",
    3: " rat that ate the",
    4: " cat that killed the",
    5: " dog that worried the",
    6: " cow with the crumpled horn that tossed the",
    7: " maiden all forlorn that milked the",
    8: " man all tattered and torn that kissed the",
    9: " priest all shaven and shorn that married the",
    10: " rooster that crowed in the morn that woke the",
    11: " farmer sowing his corn that kept the",
    12: " horse and the hound and the horn that belonged to the"
}

def verse(i):
    return rhymes[i] + verse(i - 1) if i > 1 else rhymes[i]

def recite(start_verse, end_verse):
    return ["This is the" + verse(x) for x in range(start_verse, end_verse + 1)]