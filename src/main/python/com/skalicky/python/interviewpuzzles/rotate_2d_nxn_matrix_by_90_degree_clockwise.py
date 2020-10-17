# Task:
#
# Given a square 2D matrix (n x n), rotate the matrix by 90 degrees clockwise.
#
# Here's an example and some starting code:
#
# def rotate(mat):
#   # Fill this in.
#
# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Looks like
# # 1 2 3
# # 4 5 6
# # 7 8 9
#
# # Looks like
# # 7 4 1
# # 8 5 2
# # 9 6 3
# print(rotate(mat))
# # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
from typing import List


def rotate(mat: List[List[int]]) -> List[List[int]]:
    matrix_size: int = len(mat)
    if matrix_size == 0:
        return []
    else:
        result: List[List[int]] = [[0 for i in range(0, matrix_size)] for j in range(0, matrix_size)]
        for i in range(0, matrix_size):
            for j in range(0, matrix_size):
                result[i][matrix_size - 1 - j] = mat[j][i]
        return result
