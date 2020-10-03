# Task:
#
# Given a linked list and a number k, rotate the linked list by k places.
#
# Here's some starter code and an example:
#
# class Node:
#   def __init__(self, value, next=None):
#     self.value = value
#     self.next = next
#
#   def __str__(self):
#     current = self
#     ret = ''
#     while current:
#       ret += str(current.value)
#       current = current.next
#     return ret
#
# def rotate_list(list, k):
#   # Fill this in.
#
# # Order is 1, 2, 3, 4
# llist = Node(1, Node(2, Node(3, Node(4))))
#
# # Order should now be 3, 4, 1, 2
# print(rotate_list(llist, 2))
# # 3412
from typing import Optional


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next: Optional[Node] = next_node

    def __str__(self):
        current = self
        ret = ''
        while current:
            ret += str(current.value)
            current = current.next
        return ret


def rotate_list(linked_list_head: Node, k: int):
    node_count: int = 1
    last_node: Node = linked_list_head
    while last_node.next is not None:
        last_node = last_node.next
        node_count += 1

    modulod_k: int = k % node_count
    previous_node: Optional[Node] = None
    current_node: Node = linked_list_head
    for i in range(0, modulod_k):
        previous_node = current_node
        current_node = current_node.next

    previous_node.next = None
    last_node.next = linked_list_head
    return current_node


# Order is 1, 2, 3, 4
# Order should now be 3, 4, 1, 2
print(rotate_list(Node(1, Node(2, Node(3, Node(4)))), 2))
# 3412

# Order is 1, 2, 3, 4
# Order should now be 2, 3, 4, 1
print(rotate_list(Node(1, Node(2, Node(3, Node(4)))), 9))
# 2341
