from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_shortest_task_plan_with_cooldown_when_reordering_possible import \
    schedule_tasks


class Test(TestCase):
    def test_schedule_tasks__when_one_task_has_a_lower_occurrence_and_it_equals_1__then_that_task_is_scheduled_in_cooldowns_of_others(
            self):
        self.assertEqual(['q', 'w', 's', None, 'q', 'w'], schedule_tasks(['q', 's', 'q', 'w', 'w'], 3))

    def test_schedule_tasks__when_one_task_has_a_lower_occurrence_and_it_is_greater_than_1__then_that_task_is_scheduled_in_cooldowns_of_others(
            self):
        self.assertEqual(['q', 'w', 's', None, None, 'q', 'w', 's', None, None, 'q', 'w'],
                         schedule_tasks(['q', 's', 'q', 'w', 'w', 'q', 's', 'w'], 4))

    def test_schedule_tasks__when_one_task_has_a_lower_occurrence_by_2_than_some_and_higher_occurrence_by_1_than_some__then_that_task_is_scheduled_in_cooldowns_of_others(
            self):
        self.assertEqual(['q', 's', 'h', 'q', 'r', 's', 'q', None, None, 'q'],
                         schedule_tasks(['q', 'q', 'q', 'q', 's', 's', 'h', 'r'], 2))

    def test_schedule_tasks__when_one_task_has_a_lower_occurrence_by_2_than_some_and_higher_occurrence_by_2_than_some__then_that_task_is_scheduled_in_cooldowns_of_others(
            self):
        self.assertEqual(['q', 's', 'h', 'q', 's', 'r', 'q', 's', None, 'q', None, None, 'q'],
                         schedule_tasks(['q', 'q', 'q', 'q', 'q', 's', 's', 's', 'h', 'r'], 2))
