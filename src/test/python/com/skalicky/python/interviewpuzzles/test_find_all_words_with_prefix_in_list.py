from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_all_words_with_prefix_in_list import Solution


class TestSolution(TestCase):
    def test_find_all_words_with_prefix__when_there_are_words_in_list_with_prefix__then_these_words_are_returned(self):
        s: Solution = Solution()
        s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
        self.assertSetEqual({'dog', 'door', 'dodge'}, s.find_all_words_with_prefix('do'))

    def test_find_all_words_with_prefix__when_there_are_no_words_in_list_with_prefix__then_output_is_empty(self):
        s: Solution = Solution()
        s.build(['dog'])
        self.assertSetEqual(set(), s.find_all_words_with_prefix('dr'))
