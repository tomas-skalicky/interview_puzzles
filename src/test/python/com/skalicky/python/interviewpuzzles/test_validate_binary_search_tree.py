from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.validate_binary_search_tree import is_bst, TreeNode


class Test(TestCase):
    def test_is_bst__when_tree_is_valid_binary_search_tree__then_true(self):
        root_node: TreeNode = TreeNode(5)
        root_node.left = TreeNode(3)
        root_node.right = TreeNode(7)
        root_node.left.left = TreeNode(1)
        root_node.left.right = TreeNode(4)
        root_node.right.left = TreeNode(6)
        #     5
        #    / \
        #   3   7
        #  / \ /
        # 1  4 6
        self.assertTrue(is_bst(root_node))

    def test_is_bst__when_tree_is_invalid_binary_search_tree__then_false(self):
        root_node: TreeNode = TreeNode(5)
        root_node.left = TreeNode(3)
        root_node.right = TreeNode(7)
        root_node.left.left = TreeNode(1)
        root_node.left.right = TreeNode(6)
        #     5
        #    / \
        #   3   7
        #  / \
        # 1  6
        self.assertFalse(is_bst(root_node))
