import unittest
from src.tree import Tree

class TreeTests(unittest.TestCase):
    def test_tree_init(self):
        testTree = Tree()
        self.assertEqual(testTree.root, None)

    # predefined tree creation
    def test_predefined_tree_creation(self):
        testTree = Tree()

        # initialises the root node
        testTree.root = testTree.addNode(testTree.root, 50)

        for i in [25, 75, 0, 100]:
            testTree.addNode(testTree.root, i)

        self.assertEqual(testTree.getNumOfNodes(testTree.root), 5)

    def test_predefined_tree_creation_with_invalid_starter_node_param(self):
        testTree = Tree()

        with self.assertRaises(TypeError):
            testTree.root = testTree.addNode("not a node", 50)

    # random tree creation 
    def test_tree_creation_5000_random_nodes(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(5000)

        self.assertEqual(testTree.getNumOfNodes(testTree.root), 5000)

    def test_tree_creation_0_nodes(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(0)

        self.assertEqual(testTree.getNumOfNodes(testTree.root), 0)

    def test_tree_creation_negative_5000_nodes(self):
        testTree = Tree()
        
        with self.assertRaises(TypeError):
            testTree.createMultipleRandomNodes(-5000)
            self.assertEqual(testTree.getNumOfNodes(), 0)

    def test_tree_creation_5000_and_a_half_nodes(self):
        testTree = Tree()
        
        with self.assertRaises(TypeError):
            testTree.createMultipleRandomNodes(5000.5)
            self.assertEqual(testTree.getNumOfNodes(), 0)

    #  find nodes
    def test_search_for_value_in_tree(self):
        testTree = Tree()

        # initialises the root node
        testTree.root = testTree.addNode(testTree.root, 50)

        for i in [25, 75, 0, 100]:
            testTree.addNode(testTree.root, i)

        self.assertEqual(testTree.findNode(testTree.root, 100), (100, "is present in this tree"))

    def test_search_for_value_not_in_tree(self):
        testTree = Tree()

        # initialises the root node
        testTree.root = testTree.addNode(testTree.root, 50)

        for i in [25, 75, 0, 100]:
            testTree.addNode(testTree.root, i)

        self.assertEqual(testTree.findNode(testTree.root, 1), (1, "is not present in this tree"))

    def test_search_for_invalid_value(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(5000)

        with self.assertRaises(TypeError):
            testTree.findNode(testTree.root, "Invalid string")

    def test_search_with_invalid_starter_node_param(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(5000)

        with self.assertRaises(TypeError):
            testTree.findNode("Not a node", 1)

    # find longest path
    def test_find_tree_longest_path_5_nodes(self):
        testTree = Tree()

        # initialises the root node
        testTree.root = testTree.addNode(testTree.root, 50)

        for i in [25, 75, 0, 100]:
            testTree.addNode(testTree.root, i)

        self.assertEqual(testTree.findLongestPath(testTree.root), 2)

    def test_find_tree_longest_path_1_node(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(1)

        self.assertEqual(testTree.findLongestPath(testTree.root), 0)

    def test_find_tree_longest_path_0_nodes(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(0)

        self.assertEqual(testTree.findLongestPath(testTree.root), -1)

    def test_find_tree_longest_path_with_invalid_node_param(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(5000)

        with self.assertRaises(TypeError):
            testTree.findLongestPath("not a node")

# run mock
    def test_run_mock(self):
        testTree = Tree()
        testTree.createMultipleRandomNodes(5000)
        self.assertEqual(testTree.getNumOfNodes(testTree.root), 5000)

        longestPath = testTree.findLongestPath(testTree.root)
        self.assertEqual(type(longestPath), int)
        self.assertGreaterEqual(longestPath, 0)

if __name__ == '__main__':
    unittest.main()