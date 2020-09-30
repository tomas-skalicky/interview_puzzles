# Task:
#
# Given a binary tree and an integer k, filter the binary tree such that its leaves don't contain the value k. Here are the rules:
#
# - If a leaf node has a value of k, remove it.
# - If a parent node has a value of k, and all of its children are removed, remove it.
#
# Here's an example and some starter code:
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#   def __repr__(self):
#     return f"value: {self.value}, left: ({self.left.__repr__()}), right: ({self.right.__repr__()})"
#
# def filter(tree, k):
#   # Fill this in.
#
# #     1
# #    / \
# #   1   1
# #  /   /
# # 2   1
# n5 = Node(2)
# n4 = Node(1)
# n3 = Node(1, n4)
# n2 = Node(1, n5)
# n1 = Node(1, n2, n3)
#
# print(filter(n1, 1))
# #     1
# #    /
# #   1
# #  /
# # 2
# # value: 1, left: (value: 1, left: (value: 2, left: (None), right: (None)), right: (None)), right: (None)
from collections import deque
from enum import Enum
from typing import Deque, Tuple


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Node = left
        self.right: Node = right

    def __repr__(self):
        return f"value: {self.value}, left: ({self.left.__repr__()}), right: ({self.right.__repr__()})"


class ChildType(Enum):
    LEFT = 1,
    RIGHT = 2


def filter(tree: Node, k) -> Node:
    nodes_to_process: Deque[Tuple[Node, Node, ChildType, bool]] = deque()
    nodes_to_process.append((tree, None, None, False))
    while len(nodes_to_process) > 0:
        node_to_process, parent_node, child_type, already_visited = nodes_to_process.pop()
        if not already_visited:
            nodes_to_process.append((node_to_process, parent_node, child_type, True))
            if node_to_process.left is not None:
                nodes_to_process.append((node_to_process.left, node_to_process, ChildType.LEFT, False))
            if node_to_process.right is not None:
                nodes_to_process.append((node_to_process.right, node_to_process, ChildType.RIGHT, False))
        else:
            if node_to_process.value == k and node_to_process.left is None and node_to_process.right is None:
                if child_type is None:
                    return None
                elif child_type == ChildType.LEFT:
                    parent_node.left = None
                else:
                    parent_node.right = None
    return tree


#     1
#    / \
#   1   1
#  /   /
# 2   1
print(filter(Node(1, left=Node(1, left=Node(2)), right=Node(1, left=Node(1))), 1))
#     1
#    /
#   1
#  /
# 2
# value: 1, left: (value: 1, left: (value: 2, left: (None), right: (None)), right: (None)), right: (None)

#     1
#    / \
#   1   1
#  /   /
# 2   1
print(filter(Node(1, left=Node(1, left=Node(1)), right=Node(1, left=Node(1))), 1))
# None
