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


def find_witnesses_of_murder(people_heights: List[int]):
    people_count: int = len(people_heights)
    if people_count == 0:
        return 0
    else:
        witness_count: int = 1
        height_of_currently_tallest_witness = people_heights[people_count - 1]
        for i in reversed(range(0, people_count - 1)):
            current_height: int = people_heights[i]
            if current_height > height_of_currently_tallest_witness:
                witness_count += 1
                height_of_currently_tallest_witness = current_height
        return witness_count
