# Task:
#
# You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an integer value,
# and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.
#
# Write a function that takes this tree and evaluates the expression.
#
# Example:
#
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
#
# This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.
#
# Here's a starting point:
#
# class Node:
#   def __init__(self, val, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
#
# PLUS = "+"
# MINUS = "-"
# TIMES = "*"
# DIVIDE = "/"
#
# def evaluate(root):
#   # Fill this in.
#
# tree = Node(TIMES)
# tree.left = Node(PLUS)
# tree.left.left = Node(3)
# tree.left.right = Node(2)
# tree.right = Node(PLUS)
# tree.right.left = Node(4)
# tree.right.right = Node(5)
# print evaluate(tree)
# # 45
from collections import deque
from typing import Deque, Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __str__(self):
        return str(self.val)


PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"


def is_operator(node: Node) -> bool:
    return node is not None and (node.val == PLUS or node.val == MINUS or node.val == TIMES or node.val == DIVIDE)


def can_be_evaluated(node: Node) -> bool:
    return is_operator(node) and (node.left is None or not is_operator(node.left)) and (
            node.right is None or not is_operator(node.right))


def evaluate_operator(node: Node) -> float:
    right_side = node.right.val
    if node.val == PLUS:
        return node.left.val + right_side
    elif node.val == MINUS:
        left_side = node.left.val if node.left is not None else 0
        return left_side - right_side
    elif node.val == TIMES:
        return node.left.val * right_side
    else:
        return node.left.val / right_side


def evaluate(root: Optional[Node]) -> float:
    if root is None:
        return 0
    elif is_operator(root):
        nodes_to_process: Deque[Node] = deque()
        nodes_to_process.append(root)
        while len(nodes_to_process) > 0:
            node_to_process: Node = nodes_to_process.pop()
            if can_be_evaluated(node_to_process):
                node_to_process.val = evaluate_operator(node_to_process)
            else:
                nodes_to_process.append(node_to_process)
                if is_operator(node_to_process.left):
                    nodes_to_process.append(node_to_process.left)
                if is_operator(node_to_process.right):
                    nodes_to_process.append(node_to_process.right)
        return root.val
    else:
        return root.val


print(evaluate(None))
# 0

#     3
tree = Node(3)
print(evaluate(tree))
# 3

#   -
#    \
#    2
tree2 = Node(MINUS)
tree2.right = Node(2)
print(evaluate(tree2))
# -2

#     *
#    / \
#   5    +
#       / \
#       4  5
tree3 = Node(TIMES)
tree3.left = Node(5)
tree3.right = Node(PLUS)
tree3.right.left = Node(4)
tree3.right.right = Node(5)
print(evaluate(tree3))
# 45

#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
tree4 = Node(TIMES)
tree4.left = Node(PLUS)
tree4.left.left = Node(3)
tree4.left.right = Node(2)
tree4.right = Node(PLUS)
tree4.right.left = Node(4)
tree4.right.right = Node(5)
print(evaluate(tree4))
# 45

#     *
#    / \
#   -    /
#    \  / \
#    2  4  8
tree5 = Node(TIMES)
tree5.left = Node(MINUS)
tree5.left.right = Node(2)
tree5.right = Node(DIVIDE)
tree5.right.left = Node(4)
tree5.right.right = Node(8)
print(evaluate(tree5))
# -1.0
