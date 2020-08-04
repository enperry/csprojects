from cell import Cell
from random import randint

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell() for columnCells in range(self.columns)] for rowCells in range(self.rows)]
        self.generateBoard()

    def drawBoard(self):
        print("\n"*10)
        print("printing board...")
        for row in self.grid:
            for col in row:
                print(col.getPrintCharacter(), end = "")
        print()

    def generateBoard(self):
        for row in self.grid:
            for col in row:
                chanceNumber = randint(0, 2)
                if(chanceNumber == 0):
                    col.setLive()

    def checkNeighbors(self):
        