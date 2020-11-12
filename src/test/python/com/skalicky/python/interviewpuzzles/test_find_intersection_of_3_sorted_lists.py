from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_intersection_of_3_sorted_lists import \
    find_intersection_of_3_sorted_lists


class Test(TestCase):
    def test_find_intersection_of_3_sorted_lists__when_any_list_is_empty__then_result_is_empty(self):
        self.assertListEqual([], find_intersection_of_3_sorted_lists([], [2, 3], [3, 4]))

    def test_find_intersection_of_3_sorted_lists__when_lists_have_no_element_in_common__then_result_is_empty(self):
        self.assertListEqual([], find_intersection_of_3_sorted_lists([2, 4], [2, 3], [3, 4]))

    def test_find_intersection_of_3_sorted_lists__when_lists_have_only_1_element_in_common__then_result_is_list_with_that_element(
            self):
        self.assertListEqual([4], find_intersection_of_3_sorted_lists([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))

    def test_find_intersection_of_3_sorted_lists__when_lists_have_more_elements_in_common__then_result_is_sorted(
            self):
        self.assertListEqual([3, 4, 8],
                             find_intersection_of_3_sorted_lists([1, 2, 3, 4, 8], [2, 3, 4, 6, 8], [3, 4, 5, 8]))
