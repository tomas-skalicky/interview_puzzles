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
from collections.abc import MutableSet
from typing import List


def word_search(input_matrix: List[List[str]], word: str) -> bool:
    if len(word) == 0:
        return True
    if len(input_matrix) == 0 or len(input_matrix[0]) == 0:
        return False
    all_strings_in_matrix: MutableSet[str] = set()
    row_count = len(input_matrix)
    for row_index in range(0, row_count):
        all_strings_in_matrix.add(''.join(input_matrix[row_index][:]))
    column_count = len(input_matrix[0])
    for column_index in range(0, column_count):
        column_string = ''
        for row_index in range(0, row_count):
            column_string = column_string + input_matrix[row_index][column_index]
        all_strings_in_matrix.add(column_string)
    for string_in_matrix in all_strings_in_matrix:
        if string_in_matrix.__contains__(word):
            return True
    return False


matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S'],
    ['M', 'X', 'S', 'S']]
print(word_search(matrix, 'FOAMM'))
# True
print(word_search(matrix, 'BQP'))
# True
print(word_search(matrix, 'OSS'))
# True
print(word_search(matrix, 'BP'))
# False
print(word_search([[]], ''))
# True
print(word_search([[]], 'F'))
# False
print(word_search([[]], 'OSSS'))
# False
