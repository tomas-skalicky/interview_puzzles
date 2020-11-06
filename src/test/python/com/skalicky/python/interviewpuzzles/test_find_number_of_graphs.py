from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_number_of_graphs import find_number_of_graphs


class Test(TestCase):
    def test_find_number_of_graphs__when_edges_form_2_graphs__then_2_is_returned(self):
        self.assertEqual(2, find_number_of_graphs([(1, 2), (2, 3), (4, 1), (5, 6)]))
