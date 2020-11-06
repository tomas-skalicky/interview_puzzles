from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_1_solution_how_to_place_queens_on_chessboard import \
    find_1_solution_how_to_place_queens_on_chessboard


class Test(TestCase):
    def test_find_1_solution_how_to_place_queens_on_chessboard__when_5__then_5_entries(self):
        self.assertListEqual([(0, 0), (2, 1), (4, 2), (1, 3), (3, 4)],
                             find_1_solution_how_to_place_queens_on_chessboard(5))

    def test_find_1_solution_how_to_place_queens_on_chessboard__when_8__then_8_entries(self):
        self.assertListEqual([(0, 0), (2, 1), (4, 2), (6, 3), (1, 4), (3, 5), (5, 6), (7, 7)],
                             find_1_solution_how_to_place_queens_on_chessboard(8))
