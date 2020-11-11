# Task:
#
# Given a matrix, transpose it. Transposing a matrix means the rows are now the column and vice-versa.
#
# Here's an example:
#
# def transpose(mat):
#   # Fill this in.
#
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
#
# print(transpose(mat))
# # [[1, 4],
# #  [2, 5],
# #  [3, 6]]
from typing import List, Optional


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    initial_row_count: int = len(matrix)
    initial_column_count: int = len(matrix[0])
    output_matrix: List[List[Optional[int]]] = [[None] * initial_row_count for i in range(0, initial_column_count)]
    for i in range(0, initial_row_count):
        for j in range(0, initial_column_count):
            output_matrix[j][i] = matrix[i][j]
    return output_matrix
