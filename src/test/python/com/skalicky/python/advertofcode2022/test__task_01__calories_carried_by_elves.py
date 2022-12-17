from unittest import TestCase

from src.main.python.com.skalicky.python.advertofcode2022.task_01__calories_carried_by_elves import Solution


class TestSolution(TestCase):
    def test_task_01_part_1__when_valid__then_sum(self):
        self.assertEqual(24000, Solution.task_01_part_1(
            '../../../../../resources/com/skalicky/python/advertofcode2022/task_01__calories_carried_by_elves__sample_input.txt'))

    def test_task_01_part_2__when_valid__then_sum(self):
        self.assertEqual(45000, Solution.task_01_part_2(
            '../../../../../resources/com/skalicky/python/advertofcode2022/task_01__calories_carried_by_elves__sample_input.txt'))
