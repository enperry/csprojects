"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    countEmpty = 0
    for row in board:
        for mark in row:
            if(mark == X):
                countX = countX + 1
            elif(mark == O):
                countO = countO + 1
            else:
                countEmpty = countEmpty + 1

    if(countEmpty == 9):
        return X
    elif(terminal(board)):
        return None
    elif(countX > countO):
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    setOfActions = set()

    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                setOfActions.add((i,j))

    return setOfActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    assert(board[i][j] == EMPTY), "Invalid action input"
    answerBoard = copy.deepcopy(board)
    nextPlayer = player(board)
    if(nextPlayer is not None):
        answerBoard[i][j] = nextPlayer
    return answerBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    assert board is not None, "Board is None"

    def isWinningDiagonal(mySet):
        for i in range(3):
            if((i, i) not in mySet):
                return False
        return True
    
    def isWinningAntiDiagonal(mySet):
        for i in range(3):
            if((i, 2-i) not in mySet):
                return False
        return True
    
    def isWinningRow(mySet):
        for i in range(3):
            winning = True
            for j in range(3):
                if((i, j) not in mySet):
                    winning = False
                    break
            else:
                return True
        return False
    
    def isWinningCol(mySet):
        for j in range(3):
            winning = True
            for i in range(3):
                if((i, j) not in mySet):
                    winning = False
                    break
            else:
                return True
        return False
              
    def is_winning(mySet):
        return isWinningRow(mySet) or isWinningCol(mySet) or isWinningDiagonal(mySet) or isWinningAntiDiagonal(mySet)
    
    cellsOfX = set()
    cellsOfO = set()
 
    for i in range(3):
        for j in range(3):
            if(board[i][j] == X):
                cellsOfX.add((i, j))
            elif(board[i][j] == O):
                cellsOfO.add((i, j))
                
    if(is_winning(cellsOfX)):
        return X
    elif(is_winning(cellsOfO)):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board)!= None):
        return True
    
    for row in board:
        for mark in row:
            if(mark == EMPTY):
                return False
            
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    try:
        assert(terminal(board))
        if(winner(board) == None):
            return 0
        elif(winner(board) == X):
            return 1
        else:
            return -1
        
    except AssertionError:
        print("Board is not terminal")
        return None


def maxValue(board, alpha, beta):
    if(terminal(board)):
        return (utility(board), None)
    winningAction = None
    score = -math.inf
    setofActions = actions(board)
    for action in setofActions:
        newScore, newMove =  minValue(result(board, action), alpha, beta)
        if(newScore > score):
            winningAction = action
            score = newScore
        alpha = max(score, alpha)
        if(alpha >= beta):
            break

    return (score, winningAction)


def minValue(board, alpha, beta):
    if(terminal(board)):
        return (utility(board), None)
    winningAction = None
    score = math.inf
    setofActions = actions(board)
    for action in setofActions:
        newScore, newMove =  maxValue(result(board, action), alpha, beta)
        if(newScore < score):
            winningAction = action
            score = newScore
        beta = min(score, beta)
        if(alpha >= beta):
            break
    return (score, winningAction)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None    
    if(player(board) == X):
        score, winningAction = maxValue(board, -math.inf, math.inf)
    elif(player(board) == O):
        score, winningAction = minValue(board, -math.inf, math.inf)
    return winningAction