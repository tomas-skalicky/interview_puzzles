# Task:
#
# You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid binary
# search tree.
#
# Here's a starting point:
#
# class TreeNode:
#   def __init__(self, key):
#     self.left = None
#     self.right = None
#     self.key = key
#
#   def __str__(self):
#     # preorder traversal
#     answer = str(self.key)
#     if self.left:
#       answer += str(self.left)
#     if self.right:
#       answer += str(self.right)
#     return answer
#
# def largest_bst_subtree(root):
#   # Fill this in.
#
# #     5
# #    / \
# #   6   7
# #  /   / \
# # 2   4   9
# node = TreeNode(5)
# node.left = TreeNode(6)
# node.right = TreeNode(7)
# node.left.left = TreeNode(2)
# node.right.left = TreeNode(4)
# node.right.right = TreeNode(9)
# print largest_bst_subtree(node)
# #749
from collections import deque
from typing import Deque, Dict


class TreeNode:
    def __init__(self, key: int):
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.key: int = key

    def __str__(self):
        # preorder traversal
        answer: str = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


def largest_bst_subtree(root: TreeNode):
    current_root_with_max_subtree: TreeNode = None

    nodes_to_process: Deque[TreeNode] = deque()
    nodes_to_process.append(root)

    invalid_subtree_size: int = -1

    subtree_sizes_by_keys: Dict[int, int] = dict()
    subtree_mins_by_keys: Dict[int, int] = dict()
    subtree_maxs_by_keys: Dict[int, int] = dict()
    while len(nodes_to_process) > 0:
        current_node: TreeNode = nodes_to_process.pop()
        current_key: int = current_node.key

        left_node: TreeNode = current_node.left
        left_present: bool = left_node is not None
        left_key: int = left_node.key if left_present else None

        right_node: TreeNode = current_node.right
        right_present: bool = right_node is not None
        right_key: int = right_node.key if right_present else None

        left_not_processed_yet: bool = left_present and not subtree_sizes_by_keys.__contains__(left_key)
        right_not_processed_yet: bool = right_present and not subtree_sizes_by_keys.__contains__(right_key)
        if left_not_processed_yet or right_not_processed_yet:
            # The parent needs to be processed once again after its children will have a calculated size of their
            # subtrees.
            nodes_to_process.append(current_node)
            if left_not_processed_yet:
                nodes_to_process.append(left_node)
            if right_not_processed_yet:
                nodes_to_process.append(right_node)
        else:
            subtree_mins_by_keys[current_key] = subtree_mins_by_keys[left_key] if left_present else current_key
            subtree_maxs_by_keys[current_key] = subtree_maxs_by_keys[right_key] if right_present else current_key

            left_subtree_size: int = subtree_sizes_by_keys[left_key] if left_present else 0
            right_subtree_size: int = subtree_sizes_by_keys[right_key] if right_present else 0

            left_with_current_valid_subtree: bool = left_subtree_size != invalid_subtree_size and (
                    (left_present and subtree_maxs_by_keys[
                        left_key] < current_key) or not left_present)
            right_with_current_valid_subtree: bool = right_subtree_size != invalid_subtree_size and (
                    (right_present and subtree_mins_by_keys[
                        right_key] > current_key) or not right_present)
            current_valid_subtree: bool = left_with_current_valid_subtree and right_with_current_valid_subtree

            current_subtree_size: int = 1 + left_subtree_size + right_subtree_size if current_valid_subtree else invalid_subtree_size
            subtree_sizes_by_keys[current_key] = current_subtree_size
            if current_subtree_size != invalid_subtree_size and (
                    current_root_with_max_subtree is None or current_subtree_size > subtree_sizes_by_keys[
                current_root_with_max_subtree.key]):
                current_root_with_max_subtree = current_node

    return current_root_with_max_subtree


#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))
# 749

#     5
#    / \
#   8   7
#  /   / \
# 2   4   9
#  \     /
#   3   6
node2 = TreeNode(5)
node2.left = TreeNode(8)
node2.right = TreeNode(7)
node2.left.left = TreeNode(2)
node2.right.left = TreeNode(4)
node2.right.right = TreeNode(9)
node2.left.left.right = TreeNode(3)
node2.right.right.left = TreeNode(6)
print(largest_bst_subtree(node2))
# 823
