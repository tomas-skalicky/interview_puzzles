from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.reverse_integer_without_converting_it_to_string import \
    reverse_integer_without_converting_it_to_string


class Test(TestCase):
    def test_reverse_integer_without_converting_it_to_string__when_integer_is_0__then_result_is_0(self):
        self.assertEqual(0, reverse_integer_without_converting_it_to_string(0))

    def test_reverse_integer_without_converting_it_to_string__when_integer_is_positive__then_result_is_positive(self):
        self.assertEqual(135, reverse_integer_without_converting_it_to_string(531))

    def test_reverse_integer_without_converting_it_to_string__when_integer_is_negative__then_result_is_negative(self):
        self.assertEqual(-1234, reverse_integer_without_converting_it_to_string(-4321))
