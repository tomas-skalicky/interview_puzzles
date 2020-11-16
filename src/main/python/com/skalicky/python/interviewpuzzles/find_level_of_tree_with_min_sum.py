# Task:
#
# You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, and return that
# value.
#
# For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. So, the answer here
# should be 7.
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.val = value
#     self.left = left
#     self.right = right
#
# def minimum_level_sum(root):
#   # Fill this in.
#
# #     10
# #    /  \
# #   2    8
# #  / \    \
# # 4   1    2
# node = Node(10)
# node.left = Node(2)
# node.right = Node(8)
# node.left.left = Node(4)
# node.left.right = Node(1)
# node.right.right = Node(2)
#
# print minimum_level_sum(node)
import sys
from typing import Dict, List, Optional, Tuple


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


def minimum_level_sum(root: Node) -> int:
    sums_by_levels: Dict[int, int] = {}
    nodes_and_its_level_to_process: List[Tuple[Node, int]] = [(root, 0)]
    while len(nodes_and_its_level_to_process) > 0:
        node_to_process, node_level = nodes_and_its_level_to_process.pop()
        if not sums_by_levels.__contains__(node_level):
            sums_by_levels[node_level] = 0
        sums_by_levels[node_level] += node_to_process.val
        if node_to_process.left is not None:
            nodes_and_its_level_to_process.append((node_to_process.left, node_level + 1))
        if node_to_process.right is not None:
            nodes_and_its_level_to_process.append((node_to_process.right, node_level + 1))
    min_sum: int = sys.maxsize
    for current_sum in sums_by_levels.values():
        min_sum = min(min_sum, current_sum)
    return min_sum


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))
# 7
