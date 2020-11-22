from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.compare_version_numbers import Solution


class TestSolution(TestCase):
    def test_compare_version_numbers__when_versions_have_same_major_part_and_1_version_has_non_zero_patch_part__then_version_with_non_zero_patch_part_is_greater(
            self):
        self.assertEqual(1, Solution.compare_version_numbers('1.0.1', '1'))

    def test_compare_version_numbers__when_only_patch_parts_differ__then_version_with_greater_patch_part_is_greater(
            self):
        self.assertEqual(1, Solution.compare_version_numbers('1.0.33', '1.0.27'))

    def test_compare_version_numbers__when_major_parts_differ__then_version_with_greater_major_part_is_greater(self):
        self.assertEqual(-1, Solution.compare_version_numbers('0.1', '1.1'))

    def test_compare_version_numbers__when_parts_differ_only_bt_numbers_of_preceding_zeros__then_versions_equal(self):
        self.assertEqual(0, Solution.compare_version_numbers('1.01', '1.001'))

    def test_compare_version_numbers__when_versions_differ_only_by_parts_containing_zeros__then_versions_equal(self):
        self.assertEqual(0, Solution.compare_version_numbers('1.0', '1.0.0'))
