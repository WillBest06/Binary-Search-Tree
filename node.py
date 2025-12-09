class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def editData(self, data):
        self.data = data

    def editLeftPointer(self, newPointer):
        self.left = newPointer

    def editRightPointer(self, newPointer):
        self.right = newPointer