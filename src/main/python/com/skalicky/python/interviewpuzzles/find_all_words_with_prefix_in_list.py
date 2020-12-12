# Task:
#
# Implement auto-completion. Given a large set of words (for instance 1,000,000 words) and then a single word prefix,
# find all words that it can complete to.
#
# class Solution:
#     def build(self, words):
#         # Fill this in.
#
#     def find_all_words_with_prefix(self, prefix):
#         # Fill this in.
#
# s = Solution()
# s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
# print(s.find_all_words_with_prefix('do'))
# # ['dog', 'door', 'dodge']
#
#
# Can you solve this optimally (in linear time with regards to the result set)?
from typing import Dict, List, Set


class PrefixTreeNode:
    def __init__(self):
        self.next_nodes_by_letters: Dict[str, PrefixTreeNode] = {}
        self.words_with_prefix: Set[str] = set()


class Solution:
    def __init__(self):
        self.root_node: PrefixTreeNode = PrefixTreeNode()

    def build(self, words: List[str]) -> None:
        """Time complexity ... O(n * m) where *n* is the number of input words and *m* is the length of the longest
        input word
        """

        self.root_node = PrefixTreeNode()
        for word in words:
            current_node: PrefixTreeNode = self.root_node
            for letter in word:
                if letter in current_node.next_nodes_by_letters:
                    current_node = current_node.next_nodes_by_letters[letter]
                else:
                    new_node = PrefixTreeNode()
                    current_node.next_nodes_by_letters[letter] = new_node
                    current_node = new_node
                current_node.words_with_prefix.add(word)

    def find_all_words_with_prefix(self, prefix: str) -> Set[str]:
        """Time complexity ... O(m) where *m* is the length of the *prefix*
        """

        current_node: PrefixTreeNode = self.root_node
        for letter in prefix:
            if letter in current_node.next_nodes_by_letters:
                current_node = current_node.next_nodes_by_letters[letter]
            else:
                return set()
        return current_node.words_with_prefix
