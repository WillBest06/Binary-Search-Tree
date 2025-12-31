import unittest
from src.tree import Tree

class TreeTests(unittest.TestCase):
    def test_tree_init(self):
        testTree = Tree()
        self.assertEqual(testTree.root, None)

    def test_tree_creation_5000_nodes(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(5000)

        self.assertEqual(testTree.getNumOfNodes(testTree.root), 5000)

    def test_search_for_value_in_tree(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(5000)

        self.assertEqual(testTree.findNode(testTree.root, 2500), (2500, "is present in this tree"))

    def test_search_for_value_not_in_tree(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(5000)

        self.assertEqual(testTree.findNode(testTree.root, 5001), (5001, "is not present in this tree"))


# write about how tricky it is to test this one since it will be random each time
# also hard to test output to console
    def test_get_tree_longest_path(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(2)

        self.assertEqual(testTree.printLongestPath(), (5001, "is not present in this tree"))

if __name__ == '__main__':
    unittest.main()