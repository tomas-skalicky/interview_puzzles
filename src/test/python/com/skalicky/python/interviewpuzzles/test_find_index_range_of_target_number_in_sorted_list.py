from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_index_range_of_target_number_in_sorted_list import \
    find_index_range_of_target_number_in_sorted_list


class Test(TestCase):
    def test_find_index_range_of_target_number_in_sorted_list__when_input_is_empty__then_output_is_minus_1_minus_1(
            self):
        self.assertTupleEqual((-1, -1), find_index_range_of_target_number_in_sorted_list([], 5))

    def test_find_index_range_of_target_number_in_sorted_list__when_number_is_not_in_input__then_output_is_minus_1_minus_1(
            self):
        self.assertTupleEqual((-1, -1), find_index_range_of_target_number_in_sorted_list([1, 2, 3, 4], 5))

    def test_find_index_range_of_target_number_in_sorted_list__when_number_is_in_input_once__then_output_is_index_i_index_i(
            self):
        self.assertTupleEqual((2, 2), find_index_range_of_target_number_in_sorted_list([1, 2, 4], 4))

    def test_find_index_range_of_target_number_in_sorted_list__when_number_is_in_input_multiple_times__then_output_is_index_i_index_j(
            self):
        self.assertTupleEqual((0, 1), find_index_range_of_target_number_in_sorted_list([1, 1, 3, 5, 7], 1))
