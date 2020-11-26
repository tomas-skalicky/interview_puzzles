# Task:
#
# A fixed point in a list is where the value is equal to its index. So for example the list [-5, 1, 3, 4], 1 is a fixed
# point in the list since the index and value is the same. Find all fixed point (there can be many) in
# a sorted list of distinct elements, or return empty Set if it doesn't exist. Find the first point as effective as
# possible.
#
# Here is a starting point:
#
# def find_fixed_point(nums):
#     # Fill this in.
#
# print find_fixed_points([-5, 1, 3, 4])
# # {1}
#
# Can you do this in sublinear time?
from typing import List, Set


# Finding the first fixed point is O(log n) in the worst case. Finding all fixed points is O(n) in the worst case.
def find_fixed_points(input_numbers: List[int]) -> Set[int]:
    number_count: int = len(input_numbers)
    if number_count == 0:
        return set()
    else:
        min_included_index: int = 0
        max_included_index: int = number_count
        while min_included_index < number_count and max_included_index >= 0 and min_included_index <= max_included_index:
            middle_index: int = int((max_included_index + min_included_index) / 2)
            if input_numbers[middle_index] == middle_index:
                collected_fixed_points: Set[int] = {input_numbers[middle_index]}
                current_index: int = middle_index - 1
                while 0 <= current_index == input_numbers[current_index]:
                    collected_fixed_points.add(input_numbers[current_index])
                    current_index -= 1
                current_index = middle_index + 1
                while number_count > current_index == input_numbers[current_index]:
                    collected_fixed_points.add(input_numbers[current_index])
                    current_index += 1
                return collected_fixed_points
            elif input_numbers[middle_index] > middle_index:
                max_included_index = middle_index - 1
            else:
                min_included_index = middle_index + 1
        return set()
