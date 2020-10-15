def annotate(minefield):
    if(not all(len(i) == len(minefield[0]) for i in minefield)):
        raise ValueError("all strings should be equal length")
    result = []
    for y, line in enumerate(minefield):
        temp = ""
        for x, char in enumerate(line):
            if(char == " "):
                temp = temp + str(count_position(minefield, x, y))
            elif(char == "*"):
                temp = temp + char
            else:
                raise ValueError("Invalid character in strings")
        result.append(temp)
    return result


def count_position(minefield, x, y):
    x1 = max(x - 1, 0)
    y1 = max(y - 1, 0)
    x2 = min(x + 1, len(minefield[y]))
    y2 = min(y + 1, len(minefield))
    result = str("".join([x[x1 : x2 + 1] for x in minefield[y1 : y2 + 1]]).count("*"))
    if(result == "0"):
        result = " "
    return result