from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_1_solution_how_to_place_queens_on_chessboard import n_queens


class Test(TestCase):
    def test_n_queens__when_5__then_5_entries(self):
        self.assertListEqual([(0, 0), (2, 1), (4, 2), (1, 3), (3, 4)], n_queens(5))

    def test_n_queens__when_8__then_8_entries(self):
        self.assertListEqual([(0, 0), (2, 1), (4, 2), (6, 3), (1, 4), (3, 5), (5, 6), (7, 7)], n_queens(8))
