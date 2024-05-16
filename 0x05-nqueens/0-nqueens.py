#!/usr/bin/python3
"""
N queens solver
"""
import sys


def print_solution(board):
    """Print the solution."""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i] == j:
                solution.append([i, j])
    print(solution)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[x][y]."""
    for i in range(col):
        if board[i] == row or \
                board[i] - i == row - col or \
                board[i] + i == row + col:
            return False
    return True


def solve_n_queens(board, col):
    """Use backtracking to find all solutions."""
    N = len(board)
    if col == N:
        print_solution(board)
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[col] = i
            solve_n_queens(board, col + 1)


def check_input(args):
    """Check the input."""
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not args[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(args[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N


def main():
    """Solve the N queens problem."""
    N = check_input(sys.argv)
    board = [-1] * N
    solve_n_queens(board, 0)


if __name__ == "__main__":
    main()
