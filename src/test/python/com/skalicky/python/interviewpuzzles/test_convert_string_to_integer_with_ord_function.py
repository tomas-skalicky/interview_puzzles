from unittest import TestCase
from src.main.python.com.skalicky.python.interviewpuzzles.convert_string_to_integer_with_ord_function import \
    convert_to_int


class Test(TestCase):
    def test_convert_to_int__when_input_is_negative_integer__then_conversion_works(self):
        self.assertEqual(-104, convert_to_int('-105') + 1)

    def test_convert_to_int__when_input_is_positive_integer__then_conversion_works(self):
        self.assertEqual(106, convert_to_int('105') + 1)

    def test_convert_to_int__when_input_is_integer_with_all_possible_digits__then_conversion_works(self):
        self.assertEqual(1023456799, convert_to_int('1023456798') + 1)

    def test_convert_to_int__when_input_is_invalid_integer__then_none_is_returned(self):
        self.assertIsNone(convert_to_int('10.3'))
