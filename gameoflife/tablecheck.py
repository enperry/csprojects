class tableCheck:
    def __init__(self):
        self.grid = [["A", "B", "C"],
                     ["D", "E", "F"],
                     ["G", "H", "I"],
                     ["J", "K", "L"]]

    def printGrid(self):
        for row in self.grid:
            print(row)
        