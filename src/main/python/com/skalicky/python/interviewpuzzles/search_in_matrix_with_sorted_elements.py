# Task:
#
# Given a matrix that is organized such that the numbers will always be sorted left to right, and the first number of
# each row will always be greater than the last element of the last row (mat[i][0] > mat[i - 1][-1]), search for
# a specific value in the matrix and return whether it exists.
#
# Here's an example and some starter code.
#
# def search_in_matrix_with_sorted_elements(matrix, searched_value):
#     # Fill this in.
#
# mat = [
#     [1, 3, 5, 8],
#     [10, 11, 15, 16],
#     [24, 27, 30, 31],
# ]
#
# print(search_in_matrix_with_sorted_elements(mat, 4))
# # False
#
# print(search_in_matrix_with_sorted_elements(mat, 10))
# # True
from math import floor
from typing import List, Tuple


def convert_number_to_matrix_coordinates(number: int, column_count: int) -> Tuple[int, int]:
    row_index: int = floor(number / column_count)
    column_index: int = number % column_count
    return row_index, column_index


def search_in_matrix_with_sorted_elements(matrix: List[List[int]], searched_value: int) -> bool:
    """Time complexity ... O(log n) where *n* is the size of the given matrix. Reason: binary search in matrix
     implemented"""

    row_count: int = len(matrix)
    column_count: int = len(matrix[0])
    lower_bound_included: int = 0
    upper_bound_excluded: int = row_count * column_count
    while lower_bound_included < upper_bound_excluded:
        global_index_of_element_in_middle: int = floor((upper_bound_excluded + lower_bound_included) / 2)
        row_index_of_element_in_middle, column_index_of_element_in_middle = convert_number_to_matrix_coordinates(
            global_index_of_element_in_middle, column_count)
        element_in_middle: int = matrix[row_index_of_element_in_middle][column_index_of_element_in_middle]
        if element_in_middle == searched_value:
            return True
        elif element_in_middle > searched_value:
            upper_bound_excluded = global_index_of_element_in_middle - 1
        else:
            lower_bound_included = global_index_of_element_in_middle + 1
    return False
