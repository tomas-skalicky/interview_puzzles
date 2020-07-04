# Task:
#
# A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of unival
# subtrees in the tree.
#
# For example, the following tree should return 5:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
#
# The 5 trees are:
# - The three single '1' leaf nodes. (+3)
# - The single '0' leaf node. (+1)
# - The [1, 1, 1] tree at the bottom. (+1)
#
# Here's a starting point:
#
# class Node(object):
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#
# def count_unival_subtrees(root):
#   # Fill this in.
#
# a = Node(0)
# a.left = Node(1)
# a.right = Node(0)
# a.right.left = Node(1)
# a.right.right = Node(0)
# a.right.left.left = Node(1)
# a.right.left.right = Node(1)
#
# print count_unival_subtrees(a)
# # 5
from collections import deque
from typing import Deque


class Node(object):
    def __init__(self, val):
        self.val: int = val
        self.left: Node = None
        self.right: Node = None
        self.unival_subtree_root: bool = None


def count_unival_subtrees(root: Node):
    nodes_to_process: Deque[Node] = deque()
    nodes_to_process.append(root)
    result_count: int = 0
    while len(nodes_to_process) > 0:
        current_node: Node = nodes_to_process.pop()
        left_node: Node = current_node.left
        right_node: Node = current_node.right
        left_needs_to_be_processed: bool = left_node is not None and left_node.unival_subtree_root is None
        right_needs_to_be_processed: bool = right_node is not None and right_node.unival_subtree_root is None
        if left_needs_to_be_processed or right_needs_to_be_processed:
            nodes_to_process.append(current_node)
        if left_needs_to_be_processed:
            nodes_to_process.append(left_node)
        if right_needs_to_be_processed:
            nodes_to_process.append(right_node)

        if not left_needs_to_be_processed and not right_needs_to_be_processed:
            current_node.unival_subtree_root = ((
                                                        left_node is not None and left_node.unival_subtree_root and left_node.val == current_node.val) or left_node is None) and (
                                                       (
                                                               right_node is not None and right_node.unival_subtree_root and right_node.val == current_node.val) or right_node is None)
            if current_node.unival_subtree_root:
                result_count = result_count + 1
    return result_count


a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
print(count_unival_subtrees(a))
# 5

b = Node(0)
b.left = Node(1)
b.right = Node(0)
b.right.left = Node(1)
b.right.right = Node(0)
b.right.left.left = Node(1)
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   /
#  1
print(count_unival_subtrees(b))
# 4
