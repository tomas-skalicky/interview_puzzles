# Task:
#
# N-Queens is the problem where you find a way to put n queens on a nxn chess board without them being able to attack
# each other. Given an integer n, return 1 possible solution by returning all the queen's position.
#
# Here's an example and some starter code:
#
# def n_queens(n):
#   # Fill this in.
#
# print(n_queens(5))
# # There can be many answers
# # [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]
#
# # Q . . . .
# # . . . Q .
# # . Q . . .
# # . . . . Q
# # . . Q . .
from typing import List, Tuple


def find_1_solution_how_to_place_queens_on_chessboard(queen_count: int) -> List[Tuple[int, int]]:
    """Time complexity of the algorithm is O(n) where *n* is a length of the chessboard side.
    """

    result: List[Tuple[int, int]] = []
    offset_by_next_row_reset: int = 0
    row_of_last_placed_queen: int = queen_count
    for column in range(0, queen_count):
        if row_of_last_placed_queen + 2 < queen_count:
            row_of_last_placed_queen += 2
        else:
            row_of_last_placed_queen = offset_by_next_row_reset
            offset_by_next_row_reset += 1
        result.append((row_of_last_placed_queen, column))
    return result
