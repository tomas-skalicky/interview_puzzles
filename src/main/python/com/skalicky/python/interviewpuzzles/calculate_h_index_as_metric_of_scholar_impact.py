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


def calculate_h_index_as_metric_of_scholar_impact(paper_citation_counts: List[int]) -> int:
    """Time complexity is O(n * log n) due to sorting of input List.
    """

    paper_citation_counts_sorted_descendingly: List[int] = sorted(paper_citation_counts, reverse=True)
    paper_count: int = 0
    for paper_citation_count in paper_citation_counts_sorted_descendingly:
        paper_count += 1
        if paper_citation_count <= paper_count:
            return paper_citation_count
    return 0
