# Task:
#
# Find all words that are concatenations of other words in the input set.
#
# Input:
# {"tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"}
#
# Output:
# {'techlead', 'catsdog'}
#
# class Solution:
#     @staticmethod
#     def find_all_concatenated_words_in_dictionary(words):
#         # Fill this in.
#
# input = {"tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"}
#
# print(Solution.find_all_concatenated_words_in_dictionary(input))
#
#
# Note: This question is classified as "hard."
# HINT: Start with a brute-force solution.
from collections import deque
from typing import Deque, Dict, List, Set, Tuple


class Solution:
    @staticmethod
    def find_all_concatenated_words_in_dictionary(words: Set[str]) -> Set[str]:
        """Time complexity ... in the words case O(m ^ (n*m)) where *n* is the number of words in the input and *m* is
        the length of the longest input word. Reason: for each letter in the longest word we need to try to match all
        other (*n*-1) words having the size not larger than *m*.

        The algorithm below uses a sorting of input words by lengths which prunes the number of possibilities.
        """
        word_lists_by_lengths: Dict[int, List[str]] = {}
        for word in words:
            word_length: int = len(word)
            if word_length in word_lists_by_lengths:
                word_lists_by_lengths[word_length].append(word)
            else:
                word_lists_by_lengths[word_length] = [word]

        sorted_lengths: List[int] = sorted(word_lists_by_lengths.keys())
        if len(sorted_lengths) < 2:
            return set()
        else:
            found_concatenated_words: Set[str] = set()

            # candidate ... candidate of a concatenated word
            for candidate_length_index in range(1, len(sorted_lengths)):
                candidate_length: int = sorted_lengths[candidate_length_index]
                candidates_with_indices_in_candidates_and_used_word_sets: Deque[Tuple[str, int, Set[str]]] = deque()
                for candidate in word_lists_by_lengths[candidate_length]:
                    candidates_with_indices_in_candidates_and_used_word_sets.append((candidate, 0, set()))

                while len(candidates_with_indices_in_candidates_and_used_word_sets) > 0:
                    candidate, index_in_candidate, used_word_set = candidates_with_indices_in_candidates_and_used_word_sets.pop()
                    remaining_length: int = len(candidate) - index_in_candidate
                    if remaining_length == 0:
                        found_concatenated_words.add(candidate)
                    else:

                        # word ... word what the candidate may also consist of
                        for word_length_index in range(0, candidate_length_index):
                            word_length: int = sorted_lengths[word_length_index]
                            new_index_in_candidate: int = index_in_candidate + word_length

                            if remaining_length >= word_length:

                                for word in word_lists_by_lengths[word_length]:
                                    if word not in used_word_set and Solution.match_long_word_substring_and_short_word(
                                            candidate, index_in_candidate, word):
                                        new_used_word_set: Set[str] = used_word_set.copy()
                                        new_used_word_set.add(word)
                                        candidates_with_indices_in_candidates_and_used_word_sets.append((candidate,
                                                                                                         new_index_in_candidate,
                                                                                                         new_used_word_set))
                                        # It does not make sense to try other words of the same size, but it may be that
                                        # there is a longer word which would fit as well.
                                        # Example: "cat", "cats" in "catsdog"
                                        break
                            else:
                                # There is no other word which could fit in the current candidate.
                                break

            return found_concatenated_words

    @staticmethod
    def match_long_word_substring_and_short_word(long_word: str, index_in_long_word: int, short_word: str) -> bool:
        short_word_length: int = len(short_word)
        end_index_in_long_word_excluded: int = index_in_long_word + short_word_length
        long_word_substring: str = long_word[index_in_long_word:end_index_in_long_word_excluded]
        return long_word_substring == short_word
