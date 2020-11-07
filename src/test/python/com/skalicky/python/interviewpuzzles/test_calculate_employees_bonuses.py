from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.calculate_employees_bonuses import calculate_employees_bonuses


class Test(TestCase):
    def test_calculate_employees_bonuses__when_there_are_7_performance__then_there_are_7_bonuses(self):
        self.assertListEqual([1, 2, 3, 1, 2, 3, 1], calculate_employees_bonuses([1, 2, 3, 2, 3, 5, 1]))
