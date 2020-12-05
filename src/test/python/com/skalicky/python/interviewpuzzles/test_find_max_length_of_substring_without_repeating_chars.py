from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_max_length_of_substring_without_repeating_chars import \
    Solution


class TestSolution(TestCase):
    def test_find_max_length_of_substring_without_repeating_chars__when_input_is_none__then_output_is_0(self):
        self.assertEqual(0, Solution.find_max_length_of_substring_without_repeating_chars(None))

    def test_find_max_length_of_substring_without_repeating_chars__when_input_is_empty__then_output_is_0(self):
        self.assertEqual(0, Solution.find_max_length_of_substring_without_repeating_chars(''))

    def test_find_max_length_of_substring_without_repeating_chars__when_input_contains_all_characters_only_once__then_output_is_length_of_input(
            self):
        self.assertEqual(3, Solution.find_max_length_of_substring_without_repeating_chars('abc'))

    def test_find_max_length_of_substring_without_repeating_chars__when_input_contains_1_character_2x__then_output_is_shorter_than_length_of_input(
            self):
        self.assertEqual(2, Solution.find_max_length_of_substring_without_repeating_chars('aba'))

    def test_find_max_length_of_substring_without_repeating_chars__when_input_is_abrkaabcdefghijjxxx__then_output_is_10(
            self):
        self.assertEqual(10, Solution.find_max_length_of_substring_without_repeating_chars('abrkaabcdefghijjxxx'))
