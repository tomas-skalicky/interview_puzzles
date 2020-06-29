# Task:
#
# You have a landscape, in which puddles can form. You are given an array of non-negative integers representing
# the elevation at each location. Return the amount of water that would accumulate if it rains.
#
# For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
#        X
#    X███XX█X
#  X█XX█XXXXXX
# # [0,1,0,2,1,0,1,3,2,1,2,1]
# Here's your starting pont:
#
# def capacity(arr):
#   # Fill this in.
#
# print capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# # 6
from collections import deque
from typing import List, Deque, Tuple


def identify_bottom_of_puddle(current_index: int,
                              landscape: List[int],
                              bottom_of_puddles_to_process: Deque[Tuple]):
    i: int = current_index
    current_value = landscape[current_index]
    while i > 0 and landscape[i] == current_value:
        i = i - 1
    if i >= 0 and landscape[i] > current_value:
        start_index: int = i + 1
        i = current_index
        while i < len(landscape) - 1 and landscape[i] == current_value:
            i = i + 1
        if i < len(landscape) and landscape[i] > current_value:
            bottom_of_puddles_to_process.append((start_index, i - 1))
            i = i + 1
        return i
    else:
        return current_index + 1


# Time complexity O(n ^ 2)
def capacity(arr: List[int]):
    if len(arr) < 3:
        return 0
    else:
        result_count: int = 0
        bottom_of_puddles_to_process: Deque[Tuple] = deque()
        i: int = 1
        while i < len(arr) - 1:
            i = identify_bottom_of_puddle(i, arr, bottom_of_puddles_to_process)
        while len(bottom_of_puddles_to_process) > 0:
            start_index, end_index = bottom_of_puddles_to_process.popleft()
            min_depth: int = min(arr[start_index - 1], arr[end_index + 1])
            current_value: int = arr[start_index]
            diff_depth: int = min_depth - current_value
            for j in range(start_index, end_index + 1):
                result_count = result_count + diff_depth
                arr[j] = min_depth
            identify_bottom_of_puddle(start_index - 1, arr, bottom_of_puddles_to_process)
        return result_count


print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
print(capacity([2, 0, 0, 0, 3]))
# 6
print(capacity([2, 2, 2]))
# 0
print(capacity([0, 1, 4]))
# 0
print(capacity([4, 1, 0]))
# 0
print(capacity([0, 2]))
# 0
print(capacity([0]))
# 0
print(capacity([]))
# 0
