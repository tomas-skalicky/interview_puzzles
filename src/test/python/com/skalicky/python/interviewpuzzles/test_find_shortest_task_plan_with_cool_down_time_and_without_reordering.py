from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_shortest_task_plan_with_cool_down_time_and_without_reordering import \
    find_shortest_task_plan_with_cool_down_time_and_without_reordering


class Test(TestCase):
    def test_find_shortest_task_plan_with_cool_down_time_and_without_reordering__when_same_tasks_are_ordered_so_that_cooling_down_creates_gaps_in_plan__then_plan_length_is_longer_than_length_of_input_list(
            self):
        self.assertEqual(7, find_shortest_task_plan_with_cool_down_time_and_without_reordering([1, 1, 2, 1], 2))

    def test_find_shortest_task_plan_with_cool_down_time_and_without_reordering__when_same_tasks_are_ordered_so_that_cooling_down_is_not_necessary__then_plan_length_is_same_as_length_of_input_list(
            self):
        self.assertEqual(4, find_shortest_task_plan_with_cool_down_time_and_without_reordering([1, 2, 3, 1], 1))
