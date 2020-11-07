from typing import List
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.move_zeros_at_the_end_and_keep_order import Solution


class TestSolution(TestCase):
    def test_move_zeros_at_the_end_and_keep_order__when_list_is_mixture_of_zeros_and_non_zeros__then_zeros_are_moved_at_the_end_and_order_of_non_zeros_is_kept(
            self):
        numbers: List[int] = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
        Solution.move_zeros_at_the_end_and_keep_order(numbers)
        self.assertListEqual([2, 1, 3, 4, 0, 0, 0, 0, 0, 0], numbers)

    def test_move_zeros_at_the_end_and_keep_order__when_list_is_empty__then_list_stays_empty(self):
        numbers: List[int] = []
        Solution.move_zeros_at_the_end_and_keep_order(numbers)
        self.assertListEqual([], numbers)

    def test_move_zeros_at_the_end_and_keep_order__when_list_contains_only_non_zeros__then_there_are_no_changes_in_list(
            self):
        numbers: List[int] = [2, 1]
        Solution.move_zeros_at_the_end_and_keep_order(numbers)
        self.assertListEqual([2, 1], numbers)

    def test_move_zeros_at_the_end_and_keep_order__when_list_contains_only_zeros__then_there_are_no_changes_in_list(
            self):
        numbers: List[int] = [0, 0]
        Solution.move_zeros_at_the_end_and_keep_order(numbers)
        self.assertListEqual([0, 0], numbers)
