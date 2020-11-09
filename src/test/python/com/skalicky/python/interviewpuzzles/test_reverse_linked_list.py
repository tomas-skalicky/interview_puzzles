from typing import Tuple
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.reverse_linked_list import ListNode


class TestListNode(TestCase):
    def test_reverse_linked_list_iteratively__when_input_list_is_non_empty__then_output_list_is_reversed(self):
        initial_head_node, initial_tail_node = create_linked_list_4_3_2_1_0()
        self.assertEqual('4 3 2 1 0 ', initial_head_node.serialize_to_string())
        initial_head_node.reverse_linked_list_iteratively()
        self.assertEqual('0 1 2 3 4 ', initial_tail_node.serialize_to_string())

    def test_reverse_linked_list_recursively__when_input_list_is_non_empty__then_output_list_is_reversed(self):
        initial_head_node, initial_tail_node = create_linked_list_4_3_2_1_0()
        self.assertEqual('4 3 2 1 0 ', initial_head_node.serialize_to_string())
        initial_head_node.reverse_linked_list_recursively()
        self.assertEqual('0 1 2 3 4 ', initial_tail_node.serialize_to_string())


def create_linked_list_4_3_2_1_0() -> Tuple[ListNode, ListNode]:
    node4 = ListNode(4)
    node3 = ListNode(3)
    node4.next = node3
    node2 = ListNode(2)
    node3.next = node2
    node1 = ListNode(1)
    node2.next = node1
    node0 = ListNode(0)
    node1.next = node0
    return node4, node0
