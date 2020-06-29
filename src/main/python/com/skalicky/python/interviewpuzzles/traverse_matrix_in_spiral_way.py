# Task:
#
# You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.
#
# Example:
#
# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]
#
# The clockwise spiral traversal of this array is:
#
# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
#
# Here is a starting point:
#
# def matrix_spiral_print(M):
#   # Fill this in.
#
# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]
#
# matrix_spiral_print(grid)
# # 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
from enum import Enum

from typing import List


class Direction(Enum):
    LEFT = 1,
    DOWN = 2,
    RIGHT = 3,
    UP = 4


def matrix_spiral_print(matrix: List[List[int]]):
    matrix_visited: List[List[bool]] = []
    row_count: int = len(matrix)
    for i in range(0, row_count):
        matrix_visited.append([])
        for j in range(0, len(matrix[i])):
            matrix_visited[i].append(False)
    if row_count == 0 or len(matrix[0]) == 0:
        return
    column_count: int = len(matrix[0])
    last_direction: Direction = Direction.LEFT
    i = 0
    j = 0
    while 0 <= i < row_count and 0 <= j < column_count and not matrix_visited[i][j]:
        print(matrix[i][j], end=' ')
        matrix_visited[i][j] = True
        if last_direction == Direction.DOWN:
            if i < row_count - 1 and not matrix_visited[i + 1][j]:
                i = i + 1
            else:
                last_direction = Direction.RIGHT
                j = j - 1
        elif last_direction == Direction.UP:
            if i > 0 and not matrix_visited[i - 1][j]:
                i = i - 1
            else:
                last_direction = Direction.LEFT
                j = j + 1
        elif last_direction == Direction.LEFT:
            if j < column_count - 1 and not matrix_visited[i][j + 1]:
                j = j + 1
            else:
                last_direction = Direction.DOWN
                i = i + 1
        elif last_direction == Direction.RIGHT:
            if j > 0 and not matrix_visited[i][j - 1]:
                j = j - 1
            else:
                last_direction = Direction.UP
                i = i - 1
    print()


grid = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
grid2 = [[2]]
matrix_spiral_print(grid2)
# 2
grid3 = [[]]
matrix_spiral_print(grid3)
#
