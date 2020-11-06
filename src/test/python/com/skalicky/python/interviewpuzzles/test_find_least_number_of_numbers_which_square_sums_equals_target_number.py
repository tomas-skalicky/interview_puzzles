from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_least_number_of_numbers_which_square_sums_equals_target_number import \
    find_least_number_of_numbers_which_square_sums_equals_target_number


class Test(TestCase):
    def test_find_least_number_of_numbers_which_square_sums_equals_target_number__when_input_consists_of_2_squares_like_13__then_2(
            self):
        self.assertEqual(2, find_least_number_of_numbers_which_square_sums_equals_target_number(13))

    def test_find_least_number_of_numbers_which_square_sums_equals_target_number__when_input_consists_of_1_square_like_256__then_1(
            self):
        self.assertEqual(1, find_least_number_of_numbers_which_square_sums_equals_target_number(256))

    def test_find_least_number_of_numbers_which_square_sums_equals_target_number__when_input_consists_of_3_squares_like_1041__then_3(
            self):
        self.assertEqual(3, find_least_number_of_numbers_which_square_sums_equals_target_number(1041))
