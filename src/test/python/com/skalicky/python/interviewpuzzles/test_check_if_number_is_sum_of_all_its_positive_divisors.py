from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.check_if_number_is_sum_of_all_its_positive_divisors import \
    Solution


class TestSolution(TestCase):
    def test_check_if_number_is_sum_of_all_its_positive_divisors__when_input_is_smaller_than_2__then_result_is_false(
            self):
        self.assertFalse(Solution.check_if_number_is_sum_of_all_its_positive_divisors(1))

    def test_check_if_number_is_sum_of_all_its_positive_divisors__when_input_is_prime_number__then_result_is_false(
            self):
        self.assertFalse(Solution.check_if_number_is_sum_of_all_its_positive_divisors(5))

    def test_check_if_number_is_sum_of_all_its_positive_divisors__when_input_is_6__then_result_is_true(
            self):
        self.assertTrue(Solution.check_if_number_is_sum_of_all_its_positive_divisors(6))

    def test_check_if_number_is_sum_of_all_its_positive_divisors__when_input_is_12__then_result_is_false(
            self):
        # 1 + 2 + 3 + 4 + 6 = 16
        self.assertFalse(Solution.check_if_number_is_sum_of_all_its_positive_divisors(12))

    def test_check_if_number_is_sum_of_all_its_positive_divisors__when_input_is_28__then_result_is_false(
            self):
        # 1 + 2 + 4 + 7 + 14 = 28
        self.assertTrue(Solution.check_if_number_is_sum_of_all_its_positive_divisors(28))
