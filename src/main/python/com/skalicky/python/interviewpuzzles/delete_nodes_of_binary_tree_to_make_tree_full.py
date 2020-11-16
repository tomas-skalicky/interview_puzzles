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
                result += '\n'

        return result


class ChildType(Enum):
    LEFT = 1,
    RIGHT = 2


def delete_nodes_of_binary_tree_to_make_tree_full(root_node: Optional[Node]) -> Optional[Node]:
    if root_node is None:
        return None
    else:
        new_root_node: Node = root_node
        nodes_to_process: Deque[Tuple[Node, Optional[Node], Optional[ChildType]]] = deque()
        nodes_to_process.append((root_node, None, None))
        while len(nodes_to_process) > 0:
            node_to_process, parent, parent_child_type = nodes_to_process.pop()
            right_to_replace_this: bool = node_to_process.left is None and node_to_process.right is not None
            left_to_replace_this: bool = node_to_process.left is not None and node_to_process.right is None
            if right_to_replace_this or left_to_replace_this:
                non_none_child: Node = node_to_process.right if right_to_replace_this else node_to_process.left
                if parent is None:
                    new_root_node = non_none_child
                    nodes_to_process.append((new_root_node, None, None))
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
        return new_root_node
