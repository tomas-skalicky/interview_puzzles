# Task:
#
# You are given a doubly linked list. Determine if it is a palindrome.
#
# Can you do this for a singly linked list?
#
# class Node(object):
#   def __init__(self, val):
#     self.val = val
#     self.next = None
#     self.prev = None
#
# def is_palindrome(node):
#   # Fill this in.
#
# node = Node('a')
# node.next = Node('b')
# node.next.prev = node
# node.next.next = Node('b')
# node.next.next.prev = node.next
# node.next.next.next = Node('a')
# node.next.next.next.prev = node.next.next
#
# print is_palindrome(node)
# # True
from collections import deque
from math import floor
from typing import Deque, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node] = None
        self.previous: Optional[Node] = None


def check_if_linked_list_is_palindrome_using_previous_node(input_node: Optional[Node]) -> bool:
    if input_node is None:
        return False
    else:
        current_node: Node = input_node
        count: int = 1
        while current_node.next is not None:
            current_node = current_node.next
            count += 1
        current_node_from_beginning: Node = input_node
        current_node_from_end: Node = current_node
        for i in range(0, floor(count / 2)):
            if current_node_from_beginning.value != current_node_from_end.value:
                return False
            else:
                current_node_from_beginning = current_node_from_beginning.next
                current_node_from_end = current_node_from_end.previous
        return True


def check_if_linked_list_is_palindrome_not_using_previous_node(input_node: Optional[Node]) -> bool:
    if input_node is None:
        return False
    else:
        current_node: Node = input_node
        count: int = 1
        stack: Deque[Node] = deque()
        stack.append(current_node)
        while current_node.next is not None:
            current_node = current_node.next
            count += 1
            stack.append(current_node)
        current_node_from_beginning: Node = input_node
        for i in range(0, floor(count / 2)):
            if current_node_from_beginning.value != stack.pop().value:
                return False
            else:
                current_node_from_beginning = current_node_from_beginning.next
        return True
