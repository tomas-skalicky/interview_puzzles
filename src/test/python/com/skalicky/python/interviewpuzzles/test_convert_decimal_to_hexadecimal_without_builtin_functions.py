from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.convert_decimal_to_hexadecimal_without_builtin_functions import \
    convert_decimal_to_hexadecimal_without_builtin_functions


class Test(TestCase):
    def test_convert_decimal_to_hexadecimal_without_builtin_functions__when_input_is_123__then_result_is_7b(self):
        self.assertEqual('7B', convert_decimal_to_hexadecimal_without_builtin_functions(123))

    def test_convert_decimal_to_hexadecimal_without_builtin_functions__when_input_is_0__then_result_is_0(self):
        self.assertEqual('0', convert_decimal_to_hexadecimal_without_builtin_functions(0))

    def test_convert_decimal_to_hexadecimal_without_builtin_functions__when_input_is_9__then_result_is_9(self):
        self.assertEqual('9', convert_decimal_to_hexadecimal_without_builtin_functions(9))

    def test_convert_decimal_to_hexadecimal_without_builtin_functions__when_input_is_9__then_result_is_10(self):
        self.assertEqual('A', convert_decimal_to_hexadecimal_without_builtin_functions(10))

    def test_convert_decimal_to_hexadecimal_without_builtin_functions__when_input_is_negative__then_result_is_negative(
            self):
        self.assertEqual('-7B', convert_decimal_to_hexadecimal_without_builtin_functions(-123))
