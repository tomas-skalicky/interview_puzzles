from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.transpose_matrix import transpose_matrix


class Test(TestCase):
    def test_transpose_matrix__then_input_is_matrix_2x3__then_output_is_matrix_3x2(self):
        self.assertListEqual([[1, 4], [2, 5], [3, 6]], transpose_matrix([[1, 2, 3], [4, 5, 6]]))
