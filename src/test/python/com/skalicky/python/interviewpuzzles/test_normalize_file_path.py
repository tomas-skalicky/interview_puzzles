from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.normalize_file_path import normalize_file_path


class Test(TestCase):
    def test_normalize_file_path__when_input_is_absolute_path_with_parent_and_current_paths__then_input_is_normalized(
            self):
        self.assertEqual('/Users/Joma/', normalize_file_path('/Users/Joma/Documents/../Desktop/./../'))

    def test_normalize_file_path__when_input_is_only_current_path__then_result_is_current_path(self):
        self.assertEqual('./', normalize_file_path('./'))

    def test_normalize_file_path__when_input_is_only_parent_path__then_result_is_parent_path(self):
        self.assertEqual('../', normalize_file_path('../'))

    def test_normalize_file_path__when_input_is_relative_path_with_parent_and_current_paths__then_input_is_normalized(
            self):
        self.assertEqual('../', normalize_file_path('../Desktop/./../'))
