import random


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end=" ")


def is_valid_move(board, row, col, num):

    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True


def solve_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def generate_board():

    board = [[0] * 9 for _ in range(9)]
    solve_board(board)

    for _ in range(20):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0

    return board


def main():
    sudoku_board = generate_board()

    while not is_board_full(sudoku_board):
        print_board(sudoku_board)

        try:
            row = int(input("Введите номер строки (1-9): ")) - 1
            col = int(input("Введите номер столбца (1-9): ")) - 1
            num = int(input("Введите число (1-9): "))
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
            continue

        if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
            if is_valid_move(sudoku_board, row, col, num):
                sudoku_board[row][col] = num
            else:
                print("Некорректное число. Попробуйте снова.")
        else:
            print("Некорректные координаты. Попробуйте снова.")

    print("Поздравляем! Вы решили головоломку!")
    print_board(sudoku_board)


if __name__ == "__main__":
    main()