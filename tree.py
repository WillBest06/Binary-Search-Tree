import node

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, currentNode, newNodeData):
        newNode = node.Node(newNodeData)

        # IF TREE IS EMPTY THEN FIRST ADDITION MUST BE ASSIGNED TO ROOT
        # E.G. myTree.root = myTree.addNode(myTree.root, 1)
        if currentNode == None:
            return newNode  

        if newNodeData > currentNode.data:
            currentNode.right = self.addNode(currentNode.right, newNodeData)
        elif newNodeData <= currentNode.data:
            currentNode.left = self.addNode(currentNode.left, newNodeData)

        return currentNode

myTree = Tree()
myTree.root = myTree.addNode(myTree.root, 1)
myTree.addNode(myTree.root, 2)
myTree.addNode(myTree.root, 3)