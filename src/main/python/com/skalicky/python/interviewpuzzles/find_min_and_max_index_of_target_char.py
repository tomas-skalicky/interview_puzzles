# Task:
#
# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of
# a target element, x. Return -1 if the target is not found.
#
# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]
#
# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]
#
# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]
#
# Here is a function signature example:
#
# class Solution:
#   def getRange(self, arr, target):
#     # Fill this in.
#
# # Test program
# arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# x = 2
# print(Solution().getRange(arr, x))
# # [1, 4]


class Solution:
    @staticmethod
    def get_range(input_array: list, input_target: int):
        min_index: int = -1
        length = len(input_array)
        for i in range(0, length):
            if input_array[i] == input_target:
                min_index = i
                break
        if min_index == -1:
            return -1, -1
        for i in range(0, length):
            j: int = length - 1 - i
            if input_array[j] == input_target:
                return min_index, j
        raise RuntimeError('Unreachable code')


# Test program
A = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(Solution.get_range(A, target))
# [1, 4]

A = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
target = 9
print(Solution.get_range(A, target))
# [6,8]

A = [100, 150, 150, 153]
target = 150
print(Solution.get_range(A, target))
# [1,2]

A = [1, 2, 3, 4, 5, 6, 10]
target = 9
print(Solution.get_range(A, target))
# [-1, -1]
