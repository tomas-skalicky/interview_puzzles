# Task:
#
# Given a list of sorted numbers (can be both negative or positive), return the list of numbers squared in sorted order.
#
# Here's an example and some starting code:
#
# def square_numbers(nums):
#  # Fill this in.
#
# print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# # [0, 1, 1, 9, 16, 25, 25]
#
#
# Solve this problem in O(n) time.
from typing import List, Optional


def square_numbers(nums: List[int]) -> List[int]:
    index_of_first_non_negative_number: Optional[int] = None
    number_count: int = len(nums)
    for i in range(0, number_count):
        number: int = nums[i]
        if number >= 0:
            index_of_first_non_negative_number = i
            break
    if index_of_first_non_negative_number is None:
        result_list: List[int] = []
        for i in reversed(range(0, number_count)):
            result_list.append(nums[i] ** 2)
        return result_list
    else:
        result_list: List[int] = []
        index_of_negative_numbers: int = index_of_first_non_negative_number - 1
        index_of_non_negative_numbers: int = index_of_first_non_negative_number
        while index_of_negative_numbers >= 0 or index_of_non_negative_numbers < number_count:
            if index_of_negative_numbers < 0:
                result_list.append(nums[index_of_non_negative_numbers] ** 2)
                index_of_non_negative_numbers += 1
            elif index_of_non_negative_numbers >= number_count:
                result_list.append(nums[index_of_negative_numbers] ** 2)
                index_of_negative_numbers -= 1
            else:
                current_negative_in_absolute: int = abs(nums[index_of_negative_numbers])
                current_positive: int = nums[index_of_non_negative_numbers]
                if current_negative_in_absolute < current_positive:
                    result_list.append(nums[index_of_negative_numbers] ** 2)
                    index_of_negative_numbers -= 1
                else:
                    result_list.append(nums[index_of_non_negative_numbers] ** 2)
                    index_of_non_negative_numbers += 1
        return result_list


print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]
print(square_numbers([-5, -3, -1]))
# [1, 9, 25]
print(square_numbers([-5, -3, -1, 1, 4, 5]))
# [1, 1, 9, 16, 25, 25]
