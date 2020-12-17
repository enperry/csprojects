BLACK, WHITE, NONE = "B", "W", ""
ADJACENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.height = len(self.board)
        self.width = len(self.board[0])
        self.mapping = {WHITE: set(), BLACK: set(), NONE: set()}

    def territory(self, x, y):
        if(not self.on_board(x, y)):
            raise ValueError("coordinates out of range")
        if(self.board[y][x] in (BLACK, WHITE)):
            return "", set()

        adjacents = self.adjacents(x, y)
        visited, stones, colors = {(x, y)}, set(), set()

        while(adjacents):
            x, y = adjacents.pop()
            stone = self.board[y][x]
            if(stone == " "):
                visited.add((x, y))
                adjacents = adjacents | (self.adjacents(x, y) - visited - stones)
            else:
                stones.add((x, y))
                colors.add(stone)

        if(len(colors) != 1):
            return NONE, visited

        return colors.pop(), visited

    def territories(self):
        coordinates = {(x, y) for x in range(self.width) for y in range(self.height)}

        while coordinates:
            i, j = coordinates.pop()
            owner, own = self.territory(i, j)
            self.mapping[owner] = self.mapping[owner] | own
            coordinates = coordinates - own

        return self.mapping
    
    def on_board(self, x, y):
        return x in range(self.width) and y in range(self.height)

    def adjacents(self, x, y):
        candidates = [(x + dx, y + dy) for dx, dy in ADJACENTS]
        return {(x, y) for (x, y) in candidates if self.on_board(x, y)}
        