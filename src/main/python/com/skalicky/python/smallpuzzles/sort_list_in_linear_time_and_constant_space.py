# Task:
#
# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
#
# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]
#
# Challenge: Try sorting the list using constant space.


def sort_nums(nums: list):
    frequency = {1: 0, 2: 0, 3: 0}
    for n in nums:
        frequency[n] = frequency[n] + 1
    result = []
    for n in range(1, 4):
        for i in range(0, frequency[n]):
            result.append(n)
    return result


print(sort_nums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
