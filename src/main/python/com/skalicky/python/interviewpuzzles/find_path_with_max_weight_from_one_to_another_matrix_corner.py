# Task:
#
# Given a 2d n x m matrix where each cell has a certain amount of change on the floor, your goal is to start from
# the top left corner mat[0][0] and end in the bottom right corner mat[n - 1][m - 1] with the most amount of change.
# You can only move either left or down.
#
# Here's some starter code:
#
# def max_change(mat):
#   # Fill this in.
#
# mat = [
#     [0, 3, 0, 2],
#     [1, 2, 3, 3],
#     [6, 0, 3, 2]
# ]
#
# print(max_change(mat))
# # 13
from collections import deque
from enum import Enum
from typing import Deque, List, Optional, Tuple


class MoveType(Enum):
    RIGHT = 1,
    DOWN = 2


def max_change(mat: List[List[int]]) -> Optional[int]:
    max_row: int = len(mat) - 1
    max_column: int = len(mat[0]) - 1

    current_max: Optional[int] = None
    current_max_path: Optional[List[MoveType]] = None
    coordinates_to_process_and_weight_and_path: Deque[Tuple[int, int, int, List[MoveType]]] = deque()
    coordinates_to_process_and_weight_and_path.append((0, 0, mat[0][0], []))
    while len(coordinates_to_process_and_weight_and_path) > 0:
        row_to_process, column_to_process, weight, path = coordinates_to_process_and_weight_and_path.pop()
        new_weight: int = weight + mat[row_to_process][column_to_process]
        if row_to_process == max_row and column_to_process == max_column:
            if current_max is None or new_weight > current_max:
                current_max = new_weight
                current_max_path = path
        elif row_to_process < max_row and column_to_process < max_column:
            new_path: List[MoveType] = path.copy()
            new_path.append(MoveType.DOWN)
            coordinates_to_process_and_weight_and_path.append(
                (row_to_process + 1, column_to_process, new_weight, new_path))

            path.append(MoveType.RIGHT)
            coordinates_to_process_and_weight_and_path.append((row_to_process, column_to_process + 1, new_weight, path))
        elif row_to_process < max_row:
            path.append(MoveType.DOWN)
            coordinates_to_process_and_weight_and_path.append((row_to_process + 1, column_to_process, new_weight, path))
        elif column_to_process < max_column:
            path.append(MoveType.RIGHT)
            coordinates_to_process_and_weight_and_path.append((row_to_process, column_to_process + 1, new_weight, path))

    print(current_max_path)
    return current_max


print(max_change([
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]))
# 13
