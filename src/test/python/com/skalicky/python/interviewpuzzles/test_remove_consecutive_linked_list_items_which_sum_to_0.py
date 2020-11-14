from typing import Optional
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.remove_consecutive_linked_list_items_which_sum_to_0 import \
    Node, remove_consecutive_linked_list_items_which_sum_to_0


class Test(TestCase):
    def test_remove_consecutive_linked_list_items_which_sum_to_0__when_list_contains_only_1_node_holding_0__then_result_is_no_list(
            self):
        head_node: Node = Node(0)
        self.assertIsNone(remove_consecutive_linked_list_items_which_sum_to_0(head_node))

    def test_remove_consecutive_linked_list_items_which_sum_to_0__when_list_contains_only_2_nodes_summing_to_0__then_result_is_no_list(
            self):
        head_node: Node = Node(-10)
        head_node.next = Node(10)
        self.assertIsNone(remove_consecutive_linked_list_items_which_sum_to_0(head_node))

    def test_remove_consecutive_linked_list_items_which_sum_to_0__when_list_contains_1_node_holding_0_and_one_holding_non_zero__then_result_is_list_with_latter(
            self):
        head_node: Node = Node(0)
        head_node.next = Node(10)
        self.assertEqual('10', self.serialize_linked_list_in_string(
            remove_consecutive_linked_list_items_which_sum_to_0(head_node)))

    def test_remove_consecutive_linked_list_items_which_sum_to_0__when_list_contains_2_consecutive_nodes_not_summing_to_0__then_result_contains_both_nodes(
            self):
        head_node = Node(-10)
        head_node.next = Node(10)
        head_node.next.next = Node(-3)
        head_node.next.next.next = Node(-3)
        self.assertEqual('-3 -> -3', self.serialize_linked_list_in_string(
            remove_consecutive_linked_list_items_which_sum_to_0(head_node)))

    def test_remove_consecutive_linked_list_items_which_sum_to_0__when_list_contains_more_than_2_consecutive_nodes_summing_to_0__then_result_does_not_contain_these_nodes(
            self):
        head_node = Node(10)
        head_node.next = Node(5)
        head_node.next.next = Node(-3)
        head_node.next.next.next = Node(-3)
        head_node.next.next.next.next = Node(1)
        head_node.next.next.next.next.next = Node(4)
        head_node.next.next.next.next.next.next = Node(-4)
        self.assertEqual('10', self.serialize_linked_list_in_string(
            remove_consecutive_linked_list_items_which_sum_to_0(head_node)))

    @staticmethod
    def serialize_linked_list_in_string(list_head_node: Optional[Node]) -> str:
        if list_head_node is None:
            return 'None'
        else:
            result_string: str = ''
            current_node: Node = list_head_node
            while current_node is not None:
                if current_node != list_head_node:
                    result_string += ' -> '
                result_string += str(current_node.value)
                current_node = current_node.next
            return result_string
