# Task:
#
# You are given a list of n numbers, where every number is at most k indexes away from its properly sorted index. Write
# a sorting algorithm (that will be given the number k) for this list that can solve this in O(n log k)
#
# Example:
#
# Input: [3, 2, 6, 5, 4], k=2
# Output: [2, 3, 4, 5, 6]
#
# As seen above, every number is at most 2 indexes away from its proper sorted index.
#
# Here's a starting point:
#
# def sort_partially_sorted(nums, k):
#   # Fill this in.
#
# print sort_partially_sorted([3, 2, 6, 5, 4], 2)
# # [2, 3, 4, 5, 6]
from math import floor
from typing import List


def sort_partially_sorted_list(input_numbers: List[int], k: int) -> List[int]:
    input_list_length: int = len(input_numbers)
    if input_list_length < 2 or k == 0:
        return input_numbers
    else:
        sorted_list: List[int] = [input_numbers[0]]
        for i in range(1, input_list_length):
            current_number: int = input_numbers[i]
            if current_number > sorted_list[i - 1]:
                sorted_list.append(current_number)
                continue
            else:
                min_index: int = max(0, i - k)
                if ((min_index > 0 and current_number >= sorted_list[
                    min_index - 1]) or min_index == 0) and current_number <= sorted_list[min_index]:
                    sorted_list.insert(min_index, current_number)
                else:
                    max_index: int = i
                    while True:
                        middle_index: int = floor((min_index + max_index) / 2)
                        number_to_the_left: int = sorted_list[middle_index - 1]
                        if number_to_the_left <= current_number <= sorted_list[middle_index]:
                            sorted_list.insert(middle_index, current_number)
                            break
                        elif number_to_the_left > current_number:
                            max_index = middle_index
                        else:
                            min_index = middle_index
        return sorted_list
