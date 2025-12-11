import node
import random

class Tree:
    def __init__(self):
        self.root = None

    def __addNode(self, currentNode, newNodeData):
        newNode = node.Node(newNodeData)

        # IF TREE IS EMPTY THEN FIRST ADDITION MUST BE ASSIGNED TO ROOT
        # E.G. myTree.root = myTree.addNode(myTree.root, 1)
        if currentNode == None:
            return newNode  

        if newNodeData > currentNode.data:
            currentNode.right = self.__addNode(currentNode.right, newNodeData)
        elif newNodeData <= currentNode.data:
            currentNode.left = self.__addNode(currentNode.left, newNodeData)

        return currentNode

    def findNode(self, currentNode, searchValue):
        if currentNode == None:
            return searchValue, "is not present in this tree"

        if currentNode.data == searchValue:
            return searchValue, "is present in this tree"

        if searchValue > currentNode.data:
            return self.findNode(currentNode.right, searchValue)
        elif searchValue <= currentNode.data:
            return self.findNode(currentNode.left, searchValue)

    def create5000Nodes(self):
        randNum = random.randint(1, 5000)
        self.root = self.__addNode(myTree.root, randNum)

        for i in range(4999):
            randNum = random.randint(1, 5000)
            self.__addNode(self.root, randNum)

    def __findLongestPath(self, currentNode):
        if currentNode == None:
            return -1   

        leftDepth = self.__findLongestPath(currentNode.left)

        rightDepth = self.__findLongestPath(currentNode.right)

        depth = 1 + max(leftDepth, rightDepth)

        return depth

    def printLongestPath(self):
        print("The longest path in this tree is:", self.__findLongestPath(self.root))

myTree = Tree()
myTree.create5000Nodes()
myTree.printLongestPath()