class Queen:
    def __init__(self, row, column):
        if(row not in range(0, 8) or column not in range(0, 8)):
            raise ValueError("out of bounds")

        self.x = row
        self.y = column

    def can_attack(self, another_queen):
        if(self.x == another_queen.x and self.y == another_queen.y):
            raise ValueError("same spot")
        # x-axis, y-axis, diagonal respectively
        return self.x == another_queen.x or self.y == another_queen.y or abs(another_queen.x - self.x) == abs(another_queen.y - self.y)