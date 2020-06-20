# Task:
#
# You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted, and
# could contain overlapping intervals. Return another array where the overlapping intervals are merged.
#
# For example:
# [(1, 3), (5, 8), (4, 10), (20, 25)]
#
# This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).
#
# Here's a starting point:
#
# def merge(intervals):
#   # Fill this in.
#
# print merge([(1, 3), (5, 8), (4, 10), (20, 25)])
# # [(1, 3), (4, 10), (20, 25)]
from typing import List, Tuple


def merge(intervals: List[Tuple[int, int]]):
    sorted_intervals: List[Tuple[int, int]] = sorted(intervals)
    result_intervals: List[Tuple[int, int]] = list()
    start_to_persist: int = None
    end_to_persist: int = None
    for interval in sorted_intervals:
        if start_to_persist:
            if interval[0] > end_to_persist:
                result_intervals.append((start_to_persist, end_to_persist))
                start_to_persist = interval[0]
                end_to_persist = interval[1]
            else:
                end_to_persist = max(end_to_persist, interval[1])
        else:
            start_to_persist = interval[0]
            end_to_persist = interval[1]
    if start_to_persist:
        result_intervals.append((start_to_persist, end_to_persist))
    return result_intervals


print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
print(merge([(1, 3), (3, 3), (3, 4), (18, 20), (5, 8), (4, 10), (20, 25), (-1, 0)]))
# [(-1, 0), (1, 10), (18, 25)]
