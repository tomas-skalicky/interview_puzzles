# Task:
#
# Given a positive integer n, find all primes less than n.
#
# Here's an example and some starter code:
#
# def find_primes(n):
#   # Fill this in.
from collections import deque
from typing import List, Deque


def find_all_primes_less_than_n(n: int) -> List[int]:
    """Time complexity ... O(n ^ 2)
    """

    if n <= 2:
        return []
    else:
        # Exclusion is a small optimization which does not change the asymptotic time complexity.
        result_primes: List[int] = [2]
        # Deque used because we can profit from an efficient removal of the head of the collection (in case of Deque
        # O(1)).
        candidates: Deque[int] = deque()
        for candidate in range(3, n, 2):
            candidates.append(candidate)
        while len(candidates) > 0:
            current_candidate: int = candidates.popleft()
            result_primes.append(current_candidate)
            new_candidates: Deque[int] = deque()
            while len(candidates):
                other_candidate: int = candidates.popleft()
                if other_candidate % current_candidate != 0:
                    new_candidates.append(other_candidate)
            candidates = new_candidates
        return result_primes
