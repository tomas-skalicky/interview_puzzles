from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.evaluate_expression_in_human_notation import \
    evaluate_expression_in_human_notation


class Test(TestCase):
    def test_evaluate_expression_in_human_notation__when_expression_consists_only_from_positive_constant__then_result_is_constant(
            self):
        self.assertEqual(1, evaluate_expression_in_human_notation('1'))

    def test_evaluate_expression_in_human_notation__when_expression_consists_only_from_negative_constant__then_result_is_constant(
            self):
        self.assertEqual(-1, evaluate_expression_in_human_notation('- 1'))

    def test_evaluate_expression_in_human_notation__when_expression_contains_only_subtraction__then_subtraction_is_evaluated(
            self):
        self.assertEqual(1, evaluate_expression_in_human_notation('2 - 1'))

    def test_evaluate_expression_in_human_notation__when_expression_contains_parentheses_wrapping_rest_of_expression__then_parentheses_have_no_influence_on_result(
            self):
        self.assertEqual(1, evaluate_expression_in_human_notation('( 2 - 1 )'))

    def test_evaluate_expression_in_human_notation__when_expression_contains_parentheses_not_wrapping_entire_rest_of_expression__then_parentheses_may_have_influence_on_result(
            self):
        self.assertEqual(4, evaluate_expression_in_human_notation('3 + ( 2 - 1 )'))

    def test_evaluate_expression_in_human_notation__when_expression_contains_parentheses_and_minus_in_front_of_them__then_result_of_parentheses_is_multiplied_by_minus_1(
            self):
        self.assertEqual(-4, evaluate_expression_in_human_notation('- (3 + ( 2 - 1 ) )'))

    def test_evaluate_expression_in_human_notation__when_expression_contains_double_negations__then_double_negations_cancel_themselves(
            self):
        self.assertEqual(5, evaluate_expression_in_human_notation('- (-3 + 1 + -( 2 - -(-1) ) - 2 )'))
