from typing import Optional, List
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.add_two_integers_stored_reversed_in_linked_lists import \
    ListNode, Solution


class TestSolution(TestCase):
    def test_add_two_numbers__when_742_plus_24465__then_reversed_25207_is_returned(self):
        number1_last_digit: ListNode = ListNode(2)
        number1_last_digit.next = ListNode(4)
        number1_last_digit.next.next = ListNode(7)

        number2_last_digit: ListNode = ListNode(5)
        number2_last_digit.next = ListNode(6)
        number2_last_digit.next.next = ListNode(4)
        number2_last_digit.next.next.next = ListNode(4)
        number2_last_digit.next.next.next.next = ListNode(2)

        sum_reversed: Optional[ListNode] = Solution.add_two_integers_stored_reversed_in_linked_lists(number1_last_digit,
                                                                                                     number2_last_digit)
        values: List[int] = []
        while sum_reversed:
            values.append(sum_reversed.val)
            sum_reversed = sum_reversed.next

        self.assertListEqual([7, 0, 2, 5, 2], values)
