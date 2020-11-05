from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.traverse_matrix_in_spiral_way import \
    traverse_matrix_in_spiral_way


class Test(TestCase):
    def test_traverse_matrix_in_spiral_way__when_matrix_is_4x5__then_properly_serialized(self):
        self.assertEqual('1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12 ',
                         traverse_matrix_in_spiral_way([[1, 2, 3, 4, 5],
                                                        [6, 7, 8, 9, 10],
                                                        [11, 12, 13, 14, 15],
                                                        [16, 17, 18, 19, 20]]))

    def test_traverse_matrix_in_spiral_way__when_matrix_is_1x1__then_result_is_same_as_input(self):
        self.assertEqual('2 ', traverse_matrix_in_spiral_way([[2]]))

    def test_traverse_matrix_in_spiral_way__when_matrix_is_empty__then_result_is_none(self):
        self.assertEqual('', traverse_matrix_in_spiral_way([[]]))
