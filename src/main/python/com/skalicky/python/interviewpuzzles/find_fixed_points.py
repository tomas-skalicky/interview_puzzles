# Task:
#
# A fixed point in a list is where the value is equal to its index. So for example the list [-5, 1, 3, 4], 1 is a fixed
# point in the list since the index and value is the same. Find a fixed point (there can be many, just return 1) in
# a sorted list of distinct elements, or return None if it doesn't exist.
#
# Here is a starting point:
#
# def find_fixed_point(nums):
#   # Fill this in.
#
# print find_fixed_point([-5, 1, 3, 4])
# # 1
#
# Can you do this in sublinear time?
from typing import List


# Finding the first fixed point is O(log n) in the worst case. Finding all fixed points is O(n) in the worst case.
def find_fixed_point(nums: List[int]) -> List[int]:
    nums_size: int = len(nums)
    if nums_size == 0:
        return []
    else:
        min_included_index: int = 0
        max_included_index: int = nums_size
        while min_included_index < nums_size and max_included_index >= 0 and min_included_index <= max_included_index:
            middle_index: int = int((max_included_index + min_included_index) / 2)
            if nums[middle_index] == middle_index:
                collected_fixed_points: List[int] = [nums[middle_index]]
                current_index: int = middle_index - 1
                while 0 <= current_index == nums[current_index]:
                    collected_fixed_points.append(nums[current_index])
                    current_index -= 1
                current_index = middle_index + 1
                while nums_size > current_index == nums[current_index]:
                    collected_fixed_points.append(nums[current_index])
                    current_index += 1
                return collected_fixed_points
            elif nums[middle_index] > middle_index:
                max_included_index = middle_index - 1
            else:
                min_included_index = middle_index + 1
        return []


print(find_fixed_point([-5, 1, 3, 4]))
# [1]
print(find_fixed_point([-5, 1, 2, 3, 4, 6]))
# [1, 2, 3, 4]
print(find_fixed_point([0, 1, 2, 3]))
# [0, 1, 2, 3]
print(find_fixed_point([-5]))
# []
print(find_fixed_point([]))
# []
