# Task:
#
# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that
# add up to k.
#
# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.
#
# Try to do it in a single pass of the list.
#
# def two_sum(list, k):
#   # Fill this in.
#
# print two_sum([4,7,1,-3,2], 5)
# # True


def two_sum(nums: list, k: int):
    if len(nums) < 2:
        return False
    else:
        first_second_number_candidate = k - nums[0]
        second_number_candidates_to_search_for: set = {first_second_number_candidate}
        for i in range(1, len(nums)):
            current_number = nums[i]
            current_second_number_candidate = k - current_number
            if second_number_candidates_to_search_for.__contains__(current_number):
                return True
            else:
                second_number_candidates_to_search_for.add(current_second_number_candidate)
        return False


print(two_sum([4, 7, 1, -3, 2], 5))
# True

print(two_sum([4, 7, 0, -3, 2], 5))
# False

print(two_sum([4], 5))
# False

print(two_sum([8, 1, -3, 2], 5))
# True
