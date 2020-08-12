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
    
    def checkNeighbor(self, checkRow, checkCol):
        searchMin = -1
        searchMax = 2

        neighborList = []
        for row in range(searchMin, searchMax):
            for col in range(searchMin, searchMax):
                neighborRow = checkRow + row
                neighborCol = checkCol + col

                validNeighbor = True

                if((neighborRow) == checkRow and (neighborCol) == checkCol):
                    validNeighbor = False
                elif((neighborRow) < 0 or (neighborRow) >= self.rows):
                    validNeighbor = False
                elif((neighborCol) < 0 or (neighborCol) >= self.columns):
                    validNeighbor = False

                if(validNeighbor == True):
                    neighborList.append(self.grid[neighborRow][neighborCol])
                    
        return neighborList

    def updateBoard(self):
        goesAlive = []
        getsKilled = []

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                checkNeighbor = self.checkNeighbor(row, col)

                livingNeighborsCount = []

                for neighborCell in checkNeighbor:
                    if(neighborCell.isAlive()):
                        livingNeighborsCount.append(neighborCell)
                
                cellObject = self.grid[row][col]
                statusMainCell = cellObject.isAlive()

                if(statusMainCell == True):
                    if(len(livingNeighborsCount) < 2 or len(livingNeighborsCount) > 3):
                        getsKilled.append(cellObject)

                    if(len(livingNeighborsCount) == 3 or len(livingNeighborsCount) == 2):
                        goesAlive.append(cellObject)

                else:
                    if(len(livingNeighborsCount) == 3):
                        goesAlive.append(cellObject)
        
        for cellItems in goesAlive:
            cellItems.setLive()

        for cellItems in getsKilled:
            cellItems.setDead