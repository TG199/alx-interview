#!/usr/bin/python3
""" Rotate 2D Model"""


def rotate_2d_matrix(matrix):
    """Rotate the given n x n 2D matrix 90 degrees clockwise in-place."""
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
