from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.calculate_rainwater_in_puddles import \
    calculate_rainwater_in_puddles


class Test(TestCase):
    def test_calculate_rainwater_in_puddles__when_landscape_is_less_than_3_elevations_long__then_total_rainwater_is_0(
            self):
        self.assertEqual(0, calculate_rainwater_in_puddles([0, 2]))

    def test_calculate_rainwater_in_puddles__when_elevation_is_descending__then_total_rainwater_is_0(self):
        self.assertEqual(0, calculate_rainwater_in_puddles([4, 1, 0]))

    def test_calculate_rainwater_in_puddles__when_elevation_is_non_descending__then_total_rainwater_is_0(self):
        self.assertEqual(0, calculate_rainwater_in_puddles([0, 1, 1, 4]))

    def test_calculate_rainwater_in_puddles__when_landscape_is_flat__then_total_rainwater_is_0(self):
        self.assertEqual(0, calculate_rainwater_in_puddles([2, 2, 2]))

    def test_calculate_rainwater_in_puddles__when_landscape_contains_1_long_puddle_with_flat_bottom__then_total_rainwater_is_volume_of_puddle(
            self):
        self.assertEqual(6, calculate_rainwater_in_puddles([2, 0, 0, 0, 3]))

    def test_calculate_rainwater_in_puddles__when_landscape_contains_1_long_puddle_with_non_flat_bottom__then_total_rainwater_is_volume_of_puddle(
            self):
        self.assertEqual(4, calculate_rainwater_in_puddles([3, 1, 0, 1, 2]))

    def test_calculate_rainwater_in_puddles__when_landscape_contains_more_puddles__then_total_rainwater_is_their_volume(
            self):
        self.assertEqual(6, calculate_rainwater_in_puddles([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
