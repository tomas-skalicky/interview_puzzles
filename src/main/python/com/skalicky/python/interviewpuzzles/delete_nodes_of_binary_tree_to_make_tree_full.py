# Task:
#
# Given a binary tree, remove the nodes in which there is only 1 child, so that the binary tree is a full binary tree.
#
# So leaf nodes with no children should be kept, and nodes with 2 children should be kept as well.
#
# Here's a starting point:
#
# from collections import deque
#
# class Node(object):
#   def __init__(self, value, left=None, right=None):
#     self.left = left
#     self.right = right
#     self.value = value
#   def __str__(self):
#     q = deque()
#     q.append(self)
#     result = ''
#     while len(q):
#       num = len(q)
#       while num > 0:
#         n = q.popleft()
#         result += str(n.value)
#         if n.left:
#           q.append(n.left)
#         if n.right:
#           q.append(n.right)
#         num = num - 1
#       if len(q):
#         result += "\n"
#
#     return result
#
# def fullBinaryTree(node):
#   # Fill this in.
#
# # Given this tree:
# #     1
# #    / \
# #   2   3
# #  /   / \
# # 0   9   4
#
# # We want a tree like:
# #     1
# #    / \
# #   0   3
# #      / \
# #     9   4
#
# tree = Node(1)
# tree.left = Node(2)
# tree.right = Node(3)
# tree.right.right = Node(4)
# tree.right.left = Node(9)
# tree.left.left = Node(0)
# print fullBinaryTree(tree)
# # 1
# # 03
# # 94
from collections import deque
from enum import Enum
from typing import Deque, Optional, Tuple


class Node:
    def __init__(self, value, left=None, right=None):
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right
        self.value = value

    def __str__(self) -> str:
        q: Deque = deque()
        q.append(self)
        result = ''
        while len(q):
            num = len(q)
            while num > 0:
                n = q.popleft()
                result += str(n.value)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                num = num - 1
            if len(q):
                result += "\n"

        return result


class ChildType(Enum):
    LEFT = 1,
    RIGHT = 2


def full_binary_tree(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None
    else:
        root: Node = node
        nodes_to_process: Deque[Tuple[Node, Optional[Node], Optional[ChildType]]] = deque()
        nodes_to_process.append((node, None, None))
        while len(nodes_to_process) > 0:
            node_to_process, parent, parent_child_type = nodes_to_process.pop()
            right_to_replace_this: bool = node_to_process.left is None and node_to_process.right is not None
            left_to_replace_this: bool = node_to_process.left is not None and node_to_process.right is None
            if right_to_replace_this or left_to_replace_this:
                non_none_child: Node = node_to_process.right if right_to_replace_this else node_to_process.left
                if parent is None:
                    root = non_none_child
                    nodes_to_process.append((root, None, None))
                else:
                    if parent_child_type == ChildType.LEFT:
                        parent.left = non_none_child
                        nodes_to_process.append((non_none_child, parent, ChildType.LEFT))
                    else:
                        parent.right = non_none_child
                        nodes_to_process.append((non_none_child, parent, ChildType.RIGHT))
            elif node_to_process.left is not None and node_to_process.right is not None:
                nodes_to_process.append((node_to_process.left, node_to_process, ChildType.LEFT))
                nodes_to_process.append((node_to_process.right, node_to_process, ChildType.RIGHT))
        return root


# Given this tree:
#     1
#    / \
#   2   3
#  /   / \
# 0   9   4
#
# We want a tree like:
#     1
#    / \
#   0   3
#      / \
#     9   4
#
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)
print(full_binary_tree(tree))
# 1
# 03
# 94


# Given this tree:
#     5
#    / \
#   3   7
#      /
#     6
#
# We want a tree like:
#     5
#    / \
#   3   6
#
tree2 = Node(5)
tree2.left = Node(3)
tree2.right = Node(7)
tree2.right.left = Node(6)
print(full_binary_tree(tree2))
# 5
# 36


# Given this tree:
#     5
#      \
#       7
#      /
#     6
#
# We want a tree like:
#     6
#
tree3 = Node(5)
tree3.right = Node(7)
tree3.right.left = Node(6)
print(full_binary_tree(tree3))
# 6


# Given this tree:
#
# We want a tree like:
#
print(full_binary_tree(None))
# None
