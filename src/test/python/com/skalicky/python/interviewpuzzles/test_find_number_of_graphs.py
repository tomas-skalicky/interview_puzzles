from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_number_of_graphs import num_connected_components


class Test(TestCase):
    def test_num_connected_components(self):
        self.assertEqual(2, num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]))
