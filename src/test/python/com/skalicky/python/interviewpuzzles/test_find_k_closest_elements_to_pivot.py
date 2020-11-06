from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_k_closest_elements_to_pivot import \
    find_k_closest_elements_to_pivot


class Test(TestCase):
    def test_find_k_closest_elements_to_pivot__when_there_are_not_too_many_numbers_in_same_distance_from_x_which_will_be_selected__then_all_are_selected(
            self):
        self.assertListEqual([3, 7, 8], find_k_closest_elements_to_pivot([1, 3, 7, 8, 9], 3, 5))

    def test_find_k_closest_elements_to_pivot__when_there_are_too_many_numbers_in_same_distance_from_x_which_will_be_selected__then_lowers_are_selected(
            self):
        self.assertListEqual([3], find_k_closest_elements_to_pivot([3, 7], 1, 5))

    def test_find_k_closest_elements_to_pivot__when_input_list_of_numbers_is_smaller_than_k__then_exception(
            self):
        self.assertRaisesRegex(RuntimeError, 'There is not enough input numbers in \\[3\\] to return 2 elements.',
                               find_k_closest_elements_to_pivot, [3], 2, 5)
