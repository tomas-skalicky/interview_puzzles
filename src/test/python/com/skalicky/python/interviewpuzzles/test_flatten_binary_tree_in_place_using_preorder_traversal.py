from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.flatten_binary_tree_in_place_using_preorder_traversal import \
    Node, flatten_binary_tree_in_place_using_preorder_traversal


class Test(TestCase):
    def test_flatten_binary_tree_in_place_using_preorder_traversal__when_root_has_no_children__then_output_has_1_element(
            self):
        root_node: Node = Node(2)
        flatten_binary_tree_in_place_using_preorder_traversal(root_node)
        self.assertEqual('(2, None, None)', str(root_node))

    def test_flatten_binary_tree_in_place_using_preorder_traversal__when_root_has_only_left_child__then_left_child_is_moved_to_right_child(
            self):
        root_node: Node = Node(2, Node(3))
        flatten_binary_tree_in_place_using_preorder_traversal(root_node)
        self.assertEqual('(2, None, (3, None, None))', str(root_node))

    def test_flatten_binary_tree_in_place_using_preorder_traversal__when_root_has_both_children__then_all_nodes_from_left_subtree_comes_before_nodes_from_right_subtree(
            self):
        root_node: Node = Node(2, Node(3))
        # How the tree looks like:
        #      1
        #    /   \
        #   2     3
        #  /     /
        # 5     4
        root_node: Node = Node(1, Node(2, Node(5)), Node(3, Node(4)))
        flatten_binary_tree_in_place_using_preorder_traversal(root_node)
        # How the tree should look like after flattening:
        #   1
        #    \
        #     2
        #      \
        #       5
        #        \
        #         3
        #          \
        #           4
        self.assertEqual('(1, None, (2, None, (5, None, (3, None, (4, None, None)))))', str(root_node))
