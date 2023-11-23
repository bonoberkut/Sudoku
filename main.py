from colorama import Fore, Back
import generate_board

def successfulMove(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def boardFull(board):
    for row in board:
        if 0 in row:
            return False
    return True

def solve_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if successfulMove(board, row, col, num):
                        board[row][col] = num
                        if solve_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print( f"{Fore.RED}- - - - - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(f"{Fore.RED}|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(f"{Fore.WHITE} {str(board[i][j])}", end=" ")

def successfulMove(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def boardFull(board):
    for row in board:
        if 0 in row:
            return False
    return True


def main():
    complexityChange = input("Выберите сложность игры(легкая/средняя/джиган): ")
    if complexityChange == "легкая":
        complexityNumber = 20
    if complexityChange == "средняя":
        complexityNumber = 35
    if complexityChange == "джиган":
        complexityNumber = 50

    sudoku_board = generate_board.generate_board(complexityNumber)

    while not boardFull(sudoku_board):
        print_board(sudoku_board)

        try:
            row = int(input(Fore.GREEN + "Введите номер строки (1-9): ")) - 1
            col = int(input(Fore.GREEN + "Введите номер столбца (1-9): ")) - 1
            num = int(input(Fore.GREEN + "Введите число (1-9): "))
        except ValueError:
            print(Fore.RED + "Некорректный ввод..")
            continue

        if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
            if successfulMove(sudoku_board, row, col, num):
                sudoku_board[row][col] = num
            else:
                print(Fore.RED + "Ошибка! Вы впсиали неверные числа.")
        else:
            print(Fore.RED + "Ошибка! Вы не правильно ввели координаты.")

    print(Fore.YELLOW + "Поздравляем! Вы решили SUDOKU!")
    print_board(sudoku_board)

#Точка входа
if __name__ == "__main__":
    main()