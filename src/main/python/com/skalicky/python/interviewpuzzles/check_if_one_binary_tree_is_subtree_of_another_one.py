# Task:
#
# Given 2 binary trees t and s, find if s has an equal subtree in t, where the structure and the values are the same.
# Return True if it exists, otherwise return False.
#
# Here's some starter code and an example:
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#   def __repr__(self):
#     return f"(Value: {self.value} Left: {self.left} Right: {self.right})"
#
# def find_subtree(s, t):
#   # Fill this in.
#
# t3 = Node(4, Node(3), Node(2))
# t2 = Node(5, Node(4), Node(-1))
# t = Node(1, t2, t3)
#
# s = Node(4, Node(3), Node(2))
# """
# Tree t:
#     1
#    / \
#   4   5
#  / \ / \
# 3  2 4 -1
#
# Tree s:
#   4
#  / \
# 3  2
# """
#
# print(find_subtree(s, t))
# # True
from collections import deque
from typing import Optional, Deque, Tuple


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def determine_tree_depth(root: Node) -> int:
    tree_depth: int = 0
    nodes_to_process: Deque[Tuple[Node, int]] = deque()
    nodes_to_process.append((root, 1))
    while len(nodes_to_process) > 0:
        node_to_process, current_depth = nodes_to_process.pop()
        has_left: bool = node_to_process.left is not None
        has_right: bool = node_to_process.right is not None
        if has_left or has_right:
            if has_left:
                nodes_to_process.append((node_to_process.left, current_depth + 1))
            if has_right:
                nodes_to_process.append((node_to_process.right, current_depth + 1))
        else:
            tree_depth = max(tree_depth, current_depth)
    return tree_depth


def check_if_same(subtree_root: Node, candidate_root: Node) -> bool:
    nodes_to_process: Deque[Tuple[Node, Node]] = deque()
    nodes_to_process.append((subtree_root, candidate_root))
    while len(nodes_to_process) > 0:
        subtree_node, candidate_node = nodes_to_process.pop()
        if subtree_node.value == candidate_node.value:
            if subtree_node.left is not None:
                if candidate_node.left is not None:
                    nodes_to_process.append((subtree_node.left, candidate_node.left))
                else:
                    return False
            if subtree_node.right is not None:
                if candidate_node.right is not None:
                    nodes_to_process.append((subtree_node.right, candidate_node.right))
                else:
                    return False
        else:
            return False
    return True


def find_subtree(subtree_root: Node, tree_root: Node) -> bool:
    subtree_depth: int = determine_tree_depth(subtree_root)
    tree_depth: int = determine_tree_depth(tree_root)

    nodes_to_process: Deque[Tuple[Node, int]] = deque()
    nodes_to_process.append((tree_root, 1))
    while len(nodes_to_process) > 0:
        node_to_process, current_depth = nodes_to_process.pop()
        if check_if_same(subtree_root, node_to_process):
            return True
        else:
            go_deeper: bool = tree_depth - current_depth >= subtree_depth
            if go_deeper:
                if node_to_process.left is not None:
                    nodes_to_process.append((node_to_process.left, current_depth + 1))
                if node_to_process.right is not None:
                    nodes_to_process.append((node_to_process.right, current_depth + 1))
    return False


t2 = Node(5, Node(4), Node(-1))
t4 = Node(3, Node(4))
t3 = Node(4, t4, Node(2))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))
'''
Tree t:
    1
   / \
  5   4
 / \ / \
4 -1 3  2
     /
    4

Tree s:
  4 
 / \
3  2 
'''

print(find_subtree(s, t))
# True

print(find_subtree(s, t3))
# True

print(find_subtree(s, t2))
# False
