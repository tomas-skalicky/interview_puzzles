# Task:
#
# Given a string, we want to remove 2 adjacent characters that are the same, and repeat the process with the new string
# until we can no longer perform the operation.
#
# Here's an example and some starter code:
#
# def remove_adjacent_dup(s):
#   # Fill this in.
#
# print(remove_adjacent_dup("cabba"))
# # Start with cabba
# # After remove bb: caa
# # After remove aa: c
# # print c


def remove_recursively_2_same_adjacent_characters(input_string: str) -> str:
    """Time complexity ... O(n) where *n* is the length of the input string because the algorithm visits every element
    maximum three times, two times when going from the left to the right and once when going from the right to the left.
    """

    remaining_string: str = input_string
    index_to_process: int = 0
    while index_to_process < len(remaining_string) - 1:
        if remaining_string[index_to_process] == remaining_string[index_to_process + 1]:
            left = remaining_string[:index_to_process] if index_to_process > 0 else ''
            right = remaining_string[index_to_process + 2:] if index_to_process < len(input_string) - 2 else ''
            remaining_string = left + right
            index_to_process = index_to_process - 1 if index_to_process > 0 else 0
        else:
            index_to_process += 1
    return remaining_string
