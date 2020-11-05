from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.convert_fraction_to_decimal import convert_fraction_to_decimal


class Test(TestCase):
    def test_convert_fraction_to_decimal__when_result_decimal_has_no_recurring_digits__then_ordinary_decimal_notation_is_used(
            self):
        self.assertEqual('-1.5', convert_fraction_to_decimal(-3, 2))

    def test_convert_fraction_to_decimal__when_result_decimal_has_1st_digit_after_comma_recurring__then_1st_digit_after_comma_is_in_parentheses(
            self):
        self.assertEqual('1.(3)', convert_fraction_to_decimal(4, 3))

    def test_convert_fraction_to_decimal__when_result_decimal_has_2nd_digit_after_comma_recurring__then_2nd_digit_after_comma_is_in_parentheses(
            self):
        self.assertEqual('0.1(6)', convert_fraction_to_decimal(1, 6))

    def test_convert_fraction_to_decimal__when_result_is_whole_number__then_no_comma(
            self):
        self.assertEqual('20', convert_fraction_to_decimal(120, 6))

    def test_convert_fraction_to_decimal__when_result_decimal_has_more_digits_after_comma_recurring__then_more_digits_after_comma_are_in_parentheses(
            self):
        self.assertEqual('0.(428571)', convert_fraction_to_decimal(3, 7))
