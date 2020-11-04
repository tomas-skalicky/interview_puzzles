from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.validate_closing_of_parentheses import Solution


class TestSolution(TestCase):
    def test_is_valid__when_closing_curly_brace_misses__then_invalid(self):
        self.assertFalse(Solution.is_valid('()(){(())'))

    def test_is_valid__when_empty_input__then_valid(self):
        self.assertTrue(Solution.is_valid(''))

    def test_is_valid__when_all_parentheses_and_brackets_and_curly_braces_are_properly_closed__then_valid(self):
        self.assertTrue(Solution.is_valid('([{}])()'))

    def test_is_valid__when_multiple_nesting_and_all_parentheses_are_properly_closed__then_valid(self):
        self.assertTrue(Solution.is_valid('((()))'))
