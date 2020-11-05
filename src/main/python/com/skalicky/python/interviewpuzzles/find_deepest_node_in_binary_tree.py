# Task:
#
# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).
#
# Example:
#
#     a
#    / \
#   b   c
#  /
# d
#
# The deepest node in this tree is d at depth 3.
#
# Here's a starting point:
#
# class Node(object):
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#
#   def __repr__(self):
#     # string representation
#     return self.val
#
#
# def deepest(node):
#   # Fill this in.
#
# root = Node('a')
# root.left = Node('b')
# root.left.left = Node('d')
# root.right = Node('c')
#
# print deepest(root)
# # (d, 3)
from collections import deque
from typing import Deque, Tuple


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node: Node):
    if node is None:
        return None
    else:
        nodes_to_process: Deque[Tuple[Node, int]] = deque()
        nodes_to_process.append((node, 1))
        tuple_with_max_depth: Tuple[Node, int] = nodes_to_process[0]
        while len(nodes_to_process) > 0:
            current_tuple: Tuple[Node, int] = nodes_to_process.popleft()
            node_to_process, depth = current_tuple
            if depth > tuple_with_max_depth[1]:
                tuple_with_max_depth = current_tuple
            if node_to_process.left is not None:
                nodes_to_process.append((node_to_process.left, depth + 1))
            if node_to_process.right is not None:
                nodes_to_process.append((node_to_process.right, depth + 1))
        return tuple_with_max_depth


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)
