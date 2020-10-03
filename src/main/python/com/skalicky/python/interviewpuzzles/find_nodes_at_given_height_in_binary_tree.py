# Task:
#
# Given a binary tree, return all values given a certain height h.
#
# Here's a starting point:
#
# class Node():
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
# def valuesAtHeight(root, height):
#   # Fill this in.
#
# #     1
# #    / \
# #   2   3
# #  / \   \
# # 4   5   7
#
# a = Node(1)
# a.left = Node(2)
# a.right = Node(3)
# a.left.left = Node(4)
# a.left.right = Node(5)
# a.right.right = Node(7)
# print valuesAtHeight(a, 3)
# # [4, 5, 7]
from collections import deque
from typing import Tuple, Deque, List, Optional


class Node:
    def __init__(self, value, left=None, right=None):
        self.value: int = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


def values_at_height(root: Node, height: int):
    if height < 1:
        return []
    else:
        nodes_to_process: Deque[Tuple[Node, int]] = deque()
        nodes_to_process.append((root, 1))
        collected_values: List[int] = list()
        while len(nodes_to_process) > 0:
            node_to_process, node_height = nodes_to_process.popleft()
            if node_height == height:
                collected_values.append(node_to_process.value)
            elif node_height < height:
                if node_to_process.left is not None:
                    nodes_to_process.append((node_to_process.left, node_height + 1))
                if node_to_process.right is not None:
                    nodes_to_process.append((node_to_process.right, node_height + 1))
        return collected_values


#     1
#    / \
#   2   3
#  / \   \
# 4   5   7
#          \
#           6

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
a.right.right.right = Node(6)
print(values_at_height(a, 3))
# [4, 5, 7]

b = Node(1)
print(values_at_height(b, 2))
# []

c = Node(1)
print(values_at_height(c, 1))
# [1]

c = Node(1)
print(values_at_height(c, 0))
# []
