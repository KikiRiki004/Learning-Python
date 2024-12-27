class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):
    # if binary search tree is empty, create a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root


def search(root, value):
    # node is empty
    if root is None:
        return False
    # if element is equal to the element to be searched
    elif root.data == value:
        return True
    # element to be searched is less than the current node
    elif root.data > value:
        return search(root.leftChild, value)
    # element to be searched is greater than the current node
    else:
        return search(root.rightChild, value)


root = insert(None, 50)
insert(root, 20)
insert(root, 53)
insert(root, 11)
insert(root, 22)
insert(root, 52)
insert(root, 78)
print("53 is present in the binary tree:", search(root, 53))
print("100 is present in the binary tree:", search(root, 100))