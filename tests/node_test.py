import unittest
from src.node import Node

class NodeTests(unittest.TestCase):
    def test_node_init(self):
        testNode = Node()
        self.assertEqual(testNode.data, None)
        self.assertEqual(testNode.left, None)
        self.assertEqual(testNode.right, None)

    def test_node_data_change(self):
        testNode = Node()
        testNode.data = 1
        self.assertEqual(testNode.data, 1)

    def test_node_pointer_access_for_empty_pointer(self):
        testNode = Node()
        leftVal = testNode.left
        self.assertRaises(AttributeError, leftVal.data)

if __name__ == '__main__':
    unittest.main()