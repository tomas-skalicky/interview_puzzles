from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.calculate_h_index_as_metric_of_scholar_impact import \
    calculate_h_index_as_metric_of_scholar_impact


class Test(TestCase):
    def test_calculate_h_index_as_metric_of_scholar_impact__when_scholar_has_no_paper__then_scholar_has_no_impact(self):
        self.assertEqual(0, calculate_h_index_as_metric_of_scholar_impact([]))

    def test_calculate_h_index_as_metric_of_scholar_impact__when_citation_counts_are_sorted_descendingly__then_h_index_is_calculated(
            self):
        self.assertEqual(3, calculate_h_index_as_metric_of_scholar_impact([5, 3, 3, 1, 0]))

    def test_calculate_h_index_as_metric_of_scholar_impact__when_citation_counts_are_not_sorted__then_h_index_is_calculated(
            self):
        self.assertEqual(3, calculate_h_index_as_metric_of_scholar_impact([3, 5, 0, 1, 3]))

    def test_calculate_h_index_as_metric_of_scholar_impact__when_there_is_1_citation_count_greater_than_3_and_3_citation_counts_equal_3__then_h_index_is_3(
            self):
        self.assertEqual(3, calculate_h_index_as_metric_of_scholar_impact([3, 5, 0, 1, 3, 3]))
