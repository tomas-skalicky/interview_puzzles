from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_kth_largest_number_in_list import \
    find_kth_largest_number_in_list


class Test(TestCase):
    def test_find_kth_largest_number_in_list__when_k_is_less_than_length_of_input_list__then_k_largest_number_is_returned(
            self):
        self.assertEqual(5, find_kth_largest_number_in_list([3, 5, 2, 4, 6, 8], 3))

    def test_find_kth_largest_number_in_list__when_k_is_greater_or_equal_to_length_of_input_list__then_output_is_none(
            self):
        self.assertIsNone(find_kth_largest_number_in_list([3], 2))
