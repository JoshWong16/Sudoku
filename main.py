sample_board = [
    [0, 0, 0, 0, 0, 3, 7, 0, 0],
    [0, 0, 0, 0, 8, 4, 0, 0, 0],
    [5, 4, 8, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 6, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 9, 1, 0, 7, 0, 2, 0],
    [1, 8, 6, 0, 0, 0, 3, 0, 0],
    [0, 7, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 9, 0, 0, 0, 1]
]

sample_board_solution = [
    [6, 9, 1, 5, 2, 3, 7, 4, 8],
    [7, 2, 3, 9, 8, 4, 6, 1, 5],
    [5, 4, 8, 7, 6, 1, 2, 3, 9],
    [3, 1, 7, 6, 5, 2, 9, 8, 4],
    [2, 5, 4, 8, 3, 9, 1, 6, 7],
    [8, 6, 9, 1, 4, 7, 5, 2, 3],
    [1, 8, 6, 4, 7, 5, 3, 9, 2],
    [9, 7, 2, 3, 1, 8, 4, 5, 6],
    [4, 3, 5, 2, 9, 6, 8, 7, 1]
]


def print_board(board):
    for row in range(len(board)):
        line_to_print = ""
        for col in range(len(board)):
            line_to_print += str(sample_board[row][col]) + " "
            if col % 3 == 2 and col != 8:
                line_to_print += "| "
        print(line_to_print)
        if row % 3 == 2 and row != 8:
            print("- - - - - - - - - - - -")


def find_empty_space(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row, col)


def is_valid(point, board):
    x_coord = point[1]
    y_coord = point[0]
    value = board[y_coord][x_coord]
    for col in range(len(board)):
        if board[y_coord][col] == value and col != x_coord:
            return False

    for row in range(len(board)):
        if board[row][x_coord] == value and row != y_coord:
            return False

    x_block = x_coord // 3
    y_block = y_coord // 3
    for row in range(y_block, y_coord + 3):
        for col in range(x_block, x_block + 3):
            if board[row][col] == value and row != y_coord and col != x_coord:
                return False

    return True



