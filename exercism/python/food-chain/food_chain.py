def recite(start_verse, end_verse):
    animals = ["horse", "cow", "goat", "dog", "cat", "bird", "spider", "fly"]
    consequence = ["She's dead, of course!", "I don't know how she swallowed a cow!", "Just opened her throat and swallowed a goat!", "What a hog, to swallow a dog!", "Imagine that, to swallow a cat!", "How absurd to swallow a bird!", "It wriggled and jiggled and tickled inside her.", "I don't know why she swallowed the fly. Perhaps she'll die."]
    results = []
    for i in range(start_verse, end_verse + 1):
        if(i == 8):
            results.append("I know an old lady who swallowed a {}.".format(animals[0]))
            results.append(consequence[0])
        else:
            results.append("I know an old lady who swallowed a {}.".format(animals[len(animals) - i]))
            results.append(consequence[len(consequence) - i])
            if(i > 1):
                for j in range(len(animals)-i, len(animals) - 1):
                    if(animals[j+1] == "spider"):
                        results.append("She swallowed the {} to catch the {} that {}".format(animals[j], animals[j + 1], consequence[j + 1][3 : ]))
                    else:
                        results.append("She swallowed the {} to catch the {}.".format(animals[j], animals[j + 1]))
                results.append(consequence[-1])
        results.append("")
    results.pop()
    return results
