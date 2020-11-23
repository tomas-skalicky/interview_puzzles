from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.generate_all_valid_expressions_with_given_number_of_parentheses import \
    generate_all_valid_expressions_with_given_number_of_parentheses


class Test(TestCase):
    def test_generate_all_valid_expressions_with_given_number_of_parentheses__when_number_of_parentheses_is_0__then_result_is_empty(
            self):
        self.assertListEqual([], generate_all_valid_expressions_with_given_number_of_parentheses(0))

    def test_generate_all_valid_expressions_with_given_number_of_parentheses__when_number_of_parentheses_is_1__then_there_is_only_1_expression(
            self):
        self.assertListEqual(['()'], generate_all_valid_expressions_with_given_number_of_parentheses(1))

    def test_generate_all_valid_expressions_with_given_number_of_parentheses__when_number_of_parentheses_is_3__then_there_are_5_expression(
            self):
        self.assertListEqual(['((()))', '(()())', '(())()', '()(())', '()()()'],
                             generate_all_valid_expressions_with_given_number_of_parentheses(3))
