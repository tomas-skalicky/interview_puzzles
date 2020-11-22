from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_longest_run_of_ones_in_binary_representation import \
    find_longest_run_of_ones_in_binary_representation


class Test(TestCase):
    def test_find_longest_run_of_ones_in_binary_representation__when_input_is_0__then_result_is_0(self):
        self.assertEqual(0, find_longest_run_of_ones_in_binary_representation(0))

    def test_find_longest_run_of_ones_in_binary_representation__when_input_is_1__then_result_is_1(self):
        self.assertEqual(1, find_longest_run_of_ones_in_binary_representation(1))

    def test_find_longest_run_of_ones_in_binary_representation__when_input_is_2__then_result_is_1(self):
        self.assertEqual(1, find_longest_run_of_ones_in_binary_representation(2))

    def test_find_longest_run_of_ones_in_binary_representation__when_input_is_3__then_result_is_2(self):
        self.assertEqual(2, find_longest_run_of_ones_in_binary_representation(3))

    def test_find_longest_run_of_ones_in_binary_representation__when_input_is_decimal_242_represented_binary_11110010__then_result_is_4(
            self):
        self.assertEqual(4, find_longest_run_of_ones_in_binary_representation(242))
