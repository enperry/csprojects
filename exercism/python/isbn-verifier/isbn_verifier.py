def is_valid(isbn):
    isbn = list(isbn)
    for char in isbn:
        if(char == "-"):
            isbn.remove(char)
        if(char.index != 9 and char == "X"):
            return "Invalid ISBN"

    if(isbn[9] == "X"):
        isbn[9] = 10
    isbn = [int(i) for i in isbn]
    
    return (((isbn[0] * 10) + (isbn[1] * 9) + (isbn[2] * 8) + (isbn[3] * 7) + (isbn[4] * 6) + (isbn[5] * 5) + (isbn[6] * 4) + (isbn[7] * 3) + (isbn[8] * 2) + (isbn[9] * 1)) % 11)