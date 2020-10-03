# Task:
#
# Given a postorder traversal for a binary search tree, reconstruct the tree. A postorder traversal is a traversal order
# where the left child always comes before the right child, and the right child always comes before the parent for all
# nodes.
#
# Here's some starter code:
#
# class Node():
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#   def __repr__(self):
#     return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"
#
#
# def create_tree(postorder):
#   # Fill this in.
#
# # 2 is the root node, with 1 as the left child and 3 as the right child
# print(create_tree([1, 3, 2]))
from collections import deque
from typing import List, Deque, Tuple, Optional


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __repr__(self) -> str:
        return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"


def create_tree(postorder: List[int]) -> Optional[Node]:
    node_count: int = len(postorder)
    if node_count == 0:
        return None
    else:
        root_node: Node = Node(postorder[node_count - 1])
        stacked_nodes_to_root_with_min_and_max_ranges: Deque[Tuple[Node, int, int]] = deque()
        stacked_nodes_to_root_with_min_and_max_ranges.append((root_node, None, None))

        for i in reversed(range(0, node_count - 1)):
            current_value: int = postorder[i]
            current_parent_node, min_range_included, max_range_included = stacked_nodes_to_root_with_min_and_max_ranges.pop()

            while len(stacked_nodes_to_root_with_min_and_max_ranges) > 0:
                if (min_range_included is None and current_value < current_parent_node.value) or (
                        min_range_included is not None and min_range_included <= current_value < current_parent_node.value) or (
                        max_range_included is None and current_parent_node.value < current_value) or (
                        max_range_included is not None and current_parent_node.value < current_value <= max_range_included):
                    break
                else:
                    current_parent_node, min_range_included, max_range_included = stacked_nodes_to_root_with_min_and_max_ranges.pop()

            new_node: Node = Node(current_value)

            if current_value < current_parent_node.value:
                current_parent_node.left = new_node
                new_node_min_range_included: int = min_range_included
                new_node_max_range_included: int = current_parent_node.value - 1
            else:
                current_parent_node.right = new_node
                new_node_min_range_included: int = current_parent_node.value + 1
                new_node_max_range_included: int = max_range_included

            stacked_nodes_to_root_with_min_and_max_ranges.append(
                (current_parent_node, min_range_included, max_range_included))
            stacked_nodes_to_root_with_min_and_max_ranges.append(
                (new_node, new_node_min_range_included, new_node_max_range_included))

        return root_node


#    2
#   / \
#  1   3
#
# 2 is the root node, with 1 as the left child and 3 as the right child
print(create_tree([1, 3, 2]))
# (2, (1, None, None), (3, None, None))

#     2
#    / \
#   1   6
#  /   / \
# 0   3   10
#     \
#      4
print(create_tree([0, 1, 4, 3, 10, 6, 2]))
# (2, (1, (0, None, None), None), (6, (3, None, (4, None, None)), (10, None, None)))
