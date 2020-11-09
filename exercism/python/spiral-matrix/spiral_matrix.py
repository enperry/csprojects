from itertools import cycle

def spiral_matrix(size):
    spiral = [[None] * size for _ in range(size)]
    directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    x,y = 0,0
    dx, dy = next(directions)

    for i in range(1, size ** 2 + 1):
        spiral[x][y] = i
        if(x + dx == size or y + dy == size or spiral[x + dx][y + dy]):     
            dx, dy = next(directions)
        x, y = x + dx, y + dy

    return spiral