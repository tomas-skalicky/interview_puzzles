from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_max_and_min_quickly import find_max_and_min_quickly


class Test(TestCase):
    def test_find_max_and_min_quickly__when_input_has_6_numbers__then_maximum_allowed_number_of_comparisons_is_9(self):
        minimum, maximum, comparison_count = find_max_and_min_quickly([3, 5, 1, 2, 4, 8])
        self.assertEqual(1, minimum)
        self.assertEqual(8, maximum)
        self.assertLessEqual(9, comparison_count)
