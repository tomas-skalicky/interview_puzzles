from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_continuous_sub_array_with_target_sum import \
    find_continuous_sub_array_with_target_sum


class Test(TestCase):
    def test_find_continuous_sub_array_with_target_sum__when_input_does_not_contain_sub_array_with_target_sum__then_result_is_none(
            self):
        self.assertIsNone(find_continuous_sub_array_with_target_sum([1, 3, 2, 5, 6, 2], 14))

    def test_find_continuous_sub_array_with_target_sum__when_input_contains_sub_array_with_target_sum__then_result_is_that_sub_array(
            self):
        self.assertListEqual([2, 5, 7], find_continuous_sub_array_with_target_sum([1, 3, 2, 5, 7, 2], 14))
