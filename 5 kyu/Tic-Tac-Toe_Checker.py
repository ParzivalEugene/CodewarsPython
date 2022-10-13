def is_solved(board):
    n = len(board)
    rows = [row for row in board]
    columns = [[row[i] for row in board] for i in range(n)]
    diagonal1 = [board[i][i] for i in range(n)]
    diagonal2 = [board[i][n - i - 1] for i in range(n)]
    all_lines = [] + rows + columns + [diagonal1] + [diagonal2]
    if any(line[0] == line[1] == line[2] == 1 for line in all_lines):
        return 1
    elif any(line[0] == line[1] == line[2] == 2 for line in all_lines):
        return 2
    elif any(0 in line for line in all_lines):
        return -1
    return 0


