# Task:
#
# Given a tree, find if the binary tree is height balanced or not. A height balanced binary tree is a tree where every
# node's 2 subtree do not differ in height by more than 1.
#
# Here's some starter code:
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
# def is_height_balanced(tree):
#   # Fill this in.
#
# #     1
# #    / \
# #   2   3
# #  /
# # 4
# n4 = Node(4)
# n3 = Node(3)
# n2 = Node(2, n4)
# n1 = Node(1, n2, n3)
#
# print(is_height_balanced(n1))
# # True
#
# #     1
# #    /
# #   2
# #  /
# # 4
# n1 = Node(1, n2)
# print(is_height_balanced(n1))
# # False
from collections import deque
from typing import Deque, Dict, Optional


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


def is_height_balanced(tree: Node) -> bool:
    max_heights_in_subtree_by_node_values: Dict[Node, int] = dict()
    nodes_to_process: Deque[Node] = deque()
    nodes_to_process.append(tree)
    while len(nodes_to_process) > 0:
        node_to_process: Node = nodes_to_process.pop()
        has_left: bool = node_to_process.left is not None
        has_right: bool = node_to_process.right is not None
        if not has_left and not has_right:
            max_heights_in_subtree_by_node_values[node_to_process] = 1
        else:
            left_has_height_set: bool = max_heights_in_subtree_by_node_values.__contains__(node_to_process.left)
            right_has_height_set: bool = max_heights_in_subtree_by_node_values.__contains__(node_to_process.right)
            if (has_left and left_has_height_set) or (has_right and right_has_height_set):
                if left_has_height_set and right_has_height_set:
                    if abs(max_heights_in_subtree_by_node_values[node_to_process.left] -
                           max_heights_in_subtree_by_node_values[node_to_process.right]) > 1:
                        return False
                    else:
                        max_heights_in_subtree_by_node_values[node_to_process] = max(
                            max_heights_in_subtree_by_node_values[node_to_process.left],
                            max_heights_in_subtree_by_node_values[node_to_process.right]) + 1
                elif has_left and left_has_height_set:
                    if max_heights_in_subtree_by_node_values[node_to_process.left] > 1:
                        return False
                    else:
                        max_heights_in_subtree_by_node_values[node_to_process] = max_heights_in_subtree_by_node_values[
                                                                                     node_to_process.left] + 1
                else:
                    if max_heights_in_subtree_by_node_values[node_to_process.right] > 1:
                        return False
                    else:
                        max_heights_in_subtree_by_node_values[node_to_process] = max_heights_in_subtree_by_node_values[
                                                                                     node_to_process.right] + 1
            else:
                nodes_to_process.append(node_to_process)
                if has_left:
                    nodes_to_process.append(node_to_process.left)
                if has_right:
                    nodes_to_process.append(node_to_process.right)
    return True


#     1
#    / \
#   2   3
#  /
# 4
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)
print(is_height_balanced(n1))
# True

#     1
#    /
#   2
#  /
# 4
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False
