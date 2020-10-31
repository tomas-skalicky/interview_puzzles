# Task:
#
# Given a binary search tree (BST) and a value s, split the BST into 2 trees, where one tree has all values less than
# or equal to s, and the other tree has all values greater than s while maintaining the tree structure of the original
# BST. You can assume that s will be one of the node's value in the BST. Return both tree's root node as a tuple.
#
# Here's an example and some starting code:
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#   def __repr__(self):
#     if self.left and self.right:
#       return f"({self.value}, {self.left}, {self.right})"
#     if self.left:
#       return f"({self.value}, {self.left})"
#     if self.right:
#       return f"({self.value}, None, {self.right})"
#     return f"({self.value})"
#
# def split_bst(bst, s):
#   # Fill this in.
#
# n2 = Node(2)
# n1 = Node(1, None, n2)
#
# n5 = Node(5)
# n4 = Node(4, None, n5)
#
# root = Node(3, n1, n4)
#
# print(root)
# # (3, (1, (2)), (4, None, (5)))
# # How the tree looks like
# #     3
# #   /   \
# #  1     4
# #   \     \
# #    2     5
#
# print(split_bst(root, 2))
# # ((1, None, (2)), (3, None, (4, None, (5))))
# # Split into two trees
# # 1    And   3
# #  \          \
# #   2          4
# #               \
# #                5
from collections import deque
from typing import Tuple, Optional, Deque, Dict, List


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value: int = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"


def find_path_from_root_to_node(node_value: int, root_node: Node) -> List[Node]:
    path: List[Node] = []
    current_node: Node = root_node
    while current_node.value != node_value:
        path.append(current_node)
        current_node = current_node.left if node_value < current_node.value else current_node.right
    path.append(current_node)
    return path


def split_bst(root_node: Node, split_value: int) -> Tuple[Node, Optional[Node]]:
    path: List[Node] = find_path_from_root_to_node(split_value, root_node)

    current_node: Node = path.pop()
    previous_node: Node
    last_less_node_to_hang: Optional[Node] = None
    last_greater_node_to_hang: Optional[Node] = current_node.right
    current_node.right = None
    while len(path) > 0:
        previous_node = current_node
        current_node = path.pop()
        if previous_node.value <= split_value < current_node.value:
            last_less_node_to_hang = previous_node
            current_node.left = last_greater_node_to_hang
        elif previous_node.value > split_value >= current_node.value:
            last_greater_node_to_hang = previous_node
            current_node.right = last_less_node_to_hang

    return (last_less_node_to_hang, current_node) if current_node.value > split_value else (
        current_node, last_greater_node_to_hang)
