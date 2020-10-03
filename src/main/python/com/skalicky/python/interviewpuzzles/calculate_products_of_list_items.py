# Task:
#
# You are given an array of integers. Return an array of the same size where the element at each index is the product
# of all the elements in the original array except for the element at that index.
#
# For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].
#
# You cannot use division in this problem.
#
# Here's a start:
#
# def products(nums):
#   # Fill this in.
#
# print products([1, 2, 3, 4, 5])
# # [120, 60, 40, 30, 24]
from math import floor
from typing import List


def products(nums: List[int]) -> List[int]:
    if len(nums) == 0:
        return []
    else:
        product: int = 1
        for n in nums:
            product *= n
        result: List[int] = []
        for n in nums:
            result.append(floor(product / n))
        return result


print(products([]))
# []
print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
