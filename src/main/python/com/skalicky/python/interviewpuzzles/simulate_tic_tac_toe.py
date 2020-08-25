# Task:
#
# Design a Tic-Tac-Toe game played between two players on an n x n grid. A move is guaranteed to be valid, and a valid
# move is one placed on an empty block in the grid. A player who succeeds in placing n of their marks in a horizontal,
# diagonal, or vertical row wins the game. Once a winning condition is reached, the game ends and no more moves are
# allowed. Below is an example game which ends in a winning condition:
#
# Given n = 3, assume that player 1 is "X" and player 2 is "O"
# board = TicTacToe(3);
#
# board.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |
#
# board.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |
#
# board.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|
#
# board.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|
#
# board.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|
#
# board.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|
#
# board.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
#
# Here's a starting point:
#
# class TicTacToe(object):
#   def __init__(self, n):
#     # Fill this in.
#
#   def move(self, row, col, player):
#     # Fill this in.
#
# board = TicTacToe(3)
# board.move(0, 0, 1)
# board.move(0, 2, 2)
# board.move(2, 2, 1)
# board.move(1, 1, 2)
# board.move(2, 0, 1)
# board.move(1, 0, 2)
# print(board.move(2, 1, 1))
from enum import Enum
from typing import List


class CellOccupation(Enum):
    EMPTY = ' ',
    FIRST = 'X',
    SECOND = 'O'


class TicTacToe(object):
    def __init__(self, n: int):
        self.matrix: List[List[CellOccupation]] = list()
        for i in range(0, n):
            self.matrix.append(list())
            for j in range(0, n):
                self.matrix[i].append(CellOccupation.EMPTY)

    def move(self, row: int, col: int, player: int) -> int:
        player_occupation: CellOccupation = CellOccupation.FIRST if player == 1 else CellOccupation.SECOND
        self.matrix[row][col] = player_occupation
        win_in_row: bool = True
        win_in_column: bool = True
        n: int = len(self.matrix)
        for i in range(0, n):
            win_in_row = self.matrix[row][i] == player_occupation if win_in_row else False
            win_in_column = self.matrix[i][col] == player_occupation if win_in_column else False
        if win_in_row or win_in_column:
            return 1
        else:
            if row == col:
                win_in_diagonal: bool = True
                for i in range(0, n):
                    win_in_diagonal = self.matrix[i][i] == player_occupation if win_in_diagonal else False
                if win_in_diagonal:
                    return 1
            if row + col == n - 1:
                win_in_second_diagonal: bool = True
                for i in range(0, n):
                    win_in_second_diagonal = self.matrix[i][
                                                 n - i - 1] == player_occupation if win_in_second_diagonal else False
                if win_in_second_diagonal:
                    return 1
            return 0

    def __str__(self) -> str:
        result: str = ''
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                result += '|' + str(self.matrix[i][j].value[0])
            result += '|\n'
        return result


board = TicTacToe(3)
print(board.move(0, 0, 1))
# 0
print(board)
# |X| | |
# | | | |
# | | | |
print(board.move(0, 2, 2))
# 0
print(board)
# |X| |O|
# | | | |
# | | | |
print(board.move(2, 2, 1))
# 0
print(board)
# |X| |O|
# | | | |
# | | |X|
print(board.move(1, 1, 2))
# 0
print(board)
# |X| |O|
# | |O| |
# | | |X|
print(board.move(2, 0, 1))
# 0
print(board)
# |X| |O|
# | |O| |
# |X| |X|
print(board.move(1, 0, 2))
# 0
print(board)
# |X| |O|
# |O|O| |
# |X| |X|
print(board.move(2, 1, 1))
# 1
print(board)
# |X| |O|
# |O|O| |
# |X|X|X|


board2 = TicTacToe(3)
print(board2.move(0, 0, 1))
# 0
print(board2)
# |X| | |
# | | | |
# | | | |
print(board2.move(1, 0, 1))
# 0
print(board2)
# |X| | |
# |X| | |
# | | | |
print(board2.move(2, 0, 1))
# 1
print(board2)
# |X| | |
# |X| | |
# |X| | |


board3 = TicTacToe(3)
print(board3.move(0, 0, 1))
# 0
print(board3)
# |X| | |
# | | | |
# | | | |
print(board3.move(1, 1, 1))
# 0
print(board3)
# |X| | |
# | |X| |
# | | | |
print(board3.move(2, 2, 1))
# 1
print(board3)
# |X| | |
# | |X| |
# | | |X|


board4 = TicTacToe(3)
print(board4.move(0, 2, 1))
# 0
print(board4)
# | | |X|
# | | | |
# | | | |
print(board4.move(1, 1, 1))
# 0
print(board4)
# | | |X|
# | |X| |
# | | | |
print(board4.move(2, 0, 1))
# 1
print(board4)
# | | |X|
# | |X| |
# |X| | |