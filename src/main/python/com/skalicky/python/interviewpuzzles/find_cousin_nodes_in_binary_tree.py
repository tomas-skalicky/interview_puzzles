# Task:
#
# Given a binary tree and a given node value, return all of the node's cousins. Two nodes are considered cousins if
# they are on the same level of the tree with different parents. You can assume that all nodes will have their own
# unique value.
#
# Here's some starter code:
#
# class Node(object):
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
# class Solution(object):
#   def list_cousins(self, tree, val):
#     # Fill this in.
#
# #     1
# #    / \
# #   2   3
# #  / \   \
# # 4   6   5
# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(4)
# root.left.right = Node(6)
# root.right = Node(3)
# root.right.right = Node(5)
#
# print Solution().list_cousins(root, 5)
# # [4, 6]
from collections import deque
from typing import Deque, List, Optional, Tuple


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


class Solution:

    @staticmethod
    def find_parent_and_depth(tree_root: Node, node_value: int) -> Tuple[Node, int]:
        nodes_to_process: Deque[Tuple[Optional[Node], Node, int]] = deque()
        nodes_to_process.append((None, tree_root, 0))
        while len(nodes_to_process) > 0:
            current_parent_node, node_to_process, node_depth = nodes_to_process.pop()
            if node_to_process.value == node_value:
                return current_parent_node, node_depth
            else:
                if node_to_process.left is not None:
                    nodes_to_process.append((node_to_process, node_to_process.left, node_depth + 1))
                if node_to_process.right is not None:
                    nodes_to_process.append((node_to_process, node_to_process.right, node_depth + 1))
        raise RuntimeError('No node with the value {} found in the tree.'.format(node_value))

    @staticmethod
    def find_parents_and_nodes_with_depth(tree_root: Node, depth: int) -> List[Tuple[Node, Node]]:
        parents_and_nodes_with_depth: List[Tuple[Node, Node]] = []
        nodes_to_process: Deque[Tuple[Optional[Node], Node, int]] = deque()
        nodes_to_process.append((None, tree_root, 0))
        while len(nodes_to_process) > 0:
            current_parent_node, node_to_process, node_depth = nodes_to_process.popleft()
            if node_depth == depth:
                parents_and_nodes_with_depth.append((current_parent_node, node_to_process))
            else:
                if node_to_process.left is not None:
                    nodes_to_process.append((node_to_process, node_to_process.left, node_depth + 1))
                if node_to_process.right is not None:
                    nodes_to_process.append((node_to_process, node_to_process.right, node_depth + 1))
        return parents_and_nodes_with_depth

    @staticmethod
    def list_cousins(tree_root: Node, node_value: int) -> List[int]:
        parent, node_depth = Solution.find_parent_and_depth(tree_root, node_value)
        parents_and_nodes_with_depth: List[Tuple[Node, Node]] = Solution.find_parents_and_nodes_with_depth(tree_root,
                                                                                                           node_depth)
        cousin_values: List[int] = []
        for parent_and_node_with_depth in parents_and_nodes_with_depth:
            if parent is not None and parent.value != parent_and_node_with_depth[0].value:
                cousin_values.append(parent_and_node_with_depth[1].value)
        return cousin_values


#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(Solution.list_cousins(root, 5))
# [4, 6]
print(Solution.list_cousins(root, 4))
# [5]
print(Solution.list_cousins(root, 2))
# []
print(Solution.list_cousins(root, 1))
# []
