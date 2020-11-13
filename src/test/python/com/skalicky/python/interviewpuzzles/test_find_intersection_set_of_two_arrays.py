from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_intersection_set_of_two_arrays import Solution


class TestSolution(TestCase):
    def test_find_intersection_set_of_two_arrays__when_1_number_is_multiple_times_in_both_input_arrays__then_this_number_is_only_once_in_result(
            self):
        self.assertSetEqual({2}, Solution.find_intersection_set_of_two_arrays([1, 2, 2, 1], [2, 2]))

    def test_find_intersection_set_of_two_arrays__when_there_are_2_common_unique_numbers__then_these_numbers_are_in_result(
            self):
        self.assertSetEqual({4, 9}, Solution.find_intersection_set_of_two_arrays([4, 9, 5], [9, 4, 9, 8, 4]))
