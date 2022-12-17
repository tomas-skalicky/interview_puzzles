from unittest import TestCase

from src.main.python.com.skalicky.python.advertofcode2022.task_02__rock_paper_scissors import Solution


class TestSolution(TestCase):
    def test_task_02_part_1__when_valid__then_sum(self):
        self.assertEqual(15, Solution().task_02_part_1(
            '../../../../../resources/com/skalicky/python/advertofcode2022/task_02__rock_paper_scissors__sample_input.txt'))
    def test_task_02_part_2__when_valid__then_sum(self):
        self.assertEqual(12, Solution().task_02_part_2(
            '../../../../../resources/com/skalicky/python/advertofcode2022/task_02__rock_paper_scissors__input.txt'))
