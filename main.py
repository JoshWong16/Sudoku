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


def is_valid(point):
    x_coord = point[1]
    y_coord = point[0]
    
