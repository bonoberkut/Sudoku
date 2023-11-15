import random
from main import solve_board


def generate_board():
    board = [[0] * 9 for _ in range(9)]
    solve_board(board)

    for _ in range(20):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0

    return board