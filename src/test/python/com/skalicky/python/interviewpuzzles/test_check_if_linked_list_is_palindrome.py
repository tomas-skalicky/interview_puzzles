from typing import List, Optional
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.check_if_linked_list_is_palindrome import \
    Node, check_if_linked_list_is_palindrome_not_using_previous_node, \
    check_if_linked_list_is_palindrome_using_previous_node


class Test(TestCase):
    def test_check_if_linked_list_is_palindrome_using_previous_node__when_list_is_empty__then_result_is_false(self):
        self.assertFalse(check_if_linked_list_is_palindrome_using_previous_node(None))

    def test_check_if_linked_list_is_palindrome_using_previous_node__when_list_contains_only_1_node__then_result_is_true(
            self):
        self.assertTrue(check_if_linked_list_is_palindrome_using_previous_node(Node('a')))

    def test_check_if_linked_list_is_palindrome_using_previous_node__when_list_is_palindrome_and_its_length_is_even_number__then_result_is_true(
            self):
        head: Node = self.create_linked_list(['a', 'b', 'b', 'a'])
        self.assertTrue(check_if_linked_list_is_palindrome_using_previous_node(head))

    def test_check_if_linked_list_is_palindrome_using_previous_node__when_list_is_palindrome_and_its_length_is_odd_number__then_result_is_true(
            self):
        head: Node = self.create_linked_list(['a', 'b', 'c', 'b', 'a'])
        self.assertTrue(check_if_linked_list_is_palindrome_using_previous_node(head))

    def test_check_if_linked_list_is_palindrome_using_previous_node__when_list_is_not_palindrome__then_result_is_false(
            self):
        head: Node = self.create_linked_list(['a', 'b', 'c', 'a'])
        self.assertFalse(check_if_linked_list_is_palindrome_using_previous_node(head))

    def test_check_if_linked_list_is_palindrome_not_using_previous_node__when_list_is_empty__then_result_is_false(self):
        self.assertFalse(check_if_linked_list_is_palindrome_not_using_previous_node(None))

    def test_check_if_linked_list_is_palindrome_not_using_previous_node__when_list_contains_only_1_node__then_result_is_true(
            self):
        self.assertTrue(check_if_linked_list_is_palindrome_not_using_previous_node(Node('a')))

    def test_check_if_linked_list_is_palindrome_not_using_previous_node__when_list_is_palindrome_and_its_length_is_even_number__then_result_is_true(
            self):
        head: Node = self.create_linked_list(['a', 'b', 'b', 'a'])
        self.assertTrue(check_if_linked_list_is_palindrome_not_using_previous_node(head))

    def test_check_if_linked_list_is_palindrome_not_using_previous_node__when_list_is_palindrome_and_its_length_is_odd_number__then_result_is_true(
            self):
        head: Node = self.create_linked_list(['a', 'b', 'c', 'b', 'a'])
        self.assertTrue(check_if_linked_list_is_palindrome_not_using_previous_node(head))

    def test_check_if_linked_list_is_palindrome_not_using_previous_node__when_list_is_not_palindrome__then_result_is_false(
            self):
        head: Node = self.create_linked_list(['a', 'b', 'c', 'a'])
        self.assertFalse(check_if_linked_list_is_palindrome_not_using_previous_node(head))

    @staticmethod
    def create_linked_list(elements: List[object]) -> Optional[Node]:
        head: Optional[Node] = None
        previous: Optional[Node] = None
        for element in elements:
            current: Node = Node(element)
            if previous is not None:
                previous.next = current
                current.previous = previous
            if head is None:
                head = current
            previous = current
        return head
