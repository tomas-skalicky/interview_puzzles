# Task:
#
# Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?
#
# Example:
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
#
# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None
#
#   # Function to print the list
#   def printList(self):
#     node = self
#     output = ''
#     while node != None:
#       output += str(node.val)
#       output += " "
#       node = node.next
#     print(output)
#
#   # Iterative Solution
#   def reverseIteratively(self, head):
#     # Implement this.
#
#   # Recursive Solution
#   def reverseRecursively(self, head):
#     # Implement this.
#
# # Test Program
# # Initialize the test list:
# testHead = ListNode(4)
# node1 = ListNode(3)
# testHead.next = node1
# node2 = ListNode(2)
# node1.next = node2
# node3 = ListNode(1)
# node2.next = node3
# testTail = ListNode(0)
# node3.next = testTail
#
# print("Initial list: ")
# testHead.printList()
# # 4 3 2 1 0
# testHead.reverseIteratively(testHead)
# #testHead.reverseRecursively(testHead)
# print("List after reversal: ")
# testTail.printList()
# # 0 1 2 3 4
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

    def serialize_to_string(self) -> str:
        node = self
        output = ''
        while node is not None:
            output += '{} '.format(node.val)
            node = node.next
        return output

    def reverse_linked_list_iteratively(self) -> None:
        previous_node: Optional[ListNode] = None
        current_node: ListNode = self
        next_node: ListNode = current_node.next
        while current_node is not None:
            current_node.next = previous_node
            previous_node: ListNode = current_node
            current_node: ListNode = next_node
            if current_node is not None:
                next_node: ListNode = current_node.next
            else:
                next_node: Optional[ListNode] = None

    def reverse_linked_list_recursively(self, previous_node=None) -> None:
        next_node: ListNode = self.next
        self.next = previous_node
        if next_node is not None:
            next_node.reverse_linked_list_recursively(self)
