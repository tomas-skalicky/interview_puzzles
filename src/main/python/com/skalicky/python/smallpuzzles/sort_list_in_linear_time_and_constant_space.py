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
    frequency: list = [0, 0, 0]
    for n in nums:
        frequency[n - 1] = frequency[n - 1] + 1
    result = []
    for n in range(0, 3):
        for i in range(0, frequency[n]):
            result.append(n + 1)
    return result


print(sort_nums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
