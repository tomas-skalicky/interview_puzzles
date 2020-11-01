from typing import Dict, List
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_all_duplicate_subtrees import Node, dup_trees, \
    calculate_node_levels, give_all_nodes_subtree_id


class Test(TestCase):
    def test_calculate_node_levels__when_input_is_valid__then_all_nodes_have_level(self):
        left_left_child: Node = Node(3)
        left_child: Node = Node(2, left_left_child)
        right_child: Node = Node(2)
        root_node: Node = Node(1, left_child, right_child)
        # How the tree looks like
        #     1
        #    / \
        #   2   2
        #  /
        # 3
        node_lists_by_levels: Dict[int, List[Node]]
        level_of_root_node: int
        node_lists_by_levels, level_of_root_node = calculate_node_levels(root_node)
        self.assertListEqual([right_child, left_left_child], node_lists_by_levels[0])
        self.assertListEqual([left_child], node_lists_by_levels[1])
        self.assertListEqual([root_node], node_lists_by_levels[2])
        self.assertEqual(2, level_of_root_node)

    def test_give_all_nodes_subtree_id__when_input_is_valid__then_all_nodes_have_subtree_id(self):
        left_left_child: Node = Node(3)
        left_child: Node = Node(2, left_left_child)
        right_child: Node = Node(2)
        root_node: Node = Node(1, left_child, right_child)
        # How the tree looks like
        #     1
        #    / \
        #   2   2
        #  /
        # 3
        subtrees_by_nodes: Dict[Node, int] = give_all_nodes_subtree_id(root_node)
        self.assertEqual(1, subtrees_by_nodes[root_node])
        self.assertEqual(2, subtrees_by_nodes[right_child])
        self.assertEqual(3, subtrees_by_nodes[left_child])
        self.assertEqual(4, subtrees_by_nodes[left_left_child])

    def test_dup_trees__when_2node_subtree_is_duplicated__then_duplicates_are_found(self):
        left_child: Node = Node(2, Node(3))
        right_child: Node = Node(2, Node(3))
        root_node: Node = Node(1, left_child, right_child)
        # How the tree looks like
        #     1
        #    / \
        #   2   2
        #  /   /
        # 3   3
        self.assertEquals('[[(3), (3)], [(2, (3)), (2, (3))]]', str(dup_trees(root_node)))
        # Expected duplicates:
        #     2    and just the left    3
        #    /
        #   3

    def test_dup_trees__when_node_value_equals_and_left_children_are_duplicates_but_right_childrens_are_not__then_not_duplicate(
            self):
        left_child: Node = Node(3, Node(1), Node(2))
        right_right_left_child: Node = Node(3, Node(1), Node(2))
        right_right_right_left_child: Node = Node(3, Node(1), Node(1))
        right_right_right_right_child: Node = Node(3, Node(1), Node(2))
        right_right_right_child: Node = Node(4, right_right_right_left_child, right_right_right_right_child)
        right_right_child: Node = Node(5, right_right_left_child, right_right_right_child)
        right_child: Node = Node(6, None, right_right_child)
        root_node: Node = Node(7, left_child, right_child)
        # How the tree looks like
        #       7
        #     /   \
        #   3       6
        #  / \        \
        # 1   2         5
        #              /   \
        #             3       4
        #            / \     /  \
        #           1   2   3    3
        #                  / \  / \
        #                  1 1  1 2
        self.assertEquals('[[(1), (1), (1), (1), (1)], [(2), (2), (2)], [(3, (1), (2)), (3, (1), (2)), (3, (1), (2))]]',
                          str(dup_trees(root_node)))
        # Expected duplicates:
        #     3    and just the leaves    1   and   2
        #    / \
        #   1   2
