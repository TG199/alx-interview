#!/usr/bin/env python3
"""A simple Nqueens implementation"""
import sys


def is_safe(board, row, col, n):
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


def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        if col >= n:
            solution = [[i, row.index(1)] for i, row in enumerate(board)]
            solutions.append(solution)
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
