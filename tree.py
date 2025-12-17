import node
import random
import time

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

    def createMultipleRandomNodes(self, numOfNodes):
        existingNodes = []
        randNum = random.randint(1, numOfNodes) 
        self.root = self.__addNode(myTree.root, randNum) # initialises the tree 

        for i in range(numOfNodes - 1):
            randNum = random.randint(1, numOfNodes)
            if randNum in existingNodes: continue # avoids duplicating numbers

            existingNodes.append(randNum)
            self.__addNode(self.root, randNum)

    def __findLongestPath(self, currentNode):
        if currentNode == None:
            return -1   

        leftDepth = self.__findLongestPath(currentNode.left)

        rightDepth = self.__findLongestPath(currentNode.right)

        depth = 1 + max(leftDepth, rightDepth)

        return depth

    def printLongestPath(self):
        print("\nThe longest path in this tree is:", self.__findLongestPath(self.root))

    def run(self):
        start = time.time()

        nodeCreationStart = time.time()
        self.createMultipleRandomNodes(50000)
        nodeCreationEnd = time.time()

        self.__prettyPrint(self.root)

        nodeFindStart = time.time()
        self.printLongestPath()
        nodeFindEnd = time.time()

        end = time.time()

        print(f"\nTree creation time: {round(nodeCreationEnd - nodeCreationStart, 5)}ms")
        print(f"\nLongest path location time: {round(nodeFindEnd - nodeFindStart, 5)}ms")
        print(f"\nTotal execution time: {round(end - start, 5)}ms")
        
    # Adapted from https://www.theodinproject.com/lessons/javascript-binary-search-trees#assignment
    def __prettyPrint(self, node, prefix = "", isLeft = True):
        if node == None:
            return
    
        if node.right != None:
            string = "|   " if isLeft else "    "
            self.__prettyPrint(node.right, f"{prefix}{string}", False)

        otherString = "└── " if isLeft else "┌── "
        
        print(f"{prefix}{otherString}{node.data}");

        if node.left != None:
            string = "    " if isLeft else "│   "
            self.__prettyPrint(node.left, f"{prefix}{string}", True)
   
if __name__ == "__main__": 
    myTree = Tree()
    myTree.run()