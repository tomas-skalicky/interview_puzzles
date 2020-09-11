# Task:
#
# Two words can be 'chained' if the last character of the first word is the same as the first character of the second
# word.
#
# Given a list of words, determine if there is a way to 'chain' all the words in a circle.
#
# Example:
# Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
# Output: True
# Explanation:
# The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.
#
# Here's a start:
#
# from collections import defaultdict
#
# def chainedWords(words):
#   # Fill this in.
#
# print chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna'])
# # True


from typing import List, Dict


def chained_words(words: List[str]):
    if len(words) < 2:
        return False
    else:
        words_by_first_letters: Dict[str, List[str]] = dict()
        words_by_last_letters: Dict[str, List[str]] = dict()
        for word in words:
            first_letter: str = word[0]
            if not words_by_first_letters.__contains__(first_letter):
                words_by_first_letters[first_letter] = list()
            words_by_first_letters[first_letter].append(word)
            last_letter: str = word[len(word) - 1]
            if not words_by_last_letters.__contains__(last_letter):
                words_by_last_letters[last_letter] = list()
            words_by_last_letters[last_letter].append(word)
        for first_letter in words_by_first_letters.keys():
            words_with_first_letter: List[str] = words_by_first_letters[first_letter]
            # Three conditions need to be fulfilled:
            # 1) For each letter appearing as the first letter in a word: there needs to be a word or words having
            #    this letter as the last letter.
            # 2) For each letter appearing as the first letter in a world: the number of occurrences of this letter
            #    as the first letter in a word needs to be equal to the number of occurrences of this letter
            #    as the last letter in a word. In order words, we need to have pairs.
            #    Note: the condition 1) and 2) implies the inverse implication of the condition 1).
            # 3) If there is only one occurrence of a particular letter we need to avoid false positives that a letter
            #    would create a circle with itself, i.e. starting and ending with the same letter.
            if not words_by_last_letters.__contains__(first_letter) or len(words_by_last_letters[first_letter]) != len(
                    words_with_first_letter) or (len(words_with_first_letter) == 1 and words_with_first_letter[0] ==
                                                 words_by_last_letters[first_letter][0]):
                return False
        return True


print(chained_words(['eggs', 'karat', 'apple', 'snack', 'tuna']))
# True
print(chained_words(['apple', 'eggs', 'snack', 'karat', 'luna']))
# False
print(chained_words(['wow', 'waw']))
# True
print(chained_words(['wow', 'lol']))
# False
print(chained_words(['wow']))
# False
