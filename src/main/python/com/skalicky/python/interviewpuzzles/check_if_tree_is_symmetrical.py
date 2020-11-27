# Task:
#
# A k-ary tree is a tree with k-children, and a tree is symmetrical if the data of the left side of the tree is the same
# as the right side of the tree.
#
# Here's an example of a symmetrical k-ary tree.
#         4
#      /     \
#     3        3
#   / | \    / | \
# 9   4  1  1  4  9
# Given a k-ary tree, figure out if the tree is symmetrical.
#
# Here is a starting point:
#
# class Node():
#     def __init__(self, value, children=[]):
#         self.value = value
#         self.children = children
#
# def check_if_tree_is_symmetrical(root_node):
#     # Fill this in.
#
# tree = Node(4)
# tree.children = [Node(3), Node(3)]
# tree.children[0].children = [Node(9), Node(4), Node(1)]
# tree.children[1].children = [Node(1), Node(4), Node(9)]
# print check_if_tree_is_symmetrical(tree)
# # True
from collections import deque
from math import floor
from typing import Deque, Optional, Tuple


class Node:
    def __init__(self, value: int, children: Tuple = ()):
        self.value: int = value
        self.children: Tuple = children


def check_if_tree_is_symmetrical(root_node: Optional[Node]) -> bool:
    if root_node is None:
        return True
    else:
        nodes_to_compare: Deque[Tuple[Node, Node]] = deque()
        root_children_count: int = len(root_node.children)
        if root_children_count % 2 == 1:
            return False
        else:
            for i in range(0, floor(root_children_count / 2)):
                nodes_to_compare.append((root_node.children[i], root_node.children[root_children_count - 1 - i]))
            while len(nodes_to_compare) > 0:
                node1_to_compare, node2_to_compare = nodes_to_compare.pop()
                node1_children_count: int = len(node1_to_compare.children)
                if node1_to_compare.value != node2_to_compare.value or node1_children_count != len(
                        node2_to_compare.children):
                    return False
                else:
                    for i in range(0, node1_children_count):
                        nodes_to_compare.append(
                            (node1_to_compare.children[i], node2_to_compare.children[node1_children_count - 1 - i]))
            return True
