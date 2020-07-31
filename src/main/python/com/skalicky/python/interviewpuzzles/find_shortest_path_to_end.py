# Task:
#
# Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead.
# Given a list of numbers, find the minimum number of jumps to reach the end of the list.
#
# Example:
# Input: [3, 2, 5, 1, 1, 9, 3, 4]
# Output: 2
# Explanation:
#
# The minimum number of jumps to get to the end of the list is 2:
# 3 -> 5 -> 4
#
# Here's a starting point:
#
# def jumpToEnd(nums):
#   # Fill this in.
#
# print jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4])
# # 2
from typing import List


class Node:
    def __init__(self, value: int, list_item_count_to_end: int, step_count_to_end: int = None, previous_node=None):
        self.value: int = value
        self.list_item_count_to_end: int = list_item_count_to_end
        self.step_count_to_end: int = step_count_to_end
        self.previous_node: Node = previous_node

    def __str__(self) -> str:
        return '[value={}, list_item_count_to_end={}, step_count_to_end={}, previous_node={}]'.format(self.value,
                                                                                                      self.list_item_count_to_end,
                                                                                                      self.step_count_to_end,
                                                                                                      self.previous_node)


def jump_to_end(nums: List[int]) -> int:
    number_count: int = len(nums)
    if number_count < 2:
        return 0
    else:
        last_node: Node = Node(nums[number_count - 1], 0, 0)
        # We do not want to process the last item in the list, hence -1.
        for i in reversed(range(0, number_count - 1)):
            current_number: int = nums[i]
            current_list_item_count_to_end: int = number_count - 1 - i
            reachable_list_item_count_to_end: int = current_list_item_count_to_end - current_number
            node_to_process: Node = last_node
            # We do not check here the number of steps to the end item because other shorter intermediate steps
            # (if there were any) were already eliminated by previous while-loops.
            while node_to_process.previous_node is not None and node_to_process.previous_node.list_item_count_to_end >= reachable_list_item_count_to_end:
                node_to_process = node_to_process.previous_node
            last_node = Node(current_number, current_list_item_count_to_end, node_to_process.step_count_to_end + 1,
                             node_to_process)
        return last_node.step_count_to_end


print(jump_to_end([]))
# 0
print(jump_to_end([3]))
# 0
print(jump_to_end([1, 1, 1, 4]))
# 3
print(jump_to_end([3, 2, 5, 1, 1, 9, 3, 4]))
# 2
