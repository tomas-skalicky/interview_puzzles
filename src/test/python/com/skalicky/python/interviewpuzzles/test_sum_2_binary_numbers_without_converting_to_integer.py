from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.sum_2_binary_numbers_without_converting_to_integer import \
    sum_2_binary_numbers_without_converting_to_integer


class Test(TestCase):
    def test_sum_2_binary_numbers_without_converting_to_integer__when_0_plus_0__then_result_is_0(self):
        self.assertEqual('0', sum_2_binary_numbers_without_converting_to_integer('0', '0'))

    def test_sum_2_binary_numbers_without_converting_to_integer__when_0_plus_1__then_result_is_1(self):
        self.assertEqual('1', sum_2_binary_numbers_without_converting_to_integer('0', '1'))

    def test_sum_2_binary_numbers_without_converting_to_integer__when_1_plus_1__then_result_is_10(self):
        self.assertEqual('10', sum_2_binary_numbers_without_converting_to_integer('1', '1'))

    def test_sum_2_binary_numbers_without_converting_to_integer__when_11101_plus_1011__then_result_is_101000(self):
        self.assertEqual('101000', sum_2_binary_numbers_without_converting_to_integer('11101', '1011'))
