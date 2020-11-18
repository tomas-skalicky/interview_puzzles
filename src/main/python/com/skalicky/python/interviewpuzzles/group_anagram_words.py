# Task:
#
# Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same
# letters).
#
# Example:
#
# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
#
# Here's a starting point:
#
# import collections
#
# def groupAnagramWords(strs):
#   # Fill this in.
#
# print groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg'])
# # [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]


from typing import Dict, List, Tuple


def word_to_frequencies_by_chars(word: str):
    frequencies_by_chars: Dict[str, int] = {}
    for c in list(word):
        if c in frequencies_by_chars:
            frequencies_by_chars[c] += 1
        else:
            frequencies_by_chars[c] = 0
    return frequencies_by_chars


def identical_frequencies_by_chars_for_words_having_the_same_length(one: Dict[str, int], two: Dict[str, int]):
    for c in one.keys():
        if c not in two or one[c] != two[c]:
            return False
    return True


def group_anagram_words(strs: List[str]):
    next_group_id: int = 0
    group_ids_and_frequencies_by_chars_by_word_length: Dict[int, List[Tuple[int, Dict[str, int]]]] = {}
    anagram_words_by_group_ids: Dict[int, List[str]] = {}
    for word in strs:
        current_length: int = len(word)
        current_frequencies_by_chars: Dict[str, int] = word_to_frequencies_by_chars(word)

        current_length_exists: bool = current_length in group_ids_and_frequencies_by_chars_by_word_length
        found: bool = False
        if current_length_exists:
            # Searches only in groups having the same length.
            for group_ids_and_frequencies_by_chars in group_ids_and_frequencies_by_chars_by_word_length[current_length]:
                if identical_frequencies_by_chars_for_words_having_the_same_length(current_frequencies_by_chars,
                                                                                   group_ids_and_frequencies_by_chars[
                                                                                       1]):
                    group_id: int = group_ids_and_frequencies_by_chars[0]
                    anagram_words_by_group_ids[group_id].append(word)
                    found = True
                    break

        if not found:
            if current_length_exists:
                group_ids_and_frequencies_by_chars_by_word_length[current_length].append(
                    (next_group_id, current_frequencies_by_chars))
            else:
                group_ids_and_frequencies_by_chars_by_word_length[current_length] = [
                    (next_group_id, current_frequencies_by_chars)]
            anagram_words_by_group_ids[next_group_id] = [word]
            next_group_id += 1
    return anagram_words_by_group_ids.values()


print(group_anagram_words(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
print(group_anagram_words(['abca', 'cbab', 'cbaa']))
# [['abca', 'cbaa'], ['cbab']]
print(group_anagram_words(['abc', 'abcc']))
# [['abc'], ['abcc']]
