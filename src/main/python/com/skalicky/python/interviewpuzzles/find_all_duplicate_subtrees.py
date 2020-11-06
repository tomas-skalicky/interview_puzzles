# Task:
#
# Given a binary tree, find all duplicate subtrees (subtrees with the same value and same structure) and return them
# as a list of list [subtree1, subtree2, ...] where subtree1 is a duplicate of subtree2 etc.
#
# Here's an example and some starter code:
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#   def __repr__(self):
#     if self.left and self.right:
#       return f"({self.value}, {self.left}, {self.right})"
#     if self.left:
#       return f"({self.value}, {self.left})"
#     if self.right:
#       return f"({self.value}, None, {self.right})"
#     return f"({self.value})"
#
# def dup_trees(root):
#   # Fill this in.
#
# n3_1 = Node(3)
# n2_1 = Node(2, n3_1)
# n3_2 = Node(3)
# n2_2 = Node(2, n3_2)
# n1 = Node(1, n2_1, n2_2)
# # Looks like
# #     1
# #    / \
# #   2   2
# #  /   /
# # 3   3
#
# print(dup_trees(n1))
# # [[(3), (3)], [(2, (3)), (2, (3))]]
# # There are two duplicate trees
# #
# #     2
# #    /
# #   3
# # and just the leaf
# #
# # 3
from collections import deque
from typing import Optional, List, Dict, Tuple, Deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"


def get_node_value(node: Node) -> object:
    return str(node)


def have_same_child_subtrees(node1: Node, node2: Node, subtrees_by_nodes: Dict[Node, int]):
    if node1 is not None and node2 is not None:
        return subtrees_by_nodes[node1] == subtrees_by_nodes[node2]
    elif node1 is None and node2 is None:
        return True
    else:
        return False


def are_duplicate_subtrees(node1: Node, node2: Node, subtrees_by_nodes: Dict[Node, int]):
    return node1.value == node2.value and have_same_child_subtrees(node1.left, node2.left,
                                                                   subtrees_by_nodes) and have_same_child_subtrees(
        node1.right, node2.right, subtrees_by_nodes)


LEAF_LEVEL: int = 0


def persist_node_level_to_dictionaries(node: Node, level: int, node_lists_by_levels: Dict[int, List[Node]],
                                       levels_by_nodes: Dict[Node, int]):
    levels_by_nodes[node] = level
    if node_lists_by_levels.__contains__(level):
        node_lists_by_levels[level].append(node)
    else:
        node_lists_by_levels[level] = [node]


def calculate_node_levels(root_node: Node) -> Tuple[Dict[int, List[Node]], int]:
    node_lists_by_levels: Dict[int, List[Node]] = {}
    levels_by_nodes: Dict[Node, int] = {}

    nodes_to_process: Deque[Tuple[Node, bool]] = deque()
    nodes_to_process.append((root_node, False))
    while len(nodes_to_process) > 0:
        current_node, already_processed_once = nodes_to_process.pop()
        if current_node.left is None and current_node.right is None:
            persist_node_level_to_dictionaries(current_node, LEAF_LEVEL, node_lists_by_levels, levels_by_nodes)

        else:
            if already_processed_once:
                left_level: int = levels_by_nodes[current_node.left] if current_node.left is not None else LEAF_LEVEL
                right_level: int = levels_by_nodes[current_node.right] if current_node.right is not None else LEAF_LEVEL
                current_level: int = max(left_level, right_level) + 1
                persist_node_level_to_dictionaries(current_node, current_level, node_lists_by_levels, levels_by_nodes)

            else:
                nodes_to_process.append((current_node, True))
                if current_node.left is not None:
                    nodes_to_process.append((current_node.left, False))
                if current_node.right is not None:
                    nodes_to_process.append((current_node.right, False))
    return node_lists_by_levels, levels_by_nodes[root_node]


def give_all_nodes_subtree_id(root_node: Node) -> Dict[Node, int]:
    subtrees_by_nodes: Dict[Node, int] = {}

    next_subtree_id: int = 1
    nodes_to_process: Deque[Node] = deque()
    nodes_to_process.append(root_node)
    while len(nodes_to_process) > 0:
        current_node: Node = nodes_to_process.pop()
        subtrees_by_nodes[current_node] = next_subtree_id
        next_subtree_id += 1
        if current_node.left is not None:
            nodes_to_process.append(current_node.left)
        if current_node.right is not None:
            nodes_to_process.append(current_node.right)
    return subtrees_by_nodes


def find_all_duplicate_subtrees(root_node: Node) -> List[List[Node]]:
    node_lists_by_levels: Dict[int, List[Node]]
    level_of_root_node: int
    node_lists_by_levels, level_of_root_node = calculate_node_levels(root_node)
    subtrees_by_nodes: Dict[Node, int] = give_all_nodes_subtree_id(root_node)

    all_duplicates: List[List[Node]] = []
    for current_level in range(0, level_of_root_node + 1):
        nodes_with_current_level: List[Node] = node_lists_by_levels[current_level]
        # List is sorted descendingly because the removal operation from the end of List has a time complexity of O(1).
        # The removal operation from the beginning of List has a time complexity of O(n).
        nodes_sorted_by_value_descendingly: List[Node] = sorted(nodes_with_current_level, key=get_node_value,
                                                                reverse=True)

        current_duplicates: List[Node] = []
        while len(nodes_sorted_by_value_descendingly) > 0:
            current_node: Node = nodes_sorted_by_value_descendingly.pop()
            if len(current_duplicates) == 0:
                current_duplicates.append(current_node)
            else:
                previous_node: Node = current_duplicates[0]
                if are_duplicate_subtrees(current_node, previous_node, subtrees_by_nodes):
                    subtrees_by_nodes[current_node] = subtrees_by_nodes[previous_node]
                    current_duplicates.append(current_node)
                else:
                    if len(current_duplicates) > 1:
                        all_duplicates.append(current_duplicates)
                    current_duplicates = [current_node]

        if len(current_duplicates) > 1:
            all_duplicates.append(current_duplicates)
    return all_duplicates
