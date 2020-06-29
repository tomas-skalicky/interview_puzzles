# Task:
#
# Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than
# or equal to) of k. If either does not exist, then print them as None.
#
# Here is the definition of a node for the tree.
#
# class Node:
#   def __init__(self, value):
#     self.left = None
#     self.right = None
#     self.value = value
#
# def findCeilingFloor(root_node, k, floor=None, ceil=None):
#   # Fill this in.
#
# root = Node(8)
# root.left = Node(4)
# root.right = Node(12)
#
# root.left.left = Node(2)
# root.left.right = Node(6)
#
# root.right.left = Node(10)
# root.right.right = Node(14)
#
# print findCeilingFloor(root, 5)
# # (4, 6)


class Node:
    def __init__(self, value: int):
        self.left = None
        self.right = None
        self.value: int = value


def find_ceiling_floor(root_node: Node, k: int, floor: int = None, ceil: int = None):
    current_floor: int = None
    current_ceiling: int = None
    current_node: Node = root_node
    while current_node is not None:
        if current_node.value == k:
            return k, k
        elif current_node.value < k:
            if current_floor is None or current_node.value > current_floor:
                current_floor = current_node.value
            current_node = current_node.right
        else:
            if current_ceiling is None or current_node.value < current_ceiling:
                current_ceiling = current_node.value
            current_node = current_node.left
    return current_floor, current_ceiling


root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(find_ceiling_floor(root, -1))
# (None, 2)

print(find_ceiling_floor(root, 5))
# (4, 6)

print(find_ceiling_floor(root, 14))
# (14, 14)

print(find_ceiling_floor(root, 15))
# (14, None)
