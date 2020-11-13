from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.merge_overlapping_intervals import merge_overlapping_intervals


class Test(TestCase):
    def test_merge_overlapping_intervals__when_intervals_are_not_overlapping__then_all_are_in_result(
            self):
        self.assertListEqual([(1, 3), (4, 10)], merge_overlapping_intervals([(1, 3), (4, 10)]))

    def test_merge_overlapping_intervals__when_interval_is_subset_of_another__then_former_is_not_in_result(
            self):
        self.assertListEqual([(4, 10)], merge_overlapping_intervals([(5, 8), (4, 10)]))

    def test_merge_overlapping_intervals__when_intervals_are_not_sorted_anyhow__then_sorting_has_no_effect_on_result(
            self):
        self.assertListEqual(merge_overlapping_intervals([(1, 3), (3, 4), (4, 10)]),
                             merge_overlapping_intervals([(4, 10), (1, 3), (3, 4)]))

    def test_merge_overlapping_intervals__when_there_are_3_intervals_in_total_and_2_and_2_intervals_overlap_in_boarders__then_result_is_1_interval(
            self):
        self.assertListEqual([(-1, 4)], merge_overlapping_intervals([(-1, 3), (3, 3), (3, 4)]))

    def test_merge_overlapping_intervals__when_intervals_overlap_partially__then_result_is_union(
            self):
        self.assertListEqual([(1, 8)], merge_overlapping_intervals([(1, 5), (3, 8)]))

    def test_merge_overlapping_intervals__when_2_and_2_intervals_overlap__then_2_intervals_are_in_result(
            self):
        self.assertListEqual([(1, 4), (5, 20)], merge_overlapping_intervals([(9, 20), (1, 3), (2, 4), (5, 10)]))
