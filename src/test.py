import unittest
from BinarySearchTree import BinarySearchTree, Node

class TestCases(unittest.TestCase):
    def test(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        self.assertTrue(bst.search(5))
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(7))
        self.assertFalse(bst.search(10))
    def test2(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.delete(3)
        self.assertFalse(bst.search(3))
        self.assertTrue(bst.search(5))
    def test3(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        self.assertEqual(bst.inorder(), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()