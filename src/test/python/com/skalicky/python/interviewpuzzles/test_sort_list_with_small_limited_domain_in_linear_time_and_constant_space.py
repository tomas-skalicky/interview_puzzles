from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.sort_list_with_small_limited_domain_in_linear_time_and_constant_space import \
    sort_list_with_small_limited_domain_in_linear_time_and_constant_space


class Test(TestCase):
    def test_sort_list_with_small_limited_domain_in_linear_time_and_constant_space__when_input_is_not_sorted__then_output_is_sorted(
            self):
        self.assertListEqual([1, 1, 2, 2, 3, 3, 3],
                             sort_list_with_small_limited_domain_in_linear_time_and_constant_space(
                                 [3, 3, 2, 1, 3, 2, 1]))
