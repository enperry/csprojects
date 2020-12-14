class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.direction_vectors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def search(self, word):
        for y in range(len(self.puzzle)):
            for x in range((len(self.puzzle[0]))):
                if(self.puzzle[y][x] != word[0]):
                    continue
                else:
                    for d in self.direction_vectors:
                        chunk = self.puzzle[y][x]
                        x2 = x
                        y2 = y
                        while True:
                            try:
                                if(chunk == word):
                                    return Point(x, y), Point(x2, y2)
                                x2 = x2 + d[0]
                                y2 = y2 + d[1]
                                chunk = chunk + self.puzzle[y2][x2]
                            except:
                                break
