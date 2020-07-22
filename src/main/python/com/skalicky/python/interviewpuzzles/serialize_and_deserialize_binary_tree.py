# Task:
#
# You are given the root of a binary tree. You need to implement 2 functions:
#
# 1. serialize(root) which serializes the tree into a string representation
# 2. deserialize(s) which deserializes the string back to the original tree that it represents
#
# For this problem, often you will be asked to design your own serialization format. However, for simplicity, let's use
# the pre-order traversal of the tree. Here's your starting point:
#
# class Node:
#   def __init__(self, val, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
#
#   def __str__(self):
#     # pre-order printing of the tree.
#     result = ''
#     result += str(self.val)
#     if self.left:
#       result += str(self.left)
#     if self.right:
#       result += str(self.right)
#     return result
#
# def serialize(root):
#   # Fill this in.
#
# def deserialize(data):
#   # Fill this in.
#
# #     1
# #    / \
# #   3   4
# #  / \   \
# # 2   5   7
# tree = Node(1)
# tree.left = Node(3)
# tree.left.left = Node(2)
# tree.left.right = Node(5)
# tree.right = Node(4)
# tree.right.right = Node(7)
#
# print serialize(tree)
# # 1 3 2 # # 5 # # 4 # 7 # #
# print deserialize('1 3 2 # # 5 # # 4 # 7 # #')
# # 132547
from collections import deque
from enum import Enum
from typing import List, Deque, Tuple


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val: int = val
        self.left: Node = left
        self.right: Node = right

    def __str__(self) -> str:
        # pre-order printing of the tree.
        result: str = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


class ChildType(Enum):
    LEFT = 1,
    RIGHT = 2


def serialize(root: Node) -> str:
    if root is None:
        return ''
    else:
        result: str = str(root.val)
        nodes_to_process: Deque[Tuple[Node, ChildType]] = deque()
        nodes_to_process.append((root, ChildType.RIGHT))
        nodes_to_process.append((root, ChildType.LEFT))
        while len(nodes_to_process) > 0:
            node_to_process, child_type = nodes_to_process.pop()
            child_node_to_process: Node = node_to_process.left if child_type == ChildType.LEFT else node_to_process.right
            if child_node_to_process is not None:
                result += ' {}'.format(str(child_node_to_process.val))
                nodes_to_process.append((child_node_to_process, ChildType.RIGHT))
                nodes_to_process.append((child_node_to_process, ChildType.LEFT))
            else:
                result += ' #'
        return result


def deserialize(data: str) -> Node:
    if len(data) == 0:
        return None
    else:
        node_values: List[str] = data.split()
        root: Node = Node(int(node_values[0]))
        nodes_to_process: Deque[Tuple[Node, ChildType]] = deque()
        nodes_to_process.append((root, ChildType.RIGHT))
        nodes_to_process.append((root, ChildType.LEFT))
        for i in range(1, len(node_values)):
            current_value: str = node_values[i]
            node_to_process, child_type = nodes_to_process.pop()
            if str.isnumeric(current_value):
                new_node: Node = Node(int(current_value))
                if child_type == ChildType.LEFT:
                    node_to_process.left = new_node
                else:
                    node_to_process.right = new_node
                nodes_to_process.append((new_node, ChildType.RIGHT))
                nodes_to_process.append((new_node, ChildType.LEFT))
        if len(nodes_to_process) > 0:
            raise Exception('Invalid representation of tree: {}'.format(data))
        return root


#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serialize(tree))
# 1 3 2 # # 5 # # 4 # 7 # #
print(serialize(None))
# ''
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
# 132547
print(deserialize(''))
# None
