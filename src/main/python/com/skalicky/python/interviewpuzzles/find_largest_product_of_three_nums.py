# Task:
#
# You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers
# in the array.
#
# Example:
#
# [-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.
#
# Here's a starting point:
#
# def maximum_product_of_three(lst):
#   # Fill this in.
#
# print maximum_product_of_three([-4, -4, 2, 8])
# # 128
from typing import List


# The time complexity of this algorithm is O(n log n) due to sorting of the input list.
# The naive algorithm using 3 for-loops would have O(n^3) time complexity.
def maximum_product_of_three(lst: List[int]):
    list_size: int = len(lst)
    if list_size < 3:
        return None
    else:
        # O(n x lon n)
        sorted_list: List[int] = sorted(lst)
        product_in_case_of_large_negative_nums: int = sorted_list[0] * sorted_list[1] * sorted_list[list_size - 1]
        return max(product_in_case_of_large_negative_nums,
                   sorted_list[list_size - 3] * sorted_list[list_size - 2] * sorted_list[list_size - 1])


print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
print(maximum_product_of_three([1, -4, 2, 8]))
# 16
print(maximum_product_of_three([-4, -4]))
# None
