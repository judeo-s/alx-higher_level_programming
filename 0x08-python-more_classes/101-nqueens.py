#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """
    Checks if it is safe to place a queen at board[row][col]

    Args:
        board
        row
        col
        n
    Returns:
        True/False
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens(n, board, col, solutions):
    """
    Recursively solves the N queens problem

    Args:
        n
        board
        col
        solution
    Returms:
        None
    """
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens(n, board, col + 1, solutions)
            board[i][col] = 0


def n_queens(n):
    """
    Solves the N queens problem and print the solutions

    Args:
        n: int
    Return:
        None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for i in range(n)] for j in range(n)]
    solutions = []
    solve_n_queens(n, board, 0, solutions)
    sorted_solutions = sorted(solutions)
    for solution in sorted_solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    n_queens(n)
