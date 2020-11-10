from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_characters_appearing_in_all_strings import \
    find_characters_appearing_in_all_strings


class Test(TestCase):
    def test_find_characters_appearing_in_all_strings__when_input_contains_no_strings__then_output_is_empty(
            self):
        self.assertSetEqual(set(), find_characters_appearing_in_all_strings([]))

    def test_find_characters_appearing_in_all_strings__when_input_contains_only_1_string__then_all_characters_from_string_are_common(
            self):
        self.assertSetEqual({'c', 'd'}, find_characters_appearing_in_all_strings(['dcd']))

    def test_find_characters_appearing_in_all_strings__when_input_strings_have_no_common_characters__then_output_is_empty(
            self):
        self.assertSetEqual(set(), find_characters_appearing_in_all_strings(['ab', 'cdd', 'e']))

    def test_find_characters_appearing_in_all_strings__when_input_strings_have_common_characters__then_output_are_common_characters(
            self):
        self.assertSetEqual({'e', 'o'}, find_characters_appearing_in_all_strings(['google', 'facebook', 'youtube']))
