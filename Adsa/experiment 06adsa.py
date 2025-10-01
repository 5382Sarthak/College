def print_board(board, n):
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += " Q "
            else:
                row += " . "
        print(row)
    print("\n")

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens_util(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row] = -1

def solve_nqueens(n):
    board = [-1] * n
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    print(f"Total solutions for {n}-Queens = {len(solutions)}\n")
    for sol in solutions:
        print_board(sol, n)

# Example: Solve for 6 queens
solve_nqueens(6)
