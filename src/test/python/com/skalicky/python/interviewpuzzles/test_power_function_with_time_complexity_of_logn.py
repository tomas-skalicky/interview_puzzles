from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.power_function_with_time_complexity_of_logn import \
    power_function_with_time_complexity_of_logn


class Test(TestCase):
    def test_power_function_with_time_complexity_of_logn__when_5_power_3__then_125(self):
        self.assertEqual(125, power_function_with_time_complexity_of_logn(5, 3))

    def test_power_function_with_time_complexity_of_logn__when_2_power_11__then_minus_2048(self):
        self.assertEqual(2048, power_function_with_time_complexity_of_logn(2, 11))

    def test_power_function_with_time_complexity_of_logn__when_1_power_12__then_1(self):
        self.assertEqual(1, power_function_with_time_complexity_of_logn(1, 12))

    def test_power_function_with_time_complexity_of_logn__when_minus_1_power_65__then_minus_1(self):
        self.assertEqual(-1, power_function_with_time_complexity_of_logn(-1, 65))

    def test_power_function_with_time_complexity_of_logn__when_half_power_2__then_quarter(self):
        self.assertEqual(0.25, power_function_with_time_complexity_of_logn(0.5, 2))

    def test_power_function_with_time_complexity_of_logn__when_3_power_0__then_1(self):
        self.assertEqual(1, power_function_with_time_complexity_of_logn(3, 0))
