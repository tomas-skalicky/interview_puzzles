from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.rotate_2d_nxn_matrix_by_90_degree_clockwise import \
    rotate_2d_nxn_matrix_by_90_degree_clockwise


class Test(TestCase):
    # Input:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    #
    # Expected output:
    # 7 4 1
    # 8 5 2
    # 9 6 3
    def test_rotate_2d_nxn_matrix_by_90_degree_clockwise__when_3x3__then_expected_result(self):
        self.assertListEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]],
                             rotate_2d_nxn_matrix_by_90_degree_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    # Input:
    #  1  2  3  4
    #  5  6  7  8
    #  9 10 11 12
    # 13 14 15 16
    #
    # Expected output:
    # 13  9  5  1
    # 14 10  6  2
    # 15 11  7  3
    # 16 12  8  4
    def test_rotate_2d_nxn_matrix_by_90_degree_clockwise__when_4x4__then_expected_result(self):
        self.assertListEqual([[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]],
                             rotate_2d_nxn_matrix_by_90_degree_clockwise(
                                 [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

    def test_rotate_2d_nxn_matrix_by_90_degree_clockwise__when_0x0__then_empty_list(self):
        self.assertListEqual([], rotate_2d_nxn_matrix_by_90_degree_clockwise([]))
