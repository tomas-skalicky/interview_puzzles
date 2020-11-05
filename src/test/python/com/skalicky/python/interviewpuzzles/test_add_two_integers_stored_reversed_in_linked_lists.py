from typing import Optional, List
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.add_two_integers_stored_reversed_in_linked_lists import \
    ListNode, Solution


class TestSolution(TestCase):
    def test_add_two_numbers(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(7)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        l2.next.next.next = ListNode(4)
        l2.next.next.next.next = ListNode(2)

        result: Optional[ListNode] = Solution.add_two_numbers(l1, l2)
        values: List[int] = []
        while result:
            values.append(result.val)
            result = result.next

        self.assertListEqual([7, 0, 2, 5, 2], values)
