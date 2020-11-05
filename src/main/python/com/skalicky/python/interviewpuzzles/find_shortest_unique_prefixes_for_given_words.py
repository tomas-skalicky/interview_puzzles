# Task:
#
# Given a list of words, for each word find the shortest unique prefix. You can assume a word will not be a substring
# of another word (ie play and playing won't be in the same words list)
#
# Example
#
# Input: ['joma', 'john', 'jack', 'techlead']
# Output: ['jom', 'joh', 'ja', 't']
#
# Here's some starter code:
#
# def shortest_unique_prefix(words):
#   # Fill this in.
#
# print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# # ['jom', 'joh', 'ja', 't']
from typing import List, Dict


def shortest_unique_prefix(input_words: List[str]) -> List[str]:
    shortest_unique_prefixes_by_words: Dict[str, str] = {}
    remaining_words_to_process: List[str] = list(input_words)
    prefix_length: int = 0
    while len(remaining_words_to_process) > 0:
        prefix_length += 1
        words_by_prefix_candidates: Dict[str, List[str]] = {}
        for current_word in remaining_words_to_process:
            if prefix_length > len(current_word):
                raise RuntimeError(
                    'There is no list of shortest unique prefixes for the given list [{}].'.format(input_words))
            else:
                prefix_candidate: str = current_word[0:prefix_length]
                if words_by_prefix_candidates.__contains__(prefix_candidate):
                    words_by_prefix_candidates[prefix_candidate].append(current_word)
                else:
                    words_by_prefix_candidates[prefix_candidate] = [current_word]

        for prefix_candidate in words_by_prefix_candidates.keys():
            current_words: List[str] = words_by_prefix_candidates[prefix_candidate]
            if len(current_words) == 1:
                current_word: str = current_words[0]
                shortest_unique_prefixes_by_words[current_word] = prefix_candidate
                remaining_words_to_process.remove(current_word)
    return [shortest_unique_prefixes_by_words[word] for word in input_words]


print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']

print(shortest_unique_prefix(['play', 'playing']))
# RuntimeError
