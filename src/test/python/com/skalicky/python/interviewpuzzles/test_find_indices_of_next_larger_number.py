from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_indices_of_next_larger_number import \
    find_indices_of_next_larger_number


class Test(TestCase):
    def test_find_indices_of_next_larger_number__when_there_are_no_same_input_numbers_before_finding_larger_number__then_algorithm_works(
            self):
        self.assertListEqual([2, 2, 3, 4, -1, -1], find_indices_of_next_larger_number([3, 2, 5, 6, 9, 8]))

    def test_find_indices_of_next_larger_number__when_there_are_same_input_numbers_before_finding_larger_number__then_algorithm_works(
            self):
        self.assertListEqual([5, 2, 5, 5, 5, -1], find_indices_of_next_larger_number([3, 2, 3, 3, 2, 9]))
