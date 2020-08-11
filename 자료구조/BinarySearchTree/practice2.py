class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class NodeMgt:

    def __init__(self, head):
        self.head = head

    def insert(self, data):
        currentNode = self.head

        if currentNode == None:
            currentNode = Node(data)

        while True:
            if data < currentNode.data:
                if currentNode.left == None:
                    currentNode.left = Node(data)
                    break
                else:
                    currentNode.left == currentNode
            else:
                if currentNode.right == None:
                    currentNode.right = Node(data)
                    break
                else:
                    currentNode.right == currentNode

    def search(self, data):
        currentNode = self.head
        while currentNode != None:
            if currentNode.data == data:
                return True
            elif currentNode.data > data:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return False

    def delete(self, data):
        currentNode = self.head
        parentNode = self.head
        leftNode = self.head.left
        rightNode = self.head.right








