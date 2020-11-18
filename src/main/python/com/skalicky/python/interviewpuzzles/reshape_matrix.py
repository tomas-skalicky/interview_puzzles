# Task:
#
# Reshaping a matrix means to take the same elements in a matrix but change the row and column length. This means that
# the new matrix needs to have the same elements filled in the same row order as the old matrix. Given a matrix,
# a new row size x and a new column size y, reshape the matrix. If it is not possible to reshape, return None.
#
# Here's an example and some starter code.
#
# def reshape_matrix(mat, x, y):
#   # Fill this in.
#
# print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# # [[1], [2], [3], [4]]
#
# print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# # None
from math import floor
from typing import List, Optional


def reshape_matrix(matrix: List[List[object]], new_row_size: int, new_column_size: int) -> Optional[List[List[object]]]:
    old_row_size: int = len(matrix)
    old_column_size: int = len(matrix[0])
    if old_row_size * old_column_size != new_row_size * new_column_size:
        return None
    else:
        new_matrix: List[List[object]] = [[None] * new_column_size for i in range(0, new_row_size)]
        for i in range(0, old_row_size):
            for j in range(0, old_column_size):
                current_element: object = matrix[i][j]
                current_index: int = i * old_row_size + j
                new_row_index: int = floor(current_index / new_column_size)
                new_column_index: int = current_index % new_column_size
                new_matrix[new_row_index][new_column_index] = current_element
        return new_matrix
