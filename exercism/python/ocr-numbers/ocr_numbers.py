char_map = {
    (" _ ", "| |", "|_|"): "0",
    ("   ", "  |", "  |"): "1",
    (" _ ", " _|", "|_ "): "2",
    (" _ ", " _|", " _|"): "3",
    ("   ", "|_|", "  |"): "4",
    (" _ ", "|_ ", " _|"): "5",
    (" _ ", "|_ ", "|_|"): "6",
    (" _ ", "  |", "  |"): "7",
    (" _ ", "|_|", "|_|"): "8",
    (" _ ", "|_|", " _|"): "9",
}

def convert(grid):
    if(any(len(row) % 3 != 0 for row in grid) or (len(grid) % 4 != 0)):
        raise ValueError("invalid input")
    if(len(grid) > 4):
        n = len(grid) // 4
        return ",".join(convert(grid[4 * i : 4 + 4 * i]) for i in range(n))
    
    numbers = ""

    for i in range(len(grid[0]) // 3):
        try:
            numbers = numbers + (char_map[(grid[0][i * 3 : 3 + 3 * i], grid[1][i * 3 : 3 + 3 * i], grid[2][i * 3 : 3 + 3 * i])])
        except Exception: 
            numbers = numbers + "?"

    return numbers