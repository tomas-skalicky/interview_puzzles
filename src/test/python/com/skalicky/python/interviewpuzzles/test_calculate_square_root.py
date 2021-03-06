from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.calculate_square_root import calculate_square_root


class Test(TestCase):
    def test_calculate_square_root__when_input_is_not_square__then_result_is_float(self):
        self.assertEqual(2.236, calculate_square_root(5))

    def test_calculate_square_root__when_input_is_square__then_result_is_integer(self):
        self.assertEqual(91, calculate_square_root(8281))
