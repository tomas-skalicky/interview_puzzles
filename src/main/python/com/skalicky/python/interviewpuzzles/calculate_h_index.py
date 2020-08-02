# Task:
#
# The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar.
# The definition of the h-index is if a scholar has at least h of their papers cited h times.
#
# Given a list of publications of the number of citations a scholar has, find their h-index.
#
# Example:
# Input: [3, 5, 0, 1, 3]
# Output: 3
# Explanation:
# There are 3 publications with 3 or more citations, hence the h-index is 3.
#
# Here's a starting point:
#
# def hIndex(publications):
#   # Fill this in.
#
# print hIndex([5, 3, 3, 1, 0])
# # 3
from typing import List


# Time complexity is O(n * log n) due to sorting of input list.
def h_index(publications: List[int]) -> int:
    sorted_publications_desc: List[int] = sorted(publications, reverse=True)
    publication_count: int = 0
    for publication in sorted_publications_desc:
        publication_count += 1
        if publication <= publication_count:
            return publication
    return 0


print(h_index([]))
# 0
print(h_index([5, 3, 3, 1, 0]))
# 3
print(h_index([3, 5, 0, 1, 3]))
# 3
print(h_index([3, 5, 0, 1, 3, 3]))
# 3
