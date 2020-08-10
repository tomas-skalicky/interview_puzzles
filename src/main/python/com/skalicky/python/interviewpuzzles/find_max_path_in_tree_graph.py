# Task:
#
# You are given the root of a binary tree. Find the path between 2 nodes that maximizes the sum of all the nodes
# in the path, and return the sum. The path does not necessarily need to go through the root.
#
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#
# def maxPathSum(root):
#   # Fill this in.
#
# # (* denotes the max path)
# #       *10
# #       /  \
# #     *2   *10
# #     / \     \
# #   *20  1    -25
# #             /  \
# #            3    4
# root = Node(10)
# root.left = Node(2)
# root.right = Node(10)
# root.left.left = Node(20)
# root.left.right = Node(1)
# root.right.right = Node(-25)
# root.right.right.left = Node(3)
# root.right.right.right = Node(4)
# print maxPathSum(root)
# # 42
from collections import deque
from typing import Deque, List, Tuple, Set
from src.main.python.com.skalicky.python.interviewpuzzles.find_max_sum_of_contiguous_subarray import max_subarray_sum

print()
print('find_max_path_in_tree_graph.py:')


class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None
        self.id: int = None

    def __str__(self) -> str:
        return '[id={}, val={}]'.format(self.id, self.val)


# Complexities of this method:
# - time complexity O(n) where n is the number of nodes in the tree
# - space complexity O(n)
def initialize_parents_and_ids(root_node: Node) -> None:
    next_id: int = 1
    nodes_to_process: Deque[Node] = deque()
    nodes_to_process.append(root_node)
    while len(nodes_to_process) > 0:
        node_to_process: Node = nodes_to_process.pop()
        node_to_process.id = next_id
        next_id += 1
        if node_to_process.left is not None:
            node_to_process.left.parent = node_to_process
            nodes_to_process.append(node_to_process.left)
        if node_to_process.right is not None:
            node_to_process.right.parent = node_to_process
            nodes_to_process.append(node_to_process.right)


# Complexities of this method:
# - time complexity O(n) where n is the number of nodes in the tree
# - space complexity O(n)
def retrieve_leaves(root_node: Node) -> List[Node]:
    leaves: List[Node] = list()
    nodes_to_process: Deque[Node] = deque()
    nodes_to_process.append(root_node)
    while len(nodes_to_process) > 0:
        node_to_process = nodes_to_process.pop()
        if node_to_process.left is not None or node_to_process.right is not None:
            if node_to_process.left is not None:
                nodes_to_process.append(node_to_process.left)
            if node_to_process.right is not None:
                nodes_to_process.append(node_to_process.right)
        else:
            leaves.append(node_to_process)
    return leaves


# Complexities of this method:
# - time complexity O(n^2) where n is the number of nodes in the tree. One "n" is from copy of arrays.
# - space complexity O(n^2). One "n" is from copy of arrays.
def generate_all_possible_sequences(node_to_process: Node, previous_node_id: int, current_sequence: List[int],
                                    current_sequence_start_node: Node, all_sequences: List[List[int]],
                                    leaves_of_all_sequences: Set[Tuple[int, int]]) -> None:
    current_sequence.append(node_to_process.val)
    copy_of_current_sequence_necessary: bool = False
    if node_to_process.parent is not None and node_to_process.parent.id != previous_node_id:
        generate_all_possible_sequences(node_to_process.parent, node_to_process.id, current_sequence.copy(),
                                        current_sequence_start_node, all_sequences, leaves_of_all_sequences)
        copy_of_current_sequence_necessary = True

    if node_to_process.left is not None and node_to_process.left.id != previous_node_id:
        generate_all_possible_sequences(node_to_process.left, node_to_process.id, current_sequence.copy(),
                                        current_sequence_start_node, all_sequences, leaves_of_all_sequences)
        copy_of_current_sequence_necessary = True

    if node_to_process.right is not None and node_to_process.right.id != previous_node_id:
        sequence: List[int] = current_sequence.copy() if copy_of_current_sequence_necessary else current_sequence
        generate_all_possible_sequences(node_to_process.right, node_to_process.id, sequence,
                                        current_sequence_start_node, all_sequences, leaves_of_all_sequences)
        copy_of_current_sequence_necessary = True

    if not copy_of_current_sequence_necessary:
        start_node_id: int = current_sequence_start_node.id
        end_node_id: int = node_to_process.id
        if not leaves_of_all_sequences.__contains__(
                (start_node_id, end_node_id)) and not leaves_of_all_sequences.__contains__(
            (end_node_id, start_node_id)):
            all_sequences.append(current_sequence)
            leaves_of_all_sequences.add((start_node_id, end_node_id))


# Complexities of this method:
# - time complexity O(n^3) where n is the number of nodes in the tree. Reason: the number of leaves can be
# asymptotically approximated to n.
# - space complexity O(n^3)
def max_path_sum(root_node: Node) -> int:
    if root_node is None:
        return 0
    else:
        initialize_parents_and_ids(root_node)
        leaves: List[Node] = retrieve_leaves(root_node)
        all_sequences: List[List[int]] = list()
        leaves_of_all_sequences: Set[Tuple[int, int]] = set()
        for leaf in leaves:
            generate_all_possible_sequences(leaf, None, list(), leaf, all_sequences, leaves_of_all_sequences)
        current_max_sum: int = None
        for sequence in all_sequences:
            current_sum: int = max_subarray_sum(sequence)
            current_max_sum = max(current_max_sum, current_sum) if current_max_sum is not None else current_sum
        return current_max_sum


# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(max_path_sum(root))
# 42

# (* denotes the max path)
#        1
#       / \
#     *2   1
#     / \
#   *20 *3
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(1)
root2.left.left = Node(20)
root2.left.right = Node(3)
print(max_path_sum(root2))
# 25

# (* denotes the max path)
#       *2
#       /
#     *-1
#     /
#   *2
root3 = Node(2)
root3.left = Node(-1)
root3.left.left = Node(2)
print(max_path_sum(root3))
# 3

# (* denotes the max path)
#       *2
root4 = Node(2)
print(max_path_sum(root4))
# 2

# (* denotes the max path)
#       *-2
root5 = Node(-2)
print(max_path_sum(root5))
# -2

print(max_path_sum(None))
# 0
