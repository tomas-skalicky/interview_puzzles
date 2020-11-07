from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.calculate_angle_between_clock_hands import \
    calculate_angle_between_clock_hands


class Test(TestCase):
    def test_calculate_angle_between_clock_hands__when_minutes_are_30__then_hour_hand_is_in_the_middle_between_hours(
            self):
        self.assertEqual(75, calculate_angle_between_clock_hands(3, 30))

    def test_calculate_angle_between_clock_hands__when_hours_are_12_or_more__then_12_hours_are_subtracted(self):
        self.assertEqual(calculate_angle_between_clock_hands(3, 30), calculate_angle_between_clock_hands(15, 30))

    def test_calculate_angle_between_clock_hands__when_hours_are_12__then_12_hours_are_subtracted(self):
        self.assertEqual(165, calculate_angle_between_clock_hands(12, 30))

    def test_calculate_angle_between_clock_hands__when_minutes_are_0__then_angle_is_hours_module_12_multiplied_by_30(
            self):
        self.assertEqual(30, calculate_angle_between_clock_hands(1, 0))

    def test_calculate_angle_between_clock_hands__when_hours_are_0_or_12_and_minutes_are_0__then_angle_is_0(self):
        self.assertEqual(0, calculate_angle_between_clock_hands(12, 0))
