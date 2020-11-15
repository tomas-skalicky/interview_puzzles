from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.calculate_intersection_area_of_two_rectangles import \
    calculate_intersection_area_of_two_rectangles, Rectangle


class Test(TestCase):
    def test_calculate_intersection_area_of_two_rectangles__when_rectangles_do_not_overlap_or_touch_each_other__then_intersection_is_0(
            self):
        # Rectangles look like this
        #
        # 3     B
        # 2     B
        # 1
        # 0 AAA
        #   01234
        #
        # A ... rectangle 1
        # B ... rectangle 2
        self.assertEqual(0, calculate_intersection_area_of_two_rectangles(Rectangle(0, 0, 3, 1), Rectangle(4, 2, 5, 4)))

    def test_calculate_intersection_area_of_two_rectangles__when_rectangles_touch_each_other_but_do_not_overlap__then_intersection_is_0(
            self):
        # Rectangles look like this
        #
        # 2    B
        # 1 AAAB
        # 0 AAA
        #   0123
        #
        # A ... rectangle 1
        # B ... rectangle 2
        self.assertEqual(0, calculate_intersection_area_of_two_rectangles(Rectangle(0, 0, 3, 2), Rectangle(3, 1, 4, 3)))

    def test_calculate_intersection_area_of_two_rectangles__when_rectangles_overlap_entirely__then_intersection_is_area_of_each(
            self):
        # Rectangles look like this
        #
        # 1 XXX
        # 0 XXX
        #   012
        #
        # X ... both rectangle 1 and 2
        self.assertEqual(6, calculate_intersection_area_of_two_rectangles(Rectangle(0, 0, 3, 2), Rectangle(0, 0, 3, 2)))

    def test_calculate_intersection_area_of_two_rectangles__when_rectangles_overlap_partially__then_intersection_is_less_then_their_area(
            self):
        # Rectangles look like this
        #
        # 2  BB
        # 1 AXX
        # 0 AAA
        #   012
        #
        # A ... rectangle 1
        # B ... rectangle 2
        # X ... both rectangle 1 and 2
        self.assertEqual(2, calculate_intersection_area_of_two_rectangles(Rectangle(0, 0, 3, 2), Rectangle(1, 1, 3, 3)))
