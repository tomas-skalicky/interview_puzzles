from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_fixed_points import find_fixed_points


class Test(TestCase):
    def test_find_fixed_points__when_there_is_no_input_number__then_output_is_empty(self):
        self.assertSetEqual(set(), find_fixed_points([]))

    def test_find_fixed_points__when_input_list_is_non_empty_and_there_are_no_numbers_being_equal_to_their_indiced_in_input_list__then_output_is_empty(
            self):
        self.assertSetEqual(set(), find_fixed_points([-5, 2]))

    def test_find_fixed_points__when_input_is_ascending_sequece_of_numbers_starting_with_0__then_whole_sequence_is_output(
            self):
        self.assertSetEqual({0, 1, 2, 3}, find_fixed_points([0, 1, 2, 3]))

    def test_find_fixed_points__when_input_contains_both_fixed_points_and_non_fixed_points__then_only_fixed_points_are_returned(
            self):
        self.assertSetEqual({1, 2, 3, 4}, find_fixed_points([-5, 1, 2, 3, 4, 6]))
