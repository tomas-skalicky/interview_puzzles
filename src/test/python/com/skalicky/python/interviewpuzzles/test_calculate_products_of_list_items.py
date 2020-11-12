from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.calculate_products_of_list_items import \
    calculate_products_of_list_items


class Test(TestCase):
    def test_calculate_products_of_list_items__when_input_is_empty__then_output_is_empty(self):
        self.assertListEqual([], calculate_products_of_list_items([]))

    def test_calculate_products_of_list_items__when_input_is_2_3_1__then_output_is_3_2_6(self):
        self.assertListEqual([3, 2, 6], calculate_products_of_list_items([2, 3, 1]))

    def test_calculate_products_of_list_items__when_input_is_1_2_3_4_5__then_output_is_120_60_40_30_24(self):
        self.assertListEqual([120, 60, 40, 30, 24], calculate_products_of_list_items([1, 2, 3, 4, 5]))
