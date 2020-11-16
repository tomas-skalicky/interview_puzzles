from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_3_numbers_in_list_having_sum_closest_to_target_number import \
    find_3_numbers_in_list_having_sum_closest_to_target_number


class Test(TestCase):
    def test_find_3_numbers_in_list_having_sum_closest_to_target_number__when_list_contains_less_than_3_numbers__then_exception_is_thrown(
            self):
        self.assertRaisesRegex(RuntimeError, 'The input list contains less numbers \\[2\\] than required 3.',
                               find_3_numbers_in_list_having_sum_closest_to_target_number, [4, 3], -2)

    def test_find_3_numbers_in_list_having_sum_closest_to_target_number__when_list_contains_exactly_3_numbers__then_list_is_result(
            self):
        self.assertSetEqual({4, 3, -2}, find_3_numbers_in_list_having_sum_closest_to_target_number([4, 3, -2], -2))

    def test_find_3_numbers_in_list_having_sum_closest_to_target_number__when_list_contains_only_1_triple_having_target_sum__then_this_triple_is_result(
            self):
        self.assertSetEqual({0, 44, -2},
                            find_3_numbers_in_list_having_sum_closest_to_target_number([33, 0, 44, 3, -2], 42))

    def test_find_3_numbers_in_list_having_sum_closest_to_target_number__when_list_does_not_contain_triples_having_target_sum__then_triple_having_closest_sum_is_result(
            self):
        self.assertSetEqual({0, 44, -2},
                            find_3_numbers_in_list_having_sum_closest_to_target_number([33, 0, 44, 3, -2], 40))

    def test_find_3_numbers_in_list_having_sum_closest_to_target_number__when_list_does_not_contain_triples_having_target_sum_and_there_are_multiple_triples_having_closest_sum__then_1_such_triple_is_result(
            self):
        self.assertSetEqual({0, 44, -3},
                            find_3_numbers_in_list_having_sum_closest_to_target_number([33, 0, 44, -3, 10], 42))
