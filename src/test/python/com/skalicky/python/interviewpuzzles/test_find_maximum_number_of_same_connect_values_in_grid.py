from typing import List
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_maximum_number_of_same_connect_values_in_grid import Grid


class TestGrid(TestCase):
    def test_find_recursively_maximum_number_of_same_connect_values_in_grid__when_just_1_isle_with_maximum_number_exists__then_size_of_this_isle_is_returned(
            self):
        grid: List[List[int]] = [[1, 0, 0, 1],
                                 [1, 1, 1, 1],
                                 [0, 1, 0, 0]]
        self.assertEqual(7, Grid(grid).find_recursively_maximum_number_of_same_connect_values_in_grid())

    def test_find_iteratively_maximum_number_of_same_connect_values_in_grid__when_just_1_isle_with_maximum_number_exists__then_size_of_this_isle_is_returned(
            self):
        grid: List[List[int]] = [[1, 0, 0, 1],
                                 [1, 1, 1, 1],
                                 [0, 1, 0, 0]]
        self.assertEqual(7, Grid(grid).find_iteratively_maximum_number_of_same_connect_values_in_grid())

    def test_find_recursively_maximum_number_of_same_connect_values_in_grid__when_more_isles_with_maximum_number_exist__then_their_size_is_returned(
            self):
        grid: List[List[int]] = [[0, 0, 1],
                                 [0, 1, 1],
                                 [1, 0, 0]]
        self.assertEqual(3, Grid(grid).find_recursively_maximum_number_of_same_connect_values_in_grid())

    def test_find_iteratively_maximum_number_of_same_connect_values_in_grid__when_more_isles_with_maximum_number_exist__then_their_size_is_returned(
            self):
        grid: List[List[int]] = [[0, 0, 1],
                                 [0, 1, 1],
                                 [1, 0, 0]]
        self.assertEqual(3, Grid(grid).find_iteratively_maximum_number_of_same_connect_values_in_grid())
