import unittest
from tree import Tree


class TestTree(unittest.TestCase):
    def test_find(self):
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)
        self.assertEqual(tree.find(3).data, 3)
        self.assertEqual(tree.find(4).data, 4)
        self.assertEqual(tree.find(0).data, 0)
        self.assertEqual(tree.find(8).data, 8)
        self.assertEqual(tree.find(2).data, 2)

    def test_find_not_found(self):
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)
        self.assertEqual(tree.find(5), None)
        self.assertEqual(tree.find(1), None)
        self.assertEqual(tree.find(9), None)
        self.assertEqual(tree.find(10), None)
        self.assertEqual(tree.find(11), None)
