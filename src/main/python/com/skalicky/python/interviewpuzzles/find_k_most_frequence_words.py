# Task:
#
# Given a non-empty list of words, return the k most frequent words. The output should be sorted from highest to lowest
# frequency, and if two words have the same frequency, the word with lower alphabetical order comes first. Input will
# contain only lower-case letters.
#
# Example:
# Input: ["daily", "interview", "pro", "pro",
# "for", "daily", "pro", "problems"], k = 2
# Output: ["pro", "daily"]
# class Solution(object):
#   def topKFrequent(self, words, k):
#     # Fill this in.
#
# words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
# k = 2
# print(Solution().topKFrequent(words, k))
# # ['pro', 'daily']
from typing import Dict, List


class Solution:
    @staticmethod
    def top_k_frequent(words: List[str], k: int) -> List[str]:
        frequencies_by_words: Dict[str, int] = {}
        max_frequency: int = 0
        for word in words:
            if frequencies_by_words.__contains__(word):
                frequencies_by_words[word] += 1
            else:
                frequencies_by_words[word] = 1
            max_frequency = max(max_frequency, frequencies_by_words[word])

        word_lists_by_frequencies: Dict[int, List[str]] = {}
        for word in frequencies_by_words.keys():
            frequency: int = frequencies_by_words[word]
            if not word_lists_by_frequencies.__contains__(frequency):
                word_lists_by_frequencies[frequency] = []
            word_lists_by_frequencies[frequency].append(word)

        result: List[str] = []
        current_frequency: int = max_frequency
        while len(result) < k and current_frequency > 0:
            if word_lists_by_frequencies.__contains__(current_frequency):
                sorted_words: List[str] = sorted(word_lists_by_frequencies[current_frequency])
                current_index: int = 0
                while len(result) < k and current_index < len(sorted_words):
                    result.append(sorted_words[current_index])
                    current_index += 1
            current_frequency -= 1
        if len(result) < k:
            raise RuntimeError('RuntimeError: Not enough different words to return k different words')
        else:
            return result


print(Solution.top_k_frequent(["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"], 2))
# ['pro', 'daily']
print(Solution.top_k_frequent(["dailyk", "interview", "daily"], 1))
# ['daily']
print(Solution.top_k_frequent(["daily"], 0))
# []
print(Solution.top_k_frequent(["daily", "daily"], 2))
# RuntimeError
