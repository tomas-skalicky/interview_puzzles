# Task:
#
# Return the longest run of 1s for a given integer n's binary representation.
#
# Example:
# Input: 242
# Output: 4
# 242 in binary is 0b11110010, so the longest run of 1 is 4.
#
# def find_longest_run_of_ones_in_binary_representation(n):
#     # Fill this in.
#
# print find_longest_run_of_ones_in_binary_representation(242)
# # 4


def find_longest_run_of_ones_in_binary_representation(input_integer: int) -> int:
    binary_representation: str = bin(input_integer).split('b')[1]
    max_count: int = 0
    current_count: int = 0
    for current_digit in list(binary_representation):
        if current_digit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count
