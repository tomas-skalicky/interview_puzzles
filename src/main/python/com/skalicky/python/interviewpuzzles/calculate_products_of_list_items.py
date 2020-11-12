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


def calculate_products_of_list_items(input_numbers: List[int]) -> List[int]:
    if len(input_numbers) == 0:
        return []
    else:
        product: int = 1
        for n in input_numbers:
            product *= n
        result: List[int] = []
        for n in input_numbers:
            result.append(floor(product / n))
        return result
