# Task:
#
# You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.
#
# For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you
# should return its length, 4.
#
# def longest_consecutive(nums):
#   # Fill this in.
#
# print longest_consecutive([100, 4, 200, 1, 3, 2])
# # 4
#
# Can you do this in linear time?
from typing import List, Optional, Set


def find_length_of_longest_consecutive_sequence_in_non_sorted_array(nums: List[int]) -> int:
    if len(nums) < 1:
        return 0
    else:
        max_num: Optional[int] = None
        min_num: Optional[int] = None
        # Time complexity O(n) where n is the length of the input
        for n in nums:
            max_num = max(max_num, n) if max_num is not None else n
            min_num = min(min_num, n) if min_num is not None else n

        # Time complexity O(n)
        num_set: Set[int] = set(nums)

        # Time complexity O(m) where m is the different between the minimum and maximum in the input
        max_consecutive_sequence_length: int = 1
        current_consecutive_sequence_length: int = 1
        previous_num: int = min_num
        for n in range(min_num + 1, max_num + 1):
            if n in num_set and n == previous_num + 1:
                current_consecutive_sequence_length += 1
            else:
                max_consecutive_sequence_length = max(max_consecutive_sequence_length,
                                                      current_consecutive_sequence_length)
                current_consecutive_sequence_length = 0
            previous_num = n
        return max_consecutive_sequence_length
