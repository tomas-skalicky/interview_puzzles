from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.multiply_2_large_numbers import multiply_2_large_numbers


class Test(TestCase):
    def test_multiply_2_large_numbers__when_11_times_13__then_result_is_143(self):
        self.assertEqual('143', multiply_2_large_numbers('11', '13'))

    def test_multiply_2_large_numbers__when_211_times_211__then_result_is_44521(self):
        self.assertEqual('44521', multiply_2_large_numbers('211', '211'))

    def test_multiply_2_large_numbers__when_211_times_0__then_result_is_0(self):
        self.assertEqual('0', multiply_2_large_numbers('211', '0'))
