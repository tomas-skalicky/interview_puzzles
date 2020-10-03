# Task:
#
# Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands present
# in the grid. The definition of an island is as follows:
# 1.) Must be surrounded by water blocks.
# 2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
# Assume all edges outside of the grid are water.
#
# Example:
# Input:
# 10001
# 11000
# 10110
# 00000
#
# Output: 3
# Here's your starting point:
#
# class Solution(object):
#   def inRange(self, grid, r, c):
#     numRow, numCol = len(grid), len(grid[0])
#     if r < 0 or c < 0 or r >= numRow or c >= numCol:
#       return False
#     return True
#
#   def numIslands(self, grid):
#     # Fill this in.
#
# grid = [[1, 1, 0, 0, 0],
#         [0, 1, 0, 0, 1],
#         [1, 0, 0, 1, 1],
#         [0, 0, 0, 0, 0]]
# print(Solution().numIslands(grid))
# # 3
from typing import List, Tuple, Set


class Solution(object):
    @staticmethod
    def in_range(grid: List[List[int]], r: int, c: int) -> bool:
        num_row, num_col = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= num_row or c >= num_col:
            return False
        return True

    @staticmethod
    def num_islands(grid: List[List[int]]) -> int:
        row_count: int = len(grid)
        if row_count == 0:
            return 0
        else:
            column_count: int = len(grid[0])
            isle_count: int = 0

            isle_cells_to_process: Set[Tuple[int, int]] = set()
            for row in range(0, row_count):
                for column in range(0, column_count):
                    if grid[row][column] == 1:
                        isle_cells_to_process.add((row, column))
            while len(isle_cells_to_process) > 0:
                isle_count += 1
                neighbours_to_process: Set[Tuple[int, int]] = set()
                isle_cell_to_process: Tuple[int, int] = isle_cells_to_process.pop()
                isle_cells_to_process.add(isle_cell_to_process)
                neighbours_to_process.add(isle_cell_to_process)
                while len(neighbours_to_process) > 0:
                    neighbour_to_process: Tuple[int, int] = neighbours_to_process.pop()
                    row: int = neighbour_to_process[0]
                    column: int = neighbour_to_process[1]
                    if Solution.in_range(grid, row, column) and grid[row][
                        column] == 1 and isle_cells_to_process.__contains__(neighbour_to_process):
                        isle_cells_to_process.remove(neighbour_to_process)
                        neighbours_to_process.add((row - 1, column))
                        neighbours_to_process.add((row, column - 1))
                        neighbours_to_process.add((row, column + 1))
                        neighbours_to_process.add((row + 1, column))
            return isle_count


print(Solution.num_islands([[]]))
# 0

print(Solution.num_islands([[0]]))
# 0

print(Solution.num_islands([[1]]))
# 1

print(Solution.num_islands([[1, 1, 0, 0, 0],
                            [0, 1, 0, 0, 1],
                            [1, 0, 0, 1, 1],
                            [0, 0, 0, 0, 0]]))
# 3

print(Solution.num_islands([[1, 0, 0, 0, 1],
                            [1, 1, 0, 0, 0],
                            [1, 0, 1, 1, 0],
                            [0, 0, 0, 0, 0]]))
# 3

print(Solution.num_islands([[1, 0, 0, 1, 1],
                            [1, 1, 0, 0, 1],
                            [0, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0]]))
# 1
