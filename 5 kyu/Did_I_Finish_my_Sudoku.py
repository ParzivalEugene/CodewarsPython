def done_or_not(board):
    squares = []
    for i in range(3):
        for j in range(3):
            square = [board[i * 3 + k][j * 3: j * 3 + 3] for k in range(3)]
            squares.append(set(square[0] + square[1] + square[2]))

    lines = [set(line) for line in board]
    columns = [{line[i] for line in board} for i in range(9)]
    return "Finished!" if all(set(range(1, 10)) == i for i in squares + lines + columns) else "Try again!"


sudoku = [
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 9, 8, 2, 6, 1, 3, 7, 5],
    [7, 5, 6, 3, 8, 4, 2, 1, 9],
    [6, 4, 3, 1, 5, 8, 7, 9, 2],
    [5, 2, 1, 7, 9, 3, 8, 4, 6],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [2, 1, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 5, 8, 1, 7, 9, 2, 4],
    [8, 7, 9, 6, 4, 2, 1, 5, 3]
]
print(done_or_not(sudoku))
