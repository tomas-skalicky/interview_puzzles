# Task:
#
# Given a linked list, swap the position of the 1st and 2nd node, then swap the position of the 3rd and 4th node etc.
#
# Here's some starter code:
#
# class Node:
#   def __init__(self, value, next=None):
#     self.value = value
#     self.next = next
#
#   def __repr__(self):
#     return f"{self.value}, ({self.next.__repr__()})"
#
# def swap_every_two(llist):
#   # Fill this in.
#
# llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
# print(swap_every_two(llist))
# # 2, (1, (4, (3, (5, (None)))))


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"


def swap_every_two(llist: Node) -> Node:
    root: Node = None
    previous_already_swapped: Node = None
    current: Node = llist
    while current is not None and current.next is not None:
        old_next: Node = current.next
        new_current: Node = old_next.next
        new_next: Node = current
        if previous_already_swapped is not None:
            previous_already_swapped.next = old_next
        else:
            root = old_next
        old_next.next = new_next
        previous_already_swapped = new_next
        new_next.next = None
        current = new_current

    if current is None:
        return root
    else:
        if root is None:
            return current
        else:
            previous_already_swapped.next = current
            return root


print(swap_every_two(Node(1, Node(2, Node(3, Node(4, Node(5)))))))
# 2, (1, (4, (3, (5, (None)))))
print(swap_every_two(None))
# None
print(swap_every_two(Node(1)))
# 1, (None)
print(swap_every_two(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))))
# 2, (1, (4, (3, (6, (5, (None))))))
