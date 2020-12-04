# Task:
#
# Given a binary tree, flatten the binary tree using preorder traversal. Instead of creating a new list,
# reuse the nodes, where the list is represented by following each right child. As such the root should always be
# the first element in the list so you do not need to return anything in the implementation, just rearrange the nodes
# such that following the right child will give us the list.
#
# Here's an example and some starter code.
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#   def __repr__(self):
#     return f"({self.value}, {self.left}, {self.right})"
#
# def flatten_binary_tree_in_place_using_preorder_traversal(root):
#     # Fill this in.
#
# n5 = Node(5)
# n4 = Node(4)
# n3 = Node(3, n4)
# n2 = Node(2, n5)
# n1 = Node(1, n2, n3)
#
# #      1
# #    /   \
# #   2     3
# #  /     /
# # 5     4
#
# flatten_binary_tree_in_place_using_preorder_traversal(n1)
# print(n1)
#
# # n1 should now look like
# #   1
# #    \
# #     2
# #      \
# #       5
# #        \
# #         3
# #          \
# #           4
from collections import deque
from typing import Deque, Optional


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


def flatten_binary_tree_in_place_using_preorder_traversal(root: Node) -> None:
    nodes_to_process: Deque[Node] = deque()
    nodes_to_process.append(root)
    previous_node: Optional[Node] = None
    while len(nodes_to_process) > 0:
        node_to_process: Node = nodes_to_process.pop()

        if node_to_process.right is not None:
            nodes_to_process.append(node_to_process.right)
        if node_to_process.left is not None:
            nodes_to_process.append(node_to_process.left)

        node_to_process.left = None
        if previous_node is not None:
            previous_node.right = node_to_process

        previous_node = node_to_process
