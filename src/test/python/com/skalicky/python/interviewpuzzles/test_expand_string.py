from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.expand_string import expand_string


class Test(TestCase):
    def test_expand_string__when_input_string_is_empty__then_result_string_is_empty(self):
        self.assertEqual('', expand_string(''))

    def test_expand_string__when_input_string_contains_character_0_time__then_result_string_does_not_contain_this_character(
            self):
        self.assertEqual('', expand_string('0[b]'))

    def test_expand_string__when_input_string_contains_character_more_than_1_time__then_result_string_contains_this_character_multiple_times(
            self):
        self.assertEqual('bbbbbbbbbbbbbbbbbbbbbb', expand_string('22[b]'))

    def test_expand_string__when_brackets_are_missing__then_character_is_not_expanded(self):
        self.assertEqual('2a', expand_string('2a'))

    def test_expand_string__when_input_string_contains_multiple_expansions__then_all_expansions_work(self):
        self.assertEqual('aab', expand_string('2[a]1[b]'))

    def test_expand_string__when_input_string_contains_nested_expansion__then_all_expansions_work(self):
        self.assertEqual('abbcabbc', expand_string('2[a2[b]c]'))
