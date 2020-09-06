# Task:
#
# A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k, we want to figure out
# after k random moves by a knight, the probability that the knight will still be on the chessboard. Once the knight
# leaves the board it cannot move again and will be considered off the board.
#
# Here's some starter code:
#
# def is_knight_on_board(x, y, k, cache={}):
#   # Fill this in.
#
# print is_knight_on_board(0, 0, 1)
# # 0.25
from collections import deque
from typing import Deque, Tuple


def is_on_chessboard(position: Tuple[int, int]) -> bool:
    return 0 <= position[0] < 8 and 0 <= position[1] < 8


def evaluate_position(position: Tuple[int, int], on_board_count: int, off_board_count: int,
                      new_positions_to_process: Deque[Tuple[int, int]]) -> Tuple[int, int]:
    if is_on_chessboard(position):
        new_positions_to_process.append(position)
        return on_board_count + 1, off_board_count
    else:
        return on_board_count, off_board_count + 1


def is_knight_on_board(x: int, y: int, k: int) -> float:
    positions_to_process: Deque[Tuple[int, int]] = deque()
    positions_to_process.append((x, y))
    on_board_count: int = 0
    off_board_count: int = 0
    for i in range(0, k):
        new_positions_to_process: Deque[Tuple[int, int]] = deque()
        while len(positions_to_process) > 0:
            position_to_process: Tuple[int, int] = positions_to_process.pop()
            current_x: int = position_to_process[0]
            current_y: int = position_to_process[1]

            # (0, 0) is a top left corner of the chessboard

            on_board_count, off_board_count = evaluate_position((current_x - 1, current_y + 2), on_board_count,
                                                                off_board_count, new_positions_to_process)
            on_board_count, off_board_count = evaluate_position((current_x + 1, current_y + 2), on_board_count,
                                                                off_board_count, new_positions_to_process)
            on_board_count, off_board_count = evaluate_position((current_x + 2, current_y + 1), on_board_count,
                                                                off_board_count, new_positions_to_process)
            on_board_count, off_board_count = evaluate_position((current_x + 2, current_y - 1), on_board_count,
                                                                off_board_count, new_positions_to_process)
            on_board_count, off_board_count = evaluate_position((current_x + 1, current_y - 2), on_board_count,
                                                                off_board_count, new_positions_to_process)
            on_board_count, off_board_count = evaluate_position((current_x - 1, current_y - 2), on_board_count,
                                                                off_board_count, new_positions_to_process)
            on_board_count, off_board_count = evaluate_position((current_x - 2, current_y - 1), on_board_count,
                                                                off_board_count, new_positions_to_process)
            on_board_count, off_board_count = evaluate_position((current_x - 2, current_y + 1), on_board_count,
                                                                off_board_count, new_positions_to_process)
        positions_to_process = new_positions_to_process
    return on_board_count / (on_board_count + off_board_count)


print(is_knight_on_board(0, 0, 1))
# 0.25
