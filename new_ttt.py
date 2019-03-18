# Python: Tic-Tac-Toe Game
#!/usr/bin/python


### Imports
import os
import time
import random

# Defining a header with starting information
def PrintHeader():
    os.system("clear")
    print ("""Welcome to my Tic-Tac-Toe game!
These are the corresponding numerical values for each board position:

0|1|2
-----
3|4|5
-----
6|7|8""")

# Print the current board and piece positions
def PrintBoard():
    PrintHeader()
    print ("\nCurrent game: ")
    print (m_board[0] + "|" + m_board[1] + "|" + m_board[2])
    print ("-----")
    print (m_board[3] + "|" + m_board[4] + "|" + m_board[5])
    print ("-----")
    print (m_board[6] + "|" + m_board[7] + "|" + m_board[8])

# Choose player piece X or O
def GoesFirst():
    user = input("Do you want to go first? y/n\n")
    if user == "y" or user == "Y":
        return True
    elif user == "n" or user == "N":
        return False
    else:
        print("Please choose a valid option.")
        GoesFirst()

# Choose computer difficulty
def ChooseDifficulty():
    difficulty = input("Please choose computer difficulty: 1 = EASY, 2 = INTERMEDIATE, 3 = HARD\n")
    if difficulty == "1":
        return 1
    elif difficulty == "2":
        return 3
    elif difficulty == "3":
        return 6
    else:
        print("Please choose a valid difficulty level.\n")
        ChooseDifficulty()

# Set up the game difficulty and player pieces 
def SetupGame():
    return GoesFirst(), ChooseDifficulty()
    
# Checking if given player has won with given board
def Win(board, player):
    # first row
    if board[0] == player[1] and board[1] == player[1] and board[2] == player[1]:
        return True
    # second row
    elif board[3] == player[1] and board[4] == player[1] and board[5] == player[1]:
        return True
    # last row
    elif board[6] == player[1] and board[7] == player[1] and board[8] == player[1]:
        return True
    # fist column
    elif board[0] == player[1] and board[3] == player[1] and board[6] == player[1]:
        return True
    # second column
    elif board[1] == player[1] and board[4] == player[1] and board[7] == player[1]:
        return True
    # third column
    elif board[2] == player[1] and board[5] == player[1] and board[8] == player[1]:
        return True
    # \ - diagonal
    elif board[0] == player[1] and board[4] == player[1] and board[8] == player[1]:
        return True
    # / - diagonal
    elif board[2] == player[1] and board[4] == player[1] and board[6] == player[1]:
        return True
    else:
        return False

# Checking if given board evaluates to a tie between both players
def Tie(board):
    filled = True
    for i in board:
        if i == " ":
            filled = False
    return filled

# Getting empty positions
def GetAvailableMoves(board):
    availableMoves = []
    for i, val in enumerate(board):
        if val == " ":
            # add position to list if the cell is empty
            availableMoves.append(int(i))
    return availableMoves

def EvaluateScore(board, cell_1, cell_2, cell_3):
    if board[cell_1] == m_player[1]:
        if board[cell_2] == m_player[1]:
            if board[cell_3] == m_player[1]:
                return -100
            elif board[cell_3] == m_computer[1]:
                return 0
            else:
                return -10
        elif board[cell_2] == m_computer[1]:
            return 0
        else:
            if board[cell_3] == m_player[1]:
                return -10
            elif board[cell_3] == m_computer[1]:
                return 0
            else:
                return -1
    elif board[cell_1] == m_computer[1]:
        if board[cell_2] == m_player[1]:
            return 0
        elif board[cell_2] == m_computer[1]:
            if board[cell_3] == m_player[1]:
                return 0
            elif board[cell_3] == m_computer[1]:
                return 100
            else:
                return 10
        else:
            if board[cell_3] == m_player[1]:
                return 0
            elif board[cell_3] == m_computer[1]:
                return 10
            else:
                return 1
    else:
        if board[cell_2] == m_player[1]:
            if board[cell_3] == m_player[1]:
                return -10
            elif board[cell_3] == m_computer[1]:
                return 0
            else:
                return -1
        elif board[cell_2] == m_computer[1]:
            if board[cell_3] == m_player[1]:
                return 0
            elif board[cell_3] == m_computer[1]:
                return 10
            else:
                return 1
        else:
            if board[cell_3] == m_player[1]:
                return -1
            elif board[cell_3] == m_computer[1]:
                return 1
            else: return 0

