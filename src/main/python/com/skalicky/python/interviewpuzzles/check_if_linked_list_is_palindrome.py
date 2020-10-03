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


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def is_palindrome_using_previous_node(input_node: Optional[Node]) -> bool:
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
            if current_node_from_beginning.val != current_node_from_end.val:
                return False
            else:
                current_node_from_beginning = current_node_from_beginning.next
                current_node_from_end = current_node_from_end.prev
        return True


def is_palindrome_without_previous_node(input_node: Optional[Node]) -> bool:
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
            if current_node_from_beginning.val != stack.pop().val:
                return False
            else:
                current_node_from_beginning = current_node_from_beginning.next
        return True


def is_palindrome(input_node: Optional[Node]) -> None:
    print(is_palindrome_using_previous_node(input_node))
    print(is_palindrome_without_previous_node(input_node))


node: Node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next
is_palindrome(node)
# True
# True

node2: Node = Node('a')
node2.next = Node('b')
node2.next.prev = node2
node2.next.next = Node('c')
node2.next.next.prev = node2.next
node2.next.next.next = Node('b')
node2.next.next.next.prev = node2.next.next
node2.next.next.next.next = Node('a')
node2.next.next.next.next.prev = node2.next.next.next
is_palindrome(node2)
# True
# True

node3: Node = Node('a')
node3.next = Node('c')
node3.next.prev = node3
node3.next.next = Node('b')
node3.next.next.prev = node3.next
node3.next.next.next = Node('a')
node3.next.next.next.prev = node3.next.next
is_palindrome(node3)
# False
# False

is_palindrome(Node('a'))
# True
# True

is_palindrome(None)
# False
# False
