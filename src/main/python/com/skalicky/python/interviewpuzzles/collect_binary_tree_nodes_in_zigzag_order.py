# Task:
#
# Given a binary tree, return the list of node values in zigzag order traversal. Here's an example
#
# # Input:
# #         1
# #       /   \
# #      2     3
# #     / \   / \
# #    4   5 6   7
# #
# # Output: [1, 3, 2, 4, 5, 6, 7]
#
#
# Here's some starter code
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
# def zigzag_order(tree):
#   # Fill this in.
#
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(6)
# n7 = Node(7)
# n2 = Node(2, n4, n5)
# n3 = Node(3, n6, n7)
# n1 = Node(1, n2, n3)
#
# print(zigzag_order(n1))
# # [1, 3, 2, 4, 5, 6, 7]
from collections import deque
from typing import List, Deque, Optional


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value: int = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


def zigzag_order(tree_root: Node) -> List[int]:
    nodes_to_process_on_current_level: Deque[Node] = deque()
    nodes_to_process_on_current_level.append(tree_root)
    nodes_to_process_on_next_level: Deque[Node] = deque()
    collected_nodes: List[int] = []
    level: int = 0
    while len(nodes_to_process_on_current_level) > 0 or len(nodes_to_process_on_next_level) > 0:
        while len(nodes_to_process_on_current_level) > 0:
            current_node: Node = nodes_to_process_on_current_level.pop()
            collected_nodes.append(current_node.value)
            if level % 2 == 0:
                if current_node.left is not None:
                    nodes_to_process_on_next_level.append(current_node.left)
                if current_node.right is not None:
                    nodes_to_process_on_next_level.append(current_node.right)
            else:
                if current_node.right is not None:
                    nodes_to_process_on_next_level.append(current_node.right)
                if current_node.left is not None:
                    nodes_to_process_on_next_level.append(current_node.left)

        deque_for_swapping: Deque[Node] = nodes_to_process_on_current_level
        nodes_to_process_on_current_level = nodes_to_process_on_next_level
        nodes_to_process_on_next_level = deque_for_swapping
        level += 1
    return collected_nodes


#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)
print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]

#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#       /   \
#      8     9
n2_8 = Node(8)
n2_9 = Node(9)
n2_4 = Node(4)
n2_5 = Node(5, n2_8)
n2_6 = Node(6, right=n2_9)
n2_7 = Node(7)
n2_2 = Node(2, n2_4, n2_5)
n2_3 = Node(3, n2_6, n2_7)
n2_1 = Node(1, n2_2, n2_3)
print(zigzag_order(n2_1))
# [1, 3, 2, 4, 5, 6, 7, 9, 8]
