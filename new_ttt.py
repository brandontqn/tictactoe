# Python: Tic-Tac-Toe Game
#!/usr/bin/python


### Imports
import os
import time
import random

# Declaring the Game board, extra space at the top is to 1-index the game board
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
              7|8|9""")

# Print the current board and piece positions
def print_board():
    print ("Current game: ")
    print (board[1] + "|" + board[2] + "|" + board[3])
    print ("-----")
    print (board[4] + "|" + board[5] + "|" + board[6])
    print ("-----")
    print (board[7] + "|" + board[8] + "|" + board[9])

# Choose player piece X or O
def goes_first():
    user = input("Do you want to go first? y/n")
    if user == "y" or user == "Y":
        return True
    elif user == "n" or user == "N":
        return False
    else:
        print("Please choose a valid option.")
        goes_first()

# Choose computer difficulty
def choose_difficulty():
    difficulty = input("Please choose computer difficulty: 1 = EASY, 2 = INTERMEDIATE, 3 = HARD")
    if difficulty == "1":
        return 2
    elif difficulty == "2":
        return 4
    elif difficulty == "3":
        return 6
    else:
        print("Please choose a valid difficulty level.")
        choose_difficulty()

# Set up the game difficulty and player pieces 
def setup_game():
    return goes_first(), choose_difficulty()
    
# Checking if given player has won with given board
def win(board, player):
    # first row
    if board[1] == player[1] and board[2] == player[1] and board[3] == player[1]:
        return True
    # second row
    elif board[4] == player[1] and board[5] == player[1] and board[6] == player[1]:
        return True
    # last row
    elif board[7] == player[1] and board[8] == player[1] and board[9] == player[1]:
        return True
    # fist column
    elif board[1] == player[1] and board[4] == player[1] and board[7] == player[1]:
        return True
    # second column
    elif board[2] == player[1] and board[5] == player[1] and board[8] == player[1]:
        return True
    # third column
    elif board[3] == player[1] and board[6] == player[1] and board[9] == player[1]:
        return True
    # \ - diagonal
    elif board[1] == player[1] and board[5] == player[1] and board[9] == player[1]:
        return True
    # / - diagonal
    elif board[3] == player[1] and board[5] == player[1] and board[7] == player[1]:
        return True

# Checking if given board evaluates to a tie between both players
def tie(board):
    if (not win(board, player[0]) and not win(board, player[1])):
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

def evaluateScore(thisBoard, cell_1, cell_2, cell_3):
    # bestScore = 1, if line starts with "O"
    # bestScore = -1, if line starts with "X"
    if thisBoard[cell_1] == "O":
        bestScore = 1
    elif thisBoard[cell_1] == "X":
        bestScore = -1
    else:
        bestScore = 0

    # bestScore times 10 if 2nd piece in the line matches 1st piece
    if thisBoard[cell_2] == "O":
        if bestScore == 1:
            bestScore *= 10
        elif bestScore == -1:
            bestScore =  0
        else:
            bestScore = 1
    elif thisBoard[cell_2] == "X":
        if bestScore == -1:
            bestScore *= 10
        elif bestScore == 1:
            bestScore =  0
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
        elif bestScore > 0:
            return 0
        else:
            bestScore = -1

    return bestScore

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

# Defining our computer AI
def minimax(thisBoard, player, depth):
    # Find all available moves for given board
    newBoard = list(thisBoard)
    available_moves = get_available_moves(newBoard)

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
              move = int(move)
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

# Place given player's piece on given board, player move is input and computer move is result of minimax
def placeTurn(board, player, depth):
    # Prompt player for a move
    if depth == None:
        position = int(input("Select a spot: "))
        if board[position] == " ":
            board[position] = player[1]
            os.system("clear")
            print_board()
        else:
            print("This spot is taken, please pick another spot.")
            placeTurn(board, player, depth)
    # Find best move for AI
    else:
        position = minimax(board, player, depth)[1]
        board[position] = player[1]

def play_game(player, computer, playerTurn, depth):
    while True:
        os.system("clear")
        print_header()
        print_board()

        if win(board, player):
            os.system("clear")
            print_header()
            print_board()
            print("Player wins!")
            break
        elif win(board, computer):
            os.system("clear")
            print_header()
            print_board()
            print("Computer wins!")
            break
        elif tie(board):
            os.system("clear")
            print_header()
            print_board()
            print("It's a tie!")
            break
    
        if playerTurn == True:
            placeTurn(board, player, depth)
            print_board()
            playerTurn = False
        else:
            placeTurn(board, computer, depth)
            print_board()
            playerTurn = True

### Main Section
print_header()
playerTurn, depth = setup_game()

if playerTurn == True:
    player = ["Player", "X"]
    computer = ["AI", "O"]
    play_game(player, computer, playerTurn, depth)
else:
    player = ["Player", "O"]
    computer = ["AI", "X"]
    play_game(player, computer, playerTurn, depth)