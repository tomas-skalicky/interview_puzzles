from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.invert_binary_tree import Node, invert_binary_tree


class Test(TestCase):
    def test_invert_binary_tree__when_tree_is_valid__then_tree_is_inverted(self):
        root_node: Node = Node('a')
        root_node.left = Node('b')
        root_node.right = Node('c')
        root_node.left.left = Node('d')
        root_node.left.right = Node('e')
        root_node.right.left = Node('f')
        self.assertEqual('a b d e c f ', root_node.preorder())
        invert_binary_tree(root_node)
        self.assertEqual('a c f b e d ', root_node.preorder())
