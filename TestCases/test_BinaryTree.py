
import unittest

# test_binary_tree.py

import unittest
from ProgrammeFiles.BinaryTree import BinaryTree

class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.bt = BinaryTree()
        for val in [50, 30, 70, 20, 40, 60, 80]:
            self.bt.insert(val)

    def test_inorder(self):
        self.assertEqual(self.bt.inorder(), [20, 30, 40, 50, 60, 70, 80])

    def test_preorder(self):
        self.assertEqual(self.bt.preorder(), [50, 30, 20, 40, 70, 60, 80])

    def test_postorder(self):
        self.assertEqual(self.bt.postorder(), [20, 40, 30, 60, 80, 70, 50])

    def test_search_true(self):
        self.assertTrue(self.bt.search(70))
        self.assertTrue(self.bt.search(20))

    def test_search_false(self):
        self.assertFalse(self.bt.search(100))

    def test_height(self):
        self.assertEqual(self.bt.Height(), 3)

    def test_delete_leaf(self):
        self.bt.delete_node(20)
        self.assertEqual(self.bt.inorder(), [30, 40, 50, 60, 70, 80])
        self.assertFalse(self.bt.search(20))

    def test_delete_node_with_one_child(self):
        self.bt.delete_node(30)
        self.assertEqual(self.bt.inorder(), [20, 40, 50, 60, 70, 80])
        self.assertFalse(self.bt.search(30))

    def test_delete_node_with_two_children(self):
        self.bt.delete_node(50)
        self.assertFalse(self.bt.search(50))
        self.assertEqual(self.bt.inorder(), [20, 30, 40, 60, 70, 80])

    def test_min_value(self):
        min_node = self.bt.min_currentVal(self.bt.root)
        self.assertEqual(min_node.val, 20)


if __name__ == '__main__':
    unittest.main()
