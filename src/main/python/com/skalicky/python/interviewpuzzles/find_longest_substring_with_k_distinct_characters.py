# Task:
#
# You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most
# k distinct characters.
#
# For instance, given the string:
# aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.
#
# Here's a starting point:
#
# def longest_substring_with_k_distinct_characters(s, k):
#   # Fill this in.
#
# print longest_substring_with_k_distinct_characters('aabcdefff', 3)
# # 5 (because 'defff' has length 5 with 3 characters)
from typing import Dict, List, Optional, Tuple


def count_distinct_chars(chars: List[str], from_index: int, to_index: int):
    distinct_chars: Dict[str, int] = {}
    for i in range(from_index, to_index + 1):
        current_char: str = chars[i]
        if current_char in distinct_chars:
            distinct_chars[current_char] += 1
        else:
            distinct_chars[current_char] = 1
    return distinct_chars


def longest_substring_with_k_distinct_characters(s: str, k: int) -> Tuple[int, str]:
    chars: List[str] = list(s)
    char_count: int = len(chars)
    if char_count == 0:
        return 0, ''
    elif k == 0:
        return 0, ''
    else:
        start_index_included: int = 0
        max_length: int = 0
        max_substring: Optional[List[str]] = None
        for end_index_excluded in range(0, char_count):
            distinct_char_count: Dict[str, int] = count_distinct_chars(chars, start_index_included, end_index_excluded)
            while len(distinct_char_count.keys()) > k:
                removed_start_char: str = chars[start_index_included]
                start_index_included += 1
                if distinct_char_count[removed_start_char] == 1:
                    distinct_char_count.pop(removed_start_char)
                else:
                    distinct_char_count = count_distinct_chars(chars, start_index_included, end_index_excluded)
            current_max: int = end_index_excluded - start_index_included + 1
            if current_max > max_length:
                max_length = current_max
                max_substring = chars[start_index_included:end_index_excluded + 1]
        return max_length, ''.join(max_substring)


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 distinct characters)
print(longest_substring_with_k_distinct_characters('aabacadefff', 3))
# 6 (because 'aabaca' has length 6 with 3 distinct characters)
print(longest_substring_with_k_distinct_characters('aabaca', 4))
# 6 (because 'aabaca' has length 6 with 3 distinct characters)
