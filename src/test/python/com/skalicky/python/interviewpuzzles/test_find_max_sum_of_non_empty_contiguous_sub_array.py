from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_max_sum_of_non_empty_contiguous_sub_array import \
    find_max_sum_of_non_empty_contiguous_sub_array


class Test(TestCase):
    def test_find_max_sum_of_non_empty_contiguous_sub_array__when_input_contains_only_negative_numbers__then_output_is_greatest_number(
            self):
        self.assertEqual(-5, find_max_sum_of_non_empty_contiguous_sub_array([-34, -50, -5]))

    def test_find_max_sum_of_non_empty_contiguous_sub_array__when_input_contains_non_negative_number_and_negative_number_at_the_end__then_negative_number_at_the_end_is_not_counted(
            self):
        self.assertEqual(137, find_max_sum_of_non_empty_contiguous_sub_array([34, -50, 42, 14, -5, 86, -5]))

    def test_find_max_sum_of_non_empty_contiguous_sub_array__when_input_contains_negative_number_greater_than_sum_of_previous_numbers__then_summing_is_reset(
            self):
        self.assertEqual(42, find_max_sum_of_non_empty_contiguous_sub_array([34, -50, 42]))

    def test_find_max_sum_of_non_empty_contiguous_sub_array__when_input_contains_negative_number_less_than_sum_of_previous_numbers__then_summing_continues(
            self):
        self.assertEqual(137, find_max_sum_of_non_empty_contiguous_sub_array([42, 14, -5, 86]))
