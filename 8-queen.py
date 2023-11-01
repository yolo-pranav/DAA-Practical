def is_safe(board: list[list], row: int, col: int) -> bool:
    # Check in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    # All checks passed
    return True

def solve_n_queens(board: list[list], row: int) -> bool:
    n = len(board)  # Get total rows on the board.
    # End if the last row is filled.
    if row == n:
        return True
    # Check each cell for a correct solution. Backtracks until loop ends with 'return'.
    for col in range(n):
        if is_safe(board, row, col):    # Check if the cell is safe to place.
            board[row][col] = 1         # '1' means Queen can be placed.
            # Start recursion to traverse child nodes of the nodes.
            if solve_n_queens(board, row + 1):
                return True         # Break the loop with return.
            board[row][col] = 0         # '0' means empty cell.
    # End if no solution exists.
    return False

def print_board(board: list[list]) -> None:
    for row in board:
        print(" ".join(["Q" if cell == 1 else "▯" for cell in row]))

if __name__ == "__main__":
    n = int(input("Enter the size of board > "))
    board = [[0] * n for _ in range(n)]

    if solve_n_queens(board, 0):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")