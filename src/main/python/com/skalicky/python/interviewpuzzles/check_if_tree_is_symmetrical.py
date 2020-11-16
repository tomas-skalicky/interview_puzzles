# Task:
#
# A k-ary tree is a tree with k-children, and a tree is symmetrical if the data of the left side of the tree is the same
# as the right side of the tree.
#
# Here's an example of a symmetrical k-ary tree.
#         4
#      /     \
#     3        3
#   / | \    / | \
# 9   4  1  1  4  9
# Given a k-ary tree, figure out if the tree is symmetrical.
#
# Here is a starting point:
#
# class Node():
#   def __init__(self, value, children=[]):
#     self.value = value
#     self.children = children
#
# def is_symmetric(root):
#   # Fill this in.
#
# tree = Node(4)
# tree.children = [Node(3), Node(3)]
# tree.children[0].children = [Node(9), Node(4), Node(1)]
# tree.children[1].children = [Node(1), Node(4), Node(9)]
# print is_symmetric(tree)
# # True
from collections import deque
from math import floor
from typing import Deque, List, Optional, Tuple


class Node:
    def __init__(self, value: int, children: List = ()):
        self.value: int = value
        self.children: List[Node] = children


def is_symmetric(root: Optional[Node]) -> bool:
    if root is None:
        return True
    else:
        nodes_to_compare: Deque[Tuple[Node, Node]] = deque()
        root_children_count: int = len(root.children)
        if root_children_count % 2 == 1:
            return False
        else:
            for i in range(0, floor(root_children_count / 2)):
                nodes_to_compare.append((root.children[i], root.children[root_children_count - 1 - i]))
            while len(nodes_to_compare) > 0:
                node1_to_compare, node2_to_compare = nodes_to_compare.pop()
                node1_children_count: int = len(node1_to_compare.children)
                if node1_to_compare.value != node2_to_compare.value or node1_children_count != len(
                        node2_to_compare.children):
                    return False
                else:
                    for i in range(0, node1_children_count):
                        nodes_to_compare.append(
                            (node1_to_compare.children[i], node2_to_compare.children[node1_children_count - 1 - i]))
            return True


print(is_symmetric(None))
# True
tree = Node(4)
print(is_symmetric(tree))
# True
tree1 = Node(4)
tree1.children = [Node(3)]
print(is_symmetric(tree1))
# False
tree2 = Node(4)
tree2.children = [Node(3), Node(2)]
print(is_symmetric(tree2))
# False
tree3 = Node(4)
tree3.children = [Node(3), Node(3)]
tree3.children[0].children = [Node(9), Node(4), Node(1)]
tree3.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree3))
# True
tree4 = Node(4)
tree4.children = [Node(3), Node(4), Node(4), Node(3)]
tree4.children[0].children = [Node(9), Node(4), Node(1)]
tree4.children[1].children = [Node(2), Node(4)]
tree4.children[2].children = [Node(4), Node(2)]
tree4.children[3].children = [Node(1), Node(4), Node(9)]
tree4.children[1].children[0].children = [Node(33)]
tree4.children[2].children[1].children = [Node(33)]
print(is_symmetric(tree4))
# True
tree5 = Node(4)
tree5.children = [Node(3), Node(3)]
tree5.children[0].children = [Node(9), Node(4)]
tree5.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree5))
# False
