# Task:
#
# Given a sorted list of numbers, change it into a balanced binary search tree. You can assume there will be
# no duplicate numbers in the list.
#
# Here's a starting point:
#
# from collections import deque
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#   def __str__(self):
#     # level-by-level pretty-printer
#     nodes = deque([self])
#     answer = ''
#     while len(nodes):
#       node = nodes.popleft()
#       if not node:
#         continue
#       answer += str(node.value)
#       nodes.append(node.left)
#       nodes.append(node.right)
#     return answer
#
#
# def createBalancedBST(nums):
#   # Fill this in.
#
# print createBalancedBST([1, 2, 3, 4, 5, 6, 7])
# # 4261357
# #   4
# #  / \
# # 2   6
# #/ \ / \
# #1 3 5 7


from collections import deque
from math import floor
from typing import List, Deque, Tuple, Optional


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __str__(self) -> str:
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


def create_balanced_binary_search_tree(nums: List[int]) -> Optional[Node]:
    if len(nums) == 0:
        return None
    else:
        tuples_to_process: Deque[Tuple] = deque()
        tuples_to_process.append((0, len(nums) - 1, None))
        root_node: Optional[Node] = None
        while len(tuples_to_process) > 0:
            tuple_to_process = tuples_to_process.popleft()
            from_index_included: int = tuple_to_process[0]
            to_index_included: int = tuple_to_process[1]
            parent_node: Node = tuple_to_process[2]
            new_node_index: int = floor((from_index_included + to_index_included) / 2)
            new_node_value = nums[new_node_index]
            new_node: Node = Node(new_node_value)
            if not parent_node:
                root_node = new_node
            elif new_node_value < parent_node.value:
                parent_node.left = new_node
            else:
                parent_node.right = new_node
            if from_index_included < new_node_index:
                tuples_to_process.append((from_index_included, new_node_index - 1, new_node))
            if to_index_included > new_node_index:
                tuples_to_process.append((new_node_index + 1, to_index_included, new_node))
        return root_node


print(create_balanced_binary_search_tree([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#    4
#   / \
#  2   6
# / \ / \
# 1 3 5 7
print(create_balanced_binary_search_tree([1, 2, 4, 6]))
# 2146
#   2
#  / \
# 1   4
#      \
#       6
print(create_balanced_binary_search_tree([]))
# None
# None
print(create_balanced_binary_search_tree([1]))
# 1
# 1
