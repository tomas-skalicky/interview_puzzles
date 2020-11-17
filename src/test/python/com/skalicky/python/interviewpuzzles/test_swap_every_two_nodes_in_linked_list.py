from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.swap_every_two_nodes_in_linked_list import \
    Node, swap_every_two_nodes_in_linked_list


class Test(TestCase):
    def test_swap_every_two_nodes_in_linked_list__when_input_head_is_none__then_result_is_none(self):
        self.assertIsNone(swap_every_two_nodes_in_linked_list(None))

    def test_swap_every_two_nodes_in_linked_list__when_list_contains_only_1_node__then_there_is_no_swap(self):
        self.assertEqual('1, (None)', str(swap_every_two_nodes_in_linked_list(Node(1))))

    def test_swap_every_two_nodes_in_linked_list__when_list_contains_odd_number_of_nodes__then_last_node_is_not_swapped(
            self):
        self.assertEqual('2, (1, (4, (3, (5, (None)))))',
                         str(swap_every_two_nodes_in_linked_list(Node(1, Node(2, Node(3, Node(4, Node(5))))))))

    def test_swap_every_two_nodes_in_linked_list__when_list_contains_even_number_of_nodes__then_last_node_is_swapped(
            self):
        self.assertEqual('2, (1, (4, (3, (6, (5, (None))))))', str(
            swap_every_two_nodes_in_linked_list(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))))))
