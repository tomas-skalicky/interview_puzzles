from unittest import TestCase

from src.main.python.com.skalicky.python.advertofcode2022.task_02__rock_paper_scissors import Solution
from src.test.python.com.skalicky.python.advertofcode2022.Advertofcode2022Constants import Advertofcode2022Constants


class TestSolution(TestCase):
    def test_task_02_part_1__when_valid__then_sum(self):
        self.assertEqual(15, Solution().task_02_part_1(
            "{}/task_02__rock_paper_scissors__sample_input.txt".format(
                Advertofcode2022Constants.absolute_path_to_this_folder)))

    def test_task_02_part_2__when_valid__then_sum(self):
        self.assertEqual(12, Solution().task_02_part_2(
            "{}/task_02__rock_paper_scissors__sample_input.txt".format(
                Advertofcode2022Constants.absolute_path_to_this_folder)))
