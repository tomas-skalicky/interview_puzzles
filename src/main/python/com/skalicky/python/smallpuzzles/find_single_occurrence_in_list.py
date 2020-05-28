# Task:
#
# Given a list of numbers, where every number shows up twice except for one number, find that one number.
#
# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1
#
# Challenge: Find a way to do this using O(1) memory.


def single_number_in_time_complexity_o_n(nums: list):
    seen_numbers = set()
    for n in nums:
        if seen_numbers.__contains__(n):
            seen_numbers.remove(n)
        else:
            seen_numbers.add(n)
    if len(seen_numbers) == 0:
        return None
    else:
        return list(seen_numbers)[0]


def single_number_in_space_complexity_o_1(nums: list):
    if len(nums) == 0:
        return None
    i = 0
    while i < len(nums):
        first = nums[i]
        if first is not None:
            j = i + 1
            while j < len(nums):
                if nums[j] == first:
                    nums[i] = None
                    nums[j] = None
                    break
                j = j + 1
            if nums[i] is not None:
                return first
        i = i + 1
    return None


print(single_number_in_time_complexity_o_n([4, 3, 2, 4, 1, 3, 2]))
# 1

print(single_number_in_space_complexity_o_1([4, 3, 2, 4, 1, 3, 2]))
# 1

print(single_number_in_time_complexity_o_n([]))
# None

print(single_number_in_space_complexity_o_1([]))
# None

print(single_number_in_time_complexity_o_n([4]))
# 4

print(single_number_in_space_complexity_o_1([4]))
# 4

print(single_number_in_time_complexity_o_n([4, 3, 2, 4, 3, 2]))
# None

print(single_number_in_space_complexity_o_1([4, 3, 2, 4, 3, 2]))
# None
