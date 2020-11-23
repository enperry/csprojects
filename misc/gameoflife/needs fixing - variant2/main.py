from board import Board

def main():
    userRows = int(input("how many rows? "))
    userCols = int(input("how many columns? "))

    gameOfLifeBoard = Board(userRows, userCols)
    gameOfLifeBoard.drawBoard()

    userAction = ""
    while(userAction != "q"):
        userAction = input("press enter to add a generation, or q to quit. ")

        if(userAction == ""):
            gameOfLifeBoard.updateBoard()
            gameOfLifeBoard.drawBoard()

main()