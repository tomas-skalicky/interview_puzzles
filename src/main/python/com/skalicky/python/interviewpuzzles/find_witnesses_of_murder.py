# Task:
#
# There are n people lined up, and each have a height represented as an integer. A murder has happened right in front of
# them, and only people who are taller than everyone in front of them are able to see what has happened. How many
# witnesses are there?
#
# Example:
# Input: [3, 6, 3, 4, 1]
# Output: 3
# Explanation: Only [6, 4, 1] were able to see in front of them.
#  #
#  #
#  # #
# ####
# ####
# #####
# 36341                                 x (murder scene)
# Here's your starting point:
#
# def witnesses(heights):
#   # Fill this in.
#
# print witnesses([3, 6, 3, 4, 1])
# # 3
from typing import List


def witnesses(heights: List[int]):
    if len(heights) == 0:
        return 0
    count: int = 1
    height_of_currently_tallest_witness = heights[len(heights) - 1]
    for i in range(0, len(heights) - 1).__reversed__():
        current_height: int = heights[i]
        if current_height > height_of_currently_tallest_witness:
            count = count + 1
            height_of_currently_tallest_witness = current_height
    return count


print(witnesses([]))
# 0
print(witnesses([3]))
# 1
print(witnesses([3, 6, 3, 4, 1]))
# 3
