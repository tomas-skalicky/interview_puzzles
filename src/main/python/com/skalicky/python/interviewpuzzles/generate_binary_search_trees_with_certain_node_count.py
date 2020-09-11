# Task:
#
# Given a number n, generate all binary search trees that can be constructed with nodes 1 to n.
#
# Here's some code to start with:
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#   def __str__(self):
#     result = str(self.value)
#     if self.left:
#       result = result + str(self.left)
#     if self.right:
#       result = result + str(self.right)
#     return result
#
# def generate_bst(n):
#   # Fill this in.
#
# for tree in generate_bst(3):
#   print tree
#
# # Pre-order traversals of binary trees from 1 to n.
# # 123
# # 132
# # 213
# # 312
# # 321
#
# #   1      1      2      3      3
# #    \      \    / \    /      /
# #     2      3  1   3  1      2
# #      \    /           \    /
# #       3  2             2  1
from collections import deque
from typing import List, Deque, Tuple, Set


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value: int = value
        self.left: Node = left
        self.right: Node = right

    def __str__(self) -> str:
        result = str(self.value)
        if self.left:
            result = result + str(self.left)
        if self.right:
            result = result + str(self.right)
        return result


class NodeForBuilding(Node):
    def __init__(self, value: int, left=None, right=None, parent=None, min_allowed_value_in_subtree=None,
                 max_allowed_value_in_subtree=None):
        super().__init__(value, left, right)
        self.parent: None = parent
        self.min_allowed_value_in_subtree: int = min_allowed_value_in_subtree
        self.max_allowed_value_in_subtree: int = max_allowed_value_in_subtree


def build_tree(tree_in_preorder: List[int]) -> Node:
    root: Node = None
    nodes_with_min_and_max_ranges_included: Deque[Tuple[Node, int, int]] = deque()
    for current_node_value in tree_in_preorder:
        new_node: Node = Node(current_node_value)
        if root is None:
            root = new_node
            nodes_with_min_and_max_ranges_included.append((root, None, None))
        else:
            parent_node, min_included, max_included = nodes_with_min_and_max_ranges_included.pop()
            while (min_included is not None and current_node_value < min_included) or (
                    max_included is not None and current_node_value > max_included):
                parent_node, min_included, max_included = nodes_with_min_and_max_ranges_included.pop()
            if (min_included is None or current_node_value >= min_included) and current_node_value < parent_node.value:
                parent_node.left = new_node
                nodes_with_min_and_max_ranges_included.append((parent_node, min_included, max_included))
                nodes_with_min_and_max_ranges_included.append((new_node, min_included, parent_node.value - 1))
            if (max_included is None or current_node_value <= max_included) and current_node_value > parent_node.value:
                parent_node.right = new_node
                nodes_with_min_and_max_ranges_included.append((parent_node, min_included, max_included))
                nodes_with_min_and_max_ranges_included.append((new_node, parent_node.value + 1, max_included))
    return root


def call_recursively_permutate_numbers_and_validate_trees(node_to_add: NodeForBuilding,
                                                          rest_numbers: Set[int],
                                                          tree_in_construction_in_preorder: List[int],
                                                          trees_in_preorder: List[List[int]]) -> None:
    copy_rest_numbers: Set[int] = rest_numbers.copy()
    copy_rest_numbers.remove(node_to_add.value)
    copy_tree_in_construction_in_preorder: List[int] = tree_in_construction_in_preorder.copy()
    copy_tree_in_construction_in_preorder.append(node_to_add.value)
    permutate_numbers_and_validate_trees(copy_rest_numbers, copy_tree_in_construction_in_preorder,
                                         node_to_add, trees_in_preorder)


def permutate_numbers_and_validate_trees(rest_numbers: Set[int], tree_in_construction_in_preorder: List[int],
                                         last_added_node_to_constructed_tree: NodeForBuilding,
                                         trees_in_preorder: List[List[int]]) -> None:
    if len(rest_numbers) == 0:
        trees_in_preorder.append(tree_in_construction_in_preorder)
    else:
        # Ensures a better efficiency of the algorithm by pruning the remaining domain.
        for n in rest_numbers:
            if len(tree_in_construction_in_preorder) == 0:
                call_recursively_permutate_numbers_and_validate_trees(NodeForBuilding(n), rest_numbers,
                                                                      tree_in_construction_in_preorder,
                                                                      trees_in_preorder)

            else:
                parent_node: NodeForBuilding = last_added_node_to_constructed_tree
                min_included: int = parent_node.min_allowed_value_in_subtree
                if min_included is not None and n < min_included:
                    # The current value "n" does not fit to the preorder tree.
                    continue

                else:
                    max_included: int = parent_node.max_allowed_value_in_subtree
                    while max_included is not None and n > max_included:
                        parent_node = parent_node.parent
                        min_included: int = parent_node.min_allowed_value_in_subtree
                        max_included: int = parent_node.max_allowed_value_in_subtree

                    if (min_included is None or n >= min_included) and n < parent_node.value:
                        new_node: NodeForBuilding = NodeForBuilding(n, parent=parent_node,
                                                                    min_allowed_value_in_subtree=min_included,
                                                                    max_allowed_value_in_subtree=parent_node.value - 1)
                        parent_node.left = new_node
                        call_recursively_permutate_numbers_and_validate_trees(new_node, rest_numbers,
                                                                              tree_in_construction_in_preorder,
                                                                              trees_in_preorder)
                    if (max_included is None or n <= max_included) and n > parent_node.value:
                        new_node: NodeForBuilding = NodeForBuilding(n, parent=parent_node,
                                                                    min_allowed_value_in_subtree=parent_node.value + 1,
                                                                    max_allowed_value_in_subtree=max_included)
                        parent_node.right = new_node
                        call_recursively_permutate_numbers_and_validate_trees(new_node, rest_numbers,
                                                                              tree_in_construction_in_preorder,
                                                                              trees_in_preorder)
        return


def generate_bst(n: int) -> List[Node]:
    if n == 1:
        return [Node(n)]
    else:
        trees_in_preorder: List[List[int]] = list()
        permutate_numbers_and_validate_trees(set(range(1, n + 1)), [], None, trees_in_preorder)

        result_trees: List[Node] = list()
        for tree_in_preorder in trees_in_preorder:
            result_trees.append(build_tree(tree_in_preorder))
        return result_trees


for tree in generate_bst(3):
    print(tree)

# Pre-order traversals of binary trees from 1 to n.
# 123
# 132
# 213
# 312
# 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1
