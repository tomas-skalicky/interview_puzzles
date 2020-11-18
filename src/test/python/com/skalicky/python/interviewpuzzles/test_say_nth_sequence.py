from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.say_nth_sequence import say_nth_sequence


class Test(TestCase):
    def test_say_nth_sequence__when_n_is_0__then_exception_is_raised(self):
        self.assertRaisesRegex(RuntimeError, 'non allowed n \\[0]', say_nth_sequence, 0)

    def test_say_nth_sequence__when_n_is_1__then_result_is_list_with_1(self):
        self.assertEqual([1], say_nth_sequence(1))

    def test_say_nth_sequence__when_n_is_2__then_result_is_1x1(self):
        # 11 ....... one 1's
        self.assertEqual([1, 1], say_nth_sequence(2))

    def test_say_nth_sequence__when_n_is_3__then_result_is_2x1(self):
        # 21 ....... two 1's
        self.assertEqual([2, 1], say_nth_sequence(3))

    def test_say_nth_sequence__when_n_is_4__then_result_is_1x2_and_1x1(self):
        # 1211 ..... one 2's and one 1's
        self.assertEqual([1, 2, 1, 1], say_nth_sequence(4))

    def test_say_nth_sequence__when_n_is_5__then_result_is_1x1_and_1x2_and_2x1(self):
        # 111221 ... one 1's, one 2's and two 1's
        self.assertEqual([1, 1, 1, 2, 2, 1], say_nth_sequence(5))
