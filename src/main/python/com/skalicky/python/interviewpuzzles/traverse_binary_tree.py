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
from typing import Deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_level_order(root_node: Node) -> None:
    if root_node is not None:
        nodes_to_process: Deque[Node] = deque()
        nodes_to_process.append(root_node)
        while len(nodes_to_process) > 0:
            node_to_process: Node = nodes_to_process.popleft()
            print(node_to_process.val, end=' ')
            if node_to_process.left is not None:
                nodes_to_process.append(node_to_process.left)
            if node_to_process.right is not None:
                nodes_to_process.append(node_to_process.right)
    print(end='\n')


print_level_order(None)
#
print_level_order(Node(1))
# 1
print_level_order(Node(1, Node(2), Node(3, Node(4), Node(5))))
# 1 2 3 4 5
