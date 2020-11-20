from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.convert_roman_to_decimal import Solution


class TestSolution(TestCase):
    def test_convert_roman_to_decimal__when_input_is_i__then_output_is_1(self):
        self.assertEqual(1, Solution.convert_roman_to_decimal('I'))

    def test_convert_roman_to_decimal__when_input_is_vii__then_output_is_7(self):
        self.assertEqual(7, Solution.convert_roman_to_decimal('VII'))

    def test_convert_roman_to_decimal__when_input_is_viii__then_output_is_8(self):
        self.assertEqual(8, Solution.convert_roman_to_decimal('VIII'))

    def test_convert_roman_to_decimal__when_input_is_ix__then_output_is_9(self):
        self.assertEqual(9, Solution.convert_roman_to_decimal('IX'))

    def test_convert_roman_to_decimal__when_input_is_xc__then_output_is_90(self):
        self.assertEqual(90, Solution.convert_roman_to_decimal('XC'))

    def test_convert_roman_to_decimal__when_input_is_c__then_output_is_100(self):
        self.assertEqual(100, Solution.convert_roman_to_decimal('C'))

    def test_convert_roman_to_decimal__when_input_is_cd__then_output_is_400(self):
        self.assertEqual(400, Solution.convert_roman_to_decimal('CD'))

    def test_convert_roman_to_decimal__when_input_is_mvmiv__then_output_is_1904(self):
        self.assertEqual(1904, Solution.convert_roman_to_decimal('MCMIV'))

    def test_convert_roman_to_decimal__when_input_is_mcmx__then_output_is_1910(self):
        self.assertEqual(1910, Solution.convert_roman_to_decimal('MCMX'))

    def test_convert_roman_to_decimal__when_input_is_mmmcmxcix__then_output_is_3999(self):
        self.assertEqual(3999, Solution.convert_roman_to_decimal('MMMCMXCIX'))
