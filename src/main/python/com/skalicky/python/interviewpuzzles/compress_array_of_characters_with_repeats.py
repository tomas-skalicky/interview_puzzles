# Task:
#
# Given an array of characters with repeats, compress it in place. The length after compression should be less than or
# equal to the original array.
#
# Example:
# Input: ['a', 'a', 'b', 'c', 'c', 'c']
# Output: ['a', '2', 'b', 'c', '3']
# Here's a starting point:
#
# class Solution(object):
#   def compress(self, chars):
#     # Fill this in.
#
# print Solution().compress(['a', 'a', 'b', 'c', 'c', 'c'])
# # ['a', '2', 'b', 'c', '3']
from typing import List


class Solution:
    @staticmethod
    def compress(chars: List[str]) -> List[str]:
        char_count: int = len(chars)
        if char_count < 2:
            return chars
        else:
            result: List[str] = []
            previous_char: str = chars[0]
            previous_char_count: int = 1
            for i in range(1, char_count):
                current_char: str = chars[i]
                if previous_char == current_char:
                    previous_char_count += 1
                else:
                    result.append(previous_char)
                    if previous_char_count != 1:
                        result.append(str(previous_char_count))
                    previous_char = current_char
                    previous_char_count = 1
            result.append(previous_char)
            if previous_char_count != 1:
                result.append(str(previous_char_count))
            return result


print(Solution.compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']
print(Solution.compress(['a', 'a', 'b', 'a']))
# ['a', '2', 'b', 'a']
