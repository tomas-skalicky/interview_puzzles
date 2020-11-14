# Task:
#
# You are given a 2D array of characters, and a target string. Return whether or not the word target word exists
# in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom
# in the matrix.
#
# Example:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
#
# Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down
# in the first column.
#
# Here's the function signature:
#
# def word_search(matrix, word):
#   # Fill this in.
#
# matrix = [
#   ['F', 'A', 'C', 'I'],
#   ['O', 'B', 'Q', 'P'],
#   ['A', 'N', 'O', 'B'],
#   ['M', 'A', 'S', 'S']]
# print word_search(matrix, 'FOAM')
# # True
from typing import List, Set


def find_string_in_2d_matrix(matrix: List[List[str]], searched_string: str) -> bool:
    if len(searched_string) == 0:
        return True
    else:
        row_count = len(matrix)
        if row_count == 0:
            return False
        else:
            column_count = len(matrix[0])
            if column_count == 0:
                return False
            else:
                all_strings_in_matrix: Set[str] = set()

                # Time complexity ... O(n ^ 2) where n is the size of matrix
                for row_index in range(0, row_count):
                    all_strings_in_matrix.add(''.join(matrix[row_index][:]))

                # Time complexity ... O(n ^ 2) where n is the size of matrix
                for column_index in range(0, column_count):
                    column_string = ''
                    for row_index in range(0, row_count):
                        column_string += matrix[row_index][column_index]
                    all_strings_in_matrix.add(column_string)

                # Time complexity ... O(n ^ 3) due to the complexity of str.__contains__
                for string_in_matrix in all_strings_in_matrix:
                    if searched_string in string_in_matrix:
                        return True
                return False
