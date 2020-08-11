class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class NodeMgt:
    def __init__(self, head):
        self.head = head

    def insert(self, data):
        self.currentNode = self.head
        while True:
            if data < self.currentNode.data:
                if self.currentNode.left != None:
                    self.currentNode = self.currentNode.left
                else:
                    self.currentNode.left = Node(data)
                    break
            if data > self.currentNode.data:
                if self.currentNode.right != None:
                    self.currentNode = self.currentNode.right
                else:
                    self.currentNode.right = Node(data)
                    break
    def search(self, data):
        self.currentNode = self.head
        while self.currentNode:
            if data == self.currentNode.data:
                return True
            elif data < self.currentNode.data:
                self.currentNode = self.currentNode.left
            elif data > self.currentNode.data:
                self.currentNode = self.currentNode.right
        return False

myBinarySearchTree = NodeMgt(Node(10))
myBinarySearchTree.insert(20)
print(myBinarySearchTree.search(110))

