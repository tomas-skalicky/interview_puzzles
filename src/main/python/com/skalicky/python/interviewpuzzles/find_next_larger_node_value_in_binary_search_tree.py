# Task:
#
# Given a node in a binary search tree (may not be the root), find the next largest node in the binary search tree
# (also known as an inorder successor). The nodes in this binary search tree will also have a parent field to traverse
# up the tree.
#
# Here's an example and some starter code:
#
# class Node:
#   def __init__(self, value, left=None, right=None, parent=None):
#     self.value = value
#     self.left = left
#     self.right = right
#     self.parent = parent
#
#   def __repr__(self):
#     return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"
#
# def inorder_successor(node):
#   # Fill this in.
#
# tree = Node(3)
# tree.left = Node(2)
# tree.right = Node(4)
# tree.left.parent = tree
# tree.right.parent = tree
# tree.left.left = Node(1)
# tree.left.left.parent = tree.left
# tree.right.right = Node(5)
# tree.right.right.parent = tree.right
# #     3
# #    / \
# #   2   4
# #  /     \
# # 1       5
# print(inorder_successor(tree.left))
# # 3
# print(inorder_successor(tree.right))
# # 5
from typing import Optional


class Node:
    def __init__(self, value: int, left=None, right=None, parent=None):
        self.value: int = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right
        self.parent: Optional[Node] = parent

    def __repr__(self) -> str:
        return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"


def inorder_successor(node: Node) -> Optional[int]:
    if node.right is not None:
        current_node: Node = node.right
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    else:
        if node.parent is not None:
            current_node: Node = node.parent
            if current_node.value > node.value:
                return current_node.value
            while current_node.parent is not None:
                if current_node.parent.value > node.value:
                    return current_node.parent.value
                else:
                    current_node = current_node.parent
        return None


tree = Node(3)
tree.left = Node(2)
tree.right = Node(4)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(5)
tree.right.right.parent = tree.right
#     3
#    / \
#   2   4
#  /     \
# 1       5
print(inorder_successor(tree.left))
# 3
print(inorder_successor(tree.right))
# 5
print(inorder_successor(tree.right.right))
# None

tree2 = Node(3)
tree2.left = Node(1)
tree2.right = Node(4)
tree2.left.parent = tree2
tree2.right.parent = tree2
tree2.left.right = Node(2)
tree2.left.right.parent = tree2.left
tree2.right.right = Node(7)
tree2.right.right.parent = tree2.right
tree2.right.right.left = Node(6)
tree2.right.right.left.parent = tree2.right.right
tree2.right.right.left.left = Node(5)
tree2.right.right.left.left.parent = tree2.right.right.left
#      3
#    /   \
#   1     4
#    \      \
#     2      7
#           /
#           6
#          /
#         5
print(inorder_successor(tree2.left.right))
# 3
print(inorder_successor(tree2.right))
# 5
