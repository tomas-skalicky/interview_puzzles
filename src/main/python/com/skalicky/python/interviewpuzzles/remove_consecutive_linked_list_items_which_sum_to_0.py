# Task:
#
# Given a linked list of integers, remove all consecutive nodes that sum up to 0.
#
# Example:
# Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
# Output: 10
#
# The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed. 4 -> -4 also sums up to 0
# too so that sequence should also be removed.
#
# Here's a starting point:
#
# class Node:
#   def __init__(self, value, next=None):
#     self.value = value
#     self.next = next
#
# def removeConsecutiveSumTo0(node):
#   # Fill this in.
#
# node = Node(10)
# node.next = Node(5)
# node.next.next = Node(-3)
# node.next.next.next = Node(-3)
# node.next.next.next.next = Node(1)
# node.next.next.next.next.next = Node(4)
# node.next.next.next.next.next.next = Node(-4)
# node = removeConsecutiveSumTo0(node)
# while node:
#   print node.value,
#   node = node.next
# # 10
from typing import Dict, Optional


class Node:
    def __init__(self, value, next_arg=None):
        self.value = value
        self.next: Optional[Node] = next_arg

    def __str__(self) -> str:
        return str(self.value)


def remove_consecutive_linked_list_items_which_sum_to_0(list_head_node: Node) -> Optional[Node]:
    all_possible_previous_sums_from_last_cut: Dict[int, Node] = {}
    previous_node: Optional[Node] = None
    first_node: Node = list_head_node
    current_node: Node = list_head_node
    while current_node:
        if current_node.value == 0 and len(all_possible_previous_sums_from_last_cut) == 0:
            first_node = current_node.next
        else:
            complement = 0 - current_node.value
            if complement in all_possible_previous_sums_from_last_cut:
                node_before_first_of_consecutive_nodes: Node = all_possible_previous_sums_from_last_cut[complement]
                if node_before_first_of_consecutive_nodes:
                    node_before_first_of_consecutive_nodes.next = current_node.next
                    previous_node = node_before_first_of_consecutive_nodes
                else:
                    first_node = current_node.next
                    previous_node = None
                all_possible_previous_sums_from_last_cut.clear()

            else:
                new_all_possible_previous_sums_from_last_cut: Dict[int, Node] = {}
                for current_sum in all_possible_previous_sums_from_last_cut.keys():
                    old_entry_previous_node: Node = all_possible_previous_sums_from_last_cut[current_sum]
                    new_sum: int = current_sum + current_node.value
                    new_all_possible_previous_sums_from_last_cut[new_sum] = old_entry_previous_node
                all_possible_previous_sums_from_last_cut = new_all_possible_previous_sums_from_last_cut
                all_possible_previous_sums_from_last_cut[current_node.value] = previous_node
                previous_node = current_node

        current_node = current_node.next
    return first_node
