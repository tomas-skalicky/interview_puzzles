# Task:
#
# Find the maximum number of connected colors in a grid.
#
# class Grid:
#     def __init__(self, grid):
#         self.grid = grid
#
#     def find_maximum_number_of_same_connect_values_in_grid(self):
#         # Fill this in.
#
# grid = [[1, 0, 0, 1],
#         [1, 1, 1, 1],
#         [0, 1, 0, 0]]
#
# print(Grid(grid).find_maximum_number_of_same_connect_values_in_grid())
# # 7
#
# Can you solve this both recursively and iteratively?
from collections import deque
from typing import Deque, List, Optional, Tuple


class Grid:
    def __init__(self, grid: List[List[object]]):
        self.grid: List[List[object]] = grid

    def find_recursively_new_isle_and_return_size(self, element_row: int, element_column: int, isle_color: object,
                                                  isle_id: int, grid_of_found_isles: List[List[int]], row_count: int,
                                                  column_count: int, current_isle_size: int) -> int:
        if 0 <= element_row < row_count and 0 <= element_column < column_count and \
                grid_of_found_isles[element_row][element_column] is None and self.grid[element_row][
            element_column] == isle_color:
            current_isle_size += 1
            grid_of_found_isles[element_row][element_column] = isle_id
            current_isle_size = self.find_recursively_new_isle_and_return_size(element_row, element_column - 1,
                                                                               isle_color, isle_id, grid_of_found_isles,
                                                                               row_count, column_count,
                                                                               current_isle_size)
            current_isle_size = self.find_recursively_new_isle_and_return_size(element_row + 1, element_column,
                                                                               isle_color, isle_id, grid_of_found_isles,
                                                                               row_count, column_count,
                                                                               current_isle_size)
            current_isle_size = self.find_recursively_new_isle_and_return_size(element_row, element_column + 1,
                                                                               isle_color, isle_id, grid_of_found_isles,
                                                                               row_count, column_count,
                                                                               current_isle_size)
            return self.find_recursively_new_isle_and_return_size(element_row - 1, element_column,
                                                                  isle_color, isle_id, grid_of_found_isles,
                                                                  row_count, column_count,
                                                                  current_isle_size)
        else:
            return current_isle_size

    def find_recursively_maximum_number_of_same_connect_values_in_grid(self) -> int:
        row_count: int = len(self.grid)
        column_count: int = len(self.grid[0])
        grid_of_found_isles: List[List[Optional[int]]] = [[None] * column_count for i in range(0, row_count)]
        max_isle_size: int = 0
        current_isle_id: int = 1

        for i in range(0, row_count):
            for j in range(0, column_count):
                if grid_of_found_isles[i][j] is None:
                    current_isle_color: object = self.grid[i][j]
                    current_isle_size: int = self.find_recursively_new_isle_and_return_size(i, j, current_isle_color,
                                                                                            current_isle_id,
                                                                                            grid_of_found_isles,
                                                                                            row_count, column_count, 0)
                    max_isle_size = max(max_isle_size, current_isle_size)
                    current_isle_id += 1
        return max_isle_size

    def find_iteratively_maximum_number_of_same_connect_values_in_grid(self) -> int:
        row_count: int = len(self.grid)
        column_count: int = len(self.grid[0])
        grid_of_found_isles: List[List[Optional[int]]] = [[None] * column_count for i in range(0, row_count)]
        max_isle_size: int = 0
        current_isle_id: int = 1

        for i in range(0, row_count):
            for j in range(0, column_count):
                if grid_of_found_isles[i][j] is None:
                    element_coordinates_to_process: Deque[Tuple[int, int]] = deque()
                    element_coordinates_to_process.append((i, j))
                    current_isle_size: int = 0
                    current_isle_color: object = self.grid[i][j]

                    while len(element_coordinates_to_process) > 0:
                        element_row, element_column = element_coordinates_to_process.pop()
                        if 0 <= element_row < row_count and 0 <= element_column < column_count and \
                                grid_of_found_isles[element_row][element_column] is None and self.grid[element_row][
                            element_column] == current_isle_color:
                            current_isle_size += 1
                            grid_of_found_isles[element_row][element_column] = current_isle_id
                            element_coordinates_to_process.append((element_row, element_column - 1))
                            element_coordinates_to_process.append((element_row + 1, element_column))
                            element_coordinates_to_process.append((element_row, element_column + 1))
                            element_coordinates_to_process.append((element_row - 1, element_column))
                    max_isle_size = max(max_isle_size, current_isle_size)
                    current_isle_id += 1
        return max_isle_size
