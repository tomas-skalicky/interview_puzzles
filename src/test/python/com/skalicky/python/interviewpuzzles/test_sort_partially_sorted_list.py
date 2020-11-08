from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.sort_partially_sorted_list import sort_partially_sorted_list


class Test(TestCase):
    def test_sort_partially_sorted_list__when_input_is_empty__then_output_is_empty(self):
        self.assertListEqual([], sort_partially_sorted_list([], 0))

    def test_sort_partially_sorted_list__when_input_contains_only_one_element__then_output_is_the_same_as_input(self):
        self.assertListEqual([2], sort_partially_sorted_list([2], 0))

    def test_sort_partially_sorted_list__when_input_is_sorted__then_output_is_sorted(self):
        self.assertListEqual([2, 3, 4, 5, 7], sort_partially_sorted_list([2, 3, 4, 5, 7], 0))

    def test_sort_partially_sorted_list__when_input_is_unsorted_with_max_2_indices_from_right_position_and_k_equals_2__then_output_is_sorted(
            self):
        self.assertListEqual([2, 3, 4, 5, 7], sort_partially_sorted_list([3, 2, 7, 5, 4], 2))

    def test_sort_partially_sorted_list__when_input_is_unsorted_with_max_4_indices_from_right_position_and_k_equals_4__then_output_is_sorted(
            self):
        self.assertListEqual([2, 3, 4, 5, 7], sort_partially_sorted_list([7, 2, 5, 4, 3], 4))

    def test_sort_partially_sorted_list__when_input_is_unsorted_with_max_2_indices_from_right_position_and_k_equals_3__then_output_is_sorted(
            self):
        self.assertListEqual([2, 3, 4, 5, 7], sort_partially_sorted_list([3, 2, 7, 5, 4], 3))
