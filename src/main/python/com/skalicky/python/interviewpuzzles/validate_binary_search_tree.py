# Task:
#
# You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise.
# Recall that a binary search tree has the property that all values in the left subtree are less than or equal
# to the root, and all values in the right subtree are greater than or equal to the root.
#
# Here's a starting point:
#
# class TreeNode:
#   def __init__(self, key):
#     self.left = None
#     self.right = None
#     self.key = key
#
# def is_bst(root):
#   # Fill this in.
#
# a = TreeNode(5)
# a.left = TreeNode(3)
# a.right = TreeNode(7)
# a.left.left = TreeNode(1)
# a.left.right = TreeNode(4)
# a.right.left = TreeNode(6)
# print is_bst(a)
#
# #    5
# #   / \
# #  3   7
# # / \ /
# #1  4 6
from collections import deque
from typing import Deque, Tuple, Optional


class TreeNode:
    def __init__(self, key):
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.key: int = key


def validate_binary_search_tree(root_node: TreeNode) -> bool:
    nodes_to_process: Deque[Tuple[TreeNode, Optional[int], Optional[int]]] = deque()
    nodes_to_process.append((root_node, None, None))
    while len(nodes_to_process) > 0:
        current_node, min_allowed, max_allowed = nodes_to_process.popleft()
        if current_node.left is not None:
            if current_node.left.key >= current_node.key:
                return False
            elif min_allowed is not None and current_node.left.key < min_allowed:
                return False
            else:
                nodes_to_process.append((current_node.left, min_allowed, current_node.key - 1))
        if current_node.right is not None:
            if current_node.right.key <= current_node.key:
                return False
            elif max_allowed is not None and current_node.right.key > max_allowed:
                return False
            else:
                nodes_to_process.append((current_node.right, current_node.key + 1, max_allowed))
    return True
