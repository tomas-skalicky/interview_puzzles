from typing import List
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_string_in_2d_matrix import find_string_in_2d_matrix


class Test(TestCase):
    def test_find_string_in_2d_matrix__when_searched_string_is_empty__then_result_is_true(self):
        self.assertTrue(find_string_in_2d_matrix([[]], ''))

    def test_find_string_in_2d_matrix__when_searched_string_is_non_empty_and_matrix_is_empty__then_result_is_false(
            self):
        self.assertFalse(find_string_in_2d_matrix([[]], 'F'))

    def test_find_string_in_2d_matrix__when_searched_string_is_in_matrix_only_from_bottom_to_top__then_result_is_false(
            self):
        self.assertFalse(find_string_in_2d_matrix(self.create_matrix(), 'BP'))

    def test_find_string_in_2d_matrix__when_searched_string_is_in_matrix_from_top_to_very_bottom__then_result_is_true(
            self):
        self.assertTrue(find_string_in_2d_matrix(self.create_matrix(), 'OSS'))

    def test_find_string_in_2d_matrix__when_searched_string_is_in_matrix_from_left_to_right__then_result_is_true(self):
        self.assertTrue(find_string_in_2d_matrix(self.create_matrix(), 'BQP'))

    def test_find_string_in_2d_matrix__when_searched_string_is_in_matrix_from_very_top_to_very_bottom__then_result_is_true(
            self):
        self.assertTrue(find_string_in_2d_matrix(self.create_matrix(), 'FOAMM'))

    @staticmethod
    def create_matrix() -> List[List[str]]:
        return [
            ['F', 'A', 'C', 'I'],
            ['O', 'B', 'Q', 'P'],
            ['A', 'N', 'O', 'B'],
            ['M', 'A', 'S', 'S'],
            ['M', 'X', 'S', 'S']]
