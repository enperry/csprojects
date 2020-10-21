def rectangles(strings):
    n = 0
    for index in range(len(strings)):
        if("+" in strings[index]):
            for a in range(len(strings[index])):
                if(strings[index][a] == "+"):
                    opened = a
                    for c in range(a + 1, len(strings[index])):
                        if(strings[index][c] == "+"):
                            closed = c
                            for b in range(index + 1, len(strings)):
                                if(strings[b][opened] not in "+|" or strings[b][closed] not in "+|"):
                                    break
                                if(strings[b][opened] == "+" and strings[b][closed] == "+"):
                                    n = n + 1
    return n