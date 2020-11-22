from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_4_numbers_in_list_having_target_sum import \
    find_4_numbers_in_list_having_target_sum


class Test(TestCase):
    def test_find_4_numbers_in_list_having_target_sum__when_there_are_five_0s_in_input_list_and_target_sum_is_0__then_1_solution_exists(
            self):
        self.assertSetEqual({(0, 0, 0, 0)}, find_4_numbers_in_list_having_target_sum([0, 0, 0, 0, 0], 0))

    def test_find_4_numbers_in_list_having_target_sum__when_there_is_1_possible_solution_with_unique_numbers__then_1_solution_is_returned(
            self):
        self.assertSetEqual({(-5, -1, 3, 4)}, find_4_numbers_in_list_having_target_sum([3, 0, 1, -5, 4, 0, -1], 1))

    def test_find_4_numbers_in_list_having_target_sum__when_there_are_2_possible_solutions_with_some_number_repeated__then_2_solutions_are_returned(
            self):
        self.assertSetEqual({(-1, -1, 1, 1), (-2, 0, 1, 1)},
                            find_4_numbers_in_list_having_target_sum([1, 1, -1, 0, -2, 1, -1], 0))

    def test_find_4_numbers_in_list_having_target_sum__when_there_is_no_solution__then_result_is_empty(
            self):
        self.assertSetEqual(set(), find_4_numbers_in_list_having_target_sum([0, 0, 0, 0], 1))