# Evaluate score of a board
def EvaluateBoard(board):
    bestScore = 0
    tmpBoard = list(board)

    # Horizontal lines
    bestScore += EvaluateScore(tmpBoard, 0, 1, 2)
    bestScore += EvaluateScore(tmpBoard, 3, 4, 5)
    bestScore += EvaluateScore(tmpBoard, 6, 7, 8)

    # Vertical lines
    bestScore += EvaluateScore(tmpBoard, 0, 3, 6)
    bestScore += EvaluateScore(tmpBoard, 1, 4, 7)
    bestScore += EvaluateScore(tmpBoard, 2, 5, 8)

    # Diagnal lines
    bestScore += EvaluateScore(tmpBoard, 0, 4, 8)
    bestScore += EvaluateScore(tmpBoard, 2, 4, 6)

    return bestScore

# Defining our computer AI
def Minimax(board, player, depth):
    # Find all available moves for given board
    tmpBoard = list(board)
    availableMoves = GetAvailableMoves(tmpBoard)

    if player[0] == True:
        bestScore = float("inf")
    else:
        bestScore = float("-inf")

    currentScore = 0
    bestMove = -1

    # Reached the end of recursion, board filled up
    if depth == 0 or availableMoves == []:
        bestScore = EvaluateBoard(tmpBoard)
    # Board not filled up yet
    else:
        # Iterate through possible moves
        for i in availableMoves:
            # Simulate move on board
            tmpBoard[i] = player[1]
            if player[0] == True:
                currentScore = Minimax(tmpBoard, m_computer, depth-1)[0]
                if currentScore < bestScore:
                    bestScore = currentScore
                    bestMove = i
            else:
                currentScore = Minimax(tmpBoard, m_player, depth-1)[0]
                if currentScore > bestScore:
                    bestScore = currentScore
                    bestMove = i
            tmpBoard[i] = " "

    return (bestScore, bestMove)

# Place given player's piece on given board, player move is input and computer move is result of minimax
def PlaceTurn(player, depth):
    # Prompt player for a move
    if player[0] == True:
        position = int(input("Select a spot: "))
        if m_board[position] == " ":
            m_board[position] = player[1]
        else:
            print("This spot is taken, please pick another spot.")
            PlaceTurn(player, depth)
    # Find best move for AI
    else:
        position = Minimax(m_board, player, depth)[1]
        m_board[position] = player[1]
        print("Placing computer piece")

def PlayGame(playerTurn, depth):
    if Win(m_board, m_player):
        return print("Player wins!\n")
    elif Win(m_board, m_computer):
        return print("Computer wins!\n")
    elif Tie(m_board):
        return print("It's a tie!\n")

    if playerTurn == True:
        print("Play Game for player")
        PlaceTurn(m_player, depth)
        PrintBoard()
        PlayGame(False, depth)
    else:
        print("Play Game for computer")
        PlaceTurn(m_computer, depth)
        PrintBoard()
        PlayGame(True, depth)

###
### Main Section
###

# Declaring the Game board, extra space at the top is to 1-index the game board
m_board = [" "," "," ",
           " "," "," ",
           " "," "," "]

PrintHeader()
m_playerTurn, m_depth = SetupGame()

if m_playerTurn == True:
    m_player = [True, "X"]
    m_computer = [False, "O"]
else:
    m_player = [True, "O"]
    m_computer = [False, "X"]

PrintBoard()
PlayGame(m_playerTurn, m_depth)