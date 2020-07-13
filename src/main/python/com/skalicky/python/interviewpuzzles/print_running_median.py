# Task:
#
# You are given a stream of numbers. Compute the median for each new element .
#
# Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
#
# Here's a starting point:
#
# def running_median(stream):
#   # Fill this in.
#
# running_median([2, 1, 4, 7, 2, 0, 5])
# # 2 1.5 2 3.0 2 2.0 2
import sys
from math import floor
from typing import List


# The method has a time complexity of O(n ^ 2)
def running_median(stream: List[int]):
    sorted_stream: List[int] = list()
    for i in range(0, len(stream)):
        current_number: int = stream[i]
        sorted_stream.append(current_number)
        if len(sorted_stream) > 1:
            j: int = i
            # Time complexity of this step is O(n)
            while j > 0 and sorted_stream[j - 1] > current_number:
                sorted_stream[j] = sorted_stream[j - 1]
                sorted_stream[j - 1] = current_number
                j -= 1
        lower_index: int = floor(i / 2)
        current_median = (sorted_stream[lower_index] + sorted_stream[lower_index + 1]) / 2 if (i + 1) % 2 == 0 else \
            sorted_stream[lower_index]
        print(current_median, end=' ')


running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2
