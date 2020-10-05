# Task:
#
# Given a binary tree, find and return the largest path from root to leaf.
#
# Here's an example and some starter code:
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
# def largest_path_sum(tree):
#   # Fill this in.
#
# tree = Node(1)
# tree.left = Node(3)
# tree.right = Node(2)
# tree.right.left = Node(4)
# tree.left.right = Node(5)
# #    1
# #  /   \
# # 3     2
# #  \   /
# #   5 4
# print(largest_path_sum(tree))
# # [1, 3, 5]
from collections import deque
from typing import Optional, List, Deque, Tuple


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value: int = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


def largest_path_sum(root: Node) -> List[int]:
    current_max: int = 0
    current_largest_path: List[int] = []
    path_values_and_inherited_sum_and_current_node_to_process: Deque[Tuple[List[int], int, Node]] = deque()
    path_values_and_inherited_sum_and_current_node_to_process.append(([], 0, root))
    while len(path_values_and_inherited_sum_and_current_node_to_process) > 0:
        path_values, inherited_sum, current_node_to_process = path_values_and_inherited_sum_and_current_node_to_process.pop()
        current_sum: int = inherited_sum + current_node_to_process.value
        path_values.append(current_node_to_process.value)
        has_left: bool = current_node_to_process.left is not None
        has_right: bool = current_node_to_process.right is not None
        if has_left and has_right:
            path_values_and_inherited_sum_and_current_node_to_process.append(
                (path_values.copy(), current_sum, current_node_to_process.left))
            path_values_and_inherited_sum_and_current_node_to_process.append(
                (path_values, current_sum, current_node_to_process.right))
        elif has_left:
            path_values_and_inherited_sum_and_current_node_to_process.append(
                (path_values, current_sum, current_node_to_process.left))
        elif has_right:
            path_values_and_inherited_sum_and_current_node_to_process.append(
                (path_values, current_sum, current_node_to_process.right))
        elif current_sum > current_max:
            current_largest_path = path_values
            current_max = current_sum
    return current_largest_path


#    1
#  /   \
# 3     2
#  \   /
#   5 4
print(largest_path_sum(Node(1, Node(3, right=Node(5)), Node(2, Node(4)))))
# [1, 3, 5]

#    1
#  /   \
# 3     9
#  \
#   5
print(largest_path_sum(Node(1, Node(3, right=Node(5)), Node(9))))
# [1, 9]
