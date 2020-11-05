# Task:
#
# You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and
# return it.
#
# Here's your starting point:
#
# class Node(object):
#   def __init__(self, val, next=None):
#     self.val = val
#     self.next = next
#
#   def __str__(self):
#     c = self
#     answer = ""
#     while c:
#       answer += str(c.val) if c.val else ""
#       c = c.next
#     return answer
#
# def merge(lists):
#   # Fill this in.
#
# a = Node(1, Node(3, Node(5)))
# b = Node(2, Node(4, Node(6)))
# print merge([a, b])
# # 123456
from typing import List, Optional


class Node:
    def __init__(self, val: int, next_node=None):
        self.val: int = val
        self.next_node: Node = next_node

    def __str__(self):
        current: Node = self
        answer = ""
        while current:
            answer += str(current.val) if current.val else ""
            current = current.next_node
        return answer


def set_next_node_and_determine_beginning(beginning: Node, current: Node, next_node: Node):
    if current:
        current.next_node = next_node
        return beginning, next_node
    else:
        return next_node, next_node


def merge_two_lists(first: Node, second: Node):
    first_current: Node = first
    second_current: Node = second
    result_beginning: Optional[Node] = None
    result_current: Optional[Node] = None
    while first_current and second_current:
        if first_current.val <= second_current.val:
            result_beginning, result_current = set_next_node_and_determine_beginning(result_beginning,
                                                                                     result_current,
                                                                                     first_current)
            first_current = first_current.next_node
        else:
            result_beginning, result_current = set_next_node_and_determine_beginning(result_beginning,
                                                                                     result_current,
                                                                                     second_current)
            second_current = second_current.next_node

    if not first_current and second_current:
        result_beginning, result_current = set_next_node_and_determine_beginning(result_beginning,
                                                                                 result_current,
                                                                                 second_current)
    if not second_current and first_current:
        result_beginning, result_current = set_next_node_and_determine_beginning(result_beginning,
                                                                                 result_current,
                                                                                 first_current)
    return result_beginning


def merge(lists: List[Node]):
    if len(lists) == 0:
        return ''
    else:
        current_lists: List[Node] = lists
        while len(current_lists) > 1:
            last: Node = current_lists.pop()
            one_before_last: Node = current_lists.pop()
            current_lists.append(merge_two_lists(last, one_before_last))
        return current_lists[0]


list1 = Node(1, Node(3, Node(5)))
list2 = Node(3, Node(4, Node(6, Node(7))))
list3 = Node(2, Node(8))
list4 = Node(9)
print(merge([list1, list2, list3, list4]))
# 123456
print(merge([]))
#
list5 = Node(1, Node(3, Node(5)))
print(merge([list5]))
# 135
list6 = Node(1, Node(3, Node(5)))
list7 = None
print(merge([list6, list7]))
# 135
