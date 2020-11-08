# Task:
#
# You are given the root of a binary tree. Invert the binary tree in place. That is, all left children should become
# right children, and all right children should become left children.
#
# Example:
#
#     a
#    / \
#   b   c
#  / \  /
# d   e f
#
# The inverted version of this tree is as follows:
#
#   a
#  / \
#  c  b
#  \  / \
#   f e  d
#
# Here is the function signature:
#
# class Node:
#   def __init__(self, value):
#     self.left = None
#     self.right = None
#     self.value = value
#   def preorder(self):
#     print self.value,
#     if self.left: self.left.preorder()
#     if self.right: self.right.preorder()
#
# def invert(node):
#   # Fill this in.
#
# root = Node('a')
# root.left = Node('b')
# root.right = Node('c')
# root.left.left = Node('d')
# root.left.right = Node('e')
# root.right.left = Node('f')
#
# root.preorder()
# # a b d e c f
# print "\n"
# invert(root)
# root.preorder()
# # a c f b e d
from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def preorder(self) -> str:
        preorder_string: str = '{} '.format(self.value)
        if self.left is not None:
            preorder_string += self.left.preorder()
        if self.right is not None:
            preorder_string += self.right.preorder()
        return preorder_string


def invert_binary_tree(root_node: Node):
    backup: Node = root_node.right
    root_node.right = root_node.left
    root_node.left = backup
    if root_node.left is not None:
        invert_binary_tree(root_node.left)
    if root_node.right is not None:
        invert_binary_tree(root_node.right)
