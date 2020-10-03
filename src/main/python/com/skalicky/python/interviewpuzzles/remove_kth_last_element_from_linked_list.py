# Task:
#
# You are given a singly linked list and an integer k. Return the linked list, removing the k-th last element from
# the list.
#
# Try to do it in a single pass and using constant space.
#
# Here's a starting point:
#
# class Node:
#   def __init__(self, val, next=None):
#     self.val = val
#     self.next = next
#   def __str__(self):
#     current_node = self
#     result = []
#     while current_node:
#       result.append(current_node.val)
#       current_node = current_node.next
#     return str(result)
#
# def remove_kth_from_linked_list(head, k):
#   # Fill this in
#
# head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
# print(head)
# # [1, 2, 3, 4, 5]
# head = remove_kth_from_linked_list(head, 3)
# print(head)
# # [1, 2, 4, 5]
from typing import List, Optional


class Node:
    def __init__(self, val: int, next_node=None):
        self.val: int = val
        self.next: Optional[Node] = next_node

    def __str__(self) -> str:
        current_node = self
        result: List[int] = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


def remove_kth_from_linked_list(head_arg: Optional[Node], k: int) -> Optional[Node]:
    if head_arg is None:
        return None
    else:
        before_kth_last: Optional[Node] = None
        kth_last: Optional[Node] = None
        current: Node = head_arg
        index_of_kth_last: Optional[int] = None
        index_of_current: int = 0
        while current:
            if index_of_current + 1 == k:
                kth_last = head_arg
                index_of_kth_last = 0
            elif kth_last:
                before_kth_last = kth_last
                kth_last = kth_last.next
                index_of_kth_last = index_of_kth_last + 1
            current = current.next
            index_of_current = index_of_current + 1
        if index_of_current == k:
            return kth_last.next
        elif index_of_current < k:
            return head_arg
        else:
            before_kth_last.next = kth_last.next
            return head_arg


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
print(remove_kth_from_linked_list(head, 3))
# [1, 2, 4, 5]

head2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head2)
# [1, 2, 3, 4, 5]
print(remove_kth_from_linked_list(head2, 6))
# [1, 2, 3, 4, 5]

head3 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head3)
# [1, 2, 3, 4, 5]
print(remove_kth_from_linked_list(head3, 5))
# [2, 3, 4, 5]

head4 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head4)
# [1, 2, 3, 4, 5]
print(remove_kth_from_linked_list(head4, 1))
# [1, 2, 3, 4]

head5: Optional[Node] = None
print(head5)
# None
print(remove_kth_from_linked_list(head5, 1))
# None
