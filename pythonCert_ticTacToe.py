# Scenario
# Your task is to write a simple program which pretends to play tic-tac-toe with the user.
# To make it all easier for you, we've decided to simplify the game. Here are our assumptions:
#
# the computer (i.e., your program) should play the game using 'X's;
# the user (e.g., you) should play the game using 'O's;
# the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
# all the squares are numbered row by row starting with 1 (see the example session below for reference)
# the user inputs their move by entering the number of the square they choose − the number must be valid,
# i.e., it must be an integer, it must be greater than 0 and less than 10,
# and it cannot point to a field which is already occupied;
# the program checks if the game is over − there are four possible verdicts:
# the game should continue, the game ends with a tie, you win, or the computer wins;
# the computer responds with its move and the check is repeated;
# don't implement any form of artificial intelligence
# − a random field choice made by the computer is good enough for the game.
# The example session with the program may look as follows:
#
# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 1
# +-------+-------+-------+
# |       |       |       |
# |   O   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 8
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 4
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 7
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# You won!
#
# Requirements
# Implement the following features:
#
# the board should be stored as a three-element list, while each element is another three-element list
# (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:
#
# board[row][column]
#
#
# each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number
# (such a square is considered free)
# the board's appearance should be exactly the same as the one presented in the example.
# implement the functions defined for you in the editor.
#
# Drawing a random integer number can be done by utilizing a Python function called randrange().
# The example program below shows how to use it (the program prints ten random numbers from 0 to 8).
#
# Note: the from-import instruction provides access to the randrange function
# defined within an external Python module callled random.
#
# from random import randrange
#
# for i in range(10):
#     print(randrange(8))

import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in range(0, 13):
        for col in range(0, 25):
            if row % 4 == 0 and col % 8 == 0:
                print("+", end='')
            elif row % 4 == 0 and col % 8 != 0:
                print("-", end='')
            elif row % 4 != 0 and col % 8 == 0:
                print("|", end='')
            elif row % 2 == 0 and col % 4 == 0:
                print(board[row // 4][col // 8], end='')
            else:
                print(" ", end='')
        print("")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        data = int(input("Enter your move: "))
        if data not in range(1, 11):
            print("Invalid number... ")
        else:
            row = (data - 1) // 3
            col = (data - 1) % 3
            if board[row][col] not in ["X", "O"]:
                board[row][col] = 'O'
                break
            else:
                print("Invalid move...")
    return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X", "O"]:
                free_squares.append((row, col))
    return free_squares


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        elif board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    L = make_list_of_free_fields(board)
    row, col = random.choice(L)
    board[row][col] = 'X'
    return board

board = [[x + i for x in range(1, 4)] for i in [0, 3, 6]]
board[1][1] = 'X'

while True:
    display_board(board)
    moves = make_list_of_free_fields(board)
    if len(moves) == 0:
        print("Draw")
        break
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("You won!")
        break
    draw_move(board)
    if victory_for(board, 'X'):
        display_board(board)
        print("You loose...")
        break



