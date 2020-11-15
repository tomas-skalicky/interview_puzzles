from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.calculate_xth_pascal_triangle_row import \
    calculate_xth_pascal_triangle_row


class Test(TestCase):
    def test_calculate_xth_pascal_triangle_row__when_x_is_0__then_list_contains_exactly_1(self):
        self.assertListEqual([1], calculate_xth_pascal_triangle_row(0))

    def test_calculate_xth_pascal_triangle_row__when_x_is_1__then_list_contains_exactly_1_1(self):
        self.assertListEqual([1, 1], calculate_xth_pascal_triangle_row(1))

    def test_calculate_xth_pascal_triangle_row__when_x_is_2__then_list_contains_exactly_1_2_1(self):
        self.assertListEqual([1, 2, 1], calculate_xth_pascal_triangle_row(2))

    def test_calculate_xth_pascal_triangle_row__when_x_is_5__then_list_contains_exactly_1_5_10_10_5_1(self):
        self.assertListEqual([1, 5, 10, 10, 5, 1], calculate_xth_pascal_triangle_row(5))
