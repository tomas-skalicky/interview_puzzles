# Task:
#
# Given the root of a binary tree, print its level-order traversal. For example:
#
#   1
#  / \
# 2   3
#    / \
#   4   5
#
# The following tree should output 1, 2, 3, 4, 5.
#
# class Node:
#   def __init__(self, val, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
#
# def print_level_order(root):
#   # Fill this in.
#
# root = Node(1, Node(2), Node(3, Node(4), Node(5)))
# print_level_order(root)
# # 1 2 3 4 5
from collections import deque
from typing import Deque, Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


def serialize_binary_tree_by_applying_breadth_first_traversal(root_node: Optional[Node]) -> str:
    result: str = ''
    if root_node is not None:
        nodes_to_process: Deque[Node] = deque()
        nodes_to_process.append(root_node)
        while len(nodes_to_process) > 0:
            node_to_process: Node = nodes_to_process.popleft()
            result += '{} '.format(node_to_process.val)
            if node_to_process.left is not None:
                nodes_to_process.append(node_to_process.left)
            if node_to_process.right is not None:
                nodes_to_process.append(node_to_process.right)
    return result
