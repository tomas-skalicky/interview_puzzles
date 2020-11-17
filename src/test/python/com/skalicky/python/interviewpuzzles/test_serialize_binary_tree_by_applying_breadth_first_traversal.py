from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.serialize_binary_tree_by_applying_breadth_first_traversal import \
    Node, serialize_binary_tree_by_applying_breadth_first_traversal


class Test(TestCase):
    def test_serialize_binary_tree_by_applying_breadth_first_traversal__when_root_is_none__then_result_is_empty(self):
        self.assertEqual('', serialize_binary_tree_by_applying_breadth_first_traversal(None))

    def test_serialize_binary_tree_by_applying_breadth_first_traversal__when_tree_contains_only_1_node__then_result_contains_only_1_value(
            self):
        self.assertEqual('1 ', serialize_binary_tree_by_applying_breadth_first_traversal(Node(1)))

    def test_serialize_binary_tree_by_applying_breadth_first_traversal__when_tree_contains_6_nodes___then_tree_is_serialized_by_levels_from_left_to_right(
            self):
        #     1
        #    / \
        #   2   3
        #  /   / \
        # 6   4   5
        left_child: Node = Node(2, Node(6))
        right_child: Node = Node(3, Node(4), Node(5))
        root_node: Node = Node(1, left_child, right_child)
        self.assertEqual('1 2 3 6 4 5 ', serialize_binary_tree_by_applying_breadth_first_traversal(root_node))
