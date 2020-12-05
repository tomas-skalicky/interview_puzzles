# Task:
#
# Given a list of strings, find the longest common prefix between all strings.
#
# Here's some examples and some starter code.
#
# def find_longest_common_prefix(strings):
#     # Fill this in.
#
# print(find_longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
# # hell
#
# print(find_longest_common_prefix(['daily', 'interview', 'pro']))
# # ''
from typing import List


def find_longest_common_prefix(strings: List[str]) -> str:
    string_count: int = len(strings)
    if string_count == 0:
        return ''
    elif string_count == 1:
        return strings[0]
    else:
        min_string_length: int = min([len(string) for string in strings])
        first_string: str = strings[0]
        for i in range(0, min_string_length):
            current_character: str = first_string[i]
            for j in range(1, string_count):
                if current_character != strings[j][i]:
                    return first_string[:i]
        return first_string[:min_string_length]
