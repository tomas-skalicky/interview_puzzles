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
from collections import deque
from typing import Deque, List, Set, Tuple


# Time and spacial complexity ... O(row_count! * column_count!). See
# count_ways_how_to_get_from_one_to_another_matrix_corner.py
def paths_through_maze_traversing_without_memory(maze: List[List[int]]) -> int:
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


# Time and spacial complexity ... O(n * m)
def paths_through_maze_dynamic_programming(maze: List[List[int]]) -> int:
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
            maze_with_remembered_combinations: List[List[int]] = [[0 for j in range(0, column_count)] for i in
                                                                  range(0, row_count)]

            cells_to_process: Deque[Tuple[int, int]] = deque()
            processed_and_to_be_processed_sells: Set[Tuple[int, int]] = set()
            top_left_corner: Tuple[int, int] = (0, 0)
            cells_to_process.append(top_left_corner)
            processed_and_to_be_processed_sells.add(top_left_corner)
            while len(cells_to_process) > 0:
                current_row_index, current_column_index = cells_to_process.popleft()

                if current_row_index == 0 and current_column_index == 0:
                    maze_with_remembered_combinations[current_row_index][current_column_index] = 1
                else:
                    from_top: int = maze_with_remembered_combinations[current_row_index - 1][
                        current_column_index] if current_row_index > 0 else 0
                    from_left: int = maze_with_remembered_combinations[current_row_index][
                        current_column_index - 1] if current_column_index > 0 else 0
                    maze_with_remembered_combinations[current_row_index][current_column_index] = from_top + from_left

                if current_row_index < max_row_index and not processed_and_to_be_processed_sells.__contains__(
                        (current_row_index + 1, current_column_index)) and \
                        maze[current_row_index + 1][current_column_index] == 0:
                    new_cell_to_process: Tuple[int, int] = (current_row_index + 1, current_column_index)
                    cells_to_process.append(new_cell_to_process)
                    processed_and_to_be_processed_sells.add(new_cell_to_process)

                if current_column_index < max_column_index and not processed_and_to_be_processed_sells.__contains__(
                        (current_row_index, current_column_index + 1)) and maze[current_row_index][
                    current_column_index + 1] == 0:
                    new_cell_to_process: Tuple[int, int] = (current_row_index, current_column_index + 1)
                    cells_to_process.append(new_cell_to_process)
                    processed_and_to_be_processed_sells.add(new_cell_to_process)

            return maze_with_remembered_combinations[max_row_index][max_column_index]


def paths_through_maze(maze: List[List[int]]) -> None:
    print(paths_through_maze_traversing_without_memory(maze))
    print(paths_through_maze_dynamic_programming(maze))


paths_through_maze([])
# 0
# 0
paths_through_maze([[]])
# 0
# 0
paths_through_maze([[0]])
# 1
# 1
paths_through_maze([[0, 1, 0],
                    [0, 0, 1],
                    [0, 0, 0]])
# 2
# 2
paths_through_maze([[0, 0, 0],
                    [0, 0, 1],
                    [0, 0, 0]])
# 3
# 3
paths_through_maze([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]])
# 6
# 6
