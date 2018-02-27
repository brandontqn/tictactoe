# Python: Tic-Tac-Toe Game
#!/usr/bin/python
# Imports
import os
import time
import random

# Defining the Game board
board = [" ",
         " "," "," ",
         " "," "," ",
         " "," "," "]

# Defining a header with starting information
def print_header():
    print ("""Welcome to my Tic-Tac-Toe game!
These are the corresponding numerical values for each board position:

1|2|3
-----
4|5|6
-----
7|8|9

Player is X and the computer is O.
""")

# Defining our board
def print_board():
    print ("Current game: ")
    print (board[1] + "|" + board[2] + "|" + board[3])
    print ("-----")
    print (board[4] + "|" + board[5] + "|" + board[6])
    print ("-----")
    print (board[7] + "|" + board[8] + "|" + board[9])

# Defining win conditions
def win(board, player):
    if board[1] == player[1] and board[2] == player[1] and board[3] == player[1]:
        return True
    elif board[1] == player[1] and board[5] == player[1] and board[9] == player[1]:
        return True
    elif board[1] == player[1] and board[4] == player[1] and board[7] == player[1]:
        return True
    elif board[3] == player[1] and board[5] == player[1] and board[7] == player[1]:
        return True
    elif board[3] == player[1] and board[6] == player[1] and board[9] == player[1]:
        return True
    elif board[4] == player[1] and board[5] == player[1] and board[6] == player[1]:
        return True
    elif board[7] == player[1] and board[8] == player[1] and board[9] == player[1]:
        return True
    else:
        return False

def tie(board):
    if board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " ":
        return True
    else:
        return False

# Getting empty positions
def get_available_moves(thisBoard):
    available_moves = [None]
    for i, val in enumerate(thisBoard):
        if val == " ":
            # add position to list if the cell is empty
            available_moves.append(i)
    return available_moves

# Evaluate score of a board
def evaluate(thisBoard):
    bestScore = 0
    currentBoard = list(thisBoard)

    # Horizontal lines
    bestScore += evaluateScore(currentBoard, 1, 2, 3)
    bestScore += evaluateScore(currentBoard, 4, 5, 6)
    bestScore += evaluateScore(currentBoard, 7, 8, 9)

    # Vertical lines
    bestScore += evaluateScore(currentBoard, 1, 4, 7)
    bestScore += evaluateScore(currentBoard, 2, 5, 8)
    bestScore += evaluateScore(currentBoard, 3, 6, 9)

    # Diagnal lines
    bestScore += evaluateScore(currentBoard, 1, 5, 9)
    bestScore += evaluateScore(currentBoard, 3, 5, 7)

    return bestScore

def evaluateScore(thisBoard, cell_1, cell_2, cell_3):
    bestScore = 0

    # bestScore = 1, if line starts with "O"
    # bestScore = -1, if line starts with "X"
    if thisBoard[cell_1] == "O":
        bestScore = 1
    elif thisBoard[cell_1] == "X":
        bestScore = -1

    # bestScore times 10 if 2nd piece in the line matches 1st piece
    if thisBoard[cell_2] == "O":
        if bestScore == 1:
            bestScore = 10
        elif bestScore == -1:
            return 0
        else:
            bestScore = 1
    elif thisBoard[cell_2] == "X":
        if bestScore == -1:
            bestScore = -10
        elif bestScore == 1:
            return 0
        else:
            bestScore = -1

    #bestScore times 10 again if 3rd piece matches 2nd and 1st pieces
    if thisBoard[cell_3] == "O":
        if bestScore > 0:
            bestScore *= 10
        elif bestScore < 0:
            return 0
        else:
            bestScore = 1
    elif thisBoard[cell_3] == "X":
        if bestScore < 0:
            bestScore *= 10
        elif bestScore < 0:
            return 0
        else:
            bestScore = -1

    return bestScore

# Defining our computer AI
def minimax(thisBoard, player, depth):
    # Find all available moves for given board
    newBoard = list(thisBoard)
    available_moves = get_available_moves(newBoard)

    # Makes board positions range from 1-9 instead of 0-8
    del available_moves[0]

    bestScore = 0
    if player[0] == "Player":
        bestScore = float("-inf")
    else:
        bestScore = float("inf")

    currentScore = 0
    bestMove = -1

    # Reached the end of recursion, board filled up
    if not available_moves or depth == 0:
        bestScore = evaluate(newBoard)
    # Board not filled up yet
    else:
        # Iterate through possible moves
        for move in available_moves:
              # Simulate move on board
              newBoard[move] = player[1]
              # After Player moves, determine best move for AI
              if player[0] == "Player":
                  if player[1] == "O":
                      currentScore = minimax(newBoard, ["AI", "X"], depth-1)[0]
                      if currentScore > bestScore:
                          bestScore = currentScore
                          bestMove = move
                  else:
                      currentScore = minimax(newBoard, ["AI", "O"], depth-1)[0]
                      if currentScore < bestScore:
                          bestScore = currentScore
                          bestMove = move
                  # Reset board after simulation
                  newBoard[move] = " "
              # After AI moves, determine best move for Player
              else:
                  if player[1] == "X":
                      currentScore = minimax(newBoard, ["Player", "O"], depth-1)[0]
                      if currentScore > bestScore:
                          bestScore = currentScore
                          bestMove = move
                  else:
                      currentScore = minimax(newBoard, ["Player", "X"], depth-1)[0]
                      if currentScore < bestScore:
                          bestScore = currentScore
                          bestMove = move
                  newBoard[move] = " "

    return (bestScore, bestMove)

def placeTurn(board, player):
    # Prompt player for a move
    if player[0] == "Player":
        position = input("Select a spot: ")
        position = int(position)
        if board[position] == " ":
            board[position] = player[1]
            os.system("clear")
            print_board()
        else:
            print("This spot is taken, please pick another spot.")
            placeTurn(board, player)
    # Find best move for AI
    else:
        position = minimax(board, player, 4)[1]
        board[position] = player[1]


### Main Section
user = input("Please choose whether you want to be X or O: ")
if user == "X" or user == "x":
    player = ["Player", "X"]
    computer = ["AI", "O"]
else:
    player = ["Player", "O"]
    computer = ["AI", "X"]

turn = 10
while turn >= 0:
    os.system("clear")

    print_header()

    print_board()

    placeTurn(board, player)

    if win(board, player):
        os.system("clear")
        print_header()
        print_board()
        print("Player wins!")
        turn = -1
    elif win(board, computer):
        os.system("clear")
        print_header()
        print_board()
        print("Computer wins!")
        turn = -1
    elif tie(board):
        os.system("clear")
        print_header()
        print_board()
        print("It's a tie!")
        turn = -1
    else:
        placeTurn(board, computer)
        print_board()
        if win(board, player):
            os.system("clear")
            print_header()
            print_board()
            print("Player wins!")
            turn = -1
        elif win(board, computer):
            os.system("clear")
            print_header()
            print_board()
            print("Computer wins!")
            turn = -1
        elif tie(board):
            os.system("clear")
            print_header()
            print_board()
            print("It's a tie!")
            turn = -1
        turn -= 2
