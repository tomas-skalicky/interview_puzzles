from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_minimum_number_of_operations_to_reach_target_number import \
    find_minimum_number_of_operations_to_reach_target_number


class Test(TestCase):
    def test_find_minimum_number_of_operations_to_reach_target_number__when_start_and_target_numbers_are_same__then_result_is_0(
            self):
        self.assertEqual(0, find_minimum_number_of_operations_to_reach_target_number(6, 6))

    def test_find_minimum_number_of_operations_to_reach_target_number__when_only_minus_1_once_is_needed__then_result_is_1(
            self):
        self.assertEqual(1, find_minimum_number_of_operations_to_reach_target_number(6, 5))

    def test_find_minimum_number_of_operations_to_reach_target_number__when_only_times_2_once_is_needed__then_result_is_1(
            self):
        self.assertEqual(1, find_minimum_number_of_operations_to_reach_target_number(6, 12))

    def test_find_minimum_number_of_operations_to_reach_target_number__when_minus_1_once_and_times_2_once_are_needed__then_result_is_2(
            self):
        self.assertEqual(2, find_minimum_number_of_operations_to_reach_target_number(6, 10))

    def test_find_minimum_number_of_operations_to_reach_target_number__when_times_2_once_and_minus_1_once_are_needed__then_result_is_2(
            self):
        self.assertEqual(2, find_minimum_number_of_operations_to_reach_target_number(6, 11))

    def test_find_minimum_number_of_operations_to_reach_target_number__when_times_2_more_times_are_needed__then_result_is_minimum(
            self):
        # (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
        self.assertEqual(3, find_minimum_number_of_operations_to_reach_target_number(6, 20))

    def test_find_minimum_number_of_operations_to_reach_target_number__when_start_number_is_non_negative_and_target_number_is_negative__then_result_is_different_between_numbers(
            self):
        self.assertEqual(8, find_minimum_number_of_operations_to_reach_target_number(6, -2))

    def test_find_minimum_number_of_operations_to_reach_target_number__when_start_and_target_numbers_are_negative_and_target_is_less_than_start__then_target_number_is_reachable(
            self):
        self.assertEqual(3, find_minimum_number_of_operations_to_reach_target_number(-21, -45))

    def test_find_minimum_number_of_operations_to_reach_target_number__when_start_and_target_numbers_are_negative_and_target_is_greater_than_start__then_target_number_is_not_reachable(
            self):
        self.assertRaisesRegex(RuntimeError,
                               'There is no way how we can get -2 from -3 applying operations "-1" and "\\*2".',
                               find_minimum_number_of_operations_to_reach_target_number, -3, -2)
