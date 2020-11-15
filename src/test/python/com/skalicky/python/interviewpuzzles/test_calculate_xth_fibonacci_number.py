from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.calculate_xth_fibonacci_number import Solution


class TestSolution(TestCase):
    def test_calculate_xth_fibonacci_number__when_n_is_0__then_result_is_0(self):
        self.assertEqual(0, Solution.calculate_xth_fibonacci_number(0))

    def test_calculate_xth_fibonacci_number__when_n_is_1__then_result_is_1(self):
        self.assertEqual(1, Solution.calculate_xth_fibonacci_number(1))

    def test_calculate_xth_fibonacci_number__when_n_is_2__then_result_is_1(self):
        self.assertEqual(0 + 1, Solution.calculate_xth_fibonacci_number(2))

    def test_calculate_xth_fibonacci_number__when_n_is_9__then_result_is_34(self):
        self.assertEqual(13 + 21, Solution.calculate_xth_fibonacci_number(9))
