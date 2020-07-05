# Task:
#
# You are given the preorder and inorder traversals of a binary tree in the form of arrays. Write a function that
# reconstructs the tree represented by these traversals.
#
# Example:
# Preorder: [a, b, d, e, c, f, g]
# Inorder: [d, b, e, a, f, c, g]
#
# The tree that should be constructed from these traversals is:
#
#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g
#
# Here's a start:
#
# from collections import deque
#
# class Node(object):
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#
#   def __str__(self):
#     q = deque()
#     q.append(self)
#     result = ''
#     while len(q):
#       n = q.popleft()
#       result += n.val
#       if n.left:
#         q.append(n.left)
#       if n.right:
#         q.append(n.right)
#
#     return result
#
#
# def reconstruct(preorder, inorder):
#   # Fill this in.
#
# tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
#                    ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
# print tree
# # abcdefg


from collections import deque
from typing import Deque, List, Dict, Tuple


class Node(object):
    def __init__(self, val: str):
        self.val: str = val
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        q: Deque[Node] = deque()
        q.append(self)
        result: str = ''
        while len(q):
            n: Node = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return result


def reconstruct(preorder: List[str], inorder: List[str]):
    node_count: int = len(preorder)
    if node_count == 0:
        return None
    else:
        # Auxiliary structure to reduce the time complexity from quadratic to linear.
        order_by_value: Dict[str, int] = dict()
        for i in range(0, node_count):
            order_by_value[inorder[i]] = i

        root_value: str = preorder[0]
        root_node_order: int = order_by_value[root_value]
        root: Node = Node(root_value)
        ancestors_with_order_and_ranges: Deque[Node, int, int, int] = deque()
        ancestors_with_order_and_ranges.append((root, root_node_order, None, None))

        for i in range(1, node_count):
            new_node_value: str = preorder[i]
            new_node_order: int = order_by_value[new_node_value]
            new_node: Node = Node(new_node_value)

            ancestor, ancestor_order, ancestor_min_range, ancestor_max_range = ancestors_with_order_and_ranges.pop()
            while not ((new_node_order < ancestor_order and (
                    ancestor_min_range is None or ancestor_min_range <= new_node_order)) or (
                               new_node_order > ancestor_order and (
                               ancestor_max_range is None or ancestor_max_range >= new_node_order))):
                ancestor, ancestor_order, ancestor_min_range, ancestor_max_range = ancestors_with_order_and_ranges.pop()

            ancestors_with_order_and_ranges.append((ancestor, ancestor_order, ancestor_min_range, ancestor_max_range))
            if new_node_order < ancestor_order:
                ancestor.left = new_node
                ancestors_with_order_and_ranges.append(
                    (new_node, new_node_order, ancestor_min_range, ancestor_order - 1))
            else:
                ancestor.right = new_node
                ancestors_with_order_and_ranges.append(
                    (new_node, new_node_order, ancestor_order + 1, ancestor_max_range))
    return root


#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g
print(reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g']))
# abcdefg

#     a
#    / \
#   b   c
#  /   / \
# d   f   g
#      \
#       z
print(reconstruct(['a', 'b', 'd', 'c', 'f', 'z', 'g'], ['d', 'b', 'a', 'f', 'z', 'c', 'g']))
# abcdfgz
