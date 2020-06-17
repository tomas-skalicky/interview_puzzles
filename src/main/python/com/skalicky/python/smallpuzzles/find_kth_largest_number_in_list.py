# Task:
#
# Given a list, find the k-th largest element in the list.
# Input: list = [3, 5, 2, 4, 6, 8], k = 3
# Output: 5
# Here is a starting point:
#
# def findKthLargest(nums, k):
#   # Fill this in.
#
# print findKthLargest([3, 5, 2, 4, 6, 8], 3)
# # 5
from typing import List


def swap_items_in_list(i: int, j: int, nums: List[int]):
    temp: int = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def bubble_sort_iteration(start_index: int, nums: List[int]):
    j: int = start_index
    while j < len(nums):
        if nums[j - 1] > nums[j]:
            swap_items_in_list(j - 1, j, nums)
        j = j + 1


def find_kth_largest(nums: List[int], k: int):
    if len(nums) < k:
        return None
    else:
        nums2: List[int] = []
        # Time complexity of this for-loop and sort O(k log k)
        for i in range(0, k):
            nums2.append(nums[i])
        nums3: List[int] = sorted(nums2)
        # The time complexity of this for-loop is O(n * k)
        for i in range(k, len(nums)):
            if nums[i] > nums3[0]:
                nums3[0] = nums[i]
                bubble_sort_iteration(1, nums3)
        return nums3[0]


print(find_kth_largest([3, 5, 2, 4, 6, 8], 3))
# 5
print(find_kth_largest([3, 5, 2, 4, 6, 8], 7))
# None
