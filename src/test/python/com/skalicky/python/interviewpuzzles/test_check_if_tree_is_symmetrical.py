from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.check_if_tree_is_symmetrical import \
    Node, check_if_tree_is_symmetrical


class Test(TestCase):
    def test_check_if_tree_is_symmetrical__when_root_is_none__then_tree_is_symmetrical(self):
        self.assertTrue(check_if_tree_is_symmetrical(None))

    def test_check_if_tree_is_symmetrical__when_tree_contains_only_1_node__then_tree_is_symmetrical(self):
        self.assertTrue(check_if_tree_is_symmetrical(Node(4)))

    def test_check_if_tree_is_symmetrical__when_root_has_1_child__then_tree_is_asymmetrical(self):
        root_node: Node = Node(4, tuple([Node(3)]))
        self.assertFalse(check_if_tree_is_symmetrical(root_node))

    def test_check_if_tree_is_symmetrical__when_root_has_2_children_with_different_values__then_tree_is_asymmetrical(
            self):
        root_node: Node = Node(4, (Node(3), Node(2)))
        self.assertFalse(check_if_tree_is_symmetrical(root_node))

    def test_check_if_tree_is_symmetrical__when_root_has_2_children_with_same_value_and_these_children_have_symmetrical_children__then_tree_is_symmetrical(
            self):
        left_child: Node = Node(3, (Node(9), Node(4), Node(1)))
        right_child: Node = Node(3, (Node(1), Node(4), Node(9)))
        root_node: Node = Node(4, (left_child, right_child))
        self.assertTrue(check_if_tree_is_symmetrical(root_node))

    def test_check_if_tree_is_symmetrical__when_tree_is_symmetrical_and_has_more_than_one_levels__then_result_is_true(
            self):
        first_child_of_second_root_child: Node = Node(2, tuple([Node(33)]))
        second_child_of_third_root_child: Node = Node(2, tuple([Node(33)]))

        first_root_child: Node = Node(3, (Node(9), Node(4), Node(1)))
        second_root_child: Node = Node(4, (first_child_of_second_root_child, Node(4)))
        third_root_child: Node = Node(4, (Node(4), second_child_of_third_root_child))
        forth_root_child: Node = Node(3, (Node(1), Node(4), Node(9)))

        root_node: Node = Node(4, (first_root_child, second_root_child, third_root_child, forth_root_child))
        self.assertTrue(check_if_tree_is_symmetrical(root_node))

    def test_check_if_tree_is_symmetrical__when_root_children_have_different_number_of_children__then_tree_is_asymmetrical(
            self):
        left_child: Node = Node(3, (Node(9), Node(4)))
        right_child: Node = Node(3, (Node(1), Node(4), Node(9)))
        root_node: Node = Node(4, (left_child, right_child))
        self.assertFalse(check_if_tree_is_symmetrical(root_node))
