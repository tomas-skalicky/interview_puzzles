from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.merge_consecutive_numbers_in_sorted_list_to_ranges import \
    merge_consecutive_numbers_in_sorted_list_to_ranges


class Test(TestCase):
    def test_merge_consecutive_numbers_in_sorted_list_to_ranges__when_input_is_empty__then_output_is_empty(self):
        self.assertListEqual([], merge_consecutive_numbers_in_sorted_list_to_ranges([]))

    def test_merge_consecutive_numbers_in_sorted_list_to_ranges__when_input_contains_only_1_number__then_output_contains_only_1_entry_from_that_number_to_that_number(
            self):
        self.assertListEqual(['5->5'], merge_consecutive_numbers_in_sorted_list_to_ranges([5]))

    def test_merge_consecutive_numbers_in_sorted_list_to_ranges__when_input_contains_3_consecutive_numbers__then_output_contains_entry_from_min_to_max_of_those_3_numbers(
            self):
        self.assertListEqual(['0->2'], merge_consecutive_numbers_in_sorted_list_to_ranges([0, 1, 2]))

    def test_merge_consecutive_numbers_in_sorted_list_to_ranges__when_input_contains_only_1_number_multiple_times__then_output_contains_only_1_entry_from_that_number_to_that_number(
            self):
        self.assertListEqual(['9->9'], merge_consecutive_numbers_in_sorted_list_to_ranges([9, 9]))

    def test_merge_consecutive_numbers_in_sorted_list_to_ranges__when_input_is_combination_of_various_use_cases__then_output_is_correct(
            self):
        self.assertListEqual(['0->2', '5->5', '7->11', '15->15'],
                             merge_consecutive_numbers_in_sorted_list_to_ranges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
