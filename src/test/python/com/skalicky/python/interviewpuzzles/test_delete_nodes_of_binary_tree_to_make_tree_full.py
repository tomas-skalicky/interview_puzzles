from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.delete_nodes_of_binary_tree_to_make_tree_full import \
    Node, delete_nodes_of_binary_tree_to_make_tree_full


class Test(TestCase):
    def test_delete_nodes_of_binary_tree_to_make_tree_full__when_root_is_none__then_result_is_none(self):
        self.assertIsNone(delete_nodes_of_binary_tree_to_make_tree_full(None))

    def test_delete_nodes_of_binary_tree_to_make_tree_full__when_tree_contains_only_inner_nodes_with_1_child__then_result_is_leaf(
            self):
        # Given this tree:
        #     5
        #      \
        #       7
        #      /
        #     6
        #
        root_node: Node = Node(5)
        root_node.right = Node(7)
        root_node.right.left = Node(6)

        # We want this tree:
        #     6
        self.assertEqual('6', str(delete_nodes_of_binary_tree_to_make_tree_full(root_node)))

    def test_delete_nodes_of_binary_tree_to_make_tree_full__when_tree_contains_1_inner_node_with_2_children_and_1_inner_node_with_1_child___then_result_is_tree_without_node_with_only_1_child(
            self):
        # Given this tree:
        #     5
        #    / \
        #   3   7
        #      /
        #     6
        #
        root_node: Node = Node(5)
        root_node.left = Node(3)
        root_node.right = Node(7)
        root_node.right.left = Node(6)

        # We want this tree:
        #     5
        #    / \
        #   3   6
        self.assertEqual('5\n36', str(delete_nodes_of_binary_tree_to_make_tree_full(root_node)))

    def test_delete_nodes_of_binary_tree_to_make_tree_full__when_tree_contains_2_inner_nodes_with_2_children_and_1_inner_node_with_1_child___then_result_is_tree_without_node_with_only_1_child(
            self):
        # Given this tree:
        #     1
        #    / \
        #   2   3
        #  /   / \
        # 0   9   4
        #
        root_node: Node = Node(1)
        root_node.left = Node(2)
        root_node.right = Node(3)
        root_node.right.right = Node(4)
        root_node.right.left = Node(9)
        root_node.left.left = Node(0)

        # We want this tree:
        #     1
        #    / \
        #   0   3
        #      / \
        #     9   4
        self.assertEqual('1\n03\n94', str(delete_nodes_of_binary_tree_to_make_tree_full(root_node)))
