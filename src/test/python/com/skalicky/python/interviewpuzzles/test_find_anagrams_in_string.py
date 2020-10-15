from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_anagrams_in_string import find_anagrams


class Test(TestCase):
    def test_find_anagrams__when_text_contains_multiple_non_overlapping_anagram_occurrences__then_all_occurrences_found(
            self):
        self.assertListEqual(find_anagrams('acdbacdacb', 'abc'), [3, 7])

    def test_find_anagrams__when_text_equals_anagram__then_one_anagram_found(self):
        self.assertListEqual(find_anagrams('abc', 'abc'), [0])

    def test_find_anagrams__when_text_contains_overlapping_anagram_occurrences__then_all_occurrences_found(self):
        self.assertListEqual(find_anagrams('acba', 'abc'), [0, 1])

    def test_find_anagrams__when_lengths_of_text_and_anagram_are_equal_and_text_contains_anagram_occurrence__then_occurrence_found(
            self):
        self.assertListEqual(find_anagrams('aacb', 'abac'), [0])

    def test_find_anagrams__when_text_does_not_contain_anagram_occurrences__then_empty_list(self):
        self.assertListEqual(find_anagrams('acd', 'abc'), [])

    def test_find_anagrams__when_text_is_shorter_than_anagram__then_empty_list(self):
        self.assertListEqual(find_anagrams('ac', 'abc'), [])
