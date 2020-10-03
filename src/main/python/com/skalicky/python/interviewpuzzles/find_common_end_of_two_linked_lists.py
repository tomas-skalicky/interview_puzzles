# Task:
#
# You are given two singly linked lists. The lists intersect at some node. Find, and return the node. Note: the lists
# are non-cyclical.
#
# Example:
#
# A = 1 -> 2 -> 3 -> 4
# B = 6 -> 3 -> 4
#
# This should return 3 (you may assume that any nodes with the same value are the same node).
#
# Here is a starting point:
#
# def intersection(a, b):
#   # fill this in.
#
# class Node(object):
#   def __init__(self, val):
#     self.val = val
#     self.next = None
#   def prettyPrint(self):
#     c = self
#     while c:
#       print c.val,
#       c = c.next
#
# a = Node(1)
# a.next = Node(2)
# a.next.next = Node(3)
# a.next.next.next = Node(4)
#
# b = Node(6)
# b.next = a.next.next
#
# c = intersection(a, b)
# c.prettyPrint()
# # 3 4
from typing import Optional


class Node(object):
    def __init__(self, val: int):
        self.val = val
        self.next: Optional[Node] = None
        self.previous: Optional[Node] = None

    def pretty_print_self_and_nexts(self) -> None:
        current: Node = self
        while current:
            print(current.val)
            current = current.next

    def invert_by_creating_new_list(self):
        current = self
        current_of_new_list = Node(current.val)
        current_of_new_list.previous = None
        while current.next:
            current = current.next
            previous_of_new_list = current_of_new_list
            current_of_new_list = Node(current.val)
            previous_of_new_list.next = current_of_new_list
            current_of_new_list.previous = previous_of_new_list
        return current_of_new_list

    def invert_by_setting_previous(self):
        current: Node = self
        current.previous = None
        while current.next:
            previous = current
            current = current.next
            current.previous = previous
        return current

    def __eq__(self, other) -> bool:
        return self.val == other.val

    def __str__(self) -> str:
        return str(self.val)


def intersection_intern(first: Node, second: Node) -> Optional[Node]:
    current_first: Node = first
    current_second: Node = second
    if current_first == current_second:
        while current_first.previous and current_second.previous and current_first.previous == current_second.previous:
            current_first = current_first.previous
            current_second = current_second.previous
        return current_first
    else:
        return None


def intersection_when_shared_objects_in_list(first: Node, second: Node) -> Optional[Node]:
    return intersection_intern(first.invert_by_creating_new_list(), second.invert_by_creating_new_list())


def intersection_when_no_shared_objects_in_list(first: Node, second: Node) -> Optional[Node]:
    return intersection_intern(first.invert_by_setting_previous(), second.invert_by_setting_previous())


# 1 -> 2 -> 3 -> 4
a: Node = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

# 6 -> 3 -> 4
b: Node = Node(6)
b.next = a.next.next

c: Node = intersection_when_shared_objects_in_list(a, b)
c.pretty_print_self_and_nexts()
# 3 4


# 1 -> 2 -> 3 -> 4
a: Node = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

# 6 -> 3 -> 4
b: Node = Node(6)
b.next = Node(3)
b.next.next = Node(4)

c: Node = intersection_when_no_shared_objects_in_list(a, b)
c.pretty_print_self_and_nexts()
# 3 4
