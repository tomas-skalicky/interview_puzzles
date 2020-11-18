# Task:
#
# Given a list of numbers, where every number shows up twice except for one number, find that one number.
#
# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1
#
# Challenge: Find a way to do this using O(1) memory.
#
# Here's the function signature:
#
# def singleNumber(nums):
#   # Fill this in.
#
# print singleNumber([4, 3, 2, 4, 1, 3, 2])
# # 1
from typing import List, Optional, Set


def find_single_occurrence_in_list_with_time_complexity_o_n(input_numbers: List[int]) -> Optional[int]:
    seen_numbers: Set[int] = set()
    for n in input_numbers:
        if n in seen_numbers:
            seen_numbers.remove(n)
        else:
            seen_numbers.add(n)
    if len(seen_numbers) == 0:
        return None
    else:
        return seen_numbers.pop()


def find_single_occurrence_in_list_with_space_complexity_o_1(input_numbers: List[Optional[int]]) -> Optional[int]:
    number_count: int = len(input_numbers)
    if number_count == 0:
        return None
    else:
        i: int = 0
        while i < number_count:
            first: int = input_numbers[i]
            j: int = i + 1
            while j < number_count:
                if input_numbers[j] == first:
                    input_numbers[i] = None
                    input_numbers[j] = None
                    break
                j += 1
            if input_numbers[i] is not None:
                return first
            i += 1
        return None


print(find_single_occurrence_in_list_with_time_complexity_o_n([4, 3, 2, 4, 1, 3, 2]))
# 1

print(find_single_occurrence_in_list_with_space_complexity_o_1([4, 3, 2, 4, 1, 3, 2]))
# 1

print(find_single_occurrence_in_list_with_time_complexity_o_n([]))
# None

print(find_single_occurrence_in_list_with_space_complexity_o_1([]))
# None

print(find_single_occurrence_in_list_with_time_complexity_o_n([4]))
# 4

print(find_single_occurrence_in_list_with_space_complexity_o_1([4]))
# 4

print(find_single_occurrence_in_list_with_time_complexity_o_n([4, 3, 2, 4, 3, 2]))
# None

print(find_single_occurrence_in_list_with_space_complexity_o_1([4, 3, 2, 4, 3, 2]))
# None
