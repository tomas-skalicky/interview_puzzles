from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.convert_to_binary_representation import \
    convert_to_binary_representation


class Test(TestCase):
    def test_convert_to_binary_representation__when_123__then_1111011(self):
        # 2^6 + 2^5 + 2^4 + 2^3 + 2^1 + 2^0 = 123
        self.assertEqual('1111011', convert_to_binary_representation(123))

    def test_convert_to_binary_representation__when_0__then_0(self):
        self.assertEqual('0', convert_to_binary_representation(0))

    def test_convert_to_binary_representation__when_1__then_1(self):
        self.assertEqual('1', convert_to_binary_representation(1))

    def test_convert_to_binary_representation__when_2_as_number_having_0_at_the_end_of_binary_representation__then_10(
            self):
        self.assertEqual('10', convert_to_binary_representation(2))
