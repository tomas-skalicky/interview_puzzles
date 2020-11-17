from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.collect_binary_tree_nodes_in_zigzag_order import \
    Node, collect_binary_tree_nodes_in_zigzag_order


class Test(TestCase):
    def test_collect_binary_tree_nodes_in_zigzag_order__when_tree_has_odd_number_of_levels__then_last_level_is_collected_from_left_to_right(
            self):
        #         1
        #       /   \
        #      2     3
        #     / \   / \
        #    4   5 6   7
        node4: Node = Node(4)
        node5: Node = Node(5)
        node6: Node = Node(6)
        node7: Node = Node(7)
        node2: Node = Node(2, node4, node5)
        node3: Node = Node(3, node6, node7)
        node1: Node = Node(1, node2, node3)
        self.assertListEqual([1, 3, 2, 4, 5, 6, 7], collect_binary_tree_nodes_in_zigzag_order(node1))

    def test_collect_binary_tree_nodes_in_zigzag_order__when_tree_has_even_number_of_levels__then_last_level_is_collected_from_right_to_left(
            self):
        #         1
        #       /   \
        #      2     3
        #     / \   / \
        #    4   5 6   7
        #       /   \
        #      8     9
        node8: Node = Node(8)
        node9: Node = Node(9)
        node4: Node = Node(4)
        node5: Node = Node(5, node8)
        node6: Node = Node(6, right=node9)
        node7: Node = Node(7)
        node2: Node = Node(2, node4, node5)
        node3: Node = Node(3, node6, node7)
        node1: Node = Node(1, node2, node3)
        self.assertListEqual([1, 3, 2, 4, 5, 6, 7, 9, 8], collect_binary_tree_nodes_in_zigzag_order(node1))
