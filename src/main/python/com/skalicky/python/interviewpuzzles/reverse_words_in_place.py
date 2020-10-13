# Task:
#
# Given a list of words in a string, reverse the words in-place (ie don't create a new string and reverse the words).
# Since python strings are not mutable, you can assume the input will be a mutable sequence (like list).
#
# Here's an example and some starting code:
#
# def reverse_words(words):
#   # Fill this in.
#
# s = list("can you read this")
# reverse_words(s)
# print(''.join(s))
# # this read you can
from typing import List, Set


def swap_substrings_in_place(words: List[str], substring_1_start_index: int, substring_1_end_index_excluded: int,
                             substring_2_start_index: int) -> None:
    for i in range(substring_1_start_index, substring_1_end_index_excluded):
        temp: str = words[i]
        right_index: int = substring_2_start_index + i - substring_1_start_index
        words[i] = words[right_index]
        words[right_index] = temp


def rotate_substring_to_left(words: List[str], rotation_length: int, substring_start_index: int,
                             substring_end_index_excluded: int) -> None:
    indices_with_rotated_values: Set[int] = set()
    index_span: int = substring_end_index_excluded - substring_start_index
    for i in range(0, rotation_length):
        current_index: int = i
        previous_index_value: str = words[substring_start_index + current_index]
        while not indices_with_rotated_values.__contains__(current_index):
            indices_with_rotated_values.add(current_index)
            new_index: int = (current_index - rotation_length + index_span) % index_span
            if new_index != current_index:
                old_current_index_value: str = words[substring_start_index + new_index]
                words[substring_start_index + new_index] = previous_index_value
                previous_index_value = old_current_index_value

                current_index = new_index


def reverse_words(words: List[str]) -> None:
    left_word_start_index: int = 0
    left_word_end_index_included: int = left_word_start_index
    right_word_end_index_included: int = len(words) - 1
    right_word_start_index: int = right_word_end_index_included
    while True:
        while left_word_end_index_included < right_word_start_index and words[left_word_end_index_included] != ' ':
            left_word_end_index_included += 1

        if left_word_end_index_included >= right_word_start_index:
            return
        else:
            left_word_end_index_included -= 1
            while right_word_start_index > left_word_end_index_included and words[right_word_start_index] != ' ':
                right_word_start_index -= 1
            right_word_start_index += 1

            if left_word_end_index_included >= right_word_start_index:
                raise RuntimeError('This code should be unreachable. left_word_end_index_included [{}] is equal to'
                                   ' right_word_start_index [{}]'.format(left_word_end_index_included,
                                                                         right_word_start_index))
            else:
                left_word_end_index_excluded: int = left_word_end_index_included + 1
                right_word_end_index_excluded: int = right_word_end_index_included + 1
                left_word_length = left_word_end_index_excluded - left_word_start_index
                right_word_length = right_word_end_index_excluded - right_word_start_index
                if left_word_length == right_word_length:
                    swap_substrings_in_place(words, left_word_start_index, left_word_end_index_excluded,
                                             right_word_start_index)
                elif left_word_length > right_word_length:
                    length_difference: int = left_word_length - right_word_length

                    # Swaps the end of the left word with the right word.
                    # Example: "foo yours blabla TO bar" -> "foo youTO blabla rs bar"
                    swap_substrings_in_place(words, left_word_start_index + length_difference,
                                             left_word_end_index_excluded, right_word_start_index)

                    # Rotates a substring by ${length_difference} to the left.
                    # Example: "foo youTO blabla rs bar" -> "foo TO blabla rsyou bar"
                    rotate_substring_to_left(words, length_difference, left_word_start_index,
                                             right_word_end_index_excluded)

                    # Rotates a substring by ${right_word_length} to the left.
                    # Example: "foo TO blabla rsyou bar" -> "foo TO blabla yours bar"
                    rotate_substring_to_left(words, right_word_length, right_word_start_index - length_difference,
                                             right_word_end_index_excluded)
                else:
                    # Rotates a substring by ${left_word_length} to the left.
                    # Example: "foo to blabla YOURS bar" -> "foo blabla YOURSto bar"
                    rotate_substring_to_left(words, left_word_length, left_word_start_index,
                                             right_word_end_index_excluded)

                    # Rotates a substring by ${right_word_start_index - left_word_end_index_excluded} to the
                    # left.
                    # Example: "foo blabla YOURSto bar" -> "foo TO yours bar"
                    rotate_substring_to_left(words, right_word_start_index - left_word_end_index_excluded,
                                             left_word_start_index, right_word_end_index_excluded - left_word_length)

                left_word_start_index = left_word_start_index + right_word_length + 1
                left_word_end_index_included = left_word_start_index
                right_word_end_index_included = right_word_end_index_included - left_word_length - 1
                right_word_start_index = right_word_end_index_included


s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can

s2 = list("can read you this")
reverse_words(s2)
print(''.join(s2))
# this you read can

s3 = list("you read this")
reverse_words(s3)
print(''.join(s3))
# this read you

s4 = list("you")
reverse_words(s4)
print(''.join(s4))
# you

s5 = list("you two")
reverse_words(s5)
print(''.join(s5))
# two you
