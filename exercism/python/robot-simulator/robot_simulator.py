# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 3
SOUTH = 6
WEST = 9
 

class Robot:
    def __init__(self, direction = NORTH, x = 0, y = 0):
        self.direction = direction
        self.coordinates = (x, y)

    def move(self, stream):
        for char in stream:
            _x, _y = self.coordinates
            if(char == "R"):
                self.direction = (self.direction + 3) % 12
            elif(char == 'L'):
                self.direction = (self.direction + 9) % 12
            elif(char == 'A'):
                if(self.direction == NORTH):
                    self.coordinates = (_x, _y + 1)
                elif(self.direction == SOUTH):
                    self.coordinates = (_x, _y - 1)
                elif(self.direction == WEST):
                    self.coordinates = (_x - 1, _y)
                elif(self.direction == EAST):
                    self.coordinates = (_x + 1, _y)
            else:
                raise ValueError("Invalid command.")