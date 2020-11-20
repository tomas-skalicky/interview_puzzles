from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.convert_decimal_to_roman import convert_decimal_to_roman


class Test(TestCase):
    def test_convert_decimal_to_roman__when_input_is_1__then_output_is_i(self):
        self.assertEqual('I', convert_decimal_to_roman(1))

    def test_convert_decimal_to_roman__when_input_is_7__then_output_is_vii(self):
        self.assertEqual('VII', convert_decimal_to_roman(7))

    def test_convert_decimal_to_roman__when_input_is_8__then_output_is_viii(self):
        self.assertEqual('VIII', convert_decimal_to_roman(8))

    def test_convert_decimal_to_roman__when_input_is_9__then_output_is_ix(self):
        self.assertEqual('IX', convert_decimal_to_roman(9))

    def test_convert_decimal_to_roman__when_input_is_48__then_output_is_xlviii(self):
        self.assertEqual('XLVIII', convert_decimal_to_roman(48))

    def test_convert_decimal_to_roman__when_input_is_90__then_output_is_xc(self):
        self.assertEqual('XC', convert_decimal_to_roman(90))

    def test_convert_decimal_to_roman__when_input_is_100__then_output_is_c(self):
        self.assertEqual('C', convert_decimal_to_roman(100))

    def test_convert_decimal_to_roman__when_input_is_400__then_output_is_cd(self):
        self.assertEqual('CD', convert_decimal_to_roman(400))

    def test_convert_decimal_to_roman__when_input_is_444__then_output_is_cdxliv(self):
        self.assertEqual('CDXLIV', convert_decimal_to_roman(444))

    def test_convert_decimal_to_roman__when_input_is_1000__then_output_is_m(self):
        self.assertEqual('M', convert_decimal_to_roman(1000))

    def test_convert_decimal_to_roman__when_input_is_1904__then_output_is_mcmiv(self):
        self.assertEqual('MCMIV', convert_decimal_to_roman(1904))

    def test_convert_decimal_to_roman__when_input_is_1910__then_output_is_mcmx(self):
        self.assertEqual('MCMX', convert_decimal_to_roman(1910))

    def test_convert_decimal_to_roman__when_input_is_3999__then_output_is_mmmcmxcix(self):
        self.assertEqual('MMMCMXCIX', convert_decimal_to_roman(3999))
