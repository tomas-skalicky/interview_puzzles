from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_longest_palindromic_substring import Solution


class TestSolution(TestCase):
    def test_find_longest_palindromic_substring__when_input_string_is_tracecars__then_result_is_racecar(self):
        self.assertEqual('racecar', Solution.find_longest_palindromic_substring('tracecars'))

    def test_find_longest_palindromic_substring__when_input_string_is_banana__then_result_is_anana(self):
        self.assertEqual('anana', Solution.find_longest_palindromic_substring('banana'))

    def test_find_longest_palindromic_substring__when_input_string_is_million__then_result_is_illi(self):
        self.assertEqual('racecar', Solution.find_longest_palindromic_substring('tracecars'))

    def test_find_longest_palindromic_substring__when_input_string_is_mh__then_result_is_m(self):
        self.assertEqual('m', Solution.find_longest_palindromic_substring('mh'))

    def test_find_longest_palindromic_substring__when_input_string_is_empty__then_these_is_no_result(self):
        self.assertIsNone(Solution.find_longest_palindromic_substring(''))

    def test_find_longest_palindromic_substring__when_these_is_no_input_string__then_there_is_no_result(self):
        self.assertIsNone(Solution.find_longest_palindromic_substring(None))
