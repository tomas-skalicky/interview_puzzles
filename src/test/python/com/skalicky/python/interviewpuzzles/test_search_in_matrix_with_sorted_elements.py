from typing import List
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.search_in_matrix_with_sorted_elements import \
    convert_number_to_matrix_coordinates, search_in_matrix_with_sorted_elements


class Test(TestCase):
    def test_convert_number_to_matrix_coordinates__when_number_is_less_than_number_of_columns__then_row_index_is_0(
            self):
        self.assertTupleEqual((0, 3), convert_number_to_matrix_coordinates(3, 4))

    def test_convert_number_to_matrix_coordinates__when_number_is_divided_by_number_of_columns__then_row_index_is_greater_than_0(
            self):
        self.assertTupleEqual((2, 0), convert_number_to_matrix_coordinates(8, 4))

    def test_search_in_matrix_with_sorted_elements__when_searched_value_is_in_matrix__then_result_is_true(self):
        matrix: List[List[int]] = [
            [1, 3, 5, 8],
            [10, 11, 15, 16],
            [24, 27, 30, 31],
        ]
        self.assertTrue(search_in_matrix_with_sorted_elements(matrix, 10))

    def test_search_in_matrix_with_sorted_elements__when_searched_value_is_not_in_matrix__then_result_is_false(self):
        matrix: List[List[int]] = [
            [1, 3, 5, 8],
            [10, 11, 15, 16],
            [24, 27, 30, 31],
            [32, 33, 34, 35],
        ]
        self.assertFalse(search_in_matrix_with_sorted_elements(matrix, 4))
