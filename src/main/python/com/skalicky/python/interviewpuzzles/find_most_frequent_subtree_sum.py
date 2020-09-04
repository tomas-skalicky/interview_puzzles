# Task:
#
# Given a binary tree, find the most frequent subtree sum.
#
# Example:
#
#    3
#   / \
#  1   -3
#
#
# The above tree has 3 subtrees. The root node with 3, and the 2 leaf nodes, which gives us a total of 3 subtree sums.
# The root node has a sum of 1 (3 + 1 + -3), the left leaf node has a sum of 1, and the right leaf node has a sum of -3.
# Therefore the most frequent subtree sum is 1.
#
# If there is a tie between the most frequent sum, you can return any one of them.
#
# Here's some starter code for the problem:
#
# class Node():
#   def __init__(self, value, left=None, right=None):
#     self.val = value
#     self.left = left
#     self.right = right
#
# def most_freq_subtree_sum(root):
#   # fill this in.
#
# root = Node(3, Node(1), Node(-3))
# print(most_freq_subtree_sum(root))
# # 1
from collections import deque
from typing import Deque, Dict


class Node:
    def __init__(self, value: int, left=None, right=None, subtree_sum=None):
        self.val: int = value
        self.left: Node = left
        self.right: Node = right
        self.subtree_sum: int = subtree_sum


def most_freq_subtree_sum(root: Node):
    occurrence_counts_by_sums: Dict[int, int] = dict()
    nodes_to_process: Deque[Node] = deque()
    nodes_to_process.append(root)
    while len(nodes_to_process) > 0:
        node_to_process: Node = nodes_to_process.pop()

        append_left: bool = False
        if node_to_process.left is not None:
            if node_to_process.left.subtree_sum is None:
                append_left = True
            else:
                node_to_process.subtree_sum = node_to_process.subtree_sum + node_to_process.left.subtree_sum if node_to_process.subtree_sum is not None else node_to_process.left.subtree_sum

        append_right: bool = False
        if node_to_process.right is not None:
            if node_to_process.right.subtree_sum is None:
                append_right = True
            else:
                node_to_process.subtree_sum = node_to_process.subtree_sum + node_to_process.right.subtree_sum if node_to_process.subtree_sum is not None else node_to_process.right.subtree_sum

        if append_left or append_right:
            nodes_to_process.append(node_to_process)
            if append_left:
                nodes_to_process.append(node_to_process.left)
            if append_right:
                nodes_to_process.append(node_to_process.right)
        else:
            node_to_process.subtree_sum = node_to_process.subtree_sum + node_to_process.val if node_to_process.subtree_sum is not None else node_to_process.val
            if occurrence_counts_by_sums.__contains__(node_to_process.subtree_sum):
                occurrence_counts_by_sums[node_to_process.subtree_sum] += 1
            else:
                occurrence_counts_by_sums[node_to_process.subtree_sum] = 0

    sum_with_max_occurrence_count: int = None
    max_occurrence_count: int = 0
    for current_sum in occurrence_counts_by_sums.keys():
        current_occurrence_count: int = occurrence_counts_by_sums[current_sum]
        if current_occurrence_count > max_occurrence_count:
            max_occurrence_count = current_occurrence_count
            sum_with_max_occurrence_count = current_sum
    return sum_with_max_occurrence_count


#    3
#   / \
#  1   -3
print(most_freq_subtree_sum(Node(3, Node(1), Node(-3))))
# 1

#    2
#   / \
#  4   2
#       \
#        2
print(most_freq_subtree_sum(Node(2, Node(4), Node(2, right=Node(2)))))
# 4
