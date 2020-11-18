from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_common_ancestor_in_binary_tree import TreeNode, \
    find_common_ancestor_in_binary_tree


class Test(TestCase):
    def test_find_common_ancestor_in_binary_tree__when_common_ancestor_is_parent__then_parent_is_returned(self):
        root_node: TreeNode = self.create_binary_tree()
        self.assertEqual(root_node.right,
                         find_common_ancestor_in_binary_tree(root_node.right.left, root_node.right.right))

    def test_find_common_ancestor_in_binary_tree__when_common_ancestor_is_root__then_root_is_returned(self):
        root_node: TreeNode = self.create_binary_tree()
        self.assertEqual(root_node,
                         find_common_ancestor_in_binary_tree(root_node.left, root_node.right.right))

    def test_find_common_ancestor_in_binary_tree__when_common_ancestor_is_one_of_input_nodes__then_right_one_is_returned(
            self):
        root_node: TreeNode = self.create_binary_tree()
        self.assertEqual(root_node.right,
                         find_common_ancestor_in_binary_tree(root_node.right, root_node.right.right))

    def test_find_common_ancestor_in_binary_tree__when_there_is_no_common_ancestor__then_none_is_returned(
            self):
        root_node: TreeNode = self.create_binary_tree()
        self.assertIsNone(find_common_ancestor_in_binary_tree(root_node.right, TreeNode('f')))

    @staticmethod
    def create_binary_tree() -> TreeNode:
        #   a
        #  / \
        # b   c
        #    / \
        #   d*  e*
        root_node: TreeNode = TreeNode('a')
        root_node.left = TreeNode('b')
        root_node.left.parent = root_node
        root_node.right = TreeNode('c')
        root_node.right.parent = root_node
        root_node.right.left = TreeNode('d')
        root_node.right.left.parent = root_node.right
        root_node.right.right = TreeNode('e')
        root_node.right.right.parent = root_node.right
        return root_node
