# importing random stuff
from random import randint

simulation_board = []

for x in range(20):
    simulation_board.append(["O"] * 20)

def print_board(board):
    for row in board:
        print " ".join(row)


print_board(simulation_board)
