def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def solve_n_queens_util(board, row):
        if row == n:
            return True
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                if solve_n_queens_util(board, row + 1):
                    return True
                    c+=1
        return False

    board = [-1] * n
    c=0
    if solve_n_queens_util(board, 0):
        for i in range(n):
            print(" . " * board[i] + " N " + " . " * (n - board[i] - 1))
        print(c)
solve_n_queens(4)