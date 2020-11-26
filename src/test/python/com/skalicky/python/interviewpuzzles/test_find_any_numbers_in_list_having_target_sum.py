from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_any_numbers_in_list_having_target_sum import \
    find_any_numbers_in_list_having_target_sum


class Test(TestCase):
    def test_find_any_numbers_in_list_having_target_sum__when_input_list_is_empty__then_result_is_empty(self):
        self.assertSetEqual(set(), find_any_numbers_in_list_having_target_sum([], 0))

    def test_find_any_numbers_in_list_having_target_sum__when_input_list_contains_only_1_number_and_this_number_equals_target_sum__then_result_is_set_with_1_tuple_containing_this_number(
            self):
        self.assertSetEqual({tuple([3])}, find_any_numbers_in_list_having_target_sum([3], 3))

    def test_find_any_numbers_in_list_having_target_sum__when_input_list_contains_only_1_number_and_this_number_does_not_equal_target_sum__then_result_is_empty(
            self):
        self.assertSetEqual(set(), find_any_numbers_in_list_having_target_sum([4], 3))

    def test_find_any_numbers_in_list_having_target_sum__when_input_list_contains_1_number_multiple_times_and_this_number_equals_target_sum__then_this_number_is_only_once_in_result(
            self):
        self.assertSetEqual({tuple([1])}, find_any_numbers_in_list_having_target_sum([1, 1], 1))

    def test_find_any_numbers_in_list_having_target_sum__when_input_list_contains_number_equal_to_target_sum_and_contains_2_numbers_which_sum_equals_target_sum__then_both_combinations_are_in_result(
            self):
        self.assertSetEqual({(1, 2), tuple([3])}, find_any_numbers_in_list_having_target_sum([1, 2, 3], 3))

    def test_find_any_numbers_in_list_having_target_sum__when_input_list_contains_multiple_combinations_how_to_reach_target_sum__then_all_unique_combinations_are_in_result(
            self):
        self.assertSetEqual({(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)},
                            find_any_numbers_in_list_having_target_sum([10, 1, 2, 7, 6, 1, 5], 8))
