from unittest import TestCase

from src.main.python.com.skalicky.python.advertofcode2022.task_01__calories_carried_by_elves import Solution


class TestSolution(TestCase):
    def test_part_1__when_valid__then_sum(self):
        self.assertEqual(24000, Solution.part_1(
            '../../../../../resources/com/skalicky/python/advertofcode2022/task_01__calories_carried_by_elves__sample_input.txt'))

    def test_part_2__when_valid__then_sum(self):
        self.assertEqual(45000, Solution.part_2(
            '../../../../../resources/com/skalicky/python/advertofcode2022/task_01__calories_carried_by_elves__input.txt'))
