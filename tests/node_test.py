import unittest
from src.node import Node

class NodeTests(unittest.TestCase):
    def test_node_init(self):
        testNode = Node()
        self.assertEqual(testNode.data, None)
        self.assertEqual(testNode.left, None)
        self.assertEqual(testNode.right, None)
        
    def test_node_init_with_params(self):
        leftChild = Node(1)
        rightChild = Node(3)
        parent = Node(2, leftChild, rightChild)

        self.assertEqual(parent.data, 2)
        self.assertIs(parent.left, leftChild)
        self.assertIs(parent.right, rightChild)

    def test_node_data_change(self):
        testNode = Node()
        testNode.data = 1
        self.assertEqual(testNode.data, 1)

if __name__ == '__main__':
    unittest.main()