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
from typing import Optional, Tuple


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

    # Function to print the list
    def print_list(self) -> None:
        node = self
        output = ''
        while node is not None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverse_iteratively(self) -> None:
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

    # Recursive Solution
    def reverse_recursively(self, previous_node=None) -> None:
        next_node: ListNode = self.next
        self.next = previous_node
        if next_node is not None:
            next_node.reverse_recursively(self)


def create_test_linked_list() -> Tuple[ListNode, ListNode]:
    test_head = ListNode(4)
    node1 = ListNode(3)
    test_head.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    test_tail = ListNode(0)
    node3.next = test_tail
    return test_head, test_tail


def main() -> None:
    test_head1, test_tail1 = create_test_linked_list()
    print("Initial list: ")
    test_head1.print_list()
    # 4 3 2 1 0
    test_head1.reverse_iteratively()
    print("List after reversal: ")
    test_tail1.print_list()
    # 0 1 2 3 4

    test_head2, test_tail2 = create_test_linked_list()
    print("Initial list: ")
    test_head2.print_list()
    # 4 3 2 1 0
    test_head2.reverse_recursively()
    print("List after reversal: ")
    test_tail2.print_list()
    # 0 1 2 3 4


main()
