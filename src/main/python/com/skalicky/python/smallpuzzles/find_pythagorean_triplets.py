# Task:
#
# Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables
# a, b, c where a^2 + b^2 = c^2
#
# Example:
# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 5^2 + 12^2 = 13^2.
#
# def findPythagoreanTriplets(nums):
#   # Fill this in.
#
# print findPythagoreanTriplets([3, 12, 5, 13])
# # True


def find_pythagorean_triplets(nums: list):
    if len(nums) < 3:
        return False
    squares_set = set()
    for n in nums:
        squares_set.add(n * n)
    sorted_squares: list = sorted(squares_set)
    sorted_count = len(sorted_squares)
    max_item: int = sorted_squares[sorted_count - 1]
    for i in range(0, sorted_count - 2):
        for j in range(i + 1, sorted_count - 1):
            summed: int = sorted_squares[i] + sorted_squares[j]
            if squares_set.__contains__(summed):
                return True
            elif summed > max_item:
                break
    return False


print(find_pythagorean_triplets([3, 12, 5, 13]))
# True
print(find_pythagorean_triplets([3, 5, 12, 5, 13]))
# True
print(find_pythagorean_triplets([3, 5, 4]))
# True
print(find_pythagorean_triplets([3, 6, 4]))
# False
