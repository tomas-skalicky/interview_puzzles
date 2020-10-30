from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.split_binary_search_tree import Node, split_bst


class Test(TestCase):
    def test_split_bst__when_split_node_has_parent_with_less_value_and_grandparent_with_greater_value__then_tree_splits_between_parent_and_grandparent(
            self):
        left_child: Node = Node(1, None, Node(2))
        right_child: Node = Node(4, None, Node(5))
        root_node: Node = Node(3, left_child, right_child)
        # How the tree looks like
        #     3
        #   /   \
        #  1     4
        #   \     \
        #    2     5
        self.assertEqual('((1, None, (2)), (3, None, (4, None, (5))))', str(split_bst(root_node, 2)))
        # How the split looks like
        # 1    and   3
        #  \          \
        #   2          4
        #               \
        #                5

    def test_split_bst__when_split_node_has_parent_with_less_value_and_ancestor_with_greater_value_and_has_no_right_child__then_tree_splits_between_less_ancestor_and_greater_ancestor(
            self):
        left_child: Node = Node(-1, None, Node(0, None, Node(2, Node(1), None)))
        right_child: Node = Node(5, None, Node(6))
        root_node: Node = Node(4, left_child, right_child)
        # How the tree looks like
        #      4
        #    /   \
        # -1      5
        #  \       \
        #   0       6
        #    \
        #     2
        #    /
        #    1
        self.assertEqual('((-1, None, (0, None, (2, 1, None))), (4, None, (5, None, (6))))',
                         str(split_bst(root_node, 2)))
        # How the split looks like
        # -1    and   4
        #  \           \
        #   0           5
        #    \           \
        #     2           6
        #    /
        #    1

    def test_split_bst__when_split_node_has_parent_with_less_value_and_ancestor_with_greater_value_and_has_right_child__then_tree_splits_between_less_ancestor_and_greater_ancestor_and_between_split_node_and_its_right_child(
            self):
        left_child: Node = Node(-1, None, Node(0, None, Node(2, Node(1), Node(3))))
        right_child: Node = Node(5, None, Node(6))
        root_node: Node = Node(4, left_child, right_child)
        # How the tree looks like
        #      4
        #    /   \
        # -1      5
        #  \       \
        #   0       6
        #    \
        #     2
        #    / \
        #    1 3
        self.assertEqual('((-1, None, (0, None, (2, 1, None))), (4, (3), (5, None, (6))))',
                         str(split_bst(root_node, 2)))
        # How the split looks like
        # -1    and   4
        #  \         / \
        #   0       3   5
        #    \           \
        #     2           6
        #    /
        #    1

    def test_split_bst__when_split_node_has_parent_with_less_value_and_has_no_ancestor_with_greater_value__then_tree_splits_between_split_node_and_its_right_child(
            self):
        left_child: Node = Node(1, None, Node(2))
        right_child: Node = Node(4, None, Node(6, Node(5), Node(7)))
        root_node: Node = Node(3, left_child, right_child)
        # How the tree looks like
        #     3
        #   /   \
        #  1     4
        #   \     \
        #    2     6
        #         / \
        #         5  7
        self.assertEqual('((3, (1, None, (2)), (4, None, (6, (5), None))), (7))', str(split_bst(root_node, 6)))
        # How the split looks like
        #     3        and    7
        #   /   \
        #  1     4
        #   \     \
        #    2     6
        #         /
        #         5

    def test_split_bst__when_split_node_has_parent_with_greater_value_and_ancestor_with_less_value_and_has_right_child__then_tree_splits_between_less_ancestor_and_greater_ancestor_and_between_split_node_and_its_parent_and_between_split_node_and_its_right_child(
            self):
        right_child: Node = Node(5, Node(4, Node(2, Node(1), Node(3)), None), None)
        root_node: Node = Node(0, None, right_child)
        # How the tree looks like
        #     0
        #       \
        #        5
        #        /
        #       4
        #      /
        #     2
        #    / \
        #    1 3
        self.assertEqual('((0, None, (2, (1), None)), (5, (4, (3), None), None))', str(split_bst(root_node, 2)))
        # How the split looks like
        #      0     and      5
        #       \            /
        #        2          4
        #        /         /
        #       1         3

    def test_split_bst__when_split_node_is_root__then_tree_splits_between_root_and_its_right_child(
            self):
        left_child: Node = Node(1, None, Node(2))
        right_child: Node = Node(4, None, Node(5))
        root_node: Node = Node(3, left_child, right_child)
        # How the tree looks like
        #     3
        #   /   \
        #  1     4
        #   \     \
        #    2     5
        self.assertEqual('((3, (1, None, (2), None)), (4, None, (5)))', str(split_bst(root_node, 3)))
        # How the split looks like
        #     3        and    4
        #   /                  \
        #  1                    5
        #   \
        #    2

    def test_split_bst__when_split_node_is_root_and_has_no_right_child__then_tree_does_not_split(
            self):
        root_node: Node = Node(3, None, None)
        # How the tree looks like
        #     3
        self.assertEqual('((3), None)', str(split_bst(root_node, 3)))
        # How the split looks like
        #     3        and     <None>
