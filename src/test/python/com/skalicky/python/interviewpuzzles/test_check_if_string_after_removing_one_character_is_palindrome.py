from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.check_if_string_after_removing_one_character_is_palindrome import \
    check_if_string_after_removing_one_character_is_palindrome


class Test(TestCase):
    def test_create_palindrome__when_abcdcbea__then_true(self):
        self.assertTrue(check_if_string_after_removing_one_character_is_palindrome('abcdcbea'))

    def test_create_palindrome__when_abccba__then_true(self):
        self.assertTrue(check_if_string_after_removing_one_character_is_palindrome('abccba'))

    def test_create_palindrome__when_abccaa__then_false(self):
        self.assertFalse(check_if_string_after_removing_one_character_is_palindrome('abccaa'))
