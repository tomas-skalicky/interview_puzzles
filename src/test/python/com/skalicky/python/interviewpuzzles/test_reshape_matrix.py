from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.reshape_matrix import reshape_matrix


class Test(TestCase):
    def test_reshape_matrix__when_number_of_elements_in_new_matrix_would_be_different__then_result_is_none(self):
        self.assertIsNone(reshape_matrix([[1, 2], [3, 4]], 2, 3))

    def test_reshape_matrix__when_input_matrix_is_2x2_and_new_matrix_should_be_4x1__then_new_matrix_is_returned(self):
        self.assertListEqual([[1], [2], [3], [4]], reshape_matrix([[1, 2], [3, 4]], 4, 1))

    def test_reshape_matrix__when_input_matrix_is_2x2_and_new_matrix_should_be_1x4__then_new_matrix_is_returned(self):
        self.assertListEqual([[1, 2, 3, 4]], reshape_matrix([[1, 2], [3, 4]], 1, 4))
