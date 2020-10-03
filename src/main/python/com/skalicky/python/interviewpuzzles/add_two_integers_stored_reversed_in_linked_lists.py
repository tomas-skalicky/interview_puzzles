# Task:
#
# "You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and
# each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
# Here is the function signature as a starting point (in Python):
#
# # Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None
#
# class Solution:
#   def addTwoNumbers(self, l1, l2, c = 0):
#     # Fill this in.
#
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
#
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
#
# result = Solution().addTwoNumbers(l1, l2)
# while result:
#   print result.val,
#   result = result.next
# # 7 0 8


# Definition for singly-linked list.
from typing import Optional, Tuple


class ListNode(object):
    def __init__(self, x: int):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    @staticmethod
    def add_node_values_to_new_node(node1_value: int,
                                    node2_value: int,
                                    addition_left: int,
                                    result_list_current_node: ListNode) -> Tuple[ListNode, int]:
        sum_result: int = node1_value + node2_value + addition_left
        new_node_value: int = sum_result % 10
        result_list_current_node.next = ListNode(new_node_value)
        new_result_list_current_node: ListNode = result_list_current_node.next
        new_addition_left: int = round((sum_result - new_node_value) / 10)
        return new_result_list_current_node, new_addition_left

    @staticmethod
    def add_two_numbers(l1: ListNode,
                        l2: ListNode,
                        c=0) -> Optional[ListNode]:
        result_list_dummy_first_node = ListNode(-1)
        result_list_current_node: ListNode = result_list_dummy_first_node
        list1_current_node: ListNode = l1
        list2_current_node: ListNode = l2
        addition_left: int = 0
        while list1_current_node is not None or list2_current_node is not None:
            if list1_current_node is None:
                if list2_current_node is None:
                    break
                elif addition_left == 0:
                    result_list_current_node.next = list2_current_node
                    break
                else:
                    result_list_current_node, addition_left = Solution.add_node_values_to_new_node(
                        0, list2_current_node.val, addition_left, result_list_current_node)
                    list2_current_node = list2_current_node.next
            elif list2_current_node is None:
                if addition_left == 0:
                    result_list_current_node.next = list1_current_node
                    break
                else:
                    result_list_current_node, addition_left = Solution.add_node_values_to_new_node(
                        list1_current_node.val, 0, addition_left, result_list_current_node)
                    list1_current_node = list1_current_node.next
            else:
                result_list_current_node, addition_left = Solution.add_node_values_to_new_node(
                    list1_current_node.val, list2_current_node.val, addition_left, result_list_current_node)
                list1_current_node = list1_current_node.next
                list2_current_node = list2_current_node.next
        return result_list_dummy_first_node.next


def main() -> None:
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(7)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l2.next.next.next = ListNode(4)
    l2.next.next.next.next = ListNode(2)

    result: Optional[ListNode] = Solution.add_two_numbers(l1, l2)
    while result:
        print(result.val, end=' ')
        result = result.next
        # 7 0 2 5 2


main()
