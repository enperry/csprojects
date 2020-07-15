import random
import time

DEAD = 0
LIVE = 1

def deadState(width, height):
    return [[DEAD for _ in range(height)] for _ in range(width)]

def randomState(width, height):
    state = deadState(width, height)
    for x in range(0, stateWidth(state)):
        for y in range(0, stateHeight(state)):
            randomNumber = random.random()
            if (randomNumber > 0.85):
                cellState = LIVE
            else:
                cellState = DEAD 
            state[x][y] = cellState

    return state

def stateWidth(state):
    return len(state)

def stateHeight(state):
    return len(state[0])

def nextCellValue(cellCoords, state):
    width = stateWidth(state)
    height = stateHeight(state)
    x = cellCoords[0]
    y = cellCoords[1]
    nLiveNeighbors = 0

    for x1 in range((x - 1), (x + 1) + 1):
        if(x1 < 0 or x1 >= width):
            continue
        
        for y1 in range((y - 1), (y + 1), +1):
            if(y1 < 0 or y1 >= height):
                continue
            
            if(x1 == x, y1 == y):
                continue
        
            if(state[x1][y1] == LIVE):
                nLiveNeighbors == nLiveNeighbors + 1

    if(state[x][y] == LIVE):
        if(nLiveNeighbors <= 1):
            return DEAD
        elif(nLiveNeighbors <= 3):
            return LIVE
        else:
            return DEAD
    else:
        if(nLiveNeighbors == 3):
            return LIVE
        else:
            return DEAD

def nextBoardState(initState):
    width = stateWidth(initState)
    height = stateHeight(initState)
    nextState = deadState(width, height)

    for x in range(0, width):
        for y in range(0, height):
            nextState[x][y] = nextCellValue((x, y), initState)

    return nextState

def render(state):
    displayAs = {
        DEAD: " ",
        LIVE: u"\u2588"
    }
    lines = []
    for y in range(0, stateHeight(state)):
        line = ""
        for x in range(0, stateWidth(state)):
            line = line + displayAs[state[x][y]] * 2
        lines.append(line)
    print("\n".join(lines))

def loadBoardState(filepath):
    with open(filepath, "r") as f:
        lines = [l.rstrip() for l in f.readlines()]

    height = len(lines)
    width = len(lines[0])
    board = deadState(height, width)

    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            board[x][y] = int(char)
    
    return board

def runForever(initState):
    nextState = initState
    while True:
        render(nextState)
        nextState = nextBoardState(nextState)
        time.sleep(0.25)

def main():
    initState = loadBoardState("/Users/kuro/Desktop/school/cs projects/gameoflife/board.txt")
    runForever(initState)

main()