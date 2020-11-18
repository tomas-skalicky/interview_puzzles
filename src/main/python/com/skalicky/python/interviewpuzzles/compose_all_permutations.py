# Task:
#
# You are given an array of integers. Return all the permutations of this array.
#
# def permute(nums):
#   # Fill this in.
#
# print permute([1, 2, 3])
# # [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
from typing import List, Optional, Set


def permute_recursively(num: int, remaining_nums: List[int], current_permutation: List[Optional[int]],
                        occupied_indices: Set[int],
                        collected_permutations: List[List[int]]) -> None:
    for i in range(0, len(current_permutation)):
        if i not in occupied_indices:
            current_permutation[i] = num
            occupied_indices.add(i)
            if len(remaining_nums) == 0:
                collected_permutations.append(current_permutation.copy())
            else:
                permute_recursively(remaining_nums[0], remaining_nums[1:], current_permutation, occupied_indices,
                                    collected_permutations)
            current_permutation[i] = None
            occupied_indices.remove(i)


# Time and space complexity of this method is O(n!)
def permute(nums: List[int]) -> List[List[int]]:
    num_count: int = len(nums)
    if num_count == 0:
        return []
    else:
        collected_permutations: List[List[int]] = []
        current_permutation: List[Optional[int]] = [None] * num_count
        permute_recursively(nums[0], nums[1:], current_permutation, set(), collected_permutations)
        return collected_permutations


print(permute([]))
# [[]]
print(permute([1]))
# [[1]]
print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
