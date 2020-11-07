from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_length_of_longest_consecutive_sequence_in_non_sorted_array import \
    find_length_of_longest_consecutive_sequence_in_non_sorted_array


class Test(TestCase):
    def test_find_length_of_longest_consecutive_sequence_in_non_sorted_array__when_input_sequence_is_empty__then_result_is_0(
            self):
        self.assertEqual(0, find_length_of_longest_consecutive_sequence_in_non_sorted_array([]))

    def test_find_length_of_longest_consecutive_sequence_in_non_sorted_array__when_input_sequence_contains_non_sorted_1_till_4__then_result_is_4(
            self):
        self.assertEqual(4, find_length_of_longest_consecutive_sequence_in_non_sorted_array([100, 4, 200, 1, 3, 2]))
