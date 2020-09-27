# Task:
#
# A maze is a matrix where each cell can either be a 0 or 1. A 0 represents that the cell is empty, and a 1 represents
# a wall that cannot be walked through. You can also only travel either right or down.
#
# Given a nxm matrix, find the number of ways someone can go from the top left corner to the bottom right corner. You
# can assume the two corners will always be 0.
#
# Example:
# Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
# # 0 1 0
# # 0 0 1
# # 0 0 0
# Output: 2
# The two paths that can only be taken in the above example are: down -> right -> down -> right, and down -> down ->
# right -> right.
#
# Here's some starter code:
#
# def paths_through_maze(maze):
#   # Fill this in.
#
# print(paths_through_maze([[0, 1, 0],
#                           [0, 0, 1],
#                           [0, 0, 0]]))
# # 2
from typing import List, Tuple


def paths_through_maze(maze: List[List[int]]) -> int:
    row_count: int = len(maze)
    if row_count == 0:
        return 0
    else:
        column_count: int = len(maze[0])
        if column_count == 0:
            return 0
        else:
            max_row_index: int = row_count - 1
            max_column_index: int = column_count - 1
            counter: int = 0
            last_positions: List[Tuple[int, int]] = [(0, 0)]
            while len(last_positions) > 0:
                current_row_index, current_column_index = last_positions.pop()
                if current_row_index == max_row_index and current_column_index == max_column_index:
                    counter += 1
                else:
                    if current_row_index < max_row_index and maze[current_row_index + 1][current_column_index] == 0:
                        last_positions.append((current_row_index + 1, current_column_index))
                    if current_column_index < max_column_index and maze[current_row_index][
                        current_column_index + 1] == 0:
                        last_positions.append((current_row_index, current_column_index + 1))
            return counter


print(paths_through_maze([]))
# 0
print(paths_through_maze([[]]))
# 0
print(paths_through_maze([[0, 1, 0],
                          [0, 0, 1],
                          [0, 0, 0]]))
# 2
print(paths_through_maze([[0, 0, 0],
                          [0, 0, 1],
                          [0, 0, 0]]))
# 3
print(paths_through_maze([[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]))
# 6
