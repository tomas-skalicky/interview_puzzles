# Task:
#
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving
# whitespace and initial word order.
#
# Example 1:
# Input: "The cat in the hat"
# Output: "ehT tac ni eht tah"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.
#
# Here's a starting point:
#
# class Solution:
#   def reverseWords(self, str):
#     # Fill this in.
#
# print Solution().reverseWords("The cat in the hat")
# # ehT tac ni eht tah


class Solution:
    @staticmethod
    def reverse_words(input_string: str) -> str:
        result: str = ""
        string_length: int = len(input_string)
        word_start_to_process: int = 0
        while word_start_to_process < string_length:
            word_end_to_process: int = input_string.find(" ", word_start_to_process, string_length)
            last_word: bool = False
            if word_end_to_process < 0:
                word_end_to_process = string_length
                last_word = True
            for i in range(0, word_end_to_process - word_start_to_process):
                result += input_string[word_end_to_process - i - 1]
            if not last_word:
                result += " "
            word_start_to_process = word_end_to_process + 1
        return result


print(Solution.reverse_words("The cat in the hat"))
# ehT tac ni eht tah
