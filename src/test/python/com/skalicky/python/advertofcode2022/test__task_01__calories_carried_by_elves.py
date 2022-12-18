from unittest import TestCase

from pip._internal.utils.filesystem import find_files

from src.main.python.com.skalicky.python.advertofcode2022.task_01__calories_carried_by_elves import Solution
from src.test.python.com.skalicky.python.advertofcode2022.Advertofcode2022Constants import Advertofcode2022Constants


class TestSolution(TestCase):
    def test_task_01_part_1__when_valid__then_sum(self):
        self.assertEqual(24000, Solution.task_01_part_1(
            "{}/task_01__calories_carried_by_elves__sample_input.txt".format(
                Advertofcode2022Constants.absolute_path_to_this_folder)))

    def test_task_01_part_2__when_valid__then_sum(self):
        self.assertEqual(45000, Solution.task_01_part_2(
            "{}/task_01__calories_carried_by_elves__sample_input.txt".format(
                Advertofcode2022Constants.absolute_path_to_this_folder)))
