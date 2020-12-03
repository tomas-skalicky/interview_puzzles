from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.generate_all_subsets import generate_all_subsets


class Test(TestCase):
    def test_generate_all_subsets__when_list_is_empty__then_output_contains_only_empty_set(self):
        self.assertListEqual([set()], generate_all_subsets([]))

    def test_generate_all_subsets__when_list_contains_1_element__then_output_contains_empty_list_and_list_containing_only_that_1_element(
            self):
        self.assertListEqual([set(), {1}], generate_all_subsets([1]))

    def test_generate_all_subsets__when_list_contains_2_elements__then_output_contains_unique_combinations_independent_of_order(
            self):
        self.assertListEqual([set(), {2}, {1}, {2, 1}], generate_all_subsets([2, 1]))

    def test_generate_all_subsets__when_list_contains_3_elements__then_output_contains_8_lists(
            self):
        self.assertListEqual([set(), {1}, {3}, {2}, {1, 3}, {1, 2}, {3, 2}, {1, 2, 3}], generate_all_subsets([1, 3, 2]))
