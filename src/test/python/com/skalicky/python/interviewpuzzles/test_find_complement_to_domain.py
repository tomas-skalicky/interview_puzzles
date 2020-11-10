from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_complement_to_domain import Solution


class TestSolution(TestCase):
    def test_find_complement_to_domain__when_input_contains_gaps__then_output_are_gaps(self):
        self.assertSetEqual({3, 5}, Solution.find_complement_to_domain([4, 6, 2, 6, 7, 2, 1]))

    def test_find_complement_to_domain__when_input_contains_no_gaps__then_output_is_empty(self):
        self.assertSetEqual(set(), Solution.find_complement_to_domain([3, 1, 2]))
