from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_sublist_of_non_adjacent_numbers_with_largest_sum import \
    find_sublist_of_non_adjacent_numbers_with_largest_sum


class Test(TestCase):
    def test_find_sublist_of_non_adjacent_numbers_with_largest_sum__when_input_is_empty__then_output_is_empty(self):
        self.assertListEqual([], find_sublist_of_non_adjacent_numbers_with_largest_sum([]))

    def test_find_sublist_of_non_adjacent_numbers_with_largest_sum__when_input_contains_1_number__then_output_is_this_number(
            self):
        self.assertListEqual([3], find_sublist_of_non_adjacent_numbers_with_largest_sum([3]))

    def test_find_sublist_of_non_adjacent_numbers_with_largest_sum__when_input_contains_2_numbers__then_output_is_greater_number(
            self):
        self.assertListEqual([3], find_sublist_of_non_adjacent_numbers_with_largest_sum([3, 2]))

    def test_find_sublist_of_non_adjacent_numbers_with_largest_sum__when_input_contains_4_numbers__then_output_is_pair_with_maximum_sum(
            self):
        self.assertListEqual([4, 1], find_sublist_of_non_adjacent_numbers_with_largest_sum([3, 4, 1, 1]))

    def test_find_sublist_of_non_adjacent_numbers_with_largest_sum__when_sum_of_2_numbers_is_greater_than_sum_of_3__then_output_are_those_two_numbers(
            self):
        self.assertListEqual([2, 7], find_sublist_of_non_adjacent_numbers_with_largest_sum([2, 1, 2, 7, 3]))

    def test_find_sublist_of_non_adjacent_numbers_with_largest_sum__when_input_contains_6_same_numbers__then_output_is_triple(
            self):
        self.assertListEqual([1, 1, 1], find_sublist_of_non_adjacent_numbers_with_largest_sum([1, 1, 1, 1, 1, 1]))
